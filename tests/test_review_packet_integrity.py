"""Integrity checks for the current ADR-basic specialist review packet.

These checks prove file/count consistency only. They do not establish legal correctness
or authorize any question as verified.
"""
import hashlib
import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASIC = ROOT / "podstawowy"
REVIEW = ROOT / "review" / "specialist"


class ReviewPacketIntegrityTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.bank = [
            json.loads(line)
            for line in (BASIC / "questions.jsonl").read_text(encoding="utf-8").splitlines()
            if line.strip()
        ]
        cls.by_id = {q["id"]: q for q in cls.bank}
        cls.manifest = json.loads((REVIEW / "PAKIET-0609-MANIFEST.json").read_text(encoding="utf-8"))
        cls.scenario_data = json.loads(
            (BASIC / "praktyka" / "scenariusze-13-dzialow.json").read_text(encoding="utf-8")
        )

    def test_manifest_matches_bank_and_module_counts(self):
        self.assertEqual(len(self.bank), 609)
        self.assertEqual(len(self.by_id), 609)
        self.assertEqual(self.manifest["question_count"], len(self.bank))
        self.assertEqual(self.manifest["last_id"], "ADR-B-0609")
        self.assertEqual(self.manifest["status_counts"]["needs_review"], 609)
        self.assertEqual(self.manifest["status_counts"]["verified"], 0)
        self.assertEqual(self.manifest["formal_approvals"], 0)
        actual = {}
        for question in self.bank:
            actual[question["module_id"]] = actual.get(question["module_id"], 0) + 1
            self.assertEqual(question["verification_status"], "needs_review")
        declared = {module: details["questions"] for module, details in self.manifest["modules"].items()}
        self.assertEqual(actual, declared)
        self.assertEqual(len(actual), 13)


    def test_current_review_guides_match_the_current_bank_snapshot(self):
        bank_bytes = (BASIC / "questions.jsonl").read_bytes()
        bank_blob_sha = hashlib.sha1(
            b"blob " + str(len(bank_bytes)).encode("ascii") + bytes([0]) + bank_bytes
        ).hexdigest()
        self.assertEqual(self.manifest["current_bank_blob_sha"], bank_blob_sha)
        current_docs = [
            REVIEW / "INSTRUKCJA-RECENZJI.md",
            REVIEW / "PRZEKAZANIE-ETAP4.md",
            REVIEW / "REJESTR-AKTUALNY-0001-0609.md",
            ROOT / "review" / "README.md",
        ]
        for path in current_docs:
            content = path.read_text(encoding="utf-8")
            with self.subTest(path=str(path.relative_to(ROOT))):
                self.assertIn(bank_blob_sha, content, "review guidance must identify current bank snapshot")
                self.assertIn("609", content, "review guidance must show current question count")
                self.assertIn("needs_review", content)
                self.assertIn("verified", content)
        handoff = (REVIEW / "PRZEKAZANIE-ETAP4.md").read_text(encoding="utf-8")
        self.assertIn("etapie 4x42", handoff.lower())
        self.assertIn("etap-4x42-scenariusze-egzaminy-2026-10-26.md", handoff)
        self.assertIn("lesson_path", handoff)

    def test_ledger_evidence_counts_match_manifest_without_implying_approval(self):
        ledger_path = ROOT / self.manifest["source_ledger"]
        ledger = json.loads(ledger_path.read_text(encoding="utf-8"))
        entries = ledger["entries"]
        self.assertEqual(len(entries), len(self.bank))
        not_retrieved = sum(
            row["official_polish_pdf_exact_section_access"] == "not_retrieved_not_literally_compared"
            for row in entries
        )
        targeted_pending = sum(
            row["official_polish_pdf_exact_section_access"] == "targeted_source_checked_full_literal_comparison_pending"
            for row in entries
        )
        targeted_results = sum(bool(row.get("literal_comparison_result")) for row in entries)
        ministry_compared = sum(
            row["official_polish_pdf_exact_section_access"].startswith(
                "textually_compared_against_full_polish_ADR_2025_text_copy_published_by_Ministry"
            )
            for row in entries
        )
        counts = self.manifest["literal_comparison_status_counts"]
        self.assertEqual(self.manifest["unresolved_literal_comparisons"], not_retrieved)
        self.assertEqual(counts["official_polish_text_not_retrieved"], not_retrieved)
        self.assertEqual(counts["targeted_source_checked_full_literal_comparison_pending"], targeted_pending)
        self.assertEqual(counts["records_with_recorded_targeted_comparison_result"], targeted_results)
        self.assertEqual(
            counts["compared_against_ministry_published_polish_copy_specialist_and_gazette_confirmation_pending"],
            ministry_compared,
        )
        self.assertEqual(counts["specialist_reviews_pending"], len(self.bank))
        self.assertEqual(counts["verified"], 0)
        self.assertEqual(sum((not_retrieved, targeted_pending, ministry_compared)), len(self.bank))
        self.assertTrue(all(row["verification_status"] == "needs_review" for row in entries))
        self.assertTrue(all(row["abc_independent_specialist_review"] == "pending" for row in entries))
        self.assertTrue(all(row["release_approved"] is False for row in entries))

    def test_specialist_index_covers_all_bank_ids(self):
        content = (REVIEW / "REJESTR-AKTUALNY-0001-0609.md").read_text(encoding="utf-8")
        indexed = set(re.findall(r"\|\s*(ADR-B-\d{4})\s*\|", content))
        self.assertEqual(indexed, set(self.by_id))

    def test_scenarios_cover_each_module_three_times(self):
        scenarios = self.scenario_data["scenarios"]
        self.assertEqual(len(scenarios), 39)
        counts = {}
        for scenario in scenarios:
            counts[scenario["module_id"]] = counts.get(scenario["module_id"], 0) + 1
        self.assertEqual(counts, {f"ADR-B-{n:02d}": 3 for n in range(1, 14)})

    def test_learner_and_instructor_artifacts_exist(self):
        for n in range(1, 14):
            self.assertTrue((BASIC / "lekcje" / f"ADR-B-{n:02d}.md").is_file())
            self.assertTrue((BASIC / "instruktor" / f"ADR-B-{n:02d}.md").is_file())
        self.assertTrue((BASIC / "SLOWNICZEK.md").is_file())
        self.assertEqual(self.manifest["artifact_counts"]["lessons"], 13)
        self.assertEqual(self.manifest["artifact_counts"]["instructor_guides"], 13)
        self.assertEqual(self.manifest["artifact_counts"]["glossary_terms"], 90)

    def test_all_five_mock_exam_variants_and_keys_exist(self):
        exams = BASIC / "egzamin-probny"
        for n in range(1, 6):
            variant_path = exams / f"wariant-{n:03d}.json"
            key_path = exams / f"klucz-{n:03d}.json"
            self.assertTrue(variant_path.is_file())
            self.assertTrue(key_path.is_file())
            variant = json.loads(variant_path.read_text(encoding="utf-8"))
            key = json.loads(key_path.read_text(encoding="utf-8"))
            self.assertEqual(variant["question_count"], 30)
            self.assertEqual(key["question_count"], 30)
            variant_ids = [q["id"] for q in variant["questions"]]
            key_ids = [q["id"] for q in key["answers"]]
            self.assertEqual(len(variant_ids), 30)
            self.assertEqual(len(set(variant_ids)), 30)
            self.assertEqual(variant_ids, key_ids)
            self.assertTrue(set(variant_ids).issubset(self.by_id))
        self.assertEqual(self.manifest["artifact_counts"]["mock_exam_variants"], 5)
        self.assertEqual(self.manifest["artifact_counts"]["mock_exam_keys"], 5)


    def test_current_snapshot_and_open_quote_list_stay_synchronized(self):
        bank_bytes = (BASIC / "questions.jsonl").read_bytes()
        blob_sha = hashlib.sha1(
            b"blob " + str(len(bank_bytes)).encode("ascii") + bytes([0]) + bank_bytes
        ).hexdigest()
        self.assertEqual(self.manifest["current_bank_blob_sha"], blob_sha)
        self.assertRegex(self.manifest["stage4x29"]["source_bank_blob_sha"], r"^[0-9a-f]{40}$")
        self.assertEqual(self.manifest["stage4x31"]["source_bank_blob_sha"], blob_sha)
        self.assertEqual(self.manifest["stage4x29"]["sample_size"], 60)
        self.assertEqual(self.manifest["stage4x29"]["key_mismatches_after_letter_remapping"], 0)

        open_items = self.manifest["specialist_open_items"]
        self.assertEqual(
            open_items["official_polish_text_not_retrieved"],
            self.manifest["unresolved_literal_comparisons"],
        )
        quote_list = REVIEW / "ETAP-4X24-POZYCJE-BEZ-CYTATU-MI.md"
        quote_text = quote_list.read_text(encoding="utf-8")
        quote_ids = re.findall(r"^- (ADR-B-\d{4})$", quote_text, flags=re.MULTILINE)
        self.assertEqual(len(quote_ids), 121)
        self.assertEqual(len(set(quote_ids)), 121)
        self.assertTrue(set(quote_ids).issubset(self.by_id))
        self.assertEqual(open_items["ministerial_copy_exact_quote_not_saved"], len(quote_ids))
        self.assertEqual(open_items["targeted_source_checked_full_literal_comparison_pending"], 10)

        self.assertTrue((BASIC / "raporty" / "etap-4x29-proba-wyjasnien-i-egzaminy-2026-10-26.md").is_file())
        exam_guide = (BASIC / "egzamin-probny" / "README.md").read_text(encoding="utf-8")
        self.assertIn("Jak interpretować wynik", exam_guide)
        review_guide = (REVIEW / "INSTRUKCJA-RECENZJI.md").read_text(encoding="utf-8")
        self.assertIn("etapach 4x25–4x29", review_guide)
        self.assertEqual(self.manifest["status_counts"]["needs_review"], 609)
        self.assertEqual(self.manifest["status_counts"]["verified"], 0)

    def test_secondary_priority_legal_review_queue_stays_synchronized(self):
        queue_path = REVIEW / "KOLEJKA-PRIORYTETOWA-4X44.json"
        queue = json.loads(queue_path.read_text(encoding="utf-8"))
        missing_quote_path = REVIEW / "ETAP-4X24-POZYCJE-BEZ-CYTATU-MI.md"
        missing_quote_text = missing_quote_path.read_text(encoding="utf-8")
        missing_quote_ids = set(re.findall(r"^- (ADR-B-\\d{4})$", missing_quote_text, flags=re.MULTILINE))
        primary = json.loads((REVIEW / "KOLEJKA-PRIORYTETOWA-4X40.json").read_text(encoding="utf-8"))
        bank_bytes = (BASIC / "questions.jsonl").read_bytes()
        bank_blob_sha = hashlib.sha1(
            b"blob " + str(len(bank_bytes)).encode("ascii") + bytes([0]) + bank_bytes
        ).hexdigest()

        self.assertEqual(queue["stage"], "4x44_secondary_priority_legal_review_queue")
        self.assertEqual(queue["source_bank_blob_sha"], bank_blob_sha)
        self.assertEqual(queue["queue_count"], 20)
        self.assertEqual(queue["full_missing_quote_count"], len(missing_quote_ids))
        self.assertEqual(len(queue["records"]), 20)
        self.assertEqual(len({row["id"] for row in queue["records"]}), 20)
        primary_ids = {row["id"] for row in primary["records"]}
        queue_ids = {row["id"] for row in queue["records"]}
        self.assertTrue(queue_ids.issubset(missing_quote_ids))
        self.assertTrue(queue_ids.isdisjoint(primary_ids))
        manifest_queue = self.manifest["secondary_priority_legal_review_queue"]
        self.assertEqual(manifest_queue["source_bank_blob_sha"], bank_blob_sha)
        self.assertEqual(manifest_queue["queue_count"], 20)
        self.assertEqual(manifest_queue["path"], "review/specialist/KOLEJKA-PRIORYTETOWA-4X44.json")
        for row in queue["records"]:
            with self.subTest(question_id=row["id"]):
                source = self.by_id.get(row["id"])
                self.assertIsNotNone(source)
                self.assertEqual(row["module_id"], source["module_id"])
                self.assertEqual(row["question"], source["stem"])
                self.assertEqual(row["legal_basis"], [s["reference"] for s in source["sources"]])
                self.assertEqual(row["verification_status"], "needs_review")
                self.assertEqual(row["official_gazette_comparison"], "pending")
                self.assertIsNone(row["official_gazette_page"])
                self.assertTrue(row["priority_reasons"])
                self.assertTrue(row["required_specialist_action"])
                self.assertTrue(row["why_not_auto_resolved"])

    def test_priority_legal_review_queue_stays_synchronized(self):
        queue_path = REVIEW / "KOLEJKA-PRIORYTETOWA-4X40.json"
        queue = json.loads(queue_path.read_text(encoding="utf-8"))
        missing_quote_path = REVIEW / "ETAP-4X24-POZYCJE-BEZ-CYTATU-MI.md"
        missing_quote_text = missing_quote_path.read_text(encoding="utf-8")
        missing_quote_ids = re.findall(r"^- (ADR-B-\d{4})$", missing_quote_text, flags=re.MULTILINE)
        bank_bytes = (BASIC / "questions.jsonl").read_bytes()
        bank_blob_sha = hashlib.sha1(
            b"blob " + str(len(bank_bytes)).encode("ascii") + bytes([0]) + bank_bytes
        ).hexdigest()

        self.assertEqual(queue["stage"], "4x40")
        self.assertEqual(queue["source_bank_blob_sha"], bank_blob_sha)
        self.assertEqual(queue["queue_count"], 20)
        self.assertEqual(queue["full_missing_quote_count"], len(missing_quote_ids))
        self.assertEqual(len(queue["records"]), queue["queue_count"])
        self.assertEqual(len({row["id"] for row in queue["records"]}), len(queue["records"]))
        self.assertTrue(set(row["id"] for row in queue["records"]).issubset(set(missing_quote_ids)))
        self.assertEqual(self.manifest["priority_legal_review_queue"]["source_bank_blob_sha"], bank_blob_sha)
        self.assertEqual(self.manifest["priority_legal_review_queue"]["queue_count"], queue["queue_count"])
        for row in queue["records"]:
            with self.subTest(question_id=row["id"]):
                source = self.by_id.get(row["id"])
                self.assertIsNotNone(source)
                self.assertEqual(row["module_id"], source["module_id"])
                self.assertEqual(row["question"], source["stem"])
                self.assertEqual(row["legal_basis"], [s["reference"] for s in source["sources"]])
                self.assertEqual(row["verification_status"], "needs_review")
                self.assertEqual(row["official_gazette_comparison"], "pending")
                self.assertIsNone(row["official_gazette_page"])
                self.assertTrue(row["priority_reasons"])
                self.assertTrue(row["required_specialist_action"])

if __name__ == "__main__":
    unittest.main()
