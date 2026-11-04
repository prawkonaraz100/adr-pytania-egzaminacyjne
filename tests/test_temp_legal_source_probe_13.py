"""Temporary official Dziennik Ustaw link discovery; remove before merge."""
import re,unittest,urllib.request
URL="https://www.dziennikustaw.gov.pl/DU/rok/2025/pozycja/642"
class Probe(unittest.TestCase):
 def test_official_links(self):
  try:
   with urllib.request.urlopen(URL,timeout=20) as r:html=r.read(500000).decode("utf-8","replace")
   print("LINKPROBE_LENGTH",len(html))
   for token in ["plik 1","plik 19","plik 38","plik 53","D20250642-","D20250642"]:
    p=html.find(token)
    print("LINKPROBE_TOKEN",token,p,html[max(0,p-250):p+250].replace("\n"," ") if p>=0 else "")
   for x in re.findall(r'<a[^>]+href="[^"]+"[^>]*>[^<]*</a>',html,re.I)[:70]:
    if ".pdf" in x.lower() or "plik" in x.lower():print("LINKPROBE_ANCHOR",x[:700])
  except Exception as ex:print("LINKPROBE_ERROR",str(ex))
