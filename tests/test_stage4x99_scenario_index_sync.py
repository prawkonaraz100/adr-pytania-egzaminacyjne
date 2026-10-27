"""Ensure learner, instructor and scenario indexes stay synchronized."""
import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASIC = ROOT / "podstawowy"
UPDATED = ("SC-ADR-B-02-02", "SC-ADR-B-02-03")
ID_RE = re.compile(r"ADR-B-\d{4}")


class ScenarioIndexSyncTests(unittest.TestCase):
    def test_b02_scenario_titles_and_question_ids_match_all_learning_surfaces(self):
        scenarios = json.loads(
            (BASIC / "praktyka" / "scenariusze-13-dzialow.json").read_text(encoding="utf-8")
        )["scenarios"]
        by_id = {s["id"]: s for s in scenarios}
        index = (BASIC / "praktyka" / "SCENARIUSZE.md").read_text(encoding="utf-8")
        lesson = (BASIC / "lekcje" / "ADR-B-02.md").read_text(encoding="utf-8")
        instructor = (BASIC / "instruktor" / "ADR-B-02.md").read_text(encoding="utf-8")
        tick = chr(96)
        for sid in UPDATED:
            scenario = by_id[sid]
            expected_ids = scenario["question_ids"]
            row = next(
                (line for line in index.splitlines() if f"| {tick}{sid}{tick} |" in line),
                "",
            )
            with self.subTest(scenario=sid):
                self.assertTrue(row, f"SCENARIUSZE.md has no table row for {sid}")
                self.assertIn(scenario["title"], row)
                self.assertIn(", ".join(expected_ids), row)
                self.assertIn(f"{tick}{sid}{tick} — **{scenario['title']}**", lesson)
                self.assertIn(f"{sid} — {scenario['title']}", instructor)
                heading = f"{sid} — {scenario['title']}"
                section_start = instructor.find(heading)
                self.assertGreaterEqual(section_start, 0)
                section_end = instructor.find("\n### ", section_start + len(heading))
                if section_end < 0:
                    section_end = instructor.find("\n## ", section_start + len(heading))
                section = instructor[section_start:section_end if section_end >= 0 else None]
                question_line = next(
                    (line for line in section.splitlines() if line.startswith("**Pytania powiązane:**")),
                    "",
                )
                self.assertEqual(set(ID_RE.findall(question_line)), set(expected_ids))
                self.assertEqual(len(expected_ids), len(set(expected_ids)))


if __name__ == "__main__":
    unittest.main()
