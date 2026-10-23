#!/usr/bin/env python3
"""Internal ADR basic mock-exam builder. Fail closed: never exports needs_review."""
import argparse
import json
import os
import random
import tempfile
from collections import defaultdict
from pathlib import Path

from release_gate import ROOT, eligible, load_jsonl


def draw_exam(records, seed=2025, size=30):
    """Select 30 validated questions, at least one from each of the 13 modules."""
    if size != 30:
        raise ValueError("mock exam requires exactly 30 questions")
    groups = defaultdict(list)
    for row in records:
        groups[row["module_id"]].append(row)
    required = [f"ADR-B-{i:02d}" for i in range(1, 14)]
    if any(not groups[module] for module in required):
        raise ValueError("mock exam lacks an ADR basic module")
    rng = random.Random(seed)
    selected = [rng.choice(groups[module]) for module in required]
    used = {r["id"] for r in selected}
    pool = [r for r in records if r["id"] not in used]
    if len(pool) < size - len(selected):
        raise ValueError("not enough approved distinct questions")
    selected.extend(rng.sample(pool, size - len(selected)))
    rng.shuffle(selected)
    return {
        "type": "ADR_BASIC_MOCK_INTERNAL_ONLY",
        "publication_authorized": False,
        "question_count": size,
        "time_limit_minutes": 60,
        "pass_mark_correct": 20,
        "note": "Internal configurable practice settings; not official exam certification.",
        "seed": seed,
        "questions": [
            {"number": n, "id": q["id"], "module_id": q["module_id"],
             "stem": q["stem"], "options": q["options"]}
            for n, q in enumerate(selected, 1)
        ],
        "answer_key_internal_only": {
            q["id"]: q["correct_option"] for q in selected
        },
    }


def run(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--questions", type=Path, default=ROOT / "podstawowy/questions.jsonl")
    ap.add_argument("--approvals", type=Path, default=ROOT / "review/approvals.jsonl")
    ap.add_argument("--root", type=Path, default=ROOT)
    ap.add_argument("--seed", type=int, default=2025)
    ap.add_argument("--output", type=Path, help="Explicit local-only destination; never publish")
    ap.add_argument("--report", action="store_true", help="Print blockers; never create an exam")
    args = ap.parse_args(argv)
    if args.output is None and not args.report:
        ap.error("Provide --report or --output.")
    try:
        records = load_jsonl(args.questions)
        approvals = load_jsonl(args.approvals)
        approved, blockers = eligible(records, approvals, args.root, minimum=30)
    except (ValueError, TypeError, KeyError) as e:
        print(f"BLOCKED: {e}")
        return 0 if args.report else 1
    if blockers:
        print(f"BLOCKED: mock exam requires approved questions (approved={len(approved)})")
        for reason in blockers[:15]:
            print(" - " + reason)
        return 0 if args.report else 1
    if args.report:
        print(f"READY FOR INTERNAL EXAM (no output): {len(approved)} approved")
        return 0
    try:
        exam = draw_exam(approved, args.seed)
    except ValueError as e:
        print(f"BLOCKED: {e}")
        return 1
    args.output.parent.mkdir(parents=True, exist_ok=True)
    name = None
    try:
        with tempfile.NamedTemporaryFile("w", dir=args.output.parent,
                                         encoding="utf-8", delete=False) as h:
            name = h.name
            json.dump(exam, h, ensure_ascii=False, indent=2)
            h.write("\n")
        os.replace(name, args.output)
    finally:
        if name and os.path.exists(name):
            os.unlink(name)
    print(f"INTERNAL MOCK EXAM CREATED: {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(run())
