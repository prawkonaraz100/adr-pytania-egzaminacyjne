"""Cross-artifact traceability for the ADR-basic learner path.

This verifies references and file alignment, not the legal correctness of their content.
"""
import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASIC = ROOT / "podstawowy"
ID_PATTERN = re.compile(r"ADR-B-\d{4}")
SCENARIO_PATTERN = re.compile(r"SC-ADR-B-\d{2}(?:-\d{2})?")


class LearningTraceabilityTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.bank = [
            json.loads(line)
            for line in (BASIC / "questions.jsonl").read_text(encoding="utf-8").splitlines()
            if line.strip()
        ]
        cls.by_id = {question["id"]: question for question in cls.bank}
        cls.scenarios = json.loads(
            (BASIC / "praktyka" / "scenariusze-13-dzialow.json").read_text(encoding="utf-8")
        )["scenarios"]
        cls.scenarios_by_module = {}
        for scenario in cls.scenarios:
            cls.scenarios_by_module.setdefault(scenario["module_id"], []).append(scenario)

    def test_lesson_and_instructor_question_ids_exist_in_their_module(self):
        for number in range(1, 14):
            module = f"ADR-B-{number:02d}"
            for kind, directory in (("lesson", "lekcje"), ("instructor", "instruktor")):
                path = BASIC / directory / f"{module}.md"
                self.assertTrue(path.is_file(), f"missing {kind}: {path}")
                content = path.read_text(encoding="utf-8")
                ids = set(ID_PATTERN.findall(content))
                self.assertTrue(ids, f"{path.name}: no question IDs")
                for question_id in ids:
                    with self.subTest(file=path.name, question_id=question_id):
                        self.assertIn(question_id, self.by_id, "question ID absent from bank")
                        self.assertEqual(
                            self.by_id[question_id]["module_id"], module,
                            "question ID belongs to a different module",
                        )

    def test_scenario_question_ids_exist_and_match_scenario_module(self):
        self.assertEqual(len(self.scenarios), 39)
        self.assertEqual(set(self.scenarios_by_module), {f"ADR-B-{n:02d}" for n in range(1, 14)})
        for module, scenarios in self.scenarios_by_module.items():
            self.assertEqual(len(scenarios), 3, f"{module}: expected exactly 3 scenarios")
            for scenario in scenarios:
                self.assertTrue(scenario.get("question_ids"), f"{scenario['id']}: no question IDs")
                for question_id in scenario["question_ids"]:
                    with self.subTest(scenario=scenario["id"], question_id=question_id):
                        self.assertIn(question_id, self.by_id, "question ID absent from bank")
                        self.assertEqual(
                            self.by_id[question_id]["module_id"], module,
                            "scenario links to a question from a different module",
                        )

    def test_mock_exam_keys_link_each_answer_to_the_matching_lesson(self):
        for number in range(1, 6):
            key_path = BASIC / "egzamin-probny" / f"klucz-{number:03d}.json"
            key = json.loads(key_path.read_text(encoding="utf-8"))
            self.assertEqual(len(key["answers"]), 30, f"{key_path.name}: expected 30 answers")
            for answer in key["answers"]:
                question_id = answer["id"]
                with self.subTest(key=key_path.name, question_id=question_id):
                    self.assertIn(question_id, self.by_id, "key ID absent from bank")
                    module = self.by_id[question_id]["module_id"]
                    expected = f"../lekcje/{module}.md"
                    self.assertEqual(answer.get("lesson_path"), expected,
                                     "key answer must link to the lesson for its bank module")
                    lesson_path = (key_path.parent / answer["lesson_path"]).resolve()
                    self.assertTrue(lesson_path.is_file(), f"lesson link target missing: {lesson_path}")
                    self.assertEqual(lesson_path.name, f"{module}.md")

    def test_each_lesson_and_instructor_links_all_three_scenarios(self):
        for number in range(1, 14):
            module = f"ADR-B-{number:02d}"
            expected = {scenario["id"] for scenario in self.scenarios_by_module[module]}
            for directory in ("lekcje", "instruktor"):
                path = BASIC / directory / f"{module}.md"
                content = path.read_text(encoding="utf-8")
                found = set(SCENARIO_PATTERN.findall(content))
                with self.subTest(file=path.name):
                    self.assertTrue(
                        expected.issubset(found),
                        f"{path.name}: missing scenario links {sorted(expected - found)}",
                    )


if __name__ == "__main__":
    unittest.main()
