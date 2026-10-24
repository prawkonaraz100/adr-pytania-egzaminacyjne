#!/usr/bin/env python3
"""Answer-length bias metric: advisory by default; strict release mode available."""
import argparse
import json
from collections import defaultdict
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
def measure(rows):
    groups=defaultdict(lambda:{"total":0,"strict":0,"tied":0})
    for q in rows:
        opts=q["options"]
        lengths={k:len(v.strip()) for k,v in opts.items()}
        maximum=max(lengths.values())
        group=groups[q["module_id"]]
        group["total"]+=1
        if lengths[q["correct_option"]]==maximum:
            if sum(v==maximum for v in lengths.values())==1:
                group["strict"]+=1
            else:
                group["tied"]+=1
    return dict(sorted(groups.items()))

def check(rows,limit=0.40):
    stats=measure(rows)
    total=sum(v["total"] for v in stats.values())
    strict=sum(v["strict"] for v in stats.values())
    blocked=total>0 and strict/total>limit
    blocked_modules=[k for k,v in stats.items() if v["strict"]/v["total"]>limit]
    return stats,strict,total,blocked,blocked_modules

def main(argv=None):
    p=argparse.ArgumentParser()
    p.add_argument("--questions",type=Path,default=ROOT/"podstawowy/questions.jsonl")
    p.add_argument("--threshold",type=float,default=.40)
    p.add_argument("--strict",action="store_true",help="Fail if the global target or any module target is exceeded")
    p.add_argument("--strict-global",action="store_true",help="Fail only if the global strictly-longest rate exceeds the threshold")
    a=p.parse_args(argv)
    rows=[json.loads(line) for line in a.questions.read_text(encoding="utf8").splitlines() if line.strip()]
    groups,num,den,over,modules=check(rows,a.threshold)
    print(f"Answer length bias: strictly longest correct={num}/{den} ({num/den:.1%}), target <= {a.threshold:.0%}")
    for k,v in groups.items():
        print(f"  {k}: {v['strict']}/{v['total']} ({v['strict']/v['total']:.1%}) strict; ties={v['tied']}")
    if over or modules:
        print("WARNING: correct-answer length bias threshold unmet globally or by module")
        if modules: print("  Modules:",", ".join(modules))
    if a.strict and (over or modules):
        print("FAIL: --strict requires both global and all 13 modules within threshold")
        return 1
    if a.strict_global and over:
        print("FAIL: --strict-global requires the global strictly-longest rate to be within threshold")
        return 1
    return 0

if __name__=="__main__":
    raise SystemExit(main())
