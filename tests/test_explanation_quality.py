import json
import re
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from check_explanation_quality import short_explanations


def split_learner_sentences(text):
    # Protect common Polish abbreviations so "m.in." is not split as two sentences.
    protected = re.sub(
        r"\b(m\.in|np|itd|tj|tzn|dr|prof|nr|pkt|ust|lit|str|rys)\.",
        lambda match: match.group(0).replace(".", "¤"),
        text,
        flags=re.IGNORECASE,
    )
    return [part.strip() for part in re.split(r"(?<=[.!?])\s+", protected) if part.strip()]


def learner_word_count(sentence):
    return len(re.findall(r"\b[\w]+(?:[-/][\w]+)*\b", sentence, flags=re.UNICODE))


class ExplanationQualityTests(unittest.TestCase):
    def test_accepts_explanation_at_minimum(self):
        rows = [{"id": "ADR-B-0001", "explanation": "x" * 200}]
        self.assertEqual(short_explanations(rows), [])

    def test_rejects_missing_or_short_explanations(self):
        rows = [
            {"id": "ADR-B-0001", "explanation": "x" * 199},
            {"id": "ADR-B-0002", "explanation": ""},
            {"id": "ADR-B-0003"},
        ]
        self.assertEqual(short_explanations(rows), [
            ("ADR-B-0001", 199),
            ("ADR-B-0002", 0),
            ("ADR-B-0003", 0),
        ])

    def test_custom_minimum(self):
        rows = [{"id": "ADR-B-0001", "explanation": "x" * 50}]
        self.assertEqual(short_explanations(rows, 51), [("ADR-B-0001", 50)])


    def test_all_bank_explanations_have_learner_friendly_sentence_length(self):
        root = Path(__file__).resolve().parents[1]
        rows = [
            json.loads(line)
            for line in (root / "podstawowy" / "questions.jsonl").read_text(encoding="utf-8").splitlines()
            if line.strip()
        ]
        self.assertEqual(len(rows), 609)
        for row in rows:
            with self.subTest(question_id=row["id"]):
                sentences = split_learner_sentences(row.get("explanation", ""))
                self.assertGreaterEqual(len(sentences), 2, "explanation must have at least 2 sentences")
                self.assertLessEqual(len(sentences), 5, "explanation must have at most 5 sentences")
                for sentence in sentences:
                    self.assertLessEqual(learner_word_count(sentence), 35, f"sentence exceeds 35 words: {row['id']}")

if __name__ == "__main__":
    unittest.main()
