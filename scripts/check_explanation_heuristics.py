#!/usr/bin/env python3
"""Advisory review of the 86 explanation-heuristic candidates from Stage 4x10.

A missing signal word is not a finding of poor teaching or legal error. The
script only helps reviewers find candidates after expanding the signal vocabulary.
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BANK = ROOT / "podstawowy" / "questions.jsonl"
CANDIDATES = ROOT / "review" / "stage4x11-heuristic-candidates.json"
EXPLANATORY_SIGNALS = (
    "ponieważ", "dlatego", "bo ", "więc", "czyli", "oznacza to",
    "z tego powodu", "w rezultacie", "dzięki temu", "pozwala", "służy",
    "wynika", "nie zastępuje", "nie wystarczy", "nie odpowiada",
    "nie identyfikuje", "nie oznacza", "nie dotyczy", "a nie", "zamiast",
    "natomiast", "jednak", "w przeciwieństwie", "ma znaczenie", "chodzi o",
    "obejmuje", "dotyczy", "wymaga", "nie można", "nie wolno", "nie jest",
    "nie są", "nie musi", "nie powinien", "nie należy", "samo ", "sama ",
)


def has_explanatory_signal(explanation):
    text = (explanation or "").casefold()
    return any(signal in text for signal in EXPLANATORY_SIGNALS)


def main():
    bank = {
        row["id"]: row
        for line in BANK.read_text(encoding="utf-8").splitlines()
        if line.strip()
        for row in [json.loads(line)]
    }
    baseline = json.loads(CANDIDATES.read_text(encoding="utf-8"))
    ids = baseline["question_ids"]
    missing = [question_id for question_id in ids if question_id not in bank]
    if missing:
        print("FAIL: candidate IDs missing from question bank:", ", ".join(missing))
        return 1
    remaining = [
        question_id for question_id in ids
        if not has_explanatory_signal(bank[question_id].get("explanation", ""))
    ]
    print(f"Stage 4x10 baseline warnings: {baseline['baseline_warning_count']}")
    print(f"Candidates checked against current bank: {len(ids)}")
    print(f"Remaining signal-only warnings after vocabulary expansion: {len(remaining)}")
    if remaining:
        print("Manual review candidates (absence of a signal is not itself an error):")
        for question_id in remaining:
            print(f"  {question_id}")
    print("PASS: all candidate IDs exist; heuristic results are advisory.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
