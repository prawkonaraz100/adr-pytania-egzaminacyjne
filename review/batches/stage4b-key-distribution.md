# Etap 4b — analiza i wyrównanie kluczy A/B/C (2026-10-23)

Wersja wejściowa: 506 pytań z `main`, wszystkie `needs_review`, bez otwartych PR. Przestawiono wyłącznie pozycje istniejących dosłownych tekstów opcji (A↔C lub B↔C) w 49 rekordach; pozycje prawidłowych kluczy są aktualizowane z zachowaniem znaczenia. Przeprowadzono osobno kontrolę 13 działów i sekwencji kluczy. Żadne pytanie nie otrzymuje zatwierdzenia prawnego.

| Rozkład | A | B | C |
|---|---:|---:|---:|
| Przed | 203 | 184 | 119 |
| Po | 169 | 169 | 168 |

## Działy

| Dział | Przed A/B/C | Po A/B/C |
|---|---|---|
| ADR-B-01 | 8/10/7 | 8/10/7 |
| ADR-B-02 | 20/20/13 | 19/18/16 |
| ADR-B-03 | 16/23/9 | 15/21/12 |
| ADR-B-04 | 15/19/9 | 14/17/12 |
| ADR-B-05 | 17/13/9 | 16/12/11 |
| ADR-B-06 | 13/9/9 | 11/9/11 |
| ADR-B-07 | 19/16/7 | 17/15/10 |
| ADR-B-08 | 15/12/8 | 11/10/14 |
| ADR-B-09 | 15/12/11 | 11/12/15 |
| ADR-B-10 | 24/21/9 | 19/17/18 |
| ADR-B-11 | 14/9/9 | 9/9/14 |
| ADR-B-12 | 21/13/8 | 13/12/17 |
| ADR-B-13 | 6/7/11 | 6/7/11 |

## Serie tej samej litery

- Przed: najdłuższa seria 7 × A (ADR-B-0430–ADR-B-0436); serie ≥4: 3.
- Po: najdłuższa seria 4 × A (ADR-B-0371–ADR-B-0374); serie ≥4: 2.
- Klucze zrównoważono globalnie; lokalne różnice (szczególnie w module 13) nadal istnieją, by nie zmieniać nadmiernie banku. 

## Zamiany z zachowaniem treści

| ID | Dział | Przed | Po |
|---|---|---|---|
| ADR-B-0399 | ADR-B-12 | A | C |
| ADR-B-0401 | ADR-B-12 | A | C |
| ADR-B-0402 | ADR-B-12 | A | C |
| ADR-B-0403 | ADR-B-12 | A | C |
| ADR-B-0405 | ADR-B-12 | A | C |
| ADR-B-0406 | ADR-B-12 | B | C |
| ADR-B-0409 | ADR-B-12 | A | C |
| ADR-B-0410 | ADR-B-12 | A | C |
| ADR-B-0412 | ADR-B-12 | A | C |
| ADR-B-0417 | ADR-B-08 | B | C |
| ADR-B-0420 | ADR-B-08 | A | C |
| ADR-B-0421 | ADR-B-08 | A | C |
| ADR-B-0423 | ADR-B-08 | A | C |
| ADR-B-0424 | ADR-B-09 | A | C |
| ADR-B-0425 | ADR-B-09 | A | C |
| ADR-B-0427 | ADR-B-09 | A | C |
| ADR-B-0428 | ADR-B-09 | A | C |
| ADR-B-0430 | ADR-B-11 | A | C |
| ADR-B-0431 | ADR-B-11 | A | C |
| ADR-B-0432 | ADR-B-11 | A | C |
| ADR-B-0434 | ADR-B-11 | A | C |
| ADR-B-0437 | ADR-B-10 | B | C |
| ADR-B-0438 | ADR-B-10 | A | C |
| ADR-B-0441 | ADR-B-10 | B | C |
| ADR-B-0443 | ADR-B-10 | A | C |
| ADR-B-0446 | ADR-B-10 | A | C |
| ADR-B-0448 | ADR-B-10 | B | C |
| ADR-B-0450 | ADR-B-10 | A | C |
| ADR-B-0453 | ADR-B-10 | A | C |
| ADR-B-0454 | ADR-B-10 | B | C |
| ADR-B-0462 | ADR-B-03 | B | C |
| ADR-B-0464 | ADR-B-03 | A | C |
| ADR-B-0468 | ADR-B-03 | B | C |
| ADR-B-0471 | ADR-B-04 | B | C |
| ADR-B-0472 | ADR-B-04 | A | C |
| ADR-B-0475 | ADR-B-04 | B | C |
| ADR-B-0478 | ADR-B-07 | A | C |
| ADR-B-0481 | ADR-B-07 | B | C |
| ADR-B-0482 | ADR-B-07 | A | C |
| ADR-B-0484 | ADR-B-08 | A | C |
| ADR-B-0486 | ADR-B-08 | B | C |
| ADR-B-0490 | ADR-B-11 | A | C |
| ADR-B-0493 | ADR-B-05 | A | C |
| ADR-B-0494 | ADR-B-05 | B | C |
| ADR-B-0496 | ADR-B-02 | A | C |
| ADR-B-0499 | ADR-B-02 | B | C |
| ADR-B-0502 | ADR-B-02 | B | C |
| ADR-B-0503 | ADR-B-06 | A | C |
| ADR-B-0506 | ADR-B-06 | A | C |

Spójność zapewniają: plan `review/batches/stage4b-permutations.json`, zsynchronizowany bieżący rejestr specjalisty `review/specialist/REJESTR-0001-0506.md`, nowe migawki w istniejących plikach audytu sekwencyjnego i prawnego. Literowe uzasadnienia A/B/C wymagają przeniesienia wraz z odpowiadającą im oryginalną treścią. Historycznych raportów nie usuwać. Wszystkie pozycje pozostają do niezależnej recenzji prawnej; nie są dopuszczone do publikacji.
