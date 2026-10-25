"""Integrity checks for the current ADR-basic specialist review packet.

These checks prove file/count consistency only. They do not establish legal correctness
or authorize any question as verified.
"""
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


if __name__ == "__main__":
    unittest.main()
