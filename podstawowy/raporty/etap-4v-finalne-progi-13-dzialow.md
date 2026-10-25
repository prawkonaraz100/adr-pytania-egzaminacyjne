# Etap 4v — uzupełnienie progów we wszystkich 13 działach (20 pytań)

**Świeży main:** `0ede6bd8640f09db3014445862b147b6bfc5fe6f` po PR #291. Zmienione ID: ADR-B-0177, ADR-B-0199, ADR-B-0200, ADR-B-0201, ADR-B-0202, ADR-B-0235, ADR-B-0237, ADR-B-0241, ADR-B-0331, ADR-B-0332, ADR-B-0373, ADR-B-0374, ADR-B-0375, ADR-B-0399, ADR-B-0400, ADR-B-0401, ADR-B-0402, ADR-B-0403, ADR-B-0404, ADR-B-0405.

## Metoda i zakres

W wybranych 20 pytaniach z działów ADR-B-03 (4 pytania), ADR-B-07 (3), ADR-B-09 (6) i ADR-B-12 (7) poprawiono konkretne, oczywiste dystraktory, które niepotrzebnie naprowadzały na odpowiedź przez długość lub absolutne słowa. Pozostały realistyczne błędne interpretacje obowiązków dotyczących odpadów, klas mieszanin, załadunku, mocowania, piętrzenia, dokumentów i planów ochrony. Wszystkie poprawne opcje pozostały dosłownie niezmienione. Dopasowano 20 wyjaśnień (300–500 znaków), każde zakończone istniejącą krótką podstawą ADR. Klucze, źródła, ID, kolejność i statusy `needs_review` bez zmian; niczego nie oznaczono `verified`.

Zaktualizowano migawki audytów sekwencyjnego i prawnego oraz odpowiednie arkusze i klucze egzaminu próbnego. Oceny prawne nie są zatwierdzane przez tę zmianę.

## Metryki globalnie i dla każdego działu

Definicja: `scripts/answer_leakage_metrics.py`, najkrótsza/najdłuższa ścisła bez remisów po `strip()`; wyrazy absolutne w dystraktorach liczone regexem skryptu, mianownik = 2 × liczba pytań.

| Dział | Poprawna najkrótsza przed → po | Poprawna najdłuższa przed → po | Absoluty w błędnych przed → po | Absoluty tylko w błędnych przed → po |
|---|---|---|---|---|
| GLOBAL | 186/569 (32.69%) → 166/569 (29.17%) | 80/569 (14.06%) → 80/569 (14.06%) | 220/1138 (19.33%) → 211/1138 (18.54%) | 154 → 148 |
| ADR-B-01 | 13/35 (37.14%) → 13/35 (37.14%) | 6/35 (17.14%) → 6/35 (17.14%) | 15/70 (21.43%) → 15/70 (21.43%) | 12 → 12 |
| ADR-B-02 | 13/56 (23.21%) → 13/56 (23.21%) | 9/56 (16.07%) → 9/56 (16.07%) | 24/112 (21.43%) → 24/112 (21.43%) | 15 → 15 |
| ADR-B-03 | 20/49 (40.82%) → 16/49 (32.65%) | 7/49 (14.29%) → 7/49 (14.29%) | 35/98 (35.71%) → 34/98 (34.69%) | 23 → 22 |
| ADR-B-04 | 16/44 (36.36%) → 16/44 (36.36%) | 7/44 (15.91%) → 7/44 (15.91%) | 21/88 (23.86%) → 21/88 (23.86%) | 19 → 19 |
| ADR-B-05 | 8/40 (20.00%) → 8/40 (20.00%) | 6/40 (15.00%) → 6/40 (15.00%) | 10/80 (12.50%) → 10/80 (12.50%) | 5 → 5 |
| ADR-B-06 | 6/45 (13.33%) → 6/45 (13.33%) | 5/45 (11.11%) → 5/45 (11.11%) | 2/90 (2.22%) → 2/90 (2.22%) | 1 → 1 |
| ADR-B-07 | 18/46 (39.13%) → 15/46 (32.61%) | 5/46 (10.87%) → 5/46 (10.87%) | 12/92 (13.04%) → 9/92 (9.78%) | 10 → 8 |
| ADR-B-08 | 10/40 (25.00%) → 10/40 (25.00%) | 7/40 (17.50%) → 7/40 (17.50%) | 5/80 (6.25%) → 5/80 (6.25%) | 2 → 2 |
| ADR-B-09 | 21/46 (45.65%) → 15/46 (32.61%) | 5/46 (10.87%) → 5/46 (10.87%) | 15/92 (16.30%) → 12/92 (13.04%) | 12 → 10 |
| ADR-B-10 | 17/55 (30.91%) → 17/55 (30.91%) | 4/55 (7.27%) → 4/55 (7.27%) | 27/110 (24.55%) → 27/110 (24.55%) | 18 → 18 |
| ADR-B-11 | 12/35 (34.29%) → 12/35 (34.29%) | 6/35 (17.14%) → 6/35 (17.14%) | 18/70 (25.71%) → 18/70 (25.71%) | 12 → 12 |
| ADR-B-12 | 21/43 (48.84%) → 14/43 (32.56%) | 7/43 (16.28%) → 7/43 (16.28%) | 22/86 (25.58%) → 20/86 (23.26%) | 13 → 12 |
| ADR-B-13 | 11/35 (31.43%) → 11/35 (31.43%) | 6/35 (17.14%) → 6/35 (17.14%) | 14/70 (20.00%) → 14/70 (20.00%) | 12 → 12 |

## Wynik

- **Wszystkie 13 działów**: poprawna ściśle najkrótsza **≤38%**, absoluty w błędnych odpowiedziach **≤38%**, poprawna ściśle najdłuższa **≤18%**.
- Bank nadal liczy **569 pytań, wszystkie `needs_review`, 0 `verified`**. Metryki to test heurystyk zgadywania, a nie potwierdzenie prawidłowości prawnej.
- Po zakończeniu etapu 4v priorytetem jest jakościowy przegląd powtarzalności sformułowań, merytoryczna recenzja lekcji i praktyki oraz niezależne, dosłowne porównanie z polskim tekstem ADR i sprostowaniem. Zakres bez cystern.

Quality Gate i scalenie wymagają PASS wszystkich kontroli oraz wpisu w Issue #10.
