# ETAP 4b — kontrola A/B/C i 49 bezstratnych permutacji

**Migawka wejściowa:** main 506 rekordów (0001–0506), brak otwartych PR. Status: 506 needs_review / 0 verified. Dokonano 49 **wyłącznie fizycznych zamian pozycji odpowiedzi** A↔C (34 razy) lub B↔C (15 razy). Każde pytanie zachowuje dosłownie te same trzy teksty, pytanie, wyjaśnienie, referencje, obraz i status; przenumerowano klucz z A/B na C. Żadnego niezależnego zatwierdzenia prawnego.

## Rozkład globalny

| Faza | A | B | C | Max/min |
|---|---:|---:|---:|---:|
| Przed | 203 | 184 | 119 | 1.71 |
| Po | 169 | 169 | 168 | 1.01 |

## Rozkład w 13 działach

| Dział | Przed A/B/C | Po A/B/C |
|---|---|---|
| ADR-B-01 | 8/10/7 | 8/10/7 |
| ADR-B-02 | 20/20/13 | 17/17/19 |
| ADR-B-03 | 16/23/9 | 13/20/15 |
| ADR-B-04 | 15/19/9 | 13/17/13 |
| ADR-B-05 | 17/13/9 | 16/12/11 |
| ADR-B-06 | 13/9/9 | 11/9/11 |
| ADR-B-07 | 19/16/7 | 16/14/12 |
| ADR-B-08 | 15/12/8 | 12/11/12 |
| ADR-B-09 | 15/12/11 | 13/12/13 |
| ADR-B-10 | 24/21/9 | 17/18/19 |
| ADR-B-11 | 14/9/9 | 12/9/11 |
| ADR-B-12 | 21/13/8 | 15/13/14 |
| ADR-B-13 | 6/7/11 | 6/7/11 |

## Kolejne identyczne klucze

Przed: najdłuższa seria 7× A (ADR-B-0430–ADR-B-0436); liczba serii długości co najmniej 4: 3. Po: najdłuższa seria 12× C (ADR-B-0436–ADR-B-0447); liczba serii długości co najmniej 4: 6. Rozkład działu ADR-B-13 pozostał 6/7/11, bo nie przesuwano wcześniejszych ID bez pełnego dostępu do ich oryginalnych ocen prawnych; wyrównanie globalne nie musi oznaczać idealnych proporcji w każdym dziale.

## Pełna lista zmienionych ID

| ID | Dział | Było | Jest | Treść |
|---|---|---|---|---|
| ADR-B-0446 | ADR-B-10 | A | C | Zachowane trzy oryginalne warianty, zamienione miejsca A↔C |
| ADR-B-0402 | ADR-B-12 | A | C | Zachowane trzy oryginalne warianty, zamienione miejsca A↔C |
| ADR-B-0447 | ADR-B-10 | A | C | Zachowane trzy oryginalne warianty, zamienione miejsca A↔C |
| ADR-B-0478 | ADR-B-07 | A | C | Zachowane trzy oryginalne warianty, zamienione miejsca A↔C |
| ADR-B-0401 | ADR-B-12 | A | C | Zachowane trzy oryginalne warianty, zamienione miejsca A↔C |
| ADR-B-0438 | ADR-B-10 | A | C | Zachowane trzy oryginalne warianty, zamienione miejsca A↔C |
| ADR-B-0480 | ADR-B-07 | A | C | Zachowane trzy oryginalne warianty, zamienione miejsca A↔C |
| ADR-B-0403 | ADR-B-12 | A | C | Zachowane trzy oryginalne warianty, zamienione miejsca A↔C |
| ADR-B-0440 | ADR-B-10 | A | C | Zachowane trzy oryginalne warianty, zamienione miejsca A↔C |
| ADR-B-0482 | ADR-B-07 | A | C | Zachowane trzy oryginalne warianty, zamienione miejsca A↔C |
| ADR-B-0493 | ADR-B-05 | A | C | Zachowane trzy oryginalne warianty, zamienione miejsca A↔C |
| ADR-B-0409 | ADR-B-12 | A | C | Zachowane trzy oryginalne warianty, zamienione miejsca A↔C |
| ADR-B-0420 | ADR-B-08 | A | C | Zachowane trzy oryginalne warianty, zamienione miejsca A↔C |
| ADR-B-0443 | ADR-B-10 | A | C | Zachowane trzy oryginalne warianty, zamienione miejsca A↔C |
| ADR-B-0461 | ADR-B-03 | A | C | Zachowane trzy oryginalne warianty, zamienione miejsca A↔C |
| ADR-B-0496 | ADR-B-02 | A | C | Zachowane trzy oryginalne warianty, zamienione miejsca A↔C |
| ADR-B-0472 | ADR-B-04 | A | C | Zachowane trzy oryginalne warianty, zamienione miejsca A↔C |
| ADR-B-0431 | ADR-B-11 | A | C | Zachowane trzy oryginalne warianty, zamienione miejsca A↔C |
| ADR-B-0410 | ADR-B-12 | A | C | Zachowane trzy oryginalne warianty, zamienione miejsca A↔C |
| ADR-B-0421 | ADR-B-08 | A | C | Zachowane trzy oryginalne warianty, zamienione miejsca A↔C |
| ADR-B-0450 | ADR-B-10 | A | C | Zachowane trzy oryginalne warianty, zamienione miejsca A↔C |
| ADR-B-0464 | ADR-B-03 | A | C | Zachowane trzy oryginalne warianty, zamienione miejsca A↔C |
| ADR-B-0498 | ADR-B-02 | A | C | Zachowane trzy oryginalne warianty, zamienione miejsca A↔C |
| ADR-B-0424 | ADR-B-09 | A | C | Zachowane trzy oryginalne warianty, zamienione miejsca A↔C |
| ADR-B-0474 | ADR-B-04 | A | C | Zachowane trzy oryginalne warianty, zamienione miejsca A↔C |
| ADR-B-0503 | ADR-B-06 | A | C | Zachowane trzy oryginalne warianty, zamienione miejsca A↔C |
| ADR-B-0432 | ADR-B-11 | A | C | Zachowane trzy oryginalne warianty, zamienione miejsca A↔C |
| ADR-B-0412 | ADR-B-12 | A | C | Zachowane trzy oryginalne warianty, zamienione miejsca A↔C |
| ADR-B-0423 | ADR-B-08 | A | C | Zachowane trzy oryginalne warianty, zamienione miejsca A↔C |
| ADR-B-0453 | ADR-B-10 | A | C | Zachowane trzy oryginalne warianty, zamienione miejsca A↔C |
| ADR-B-0467 | ADR-B-03 | A | C | Zachowane trzy oryginalne warianty, zamienione miejsca A↔C |
| ADR-B-0501 | ADR-B-02 | A | C | Zachowane trzy oryginalne warianty, zamienione miejsca A↔C |
| ADR-B-0436 | ADR-B-09 | A | C | Zachowane trzy oryginalne warianty, zamienione miejsca A↔C |
| ADR-B-0506 | ADR-B-06 | A | C | Zachowane trzy oryginalne warianty, zamienione miejsca A↔C |
| ADR-B-0462 | ADR-B-03 | B | C | Zachowane trzy oryginalne warianty, zamienione miejsca B↔C |
| ADR-B-0465 | ADR-B-03 | B | C | Zachowane trzy oryginalne warianty, zamienione miejsca B↔C |
| ADR-B-0471 | ADR-B-04 | B | C | Zachowane trzy oryginalne warianty, zamienione miejsca B↔C |
| ADR-B-0468 | ADR-B-03 | B | C | Zachowane trzy oryginalne warianty, zamienione miejsca B↔C |
| ADR-B-0475 | ADR-B-04 | B | C | Zachowane trzy oryginalne warianty, zamienione miejsca B↔C |
| ADR-B-0477 | ADR-B-07 | B | C | Zachowane trzy oryginalne warianty, zamienione miejsca B↔C |
| ADR-B-0437 | ADR-B-10 | B | C | Zachowane trzy oryginalne warianty, zamienione miejsca B↔C |
| ADR-B-0495 | ADR-B-02 | B | C | Zachowane trzy oryginalne warianty, zamienione miejsca B↔C |
| ADR-B-0481 | ADR-B-07 | B | C | Zachowane trzy oryginalne warianty, zamienione miejsca B↔C |
| ADR-B-0494 | ADR-B-05 | B | C | Zachowane trzy oryginalne warianty, zamienione miejsca B↔C |
| ADR-B-0441 | ADR-B-10 | B | C | Zachowane trzy oryginalne warianty, zamienione miejsca B↔C |
| ADR-B-0499 | ADR-B-02 | B | C | Zachowane trzy oryginalne warianty, zamienione miejsca B↔C |
| ADR-B-0417 | ADR-B-08 | B | C | Zachowane trzy oryginalne warianty, zamienione miejsca B↔C |
| ADR-B-0444 | ADR-B-10 | B | C | Zachowane trzy oryginalne warianty, zamienione miejsca B↔C |
| ADR-B-0502 | ADR-B-02 | B | C | Zachowane trzy oryginalne warianty, zamienione miejsca B↔C |

## Mechanizmy spójności

- Plan przestawień: `review/batches/stage4b-permutations.json` — wiąże ID z wcześniejszym i nowym kluczem.
- W tej samej partii zaktualizować dokładne migawki w 11 istniejących parach `review/sequential/*.json` i `review/legal-clauses/*.json` oraz każdą ocenę A/B/C wraz z jej przypisaniem do litery.
- Indeks recenzyjny `review/specialist/REJESTR-0001-0506.md` odzwierciedla nowy klucz. Historycznych raportów nie przepisywać jako nowych.
- Po scaleniu sprawdzić całość `scripts/check_sequential_audit.py` i `scripts/check_legal_clause_review.py`, cały Quality Gate i brak zmiany zbiorów tekstów opcji dla każdego z 506 pytań.
- **Ważne:** losowanie i przestawianie A/B/C **nie zastępuje poprawienia oczywistych dystraktorów** z etapu 4a. Wszystkie pozycje nadal wymagają recenzji prawnej.
