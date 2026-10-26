import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from check_mock_exam_variants import audit, longest_run, near_duplicate_pairs


class MockExamVariantBalanceTests(unittest.TestCase):
    def test_all_variants_match_bank_and_balance_answers(self):
        errors, stats, _warnings = audit()
        self.assertEqual(errors, [])
        self.assertEqual(len(stats), 5)
        for item in stats:
            self.assertEqual(item["letters"], {"A": 10, "B": 10, "C": 10})
            self.assertLessEqual(item["longest_run"], 3)
            self.assertLessEqual(item["strictly_longest_rate"], 0.18)
            self.assertEqual(len(item["modules"]), 13)
            self.assertEqual(sum(item["modules"].values()), 30)
            self.assertTrue(all(count in (2, 3) for count in item["modules"].values()))

    def test_near_duplicate_guard(self):
        rows = [
            {"id": "A", "stem": "Kierowca przed wyjazdem sprawdza wymagane dokumenty przewozowe towaru niebezpiecznego"},
            {"id": "B", "stem": "Kierowca przed wyjazdem sprawdza wymagane dokumenty przewozowe towaru niebezpiecznego!"},
            {"id": "C", "stem": "Jakie są kategorie tuneli drogowych wskazane w ADR?"},
        ]
        self.assertEqual(near_duplicate_pairs(rows), [("A", "B")])
        self.assertEqual(near_duplicate_pairs([rows[0], rows[2]]), [])

    def test_run_counter(self):
        self.assertEqual(longest_run(list("AABBBCC")), 3)
        self.assertEqual(longest_run(list("AAAAB")), 4)


if __name__ == "__main__":
    unittest.main()
