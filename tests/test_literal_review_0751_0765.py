"""Kontrola pierwsza ADR-B-0751–0765: manifest i niezmienność banku."""
from collections import Counter
import hashlib
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
BANK = ROOT / "podstawowy/questions.jsonl"
REPORT = ROOT / "review/literal-pl/PARTIA-0751-0765.md"
MANIFEST = ROOT / "review/literal-pl/PARTIA-0751-0765.json"
COMPETENCIES = ROOT / "podstawowy/kompetencje.json"

FIRST_PASS_BANK_SHA = "ff19af70af76de006d2f58b1fbfed7c091d52590"
EXPECTED_BANK_SHA = "ff19af70af76de006d2f58b1fbfed7c091d52590"
EXPECTED_IDS = [f"ADR-B-{n:04d}" for n in range(751, 766)]


def git_blob_sha(data):
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


class Partia51LiteralReview(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
        cls.raw = BANK.read_bytes()
        cls.questions = [json.loads(line) for line in cls.raw.decode("utf-8").splitlines() if line.strip()]
        cls.bank = {row["id"]: row for row in cls.questions}
        matrix = json.loads(COMPETENCIES.read_text(encoding="utf-8"))
        cls.competencies = {
            question_id: competency["id"]
            for competency in matrix["competencies"]
            for question_id in competency["question_ids"]
        }

    def test_first_pass_scope_and_unchanged_bank(self):
        self.assertTrue(REPORT.is_file())
        self.assertEqual(git_blob_sha(self.raw), EXPECTED_BANK_SHA)
        self.assertEqual(FIRST_PASS_BANK_SHA, EXPECTED_BANK_SHA)
        self.assertEqual(len(self.questions), 780)
        self.assertEqual(self.manifest["scope"], "first_pass_literal_review")
        self.assertEqual(self.manifest["batch"], "ADR-B-0751–0765")
        self.assertEqual(self.manifest["bank_blob_sha"], FIRST_PASS_BANK_SHA)
        self.assertFalse(self.manifest["bank_changed"])
        self.assertEqual(self.manifest["bank_count"], 780)
        self.assertEqual(self.manifest["previous_uncompared"], 30)
        self.assertEqual(self.manifest["compared"], 15)
        self.assertEqual(self.manifest["remaining_without_comparison"], 15)
        self.assertEqual(self.manifest["verified"], 0)

    def test_manifest_records_and_counts(self):
        rows = self.manifest["records"]
        self.assertEqual([row["id"] for row in rows], EXPECTED_IDS)
        self.assertEqual(len(rows), 15)
        counts = Counter(row["verdict"] for row in rows)
        self.assertEqual(
            self.manifest["counts"],
            {key: counts.get(key, 0) for key in ("OK", "POPRAW", "BLOKUJ")},
        )
        self.assertEqual(self.manifest["counts"], {"OK": 0, "POPRAW": 15, "BLOKUJ": 0})

        for row in rows:
            with self.subTest(id=row["id"]):
                question = self.bank[row["id"]]
                self.assertEqual(row["module_id"], question["module_id"])
                self.assertEqual(row["original_correct_option"], question["correct_option"])
                self.assertEqual(row["competency_id"], self.competencies[row["id"]])
                self.assertTrue(row["legal_basis"])
                self.assertTrue(row["exact_quote"])
                self.assertTrue(row["gazette_pages"])
                self.assertTrue(all(isinstance(page, int) and page > 0 for page in row["gazette_pages"]))
                self.assertTrue(row["finding"])
                self.assertEqual(row["verdict"], "POPRAW")
                self.assertEqual(row["verification_status"], "needs_review")
                self.assertEqual(question["verification_status"], "needs_review")
                self.assertIsNone(question["checked_at"])
                self.assertIsNone(question["reviewer"])


if __name__ == "__main__":
    unittest.main()
