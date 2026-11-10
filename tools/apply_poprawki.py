#!/usr/bin/env python3
"""Hurtowo stosuje pełne rekordy korekt kontroli literalnej, tylko kurs podstawowy ADR.

Przykład: python tools/apply_poprawki.py
Późniejsze pliki POPRAWKI mają pierwszeństwo nad wcześniejszymi.
"""
from __future__ import annotations
import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_BANK = ROOT / "podstawowy/questions.jsonl"
SOURCES = [
    "POPRAWKI-0001-0015.jsonl",
    "POPRAWKI-UZUPELNIENIE-0001-0015.jsonl",
    "POPRAWKI-0016-0030.jsonl",
    "POPRAWKI-0031-0045.jsonl",
    "POPRAWKI-0046-0060.jsonl",
    "POPRAWKI-0061-0075.jsonl",
    "POPRAWKI-KONTROLA2-0061-0075.jsonl",
    "POPRAWKI-0076-0090.jsonl",
    "POPRAWKI-KONTROLA2-0076-0090.jsonl",
    "POPRAWKI-0091-0105.jsonl",
    "POPRAWKI-KONTROLA2-0091-0105.jsonl",
    "POPRAWKI-0106-0120.jsonl",
    "POPRAWKI-KONTROLA2-0106-0120.jsonl",
    "POPRAWKI-0121-0135.jsonl",
    "POPRAWKI-KONTROLA2-0121-0135.jsonl",
    "POPRAWKI-0136-0150.jsonl",
    "POPRAWKI-KONTROLA2-0136-0150.jsonl",
    "POPRAWKI-0151-0165.jsonl",
    "POPRAWKI-KONTROLA2-0151-0165.jsonl",
    "POPRAWKI-0166-0180.jsonl",
    "POPRAWKI-KONTROLA2-0166-0180.jsonl",
    "POPRAWKI-0181-0195.jsonl",
    "POPRAWKI-KONTROLA2-0181-0195.jsonl",
    "POPRAWKI-0196-0210.jsonl",
    "POPRAWKI-KONTROLA2-0196-0210.jsonl",
    "POPRAWKI-KONTROLA2-0211-0225.jsonl",
    "POPRAWKI-KONTROLA2-0226-0240.jsonl",
    "POPRAWKI-KONTROLA2-0241-0255.jsonl",
    "POPRAWKI-KONTROLA2-0484-KLUCZ.jsonl",
    "POPRAWKI-KONTROLA2-0256.jsonl",
    "POPRAWKI-KONTROLA2-0257-0270.jsonl",
    "POPRAWKI-WDROZENIE-0271-0285.jsonl",
    "POPRAWKI-KONTROLA2-0256-0270.jsonl",
    "POPRAWKI-KONTROLA2-0271-0285.jsonl",
    "POPRAWKI-KONTROLA2-0286-0300.jsonl",
    "POPRAWKI-KONTROLA2-0301-0315.jsonl",
    "POPRAWKI-KONTROLA2-0316-0330.jsonl",
    "POPRAWKI-KONTROLA2-0331-0345.jsonl",
    "POPRAWKI-KONTROLA2-0346-0360.jsonl",
    "POPRAWKI-KONTROLA2-0361-0375.jsonl",
    "POPRAWKI-KONTROLA2-0376-0390.jsonl",
    "POPRAWKI-KONTROLA2-0391-0405.jsonl",
    "POPRAWKI-KONTROLA2-0406-0420.jsonl",
    "POPRAWKI-KONTROLA2-0421-0435.jsonl",
    "POPRAWKI-KONTROLA2-0436-0450.jsonl",
    "POPRAWKI-KONTROLA2-0451-0465.jsonl",
    "POPRAWKI-KONTROLA2-0466-0480.jsonl",
    "POPRAWKI-KONTROLA2-0481-0495.jsonl",
    "POPRAWKI-KONTROLA2-0496-0510.jsonl",
    "POPRAWKI-KONTROLA2-0511-0525.jsonl",
    "POPRAWKI-KONTROLA2-0526-0540.jsonl",
    "POPRAWKI-KONTROLA2-0541-0555.jsonl",
    "POPRAWKI-KONTROLA2-0556-0570.jsonl",
    "POPRAWKI-KONTROLA2-0571-0585.jsonl",
]

def read_jsonl(path: Path):
    with path.open(encoding="utf-8") as fh:
        for lineno, line in enumerate(fh, 1):
            if line.strip():
                try:
                    yield json.loads(line)
                except json.JSONDecodeError as e:
                    raise ValueError(f"{path}:{lineno}: {e}") from e

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--bank", type=Path, default=DEFAULT_BANK)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()
    bank_path = args.bank
    records = list(read_jsonl(bank_path))
    lookup = {record["id"]: i for i, record in enumerate(records)}
    if len(lookup) != len(records):
        raise ValueError("Duplicate IDs in bank")
    old = {x["id"]: x for x in records}
    patches = {}
    for filename in SOURCES:
        path = ROOT / "review/literal-pl" / filename
        for patch in read_jsonl(path):
            qid = patch["id"]
            if qid not in lookup:
                raise ValueError(f"Unknown correction ID: {qid}")
            original = old[qid]
            if list(patch) != list(original):
                raise ValueError(f"Schema or field order mismatch: {qid}")
            if patch["correct_option"] != original["correct_option"]:
                raise ValueError(f"Correct option changed: {qid}")
            if patch["verification_status"] != "needs_review" or patch["checked_at"] is not None or patch["reviewer"] is not None:
                raise ValueError(f"Review status mismatch: {qid}")
            patches[qid] = patch
    changed = sorted(qid for qid, patch in patches.items() if patch != old[qid])
    print(f"Changed ({len(changed)}): " + ", ".join(changed))
    if not args.dry_run:
        for qid in changed:
            records[lookup[qid]] = patches[qid]
        with bank_path.open("w", encoding="utf-8", newline="\n") as fh:
            for record in records:
                fh.write(json.dumps(record, ensure_ascii=False, separators=(",", ":")) + "\n")
if __name__ == "__main__":
    main()
