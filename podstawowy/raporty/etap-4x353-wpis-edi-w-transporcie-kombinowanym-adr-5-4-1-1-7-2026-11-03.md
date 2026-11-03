# Etap 4x353 — ADR-B-0779: wymagany wpis w dokumencie EDI

Data: 03.11.2026  
Gałąź: `stage4x353-edi-combined-transport-entry`  
Baza: `7b417f4c16385af8315fcfb63ecb2440e6371233`

## Zakres i podstawa

Dodano ADR-B-0779 do kompetencji teoretycznej `ADR-B-13-K06` — „Dodatkowy wpis w transporcie kombinowanym” (5→6). Pytanie łączy wymóg wpisu dla przewozu na warunkach 1.1.4.2.1 z dopuszczeniem elektronicznej wymiany danych: forma EDI nie zwalnia z wymaganej treści dokumentu.

Podstawa: ADR 2025, 5.4.1.1.7 i 5.4.0.2 (Dz.U. 2025 poz. 642).

## Audyt odpowiedzi A/B/C

- A — błędna: wpis 5.4.1.1.7 nie dotyczy wyłącznie dokumentów papierowych.
- B — poprawna: elektroniczny dokument musi zawierać wymagany wpis „PRZEWÓZ ZGODNY Z 1.1.4.2.1”.
- C — błędna: wewnętrzna notatka przewoźnika nie uzupełnia dokumentu przewozowego.

## Explanation i jakość odpowiedzi

- Explanation: 387 znaków, 5 zdań; prosty język kierowcy.
- Długości A/B/C: 110/106/122 znaków; poprawna B nie jest najdłuższa.
- Klucz: B; status `needs_review`; nic nie oznaczono jako `verified`.

## Metryki banku po partii

- Bank: **779** pytań, 779 `needs_review`, 0 `verified`; blob SHA `6c816f78f6e83644ed8667311de9c1fb4d95bebc`.
- Kompetencje teorii z mniej niż 6 pytaniami: **1** (3 praktyczne pominięte).
- ADR-B-13: **53** pytania; ADR-B-13-K06: 5→6.
- Rozkład kluczy A/B/C: **258/290/231**.
- Poprawna odpowiedź jest jedyną najdłuższą: **84/779 = 10,78%**; maksimum działu: **15,22%**.

## Artefakty

- Klucze i warianty egzaminów próbnych 001–005 wskazują blob banku `6c816f78f6e83644ed8667311de9c1fb4d95bebc`.
- Dodano snapshoty `review/sequential/779-779.json` i `review/legal-clauses/779-779.json`.
- Uzupełniono ledger źródeł, rejestr partii, rejestr aktualny i pakiet specjalisty.
- Zaktualizowano `docs/POKRYCIE-KURSU.md`, README i lekcję ADR-B-13.

Pełne porównanie tekstu polskiego ADR 2025 i niezależna recenzja specjalisty pozostają otwarte.

## Źródło

ADR 2025, Dz.U. 2025 poz. 642, 5.4.1.1.7 i 5.4.0.2: https://dziennikustaw.gov.pl/DU/2025/642
