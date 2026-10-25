#!/usr/bin/env python3
"""Block new near-duplicate question stems/options within a course module.

Similarity is a triage heuristic, not proof of legal or semantic duplication.
Reviewed pairs remain allowlisted with a rationale; remove an entry once its
question is rewritten or the pair is otherwise resolved.
"""
import argparse
import json
import re
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_PATH = ROOT / "podstawowy" / "questions.jsonl"
THRESHOLD = 0.60

# Existing pairs reviewed manually. 0071/0072 test different DMC bands and
# distinct numerical thresholds. 0330/0337 test different ADR exclusions:
# class 5.2 versus class 6.2. Confirmed duplicate 0169/0585 was resolved by
# rewriting 0585 to test mounting/protection against damage rather than access.
REVIEWED_PAIR_ALLOWLIST = {
    ("ADR-B-0071", "ADR-B-0072"): "Same rule, different DMC band; answers test distinct threshold.",
    ("ADR-B-0330", "ADR-B-0337"): "Same procedural question but distinct ADR exclusions: class 5.2 versus class 6.2.",
}
STOP = {"jakie", "jaki", "ktora", "ktore", "ktory", "przy", "podczas", "zgodnie",
        "przewozu", "przewoz", "przed", "nalezy", "powinien", "powinna", "towaru",
        "towarow", "niebezpiecznych", "jesli", "jezeli", "przez", "mozna", "jest",
        "oraz", "tylko", "ktorych", "jak", "czy", "sie", "tym", "tego"}

def normalize(text):
    text = unicodedata.normalize("NFKD", str(text or "").casefold())
    text = "".join(ch for ch in text if not unicodedata.combining(ch))
    return re.sub(r"[^a-z0-9]+", " ", text).strip()

def tokens(text):
    return {word for word in normalize(text).split()
            if len(word) >= 4 and word not in STOP}

def jaccard(a, b):
    union = a | b
    return len(a & b) / len(union) if union else 0.0

def option_signature(row):
    options = row.get("options") or {}
    return tuple(sorted(normalize(options.get(letter, "")) for letter in "ABC"))

def find_candidates(rows, threshold=THRESHOLD):
    pairs = []
    for i, left in enumerate(rows):
        for right in rows[i + 1:]:
            if left.get("module_id") != right.get("module_id"):
                continue
            left_id, right_id = left.get("id", ""), right.get("id", "")
            pair = tuple(sorted((left_id, right_id)))
            score = jaccard(tokens(left.get("stem", "")), tokens(right.get("stem", "")))
            same_options = option_signature(left) == option_signature(right)
            if (score >= threshold or same_options) and pair not in REVIEWED_PAIR_ALLOWLIST:
                pairs.append((round(score, 3), left_id, right_id, same_options,
                              left.get("stem", ""), right.get("stem", "")))
    return sorted(pairs, key=lambda item: (-item[0], item[1], item[2]))

def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("--questions", type=Path, default=DEFAULT_PATH)
    parser.add_argument("--threshold", type=float, default=THRESHOLD)
    args = parser.parse_args(argv)
    if not 0 <= args.threshold <= 1:
        parser.error("threshold must be between 0 and 1")
    rows = [json.loads(line) for line in args.questions.read_text(encoding="utf-8").splitlines() if line.strip()]
    pairs = find_candidates(rows, args.threshold)
    print(f"Near-duplicate gate: {len(rows)} questions; threshold={args.threshold:.2f}; unreviewed candidates={len(pairs)}")
    if pairs:
        for score, left, right, same_options, stem_a, stem_b in pairs:
            print(f"FAIL {score:.3f} {left} / {right}; same_options={same_options}")
            print(f"  A: {stem_a}")
            print(f"  B: {stem_b}")
        return 1
    print(f"PASS: no unreviewed near-duplicate pairs. Reviewed allowlist: {len(REVIEWED_PAIR_ALLOWLIST)} pair(s).")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
