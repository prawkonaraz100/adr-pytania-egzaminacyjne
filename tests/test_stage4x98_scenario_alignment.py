"""Regression checks for scenario/question alignment found in stage 4x98."""
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASIC = ROOT / "podstawowy"


class ScenarioQuestionAlignmentTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.bank = [
            json.loads(line)
            for line in (BASIC / "questions.jsonl").read_text(encoding="utf-8").splitlines()
            if line.strip()
        ]
        cls.by_id = {q["id"]: q for q in cls.bank}
        cls.scenarios = {
            s["id"]: s
            for s in json.loads(
                (BASIC / "praktyka" / "scenariusze-13-dzialow.json").read_text(encoding="utf-8")
            )["scenarios"]
        }

    def test_unloading_scenario_names_both_classes_in_its_situation_and_links_them(self):
        scenario = self.scenarios["SC-ADR-B-02-02"]
        self.assertIn("klasy 8", scenario["situation"].lower())
        self.assertIn("klasy 4.3", scenario["situation"].lower())
        self.assertEqual(set(scenario["question_ids"]), {"ADR-B-0005", "ADR-B-0006", "ADR-B-0510"})
        self.assertIn("klas", scenario["title"].lower())
        self.assertIn("wod", " ".join(scenario["steps"]).lower())

    def test_classification_scenario_does_not_claim_packaging_group_coverage(self):
        scenario = self.scenarios["SC-ADR-B-02-03"]
        self.assertNotIn("grup", scenario["title"].lower())
        self.assertIn("benzyn", scenario["situation"].lower())
        self.assertIn("materiał żrący", scenario["situation"].lower())
        self.assertIn("klasą 4.3", scenario["situation"].lower())
        self.assertEqual(scenario["question_ids"], ["ADR-B-0004", "ADR-B-0005", "ADR-B-0006"])
        expected = {
            "ADR-B-0004": "Klasa 3",
            "ADR-B-0005": "Działanie żrące",
            "ADR-B-0006": "W kontakcie z wodą wydzielają gazy palne",
        }
        for question_id, phrase in expected.items():
            with self.subTest(question_id=question_id):
                self.assertIn(question_id, self.by_id)
                self.assertEqual(self.by_id[question_id]["module_id"], "ADR-B-02")
                self.assertIn(phrase.lower(), self.by_id[question_id]["options"][self.by_id[question_id]["correct_option"]].lower())


if __name__ == "__main__":
    unittest.main()
