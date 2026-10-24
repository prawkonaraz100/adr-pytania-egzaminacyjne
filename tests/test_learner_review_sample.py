"""Keep the deterministic 4q learner-eye sample reproducible and grounded in the bank."""
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

class LearnerReviewSampleTests(unittest.TestCase):
    def test_sample_has_five_existing_question_ids_per_module(self):
        manifest = json.loads((ROOT / "podstawowy" / "raporty" / "etap-4q-probka.json").read_text(encoding="utf-8"))
        bank = [json.loads(line) for line in (ROOT / "podstawowy" / "questions.jsonl").read_text(encoding="utf-8").splitlines() if line.strip()]
        by_id = {q["id"]: q for q in bank}
        self.assertEqual(manifest["bank_count"], len(bank))
        self.assertEqual(manifest["seed"], 202610250050)
        self.assertEqual(manifest["selection"]["per_module"], 5)
        self.assertEqual(manifest["selection"]["total"], 65)
        self.assertEqual(len(manifest["question_ids_by_module"]), 13)
        all_ids = []
        for module_id, ids in manifest["question_ids_by_module"].items():
            self.assertEqual(len(ids), 5, f"{module_id}: sample must contain five questions")
            self.assertEqual(len(set(ids)), 5, f"{module_id}: duplicate sample IDs")
            for question_id in ids:
                self.assertIn(question_id, by_id, f"sample refers to missing question {question_id}")
                self.assertEqual(by_id[question_id]["module_id"], module_id, f"{question_id}: wrong module")
            all_ids.extend(ids)
        self.assertEqual(len(all_ids), 65)
        self.assertEqual(len(set(all_ids)), 65, "sample IDs must be unique across modules")

if __name__ == "__main__":
    unittest.main()
