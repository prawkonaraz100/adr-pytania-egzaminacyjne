"""Validate applied second-review batch 11 corrections and their legal-audit reports."""
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BANK = ROOT / "podstawowy/questions.jsonl"
SECOND = ROOT / "review/literal-pl/POPRAWKI-KONTROLA2-0151-0165.jsonl"
REPORT = ROOT / "review/literal-pl/PARTIA-0151-0165.json"
EXPECTED = {f"ADR-B-{n:04d}" for n in range(151, 166)}

def read_jsonl(p):
    return [json.loads(line) for line in p.read_text(encoding="utf-8").splitlines() if line.strip()]

class LiteralBatch11Tests(unittest.TestCase):
    def test_all_second_review_records_applied_exactly(self):
        current = {q["id"]: q for q in read_jsonl(BANK)}
        patches = read_jsonl(SECOND)
        self.assertEqual(len(current), 780)
        self.assertEqual({q["id"] for q in patches}, EXPECTED)
        for q in patches:
            self.assertEqual(current[q["id"]], q)
            self.assertEqual(q["verification_status"], "needs_review")
            self.assertIsNone(q["checked_at"])
            self.assertIsNone(q["reviewer"])
        self.assertTrue(all(q["verification_status"] == "needs_review" for q in current.values()))
        self.assertTrue(all(q["checked_at"] is None and q["reviewer"] is None for q in current.values()))
        self.assertIn("S12", current["ADR-B-0160"]["explanation"])
        self.assertIn("S12", current["ADR-B-0160"]["sources"][0]["reference"])
        self.assertIn("nie kontener-cysterna", current["ADR-B-0140"]["stem"])
        self.assertIn("kontenerów-cystern", current["ADR-B-0140"]["explanation"])

    def test_second_review_verdicts_and_counters(self):
        report = json.loads(REPORT.read_text(encoding="utf-8"))
        self.assertEqual(report["previous_uncompared"], 603)
        self.assertEqual(report["remaining_without_comparison"], 588)
        self.assertEqual(report["counts"], {"OK": 0, "POPRAW": 15, "BLOKUJ": 0})
        self.assertEqual(len(report["records"]), 15)
        self.assertEqual({q["id"] for q in report["records"]}, EXPECTED)
        self.assertTrue(all(q["verdict"] == "POPRAW" for q in report["records"]))

if __name__ == "__main__":
    unittest.main()
