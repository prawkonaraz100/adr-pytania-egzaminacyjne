#!/usr/bin/env python3
"""Repeatable structural course audit; never a legal certification."""
import argparse
import json
import re
from collections import Counter
from pathlib import Path
import xml.etree.ElementTree as ET



def validate_image_assets(root: Path, questions):
    """Reject missing or unsafe linked SVG art; does not certify ADR symbol accuracy."""
    errors = []
    for record in questions:
        rel_text = record.get("image")
        if rel_text is None:
            continue
        qid = record["id"]
        if not isinstance(rel_text, str):
            errors.append(f"{qid}: non-string SVG path")
            continue
        rel = Path(rel_text)
        if rel.is_absolute() or ".." in rel.parts or len(rel.parts) < 2 or rel.parts[0] != "assets" or rel.suffix.lower() != ".svg":
            errors.append(f"{qid}: unsafe or non-SVG image path")
            continue
        file = root / rel
        if not file.is_file():
            errors.append(f"{qid}: missing SVG asset: {rel_text}")
            continue
        try:
            svg = ET.fromstring(file.read_text(encoding="utf-8"))
        except (ET.ParseError, UnicodeError) as exc:
            errors.append(f"{qid}: malformed SVG: {exc}")
            continue
        tags = [element.tag.rsplit("}", 1)[-1] for element in svg.iter()]
        if tags[0] != "svg":
            errors.append(f"{qid}: image is not SVG")
        if "title" not in tags or "desc" not in tags:
            errors.append(f"{qid}: SVG missing accessible title or description")
        if any(tag in {"script", "foreignObject", "image"} for tag in tags):
            errors.append(f"{qid}: active/embedded content is forbidden in training SVG")
        for element in svg.iter():
            for key, value in element.attrib.items():
                if key.rsplit("}", 1)[-1] == "href" and not value.startswith("#"):
                    errors.append(f"{qid}: external SVG reference is forbidden")
    return errors

def audit(root: Path):
    failures = []
    warnings = []
    question_file = root / "podstawowy/questions.jsonl"
    matrix_file = root / "podstawowy/kompetencje.json"
    index_files = sorted(p for p in (root / "review/specialist").glob("REJESTR-*.md")
                         if not p.name.startswith("REJESTR-AKTUALNY-"))
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
    failures.extend(validate_image_assets(root, questions))
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
    if not index_files:
        failures.append("Missing specialist question registry")
    else:
        indexed_ids = []
        for index_file in index_files:
            indexed_ids.extend(re.findall(r"^\| (ADR-B-\d{4}) \|",
                                          index_file.read_text(encoding="utf-8"), flags=re.M))
        if len(indexed_ids) != len(qids) or set(indexed_ids) != qset:
            failures.append(f"Specialist index differs from bank: index={len(indexed_ids)}, bank={len(qids)}")
    # Current non-archival review handoff must match every question ID, key and SVG path.
    current_files = sorted((root / "review/specialist").glob("REJESTR-AKTUALNY-0001-*.md"))
    if current_files:
        latest = max(current_files, key=lambda p: int(p.stem.rsplit("-", 1)[-1]))
        index_rows = {}
        for line in latest.read_text(encoding="utf-8").splitlines():
            if not re.match(r"^\| ADR-B-\d{4} \|", line):
                continue
            cells = [piece.strip() for piece in line.strip("|").split("|")]
            if len(cells) < 7:
                failures.append("Malformed current reviewer index row")
                continue
            if cells[0] in index_rows:
                failures.append("Duplicate reviewer index row: " + cells[0])
            index_rows[cells[0]] = cells
        if set(index_rows) != qset or len(index_rows) != len(questions):
            failures.append("Current reviewer index does not match current bank")
        else:
            for question in questions:
                cells = index_rows[question["id"]]
                if cells[4] != question["correct_option"]:
                    failures.append("Stale reviewer index answer key: " + question["id"])
                if cells[6].strip("`") != (question.get("image") or "—"):
                    failures.append("Stale reviewer index image: " + question["id"])
    else:
        warnings.append("Current full reviewer index missing")
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
