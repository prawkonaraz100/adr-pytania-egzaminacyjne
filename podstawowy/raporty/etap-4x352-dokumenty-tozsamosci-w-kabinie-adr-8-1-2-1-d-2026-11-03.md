# Etap 4x352 — ADR-B-0778: dokumenty tożsamości w kabinie kierowcy

Data: 03.11.2026  
Gałąź: `stage4x352-photo-id-in-drivers-cab`  
Baza: `d6d75881e7a3512186c93adfe390bbed299c3f88`

## Zakres i podstawa

Dodano ADR-B-0778 do kompetencji teoretycznej `ADR-B-13-K05` — „Dokumenty i dowód tożsamości załogi” (5→6). Pytanie sprawdza nie tylko to, jakie dokumenty muszą identyfikować członków załogi, lecz także gdzie powinny być przewożone: w kabinie kierowcy, a nie w skrzynce poza kabiną.

Podstawa: ADR 2025, 8.1.2.1(d) i 1.10.1.4 (Dz.U. 2025 poz. 642).

## Audyt odpowiedzi A/B/C

- A — błędna: ADR nie pozwala przechowywać tych dokumentów w dowolnym miejscu jednostki transportowej; wskazuje kabinę kierowcy.
- B — poprawna: w kabinie powinny znajdować się dokumenty ze zdjęciem umożliwiające identyfikację wszystkich członków załogi.
- C — błędna: wymóg obejmuje każdego członka załogi, nie tylko kierowcę.

## Explanation i jakość odpowiedzi

- Explanation: 355 znaków, 4 zdania; prosty język kierowcy.
- Długości A/B/C: 104/89/99 znaków; poprawna B nie jest najdłuższa.
- Klucz: B; status `needs_review`; nic nie oznaczono jako `verified`.

## Metryki banku po partii

- Bank: **778** pytań, 778 `needs_review`, 0 `verified`; blob SHA `ab9c275f699c82c76357be53051250d404cba85d`.
- Kompetencje teorii z mniej niż 6 pytaniami: **2** (3 praktyczne pominięte).
- ADR-B-13: **52** pytania; ADR-B-13-K05: 5→6.
- Rozkład kluczy A/B/C: **258/289/231**.
- Poprawna odpowiedź jest jedyną najdłuższą: **84/778 = 10,80%**; maksimum działu: **15,22%**.

## Artefakty

- Klucze i warianty egzaminów próbnych 001–005 wskazują blob banku `ab9c275f699c82c76357be53051250d404cba85d`.
- Dodano snapshoty `review/sequential/778-778.json` i `review/legal-clauses/778-778.json`.
- Uzupełniono ledger źródeł, rejestr partii, rejestr aktualny i pakiet specjalisty.
- Zaktualizowano `docs/POKRYCIE-KURSU.md`, README i lekcję ADR-B-13.

Pełne porównanie tekstu polskiego ADR 2025 i niezależna recenzja specjalisty pozostają otwarte.

## Źródło

ADR 2025, Dz.U. 2025 poz. 642, 8.1.2.1(d): https://dziennikustaw.gov.pl/DU/2025/642
