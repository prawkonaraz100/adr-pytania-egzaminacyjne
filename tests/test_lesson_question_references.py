"""Every question ID referenced by a lesson must exist and canonical lessons must link their own module."""
import json, re, unittest
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
ID_RE = re.compile(r"ADR-B-\d{4}")

class LessonQuestionReferenceTests(unittest.TestCase):
    def test_all_13_lessons_have_maps_and_existing_question_ids(self):
        bank = [json.loads(x) for x in (ROOT / "podstawowy" / "questions.jsonl").read_text(encoding="utf-8").splitlines() if x.strip()]
        by_id = {q["id"]: q for q in bank}
        valid = set(by_id)
        for n in range(1, 14):
            path = ROOT / "podstawowy" / "lekcje" / f"ADR-B-{n:02d}.md"
            self.assertTrue(path.is_file(), f"missing lesson {path.name}")
            content = path.read_text(encoding="utf-8")
            canonical = all(marker in content for marker in ("## Po co to jest?", "## Czego się nauczysz", "## Typowe błędy kursantów", "## Scenariusze praktyczne", "## Co musisz zapamiętać", "## Sprawdź się", "## Powiązane pytania w banku", "## Podstawa prawna"))
            self.assertTrue(canonical or "Mapa pytań i przykład praktyczny" in content,
                            f"{path.name}: missing question map")
            refs = set(ID_RE.findall(content))
            self.assertTrue(refs, f"{path.name}: no question IDs")
            self.assertFalse(refs - valid, f"{path.name}: unknown IDs {sorted(refs - valid)}")
            if canonical:
                expected_module = f"ADR-B-{n:02d}"
                wrong = sorted(qid for qid in refs if by_id[qid]["module_id"] != expected_module)
                self.assertFalse(wrong, f"{path.name}: question IDs from another module: {wrong}")


    def test_every_bank_question_is_referenced_by_its_own_lesson(self):
        bank = [
            json.loads(line)
            for line in (ROOT / "podstawowy" / "questions.jsonl").read_text(encoding="utf-8").splitlines()
            if line.strip()
        ]
        for number in range(1, 14):
            module = f"ADR-B-{number:02d}"
            path = ROOT / "podstawowy" / "lekcje" / f"{module}.md"
            lesson_ids = set(ID_RE.findall(path.read_text(encoding="utf-8")))
            expected_ids = {q["id"] for q in bank if q["module_id"] == module}
            self.assertTrue(
                expected_ids.issubset(lesson_ids),
                f"{module}: questions missing from its lesson: {sorted(expected_ids - lesson_ids)}",
            )

if __name__ == "__main__":
    unittest.main()
