import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LESSONS = ROOT / "podstawowy" / "lekcje"
INSTRUCTORS = ROOT / "podstawowy" / "instruktor"
BASIC = ROOT / "podstawowy"
SCENARIOS = BASIC / "praktyka" / "scenariusze-13-dzialow.json"
QUESTIONS = BASIC / "questions.jsonl"
GLOSSARY = BASIC / "SLOWNICZEK.md"

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

        headings = [heading.strip() for heading in re.findall(r"(?im)^\| \*\*(.*?)\*\*", glossary) if heading.strip()]
        normalized = [heading.casefold() for heading in headings]
        duplicate_headings = sorted({heading for heading in normalized if normalized.count(heading) > 1})
        self.assertEqual(duplicate_headings, [], f"duplicate glossary headings: {duplicate_headings}")


    def test_instructor_guides_link_glossary_and_all_scenarios(self):
        files = sorted(INSTRUCTORS.glob("ADR-B-*.md"))
        self.assertEqual(len(files), 13)
        scenario_data = __import__("json").loads(SCENARIOS.read_text(encoding="utf-8"))
        scenario_ids = {item["id"] for item in scenario_data["scenarios"]}
        for path in files:
            module_number = path.stem[-2:]
            expected = {
                f"SC-ADR-B-{module_number}",
                f"SC-ADR-B-{module_number}-02",
                f"SC-ADR-B-{module_number}-03",
            }
            text = path.read_text(encoding="utf-8")
            with self.subTest(instructor=path.name):
                self.assertIn("../SLOWNICZEK.md", text, "brak odsyłacza do słowniczka")
                self.assertTrue(expected.issubset(scenario_ids), f"brak scenariusza w JSON: {expected - scenario_ids}")
                for scenario_id in expected:
                    self.assertIn(scenario_id, text, f"brak odwołania do {scenario_id}")

    def test_question_ids_in_lessons_and_instructor_guides_exist_in_their_module(self):
        bank = [
            __import__("json").loads(line)
            for line in QUESTIONS.read_text(encoding="utf-8").splitlines()
            if line.strip()
        ]
        by_id = {question["id"]: question for question in bank}
        self.assertEqual(len(by_id), len(bank), "duplikaty ID w banku")
        files = sorted(LESSONS.glob("ADR-B-*.md")) + sorted(INSTRUCTORS.glob("ADR-B-*.md"))
        self.assertEqual(len(files), 26)
        for path in files:
            module = f"ADR-B-{path.stem[-2:]}"
            text = path.read_text(encoding="utf-8")
            ids = set(re.findall(r"ADR-B-\\d{4}", text))
            for question_id in ids:
                with self.subTest(file=path.relative_to(ROOT).as_posix(), question=question_id):
                    self.assertIn(question_id, by_id, "question ID nie istnieje w banku")
                    self.assertEqual(by_id[question_id]["module_id"], module, "question ID wskazuje inny dział")

    def test_scenario_question_ids_exist_and_match_scenario_module(self):
        bank = [
            __import__("json").loads(line)
            for line in QUESTIONS.read_text(encoding="utf-8").splitlines()
            if line.strip()
        ]
        by_id = {question["id"]: question for question in bank}
        scenario_data = __import__("json").loads(SCENARIOS.read_text(encoding="utf-8"))
        self.assertEqual(len(scenario_data["scenarios"]), 39)
        for scenario in scenario_data["scenarios"]:
            with self.subTest(scenario=scenario["id"]):
                for question_id in scenario["question_ids"]:
                    self.assertIn(question_id, by_id, "scenario question ID nie istnieje")
                    self.assertEqual(by_id[question_id]["module_id"], scenario["module_id"])

if __name__ == "__main__":
    unittest.main()
