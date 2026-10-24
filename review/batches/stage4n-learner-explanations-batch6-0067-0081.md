# Etap 4n — partia 6: pytania 0067–0081

24.10.2026. Fresh main po scalonym PR #175: 545 pytań, 545 needs_review, 0 verified, brak otwartych PR. Zredagowano 15 kolejnych explanation (0067–0081), każde 297–352 znaki: sens właściwej opcji wyjaśniony dla początkującego, następnie dlaczego pozostałe warianty nie pasują, na końcu krótka podstawa ADR. Zmiany wyłącznie w explanation; bez ingerencji w A/B/C, key, stem, image, sources, verification_status.

Synchronizacja dokładnych wpisów wyłącznie dla 0067–0081 w review/sequential/061-090.json oraz review/legal-clauses/061-090.json. Nie stwierdzono potwierdzonego błędu podstawy prawnej wymagającego osobnego PR; bez niezależnego i literalnego sprawdzenia Dz.U. 642 + 1575 status pozostaje needs_review. Po scaleniu etap 4n obejmie 81/545 pytań. Bez innych kursów. Etap 4m nadal otwarty; dalsze B10 30/55, globalnie 333/545.

## Korekta po pierwszym CI

Pierwszy Quality Gate #1507 zakończył się FAIL w jednostkowym teście regresji 0073: test wymaga dokładnego ciągu „nie jest wymaganym minimum”. W explanation 0073 przywrócono tę frazę bez zmiany znaczenia (minimum nadal 2 kg, gaśnica 6 kg może spełniać wymóg). Zaktualizowano audyty i ponowiono Quality Gate. Nie obniżono ani nie pominięto testu.
