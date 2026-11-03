# Etap 4x344 — wyłączenie z odstępstwa ADR 1.1.4.2.1 (IMDG/ICAO)

Data: 03.11.2026. Gałąź: `stage4x344-multimodal-derogation-exclusion`. Bazowy main: `5bfbe4b5112ea8fcc559065378537986368ed2a4`.

## Zakres i wynik

- Dodano ADR-B-0770 do kompetencji teoretycznej `ADR-B-10-K02` — „Dodatkowy wpis w dokumencie przy 1.1.4.2.1”; liczba pytań: 5→6.
- Pytanie sprawdza wyraźne wyłączenie z 1.1.4.2.1: nie można stosować odstępstwa do towarów niebezpiecznych według ADR, które według IMDG Code lub ICAO Technical Instructions są uznawane za niebędące towarami niebezpiecznymi. Wpis 5.4.1.1.7 nie tworzy samodzielnie prawa do odstępstwa.
- Podstawa: ADR 2025, 1.1.4.2.1 i 5.4.1.1.7 (Dz.U. 2025 poz. 642).
- Explanation: 437 znaków / 4 zdania; status `needs_review`.

## Audyt odpowiedzi A/B/C

- A — błędna: sam przewóz morski nie uchyla wyraźnego wyłączenia.
- B — poprawna: wskazana kategoria towarów nie może korzystać z odstępstwa 1.1.4.2.1.
- C — błędna: wpis w dokumencie nie legalizuje zastosowania wyłączonego odstępstwa.

## Metryki banku po partii

- Bank: **770** pytań, 770 `needs_review`, 0 `verified`; blob SHA `d96529ee430bb92d93c6067033a90470e51861b7`.
- Kompetencje teorii z mniej niż 6 pytaniami: **10** (3 praktyczne pominięte).
- Moduł ADR-B-10: **57** pytań.
- Rozkład prawidłowych opcji: A/B/C = **257/284/229**.
- Poprawna odpowiedź jest jedyną najdłuższą: **83/770 = 10,78%**; maksimum działu: **14,61%**.

## Synchronizacja artefaktów

- Klucze i warianty egzaminów próbnych 001–005 wskazują aktualny blob banku.
- Snapshoty: `review/sequential/770-770.json`, `review/legal-clauses/770-770.json`.
- Ledger prawny i rejestr specjalisty uzupełnione; status pozostaje `needs_review`.
- Pełne literalne porównanie polskiego tekstu i niezależna recenzja specjalisty pozostają otwarte.

## Źródło

ADR 2025, Dz.U. 2025 poz. 642, 1.1.4.2.1 i 5.4.1.1.7: https://eli.gov.pl/api/acts/DU/2025/642
