"""First-pass literal review for ADR-B-0571–0585; first-pass report plus second-pass deployment checks."""

import hashlib
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BANK = ROOT / "podstawowy" / "questions.jsonl"
REPORT = ROOT / "review" / "literal-pl" / "PARTIA-0571-0585.md"
MANIFEST = ROOT / "review" / "literal-pl" / "PARTIA-0571-0585.json"
FIRST_PASS_BANK_SHA = "b240a96d8c9d0bae561d132b0a6bc8f705ee7ca2"
EXPECTED_BANK_SHA = "7c6b46d4134301f616cfc39d2b3e33e4318da428"
EXPECTED_IDS = [f"ADR-B-{i:04d}" for i in range(571, 586)]
EXPECTED_PAGES = {
    "ADR-B-0571": [28], "ADR-B-0572": [690, 691, 692, 693],
    "ADR-B-0573": [693], "ADR-B-0574": [1338], "ADR-B-0575": [1338],
    "ADR-B-0576": [1338, 1339], "ADR-B-0577": [961], "ADR-B-0578": [962],
    "ADR-B-0579": [962], "ADR-B-0580": [1333, 1334], "ADR-B-0581": [1333, 1334],
    "ADR-B-0582": [113], "ADR-B-0583": [57], "ADR-B-0584": [57], "ADR-B-0585": [1325],
}
EXPECTED_COUNTS = {"OK": 8, "POPRAW": 7, "BLOKUJ": 0}


def git_blob_sha(data: bytes) -> str:
    header = b"blob " + str(len(data)).encode("ascii") + b"\0"
    return hashlib.sha1(header + data).hexdigest()


class Partia39LiteralReview(unittest.TestCase):
    def test_report_scope_counts_pages_and_quotes(self):
        self.assertTrue(REPORT.is_file())
        manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
        self.assertEqual(manifest["scope"], "first_pass_literal_review")
        self.assertEqual(manifest["batch"], "ADR-B-0571–0585")
        self.assertEqual(manifest["bank_count"], 780)
        self.assertEqual(manifest["bank_blob_sha"], FIRST_PASS_BANK_SHA)
        self.assertFalse(manifest["bank_changed"])
        self.assertEqual(manifest["previous_uncompared"], 210)
        self.assertEqual(manifest["compared"], 15)
        self.assertEqual(manifest["remaining_without_comparison"], 195)
        self.assertEqual(manifest["counts"], EXPECTED_COUNTS)
        self.assertEqual([row["id"] for row in manifest["records"]], EXPECTED_IDS)
        self.assertEqual({row["id"]: row["gazette_pages"] for row in manifest["records"]}, EXPECTED_PAGES)
        self.assertTrue(all(row["exact_quote"] and row["legal_basis"] and row["gazette_pages"] for row in manifest["records"]))
        self.assertTrue(all(row["verification_status"] == "needs_review" for row in manifest["records"]))
        self.assertEqual(manifest["verified"], 0)
        self.assertTrue(manifest["duplicate_search"]["manual_duplicate_pairs"])
        self.assertEqual(manifest["duplicate_search"]["threshold_0_45_pairs"], 0)
        self.assertEqual(manifest["duplicate_search"]["threshold_0_25_pairs"], 5)

    def test_bank_after_second_pass_and_records_remain_unverified(self):
        raw = BANK.read_bytes()
        self.assertEqual(git_blob_sha(raw), EXPECTED_BANK_SHA)
        questions = [json.loads(line) for line in raw.decode("utf-8").splitlines() if line.strip()]
        self.assertEqual(len(questions), 780)
        by_id = {row["id"]: row for row in questions}
        for question_id in EXPECTED_IDS:
            self.assertEqual(by_id[question_id]["verification_status"], "needs_review")
            self.assertIsNone(by_id[question_id]["checked_at"])
            self.assertIsNone(by_id[question_id]["reviewer"])


    def test_second_pass_corrections_file(self):
        corrections = ROOT / "review" / "literal-pl" / "POPRAWKI-KONTROLA2-0571-0585.jsonl"
        second_pass = ROOT / "review" / "literal-pl" / "KONTROLA2-PARTIA-0571-0585.md"
        self.assertTrue(second_pass.is_file())
        records = [json.loads(line) for line in corrections.read_text(encoding="utf-8").splitlines() if line.strip()]
        self.assertEqual(len(records), 15)
        self.assertEqual([row["id"] for row in records], EXPECTED_IDS)


if __name__ == "__main__":
    unittest.main()
