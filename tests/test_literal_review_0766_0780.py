"""Literal first-pass gate for ADR-B-0766–0780."""
from collections import Counter
import hashlib
import json
import re
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
BANK = ROOT / "podstawowy/questions.jsonl"
REPORT = ROOT / "review/literal-pl/PARTIA-0766-0780.md"
MANIFEST = ROOT / "review/literal-pl/PARTIA-0766-0780.json"
COMPETENCIES = ROOT / "podstawowy/kompetencje.json"
APPROVALS = ROOT / "review/approvals.jsonl"

FIRST_PASS_BANK_SHA = "cef031e32248db1a3a0ae05e0b725bcacb9f0b0a"
EXPECTED_BANK_SHA = "e2fba7594e5334356a1e5f3192987e538d58ee2c"
EXPECTED_IDS = [f"ADR-B-{n:04d}" for n in range(766, 781)]
ABSOLUTES = ("tylko", "wyłącznie", "zawsze", "nigdy", "żaden", "żadna", "żadne", "wszystkie", "każdy", "każda", "każde", "niezależnie")


def git_blob_sha(data):
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


class Partia52LiteralReview(unittest.TestCase):
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

    def test_scope_and_unchanged_bank(self):
        self.assertTrue(REPORT.is_file())
        self.assertTrue(APPROVALS.is_file())
        self.assertEqual(APPROVALS.read_text(encoding="utf-8").strip(), "")
        self.assertEqual(git_blob_sha(self.raw), EXPECTED_BANK_SHA)
        self.assertNotEqual(FIRST_PASS_BANK_SHA, EXPECTED_BANK_SHA)
        self.assertEqual(len(self.questions), 780)
        self.assertEqual(self.manifest["scope"], "first_pass_literal_review")
        self.assertEqual(self.manifest["batch"], "ADR-B-0766–0780")
        self.assertEqual(self.manifest["bank_blob_sha"], FIRST_PASS_BANK_SHA)
        self.assertFalse(self.manifest["bank_changed"])
        self.assertEqual(self.manifest["bank_count"], 780)
        self.assertEqual(self.manifest["previous_uncompared"], 15)
        self.assertEqual(self.manifest["compared"], 15)
        self.assertEqual(self.manifest["remaining_without_comparison"], 0)
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
                replacement = row["proposed_replacement"]
                self.assertEqual(row["module_id"], question["module_id"])
                self.assertEqual(row["original_correct_option"], question["correct_option"])
                self.assertEqual(row["competency_id"], self.competencies[row["id"]])
                self.assertTrue(row["legal_basis"])
                self.assertTrue(row["exact_quote"])
                self.assertTrue(row["gazette_pages"])
                self.assertTrue(row["finding"])
                self.assertEqual(row["verdict"], "POPRAW")
                self.assertEqual(row["verification_status"], "needs_review")
                self.assertEqual(question["verification_status"], "needs_review")
                self.assertIsNone(question.get("checked_at"))
                self.assertIsNone(question.get("reviewer"))
                self.assertEqual(replacement["module_id"], question["module_id"])
                self.assertEqual(replacement["competency_id"], self.competencies[row["id"]])
                self.assertEqual(replacement["correct_option"], question["correct_option"])
                self.assertEqual(set(replacement["options"]), {"A", "B", "C"})
                options = [replacement["options"][letter] for letter in "ABC"]
                lengths = [len(option) for option in options]
                self.assertTrue(all(0 < length <= 80 for length in lengths))
                correct_length = lengths["ABC".index(replacement["correct_option"])]
                self.assertFalse(lengths.count(min(lengths)) == 1 and correct_length == min(lengths))
                self.assertFalse(lengths.count(max(lengths)) == 1 and correct_length == max(lengths))
                for option in options:
                    self.assertFalse(option.endswith((".", ";")))
                    self.assertFalse(option.startswith(("Tak.", "Nie.", "Tak,", "Nie,")))
                    for word in ABSOLUTES:
                        self.assertNotIn(word, option.lower().split())
                explanation = replacement["explanation"]
                self.assertGreaterEqual(len(explanation), 200)
                self.assertLessEqual(len(explanation), 500)
                self.assertRegex(explanation, r"Podstawa: ADR 2025, .+\.$")
                self.assertTrue(replacement["sources"])
                self.assertTrue(replacement["replacement_quote"])
                self.assertTrue(replacement["replacement_pages"])


    def test_second_pass_artifacts_and_bank_sha(self):
        corrections_path = ROOT / "review/literal-pl/POPRAWKI-KONTROLA2-0766-0780.jsonl"
        report_path = ROOT / "review/literal-pl/KONTROLA2-PARTIA-0766-0780.md"
        self.assertTrue(report_path.is_file())
        self.assertTrue(corrections_path.is_file())
        corrections = [json.loads(line) for line in corrections_path.read_text(encoding="utf-8").splitlines() if line.strip()]
        self.assertEqual(len(corrections), 15)
        self.assertEqual([row["id"] for row in corrections], EXPECTED_IDS)
        for row in corrections:
            with self.subTest(id=row["id"]):
                self.assertEqual(row["verification_status"], "needs_review")
                self.assertEqual(row["correct_option"], self.bank[row["id"]]["correct_option"])
                self.assertEqual(row, self.bank[row["id"]])
        self.assertEqual(git_blob_sha(self.raw), EXPECTED_BANK_SHA)

if __name__ == "__main__":
    unittest.main()
