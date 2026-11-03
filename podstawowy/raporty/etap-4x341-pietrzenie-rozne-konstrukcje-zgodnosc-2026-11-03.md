# Etap 4x341 — zgodność piętrzenia różnych konstrukcji opakowań (ADR 7.5.7.2)

Data: 03.11.2026. Gałąź: `stage4x341-stacking-compatibility-assessment`. Bazowy main: `db6e024fea2743b2d5aef4e91b120f9f81ae4019`.

## Zakres i wynik

- Dodano ADR-B-0767 do kompetencji teoretycznej `ADR-B-09-K05` — „Piętrzenie opakowań”; liczba pytań: 5→6.
- Dwa typy opakowań mogą być osobno przeznaczone do piętrzenia, ale przed połączeniem ich w jeden stos trzeba ocenić wzajemną zgodność konstrukcji. Samo oznaczenie każdego typu osobno ani pas mocujący nie zastępują tej oceny.
- Podstawa: ADR 2025, 7.5.7.2 (Dz.U. 2025 poz. 642).
- Explanation: 415 znaków, 4 zdania; status `needs_review`.

## Audyt odpowiedzi A/B/C

- A — błędna: indywidualna możliwość piętrzenia nie potwierdza zgodności różnych typów ze sobą.
- B — poprawna: przed wspólnym piętrzeniem trzeba ocenić wzajemną zgodność konstrukcji.
- C — błędna: ułożenie według masy i spięcie pasem nie zastępują oceny zgodności.

## Metryki banku po partii

- Bank: **767** pytań, 767 `needs_review`, 0 `verified`; blob SHA `701e9768435d9ca39f34690386dfa10482f86da8`.
- Kompetencje teorii z mniej niż 6 pytaniami: **13** (3 praktyczne pominięte).
- Moduł ADR-B-09: **60** pytań.
- Rozkład prawidłowych opcji: A/B/C = **257/281/229**.
- Poprawna odpowiedź jest jedyną najdłuższą: **83/767 = 10,82%**; maksimum działu: **14,61%**.

## Synchronizacja artefaktów

- Klucze i warianty egzaminów próbnych 001–005 wskazują aktualny blob banku.
- Snapshoty: `review/sequential/767-767.json`, `review/legal-clauses/767-767.json`.
- Ledger prawny i rejestr specjalisty uzupełnione; status pozostaje `needs_review`.
- Pełne literalne porównanie polskiego tekstu i niezależna recenzja specjalisty pozostają otwarte.

## Źródło

ADR 2025, Dz.U. 2025 poz. 642, 7.5.7.2: https://eli.gov.pl/api/acts/DU/2025/642
