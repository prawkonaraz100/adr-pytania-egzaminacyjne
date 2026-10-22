"""Regression checks for first 30-question ADR risk-review batch.

These checks confirm bookkeeping and previously identified drafting traps.
They are NOT legal verification or professional ADR attestation.
"""
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load_questions():
    path = ROOT / "podstawowy" / "questions.jsonl"
    return {q["id"]: q for q in (
        json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()
    )}


def load_review():
    return json.loads((ROOT / "review" / "batches" / "risk-001.json").read_text(encoding="utf-8"))


class RiskReviewBatchTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.questions = load_questions()
        cls.audit = load_review()

    def test_exactly_30_unique_reviewed_ids_with_existing_questions(self):
        records = self.audit["records"]
        self.assertEqual(len(records), 30)
        ids = [q["id"] for q in records]
        self.assertEqual(len(set(ids)), 30)
        self.assertTrue(set(ids).issubset(self.questions))

    def test_review_does_not_fabricate_approvals(self):
        self.assertEqual(self.audit["status"], "needs_expert")
        for record in self.audit["records"]:
            with self.subTest(id=record["id"]):
                self.assertEqual(record["verification_status"], "needs_review")
                self.assertIs(record["expert_signoff"], False)
                self.assertEqual(self.questions[record["id"]]["verification_status"], "needs_review")
                self.assertTrue(record["legal_refs"].strip())
                self.assertTrue(record["source_url"].startswith("https://"))
                self.assertTrue(record["next_step"].strip())
        self.assertEqual((ROOT / "review" / "approvals.jsonl").read_text(encoding="utf-8").strip(), "")

    def test_minimum_extinguisher_question_no_longer_claims_six_kg_is_invalid(self):
        q = self.questions["ADR-B-0073"]
        self.assertIn("minimalna", q["stem"].lower())
        self.assertEqual(q["correct_option"], "B")
        self.assertIn("2 kg", q["options"]["B"])
        self.assertIn("nie jest wymaganym minimum", q["explanation"])

    def test_bulk_authorization_includes_specific_paragraph_ref(self):
        q = self.questions["ADR-B-0139"]
        answer = q["options"][q["correct_option"]]
        self.assertIn("BK", answer)
        self.assertIn("VC", answer)
        self.assertIn("odesłanie", answer)
        self.assertIn("7.3.2", q["explanation"])
        self.assertIn("7.3.3", q["explanation"])

    def test_container_certificate_question_excludes_tank_container(self):
        q = self.questions["ADR-B-0140"]
        self.assertIn("nie kontener-cysterna", q["stem"])
        self.assertIn("kontenerów-cystern", q["explanation"])

    def test_class_7_training_exceptions_not_hidden(self):
        q = self.questions["ADR-B-0160"]
        self.assertIn("S12", q["explanation"])
        self.assertIn("S12", q["sources"][0]["reference"])

    def test_risk_review_markdown_exists(self):
        text = (ROOT / "review" / "batches" / "risk-001.md").read_text(encoding="utf-8")
        self.assertIn("NIE ZATWIERDZENIE EKSPERCKIE", text)
        for row in self.audit["records"]:
            self.assertIn(row["id"], text)


if __name__ == "__main__":
    unittest.main()
