"""Blocking Stage 4v regression tests: answer-length and lexical shortcuts per module.

These are editorial heuristics, not an independent verification of ADR law.
"""
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from answer_leakage_metrics import measure


class Stage4vLeakageGate(unittest.TestCase):
    def test_shortest_and_absolute_rates_per_module(self):
        path = ROOT / "podstawowy" / "questions.jsonl"
        questions = [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]
        stats = measure(questions)
        self.assertEqual(len(stats), 13, "Expected 13 modules in ADR basic course")
        for module, g in stats.items():
            with self.subTest(module=module, metric="strictly shortest"):
                self.assertGreater(g["questions"], 0)
                self.assertLessEqual(
                    100 * g["shortest"], 38 * g["questions"],
                    f"{module}: shortest answer cue {g['shortest']}/{g['questions']} exceeds 38%"
                )
            with self.subTest(module=module, metric="absolute words in wrong options"):
                self.assertEqual(g["wrong_options"], 2 * g["questions"])
                self.assertLessEqual(
                    100 * g["wrong_abs"], 38 * g["wrong_options"],
                    f"{module}: wrong-option absolute words {g['wrong_abs']}/{g['wrong_options']} exceeds 38%"
                )
            with self.subTest(module=module, metric="strictly longest"):
                self.assertLessEqual(
                    100 * g["longest"], 18 * g["questions"],
                    f"{module}: longest answer cue {g['longest']}/{g['questions']} exceeds 18%"
                )

    def test_measure_detects_shortest_and_absolute_cues(self):
        synthetic = [{
            "module_id": "ADR-B-01",
            "options": {
                "A": "Poprawna",
                "B": "Ta odpowiedź zawsze nie działa",
                "C": "Ta odpowiedź nie działa w tym przypadku",
            },
            "correct_option": "A",
        }]
        g = measure(synthetic)["ADR-B-01"]
        self.assertEqual(g["questions"], 1)
        self.assertEqual(g["shortest"], 1)
        self.assertEqual(g["wrong_abs"], 1)
        self.assertEqual(g["only_wrong_abs"], 1)


if __name__ == "__main__":
    unittest.main()
