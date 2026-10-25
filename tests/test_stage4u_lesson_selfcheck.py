"""Stage 4u regression checks: lesson self-check and mock exam variant 003."""
import json
import re
import sys
import unittest
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from check_mock_exam_variants import remap_explanation

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

    def test_all_mock_exam_variants_and_keys_match_live_bank(self):
        base = ROOT/"podstawowy/egzamin-probny"
        bank = {q["id"]: q for ln in (ROOT/"podstawowy/questions.jsonl").read_text(encoding="utf-8").splitlines() if ln.strip() for q in [json.loads(ln)]}
        seen = set()
        for number in range(1, 6):
            variant = json.loads((base/f"wariant-{number:03d}.json").read_text(encoding="utf-8"))
            key = json.loads((base/f"klucz-{number:03d}.json").read_text(encoding="utf-8"))
            questions = variant["questions"]
            answers = key["answers"]
            ids = [q["id"] for q in questions]
            self.assertEqual(len(ids), 30, f"variant {number}")
            self.assertEqual(len(set(ids)), 30, f"duplicate IDs in variant {number}")
            self.assertFalse(seen.intersection(ids), f"cross-variant overlap in variant {number}")
            seen.update(ids)
            self.assertEqual([q["number"] for q in questions], list(range(1, 31)))
            self.assertEqual([q["id"] for q in questions], [a["id"] for a in answers])
            self.assertEqual([a["number"] for a in answers], list(range(1, 31)))
            self.assertEqual({q["module_id"] for q in questions}, {f"ADR-B-{i:02d}" for i in range(1, 14)})
            self.assertEqual(sum(variant["module_distribution"].values()), 30)
            self.assertEqual(variant["pass_mark_correct"], 20)
            self.assertFalse(variant["publication_authorized"])
            self.assertFalse(key["publication_authorized"])
            paper_by_id = {q["id"]: q for q in questions}
            for q in questions:
                self.assertIn(q["id"], bank)
                source = bank[q["id"]]
                self.assertEqual(q["module_id"], source["module_id"])
                self.assertEqual(q["stem"], source["stem"])
                self.assertEqual(Counter(q["options"].values()), Counter(source["options"].values()))
            for answer in answers:
                source = bank[answer["id"]]
                paper = paper_by_id[answer["id"]]
                mapping = {old: next(new for new in "ABC" if paper["options"][new] == source["options"][old]) for old in "ABC"}
                self.assertEqual(paper["options"][answer["correct_option"]], source["options"][source["correct_option"]])
                self.assertEqual(answer["explanation"], remap_explanation(source["explanation"], mapping))
                self.assertEqual(answer["legal_basis"], [s.get("reference", "") for s in source.get("sources", [])])
            distribution = {letter: sum(1 for a in answers if a["correct_option"] == letter) for letter in "ABC"}
            self.assertEqual(distribution, {"A": 10, "B": 10, "C": 10})
            self.assertLessEqual(max_run([a["correct_option"] for a in answers]), 3, f"unbalanced run in variant {number}")

def max_run(values):
    best = run = 0
    previous = None
    for value in values:
        run = run + 1 if value == previous else 1
        previous = value
        best = max(best, run)
    return best


if __name__ == "__main__":
    unittest.main()
