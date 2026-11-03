# Etap 4x334 — gaśnica dla każdej jednostki transportowej

Data: 03.11.2026. Gałąź: `stage4x334-fire-extinguisher-1-1-3-6`. Bazowy main: `ce8b97d811f11ad9a7bdfd3beaa3971357b1d8c3`.

## Zakres i wynik

- Dodano ADR-B-0760 do kompetencji teoretycznej `ADR-B-08-K02` — „Gaśnica przy 1.1.3.6”; liczba pytań w kompetencji: 5→6.
- Pytanie odróżnia dwa osobne samochody jadące w konwoju od ciągnika z dołączoną naczepą. Każdy osobny samochód jest własną jednostką transportową i musi mieć wymaganą gaśnicę.
- Podstawa: ADR 2025, 1.2.1 (definicja jednostki transportowej), 8.1.4.2 (gaśnica dla każdej jednostki) oraz 1.1.3.6.
- Explanation: 375 znaków, 4 zdania; status `needs_review`.

## Audyt odpowiedzi A/B/C

- A — poprawna: dwa oddzielne samochody są dwiema jednostkami transportowymi; wymóg z 8.1.4.2 dotyczy każdej z nich.
- B — błędna: wspólna trasa ani jazda w konwoju nie łączą dwóch samochodów w jedną jednostkę.
- C — błędna: wyłączenie 1.1.3.6 nie usuwa obowiązku posiadania gaśnicy.

## Metryki banku po partii

- Bank: **760** pytań, 760 `needs_review`, 0 `verified`; blob SHA `46cbbc7ab6e1fa7f513060fa22ca61db78f9dba7`.
- Kompetencje teorii z mniej niż 6 pytaniami: **20** (3 praktyczne pominięte).
- Rozkład prawidłowych opcji: A/B/C = **257/274/229**.
- Poprawna odpowiedź jest jedyną najdłuższą: **82/760 = 10,79%**; maksimum działu: **14,61%**.
- Długości opcji A/B/C: **107/111/109**; klucz: **A** (nie jest najdłuższa).

## Synchronizacja artefaktów

- Klucze i warianty egzaminów próbnych 001–005 wskazują aktualny blob banku.
- Snapshoty: `review/sequential/760-760.json`, `review/legal-clauses/760-760.json`.
- Ledger prawny, kolejki i manifesty pakietu specjalisty zsynchronizowane.
- Rejestr specjalisty: `review/specialist/REJESTR-AKTUALNY-0001-0760.md` (760 unikalnych ID).
- Coverage, README, lekcja B-08 i testy liczebności zaktualizowane.
- Pełne literalne porównanie polskiego tekstu i niezależna recenzja specjalisty pozostają otwarte; żadnego pytania nie oznaczono `verified`.

## Źródło

ADR 2025, Dz.U. 2025 poz. 642, 1.2.1; 8.1.4.2; 1.1.3.6: https://eli.gov.pl/api/acts/DU/2025/642
