# ETAP 4m — kontrola „najdłuższa poprawna” i poprawki redakcyjne, partia 1

Data: 2026-10-23. Źródło: świeży `main` (542 pytań ADR-B-0001–0542, status needs_review, 0 verified, brak otwartych PR przed startem).

## Definicja i wynik

Jednoznacznie najdłuższa odpowiedź: długość poprawnego wariantu w znakach **ściśle większa** niż długości obu dystraktorów, po `strip()`. Remisy na maksimum raportowane osobno. Jedynie ta miara wchodzi do celu ≤40%; wskaźnik nie potwierdza merytorycznej jakości odpowiedzi.

| Pomiar | Przed | Po partii 1 |
|---|---:|---:|
| Wszystkie pytania | 542 | 542 |
| Poprawna ściśle najdłuższa | 393 (72.5%) | 381 (70.3%) |
| Remis długości poprawnej z innym wariantem | 19 | 20 |
| Cel użytkownika | ≤40% globalnie i w każdym dziale | **nieosiągnięty, pozostaje otwarty** |

### Rozkład 13 działów

| Dział | Przed | Po | Ocena po |
|---|---:|---:|---|
| ADR-B-01 | 22/35 (62.9%) | 18/35 (51.4%) | powyżej progu |
| ADR-B-02 | 34/56 (60.7%) | 34/56 (60.7%) | powyżej progu |
| ADR-B-03 | 40/49 (81.6%) | 40/49 (81.6%) | powyżej progu |
| ADR-B-04 | 36/44 (81.8%) | 36/44 (81.8%) | powyżej progu |
| ADR-B-05 | 30/40 (75.0%) | 30/40 (75.0%) | powyżej progu |
| ADR-B-06 | 17/32 (53.1%) | 17/32 (53.1%) | powyżej progu |
| ADR-B-07 | 34/43 (79.1%) | 34/43 (79.1%) | powyżej progu |
| ADR-B-08 | 20/36 (55.6%) | 20/36 (55.6%) | powyżej progu |
| ADR-B-09 | 32/39 (82.1%) | 32/39 (82.1%) | powyżej progu |
| ADR-B-10 | 45/55 (81.8%) | 45/55 (81.8%) | powyżej progu |
| ADR-B-11 | 24/35 (68.6%) | 22/35 (62.9%) | powyżej progu |
| ADR-B-12 | 35/43 (81.4%) | 35/43 (81.4%) | powyżej progu |
| ADR-B-13 | 24/35 (68.6%) | 18/35 (51.4%) | powyżej progu |

## Zmiany w tej partii — 12 pytań

Wyłącznie skrócenie nadmiarowych członów poprawnych odpowiedzi lub wydłużenie dystraktora do realistycznej, nadal błędnej interpretacji. Żadnego numeru UN, klucza poprawnej litery, odnośnika ADR, identyfikatora ani statusu nie zmieniono. Aktualizacja istniejących migawek i recenzji A/B/C jest częścią tej samej partii.

| ID | Klucz | Dawna poprawna | Nowa poprawna | Zakres korekty |
|---|---|---|---|---|
| ADR-B-0523 | A | Podać odpowiedni numer nalepki zagrożenia dodatkowego w nawiasie. | Podać numer nalepki zagrożenia dodatkowego w nawiasie. | A |
| ADR-B-0526 | A | Przekracza ona limit 1 000 sztuk dla jednego pojazdu lub kontenera. | Przekracza limit 1 000 sztuk dla pojazdu lub kontenera. | A |
| ADR-B-0527 | B | Informacja o towarach w ilościach wyłączonych oraz liczba sztuk przesyłek. | Wskazać ilości wyłączone EQ oraz liczbę sztuk przesyłek. | B |
| ADR-B-0529 | A | Zagrożenia wynikające z towaru, bezpieczne działania i reakcja na zdarzenia. | Zagrożenia, działania ochronne i reagowanie na zdarzenia. | A |
| ADR-B-0530 | B | Poprzedzenie właściwej nazwy przewozowej słowem ODPAD, jeśli wymagane. | Wpisanie słowa ODPAD przed nazwą przewozową, gdy wymagane. | A, B |
| ADR-B-0532 | A | Dodać właściwe określenie pusty, nieoczyszczony lub pozostałość po zawartości. | Dodać właściwe określenie pusty, nieoczyszczony lub pozostałość po zawartości. | B |
| ADR-B-0533 | B | Wymagana jest także wersja w jednym z języków: angielskim, francuskim lub niemieckim. | Dodać wersję w języku angielskim, francuskim albo niemieckim. | B |
| ADR-B-0535 | B | Całkowitą masę brutto towarów LQ przeznaczonych do przewozu. | Całkowitą masę brutto przewożonych towarów LQ. | A, B |
| ADR-B-0537 | A | Czy podano odpowiednią łączną ilość oddzielnie dla każdego wymaganego rodzaju towaru. | Ilość oddzielnie dla każdego rodzaju towaru niebezpiecznego. | A |
| ADR-B-0538 | B | Przygotowuje co najmniej tyle dokumentów lub kopii, ile załadowano jednostek transportowych. | Tyle dokumentów lub kopii, ile załadowano jednostek transportowych. | B |
| ADR-B-0539 | B | Dla całego ładunku obowiązuje bardziej restrykcyjny B/D; w sztukach ogranicza on D i E, a nie C. | Kod B/D w sztukach wyklucza tunele D i E, nie C. | B |
| ADR-B-0540 | C | Wybrać dopuszczalną trasę poza tunelem E z uwagi na ograniczenie 8.6.4. | Wybrać trasę omijającą tunel E zgodnie z ADR 8.6.4. | C |

## Quality Gate

Dodano `scripts/answer_length_bias.py` oraz testy regresyjne. Workflow `.github/workflows/quality.yml` wywołuje `python scripts/answer_length_bias.py --threshold 0.40` i raportuje globalną oraz per-działową proporcję jako **ostrzeżenie**. Tryb `--strict` wymusza błąd, jeśli choć jeden dział lub całość przekracza próg, lecz nie jest domyślnie włączony przed wykonaniem całego planu naprawczego. Przedstawienie ostrzeżenia jako „PASS progu 40%” byłoby nieprawdziwe.

## Ograniczenia i dalsza kolejność

- Dalsze poprawki powinny obejmować najpierw ADR-B-03/04/07/09/10/12, ale wyłącznie po kontroli treści źródłowej i zachowaniu wiarygodnych dystraktorów; bez mechanicznego wydłużania błędów.
- Status każdego z 542 rekordów: `needs_review`. Niezależne zatwierdzenie specjalisty, aktualizacja pakietu recenzyjnego i raportu gotowości pozostają otwarte.
- Osobna część 4m: ADR-B-06 ma 32 pytania. Należy sprawdzić niepokryte szczegółowe warunki sylabusa i dosłownie porównać nowe pytania z ADR 2025 Dz.U. 642 oraz sprostowaniem 1575, zanim powstaną nowe numery 0543+.
- CI PASS kontroluje spójność techniczną, nie prawną poprawność wariantów.

