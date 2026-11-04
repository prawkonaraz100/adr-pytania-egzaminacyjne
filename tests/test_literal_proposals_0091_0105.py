"""Tests on an in-memory copy of the ADR bank with proposed literal corrections.
This does not apply proposals to production or assert legal approval.
"""
import copy
import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BANK = ROOT / "podstawowy" / "questions.jsonl"
PROPOSALS = ROOT / "review" / "literal-pl" / "POPRAWKI-0091-0105.jsonl"
EXPECTED = {"ADR-B-0092", "ADR-B-0093"}

def read_jsonl(path):
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]

class Part7ProposalTests(unittest.TestCase):
    def test_every_proposal_on_bank_copy(self):
        original = read_jsonl(BANK)
        changes = read_jsonl(PROPOSALS)
        self.assertEqual({x["id"] for x in changes}, EXPECTED)
        self.assertEqual(len(changes), len(EXPECTED))
        current = {x["id"]: x for x in original}
        test_copy = copy.deepcopy(current)
        for proposed in changes:
            ident = proposed["id"]
            self.assertIn(ident, current)
            old = current[ident]
            self.assertEqual(list(proposed), list(old))
            self.assertEqual(proposed["correct_option"], old["correct_option"])
            self.assertEqual(proposed["verification_status"], "needs_review")
            self.assertIsNone(proposed["checked_at"])
            self.assertIsNone(proposed["reviewer"])
            self.assertEqual(set(proposed["options"]), {"A", "B", "C"})
            self.assertEqual(len(set(proposed["options"].values())), 3)
            exp = proposed["explanation"].strip()
            self.assertGreaterEqual(len(exp), 300)
            sentences = re.split(r"(?<=[.!?])\\s+", exp)
            self.assertGreaterEqual(len(sentences), 2)
            self.assertLessEqual(len(sentences), 5)
            self.assertTrue(all(len(s.split()) <= 35 for s in sentences))
            self.assertRegex(exp, r"Podstawa: ADR .+\\.$")
            self.assertIn(proposed["sources"][0]["code"], {"ADR-2025-PL"})
            test_copy[ident] = proposed
        self.assertEqual(len(test_copy), 780)
        self.assertEqual(sum(x["verification_status"] == "needs_review" for x in test_copy.values()), 780)
        self.assertTrue(all(x["checked_at"] is None and x["reviewer"] is None for x in test_copy.values()))
        self.assertIn("nie jest wymaganym minimum", test_copy["ADR-B-0073"]["explanation"])
        self.assertEqual(test_copy["ADR-B-0073"]["correct_option"], "B")

if __name__ == "__main__":
    unittest.main()
