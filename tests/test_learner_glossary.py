import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LESSONS = ROOT / "podstawowy" / "lekcje"
GLOSSARY = ROOT / "podstawowy" / "SLOWNICZEK.md"

# Canonical glossary heading -> expression that finds the term in lessons.
TERMS = {
    "ADR": r"\\bADR\\b",
    "Numer UN": r"\\bUN\\b",
    "LQ — ilości ograniczone": r"\\bLQ\\b",
    "EQ — ilości wyłączone": r"\\bEQ\\b",
    "DMC": r"\\bDMC\\b",
    "RID / IMDG": r"\\bRID\\b",
    "RID / IMDG": r"\\bIMDG\\b",
    "Pojazd FL": r"\\bFL\\b",
    "Pojazd AT": r"\\bAT\\b",
    "EX/II i EX/III": r"EX/II|EX/III",
    "MEMU": r"\\bMEMU\\b",
    "DGSA / doradca ds. bezpieczeństwa": r"\\bDGSA\\b",
    "Kod ograniczenia przejazdu przez tunele": r"kod tunelowy|kod ograniczenia przejazdu przez tunele",
    "Instrukcje pisemne": r"instrukcj(?:a|e|ami) pisemn",
    "Grupa pakowania": r"grup(?:a|y|ę) pakowania",
    "Numer rozpoznawczy zagrożenia": r"numer rozpoznawczy zagrożenia",
    "Tablica pomarańczowa": r"tablic(?:a|e|y) pomarańczow",
    "Świadectwo dopuszczenia pojazdu": r"świadectw(?:o|a) dopuszczenia pojazdu",
    "Zaświadczenie kierowcy ADR": r"zaświadczeni(?:e|a) kierowcy ADR",
    "Opakowanie zbiorcze (OVERPACK)": r"OVERPACK|opakowanie zbiorcze",
    "Kategoria transportowa": r"kategori(?:a|ę|i) transportow",
    "Plan ochrony": r"plan(?:u)? ochrony",
    "Towary dużego ryzyka": r"towar(?:y|ów) dużego ryzyka",
    "Kod klasyfikacyjny": r"kod(?:u)? klasyfikacyjn",
    "Zagrożenie dodatkowe": r"zagrożeni(?:e|a) dodatkowe",
    "Tabela A": r"tabel(?:a|i) A",
}

class LearnerGlossaryTests(unittest.TestCase):
    def test_every_established_term_has_glossary_entry(self):
        glossary = GLOSSARY.read_text(encoding="utf-8")
        for heading in TERMS:
            with self.subTest(term=heading):
                self.assertRegex(glossary, r"(?im)^\\| \\*\\*" + re.escape(heading) + r"\\*\\*")

    def test_each_lesson_links_glossary(self):
        files = sorted(LESSONS.glob("ADR-B-*.md"))
        self.assertEqual(len(files), 13)
        for path in files:
            with self.subTest(lesson=path.name):
                text = path.read_text(encoding="utf-8")
                self.assertIn("../SLOWNICZEK.md", text, "brak odsyłacza do słowniczka")

    def test_terms_used_in_lessons_are_registered(self):
        glossary = GLOSSARY.read_text(encoding="utf-8")
        all_lessons = "\\n".join(p.read_text(encoding="utf-8") for p in sorted(LESSONS.glob("ADR-B-*.md")))
        for heading, pattern in TERMS.items():
            with self.subTest(term=heading):
                if re.search(pattern, all_lessons, flags=re.IGNORECASE):
                    self.assertRegex(glossary, r"(?im)^\\| \\*\\*" + re.escape(heading) + r"\\*\\*")

if __name__ == "__main__":
    unittest.main()
