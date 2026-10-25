import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LESSONS = ROOT / "podstawowy" / "lekcje"
GLOSSARY = ROOT / "podstawowy" / "SLOWNICZEK.md"

# Ustalona lista skrótów i fachowych etykiet, które pojawiają się w lekcjach.
# Test jest blokujący dla braku hasła albo wspólnego odsyłacza; nie ocenia
# samodzielnie poprawności prawnej definicji.
TERMS = {
    "ADR": r"\bADR\b",
    "Numer UN": r"\bUN\b",
    "LQ": r"\bLQ\b",
    "EQ": r"\bEQ\b",
    "DMC": r"\bDMC\b",
    "RID": r"\bRID\b",
    "IMDG": r"\bIMDG\b",
    "FL": r"\bFL\b",
    "AT": r"\bAT\b",
    "EX/II": r"EX/II",
    "EX/III": r"EX/III",
    "MEMU": r"\bMEMU\b",
    "DGSA / doradca ds. bezpieczeństwa": r"\bDGSA\b",
    "Kod ograniczenia przejazdu przez tunele": r"kod tunelowy|kod ograniczenia przejazdu przez tunele",
    "Instrukcje pisemne": r"instrukcj(?:a|e|ami) pisemn",
    "Grupa pakowania": r"grup(?:a|y|ę) pakowania",
    "Numer rozpoznawczy zagrożenia": r"numer rozpoznawczy zagrożenia",
    "Tablica pomarańczowa": r"tablic(?:a|e|y) pomarańczow",
    "Świadectwo dopuszczenia pojazdu": r"świadectw(?:o|a) dopuszczenia pojazdu",
    "Zaświadczenie kierowcy ADR": r"zaświadczeni(?:e|a) kierowcy ADR",
    "OVERPACK / opakowanie zbiorcze": r"OVERPACK|opakowanie zbiorcze",
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
        for term in TERMS:
            with self.subTest(term=term):
                self.assertRegex(glossary, r"(?im)^\| \*\*" + re.escape(term) + r"\*\*")

    def test_each_lesson_links_glossary_before_content(self):
        files = sorted(LESSONS.glob("ADR-B-*.md"))
        self.assertEqual(len(files), 13)
        for path in files:
            with self.subTest(lesson=path.name):
                text = path.read_text(encoding="utf-8")
                link = text.find("../SLOWNICZEK.md")
                self.assertGreaterEqual(link, 0, "brak odsyłacza do słowniczka")
                first_heading = text.find("\n## ")
                self.assertTrue(first_heading < 0 or link < first_heading,
                                "odsyłacz powinien pojawić się przed rozdziałami lekcji")

    def test_terms_used_in_lessons_are_registered(self):
        glossary = GLOSSARY.read_text(encoding="utf-8")
        all_lessons = "\n".join(p.read_text(encoding="utf-8") for p in sorted(LESSONS.glob("ADR-B-*.md")))
        for term, pattern in TERMS.items():
            with self.subTest(term=term):
                if re.search(pattern, all_lessons, flags=re.IGNORECASE):
                    self.assertRegex(glossary, r"(?im)^\| \*\*" + re.escape(term) + r"\*\*")

if __name__ == "__main__":
    unittest.main()
