"""Verify batch 14 first-review proposals only on a complete copy of the ADR bank."""
import copy
import json
import re
import unittest
from pathlib import Path
from scripts.check_near_duplicates import find_candidates

ROOT=Path(__file__).resolve().parents[1]
BANK=ROOT/"podstawowy/questions.jsonl"
PROPOSALS=ROOT/"review/literal-pl/POPRAWKI-0196-0210.jsonl"
REPORT=ROOT/"review/literal-pl/PARTIA-0196-0210.json"
EXPECTED={f"ADR-B-{n:04d}" for n in range(196,211)}

def read_jsonl(p):
    return [json.loads(line) for line in p.read_text(encoding="utf-8").splitlines() if line.strip()]

class Batch14FirstReview(unittest.TestCase):
    def test_proposals_on_isolated_bank_copy(self):
        base=read_jsonl(BANK)
        self.assertEqual(len(base),780)
        before={q["id"]:q for q in base}
        proposed=read_jsonl(PROPOSALS)
        self.assertEqual(len(proposed),15)
        self.assertEqual({q["id"] for q in proposed},EXPECTED)
        simulated=copy.deepcopy(before)
        for q in proposed:
            ident=q["id"]
            self.assertEqual(list(q),list(before[ident]))
            self.assertEqual(q["correct_option"],before[ident]["correct_option"])
            self.assertEqual(q["verification_status"],"needs_review")
            self.assertIsNone(q["checked_at"])
            self.assertIsNone(q["reviewer"])
            self.assertEqual(set(q["options"]),{"A","B","C"})
            self.assertEqual(len(set(q["options"].values())),3)
            lengths=[len(value) for value in q["options"].values()]
            key_length=len(q["options"][q["correct_option"]])
            self.assertLessEqual(max(lengths),80,ident)
            self.assertFalse((key_length==max(lengths) or key_length==min(lengths)) and lengths.count(key_length)==1,ident)
            exp=q["explanation"].strip()
            self.assertGreaterEqual(len(exp),300,ident)
            sentences=re.split(r"(?<=[.!?])\s+",exp)
            self.assertTrue(2<=len(sentences)<=5,(ident,len(sentences)))
            self.assertTrue(all(len(s.split())<=35 for s in sentences),ident)
            self.assertRegex(exp,r"Podstawa: ADR .+\.$")
            self.assertTrue(q["sources"])
            simulated[ident]=q
        self.assertEqual(len(simulated),780)
        self.assertTrue(all(q["verification_status"]=="needs_review" for q in simulated.values()))
        self.assertTrue(all(q["reviewer"] is None and q["checked_at"] is None for q in simulated.values()))
        new_pairs=[]
        for a,b,score in find_candidates(list(simulated.values()),threshold=0.60):
            if a in EXPECTED or b in EXPECTED:
                new_pairs.append((a,b,round(score,3)))
        self.assertEqual(new_pairs,[],f"New near-duplicates: {new_pairs[:10]}")
    def test_report_and_counter(self):
        o=json.loads(REPORT.read_text(encoding="utf-8"))
        self.assertEqual(o["previous_uncompared"],558)
        self.assertEqual(o["remaining_without_comparison"],543)
        self.assertEqual(o["counts"],{"OK":0,"POPRAW":15,"BLOKUJ":0})
        self.assertEqual(len(o["records"]),15)
        self.assertEqual({q["id"] for q in o["records"]},EXPECTED)
        self.assertTrue(all(q["quote"] and q["clause"] and q["page"] for q in o["records"]))

if __name__=="__main__":
    unittest.main()
