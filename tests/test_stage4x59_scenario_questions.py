import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

class ScenarioLearnerQuestionsTest(unittest.TestCase):
    def test_scenarios_are_actionable_and_reference_bank(self):
        data = json.loads((ROOT / "podstawowy/praktyka/scenariusze-13-dzialow.json").read_text(encoding="utf-8"))
        questions = [json.loads(x) for x in (ROOT / "podstawowy/questions.jsonl").read_text(encoding="utf-8").splitlines() if x.strip()]
        by_id = {q["id"]: q for q in questions}
        self.assertEqual(39, len(data["scenarios"]))
        for s in data["scenarios"]:
            with self.subTest(id=s["id"]):
                self.assertTrue(s.get("situation", "").strip())
                self.assertTrue(s.get("learner_question", "").strip().endswith("?"))
                self.assertGreaterEqual(len(s.get("steps", [])), 3)
                self.assertTrue(s.get("learner_takeaway", "").strip())
                self.assertTrue(s.get("common_mistakes"))
                self.assertTrue(s.get("legal_basis"))
                self.assertTrue(s.get("assessment_criteria"))
                self.assertTrue(s.get("question_ids"))
                for id in s["question_ids"]:
                    self.assertIn(id, by_id)
                    self.assertEqual(s["module_id"], by_id[id]["module_id"])


    def test_scenarios_do_not_all_repeat_the_same_question_set_per_module(self):
        data = json.loads((ROOT / "podstawowy/praktyka/scenariusze-13-dzialow.json").read_text(encoding="utf-8"))
        groups = {}
        for scenario in data["scenarios"]:
            groups.setdefault(scenario["module_id"], []).append(
                frozenset(scenario.get("question_ids", []))
            )
        for module, sets in groups.items():
            with self.subTest(module=module):
                self.assertEqual(len(sets), 3, f"{module}: expected exactly three scenarios")
                self.assertGreaterEqual(len(set(sets)), 2,
                    f"{module}: all three scenarios link the identical question set")

if __name__ == "__main__":
    unittest.main()
