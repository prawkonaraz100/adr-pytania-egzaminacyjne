"""Guard the competency map, program summary and coverage matrix against drift."""
import json
import unittest
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASIC = ROOT / "podstawowy"
BANK_PATH = BASIC / "questions.jsonl"
COMP_PATH = BASIC / "kompetencje.json"
COVERAGE_PATH = ROOT / "docs" / "POKRYCIE-KURSU.md"
PROGRAM_PATH = ROOT / "docs" / "PROGRAM-PODSTAWOWY.md"


class CompetencyDepthCoverageTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.questions = [
            json.loads(line)
            for line in BANK_PATH.read_text(encoding="utf-8").splitlines()
            if line.strip()
        ]
        cls.by_id = {q["id"]: q for q in cls.questions}
        cls.competencies = json.loads(COMP_PATH.read_text(encoding="utf-8"))["competencies"]
        cls.coverage = COVERAGE_PATH.read_text(encoding="utf-8")
        cls.program = PROGRAM_PATH.read_text(encoding="utf-8")

    def test_all_theory_competencies_have_two_draft_questions_and_valid_links(self):
        theory = [c for c in self.competencies if c["delivery"] == "theory"]
        practical = [c for c in self.competencies if c["delivery"] == "practical"]
        self.assertEqual(len(self.competencies), 107)
        self.assertEqual(len(theory), 104)
        self.assertEqual(len(practical), 3)
        referenced = set()
        for competency in self.competencies:
            ids = competency["question_ids"]
            self.assertEqual(len(ids), len(set(ids)), competency["id"])
            for question_id in ids:
                self.assertIn(question_id, self.by_id, competency["id"])
                self.assertEqual(
                    self.by_id[question_id]["module_id"],
                    competency["module_id"],
                    f"{competency['id']} points to another module: {question_id}",
                )
                referenced.add(question_id)
            if competency["delivery"] == "theory":
                self.assertGreaterEqual(len(ids), 2, competency["id"])
        self.assertEqual(referenced, set(self.by_id))
        self.assertTrue(all(q["verification_status"] == "needs_review" for q in self.questions))
        self.assertEqual(sum(q["verification_status"] == "verified" for q in self.questions), 0)
        self.assertIn("107 roboczych kompetencji", self.program)
        self.assertIn("104/104 kompetencji teoretycznych", self.coverage)
        self.assertIn("co najmniej dwa pytania robocze", self.coverage)

    def test_module_competency_counts_and_question_counts_match_coverage_table(self):
        theory_count = Counter(c["module_id"] for c in self.competencies if c["delivery"] == "theory")
        practical_count = Counter(c["module_id"] for c in self.competencies if c["delivery"] == "practical")
        question_count = Counter(q["module_id"] for q in self.questions)
        matrix = self.coverage.split("## Matryca gotowości", 1)[1].split(
            "## Pogłębienie zagadnień", 1
        )[0]
        rows = {}
        for line in matrix.splitlines():
            if line.startswith("| ADR-B-"):
                cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
                rows[cells[0]] = cells
        for i in range(1, 14):
            module = f"ADR-B-{i:02d}"
            with self.subTest(module=module):
                cells = rows[module]
                self.assertEqual(cells[2].strip("*"), f"{theory_count[module]}/{theory_count[module]}")
                self.assertEqual(int(cells[3].strip("*")), practical_count[module])
                self.assertEqual(int(cells[4].strip("*")), question_count[module])
        total = next(line for line in matrix.splitlines() if line.startswith("| **Razem**"))
        cells = [cell.strip() for cell in total.strip().strip("|").split("|")]
        self.assertEqual(cells[2].strip("*"), "104/104")
        self.assertEqual(int(cells[3].strip("*"), 10), 3)
        self.assertEqual(int(cells[4].strip("*"), 10), 676)


if __name__ == "__main__":
    unittest.main()
