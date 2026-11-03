# Etap 4x332 — odpowiedzialność za szkodę wyrządzoną osobie trzeciej

Data: 03.11.2026. Gałąź: `stage4x332-third-party-civil-liability`. Bazowy main: `9a1a844eae8fa99bdcfc6f6b9ca52335fa22f9a3`.

- Dodano ADR-B-0758 do kompetencji `ADR-B-07-K07` — rozróżnienie odpowiedzialności deliktowej i umownej; K07: 5→6.
- Podstawa: ADR 2025, 8.2.2.3.2(k) (ogólne informacje o odpowiedzialności cywilnej); Kodeks cywilny, t.j. Dz.U. 2026 poz. 795, art. 415 i 471.
- Bank: **758** pytań (ADR-B-0001–0758), 758 `needs_review`, 0 `verified`; SHA `2b708a1f1c72732bb6b50a067d94fcbac1032a06`.
- Moduł ADR-B-07: **54** pytania.
- Rozkład kluczy A/B/C: **256/273/229**.
- „Poprawna odpowiedź jest jedyną najdłuższą”: **81/758 = 10,69%**; maksimum działu **14,61%**.
- Długości opcji A/B/C: **97/98/94**; poprawna A nie jest najdłuższa.
- Explanation: **452 znaki, 4 zdania**.
- Kompetencje teorii z mniej niż 6 pytaniami: **22** (3 praktyczne pominięte).

## Pytanie ADR-B-0758

Podczas rozładunku kierowca przez nieuwagę uszkadza sprzęt pracownika magazynu, który nie jest stroną umowy przewozu. Którą ogólną zasadę odpowiedzialności cywilnej należy rozważyć?

A. Odpowiedzialność za czyn niedozwolony, ponieważ szkoda została wyrządzona z winy osobie trzeciej.

B. Wyłącznie odpowiedzialność umowną z art. 471, ponieważ każda szkoda przy przewozie wynika z umowy.

C. Wyłącznie odpowiedzialność administracyjną, ponieważ zdarzenie nastąpiło podczas przewozu ADR.

Pracownik magazynu nie jest stroną umowy przewozu, więc nie dochodzi od przewoźnika wykonania tej umowy. Jeśli szkoda została wyrządzona z winy, należy rozważyć odpowiedzialność za czyn niedozwolony na podstawie przepisu 415 Kodeksu cywilnego; trzeba jeszcze ocenić wszystkie przesłanki. Przepis 471 dotyczy szkody wynikłej z niewykonania lub nienależytego wykonania zobowiązania, a kara administracyjna nie jest odszkodowaniem. Podstawa: ADR 2025, 8.2.2.3.2(k); Kodeks cywilny, przepisy 415 i 471.

## Audyt A/B/C i źródła

- A — poprawna: poszkodowany nie jest stroną umowy przewozu; przy zawinionym wyrządzeniu szkody należy rozważyć odpowiedzialność deliktową z art. 415 KC.
- B — błędna: art. 471 KC dotyczy szkody wynikłej z niewykonania lub nienależytego wykonania zobowiązania; nie każda szkoda przy przewozie jest roszczeniem umownym poszkodowanego.
- C — błędna: sankcja administracyjna i cywilne odszkodowanie to odrębne kwestie; przewóz ADR nie wyłącza odpowiedzialności cywilnej.
- Źródła: ADR 2025, 8.2.2.3.2(k), Dz.U. 2025 poz. 642 — https://eli.gov.pl/api/acts/DU/2025/642/text.pdf; Kodeks cywilny, t.j. Dz.U. 2026 poz. 795, art. 415 i 471 — https://api.sejm.gov.pl/eli/acts/DU/2026/795/text.pdf.
- Pytanie ma charakter edukacyjny; nie rozstrzyga automatycznie odpowiedzialności konkretnego kierowcy lub przewoźnika. Status pozostaje `needs_review`; nie oznaczono żadnego pytania jako `verified`.

## Synchronizacja artefaktów

Klucze i warianty egzaminów próbnych 001–005 wskazują SHA bieżącego banku. Snapshoty `review/sequential/758-758.json` i `review/legal-clauses/758-758.json` zawierają ADR-B-0758. Zaktualizowano ledger prawny, manifesty pakietu specjalisty, kolejki, rejestr bieżący i rejestr partii, coverage, README, lekcję B-07 oraz testy liczebności. Pełne literalne porównanie tekstu polskiego i niezależna recenzja specjalisty pozostają otwarte.
