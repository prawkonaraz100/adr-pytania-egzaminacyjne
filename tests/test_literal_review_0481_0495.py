"""First-pass literal review for ADR-B-0481–0495; report-only, with the bank unchanged."""

import hashlib
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BANK = ROOT / "podstawowy" / "questions.jsonl"
REPORT = ROOT / "review" / "literal-pl" / "PARTIA-0481-0495.md"
MANIFEST = ROOT / "review" / "literal-pl" / "PARTIA-0481-0495.json"
FIRST_PASS_BANK_SHA = "ba829d36bc7e1c04aeab108d826bfae33938422f"
EXPECTED_BANK_SHA = "f2cea3f46167e3f99d4c5c7b91658744eba1d8c7"
EXPECTED_IDS = [f"ADR-B-{i:04d}" for i in range(481, 496)]
EXPECTED_PAGES = {
    "ADR-B-0481": "59",
    "ADR-B-0482": "57",
    "ADR-B-0483": "1325",
    "ADR-B-0484": "1325",
    "ADR-B-0485": "1325",
    "ADR-B-0486": "1325",
    "ADR-B-0487": "1339",
    "ADR-B-0488": "1339",
    "ADR-B-0489": "1339",
    "ADR-B-0490": "1339",
    "ADR-B-0491": "1305",
    "ADR-B-0492": "1305",
    "ADR-B-0493": "975",
    "ADR-B-0494": "975",
    "ADR-B-0495": "129",
}
EXPECTED_COUNTS = {"OK": 2, "POPRAW": 13, "BLOKUJ": 0}
EXPECTED_PAGES_ALL = {
    "ADR-B-0481": [59], "ADR-B-0482": [57], "ADR-B-0483": [1325],
    "ADR-B-0484": [1325], "ADR-B-0485": [1325], "ADR-B-0486": [1325],
    "ADR-B-0487": [1339], "ADR-B-0488": [1339], "ADR-B-0489": [1339],
    "ADR-B-0490": [1339], "ADR-B-0491": [1305, 1306],
    "ADR-B-0492": [1305, 972], "ADR-B-0493": [975],
    "ADR-B-0494": [975], "ADR-B-0495": [129],
}


def git_blob_sha(data: bytes) -> str:
    header = b"blob " + str(len(data)).encode("ascii") + b"\0"
    return hashlib.sha1(header + data).hexdigest()


class Partia33LiteralReview(unittest.TestCase):
    def test_report_scope_counts_and_printed_page_headers(self):
        self.assertTrue(REPORT.is_file())
        manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
        self.assertEqual(manifest["scope"], "first_pass_literal_review")
        self.assertEqual(manifest["batch"], "ADR-B-0481–0495")
        self.assertEqual(manifest["bank_count"], 780)
        self.assertEqual(manifest["bank_blob_sha"], FIRST_PASS_BANK_SHA)
        self.assertFalse(manifest["bank_changed"])
        self.assertEqual(manifest["previous_uncompared"], 300)
        self.assertEqual(manifest["compared"], 15)
        self.assertEqual(manifest["remaining_without_comparison"], 285)
        self.assertEqual(manifest["counts"], EXPECTED_COUNTS)
        self.assertEqual([row["id"] for row in manifest["records"]], EXPECTED_IDS)
        self.assertEqual(
            {row["id"]: str(row["gazette_page"]) for row in manifest["records"]},
            EXPECTED_PAGES,
        )
        self.assertEqual({row["id"]: row["gazette_pages"] for row in manifest["records"]}, EXPECTED_PAGES_ALL)
        self.assertTrue(all(row["verification_status"] == "needs_review" for row in manifest["records"]))
        self.assertEqual(manifest["verified"], 0)

    def test_bank_is_unchanged_and_all_batch_questions_remain_unverified(self):
        raw = BANK.read_bytes()
        self.assertEqual(git_blob_sha(raw), EXPECTED_BANK_SHA)
        questions = [json.loads(line) for line in raw.decode("utf-8").splitlines() if line.strip()]
        self.assertEqual(len(questions), 780)
        by_id = {row["id"]: row for row in questions}
        self.assertTrue(set(EXPECTED_IDS).issubset(by_id))
        for question_id in EXPECTED_IDS:
            row = by_id[question_id]
            self.assertEqual(row["verification_status"], "needs_review")
            self.assertIsNone(row["checked_at"])
            self.assertIsNone(row["reviewer"])
            self.assertIsNone(row["image"])
        self.assertEqual(sum(row["verification_status"] == "verified" for row in questions), 0)

    def test_duplicate_candidates_are_recorded_without_claiming_lexical_certainty(self):
        manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
        self.assertEqual(manifest["duplicate_search"]["threshold_0_45_pairs"], 0)
        self.assertEqual(manifest["duplicate_search"]["threshold_0_25_pairs"], 2)
        rows = {row["id"]: row for row in manifest["records"]}
        self.assertEqual(rows["ADR-B-0487"]["duplicate_candidates"], ["ADR-B-0033", "ADR-B-0576"])
        self.assertEqual(rows["ADR-B-0493"]["duplicate_candidates"], ["ADR-B-0108", "ADR-B-0184"])
        self.assertEqual(rows["ADR-B-0494"]["duplicate_candidates"], ["ADR-B-0163"])

    def test_no_bank_or_exam_artifacts_are_in_scope(self):
        manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
        self.assertFalse(manifest["bank_changed"])
        self.assertEqual(manifest["bank_blob_sha"], EXPECTED_BANK_SHA)
        self.assertEqual(len(manifest["records"]), 15)


if __name__ == "__main__":
    unittest.main()
