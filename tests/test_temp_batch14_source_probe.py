"""Temporary read-only ADR 2025 source excerpt probe, remove before merge."""
import io, subprocess, sys, unittest, urllib.request, re
URLS={
 "I":"https://www.gov.pl/attachment/8856b22a-bfd8-4567-8386-b9709bba8da7",
 "II":"https://www.gov.pl/attachment/b7292c03-ac9d-4f80-9a29-c22f53d847b8",
}
WANTED={
 "I":{ "1.1.4.2":range(12,43),"1.1.4.3":range(12,43),"1.9.5.2.2":range(80,145),"3.4.13":range(660,692)},
 "II":{"5.2.1.1":range(232,254),"5.4.1.1.7":range(268,281),"5.4.2":range(274,282),"5.4.3.4":range(279,284),
 "7.5.1.2":range(604,619),"7.5.2.1":range(604,620),"7.5.7.1":range(610,625),"7.5.8.2":range(610,625),
 "8.1.2.2":range(620,638),"8.1.4.2":range(620,640),"8.3.1":range(636,653),"8.6.3.3":range(637,662),"8.6.4":range(637,662)}}
class LegalProbe(unittest.TestCase):
 def test_extract(self):
  try:from pypdf import PdfReader
  except ImportError:
   r=subprocess.run([sys.executable,"-m","pip","install","-q","pypdf"],capture_output=True,text=True,timeout=90)
   if r.returncode:print("ADRPROBE_PIP",r.stderr[-200:]);return
   from pypdf import PdfReader
  for vol,url in URLS.items():
   try:
    with urllib.request.urlopen(url,timeout=35) as f: raw=f.read(19000000)
    pdf=PdfReader(io.BytesIO(raw));print("ADRPROBE_SOURCE",vol,len(raw),len(pdf.pages))
    indexes=sorted(set(k for span in WANTED[vol].values() for k in span if k<len(pdf.pages)))
    for i in indexes:
     t=pdf.pages[i].extract_text(extraction_mode="layout") or ""
     for clause,allowed in WANTED[vol].items():
      if i not in allowed:continue
      hits=list(re.finditer(r"(?m)^\s*"+re.escape(clause)+r"(?:\s|$)",t))
      if not hits:continue
      hit=hits[0]
      text=" ".join(t[hit.start():hit.start()+1150].split())
      head=" ".join(t[:80].split())
      print("ADRPROBE_EXCERPT",vol,clause,"PDF_INDEX",i,"EST_DZU",i+(2 if vol=="I" else 694),"HEAD",head,"TEXT",text[:950])
   except Exception as e:print("ADRPROBE_FAIL",vol,type(e).__name__,str(e)[:300])
