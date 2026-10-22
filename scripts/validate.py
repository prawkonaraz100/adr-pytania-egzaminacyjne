#!/usr/bin/env python3
"""ADR podstawowy: walidacja struktury i metadanych JSONL (bez zastępowania recenzji prawnej)."""

import argparse
import datetime as dt
import json
import re
import sys
import unicodedata
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_PATH = ROOT / "podstawowy" / "questions.jsonl"
REQUIRED = {
    "id", "module_id", "stem", "options", "correct_option", "explanation",
    "sources", "legal_basis_version", "verification_status",
    "checked_at", "reviewer", "image",
}
SOURCE_KEYS = {"code", "reference", "url"}
MODULES = {f"ADR-B-{i:02d}" for i in range(1, 14)}
STATUSES = {"draft", "needs_review", "verified", "blocked"}


def clean(text):
    return " ".join(unicodedata.normalize("NFKC", text).casefold().split())


def validate_record(record, seen_ids=None, seen_stems=None):
    errors = []
    if not isinstance(record, dict):
        return ["rekord nie jest obiektem JSON"]
    absent = REQUIRED - set(record)
    extra = set(record) - REQUIRED
    if absent:
        errors.append("brakuje pól: " + ", ".join(sorted(absent)))
    if extra:
        errors.append("niedozwolone pola: " + ", ".join(sorted(extra)))

    qid = record.get("id")
    if not isinstance(qid, str) or not re.fullmatch(r"ADR-B-[0-9]{4}", qid):
        errors.append("id: oczekiwano ADR-B-0001")
    elif seen_ids is not None:
        if qid in seen_ids:
            errors.append("zduplikowane id: " + qid)
        seen_ids.add(qid)

    if not isinstance(record.get("module_id"), str) or record.get("module_id") not in MODULES:
        errors.append("module_id spoza zakresu ADR-B-01 ... ADR-B-13")

    stem = record.get("stem")
    if not isinstance(stem, str) or len(stem.strip()) < 12:
        errors.append("stem: pytanie zbyt krótkie")
    elif seen_stems is not None:
        normalized = clean(stem)
        if normalized in seen_stems:
            errors.append("duplikat treści pytania")
        seen_stems.add(normalized)

    options = record.get("options")
    if not isinstance(options, dict) or set(options) != {"A", "B", "C"}:
        errors.append("options: wymagane dokładnie A, B, C")
    else:
        vals = list(options.values())
        if any(not isinstance(v, str) or not v.strip() for v in vals):
            errors.append("options: odpowiedzi muszą być niepustymi napisami")
        elif len({clean(v) for v in vals}) != 3:
            errors.append("options: odpowiedzi nie mogą się powtarzać")

    if record.get("correct_option") not in {"A", "B", "C"}:
        errors.append("correct_option: tylko A, B albo C")

    explanation = record.get("explanation")
    if not isinstance(explanation, str) or len(explanation.strip()) < 25:
        errors.append("explanation: co najmniej 25 znaków")

    sources = record.get("sources")
    if not isinstance(sources, list) or not sources:
        errors.append("sources: wymagany co najmniej jeden odnośnik")
    else:
        for i, source in enumerate(sources, 1):
            if not isinstance(source, dict) or set(source) != SOURCE_KEYS:
                errors.append(f"sources[{i}]: pola code, reference, url")
                continue
            for k in ("code", "reference"):
                if not isinstance(source[k], str) or len(source[k].strip()) < (3 if k == "reference" else 1):
                    errors.append(f"sources[{i}].{k}: brak konkretnego wskazania")
            if not isinstance(source["url"], str) or not source["url"].startswith("https://"):
                errors.append(f"sources[{i}].url: wymagany adres https")

    v = record.get("legal_basis_version")
    if not isinstance(v, str) or len(v.strip()) < 4:
        errors.append("legal_basis_version: brak wersji przepisów")

    status = record.get("verification_status")
    if not isinstance(status, str) or status not in STATUSES:
        errors.append("verification_status: niepoprawny status")

    checked = record.get("checked_at")
    if checked is not None:
        if not isinstance(checked, str):
            errors.append("checked_at: data YYYY-MM-DD albo null")
        else:
            try:
                d = dt.date.fromisoformat(checked)
                if d.isoformat() != checked or d > dt.date.today():
                    errors.append("checked_at: data niepoprawna lub przyszła")
            except ValueError:
                errors.append("checked_at: data YYYY-MM-DD")
    reviewer = record.get("reviewer")
    if reviewer is not None and (not isinstance(reviewer, str) or len(reviewer.strip()) < 2):
        errors.append("reviewer: nazwa recenzenta albo null")
    if status == "verified" and (checked is None or reviewer is None):
        errors.append("verified wymaga checked_at i reviewer")

    image = record.get("image")
    if image is not None:
        if not isinstance(image, str) or not image.startswith("assets/") or ".." in Path(image).parts:
            errors.append("image: tylko bezpieczna ścieżka assets/...")
    return errors


def validate_file(path, release=False):
    seen_ids, seen_stems = set(), set()
    counts = Counter()
    modules = set()
    errors = []
    with open(path, encoding="utf-8") as handle:
        for line_no, raw in enumerate(handle, 1):
            if not raw.strip():
                continue
            try:
                record = json.loads(raw)
            except json.JSONDecodeError as exc:
                errors.append(f"linia {line_no}: błędny JSON ({exc.msg})")
                continue
            for msg in validate_record(record, seen_ids, seen_stems):
                errors.append(f"linia {line_no}: {msg}")
            if isinstance(record, dict):
                status = record.get("verification_status")
                counts[status if isinstance(status, str) else "unknown"] += 1
                if record.get("verification_status") == "verified":
                    module_id = record.get("module_id")
                    if isinstance(module_id, str):
                        modules.add(module_id)
    if release:
        if counts["verified"] < 30:
            errors.append("release: wymagane co najmniej 30 verified")
        if modules != MODULES:
            errors.append("release: niepokryte moduły: " + ", ".join(sorted(MODULES - modules)))
        if sum(v for k, v in counts.items() if k != "verified"):
            errors.append("release: plik może zawierać tylko rekordy verified")
    return errors, counts


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("--path", type=Path, default=DEFAULT_PATH)
    parser.add_argument("--release", action="store_true",
                        help="Oprócz struktury wymaga minimalnego pokrycia i samych verified.")
    args = parser.parse_args(argv)
    if not args.path.is_file():
        print(f"FAIL: nie znaleziono pliku {args.path}", file=sys.stderr)
        return 1
    errors, counts = validate_file(args.path, release=args.release)
    print("Pytania: " + str(sum(counts.values())) + " | " +
          ", ".join(f"{k}: {v}" for k, v in sorted(counts.items())))
    for err in errors:
        print("FAIL: " + err, file=sys.stderr)
    print("PASS: kontrola struktury" if not errors else f"FAIL: {len(errors)} błędów")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
