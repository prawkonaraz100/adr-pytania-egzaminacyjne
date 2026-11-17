"""First-pass literal ADR review ADR-B-0691–0705; no bank modifications."""
from collections import Counter
from pathlib import Path
import hashlib
import json
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
BANK = ROOT / "podstawowy/questions.jsonl"
REPORT = ROOT / "review/literal-pl/PARTIA-0691-0705.md"
MANIFEST = ROOT / "review/literal-pl/PARTIA-0691-0705.json"
FIRST_PASS_BANK_SHA = "092325a21fe95a47406e2d28e4947885c19dc0dc"
EXPECTED_BANK_SHA = "092325a21fe95a47406e2d28e4947885c19dc0dc"
EXPECTED_IDS = [f"ADR-B-{n:04d}" for n in range(691, 706)]
ABSOLUTE = re.compile(r"\b(tylko|zawsze|każdy|każda|każde|każdej|wszystkie|wyłącznie|żaden|żadnych|nigdy|całkowicie|automatycznie|niezależnie)\b", re.I)

def git_blob_sha(data):
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()

class Partia47LiteralReview(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.m = json.loads(MANIFEST.read_text(encoding="utf-8"))
        cls.raw = BANK.read_bytes()
        cls.bank = {q["id"]: q for q in (json.loads(line) for line in cls.raw.decode("utf-8").splitlines() if line.strip())}

    def test_scope_counts_and_sources(self):
        m = self.m
        self.assertTrue(REPORT.is_file())
        self.assertEqual(m["scope"], "first_pass_literal_review")
        self.assertEqual(m["batch"], "ADR-B-0691–0705")
        self.assertEqual(m["bank_count"], 780)
        self.assertEqual(m["bank_blob_sha"], FIRST_PASS_BANK_SHA)
        self.assertFalse(m["bank_changed"])
        self.assertEqual(m["previous_uncompared"], 90)
        self.assertEqual(m["compared"], 15)
        self.assertEqual(m["remaining_without_comparison"], 75)
        self.assertEqual(m["verified"], 0)
        rows = m["records"]
        self.assertEqual([r["id"] for r in rows], EXPECTED_IDS)
        self.assertEqual(len(rows), 15)
        counts = dict(Counter(r["verdict"] for r in rows))
        self.assertEqual(m["counts"], {key: counts.get(key, 0) for key in ("OK", "POPRAW", "BLOKUJ")})
        for r in rows:
            self.assertIn(r["verdict"], ("OK", "POPRAW", "BLOKUJ"))
            self.assertTrue(r["legal_basis"])
            self.assertTrue(r["exact_quote"])
            self.assertTrue(r["gazette_pages"])
            self.assertTrue(all(isinstance(p, int) and p > 0 for p in r["gazette_pages"]))
            self.assertEqual(r["verification_status"], "needs_review")
            self.assertEqual(r["original_correct_option"], self.bank[r["id"]]["correct_option"])

    def test_proposed_replacements(self):
        for row in self.m["records"]:
            if row["verdict"] != "POPRAW":
                continue
            with self.subTest(id=row["id"]):
                p = row["proposed_replacement"]
                self.assertIsInstance(p, dict)
                self.assertTrue(p["stem"])
                self.assertEqual(p["module_id"], row["module_id"])
                self.assertEqual(p["competency_id"], row["competency_id"])
                self.assertEqual(set(p["options"]), {"A", "B", "C"})
                self.assertEqual(p["correct_option"], self.bank[row["id"]]["correct_option"])
                lens = {key: len(value) for key, value in p["options"].items()}
                self.assertLessEqual(max(lens.values()), 80)
                v = lens[p["correct_option"]]
                self.assertFalse(v == max(lens.values()) and list(lens.values()).count(v) == 1)
                self.assertFalse(v == min(lens.values()) and list(lens.values()).count(v) == 1)
                for option in p["options"].values():
                    self.assertFalse(option.endswith("."))
                    self.assertNotIn(";", option)
                    self.assertIsNone(ABSOLUTE.search(option))
                explanation = p["explanation"]
                self.assertGreaterEqual(len(explanation), 300)
                self.assertRegex(explanation, r"Podstawa: ADR [\d.]+\.$")
                sentences = re.split(r"(?<=[.!?])\s+(?=[A-ZĄĆĘŁŃÓŚŹŻ])", explanation.strip())
                self.assertGreaterEqual(len(sentences), 2)
                self.assertLessEqual(len(sentences), 5)
                for sentence in sentences:
                    self.assertLessEqual(len(re.findall(r"\b[\wąćęłńóśźżĄĆĘŁŃÓŚŹŻ-]+\b", sentence)), 35)
                self.assertTrue(p["sources"])
                self.assertTrue(p["replacement_quote"])
                self.assertTrue(p["replacement_pages"])

    def test_bank_unchanged_and_no_verified(self):
        self.assertEqual(git_blob_sha(self.raw), EXPECTED_BANK_SHA)
        self.assertEqual(len(self.bank), 780)
        for id in EXPECTED_IDS:
            q = self.bank[id]
            self.assertEqual(q["verification_status"], "needs_review")
            self.assertIsNone(q["checked_at"])
            self.assertIsNone(q["reviewer"])

if __name__ == "__main__":
    unittest.main()
