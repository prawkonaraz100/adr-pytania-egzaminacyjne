# Etap 4x337 — para rękawic dla każdego członka załogi

Data: 03.11.2026. Gałąź: `stage4x337-gloves-and-eye-protection-scope`. Bazowy main: `80b3068a790daaee5151553c0b63eec468b2761d`.

## Zakres i wynik

- Dodano ADR-B-0763 do kompetencji teoretycznej `ADR-B-08-K06` — „Rękawice i ochrona oczu”; liczba pytań w kompetencji: 5→6.
- Pytanie sprawdza literalny wymóg „pary rękawic” dla każdego członka załogi: jedna sztuka nie stanowi wymaganego kompletu. Ochrona oczu jest osobnym elementem i nie zastępuje ochrony dłoni.
- Podstawa: ADR 2025, 8.1.5.2.
- Explanation: 367 znaków, 4 zdania; status `needs_review`.

## Audyt odpowiedzi A/B/C

- A — błędna: przepis wymaga pary rękawic, a nie jednej sztuki na osobę.
- B — poprawna: „para” oznacza dwie rękawice dla każdego członka załogi.
- C — błędna: okulary chronią oczy, nie dłonie; nie mogą zastąpić rękawicy.

## Metryki banku po partii

- Bank: **763** pytań, 763 `needs_review`, 0 `verified`; blob SHA `30f597dd668581ee6b16a810e1d21e0c2661dfd4`.
- Kompetencje teorii z mniej niż 6 pytaniami: **17** (3 praktyczne pominięte).
- Rozkład prawidłowych opcji: A/B/C = **257/277/229**.
- Poprawna odpowiedź jest jedyną najdłuższą: **82/763 = 10,75%**; maksimum działu: **14,61%**.
- Długości opcji A/B/C: **90/86/100**; klucz: **B** (nie jest najdłuższa).

## Synchronizacja artefaktów

- Klucze i warianty egzaminów próbnych 001–005 wskazują aktualny blob banku.
- Snapshoty: `review/sequential/763-763.json`, `review/legal-clauses/763-763.json`.
- Ledger prawny, kolejki i manifesty pakietu specjalisty zsynchronizowane.
- Rejestr specjalisty: `review/specialist/REJESTR-AKTUALNY-0001-0763.md` (763 unikalne ID).
- Coverage, README, lekcja B-08 i testy liczebności zaktualizowane.
- Pełne literalne porównanie polskiego tekstu i niezależna recenzja specjalisty pozostają otwarte; żadnego pytania nie oznaczono `verified`.

## Źródło

ADR 2025, Dz.U. 2025 poz. 642, 8.1.5.2: https://eli.gov.pl/api/acts/DU/2025/642
