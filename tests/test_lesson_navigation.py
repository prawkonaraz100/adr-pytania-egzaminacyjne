"""Every lesson distinguishes the main learning path from supplemental scenarios."""
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

class LessonNavigationTests(unittest.TestCase):
    def test_all_thirteen_lessons_have_plain_language_navigation(self):
        for number in range(1, 14):
            path = ROOT / "podstawowy" / "lekcje" / f"ADR-B-{number:02d}.md"
            self.assertTrue(path.is_file(), f"missing {path.name}")
            content = path.read_text(encoding="utf-8")
            self.assertIn("## Jak korzystać z tej lekcji", content, f"{path.name}: missing learner guide")
            self.assertIn("materiałem uzupełniającym", content, f"{path.name}: supplemental sections not explained")
            self.assertIn("needs_review", content, f"{path.name}: draft status caveat missing")

if __name__ == "__main__":
    unittest.main()
