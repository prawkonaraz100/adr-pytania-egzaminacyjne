"""Temporary locator for real official Dziennik Ustaw PDF parts; remove before merge."""
import re,unittest,urllib.request,html as htmlmod
URL="https://www.dziennikustaw.gov.pl/DU/rok/2025/pozycja/642"
class Probe(unittest.TestCase):
 def test_link_metadata(self):
  try:
   with urllib.request.urlopen(URL,timeout=20) as r: doc=r.read(500000).decode("utf-8","replace")
   for no in [1,2,3,19,38,39,53,54]:
    matches=list(re.finditer(r"plik\s+"+str(no)+r"(?!\d)",doc,re.I))
    for x in matches[:1]:
     snip=" ".join(doc[max(0,x.start()-1000):x.end()+300].split())
     print("OFFICIAL_LINK",no,snip[:1600])
   for href in sorted(set(re.findall(r'(?:https?://)?[A-Za-z0-9/:._?&=%-]*20250000642[0-9]{2}\.pdf',doc))):
    print("OFFICIAL_HREF",htmlmod.unescape(href))
  except Exception as e:print("OFFICIAL_ERROR",str(e))
