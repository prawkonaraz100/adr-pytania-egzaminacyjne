# Etap 4x354 — ADR-B-0780: instrukcje pisemne po zmianie pojazdu

Data: 03.11.2026. Gałąź: `stage4x354-written-instructions-vehicle-changeover`; baza: `0b0f9edc07c0138051d11623db8012888344ebe7`.

## Pytanie, podstawa i audyt A/B/C

Ostatnia luka kompetencji teoretycznych: `ADR-B-13-K07` (5→6). Awaria ciągnika i podstawienie pojazdu zastępczego nie znoszą wymogu posiadania łatwo dostępnych instrukcji pisemnych w nowej kabinie. Podstawy ADR 2025: 5.4.3.1 (kabina i dostępność) oraz 8.1.2.3 (łatwo dostępne instrukcje); 8.1.2.1(b) (kabina kierowcy).

- A — błędna: przekaz telefoniczny nie zastępuje instrukcji przewożonych w kabinie.
- B — poprawna: należy wyposażyć kabinę zastępczego pojazdu w łatwo dostępne instrukcje.
- C — błędna: wymóg dotyczy aktualnie wykonującej przewóz jednostki, nie tylko pierwszego ciągnika.

Explanation: **378 znaków**, 4 zdania, w języku kursanta. Długości A/B/C: **137/102/137**; odpowiedź B nie jest najdłuższa. Status: `needs_review`, bez `verified`.

## Metryki po partii

- **780 pytań**, 780 `needs_review`, 0 `verified`.
- Blob SHA banku: `db5b90f4305fd75c1bb2f73a8b5c8b7a6bb42d63`.
- Kompetencje teorii z mniej niż 6 pytaniami: **0**; trzy kompetencje praktyczne wyłączone.
- ADR-B-13: **54** pytania; ADR-B-13-K07: 5→6.
- Rozkład A/B/C: **258/291/231**.
- Poprawna jako jedyna najdłuższa: **84/780 = 10,77%** (maksimum działu 15,22%).

Zaktualizowano klucze i warianty egzaminów 001–005, snapshoty sequential/legal dla ADR-B-0780, rejestr i ledger źródeł, pakiet specjalisty, dokumentację pokrycia. Wszystkie pytania są wyłącznie do recenzji; pełne literalne porównanie ADR 2025 oraz niezależna weryfikacja prawna pozostają otwarte.

Źródło urzędowe: https://dziennikustaw.gov.pl/DU/2025/642
