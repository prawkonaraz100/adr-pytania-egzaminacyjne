import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from coverage import analyse, check_lessons


def sample():
    questions = []
    objectives = []
    for i in range(1, 14):
        module = f"ADR-B-{i:02d}"
        qid = f"ADR-B-{i:04d}"
        questions.append({"id": qid, "module_id": module, "verification_status": "needs_review"})
        objectives.append({
            "id": f"{module}-K01",
            "module_id": module,
            "objective": f"Zrozumienie zasad modułu {module}",
            "legal_refs": "1.1.1",
            "question_ids": [qid],
            "delivery": "theory",
            "review_status": "needs_review",
        })
    return questions, {"competencies": objectives}


class CoverageTests(unittest.TestCase):
    def test_consistent_map_passes_without_expert_approval(self):
        questions, curriculum = sample()
        errors, report = analyse(questions, curriculum)
        self.assertEqual(errors, [])
        self.assertEqual(report["draft_question_coverage"], 13)
        self.assertEqual(report["verified_question_coverage"], 0)

    def test_unmapped_question_is_error(self):
        questions, curriculum = sample()
        curriculum["competencies"][0]["question_ids"] = []
        errors, report = analyse(questions, curriculum)
        self.assertTrue(any("nieprzypisane pytania" in x for x in errors))
        self.assertEqual(len(report["theory_without_questions"]), 1)

    def test_foreign_module_link_is_error(self):
        questions, curriculum = sample()
        curriculum["competencies"][0]["question_ids"] = ["ADR-B-0002"]
        errors, _ = analyse(questions, curriculum)
        self.assertTrue(any("z innego modułu" in x for x in errors))

    def test_release_requires_verified_coverage(self):
        questions, curriculum = sample()
        errors, _ = analyse(questions, curriculum, release=True)
        self.assertTrue(any("celów teorii bez verified" in x for x in errors))

    def test_practical_not_treated_as_multiple_choice(self):
        questions, curriculum = sample()
        curriculum["competencies"].append({
            "id": "ADR-B-05-K02",
            "module_id": "ADR-B-05",
            "objective": "Praktyczny instruktaż używania gaśnicy",
            "legal_refs": "program praktyczny zał. 1",
            "question_ids": [],
            "delivery": "practical",
            "review_status": "needs_review",
        })
        errors, report = analyse(questions, curriculum)
        self.assertEqual(errors, [])
        self.assertEqual(report["practical_competencies"], 1)
        self.assertEqual(report["draft_question_coverage"], 13)


    def test_lesson_inventory_reports_missing_files(self):
        with tempfile.TemporaryDirectory() as tmp:
            self.assertEqual(len(check_lessons(Path(tmp))), 13)

    def test_lesson_inventory_accepts_substantive_stubs(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            folder = root / "podstawowy" / "lekcje"
            folder.mkdir(parents=True)
            for i in range(1, 14):
                n = f"ADR-B-{i:02d}"
                (folder / f"{n}.md").write_text(
                    f"# {n} — Test zajęć\\n\\n## Źródła\\nADR 2025\\n" +
                    "Kwestie do opanowania. " * 70, encoding="utf-8"
                )
            self.assertEqual(check_lessons(root), [])

    def test_lesson_inventory_accepts_legacy_heading_and_podstawa(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            folder = root / "podstawowy" / "lekcje"
            folder.mkdir(parents=True)
            for i in range(1, 14):
                n = f"ADR-B-{i:02d}"
                title = f"# Lekcja {n} — szkolenie"
                (folder / f"{n}.md").write_text(
                    title + "\\n\\n## Podstawa\\nADR 2025\\n" +
                    "Przykładowe treści edukacyjne. " * 50, encoding="utf-8"
                )
            self.assertEqual(check_lessons(root), [])


if __name__ == "__main__":
    unittest.main()
