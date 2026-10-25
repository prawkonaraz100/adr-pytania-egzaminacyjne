#!/usr/bin/env python3
"""Advisory lexical/shortest-answer leakage metrics; never marks ADR legal review."""
import argparse
import json
import re
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ABSOLUTE = re.compile(r"(?<!\w)(?:zawsze|nigdy|wyłącznie|tylko|jedynie|każdy|żaden|całkowicie|niezależnie|bez\s+względu)(?!\w)",re.IGNORECASE)

def measure(rows):
    groups=defaultdict(lambda:{"questions":0,"shortest":0,"longest":0,"correct_abs":0,"wrong_abs":0,"wrong_options":0,"only_wrong_abs":0})
    for q in rows:
        g=groups[q["module_id"]]
        opts=q["options"]; key=q["correct_option"]; correct=opts[key]
        wrong=[v for k,v in opts.items() if k!=key]
        lengths=[len(x.strip()) for x in wrong]
        g["questions"]+=1
        g["shortest"]+=len(correct.strip())<min(lengths)
        g["longest"]+=len(correct.strip())>max(lengths)
        ca=bool(ABSOLUTE.search(correct)); wa=sum(bool(ABSOLUTE.search(v)) for v in wrong)
        g["correct_abs"]+=ca;g["wrong_abs"]+=wa;g["wrong_options"]+=len(wrong)
        g["only_wrong_abs"]+=not ca and wa>0
    return dict(sorted(groups.items()))

def format_row(label,g):
    n=g["questions"]; wrong=g["wrong_options"]
    s=g["shortest"]/n if n else 0
    l=g["longest"]/n if n else 0
    c=g["correct_abs"]/n if n else 0
    w=g["wrong_abs"]/wrong if wrong else 0
    return f"{label}: shortest={g['shortest']}/{n} ({s:.2%}), longest={g['longest']}/{n} ({l:.2%}), absolute correct={g['correct_abs']}/{n} ({c:.2%}), absolute distractors={g['wrong_abs']}/{wrong} ({w:.2%}), gap={w-c:+.2%}, only-distractors={g['only_wrong_abs']}"

def main(argv=None):
    parser=argparse.ArgumentParser()
    parser.add_argument("--questions",type=Path,default=ROOT/"podstawowy/questions.jsonl")
    args=parser.parse_args(argv)
    rows=[json.loads(line) for line in args.questions.read_text(encoding="utf8").splitlines() if line.strip()]
    groups=measure(rows)
    totals={k:sum(g[k] for g in groups.values()) for k in next(iter(groups.values()))} if groups else {}
    print("Stage 4v, advisory only; strict shortest and longest exclude ties.")
    print("Absolute-word matching is case-insensitive and matches whole words/phrase; percentages use correct options vs all incorrect options.")
    print(format_row("GLOBAL",totals))
    for k,g in groups.items(): print(format_row(k,g))
    return 0

if __name__=="__main__":
    raise SystemExit(main())
