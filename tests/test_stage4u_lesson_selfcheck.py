"""Stage 4u regression checks: lesson self-check and mock exam variant 003."""
import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

class Stage4uSelfCheckTests(unittest.TestCase):
    def test_all_lessons_link_valid_questions_and_scenarios(self):
        bank = {q["id"]: q for ln in (ROOT/"podstawowy/questions.jsonl").read_text(encoding="utf-8").splitlines() if ln.strip() for q in [json.loads(ln)]}
        scenarios = {s["id"]: s for s in json.loads((ROOT/"podstawowy/praktyka/scenariusze-13-dzialow.json").read_text(encoding="utf-8"))["scenarios"]}
        for i in range(1, 14):
            module = f"ADR-B-{i:02d}"
            contents = (ROOT/"podstawowy/lekcje"/f"{module}.md").read_text(encoding="utf-8")
            self.assertEqual(contents.count("## Sprawdź się"), 1, module)
            section = contents.split("## Sprawdź się", 1)[1]
            ids = re.findall(r"^- `(ADR-B-[0-9]{4})`$", section, re.M)
            self.assertTrue(5 <= len(ids) <= 10, module)
            self.assertEqual(len(ids), len(set(ids)), module)
            for qid in ids:
                self.assertIn(qid, bank, module)
                self.assertEqual(bank[qid]["module_id"], module, qid)
            sid = "SC-" + module
            self.assertIn(sid, scenarios)
            self.assertEqual(scenarios[sid]["module_id"], module)
            self.assertIn(sid, section)
            self.assertIn("../praktyka/scenariusze-13-dzialow.json", section)

    def test_variant_003_ids_answer_key_and_no_overlap(self):
        base = ROOT/"podstawowy/egzamin-probny"
        variants = [json.loads((base/f"wariant-{i:03d}.json").read_text(encoding="utf-8")) for i in (1, 2, 3)]
        key = json.loads((base/"klucz-003.json").read_text(encoding="utf-8"))
        bank = {q["id"]: q for ln in (ROOT/"podstawowy/questions.jsonl").read_text(encoding="utf-8").splitlines() if ln.strip() for q in [json.loads(ln)]}
        sets = [{q["id"] for q in v["questions"]} for v in variants]
        self.assertEqual(len(sets[2]), 30)
        self.assertFalse(sets[0] & sets[2])
        self.assertFalse(sets[1] & sets[2])
        self.assertEqual({q["module_id"] for q in variants[2]["questions"]}, {f"ADR-B-{i:02d}" for i in range(1,14)})
        self.assertEqual([q["id"] for q in variants[2]["questions"]], [a["id"] for a in key["answers"]])
        self.assertEqual(variants[2]["pass_mark_correct"], 20)
        self.assertFalse(variants[2]["publication_authorized"])
        for q in variants[2]["questions"]:
            self.assertIn(q["id"], bank)
            self.assertEqual(q["module_id"], bank[q["id"]]["module_id"])
            self.assertEqual(q["options"], bank[q["id"]]["options"])
        for a in key["answers"]:
            self.assertEqual(a["correct_option"], bank[a["id"]]["correct_option"])
            self.assertEqual(a["explanation"], bank[a["id"]]["explanation"])

if __name__ == "__main__":
    unittest.main()
