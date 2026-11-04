"""Temporary read-only legal PDF probe for batch 13; REMOVE BEFORE MERGE."""
import io
import re
import subprocess
import sys
import unittest
import urllib.request

SOURCES=[
 ("official-03","https://eli.gov.pl/api/acts/DU/2025/642/text/O/D20250642-03.pdf"),
 ("official-38","https://eli.gov.pl/api/acts/DU/2025/642/text/O/D20250642-38.pdf"),
 ("official-39","https://eli.gov.pl/api/acts/DU/2025/642/text/O/D20250642-39.pdf"),
 ("official-53","https://eli.gov.pl/api/acts/DU/2025/642/text/O/D20250642-53.pdf"),
 ("official-54","https://eli.gov.pl/api/acts/DU/2025/642/text/O/D20250642-54.pdf"),
 ("ministry-I","https://www.gov.pl/attachment/8856b22a-bfd8-4567-8386-b9709bba8da7"),
 ("ministry-II","https://www.gov.pl/attachment/b7292c03-ac9d-4f80-9a29-c22f53d847b8"),
]
CLAUSES=["1.4.2.3.2","8.4.1","5.2.1.1","5.2.2.1.1","5.3.2.2.1","5.3.2.2.2","5.3.2.3.1","5.4.3.4"]
class Probe(unittest.TestCase):
 def test_legal_probe(self):
    try:from pypdf import PdfReader
    except ImportError:
      pip=subprocess.run([sys.executable,"-m","pip","install","-q","pypdf"],capture_output=True,text=True,timeout=90)
      if pip.returncode: print("PROBE_PIP_ERROR",pip.stderr[-400:]);return
      from pypdf import PdfReader
    for name,url in SOURCES:
      try:
       with urllib.request.urlopen(url,timeout=20) as r: raw=r.read(18000000)
       if not raw.startswith(b"%PDF"): print("PROBE_NOT_PDF",name,len(raw));continue
       reader=PdfReader(io.BytesIO(raw));print("PROBE_PDF",name,"pages",len(reader.pages),"bytes",len(raw))
       if name.startswith("ministry-"):
         target=([55] if name=="ministry-I" else [239,242,248,250,253,261,262,280,281,636,637])
       else:target=list(range(min(3,len(reader.pages))))
       for index in target:
        if index>=len(reader.pages):continue
        s=reader.pages[index].extract_text(extraction_mode="layout") or ""
        st=" ".join(s.split())
        print("PROBE_PAGE",name,index,"HEAD",st[:100],"TAIL",st[-100:])
        for clause in CLAUSES:
         match=re.search(r"(?<![\d.])"+re.escape(clause)+r"(?:\s+|\s*[\-–])",s)
         if match:
          text=" ".join(s[match.start():match.start()+1100].split())
          print("PROBE_CLAUSE",name,index,clause,text[:950])
      except Exception as ex:print("PROBE_ERROR",name,type(ex).__name__,str(ex)[:220])
