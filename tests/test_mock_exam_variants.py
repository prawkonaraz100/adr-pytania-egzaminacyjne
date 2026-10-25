import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from check_mock_exam_variants import audit, longest_run


class MockExamVariantBalanceTests(unittest.TestCase):
    def test_all_variants_match_bank_and_balance_answers(self):
        errors, stats, _warnings = audit()
        self.assertEqual(errors, [])
        self.assertEqual(len(stats), 5)
        for item in stats:
            self.assertEqual(item["letters"], {"A": 10, "B": 10, "C": 10})
            self.assertLessEqual(item["longest_run"], 3)
            self.assertEqual(len(item["modules"]), 13)
            self.assertEqual(sum(item["modules"].values()), 30)
            self.assertTrue(all(count in (2, 3) for count in item["modules"].values()))

    def test_run_counter(self):
        self.assertEqual(longest_run(list("AABBBCC")), 3)
        self.assertEqual(longest_run(list("AAAAB")), 4)


if __name__ == "__main__":
    unittest.main()
