# Etap 4v — 12 pytań ADR-B-10 (transport kombinowany)

**Świeży main:** `418c6a80760e5085eeccc18ced85386ca653edf2` po PR #290. ID: ADR-B-0203, ADR-B-0204, ADR-B-0205, ADR-B-0206, ADR-B-0277, ADR-B-0381, ADR-B-0382, ADR-B-0383, ADR-B-0384, ADR-B-0385, ADR-B-0386, ADR-B-0388.

## Zmiany dydaktyczne

Dopracowano dystraktory związane z IMDG, RID, ICAO, ADR 1.1.4.2.1 i dokumentami kontenerowymi. Sformułowano realistyczne, błędne sytuacje (np. uznanie dokumentacji przewozowej lub samego dojazdu do portu za zwolnienie z wymagań), bez prostych słów zdradzających odpowiedź. 12 `explanation` przepisano pod nowe warianty, każde 300–500 znaków i na końcu podstawa ADR. Pozostawiono bez zmian **dosłowne poprawne opcje**, klucze, ID, źródła, podstawy prawne i `needs_review`.

Uaktualniono tylko techniczne migawki audytu sekwencyjnego oraz klauzulowego i odpowiadające zmienionym pytaniom arkusze egzaminu próbnego.

## Metryki po zmianie na 569 pytaniach

Definicje skryptu `scripts/answer_leakage_metrics.py`: długości po `strip()`, strict shortest/longest bez remisów; absolutes regex, mianownik dystraktorów 2 × pytania.

| Dział | Poprawna najkrótsza przed → po | Poprawna najdłuższa przed → po | Absoluty w dystraktorach przed → po | Tylko w dystraktorach przed → po |
|---|---|---|---|---|
| GLOBAL | 195/569 (34.27%) → 186/569 (32.69%) | 80/569 (14.06%) → 80/569 (14.06%) | 233/1138 (20.47%) → 220/1138 (19.33%) | 162 → 154 |
| ADR-B-01 | 13/35 (37.14%) → 13/35 (37.14%) | 6/35 (17.14%) → 6/35 (17.14%) | 15/70 (21.43%) → 15/70 (21.43%) | 12 → 12 |
| ADR-B-02 | 13/56 (23.21%) → 13/56 (23.21%) | 9/56 (16.07%) → 9/56 (16.07%) | 24/112 (21.43%) → 24/112 (21.43%) | 15 → 15 |
| ADR-B-03 | 20/49 (40.82%) → 20/49 (40.82%) | 7/49 (14.29%) → 7/49 (14.29%) | 35/98 (35.71%) → 35/98 (35.71%) | 23 → 23 |
| ADR-B-04 | 16/44 (36.36%) → 16/44 (36.36%) | 7/44 (15.91%) → 7/44 (15.91%) | 21/88 (23.86%) → 21/88 (23.86%) | 19 → 19 |
| ADR-B-05 | 8/40 (20.00%) → 8/40 (20.00%) | 6/40 (15.00%) → 6/40 (15.00%) | 10/80 (12.50%) → 10/80 (12.50%) | 5 → 5 |
| ADR-B-06 | 6/45 (13.33%) → 6/45 (13.33%) | 5/45 (11.11%) → 5/45 (11.11%) | 2/90 (2.22%) → 2/90 (2.22%) | 1 → 1 |
| ADR-B-07 | 18/46 (39.13%) → 18/46 (39.13%) | 5/46 (10.87%) → 5/46 (10.87%) | 12/92 (13.04%) → 12/92 (13.04%) | 10 → 10 |
| ADR-B-08 | 10/40 (25.00%) → 10/40 (25.00%) | 7/40 (17.50%) → 7/40 (17.50%) | 5/80 (6.25%) → 5/80 (6.25%) | 2 → 2 |
| ADR-B-09 | 21/46 (45.65%) → 21/46 (45.65%) | 5/46 (10.87%) → 5/46 (10.87%) | 15/92 (16.30%) → 15/92 (16.30%) | 12 → 12 |
| ADR-B-10 | 26/55 (47.27%) → 17/55 (30.91%) | 4/55 (7.27%) → 4/55 (7.27%) | 40/110 (36.36%) → 27/110 (24.55%) | 26 → 18 |
| ADR-B-11 | 12/35 (34.29%) → 12/35 (34.29%) | 6/35 (17.14%) → 6/35 (17.14%) | 18/70 (25.71%) → 18/70 (25.71%) | 12 → 12 |
| ADR-B-12 | 21/43 (48.84%) → 21/43 (48.84%) | 7/43 (16.28%) → 7/43 (16.28%) | 22/86 (25.58%) → 22/86 (25.58%) | 13 → 13 |
| ADR-B-13 | 11/35 (31.43%) → 11/35 (31.43%) | 6/35 (17.14%) → 6/35 (17.14%) | 14/70 (20.00%) → 14/70 (20.00%) | 12 → 12 |

## Kontrola i dalsze zadania

- 569 pytań, 569 `needs_review`, 0 `verified`; klucze i materiały prawne zachowane.
- Najdłuższa poprawna ≤18% w każdym dziale.
- Globalny wynik najkrótszej może spełniać ≤38%, ale to nie zastępuje wymogu per dział. Dalsze partie powinny obejmować B-03, B-07 i inne działy powyżej 38%.
- Nie oznaczono pytań jako zweryfikowanych; dosłowne porównanie z polskim tekstem ADR 2025 i sprostowaniem pozostaje otwarte.

PASS Quality Gate i scalenie wymagają odnotowania w Issue #10.
