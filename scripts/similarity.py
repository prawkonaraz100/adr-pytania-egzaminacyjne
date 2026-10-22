#!/usr/bin/env python3
"""Human review candidates, never a legal or semantic correctness certificate."""
import argparse
import json
import re
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STOP = {
    "adr", "jakie", "jaki", "ktora", "ktore", "ktory", "ktorego", "przy",
    "podczas", "zgodnie", "przewozu", "przewoz", "przed", "nalezy",
    "powinien", "powinna", "powinno", "towaru", "towarow", "niebezpiecznych",
    "niebezpieczne", "jesli", "jezeli", "przez", "mozna", "jest", "oraz",
    "tylko", "ktora", "ktorych", "jak", "czy", "sie", "tym", "tego"
}


def tokens(text):
    normalized = unicodedata.normalize("NFKD", text.casefold())
    normalized = "".join(c for c in normalized if not unicodedata.combining(c))
    return set(w for w in re.findall(r"[a-z0-9]{4,}", normalized) if w not in STOP)


def jaccard(a, b):
    union = a | b
    return len(a & b) / len(union) if union else 0.0


def find_candidates(records, threshold=0.45):
    pairs = []
    stems = [(row["id"], row["module_id"], row["stem"], tokens(row["stem"])) for row in records]
    for i, (id_a, module_a, stem_a, t_a) in enumerate(stems):
        for id_b, module_b, stem_b, t_b in stems[i + 1:]:
            if module_a != module_b:
                continue
            score = jaccard(t_a, t_b)
            if score >= threshold:
                pairs.append((round(score, 3), id_a, id_b, stem_a, stem_b))
    return sorted(pairs, key=lambda p: (-p[0], p[1], p[2]))


def main():
    parser = argparse.ArgumentParser(description="Rank question-pair wording overlap for human review")
    parser.add_argument("--questions", type=Path, default=ROOT / "podstawowy/questions.jsonl")
    parser.add_argument("--threshold", type=float, default=0.45)
    parser.add_argument("--limit", type=int, default=12)
    args = parser.parse_args()
    if not 0 <= args.threshold <= 1 or args.limit < 0:
        parser.error("threshold must be 0..1 and limit must be nonnegative")
    records = [json.loads(line) for line in args.questions.read_text(encoding="utf-8").splitlines() if line.strip()]
    matches = find_candidates(records, threshold=args.threshold)
    print(f"Near-duplicate wording candidates (human review only): {len(matches)}")
    for score, a, b, stem_a, stem_b in matches[:args.limit]:
        print(f"  {score:.3f}: {a} / {b}")
        print(f"    A: {stem_a}")
        print(f"    B: {stem_b}")
    print("NOTE: similar questions can test different thresholds or conditions; similarity does not imply a factual error.")
    print("NOTE: this does not check answer correctness, ADR legal compliance, or semantic paraphrases.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
