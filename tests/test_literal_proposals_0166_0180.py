"""Test batch 12 first-literal-pass proposals only on an isolated copy of the live ADR bank."""
import copy
import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BANK = ROOT / "podstawowy/questions.jsonl"
PROPOSALS = ROOT / "review/literal-pl/POPRAWKI-0166-0180.jsonl"
REPORT = ROOT / "review/literal-pl/PARTIA-0166-0180.json"
EXPECTED = {f"ADR-B-{n:04d}" for n in range(166, 181)}

def read_jsonl(path):
    return [json.loads(s) for s in path.read_text(encoding="utf-8").splitlines() if s.strip()]

class Batch12LiteralProposalTests(unittest.TestCase):
    def test_proposals_on_copy_only(self):
        bank = {r["id"]:r for r in read_jsonl(BANK)}
        self.assertEqual(len(bank), 780)
        proposals = read_jsonl(PROPOSALS)
        self.assertEqual({r["id"] for r in proposals}, EXPECTED)
        self.assertEqual(len(proposals), 15)
        copy_bank = copy.deepcopy(bank)
        for r in proposals:
            ident = r["id"]
            original = bank[ident]
            self.assertEqual(list(r), list(original))
            self.assertEqual(r["correct_option"], original["correct_option"])
            self.assertEqual(r["verification_status"], "needs_review")
            self.assertIsNone(r["checked_at"])
            self.assertIsNone(r["reviewer"])
            self.assertEqual(set(r["options"]), {"A", "B", "C"})
            self.assertEqual(len(set(r["options"].values())), 3)
            lengths = {key:len(v) for key,v in r["options"].items()}
            key_length = lengths[r["correct_option"]]
            self.assertFalse(key_length == max(lengths.values()) and list(lengths.values()).count(key_length) == 1, ident)
            self.assertFalse(key_length == min(lengths.values()) and list(lengths.values()).count(key_length) == 1, ident)
            exp = r["explanation"].strip()
            self.assertGreaterEqual(len(exp), 300)
            sentences = re.split(r"(?<=[.!?])\s+", exp)
            self.assertTrue(2 <= len(sentences) <= 5, ident)
            self.assertTrue(all(len(s.split()) <= 35 for s in sentences), ident)
            self.assertRegex(exp, r"Podstawa: ADR .+\.$")
            self.assertTrue(r["sources"])
            self.assertEqual(r["sources"],original["sources"])
            copy_bank[ident] = r
        self.assertEqual(len(copy_bank), 780)
        self.assertTrue(all(r["verification_status"] == "needs_review" for r in copy_bank.values()))
        self.assertTrue(all(r["checked_at"] is None and r["reviewer"] is None for r in copy_bank.values()))
        self.assertIn("S12", copy_bank["ADR-B-0160"]["explanation"])
        self.assertIn("S12", copy_bank["ADR-B-0160"]["sources"][0]["reference"])
        self.assertIn("nie kontener-cysterna", copy_bank["ADR-B-0140"]["stem"])
        self.assertIn("kontenerów-cystern", copy_bank["ADR-B-0140"]["explanation"])

    def test_report_count_and_legal_quotes(self):
        report = json.loads(REPORT.read_text(encoding="utf-8"))
        self.assertEqual(report["previous_uncompared"], 588)
        self.assertEqual(report["remaining_without_comparison"], 573)
        self.assertEqual(report["counts"], {"OK":0, "POPRAW":15, "BLOKUJ":0})
        self.assertEqual({r["id"] for r in report["records"]}, EXPECTED)
        self.assertEqual(len(report["records"]), 15)
        for r in report["records"]:
            self.assertEqual(r["verdict"], "POPRAW")
            self.assertTrue(r["clause"] and r["page"] and r["quote"])
            self.assertIn("NIE zastosowano", r["fix"])

if __name__ == "__main__":
    unittest.main()
