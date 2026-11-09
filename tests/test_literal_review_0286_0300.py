"""First literal review report for ADR-B-0286–0300; bank must remain unchanged."""
import json
import unittest
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
class Partia20LiteralReview(unittest.TestCase):
    def test_report_counts_and_counter(self):
        d = json.loads((ROOT / "review/literal-pl/PARTIA-0286-0300.json").read_text(encoding="utf-8"))
        self.assertEqual(d["bank_count"], 780)
        self.assertEqual(d["counts"], {"OK": 0, "POPRAW": 13, "BLOKUJ": 2})
        self.assertEqual((d["previous_uncompared"], d["remaining_without_comparison"]), (468, 453))
        self.assertEqual(len(d["records"]), 15)
    def test_questions_are_not_changed_or_verified(self):
        rows = [json.loads(x) for x in (ROOT / "podstawowy/questions.jsonl").read_text(encoding="utf-8").splitlines() if x.strip()]
        self.assertEqual(len(rows), 780)
        for q in rows:
            if 286 <= int(q["id"][-4:]) <= 300:
                self.assertEqual(q["verification_status"], "needs_review")
                self.assertIsNone(q["checked_at"])
                self.assertIsNone(q["reviewer"])
if __name__ == "__main__":
    unittest.main()
