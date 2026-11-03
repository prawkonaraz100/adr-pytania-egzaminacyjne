# Etap 4x349 — ADR-B-0775: zastrzeżenie dotyczące dostępu publicznego

Data: 03.11.2026  
Gałąź: `stage4x349-conditional-public-access-security-area`  
Baza: `c77d59264616a7afda2d73a7d82400c3d84e92f2`

## Zakres i podstawa

Dodano ADR-B-0775 do kompetencji teoretycznej `ADR-B-12-K02` — „Zabezpieczenie placów i składowania” (5→6). Pytanie sprawdza precyzyjny zakres zwrotu „gdzie to możliwe i właściwe” w ADR 1.10.1.3. Wymóg właściwego zabezpieczenia i dobrego oświetlenia obszarów czasowego składowania podczas przewozu nie jest objęty tym zastrzeżeniem; dotyczy ono wyłącznie niedostępności dla ogółu.

Podstawa: ADR 2025, 1.10.1.3 (Dz.U. 2025 poz. 642).

## Audyt odpowiedzi A/B/C

- A — błędna: rozciąga zastrzeżenie „gdzie to możliwe i właściwe” na wszystkie trzy wymagania, choć dotyczy ono tylko dostępu ogółu.
- B — poprawna: obszar ma być właściwie zabezpieczony i dobrze oświetlony; tylko ograniczenie dostępu dla ogółu jest warunkowe.
- C — błędna: zmienia warunkowy wymóg niedostępności dla ogółu w bezwzględny zakaz dostępu publicznego.

## Explanation i jakość odpowiedzi

- Explanation: 386 znaków, 4 zdania; prosty język kierowcy.
- Długości A/B/C: 167/163/171 znaków; poprawna B nie jest najdłuższa.
- Klucz: B; status `needs_review`; nic nie oznaczono jako `verified`.

## Metryki banku po partii

- Bank: **775** pytań, 775 `needs_review`, 0 `verified`; blob SHA `f031ae4b9771c127a38bbb5266bf69f56310ad95`.
- Kompetencje teorii z mniej niż 6 pytaniami: **5** (3 praktyczne pominięte).
- ADR-B-12: **47** pytań; ADR-B-12-K02: 5→6.
- Rozkład kluczy A/B/C: **258/287/230**.
- Poprawna odpowiedź jest jedyną najdłuższą: **84/775 = 10,84%**; maksimum działu: **15,22%**.

## Artefakty

- Klucze i warianty egzaminów próbnych 001–005 wskazują blob banku `f031ae4b9771c127a38bbb5266bf69f56310ad95`.
- Dodano snapshoty `review/sequential/775-775.json` i `review/legal-clauses/775-775.json`.
- Uzupełniono ledger prawny, rejestr partii, rejestr aktualny i pakiet specjalisty.
- Zaktualizowano `docs/POKRYCIE-KURSU.md`, README i lekcję ADR-B-12.

Pełne porównanie tekstu polskiego ADR 2025 i niezależna recenzja specjalisty pozostają otwarte.

## Źródło

ADR 2025, Dz.U. 2025 poz. 642, 1.10.1.3: https://dziennikustaw.gov.pl/DU/2025/642
