# Etap 4x335 — klin pod koło a wyłączenie 1.1.3.6

Data: 03.11.2026. Gałąź: `stage4x335-wheel-chock-each-vehicle`. Bazowy main: `c9c7fa49af667c69a16da0d4678f8831aaa44ccb`.

## Zakres i wynik

- Dodano ADR-B-0761 do kompetencji teoretycznej `ADR-B-08-K04` — „Klin pod koło”; liczba pytań w kompetencji: 5→6.
- Pytanie sprawdza granicę wyłączenia: przy prawidłowym zastosowaniu 1.1.3.6.2 część 8 ADR nie stosuje się poza wyjątkami wyraźnie wymienionymi w tym punkcie. 8.1.5.2 (klin) nie jest wśród wyjątków, natomiast 8.1.4.2 (gaśnica) pozostaje wymagany.
- Podstawa: ADR 2025, 1.1.3.6.2; 8.1.5.2; 8.1.4.2.
- Explanation: 408 znaków, 4 zdania; status `needs_review`.

## Audyt odpowiedzi A/B/C

- A — błędna: pomija wyłączenie części 8 przewidziane w 1.1.3.6.2.
- B — poprawna: 8.1.5.2 nie znajduje się w katalogu przepisów części 8, które pozostają stosowane przy tym wyłączeniu.
- C — błędna: 1.1.3.6 nie zwalnia z całego ADR; m.in. 8.1.4.2 dotyczący gaśnicy pozostaje wśród wyjątków.

## Metryki banku po partii

- Bank: **761** pytań, 761 `needs_review`, 0 `verified`; blob SHA `51d30c1588cbb1e78c330876d3e59572aca531ec`.
- Kompetencje teorii z mniej niż 6 pytaniami: **19** (3 praktyczne pominięte).
- Rozkład prawidłowych opcji: A/B/C = **257/275/229**.
- Poprawna odpowiedź jest jedyną najdłuższą: **82/761 = 10,78%**; maksimum działu: **14,61%**.
- Długości opcji A/B/C: **96/93/106**; klucz: **B**.

## Synchronizacja artefaktów

- Klucze i warianty egzaminów próbnych 001–005 wskazują aktualny blob banku.
- Snapshoty: `review/sequential/761-761.json`, `review/legal-clauses/761-761.json`.
- Ledger prawny, kolejki i manifesty pakietu specjalisty zsynchronizowane.
- Rejestr specjalisty: `review/specialist/REJESTR-AKTUALNY-0001-0761.md` (761 unikalnych ID).
- Coverage, README, lekcja B-08 i testy liczebności zaktualizowane.
- Pełne literalne porównanie polskiego tekstu i niezależna recenzja specjalisty pozostają otwarte; żadnego pytania nie oznaczono `verified`.

## Źródło

ADR 2025, Dz.U. 2025 poz. 642, 1.1.3.6.2; 8.1.5.2; 8.1.4.2: https://eli.gov.pl/api/acts/DU/2025/642
