"""First-pass literal review for ADR-B-0571–0585; report-only; bank must remain unchanged."""

import hashlib
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BANK = ROOT / "podstawowy" / "questions.jsonl"
REPORT = ROOT / "review" / "literal-pl" / "PARTIA-0571-0585.md"
MANIFEST = ROOT / "review" / "literal-pl" / "PARTIA-0571-0585.json"
FIRST_PASS_BANK_SHA = "b240a96d8c9d0bae561d132b0a6bc8f705ee7ca2"
EXPECTED_BANK_SHA = "b240a96d8c9d0bae561d132b0a6bc8f705ee7ca2"
EXPECTED_IDS = [f"ADR-B-{i:04d}" for i in range(571, 586)]
EXPECTED_PAGES = {
    "ADR-B-0571": [28], "ADR-B-0572": [690, 691, 692, 693],
    "ADR-B-0573": [693], "ADR-B-0574": [1338], "ADR-B-0575": [1338],
    "ADR-B-0576": [1338, 1339], "ADR-B-0577": [962], "ADR-B-0578": [962],
    "ADR-B-0579": [962], "ADR-B-0580": [1333, 1334], "ADR-B-0581": [1333, 1334],
    "ADR-B-0582": [113], "ADR-B-0583": [57], "ADR-B-0584": [57], "ADR-B-0585": [1325],
}
EXPECTED_COUNTS = {"OK": 6, "POPRAW": 9, "BLOKUJ": 0}


def git_blob_sha(data: bytes) -> str:
    header = b"blob " + str(len(data)).encode("ascii") + b"\\0"
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

    def test_bank_is_unchanged_and_records_remain_unverified(self):
        raw = BANK.read_bytes()
        self.assertEqual(git_blob_sha(raw), EXPECTED_BANK_SHA)
        questions = [json.loads(line) for line in raw.decode("utf-8").splitlines() if line.strip()]
        self.assertEqual(len(questions), 780)
        by_id = {row["id"]: row for row in questions}
        for question_id in EXPECTED_IDS:
            self.assertEqual(by_id[question_id]["verification_status"], "needs_review")
            self.assertIsNone(by_id[question_id]["checked_at"])
            self.assertIsNone(by_id[question_id]["reviewer"])


if __name__ == "__main__":
    unittest.main()
