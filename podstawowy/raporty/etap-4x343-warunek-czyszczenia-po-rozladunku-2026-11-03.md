# Etap 4x343 — warunek czyszczenia po rozładunku (ADR 7.5.8.1)

Data: 03.11.2026. Gałąź: `stage4x343-cleaning-trigger-after-spill`. Bazowy main: `45f98a6d1d1ae0b3e29641444c75dc679f85d356`.

## Zakres i wynik

- Dodano ADR-B-0769 do kompetencji teoretycznej `ADR-B-09-K07` — „Czyszczenie pojazdu po rozładunku, także po wycieku”; liczba pytań: 5→6.
- Pytanie rozróżnia samo zakończenie przewozu sztuk przesyłek ADR od sytuacji, w której po rozładunku stwierdzono uwolnienie części zawartości. Szczególny obowiązek czyszczenia z 7.5.8.1 uruchamia właśnie stwierdzenie uwolnienia zawartości.
- Podstawa: ADR 2025, 7.5.8.1 (Dz.U. 2025 poz. 642).
- Explanation: 412 znaków / 4 zdania; status `needs_review`.

## Audyt odpowiedzi A/B/C

- A — błędna: 7.5.8.1 nie ustanawia automatycznego czyszczenia po każdym przewozie opakowanych towarów.
- B — poprawna: warunkiem jest stwierdzenie, że część zawartości wydostała się z opakowania.
- C — błędna: sucha podłoga nie uchyla obowiązku, jeśli wyciek został wcześniej stwierdzony.

## Metryki banku po partii

- Bank: **769** pytań, 769 `needs_review`, 0 `verified`; blob SHA `1e385ca71f77ac772ac24945c370db41679752b7`.
- Kompetencje teorii z mniej niż 6 pytaniami: **11** (3 praktyczne pominięte).
- Moduł ADR-B-09: **62** pytania.
- Rozkład prawidłowych opcji: A/B/C = **257/283/229**.
- Poprawna odpowiedź jest jedyną najdłuższą: **83/769 = 10,79%**; maksimum działu: **14,61%**.

## Synchronizacja artefaktów

- Klucze i warianty egzaminów próbnych 001–005 wskazują aktualny blob banku.
- Snapshoty: `review/sequential/769-769.json`, `review/legal-clauses/769-769.json`.
- Ledger prawny i rejestr specjalisty uzupełnione; status pozostaje `needs_review`.
- Pełne literalne porównanie polskiego tekstu i niezależna recenzja specjalisty pozostają otwarte.

## Źródło

ADR 2025, Dz.U. 2025 poz. 642, 7.5.8.1: https://eli.gov.pl/api/acts/DU/2025/642
