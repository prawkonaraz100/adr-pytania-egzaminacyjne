"""First-pass literal review tests for ADR-B-0601–0615; first-pass report plus second-pass deployment checks."""

import hashlib
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BANK = ROOT / "podstawowy" / "questions.jsonl"
REPORT = ROOT / "review" / "literal-pl" / "PARTIA-0601-0615.md"
MANIFEST = ROOT / "review" / "literal-pl" / "PARTIA-0601-0615.json"
FIRST_PASS_BANK_SHA = "6147aeb45bf0efd1631ae17ce5e1d82357bffb0b"
EXPECTED_BANK_SHA = "ff06e555f833fa3f679c7c145c1223395ae923db"
EXPECTED_IDS = [f"ADR-B-{i:04d}" for i in range(601, 616)]
EXPECTED_PAGES = {
    "ADR-B-0601": [29, 965], "ADR-B-0602": [1338, 1339],
    "ADR-B-0603": [1338], "ADR-B-0604": [1339], "ADR-B-0605": [686],
    "ADR-B-0606": [25, 28], "ADR-B-0607": [1326], "ADR-B-0608": [119],
    "ADR-B-0609": [687], "ADR-B-0610": [308], "ADR-B-0611": [171, 182],
    "ADR-B-0612": [975], "ADR-B-0613": [975], "ADR-B-0614": [975],
    "ADR-B-0615": [956],
}
EXPECTED_COUNTS = {"OK": 2, "POPRAW": 13, "BLOKUJ": 0}


def git_blob_sha(data: bytes) -> str:
    return hashlib.sha1(b"blob " + str(len(data)).encode("ascii") + b"\0" + data).hexdigest()


class Partia41LiteralReview(unittest.TestCase):
    def test_report_scope_counts_pages_and_quotes(self):
        self.assertTrue(REPORT.is_file())
        manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
        self.assertEqual(manifest["scope"], "first_pass_literal_review")
        self.assertEqual(manifest["batch"], "ADR-B-0601–0615")
        self.assertEqual(manifest["bank_count"], 780)
        self.assertEqual(manifest["bank_blob_sha"], FIRST_PASS_BANK_SHA)
        self.assertFalse(manifest["bank_changed"])
        self.assertEqual(manifest["previous_uncompared"], 180)
        self.assertEqual(manifest["compared"], 15)
        self.assertEqual(manifest["remaining_without_comparison"], 165)
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
        self.assertEqual(manifest["duplicate_search"]["threshold_0_45_pairs"], 0)
        self.assertEqual(manifest["duplicate_search"]["threshold_0_25_pairs"], 6)
        self.assertTrue(manifest["duplicate_search"]["manual_duplicate_pairs"])
        for row in manifest["records"]:
            if row["verdict"] == "POPRAW":
                self.assertTrue(row.get("proposed_replacement"))

    def test_bank_after_second_pass_and_batch_records_remain_unverified(self):
        raw = BANK.read_bytes()
        self.assertEqual(git_blob_sha(raw), EXPECTED_BANK_SHA)
        questions = [json.loads(line) for line in raw.decode("utf-8").splitlines() if line.strip()]
        self.assertEqual(len(questions), 780)
        by_id = {row["id"]: row for row in questions}
        self.assertEqual(len(by_id), 780)
        for question_id in EXPECTED_IDS:
            self.assertEqual(by_id[question_id]["verification_status"], "needs_review")
            self.assertIsNone(by_id[question_id]["checked_at"])
            self.assertIsNone(by_id[question_id]["reviewer"])



    def test_second_pass_artifacts_and_bank_sha(self):
        second_pass = ROOT / "review" / "literal-pl" / "KONTROLA2-PARTIA-0601-0615.md"
        corrections = ROOT / "review" / "literal-pl" / "POPRAWKI-KONTROLA2-0601-0615.jsonl"
        self.assertTrue(second_pass.is_file())
        lines = [line for line in corrections.read_text(encoding="utf-8").splitlines() if line.strip()]
        self.assertEqual(len(lines), 15)
        records = [json.loads(line) for line in lines]
        self.assertEqual([row["id"] for row in records], EXPECTED_IDS)
        self.assertEqual(git_blob_sha(BANK.read_bytes()), EXPECTED_BANK_SHA)

if __name__ == "__main__":
    unittest.main()
