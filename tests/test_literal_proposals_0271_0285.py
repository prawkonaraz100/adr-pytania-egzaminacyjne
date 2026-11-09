"""Regression record for the first literal review of ADR-B-0271–0285."""
import json
import unittest
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
class Partia19(unittest.TestCase):
    def test_first_review_report_and_second_review_outcomes(self):
        d = json.loads((ROOT / "review/literal-pl/PARTIA-0271-0285.json").read_text(encoding="utf-8"))
        self.assertEqual(d["counts"], {"OK": 2, "POPRAW": 13, "BLOKUJ": 0})
        self.assertEqual((d["previous_uncompared"], d["remaining_without_comparison"]), (483, 468))
        self.assertEqual(len(d["records"]), 15)
        self.assertEqual(sum(x["second_review_verdict"] == "POPRAW" for x in d["records"]), 15)
    def test_bank_records_remain_unverified(self):
        rows = [json.loads(x) for x in (ROOT / "podstawowy/questions.jsonl").read_text(encoding="utf-8").splitlines() if x.strip()]
        self.assertEqual(len(rows), 780)
        for q in rows:
            if 271 <= int(q["id"][-4:]) <= 285:
                self.assertEqual(q["verification_status"], "needs_review")
                self.assertIsNone(q["checked_at"])
                self.assertIsNone(q["reviewer"])
if __name__ == "__main__":
    unittest.main()
