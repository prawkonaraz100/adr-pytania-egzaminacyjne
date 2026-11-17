"""First-pass literal review tests for ADR-B-0706–0720; no bank modifications."""
from collections import Counter
from pathlib import Path
import hashlib
import json
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
BANK = ROOT / "podstawowy/questions.jsonl"
REPORT = ROOT / "review/literal-pl/PARTIA-0706-0720.md"
MANIFEST = ROOT / "review/literal-pl/PARTIA-0706-0720.json"
EXPECTED_BANK_SHA = "e92048bdde4e05422e3265542636b6213f3e10b4"
EXPECTED_IDS = [f"ADR-B-{n:04d}" for n in range(706, 721)]

def git_blob_sha(data):
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()

class Partia48LiteralReview(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.m = json.loads(MANIFEST.read_text(encoding="utf-8"))
        cls.raw = BANK.read_bytes()
        cls.rows = [json.loads(line) for line in cls.raw.decode("utf-8").splitlines() if line.strip()]
        cls.bank = {q["id"]: q for q in cls.rows}

    def test_scope_and_counts(self):
        self.assertTrue(REPORT.is_file())
        self.assertEqual(len(self.rows), 780)
        self.assertEqual(git_blob_sha(self.raw), EXPECTED_BANK_SHA)
        self.assertEqual(self.m["bank_blob_sha"], EXPECTED_BANK_SHA)
        self.assertFalse(self.m["bank_changed"])
        self.assertEqual(self.m["batch"], "ADR-B-0706–0720")
        self.assertEqual(self.m["previous_uncompared"], 75)
        self.assertEqual(self.m["compared"], 15)
        self.assertEqual(self.m["remaining_without_comparison"], 60)
        self.assertEqual(self.m["verified"], 0)
        self.assertEqual([r["id"] for r in self.m["records"]], EXPECTED_IDS)
        self.assertEqual(len(self.m["records"]), 15)
        counts = Counter(r["verdict"] for r in self.m["records"])
        self.assertEqual(dict(counts), {"POPRAW": 5, "BLOKUJ": 10})
        self.assertEqual(self.m["counts"], {"OK": 0, "POPRAW": 5, "BLOKUJ": 10})

    def test_bank_records_remain_unverified(self):
        for id in EXPECTED_IDS:
            q = self.bank[id]
            self.assertEqual(q["verification_status"], "needs_review")
            self.assertIsNone(q["checked_at"])
            self.assertIsNone(q["reviewer"])

    def test_replacement_form(self):
        for row in self.m["records"]:
            if row["verdict"] != "POPRAW":
                continue
            with self.subTest(id=row["id"]):
                p = row["proposed_replacement"]
                self.assertEqual(p["module_id"], row["module_id"])
                self.assertEqual(p["competency_id"], row["competency_id"])
                self.assertEqual(p["correct_option"], row["original_correct_option"])
                self.assertEqual(set(p["options"]), {"A", "B", "C"})
                lengths = {k: len(v) for k, v in p["options"].items()}
                self.assertLessEqual(max(lengths.values()), 80)
                key_length = lengths[p["correct_option"]]
                self.assertFalse(key_length == max(lengths.values()) and list(lengths.values()).count(key_length) == 1)
                self.assertFalse(key_length == min(lengths.values()) and list(lengths.values()).count(key_length) == 1)
                for option in p["options"].values():
                    self.assertFalse(option.endswith("."))
                    self.assertNotIn(";", option)
                self.assertGreaterEqual(len(p["explanation"]), 300)
                self.assertLessEqual(len(p["explanation"]), 500)
                self.assertRegex(p["explanation"], r"Podstawa: ADR [\d.]+\.$")
                self.assertTrue(p["sources"])
                self.assertTrue(p["replacement_quote"])
                self.assertTrue(p["replacement_pages"])

if __name__ == "__main__":
    unittest.main()
