# Etap 4x309 — rozlew: dokumenty w kabinie, strona nawietrzna

2026-11-02. Bazowy main `62eb3b1e1fd8ed75d29241650c87aceb3a5cbc04`; gałąź `stage4x309-spill-upwind-documents`.

- Dodano ADR-B-0735 do `ADR-B-03-K05`: unikanie skażenia przy rozlewie, konflikt między dostępem do dokumentów a przejściem przez strefę rozlewu i oparów.
- Kompetencja wzrosła z 5 do 6 pytań; kompetencje teorii z mniej niż 6 pytaniami: **45** (3 praktyczne pominięte).
- Bank: 735 pytań (ADR-B-0001–0735), 735 `needs_review`, 0 `verified`; SHA `9c6375775b1f40f18aad9124aa6b963e752ebb64`.
- Moduł ADR-B-03: 60 pytań.
- Rozkład kluczy A/B/C: 246/264/225.
- „Poprawna odpowiedź jest jedyną najdłuższą”: **81/735 = 11,02%**; maksimum działu **14,61%**. Długości opcji ADR-B-0735: A=169, B=185, C=180; poprawna A nie jest najdłuższa.
- Explanation: 430 znaków, 4 zdania. A nakazuje pozostać poza skażonym obszarem, przejść na stronę nawietrzną i wskazać służbom miejsce dokumentów; B błędnie uznaje, że rękawice uzasadniają wejście w rozlew; C nakazuje pozostać po stronie zawietrznej przy pojeździe.
- Podstawa: ADR 2025, 5.4.3.4 — model instrukcji pisemnych: dostępność dokumentów dla ratowników, zakaz wchodzenia w rozlew, unikanie oparów przez pozostanie po stronie nawietrznej, oddalenie się i ostrzeżenie innych. Status `needs_review`; pełne literalne porównanie i niezależna recenzja pozostają otwarte.
- Odświeżono klucze i warianty 001–005, snapshoty sequential/legal 735, ledger, manifesty, kolejki prawne, rejestr specjalisty, coverage, lekcję B-03, README i testy regresji.

## Pytanie ADR-B-0735

Po awarii kierowca widzi, że dokumenty przewozowe pozostały w kabinie. Jedyna droga do pojazdu prowadzi przez rozlew, a wiatr niesie opary w jego stronę. Co powinien zrobić, aby ograniczyć ryzyko skażenia i postąpić zgodnie z instrukcjami pisemnymi ADR?

A. Nie wchodzić w rozlew ani opary; odejść na stronę nawietrzną, ostrzec innych i wskazać służbom miejsce dokumentów. Udostępnić je dopiero wtedy, gdy będzie to bezpieczne.

B. Założyć rękawice ochronne z wyposażenia, przejść najkrótszą drogą przez rozlew i zabrać dokumenty; ich natychmiastowa dostępność dla ratowników ma pierwszeństwo przed ryzykiem skażenia.

C. Zostać przy pojeździe po stronie zawietrznej, pilnować kabiny i czekać na ustąpienie oparów; pozostanie przy ładunku ograniczy dostęp osób postronnych i pozwoli zachować dokumenty.

Instrukcje pisemne wymagają, by dokumenty były dostępne dla ratowników, ale nie nakazują narażać załogi na wejście w rozlew. Nie wolno chodzić po rozlanej substancji ani wdychać oparów; trzeba oddalić się na stronę nawietrzną, ostrzec innych i przekazać służbom, gdzie znajdują się dokumenty. Przejście przez rozlew w rękawicach nie jest bezpieczne, a pozostawanie po stronie zawietrznej zwiększa narażenie. Podstawa: ADR 5.4.3.4.

## Audyt A/B/C i źródła

- A — poprawna: łączy zakaz wchodzenia w rozlew z pozostaniem po stronie nawietrznej i ostrzeżeniem innych; dokumenty mają być dostępne dla ratowników, ale bez narażania załogi.
- B — błędna: rękawice nie znoszą zakazu wchodzenia w rozlew ani ryzyka nieznanych oparów.
- C — błędna: pozostawanie po stronie zawietrznej i przy rozlewie zwiększa narażenie, zamiast oddalić załogę.
- Źródło: Dz.U. 2025 poz. 642, ADR 2025, 5.4.3.4 — https://dziennikustaw.gov.pl/DU/2025/642. Model instrukcji pisemnych UNECE: https://unece.org/transport/road-transport/linguistic-versions-adr-instructions-writing.
- Nie oznaczono żadnego pytania jako `verified`.
