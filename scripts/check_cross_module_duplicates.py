#!/usr/bin/env python3
"""Block identical or near-identical questions assigned to different ADR modules.

This is an editorial integrity check, not a semantic/legal correctness verdict.
"""
import argparse
import json
import re
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_PATH = ROOT / "podstawowy" / "questions.jsonl"
LETTERS = "ABC"
STOP = {
    "jakie", "jaki", "ktora", "ktore", "ktory", "przy", "podczas", "zgodnie",
    "przewozu", "przewoz", "przed", "nalezy", "powinien", "powinna", "towaru",
    "towarow", "niebezpiecznych", "jesli", "jezeli", "przez", "mozna", "jest",
    "oraz", "tylko", "ktorych", "jak", "czy", "sie", "tym", "tego",
}


def normalize(text):
    text = unicodedata.normalize("NFKD", str(text or "").casefold())
    text = "".join(ch for ch in text if not unicodedata.combining(ch))
    return re.sub(r"[^a-z0-9]+", " ", text).strip()


def tokens(text):
    return {word for word in normalize(text).split()
            if len(word) >= 4 and word not in STOP}


def jaccard(left, right):
    union = left | right
    return len(left & right) / len(union) if union else 0.0


def option_signature(row):
    options = row.get("options") or {}
    return tuple(sorted(normalize(options.get(letter, "")) for letter in LETTERS))


def find_candidates(rows, threshold=0.80):
    candidates = []
    for index, left in enumerate(rows):
        for right in rows[index + 1:]:
            if left.get("module_id") == right.get("module_id"):
                continue
            left_id, right_id = left.get("id", ""), right.get("id", "")
            score = jaccard(tokens(left.get("stem", "")), tokens(right.get("stem", "")))
            same_stem = normalize(left.get("stem", "")) == normalize(right.get("stem", ""))
            same_options = option_signature(left) == option_signature(right)
            if same_stem or same_options or score >= threshold:
                candidates.append({
                    "score": round(score, 3),
                    "left_id": left_id,
                    "right_id": right_id,
                    "left_module": left.get("module_id", ""),
                    "right_module": right.get("module_id", ""),
                    "same_stem": same_stem,
                    "same_options": same_options,
                    "left_stem": left.get("stem", ""),
                    "right_stem": right.get("stem", ""),
                })
    return sorted(candidates, key=lambda item: (-item["score"], item["left_id"], item["right_id"]))


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("--questions", type=Path, default=DEFAULT_PATH)
    parser.add_argument("--threshold", type=float, default=0.80)
    args = parser.parse_args(argv)
    if not 0 <= args.threshold <= 1:
        parser.error("threshold must be between 0 and 1")
    rows = [json.loads(line) for line in args.questions.read_text(encoding="utf-8").splitlines() if line.strip()]
    candidates = find_candidates(rows, args.threshold)
    print(f"Cross-module duplicate gate: {len(rows)} questions; threshold={args.threshold:.2f}; candidates={len(candidates)}")
    for item in candidates:
        print(f"FAIL {item['left_id']} ({item['left_module']}) / {item['right_id']} ({item['right_module']}); "
              f"similarity={item['score']:.3f}; same_stem={item['same_stem']}; same_options={item['same_options']}")
        print(f"  A: {item['left_stem']}")
        print(f"  B: {item['right_stem']}")
    if candidates:
        return 1
    print("PASS: no cross-module identical or near-identical question pairs.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
