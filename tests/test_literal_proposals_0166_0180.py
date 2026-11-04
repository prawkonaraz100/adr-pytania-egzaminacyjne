"""Ensure all 15 approved second-review records for batch 12 match the current bank."""
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BANK = ROOT / "podstawowy/questions.jsonl"
SECOND = ROOT / "review/literal-pl/POPRAWKI-KONTROLA2-0166-0180.jsonl"
REPORT = ROOT / "review/literal-pl/PARTIA-0166-0180.json"
EXPECTED = {f"ADR-B-{n:04d}" for n in range(166,181)}

def read_jsonl(path):
    return [json.loads(s) for s in path.read_text(encoding="utf-8").splitlines() if s.strip()]

class Batch12LiteralProposalTests(unittest.TestCase):
    def test_second_pass_applied_exactly(self):
        bank = {r["id"]:r for r in read_jsonl(BANK)}
        patches = read_jsonl(SECOND)
        self.assertEqual(len(bank),780)
        self.assertEqual({r["id"] for r in patches},EXPECTED)
        for q in patches:
            self.assertEqual(bank[q["id"]],q)
            self.assertEqual(q["verification_status"],"needs_review")
            self.assertIsNone(q["checked_at"])
            self.assertIsNone(q["reviewer"])
        self.assertTrue(all(q["verification_status"]=="needs_review" for q in bank.values()))
        self.assertTrue(all(q["checked_at"] is None and q["reviewer"] is None for q in bank.values()))
        self.assertIn("S12",bank["ADR-B-0160"]["explanation"])
        self.assertIn("nie kontener-cysterna",bank["ADR-B-0140"]["stem"])

    def test_verdicts_official_page_numbers(self):
        report = json.loads(REPORT.read_text(encoding="utf-8"))
        self.assertEqual(report["previous_uncompared"],588)
        self.assertEqual(report["remaining_without_comparison"],573)
        self.assertEqual(report["counts"],{"OK":0,"POPRAW":15,"BLOKUJ":0})
        self.assertEqual(len(report["records"]),15)
        self.assertEqual({q["id"] for q in report["records"]},EXPECTED)
        self.assertTrue(all(q["verdict"]=="POPRAW" for q in report["records"]))
        self.assertEqual(next(x["page"] for x in report["records"] if x["id"]=="ADR-B-0174"),1338)

if __name__=="__main__":
    unittest.main()
