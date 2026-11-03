# Etap 4x333 — oznaczenie kontroli lub maksymalnego okresu użytkowania gaśnicy

Data: 03.11.2026. Gałąź: `stage4x333-extinguisher-inspection-date-seal`. Bazowy main: `2f7ccba4d7d975389f44d6406cfdbee14d234f83`.

## Zakres i wynik

- Dodano ADR-B-0759 do kompetencji teoretycznej `ADR-B-08-K03` — „Stan techniczny, ważność i dostępność gaśnic”; liczba pytań w kompetencji: 5→6.
- Pytanie rozróżnia dwie dopuszczone formy oznaczenia: datę (miesiąc/rok) następnej kontroli albo, odpowiednio, maksymalny dopuszczalny okres użytkowania. Nienaruszona plomba nie zastępuje wymaganego oznaczenia ani okresowych kontroli.
- Podstawa: ADR 2025, 8.1.4.4–8.1.4.5, ogłoszony w Dz.U. 2025 poz. 642.
- Explanation: 422 znaki, 4 zdania; język kursanta. Status `needs_review`; brak zmian statusu innych pytań.

## Audyt odpowiedzi A/B/C

- A — błędna: twierdzi, że zawsze musi występować wyłącznie data następnej kontroli; pomija alternatywę maksymalnego dopuszczalnego okresu użytkowania.
- B — poprawna: oddaje alternatywę wskazaną w ADR 8.1.4.4, z zachowaniem zastrzeżenia „odpowiednio”.
- C — błędna: plomba potwierdza, że gaśnica nie była używana; nie znosi obowiązku oznaczenia i okresowych kontroli.

## Metryki banku po partii

- Bank: **759** pytań, 759 `needs_review`, 0 `verified`; blob SHA `3d6a943093405340d3e4b029e9b835b6318b624b`.
- Kompetencje teorii z mniej niż 6 pytaniami: **21** (3 praktyczne pominięte).
- Rozkład prawidłowych opcji: A/B/C = **256/274/229**.
- Poprawna odpowiedź jest jedyną najdłuższą: **82/759 = 10,80%**; maksimum działu: **14,61%**.
- Długości opcji A/B/C: **117/120/105**; klucz: **B**.

## Synchronizacja artefaktów

- Klucze i warianty egzaminów próbnych 001–005: `source_bank_head` ustawiony na aktualny blob SHA.
- Snapshoty: `review/sequential/759-759.json`, `review/legal-clauses/759-759.json`.
- Ledger prawny rozszerzony o ADR-B-0759; kolejki i manifesty pakietu specjalisty zsynchronizowane.
- Rejestr specjalisty: `review/specialist/REJESTR-AKTUALNY-0001-0759.md` (759 unikalnych identyfikatorów).
- Raport coverage, README, lekcja ADR-B-08 i testy liczebności zaktualizowane.
- Pełne literalne porównanie tekstu polskiego oraz niezależna recenzja specjalisty pozostają otwarte. CI i walidatory nie nadają statusu `verified`.

## Źródła

- ADR 2025, Dz.U. 2025 poz. 642, 8.1.4.4–8.1.4.5: https://eli.gov.pl/api/acts/DU/2025/642
- Oficjalna strona Ministerstwa Infrastruktury z linkiem do tekstu ADR 2025: https://www.gov.pl/web/infrastruktura/towary-niebezpieczne
