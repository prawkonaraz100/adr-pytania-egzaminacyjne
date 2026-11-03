# Etap 4x336 — przenośna lampa i metalowa powierzchnia przy 1.1.3.6

Data: 03.11.2026. Gałąź: `stage4x336-vest-and-portable-lighting-per-crew`. Bazowy main: `7c5dd6954346746f1c1d0299ebdc4cd3b2890697`.

## Zakres i wynik

- Dodano ADR-B-0762 do kompetencji teoretycznej `ADR-B-08-K05` — „Kamizelki i latarki dla członków załogi”; liczba pytań w kompetencji: 5→6.
- Pytanie rozróżnia obowiązek przewożenia lampy z 8.1.5.2 od odrębnego ograniczenia jej używania z 8.3.4. Przy wyłączeniu 1.1.3.6.2 punkt 8.3.4 pozostaje stosowany.
- Podstawa: ADR 2025, 1.1.3.6.2; 8.3.4; 8.1.5.2.
- Explanation: 353 znaki, 3 zdania; status `needs_review`.

## Audyt odpowiedzi A/B/C

- A — błędna: 1.1.3.6.2 nie wyłącza całej części 8; pozostawia m.in. 8.3.4.
- B — poprawna: 8.3.4 nadal obowiązuje i zakazuje używanej lampy z metalową powierzchnią mogącą wywołać iskry.
- C — błędna: sama przenośność i sprawność lampy nie wystarczają; jej powierzchnia nie może stwarzać ryzyka iskrzenia.

## Metryki banku po partii

- Bank: **762** pytań, 762 `needs_review`, 0 `verified`; blob SHA `e1e944f3836c9b523c11148b3a7811c013cb6cfa`.
- Kompetencje teorii z mniej niż 6 pytaniami: **18** (3 praktyczne pominięte).
- Rozkład prawidłowych opcji: A/B/C = **257/276/229**.
- Poprawna odpowiedź jest jedyną najdłuższą: **82/762 = 10,76%**; maksimum działu: **14,61%**.
- Długości opcji A/B/C: **95/109/109**; klucz: **B** (remis długości z C).

## Synchronizacja artefaktów

- Klucze i warianty egzaminów próbnych 001–005 wskazują aktualny blob banku.
- Snapshoty: `review/sequential/762-762.json`, `review/legal-clauses/762-762.json`.
- Ledger prawny, kolejki i manifesty pakietu specjalisty zsynchronizowane.
- Rejestr specjalisty: `review/specialist/REJESTR-AKTUALNY-0001-0762.md` (762 unikalne ID).
- Coverage, README, lekcja B-08 i testy liczebności zaktualizowane.
- Pełne literalne porównanie polskiego tekstu i niezależna recenzja specjalisty pozostają otwarte; żadnego pytania nie oznaczono `verified`.

## Źródło

ADR 2025, Dz.U. 2025 poz. 642, 1.1.3.6.2; 8.3.4; 8.1.5.2: https://eli.gov.pl/api/acts/DU/2025/642
