# Etap 4x327 — tablice pomarańczowe: tolerancja wymiarów

Data: 03.11.2026. Gałąź: `stage4x327-orange-plate-dimensions`. Bazowy main: `1e0e1c7a4fecfd3ab6b4bb5e4a00b1abcd0d2501`.

## Zakres i wynik

Dodano ADR-B-0753 do kompetencji `ADR-B-06-K05` (powtórzone cyfry i szczególne kombinacje numerów zagrożenia? **Uwaga: przypisanie w mapie kompetencji i manifeście wskazuje K05 — tablice pomarańczowe i ich wymiary**). Podstawa: ADR 2025, 5.3.2.2.1 i 5.3.2.2.4.

- Bank: **753** pytania (ADR-B-0001–0753), 753 `needs_review`, 0 `verified`.
- SHA `92d2325d63fc4099535b1ea89c6aac7503743678`.
- Moduł ADR-B-06: **63** pytania; K05: 5→6.
- Kompetencje teorii z mniej niż 6 pytaniami: **27** (3 praktyczne pominięte).
- Rozkład kluczy A/B/C: **253/271/229**.
- „Poprawna odpowiedź jest jedyną najdłuższą”: **81/753 = 10,76%**; maksimum działu **14,61%**.
- Długości opcji: A=135, B=110, C=134; poprawna B nie jest najdłuższa.
- Explanation: 355 znaków, 4 zdania.

## Pytanie ADR-B-0753

Przed wyjazdem sprawdzasz pomarańczową tablicę o wymiarach 36 × 27 cm. Standard to 40 × 30 cm, a konstrukcja pojazdu pozwala na montaż pełnego rozmiaru. Czy sam wymiar oznacza niezgodność z ADR?

A. Tak, każda tablica musi mieć dokładnie 40 × 30 cm; mniejszy rozmiar jest dopuszczony wyłącznie wtedy, gdy brakuje miejsca na pojeździe.

B. Nie, 36 × 27 cm mieści się na dolnej granicy tolerancji ±10% dla standardowych wymiarów tablicy pomarańczowej.

C. Tak, ponieważ tolerancja dotyczy jedynie szerokości czarnego obrzeża, a wymiary tablicy mogą być wyłącznie standardowe lub 30 × 12 cm.

Standardowa tablica ma 40 × 30 cm, ale ADR dopuszcza ±10% tolerancji dla wymiarów podanych w tym podrozdziale. Dlatego 36 × 27 cm mieści się dokładnie na dolnej granicy tolerancji i nie wymaga powoływania się na wyjątek dla pojazdu bez miejsca. Odpowiedź A pomija tolerancję, a C błędnie ogranicza ją do obrzeża. Podstawa: ADR 2025, 5.3.2.2.1 i 5.3.2.2.4.

## Audyt A/B/C i źródła

- A — błędna: pomija ogólną tolerancję wymiarów ±10%.
- B — poprawna: 36 × 27 cm to dokładnie 90% standardowych wymiarów 40 × 30 cm.
- C — błędna: tolerancja nie dotyczy wyłącznie obrzeża.
- Podstawa prawna: Dz.U. 2025 poz. 642, ADR 2025, 5.3.2.2.1 i 5.3.2.2.4 — https://eli.gov.pl/api/acts/DU/2025/642/text.pdf.
- Źródło pomocnicze: ADR 2025, tom II, s. 251, 5.3.2.2.4 — https://www.gov.pl/attachment/b4638c72-30e3-4bff-afd1-1b9ba4100e70.
- Pytanie pozostaje `needs_review`; pełne literalne porównanie i niezależna recenzja specjalisty są nadal wymagane. Nie oznaczono żadnego pytania jako `verified`.

## Synchronizacja artefaktów

Klucze i warianty egzaminów próbnych 001–005 wskazują SHA bieżącego banku. Snapshoty `review/sequential/753-753.json` i `review/legal-clauses/753-753.json` zawierają ADR-B-0753. Ledger prawny oraz manifesty pakietu specjalisty zawierają rekord etapu 4x327, aktualny SHA, 753 pytania i licznik 27 kompetencji teoretycznych poniżej progu. Zaktualizowano raport coverage, README kursanta i specjalisty, rejestr specjalisty oraz asercje testów liczebności.
