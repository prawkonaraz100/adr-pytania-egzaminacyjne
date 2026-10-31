"""Guard the current coverage matrix against drift from the question bank."""
import json
import re
import unittest
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BANK = ROOT / "podstawowy" / "questions.jsonl"
COVERAGE = ROOT / "docs" / "POKRYCIE-KURSU.md"


class CoverageReportMetricsTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.questions = [
            json.loads(line)
            for line in BANK.read_text(encoding="utf-8").splitlines()
            if line.strip()
        ]
        cls.coverage = COVERAGE.read_text(encoding="utf-8")

    def test_question_counts_by_module_match_the_current_matrix(self):
        counts = Counter(q["module_id"] for q in self.questions)
        matrix = self.coverage.split("## Matryca gotowości", 1)[1].split(
            "## Pogłębienie zagadnień", 1
        )[0]
        rows = {}
        for line in matrix.splitlines():
            match = re.match(r"\|\s*(ADR-B-\d{2})\s*\|", line)
            if match:
                cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
                rows[match.group(1)] = int(cells[4])
        self.assertEqual(set(rows), {f"ADR-B-{i:02d}" for i in range(1, 14)})
        self.assertEqual(rows, {f"ADR-B-{i:02d}": counts[f"ADR-B-{i:02d}"] for i in range(1, 14)})
        self.assertEqual(sum(rows.values()), len(self.questions))

    def test_answer_distribution_and_unique_longest_metric_match_the_bank(self):
        letters = Counter(q["correct_option"] for q in self.questions)
        dist = re.search(
            r"Rozkład prawidłowych opcji: A=(\d+), B=(\d+), C=(\d+)", self.coverage
        )
        self.assertIsNotNone(dist)
        self.assertEqual(
            tuple(map(int, dist.groups())),
            (letters["A"], letters["B"], letters["C"]),
        )
        strict = 0
        per_module = Counter()
        module_counts = Counter(q["module_id"] for q in self.questions)
        for q in self.questions:
            lengths = [len(q["options"][letter]) for letter in "ABC"]
            max_length = max(lengths)
            correct_length = len(q["options"][q["correct_option"]])
            if correct_length == max_length and lengths.count(max_length) == 1:
                strict += 1
                per_module[q["module_id"]] += 1
        summary = re.search(
            r"Globalny wskaźnik .*?\*\*(\d+)/(\d+) = ([\d,]+)%\*\*; maksimum działu to ([\d,]+)%",
            self.coverage,
        )
        self.assertIsNotNone(summary)
        self.assertEqual(int(summary.group(1)), strict)
        self.assertEqual(int(summary.group(2)), len(self.questions))
        self.assertEqual(summary.group(3), f"{100 * strict / len(self.questions):.2f}".replace(".", ","))
        maximum = max(100 * per_module[m] / module_counts[m] for m in module_counts)
        self.assertEqual(summary.group(4), f"{maximum:.2f}".replace(".", ","))

    def test_bank_statuses_remain_draft_only(self):
        self.assertEqual(len(self.questions), 677)
        self.assertEqual(len({q["id"] for q in self.questions}), 677)
        self.assertTrue(all(q["verification_status"] == "needs_review" for q in self.questions))
        self.assertEqual(sum(q["verification_status"] == "verified" for q in self.questions), 0)
        self.assertIn("Stan aktualny po etapie 4x251: 31.10.2026.", self.coverage)


if __name__ == "__main__":
    unittest.main()
