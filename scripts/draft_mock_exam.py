#!/usr/bin/env python3
"""Internal-only proportional 30-question ADR basic practice variant generator."""
import argparse,json,random
from collections import Counter
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];BANK=ROOT/"podstawowy"/"questions.jsonl"
MODULES=[f"ADR-B-{i:02d}" for i in range(1,14)];PASS_MARK=20
def load_bank(path):
 rows=[]
 for n,line in enumerate(path.read_text(encoding="utf-8").splitlines(),1):
  if not line.strip():continue
  try:q=json.loads(line)
  except json.JSONDecodeError as e:raise ValueError(f"{path}:{n}: invalid JSON") from e
  if not isinstance(q,dict) or not isinstance(q.get("id"),str):raise ValueError(f"{path}:{n}: invalid record")
  rows.append(q)
 ids=[q["id"] for q in rows]
 if len(ids)!=len(set(ids)):raise ValueError("duplicate question IDs")
 return rows
def proportional_quotas(rows,size=30):
 counts=Counter(q.get("module_id") for q in rows)
 if any(counts[m]==0 for m in MODULES):raise ValueError("all 13 modules must contain questions")
 total=sum(counts[m] for m in MODULES);remaining=size-len(MODULES);out={};rem={}
 for m in MODULES:
  raw=remaining*counts[m]/total;out[m]=1+int(raw);rem[m]=raw-int(raw)
 for m in sorted(MODULES,key=lambda m:(-rem[m],m))[:size-sum(out.values())]:out[m]+=1
 if sum(out.values())!=size or any(out[m]>counts[m] for m in MODULES):raise ValueError("cannot allocate 30 questions")
 return out
class DeterministicRNG:
 def __init__(self,seed): self.state=seed & 0xffffffff
 def random(self):
  self.state=(1664525*self.state+1013904223)&0xffffffff
  return self.state/4294967296
 def shuffle(self,items):
  for i in range(len(items)-1,0,-1):
   j=int(self.random()*(i+1));items[i],items[j]=items[j],items[i]
 def sample(self,population,k):
  pool=list(population);self.shuffle(pool);return pool[:k]
def draw_exam(rows,seed,exclude_ids=None,variant=1,source_bank_head=None):
 excluded=set(exclude_ids or []);eligible=[q for q in rows if q["id"] not in excluded]
 quotas=proportional_quotas(eligible);rng=DeterministicRNG(seed);selected=[]
 for m in MODULES:selected.extend(rng.sample([q for q in eligible if q.get("module_id")==m],quotas[m]))
 rng.shuffle(selected)
 exam={"schema_version":"1.0","exam_type":"ADR_BASIC_PRACTICE_DRAFT","publication_authorized":False,"legal_review_status":"NOT_APPROVED_ALL_QUESTIONS_NEEDS_REVIEW","seed":seed,"variant":variant,"generated_from":"podstawowy/questions.jsonl","source_bank_head":source_bank_head,"excluded_question_ids":sorted(excluded),"question_count":30,"time_limit_minutes":60,"pass_mark_correct":PASS_MARK,"pass_mark_fraction":"2/3","note":"Internal practice only; not official. All questions remain unapproved.","module_distribution":quotas,"questions":[{"number":i,"id":q["id"],"module_id":q["module_id"],"stem":q["stem"],"options":q["options"],"image":q.get("image")} for i,q in enumerate(selected,1)]}
 key={"schema_version":"1.0","exam_type":"ADR_BASIC_PRACTICE_DRAFT","publication_authorized":False,"seed":seed,"question_count":30,"pass_mark_correct":PASS_MARK,"pass_mark_fraction":"2/3","answers":[{"number":i,"id":q["id"],"correct_option":q["correct_option"],"explanation":q["explanation"],"legal_basis":[s.get("reference","") for s in q.get("sources",[])]} for i,q in enumerate(selected,1)]}
 return exam,key
def run(argv=None):
 p=argparse.ArgumentParser();p.add_argument("--questions",type=Path,default=BANK);p.add_argument("--seed",type=int,default=None);p.add_argument("--variant",type=int,default=1);p.add_argument("--source-head",type=str,default=None);p.add_argument("--exclude",type=Path,default=None,help="existing exam JSON; its question IDs are excluded when possible");p.add_argument("--output",type=Path,required=True);p.add_argument("--key-output",type=Path,required=True);a=p.parse_args(argv)
 rows=load_bank(a.questions);seed=a.seed if a.seed is not None else random.SystemRandom().randrange(1,2**31);excluded=set()
 if a.exclude:
  old=json.loads(a.exclude.read_text(encoding="utf-8"));excluded={q["id"] for q in old.get("questions",[]) if isinstance(q,dict) and isinstance(q.get("id"),str)}
 exam,key=draw_exam(rows,seed,excluded,a.variant,a.source_head);ids=[q["id"] for q in exam["questions"]]
 if len(ids)!=30 or len(set(ids))!=30 or not set(ids)<={q["id"] for q in rows} or set(ids)&excluded:raise ValueError("invalid generated ID set or exclusion collision")
 for path,data in ((a.output,exam),(a.key_output,key)):
  path.parent.mkdir(parents=True,exist_ok=True);path.write_text(json.dumps(data,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 print(f"Draft exam generated; pass >= {PASS_MARK}/30. NOT APPROVED FOR OFFICIAL USE.");return 0
if __name__=="__main__":raise SystemExit(run())
