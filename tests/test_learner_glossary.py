import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LESSONS = ROOT / "podstawowy" / "lekcje"
GLOSSARY = ROOT / "podstawowy" / "SLOWNICZEK.md"

# Canonical learner-facing terms. Slugs are explicit HTML anchors in SLOWNICZEK.md.
TERMS = {
    "ADR": (r"\bADR\b", ("adr",)),
    "Nadawca": (r"\bnadawc(?:a|y|ę|ą|e)\b", ("nadawca",)),
    "Numer UN": (r"\bnumer(?:u)?\s+UN\b|\bUN\b", ("numer-un",)),
    "LQ — ilości ograniczone": (r"\bLQ\b", ("lq-ilosci-ograniczone",)),
    "EQ — ilości wyłączone": (r"\bEQ\b", ("eq-ilosci-wylaczone",)),
    "DMC": (r"\bDMC\b", ("dmc",)),
    "RID / IMDG": (r"\bRID\b|\bIMDG(?:\s+Code)?\b", ("rid-imdg",)),
    "Pojazd FL": (r"\bFL\b", ("pojazd-fl",)),
    "Pojazd AT": (r"\bAT\b", ("pojazd-at",)),
    "EX/II i EX/III": (r"EX/II|EX/III", ("ex-ii-i-ex-iii",)),
    "MEMU": (r"\bMEMU\b", ("memu",)),
    "DGSA / doradca ds. bezpieczeństwa": (r"\bDGSA\b", ("dgsa-doradca-ds-bezpieczenstwa",)),
    "Kod ograniczenia przejazdu przez tunele": (r"kod(?:u|em|zie)?\s+tunelow(?:y|ego|ym|e|ych|ymi)|kod ograniczenia przejazdu przez tunele", ("kod-ograniczenia-przejazdu-przez-tunele", "kod-tunelowy-d-e")),
    "Instrukcje pisemne": (r"instrukcj(?:a pisemna|ę pisemną|i pisemnej|e pisemne|i pisemne|i pisemnych|ach pisemnych|ami pisemnymi)", ("instrukcje-pisemne",)),
    "Grupa pakowania": (r"grup(?:a|y|ę|ie)\s+pakowania", ("grupa-pakowania",)),
    "Numer rozpoznawczy zagrożenia": (r"numer(?:u)?\s+rozpoznawcz(?:y|ego)\s+zagrożenia", ("numer-rozpoznawczy-zagrozenia",)),
    "Tablica pomarańczowa": (r"tablic(?:a|y|ę|e|ami|ach)\s+pomarańczow(?:a|ej|e|ych|ymi|ą|y)", ("tablica-pomaranczowa",)),
    "Świadectwo dopuszczenia pojazdu": (r"świadectw(?:o|a|em|ie|wa)\s+dopuszczenia pojazdu", ("swiadectwo-dopuszczenia-pojazdu",)),
    "Zaświadczenie kierowcy ADR": (r"zaświadczeni(?:e|a|em)\s+kierowcy ADR|zaświadczenie ADR", ("zaswiadczenie-kierowcy-adr",)),
    "Opakowanie zbiorcze (OVERPACK)": (r"OVERPACK|opakowanie zbiorcze", ("opakowanie-zbiorcze-overpack",)),
    "Kategoria transportowa": (r"kategori(?:a|ę|i|ą)\s+transportow(?:a|ej|e|ych|ymi)", ("kategoria-transportowa",)),
    "Plan ochrony": (r"plan(?:u|em)?\s+ochrony", ("plan-ochrony",)),
    "Towary dużego ryzyka": (r"towar(?:y|ów)\s+dużego ryzyka", ("towary-duzego-ryzyka",)),
    "Kod klasyfikacyjny": (r"kod(?:u)?\s+klasyfikacyjn(?:y|ego|ym|e)", ("kod-klasyfikacyjny",)),
    "Zagrożenie dodatkowe": (r"zagrożeni(?:e|a|em)\s+dodatkowe", ("zagrozenie-dodatkowe",)),
    "Tabela A": (r"tabel(?:a|i|ę)\s+A", ("tabela-a",)),
}

class LearnerGlossaryTests(unittest.TestCase):
    def test_every_established_term_has_glossary_entry_and_anchor(self):
        glossary = GLOSSARY.read_text(encoding="utf-8")
        for heading, (_, slugs) in TERMS.items():
            with self.subTest(term=heading):
                self.assertRegex(glossary, r"(?im)^\| \*\*" + re.escape(heading) + r"\*\*")
                for slug in slugs:
                    self.assertIn(f'<a id="{slug}"></a>', glossary, f"brak kotwicy #{slug}")

    def test_each_lesson_links_glossary(self):
        files = sorted(LESSONS.glob("ADR-B-*.md"))
        self.assertEqual(len(files), 13)
        for path in files:
            with self.subTest(lesson=path.name):
                text = path.read_text(encoding="utf-8")
                self.assertIn("../SLOWNICZEK.md", text, "brak odsyłacza do słowniczka")

    @staticmethod
    def _inside_glossary_definition(text, position):
        opening = text.rfind("(", 0, position)
        closing = text.rfind(")", 0, position)
        return opening > closing and "SLOWNICZEK.md#" in text[opening:position]

    @staticmethod
    def _paragraph_or_list_item(text, position):
        line_start = text.rfind("\n", 0, position) + 1
        line_end = text.find("\n", position)
        if line_end < 0:
            line_end = len(text)
        line = text[line_start:line_end]
        if line.lstrip().startswith(("- ", "* ", "+ ")):
            return line
        start = text.rfind("\n\n", 0, position) + 2
        end = text.find("\n\n", position)
        if end < 0:
            end = len(text)
        return text[start:end]

    def test_first_use_of_each_established_term_has_inline_explanation_or_glossary_link(self):
        glossary = GLOSSARY.read_text(encoding="utf-8")
        files = sorted(LESSONS.glob("ADR-B-*.md"))
        for path in files:
            text = path.read_text(encoding="utf-8")
            start = text.find("## Po co to jest?")
            self.assertGreaterEqual(start, 0, f"{path.name}: brak sekcji wprowadzającej")
            learner_text = text[start:]
            for heading, (pattern, slugs) in TERMS.items():
                compiled = re.compile(pattern, re.IGNORECASE)
                match = None
                for candidate in compiled.finditer(learner_text):
                    if self._inside_glossary_definition(learner_text, candidate.start()):
                        continue
                    match = candidate
                    break
                if match is None:
                    continue
                paragraph = self._paragraph_or_list_item(learner_text, match.start())
                with self.subTest(lesson=path.name, term=heading):
                    self.assertTrue(
                        any(f"SLOWNICZEK.md#{slug}" in paragraph for slug in slugs),
                        f"{path.name}: pierwsze użycie „{heading}” nie ma objaśnienia ani linku do kotwicy w tym samym akapicie/list item",
                    )


    def test_glossary_anchors_and_exact_headings_are_unique(self):
        glossary = GLOSSARY.read_text(encoding="utf-8")
        anchors = re.findall(r'<a id="([^"]+)"></a>', glossary)
        duplicate_anchors = sorted({slug for slug in anchors if anchors.count(slug) > 1})
        self.assertEqual(duplicate_anchors, [], f"duplicate glossary anchors: {duplicate_anchors}")

        headings = re.findall(r"(?im)^\\| \\*\\*(.*?)\\*\\*", glossary)
        normalized = [heading.strip().casefold() for heading in headings]
        duplicate_headings = sorted({heading for heading in normalized if normalized.count(heading) > 1})
        self.assertEqual(duplicate_headings, [], f"duplicate glossary headings: {duplicate_headings}")

if __name__ == "__main__":
    unittest.main()
