"""Check batch 13 first-pass proposals against an isolated copy of the live ADR bank."""
import copy
import json
import re
import unittest
from pathlib import Path
from scripts.check_near_duplicates import find_candidates
ROOT=Path(__file__).resolve().parents[1]
BANK=ROOT/"podstawowy/questions.jsonl"
PATCHES=ROOT/"review/literal-pl/POPRAWKI-0181-0195.jsonl"
REPORT=ROOT/"review/literal-pl/PARTIA-0181-0195.json"
EXPECTED={f"ADR-B-{n:04d}" for n in range(181,196)}

def read_jsonl(path):
    return [json.loads(s) for s in path.read_text(encoding="utf-8").splitlines() if s.strip()]

class Batch13LiteralProposalTests(unittest.TestCase):
    def test_proposals_only_on_bank_copy(self):
        base=read_jsonl(BANK);self.assertEqual(len(base),780)
        before={r["id"]:r for r in base}
        proposals=read_jsonl(PATCHES)
        self.assertEqual(len(proposals),15)
        self.assertEqual({r["id"] for r in proposals},EXPECTED)
        simulated=copy.deepcopy(before)
        for q in proposals:
            ident=q["id"];old=before[ident]
            self.assertEqual(list(q),list(old))
            self.assertEqual(q["correct_option"],old["correct_option"])
            self.assertEqual(q["verification_status"],"needs_review")
            self.assertIsNone(q["checked_at"])
            self.assertIsNone(q["reviewer"])
            self.assertEqual(set(q["options"]),{"A","B","C"})
            self.assertEqual(len(set(q["options"].values())),3)
            lengths={k:len(v) for k,v in q["options"].items()}
            key_len=lengths[q["correct_option"]]
            self.assertLessEqual(max(lengths.values()),80,ident)
            self.assertFalse(key_len==max(lengths.values()) and list(lengths.values()).count(key_len)==1,ident)
            self.assertFalse(key_len==min(lengths.values()) and list(lengths.values()).count(key_len)==1,ident)
            exp=q["explanation"].strip()
            self.assertGreaterEqual(len(exp),300,ident)
            sentences=re.split(r"(?<=[.!?])\s+",exp)
            self.assertTrue(2<=len(sentences)<=5,ident)
            self.assertTrue(all(len(s.split())<=35 for s in sentences),ident)
            self.assertRegex(exp,r"Podstawa: ADR .+\.$")
            self.assertTrue(q["sources"])
            simulated[ident]=q
        changed=[ident for ident in EXPECTED if before[ident]!=simulated[ident]]
        self.assertEqual(len(changed),15)
        self.assertEqual(len(simulated),780)
        self.assertTrue(all(x["verification_status"]=="needs_review" for x in simulated.values()))
        candidates=find_candidates(list(simulated.values()),threshold=0.60)
        self.assertEqual(candidates,[],f"New near-duplicate pairs: {candidates[:5]}")

    def test_report_complete_and_still_pending_second_review(self):
        report=json.loads(REPORT.read_text(encoding="utf-8"))
        self.assertEqual(report["previous_uncompared"],573)
        self.assertEqual(report["remaining_without_comparison"],558)
        self.assertEqual(len(report["records"]),15)
        self.assertEqual({x["id"] for x in report["records"]},EXPECTED)
        self.assertEqual(sum(report["counts"].values()),15)
        self.assertEqual(report["verified"],0)

if __name__=="__main__":
    unittest.main()
