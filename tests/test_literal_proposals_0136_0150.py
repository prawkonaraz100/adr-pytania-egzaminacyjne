"""Validate batch 10 proposals on an in-memory bank copy, without publishing or legal approval."""
import copy
import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BANK = ROOT / "podstawowy" / "questions.jsonl"
PROPOSALS = ROOT / "review" / "literal-pl" / "POPRAWKI-0136-0150.jsonl"
REPORT = ROOT / "review" / "literal-pl" / "PARTIA-0136-0150.json"
EXPECTED = {
    "ADR-B-0136", "ADR-B-0137", "ADR-B-0138", "ADR-B-0140",
    "ADR-B-0141", "ADR-B-0142", "ADR-B-0144", "ADR-B-0145",
    "ADR-B-0146", "ADR-B-0147", "ADR-B-0150",
}
BLOCKED = set()
SECOND_EXPECTED = {"ADR-B-%04d" % n for n in range(136, 151)}
SECOND_PROPOSALS = ROOT / "review" / "literal-pl" / "POPRAWKI-KONTROLA2-0136-0150.jsonl"

def read_jsonl(path):
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]

class Batch10ProposalTests(unittest.TestCase):
    def test_full_proposals_on_bank_copy(self):
        original = read_jsonl(BANK)
        proposals = read_jsonl(PROPOSALS)
        current = {record["id"]: record for record in original}
        self.assertEqual(len(current), 780)
        self.assertEqual({p["id"] for p in proposals}, EXPECTED)
        working = copy.deepcopy(current)
        for proposal in proposals:
            ident = proposal["id"]
            self.assertEqual(list(proposal), list(current[ident]))
            self.assertEqual(proposal["correct_option"], current[ident]["correct_option"])
            self.assertEqual(proposal["verification_status"], "needs_review")
            self.assertIsNone(proposal["checked_at"])
            self.assertIsNone(proposal["reviewer"])
            self.assertEqual(set(proposal["options"]), {"A", "B", "C"})
            self.assertEqual(len(set(proposal["options"].values())), 3)
            lengths = {key: len(value) for key, value in proposal["options"].items()}
            longest = max(lengths.values())
            self.assertFalse(lengths[proposal["correct_option"]] == longest
                             and list(lengths.values()).count(longest) == 1, ident)
            explanation = proposal["explanation"].strip()
            self.assertGreaterEqual(len(explanation), 300)
            sentences = re.split(r"(?<=[.!?])\s+", explanation)
            self.assertTrue(2 <= len(sentences) <= 5, ident)
            self.assertTrue(all(len(sentence.split()) <= 35 for sentence in sentences), ident)
            self.assertRegex(explanation, r"Podstawa: ADR .+\.$")
            self.assertTrue(proposal["sources"])
            self.assertTrue(all(source["code"] == "ADR-2025-PL" or source["code"] == "M364"
                                for source in proposal["sources"]))
            working[ident] = proposal
        self.assertEqual(len(working), 780)
        self.assertTrue(all(q["verification_status"] == "needs_review" for q in working.values()))
        self.assertTrue(all(q["checked_at"] is None and q["reviewer"] is None for q in working.values()))
        for ident in BLOCKED:
            self.assertEqual(working[ident], current[ident])
        # Existing risk-review regression tests must hold on the proposal copy.
        self.assertIn("nie kontener-cysterna", working["ADR-B-0140"]["stem"])
        self.assertIn("kontenerów-cystern", working["ADR-B-0140"]["explanation"])
        self.assertIn("BK", working["ADR-B-0139"]["options"]["B"])
        self.assertIn("VC", working["ADR-B-0139"]["options"]["B"])
        self.assertIn("odesłanie", working["ADR-B-0139"]["options"]["B"])

    def test_all_second_review_records_are_applied(self):
        current = {x["id"]: x for x in read_jsonl(BANK)}
        patches = read_jsonl(SECOND_PROPOSALS)
        self.assertEqual({p["id"] for p in patches}, SECOND_EXPECTED)
        for p in patches:
            self.assertEqual(current[p["id"]], p)
            self.assertEqual(p["verification_status"], "needs_review")
            self.assertIsNone(p["checked_at"])
            self.assertIsNone(p["reviewer"])

    def test_report_counter_and_verdicts(self):
        report = json.loads(REPORT.read_text(encoding="utf-8"))
        self.assertEqual(report["previous_uncompared"], 618)
        self.assertEqual(report["remaining_without_comparison"], 603)
        self.assertEqual(report["counts"], {"OK": 0, "POPRAW": 15, "BLOKUJ": 0})
        self.assertEqual(len(report["records"]), 15)
        self.assertEqual({r["id"] for r in report["records"] if r["verdict"] == "POPRAW"}, SECOND_EXPECTED)
        self.assertEqual({r["id"] for r in report["records"] if r["verdict"] == "BLOKUJ"}, BLOCKED)

if __name__ == "__main__":
    unittest.main()
