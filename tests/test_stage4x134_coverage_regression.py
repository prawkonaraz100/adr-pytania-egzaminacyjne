"""Regression guard for the current 13-module ADR-basic theoretical and practical coverage.

This checks only map completeness and references; it never certifies legal correctness.
"""
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASIC = ROOT / "podstawowy"

class CurrentCoverageGate(unittest.TestCase):
    def test_theoretical_map_and_practical_scope(self):
        bank = [json.loads(line) for line in (BASIC / "questions.jsonl").read_text(encoding="utf-8").splitlines() if line.strip()]
        by_id = {row["id"]: row for row in bank}
        self.assertEqual(len(bank), 679)
        self.assertEqual(len(by_id), len(bank))
        self.assertTrue(all(row["verification_status"] == "needs_review" for row in bank))
        competencies = json.loads((BASIC / "kompetencje.json").read_text(encoding="utf-8"))["competencies"]
        self.assertEqual(len(competencies), 107)
        theoretical = [c for c in competencies if c["delivery"] == "theory"]
        practical = [c for c in competencies if c["delivery"] != "theory"]
        self.assertEqual(len(theoretical), 104)
        self.assertEqual(len(practical), 3)
        covered = set()
        for c in competencies:
            refs = c["question_ids"]
            if c["delivery"] == "theory":
                self.assertGreaterEqual(len(set(refs)), 3, c["id"])
            else:
                # These questions test prerequisites for safe decisions, not completion of the practical skill.
                self.assertGreaterEqual(len(refs), 2, f"practical objective {c['id']} needs at least two linked knowledge-prerequisite questions")
            for question_id in refs:
                self.assertIn(question_id, by_id)
                self.assertEqual(by_id[question_id]["module_id"], c["module_id"])
                covered.add(question_id)
        self.assertEqual(covered, set(by_id))
        lesson = (BASIC / "lekcje" / "ADR-B-05.md").read_text(encoding="utf-8")
        self.assertIn("nie zastępują rzeczywistego ćwiczenia", lesson)
        self.assertIn("praktycznego szkolenia z pierwszej pomocy i sprzętu gaśniczego", lesson)

    def test_three_scenarios_per_module(self):
        data = json.loads((BASIC / "praktyka" / "scenariusze-13-dzialow.json").read_text(encoding="utf-8"))
        scenarios = data["scenarios"]
        self.assertEqual(len(scenarios), 42)
        self.assertEqual(
            {module: sum(s["module_id"] == module for s in scenarios)
             for module in (f"ADR-B-{n:02}" for n in range(1, 14))},
            {**{f"ADR-B-{n:02}": 3 for n in range(1, 14)}, "ADR-B-03": 4, "ADR-B-04": 4, "ADR-B-05": 4}
        )

if __name__ == "__main__":
    unittest.main()
