"""Regression guard for the latest ADR-basic editorial snapshot and handoff."""
import hashlib
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASIC = ROOT / "podstawowy"
REPORT = BASIC / "raporty" / "etap-4x96-proba60-integracja-2026-10-27.md"
SAMPLE = BASIC / "raporty" / "etap-4x96-wykluczenia-prob.json"
MANIFEST = ROOT / "review" / "specialist" / "PAKIET-0609-MANIFEST.json"


class Stage4x97CurrentSnapshotTests(unittest.TestCase):
    def test_current_stage_is_linked_from_learner_and_specialist_indexes(self):
        learner = (BASIC / "README.md").read_text(encoding="utf-8")
        handoff = (ROOT / "review" / "specialist" / "PRZEKAZANIE-ETAP4.md").read_text(encoding="utf-8")
        review_index = (ROOT / "review" / "README.md").read_text(encoding="utf-8")
        self.assertIn("etap 4x97 (po scaleniu 4x96)", learner)
        self.assertIn("raporty/etap-4x96-proba60-integracja-2026-10-27.md", learner)
        self.assertIn("raporty/etap-4x96-wykluczenia-prob.json", learner)
        self.assertIn("Bieżąca migawka — etap 4x96", handoff)
        self.assertIn("etap-4x96-proba60-integracja-2026-10-27.md", handoff)
        self.assertIn("Bieżąca migawka — etap 4x96", review_index)
        self.assertIn("etap-4x96-proba60-integracja-2026-10-27.md", review_index)
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
        self.assertEqual(sample["source_bank_blob_sha"], bank_sha)
        self.assertEqual(manifest["current_bank_blob_sha"], bank_sha)
        self.assertEqual(len(sample["sample_ids"]), 60)
        self.assertEqual(len(set(sample["sample_ids"])), 60)
        self.assertTrue(set(sample["sample_ids"]).issubset(by_id))
        excluded = set(sample["excluded_ids"])
        self.assertTrue(set(sample["sample_ids"]).isdisjoint(excluded))
        self.assertEqual(sample["excluded_distinct_ids"], len(excluded))
        self.assertEqual(sample["candidate_pool_size"], len(bank) - len(excluded))
        self.assertIn("4x86", sample["limitation"])
        self.assertIn("cannot prove disjointness", sample["limitation"])
        self.assertEqual(len(bank), 609)
        self.assertEqual(len(by_id), 609)
        self.assertTrue(all(row["verification_status"] == "needs_review" for row in bank))
        self.assertEqual(sum(row["verification_status"] == "verified" for row in bank), 0)


if __name__ == "__main__":
    unittest.main()
