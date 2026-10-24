#!/usr/bin/env python3
"""Enforce a minimum learner-facing explanation length; this is not legal review."""
import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_PATH = ROOT / "podstawowy" / "questions.jsonl"


def short_explanations(rows, minimum=200):
    return [
        (row.get("id", "<missing-id>"), len((row.get("explanation") or "").strip()))
        for row in rows
        if len((row.get("explanation") or "").strip()) < minimum
    ]


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("--questions", type=Path, default=DEFAULT_PATH)
    parser.add_argument("--minimum", type=int, default=200)
    args = parser.parse_args(argv)
    rows = [
        json.loads(line)
        for line in args.questions.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]
    short = short_explanations(rows, args.minimum)
    print(f"Explanation minimum: {args.minimum} characters; checked {len(rows)} questions.")
    if short:
        print("FAIL: explanations below minimum:")
        for question_id, length in short:
            print(f"  {question_id}: {length} characters")
        return 1
    print("PASS: all explanations meet the minimum length.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
