# Etap 4x339 — wysokość przegrody przy CV28 (ADR 7.5.4)

Data: 03.11.2026. Gałąź: `stage4x339-food-feed-separation-7-5-4`. Bazowy main: `dc010fb5582e09328382aa2af8774b4c6b4e2f00`.

## Zakres i wynik

- Dodano ADR-B-0765 do kompetencji teoretycznej `ADR-B-09-K03` — „Kontakt z żywnością i paszami”; liczba pytań: 5→6.
- Pytanie sprawdza jeden z dozwolonych sposobów oddzielenia przesyłek objętych CV28 od żywności. Jeżeli wybiera się przegrodę, musi ona mieć wysokość co najmniej równą wysokości tych przesyłek. Krótsza przegroda nie spełnia tego warunku; ADR dopuszcza inne sposoby oddzielenia.
- Podstawa: ADR 2025, 7.5.4 oraz CV28 w 7.5.11 (Dz.U. 2025 poz. 642).
- Explanation: 398 znaków, 4 zdania; status `needs_review`.

## Audyt odpowiedzi A/B/C

- A — błędna: stabilność i szerokość przegrody nie zastępują wymaganej wysokości.
- B — poprawna: przegroda musi sięgać co najmniej do wysokości przesyłek objętych CV28.
- C — błędna: przepis nie nakazuje zawsze prowadzić przegrody aż do dachu; jej wysokość odnosi do wysokości wskazanych przesyłek.

## Metryki banku po partii

- Bank: **765** pytań, 765 `needs_review`, 0 `verified`; blob SHA `d6cd7215399b36e8783209c9e34a35ff86ac35ad`.
- Kompetencje teorii z mniej niż 6 pytaniami: **15** (3 praktyczne pominięte).
- Moduł ADR-B-09: **58** pytań.
- Rozkład prawidłowych opcji: A/B/C = **257/279/229**.
- Poprawna odpowiedź jest jedyną najdłuższą: **83/765 = 10,85%**; maksimum działu: **14,61%**.
- Długości opcji A/B/C: **90/91/101**; klucz: **B** (nie jest najdłuższa).

## Synchronizacja artefaktów

- Klucze i warianty egzaminów próbnych 001–005 wskazują aktualny blob banku.
- Snapshoty: `review/sequential/765-765.json`, `review/legal-clauses/765-765.json`.
- Ledger prawny, kolejki i manifesty pakietu specjalisty zsynchronizowane.
- Rejestr specjalisty: `review/specialist/REJESTR-AKTUALNY-0001-0765.md` (765 unikalnych ID).
- Coverage, README, lekcja B-09, instrukcja specjalisty i testy liczebności zaktualizowane.
- Pełne literalne porównanie polskiego tekstu i niezależna recenzja specjalisty pozostają otwarte; pytania nie oznaczono `verified`.

## Źródło

ADR 2025, Dz.U. 2025 poz. 642, 7.5.4 i 7.5.11 (CV28): https://eli.gov.pl/api/acts/DU/2025/642
