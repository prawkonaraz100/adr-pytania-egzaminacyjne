"""First-pass literal review tests for ADR-B-0616–0630."""

import hashlib
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BANK = ROOT / "podstawowy" / "questions.jsonl"
REPORT = ROOT / "review" / "literal-pl" / "PARTIA-0616-0630.md"
MANIFEST = ROOT / "review" / "literal-pl" / "PARTIA-0616-0630.json"
FIRST_PASS_BANK_SHA = "7c6b46d4134301f616cfc39d2b3e33e4318da428"
EXPECTED_BANK_SHA = "7c6b46d4134301f616cfc39d2b3e33e4318da428"
EXPECTED_IDS = [f"ADR-B-{i:04d}" for i in range(616, 631)]
EXPECTED_PAGES = {
    "ADR-B-0616": [955, 961], "ADR-B-0617": [939],
    "ADR-B-0618": [1308, 1309], "ADR-B-0619": [1330],
    "ADR-B-0620": [974], "ADR-B-0621": [182],
    "ADR-B-0622": [196], "ADR-B-0623": [214],
    "ADR-B-0624": [234], "ADR-B-0625": [264],
    "ADR-B-0626": [975], "ADR-B-0627": [939],
    "ADR-B-0628": [1308], "ADR-B-0629": [962],
    "ADR-B-0630": [975],
}
EXPECTED_COUNTS = {"OK": 5, "POPRAW": 10, "BLOKUJ": 0}


def git_blob_sha(data: bytes) -> str:
    return hashlib.sha1(b"blob " + str(len(data)).encode("ascii") + b"\\0" + data).hexdigest()


class Partia42LiteralReview(unittest.TestCase):
    def test_report_scope_counts_pages_and_quotes(self):
        self.assertTrue(REPORT.is_file())
        manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
        self.assertEqual(manifest["scope"], "first_pass_literal_review")
        self.assertEqual(manifest["batch"], "ADR-B-0616–0630")
        self.assertEqual(manifest["bank_count"], 780)
        self.assertEqual(manifest["bank_blob_sha"], FIRST_PASS_BANK_SHA)
        self.assertFalse(manifest["bank_changed"])
        self.assertEqual(manifest["previous_uncompared"], 165)
        self.assertEqual(manifest["compared"], 15)
        self.assertEqual(manifest["remaining_without_comparison"], 150)
        self.assertEqual(manifest["counts"], EXPECTED_COUNTS)
        verdict_counts = {
            key: sum(row["verdict"] == key for row in manifest["records"])
            for key in ("OK", "POPRAW", "BLOKUJ")
        }
        self.assertEqual(verdict_counts, EXPECTED_COUNTS)
        self.assertEqual([row["id"] for row in manifest["records"]], EXPECTED_IDS)
        self.assertEqual(
            {row["id"]: row["gazette_pages"] for row in manifest["records"]},
            EXPECTED_PAGES,
        )
        self.assertTrue(all(row["exact_quote"] and row["legal_basis"] for row in manifest["records"]))
        self.assertTrue(all(row["verification_status"] == "needs_review" for row in manifest["records"]))
        self.assertEqual(manifest["verified"], 0)
        self.assertEqual(manifest["duplicate_search"]["threshold_0_45_pairs"], 1)
        self.assertEqual(manifest["duplicate_search"]["threshold_0_25_pairs"], 11)
        self.assertTrue(manifest["duplicate_search"]["manual_duplicate_pairs"])
        for row in manifest["records"]:
            if row["verdict"] == "POPRAW":
                self.assertTrue(row.get("proposed_replacement") or row.get("reason_no_safe_candidate"))

    def test_bank_is_unchanged_and_batch_records_remain_unverified(self):
        raw = BANK.read_bytes()
        self.assertEqual(git_blob_sha(raw), FIRST_PASS_BANK_SHA)
        self.assertEqual(git_blob_sha(raw), EXPECTED_BANK_SHA)
        questions = [json.loads(line) for line in raw.decode("utf-8").splitlines() if line.strip()]
        self.assertEqual(len(questions), 780)
        by_id = {row["id"]: row for row in questions}
        self.assertEqual(len(by_id), 780)
        for question_id in EXPECTED_IDS:
            self.assertEqual(by_id[question_id]["verification_status"], "needs_review")
            self.assertIsNone(by_id[question_id]["checked_at"])
            self.assertIsNone(by_id[question_id]["reviewer"])


if __name__ == "__main__":
    unittest.main()
