"""Regression guard for the latest ADR-basic editorial snapshot and handoff."""
import hashlib
import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASIC = ROOT / "podstawowy"
REPORT = BASIC / "raporty" / "etap-4x136-poglebienie-kompetencji-0629-0638-2026-10-29.md"
SAMPLE = BASIC / "raporty" / "etap-4x135-wykluczenia-proby.json"
MANIFEST = ROOT / "review" / "specialist" / "PAKIET-0628-MANIFEST.json"


class CurrentSnapshotTests(unittest.TestCase):
    def test_current_stage_is_linked_from_learner_and_specialist_indexes(self):
        learner = (BASIC / "README.md").read_text(encoding="utf-8")
        handoff = (ROOT / "review" / "specialist" / "PRZEKAZANIE-ETAP4.md").read_text(encoding="utf-8")
        review_index = (ROOT / "review" / "README.md").read_text(encoding="utf-8")
        status = re.search(r"\*\*Stan na [^,]+, etap (4x\d+)", learner)
        self.assertIsNotNone(status)
        stage = status.group(1)
        self.assertIn(f"Bieżąca migawka — etap {stage}", handoff)
        self.assertIn(f"Bieżąca migawka — etap {stage}", review_index)
        reports_section = learner.split("## Raporty jakości", 1)[1]
        first_link = re.search(r"- \[Etap (4x\d+) — [^\]]+\]\(raporty/([^)]+)\)", reports_section)
        self.assertIsNotNone(first_link)
        self.assertEqual(first_link.group(1), stage)
        current_report = first_link.group(2)
        self.assertTrue((BASIC / "raporty" / current_report).is_file())
        self.assertIn(current_report, handoff)
        self.assertIn(current_report, review_index)
        self.assertIn("raporty/etap-4x108-proba40-dystraktory-regresja-2026-10-28.md", learner)
        self.assertIn("raporty/etap-4x108-wykluczenia-proby.json", learner)
        self.assertIn("raporty/etap-4x107-wykluczenia-proby.json", learner)
        self.assertTrue(REPORT.is_file())
        self.assertTrue(SAMPLE.is_file())

    def test_sample_manifest_is_reproducible_and_honest_about_limits(self):
        bank_bytes = (BASIC / "questions.jsonl").read_bytes()
        bank_sha = hashlib.sha1(
            b"blob " + str(len(bank_bytes)).encode("ascii") + bytes([0]) + bank_bytes
        ).hexdigest()
        bank = [json.loads(line) for line in bank_bytes.decode("utf-8").splitlines() if line.strip()]
        by_id = {row["id"]: row for row in bank}
        sample = json.loads(SAMPLE.read_text(encoding="utf-8"))
        manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
        self.assertEqual(sample["selection_source_bank_blob_sha"], "9fa7e964d86b0bd0c38f97a80b5965777d69d7da")
        self.assertEqual(sample["updated_bank_blob_sha"], bank_sha)
        self.assertEqual(manifest["current_bank_blob_sha"], bank_sha)
        self.assertEqual(len(sample["sample_ids"]), sample["sample_count"])
        self.assertEqual(len(set(sample["sample_ids"])), sample["sample_count"])
        self.assertTrue(set(sample["sample_ids"]).issubset(by_id))
        excluded = set(sample["excluded_ids"])
        self.assertTrue(set(sample["sample_ids"]).isdisjoint(excluded))
        self.assertEqual(sample["excluded_distinct_ids"], len(excluded))
        self.assertLessEqual(sample["candidate_pool_size"], len(bank) - len(excluded))
        self.assertIn("4x103–4x113", sample["limitation"])
        self.assertIn("nakładanie jest jawnie opisane", sample["limitation"])
        self.assertLessEqual(sample["sample_count"], sample["candidate_pool_size"])
        self.assertEqual(len(bank), 689)
        self.assertEqual(len(by_id), 689)
        self.assertTrue(all(row["verification_status"] == "needs_review" for row in bank))
        self.assertEqual(sum(row["verification_status"] == "verified" for row in bank), 0)


if __name__ == "__main__":
    unittest.main()
