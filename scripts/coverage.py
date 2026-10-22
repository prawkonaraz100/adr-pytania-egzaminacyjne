#!/usr/bin/env python3
"""ADR podstawowy: pokrycie kompetencji. Obecność pytania NIE oznacza recenzji prawnej."""

import argparse
import json
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def analyse(questions, curriculum, release=False):
    errors = []
    modules = {f"ADR-B-{n:02}" for n in range(1, 14)}
    qids = {}
    for i, q in enumerate(questions, 1):
        if not isinstance(q, dict) or not isinstance(q.get("id"), str):
            errors.append(f"pytanie {i}: nieprawidłowy identyfikator")
            continue
        if q["id"] in qids:
            errors.append(f"pytanie {i}: powtórzone ID {q['id']}")
        qids[q["id"]] = q

    objectives = curriculum.get("competencies", [])
    if not isinstance(objectives, list):
        return ["kompetencje: nieprawidłowy typ listy"], {}
    seen = set()
    referenced = Counter()
    by_module = Counter()
    draft = verified = 0
    practice = 0
    uncovered = []
    gaps = []
    for index, obj in enumerate(objectives, 1):
        if not isinstance(obj, dict):
            errors.append(f"kompetencja {index}: nie jest obiektem")
            continue
        oid = obj.get("id")
        m = obj.get("module_id")
        if not isinstance(oid, str) or not re.fullmatch(r"ADR-B-(?:0[1-9]|1[0-3])-K[0-9]{2}", oid):
            errors.append(f"kompetencja {index}: błędne ID")
        if oid in seen:
            errors.append(f"powtórzone ID kompetencji: {oid}")
        seen.add(oid)
        if m not in modules or not isinstance(oid, str) or not oid.startswith(m + "-"):
            errors.append(f"{oid}: moduł poza programem lub niespójny")
            continue
        refs = obj.get("legal_refs")
        if not isinstance(refs, str) or not refs.strip():
            errors.append(f"{oid}: brak podstawy do kontroli")
        if not isinstance(obj.get("objective"), str) or len(obj["objective"]) < 8:
            errors.append(f"{oid}: nieopisany cel nauki")
        kind = obj.get("delivery")
        if kind not in ("theory", "practical"):
            errors.append(f"{oid}: delivery musi być theory albo practical")
        ids = obj.get("question_ids")
        if not isinstance(ids, list) or not all(isinstance(item, str) for item in ids) or len(ids) != len(set(ids)):
            errors.append(f"{oid}: question_ids nie jest listą unikalnych ID")
            continue
        by_module[m] += 1
        if kind == "practical":
            practice += 1
        else:
            if not ids:
                uncovered.append(oid)
            else:
                draft += 1
        qverified = 0
        for qid in ids:
            if qid not in qids:
                errors.append(f"{oid}: brak pytania {qid}")
                continue
            if qids[qid].get("module_id") != m:
                errors.append(f"{oid}: pytanie {qid} z innego modułu")
            referenced[qid] += 1
            if qids[qid].get("verification_status") == "verified":
                qverified += 1
        if kind == "theory" and qverified:
            verified += 1
        elif kind == "theory":
            gaps.append(oid)
        if release and kind == "practical" and obj.get("review_status") != "verified":
            errors.append(f"release: brak udokumentowanej akceptacji programu ćwiczeń {oid}")
    if set(by_module) != modules:
        errors.append("brakuje modułów: " + ", ".join(sorted(modules - set(by_module))))
    omitted = sorted(set(qids) - set(referenced))
    if omitted:
        errors.append("nieprzypisane pytania: " + ", ".join(omitted))
    if release:
        if gaps:
            errors.append(f"release: {len(gaps)} celów teorii bez verified")
        # Opracowanie materiałów do zajęć praktycznych i ich recenzja nie potwierdzają
        # uczestnictwa kursanta w ćwiczeniach. Ewidencja obecności pozostaje w OSK.
    stats = {
        "questions": len(qids),
        "modules": len(by_module),
        "competencies": len(objectives),
        "theory_competencies": len(objectives) - practice,
        "practical_competencies": practice,
        "draft_question_coverage": draft,
        "verified_question_coverage": verified,
        "theory_without_questions": uncovered,
        "theory_without_verified": gaps,
        "questions_unmapped": omitted,
        "question_statuses": dict(Counter(q.get("verification_status", "unknown") for q in qids.values()))
    }
    return errors, stats


def check_lessons(root):
    """Techniczna obecność i podstawowy szkielet 13 lekcji, bez oceny prawnej."""
    errors = []
    for number in range(1, 14):
        name = f"ADR-B-{number:02d}"
        path = root / "podstawowy" / "lekcje" / f"{name}.md"
        if not path.is_file():
            errors.append(f"brak lekcji: {name}")
            continue
        content = path.read_text(encoding="utf-8")
        if len(content.strip()) < 900:
            errors.append(f"lekcja za krótka: {name}")
        if not content.startswith(f"# {name}"):
            errors.append(f"błędny tytuł lekcji: {name}")
        if "2025" not in content or "źródł" not in content.lower():
            errors.append(f"brak podstaw prawnych w lekcji: {name}")
    return errors


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--questions", type=Path, default=ROOT / "podstawowy/questions.jsonl")
    parser.add_argument("--curriculum", type=Path, default=ROOT / "podstawowy/kompetencje.json")
    parser.add_argument("--release", action="store_true", help="Sprawdza pełne pokrycie, nie zastępuje recenzji.")
    args = parser.parse_args()
    questions = [json.loads(s) for s in args.questions.read_text(encoding="utf-8").splitlines() if s.strip()]
    matrix = json.loads(args.curriculum.read_text(encoding="utf-8"))
    errors, stats = analyse(questions, matrix, release=args.release)
    errors.extend(check_lessons(ROOT))
    for name, value in stats.items():
        if isinstance(value, list) and len(value) > 10:
            print(f"{name}: {len(value)} pozycji; pierwsze: {', '.join(value[:8])} ...")
        else:
            print(f"{name}: {value}")
    for issue in errors:
        print("FAIL: " + issue)
    print("PASS: spójność mapy kompetencji" if not errors else f"FAIL: {len(errors)} błędów")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
