"""Tests of batch 11 first-pass proposals against a copy of the 780-question bank."""
import copy
import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BANK = ROOT / "podstawowy" / "questions.jsonl"
PROPOSALS = ROOT / "review/literal-pl/POPRAWKI-0151-0165.jsonl"
REPORT = ROOT / "review/literal-pl/PARTIA-0151-0165.json"
EXPECTED = {f"ADR-B-{x:04d}" for x in [152,153,154,155,156,157,159,160,161,163,164,165]}
BLOCKED = {f"ADR-B-{x:04d}" for x in [151,158,162]}

def read_jsonl(path):
    return [json.loads(x) for x in path.read_text(encoding="utf-8").splitlines() if x.strip()]

class LiteralBatch11Tests(unittest.TestCase):
    def test_proposals_only_on_bank_copy(self):
        current = {q["id"]: q for q in read_jsonl(BANK)}
        self.assertEqual(len(current), 780)
        proposed = read_jsonl(PROPOSALS)
        self.assertEqual({q["id"] for q in proposed}, EXPECTED)
        copy_bank = copy.deepcopy(current)
        for q in proposed:
            ident = q["id"]
            self.assertEqual(list(q), list(current[ident]))
            self.assertEqual(q["correct_option"], current[ident]["correct_option"])
            self.assertEqual(q["verification_status"], "needs_review")
            self.assertIsNone(q["checked_at"])
            self.assertIsNone(q["reviewer"])
            self.assertEqual(set(q["options"]), {"A", "B", "C"})
            self.assertEqual(len(set(q["options"].values())), 3)
            lengths = {letter: len(text) for letter, text in q["options"].items()}
            correct = lengths[q["correct_option"]]
            self.assertFalse(correct == max(lengths.values()) and list(lengths.values()).count(correct) == 1, ident)
            self.assertFalse(correct == min(lengths.values()) and list(lengths.values()).count(correct) == 1, ident)
            exp = q["explanation"]
            self.assertGreaterEqual(len(exp), 300)
            sentences = re.split(r"(?<=[.!?])\s+", exp)
            self.assertTrue(2 <= len(sentences) <= 5, ident)
            self.assertTrue(all(len(s.split()) <= 35 for s in sentences), ident)
            self.assertRegex(exp, r"Podstawa: ADR .+\.$")
            self.assertTrue(q["sources"])
            copy_bank[ident] = q
        for ident in BLOCKED:
            self.assertEqual(copy_bank[ident], current[ident])
        self.assertEqual(len(copy_bank), 780)
        self.assertTrue(all(q["verification_status"] == "needs_review" for q in copy_bank.values()))
        self.assertTrue(all(q["reviewer"] is None and q["checked_at"] is None for q in copy_bank.values()))
        self.assertIn("S12", copy_bank["ADR-B-0160"]["explanation"])
        self.assertIn("S12", copy_bank["ADR-B-0160"]["sources"][0]["reference"])
        self.assertIn("nie kontener-cysterna", copy_bank["ADR-B-0140"]["stem"])
        self.assertIn("kontenerów-cystern", copy_bank["ADR-B-0140"]["explanation"])

    def test_audit_counts(self):
        report = json.loads(REPORT.read_text(encoding="utf-8"))
        self.assertEqual(report["previous_uncompared"], 603)
        self.assertEqual(report["remaining_without_comparison"], 588)
        self.assertEqual(report["counts"], {"OK": 0, "POPRAW": 12, "BLOKUJ": 3})
        self.assertEqual(len(report["records"]), 15)
        self.assertEqual({r["id"] for r in report["records"] if r["verdict"] == "POPRAW"}, EXPECTED)
        self.assertEqual({r["id"] for r in report["records"] if r["verdict"] == "BLOKUJ"}, BLOCKED)

if __name__ == "__main__":
    unittest.main()
