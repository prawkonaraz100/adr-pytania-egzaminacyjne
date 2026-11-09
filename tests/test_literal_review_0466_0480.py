"""First-pass literal review for ADR-B-0466–0480; report-only, bank unchanged."""

import hashlib
import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BANK = ROOT / "podstawowy" / "questions.jsonl"
COMPETENCIES = ROOT / "podstawowy" / "kompetencje.json"
REPORT = ROOT / "review" / "literal-pl" / "PARTIA-0466-0480.json"
EXPECTED_BANK_SHA = "e560a3892b2b76217bf4ff9a977a1a4c2771eff8"
EXPECTED_IDS = [f"ADR-B-{number:04d}" for number in range(466, 481)]
EXPECTED_PAGES = {
    "ADR-B-0466": "066",
    "ADR-B-0467": "066",
    "ADR-B-0468": "960",
    "ADR-B-0469": "960",
    "ADR-B-0470": "960",
    "ADR-B-0471": "1332",
    "ADR-B-0472": "1332",
    "ADR-B-0473": "1332",
    "ADR-B-0474": "1304",
    "ADR-B-0475": "1304",
    "ADR-B-0476": "1304",
    "ADR-B-0477": "57",
    "ADR-B-0478": "59",
    "ADR-B-0479": "57",
    "ADR-B-0480": "59",
}
EXPECTED_COUNTS = {"OK": 1, "POPRAW": 14, "BLOKUJ": 0}
EXPECTED_REPLACEMENTS = {
    "ADR-B-0471": "ADR-B-04-K06",
    "ADR-B-0473": "ADR-B-04-K06",
    "ADR-B-0475": "ADR-B-04-K05",
}


def git_blob_sha(data: bytes) -> str:
    header = b"blob " + str(len(data)).encode("ascii") + b"\0"
    return hashlib.sha1(header + data).hexdigest()


def sentence_word_counts(text: str):
    sentences = re.split(r"(?<=[.!?])\s+(?=[A-ZŁŚŻŹĆŃÓĘĄ])", text.strip())
    return [len(sentence.split()) for sentence in sentences if sentence.strip()]


class FirstPassLiteralReview0466To0480Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.manifest = json.loads(REPORT.read_text(encoding="utf-8"))
        cls.questions = [
            json.loads(line)
            for line in BANK.read_text(encoding="utf-8").splitlines()
            if line.strip()
        ]
        cls.competencies = json.loads(COMPETENCIES.read_text(encoding="utf-8"))["competencies"]

    def test_report_scope_counts_and_page_headers(self):
        self.assertEqual(self.manifest["scope"], "first_pass_literal_review")
        self.assertEqual(self.manifest["batch"], "ADR-B-0466–0480")
        self.assertEqual(self.manifest["bank_count"], 780)
        self.assertEqual(self.manifest["bank_blob_sha"], EXPECTED_BANK_SHA)
        self.assertFalse(self.manifest["bank_changed"])
        self.assertEqual(self.manifest["previous_uncompared"], 315)
        self.assertEqual(self.manifest["compared"], 15)
        self.assertEqual(self.manifest["remaining_without_comparison"], 300)
        self.assertEqual(self.manifest["counts"], EXPECTED_COUNTS)
        self.assertEqual([row["id"] for row in self.manifest["records"]], EXPECTED_IDS)
        self.assertEqual(
            {row["id"]: row["gazette_page"] for row in self.manifest["records"]},
            EXPECTED_PAGES,
        )
        self.assertTrue(all(row["verification_status"] == "needs_review" for row in self.manifest["records"]))
        self.assertEqual(self.manifest["verified"], 0)

    def test_bank_is_unchanged_and_all_batch_questions_remain_unverified(self):
        raw = BANK.read_bytes()
        self.assertEqual(git_blob_sha(raw), EXPECTED_BANK_SHA)
        self.assertEqual(len(self.questions), 780)
        by_id = {row["id"]: row for row in self.questions}
        self.assertTrue(set(EXPECTED_IDS).issubset(by_id))
        for question_id in EXPECTED_IDS:
            row = by_id[question_id]
            self.assertEqual(row["verification_status"], "needs_review")
            self.assertIsNone(row["checked_at"])
            self.assertIsNone(row["reviewer"])
            self.assertIsNone(row["image"])
        self.assertEqual(
            sum(row["verification_status"] == "verified" for row in self.questions),
            0,
        )

    def test_duplicate_replacements_stay_in_the_same_competency(self):
        rows = {row["id"]: row for row in self.manifest["records"]}
        for question_id, expected_competency in EXPECTED_REPLACEMENTS.items():
            record = rows[question_id]
            proposal = record["proposed_replacement"]
            self.assertIsNotNone(proposal)
            self.assertEqual(proposal["correct_option"], record["original_correct_option"])
            memberships = [
                competency
                for competency in self.competencies
                if question_id in competency["question_ids"]
            ]
            self.assertEqual(len(memberships), 1)
            self.assertEqual(memberships[0]["id"], expected_competency)
            text = proposal["stem"] + " " + " ".join(proposal["options"].values())
            self.assertNotRegex(text.lower(), r"cystern|tank")
            self.assertEqual(set(proposal["options"]), {"A", "B", "C"})
            lengths = [len(value) for value in proposal["options"].values()]
            self.assertLessEqual(max(lengths), 80)
            key_length = len(proposal["options"][proposal["correct_option"]])
            self.assertFalse(lengths.count(max(lengths)) == 1 and key_length == max(lengths))
            self.assertFalse(lengths.count(min(lengths)) == 1 and key_length == min(lengths))
            self.assertGreaterEqual(len(proposal["explanation"]), 300)
            self.assertLessEqual(len(proposal["explanation"]), 500)
            counts = sentence_word_counts(proposal["explanation"])
            self.assertGreaterEqual(len(counts), 2)
            self.assertLessEqual(len(counts), 5)
            self.assertLessEqual(max(counts), 35)
            self.assertTrue(proposal["sources"])
        self.assertEqual(
            sum(record["proposed_replacement"] is not None for record in rows.values()),
            3,
        )

    def test_automated_and_manual_duplicate_audit_is_recorded(self):
        duplicate_search = self.manifest["duplicate_search"]
        self.assertEqual(duplicate_search["scope"], "all_780_questions")
        self.assertIn("scripts/similarity.py", duplicate_search["method"])
        self.assertIn("0 kandydatów leksykalnych", duplicate_search["method"])
        self.assertTrue(duplicate_search["manual_pairs"])
        self.assertIn(
            "ADR-B-0136",
            next(row for row in self.manifest["records"] if row["id"] == "ADR-B-0471")["duplicate_candidates"],
        )
        self.assertIn(
            "ADR-B-0664",
            next(row for row in self.manifest["records"] if row["id"] == "ADR-B-0473")["duplicate_candidates"],
        )
        self.assertIn(
            "ADR-B-0436",
            next(row for row in self.manifest["records"] if row["id"] == "ADR-B-0475")["duplicate_candidates"],
        )


if __name__ == "__main__":
    unittest.main()
