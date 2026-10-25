"""All lessons provide clear learner navigation; during staged editing legacy lessons remain supported."""
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

class LessonNavigationTests(unittest.TestCase):
    def test_all_thirteen_lessons_have_plain_language_navigation(self):
        for number in range(1, 14):
            path = ROOT / "podstawowy" / "lekcje" / f"ADR-B-{number:02d}.md"
            self.assertTrue(path.is_file(), f"missing {path.name}")
            content = path.read_text(encoding="utf-8")
            canonical = all(marker in content for marker in (
                "## Po co to jest?", "## Czego się nauczysz",
                "## Typowe błędy kursantów", "## Scenariusze praktyczne",
                "## Co musisz zapamiętać", "## Sprawdź się",
                "## Powiązane pytania w banku", "## Podstawa prawna"))
            legacy = ("## Jak korzystać z tej lekcji" in content
                      and "materiałem uzupełniającym" in content)
            self.assertTrue(canonical or legacy,
                            f"{path.name}: neither canonical learner structure nor supported legacy structure")
            self.assertIn("needs_review", content, f"{path.name}: draft status caveat missing")

if __name__ == "__main__":
    unittest.main()
