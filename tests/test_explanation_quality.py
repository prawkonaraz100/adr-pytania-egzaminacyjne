import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from check_explanation_quality import short_explanations


class ExplanationQualityTests(unittest.TestCase):
    def test_accepts_explanation_at_minimum(self):
        rows = [{"id": "ADR-B-0001", "explanation": "x" * 200}]
        self.assertEqual(short_explanations(rows), [])

    def test_rejects_missing_or_short_explanations(self):
        rows = [
            {"id": "ADR-B-0001", "explanation": "x" * 199},
            {"id": "ADR-B-0002", "explanation": ""},
            {"id": "ADR-B-0003"},
        ]
        self.assertEqual(short_explanations(rows), [
            ("ADR-B-0001", 199),
            ("ADR-B-0002", 0),
            ("ADR-B-0003", 0),
        ])

    def test_custom_minimum(self):
        rows = [{"id": "ADR-B-0001", "explanation": "x" * 50}]
        self.assertEqual(short_explanations(rows, 51), [("ADR-B-0001", 50)])


if __name__ == "__main__":
    unittest.main()
