#!/usr/bin/env python3
"""Repeatable structural course audit; never a legal certification."""
import argparse
import json
import re
from collections import Counter
from pathlib import Path


def audit(root: Path):
    failures = []
    warnings = []
    question_file = root / "podstawowy/questions.jsonl"
    matrix_file = root / "podstawowy/kompetencje.json"
    index_file = root / "review/specialist/REJESTR-0001-0506.md"
    if not question_file.is_file() or not matrix_file.is_file():
        return ["Missing question bank or competency matrix"], []
    questions = [json.loads(x) for x in question_file.read_text(encoding="utf-8").splitlines() if x.strip()]
    matrix = json.loads(matrix_file.read_text(encoding="utf-8"))["competencies"]
    qids = [q["id"] for q in questions]
    qset = set(qids)
    if len(qset) != len(qids):
        failures.append("Duplicate question IDs")
    numbers = [int(x.split("-")[-1]) for x in qids]
    if numbers != list(range(1, len(qids) + 1)):
        failures.append("IDs are not consecutive from ADR-B-0001")
    modules = {f"ADR-B-{n:02d}" for n in range(1, 14)}
    if {q["module_id"] for q in questions} != modules:
        failures.append("Question bank does not cover all 13 basic modules")
    if len(matrix) != 106:
        warnings.append(f"Expected 106 internal competencies, found {len(matrix)}")
    theory = [o for o in matrix if o["delivery"] == "theory"]
    practical = [o for o in matrix if o["delivery"] == "practical"]
    if len(theory) != 103 or len(practical) != 3:
        failures.append("Expected 103 theoretical and 3 practical competencies")
    linked = Counter()
    for c in matrix:
        for id in c["question_ids"]:
            linked[id] += 1
            if id not in qset:
                failures.append(f"Dangling competency link: {c['id']} / {id}")
            elif next(x for x in questions if x["id"] == id)["module_id"] != c["module_id"]:
                failures.append(f"Wrong competency module: {c['id']} / {id}")
        if c["delivery"] == "theory" and not c["question_ids"]:
            failures.append(f"Theoretical objective without any question: {c['id']}")
    missing = qset - set(linked)
    if missing:
        failures.append("Unmapped questions: "+", ".join(sorted(missing)[:10]))
    lessons = root / "podstawowy/lekcje"
    for n in range(1, 14):
        ident = f"ADR-B-{n:02d}"
        f = lessons / f"{ident}.md"
        if not f.is_file():
            failures.append(f"Missing lesson {ident}")
            continue
        body = f.read_text(encoding="utf-8")
        if not body.startswith("# ") or ident not in body.splitlines()[0]:
            failures.append(f"Missing lesson identity {ident}")
        if len(body) < 1200 or "2025" not in body:
            failures.append(f"Insufficient lesson text or legal year: {ident}")
    program = root / "docs/PROGRAM-PODSTAWOWY.md"
    if not program.is_file() or "**18**" not in program.read_text(encoding="utf-8"):
        failures.append("Official basic curriculum time table not found")
    practice = root / "podstawowy/praktyka/SCENARIUSZE.md"
    if not practice.is_file():
        failures.append("Missing practical scenarios")
    else:
        body = practice.read_text(encoding="utf-8")
        for code in ("P1", "P2", "P3"):
            if code not in body:
                failures.append(f"Missing practical scenario {code}")
    if not index_file.is_file():
        failures.append("Missing specialist question registry")
    else:
        lines = re.findall(r"^\| (ADR-B-\d{4}) \|",index_file.read_text(encoding="utf-8"),flags=re.M)
        if len(lines)!=len(qids) or set(lines)!=qset:
            failures.append(f"Specialist index differs from bank: index={len(lines)}, bank={len(qids)}")
    approval = root / "review/approvals.jsonl"
    if not approval.is_file():
        failures.append("Missing release approval ledger")
    statuses = Counter(q.get("verification_status") for q in questions)
    if statuses.get("needs_review"):
        warnings.append(f"{statuses['needs_review']} questions are not professionally approved")
    if statuses.get("verified"):
        warnings.append("Any verified questions require real documented independent approvals")
    if approval.is_file() and approval.read_text(encoding="utf-8").strip():
        warnings.append("Review approvals exist: check authenticity and release gate manually")
    if not (root / "scripts/mock_exam.py").is_file():
        failures.append("Missing gated internal mock exam generator")
    return failures, warnings


def main(argv=None):
    ap=argparse.ArgumentParser()
    ap.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args=ap.parse_args(argv)
    failures, warnings = audit(args.root)
    for line in warnings:
        print("PENDING: "+line)
    for line in failures:
        print("FAIL: "+line)
    print("PASS: structural course audit; not legal approval" if not failures else
          f"FAIL: {len(failures)} structural issue(s)")
    return 1 if failures else 0


if __name__=="__main__":
    raise SystemExit(main())
