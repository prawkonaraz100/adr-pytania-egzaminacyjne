# Etap 4x340 — strzałki kierunkowe na dwóch przeciwległych bokach (ADR 5.2.1.10.1)

Data: 03.11.2026. Gałąź: `stage4x340-orientation-arrows-two-sides`. Bazowy main: `6f036ce9af9216846b2038f03d1c49e7506b2627`.

## Zakres i wynik

- Dodano ADR-B-0766 do kompetencji teoretycznej `ADR-B-09-K04` — „Strzałki kierunkowe”; liczba pytań: 5→6.
- Opakowanie kombinowane z opakowaniami wewnętrznymi zawierającymi 750 ml cieczy musi mieć strzałki kierunkowe na dwóch przeciwległych pionowych bokach, skierowane dokładnie ku górze.
- Podstawa: ADR 2025, 5.2.1.10.1–5.2.1.10.3 (Dz.U. 2025 poz. 642).
- Explanation: 437 znaków; status `needs_review`.

## Audyt odpowiedzi A/B/C

- A — błędna: jeden bok nie wystarcza; oznakowanie ma być na dwóch przeciwległych pionowych bokach.
- B — poprawna: wskazuje właściwe położenie i kierunek strzałek.
- C — błędna: boki sąsiednie nie są przeciwległe, a strzałki nie mogą wskazywać w bok.

## Metryki banku po partii

- Bank: **766** pytań, 766 `needs_review`, 0 `verified`; blob SHA `c239993abadeca16db4e1df9a1706f9d47276517`.
- Kompetencje teorii z mniej niż 6 pytaniami: **14** (3 praktyczne pominięte).
- Moduł ADR-B-09: **59** pytań.
- Rozkład prawidłowych opcji: A/B/C = **257/280/229**.
- Poprawna odpowiedź jest jedyną najdłuższą: **84/766 = 10,97%** (poniżej Quality Gate 18%).

## Synchronizacja artefaktów

- Klucze i warianty egzaminów próbnych 001–005 wskazują aktualny blob banku.
- Snapshoty: `review/sequential/766-766.json`, `review/legal-clauses/766-766.json`.
- Ledger prawny i rejestr specjalisty uzupełnione o ADR-B-0766; status pozostaje `needs_review`.
- Pełne literalne porównanie polskiego tekstu i niezależna recenzja specjalisty pozostają otwarte; pytania nie oznaczono `verified`.

## Źródło

ADR 2025, Dz.U. 2025 poz. 642, 5.2.1.10.1–5.2.1.10.3: https://eli.gov.pl/api/acts/DU/2025/642
