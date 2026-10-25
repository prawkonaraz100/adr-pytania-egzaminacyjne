# Etap 4v — część 3: 15 pytań ADR-B-08 (0197–0486)

**Punkt wyjścia:** świeży main `d5472c0d055843be26fd8850d51b7e0cc70997bb` po PR #289. IDs: ADR-B-0197, ADR-B-0198, ADR-B-0251, ADR-B-0254, ADR-B-0282, ADR-B-0319, ADR-B-0417, ADR-B-0418, ADR-B-0420, ADR-B-0421, ADR-B-0422, ADR-B-0423, ADR-B-0483, ADR-B-0484, ADR-B-0486.

## Cel i metoda

Dopracowano 15 pytań o wymaganym wyposażeniu pojazdu ADR, gaśnicach, klinach, masce ucieczkowej i świadectwie dopuszczenia. Zastąpiono dystraktory oparte na „zawsze/tylko/wyłącznie” realistycznymi, lecz błędnymi decyzjami (np. ocena samej masy gaśnicy zamiast skuteczności lub zastępowanie klina hamulcem). W jednym pytaniu (ADR-B-0282) skrócono **poprawne brzmienie bez zmiany sensu** — nadal jedna gaśnica 2 kg proszku lub równoważna. W pozostałych 14 pytaniach poprawne opcje pozostały dosłownie niezmienione. Każde `explanation` zaktualizowano do 300–500 znaków i zakończono podstawą ADR. Nie zmieniono źródeł, kluczy, ID, kolejności ani `needs_review`.

Zaktualizowano migawki audytów sekwencyjnego i klauzulowego oraz właściwe wersje arkusza i klucza egzaminu próbnego. Istniejące decyzje audytowe są niezmienione; niezależna kontrola prawnika ADR nadal wymagana.

## Metryki przed → po (569 pytań)

Metoda zgodna z `scripts/answer_leakage_metrics.py`; najkrótsza/najdłuższa = wynik ściśle bez remisów, po `strip()`; dla absolutów mianownik dystraktorów = 2 × pytania.

| Dział | Poprawna najkrótsza | Poprawna najdłuższa | Absoluty w błędnych | Absoluty wyłącznie w błędnych (pytania) |
|---|---|---|---|---|
| GLOBAL | 205/569 (36.03%) → 195/569 (34.27%) | 80/569 (14.06%) → 80/569 (14.06%) | 252/1138 (22.14%) → 233/1138 (20.47%) | 175 → 162 |
| ADR-B-01 | 13/35 (37.14%) → 13/35 (37.14%) | 6/35 (17.14%) → 6/35 (17.14%) | 15/70 (21.43%) → 15/70 (21.43%) | 12 → 12 |
| ADR-B-02 | 13/56 (23.21%) → 13/56 (23.21%) | 9/56 (16.07%) → 9/56 (16.07%) | 24/112 (21.43%) → 24/112 (21.43%) | 15 → 15 |
| ADR-B-03 | 20/49 (40.82%) → 20/49 (40.82%) | 7/49 (14.29%) → 7/49 (14.29%) | 35/98 (35.71%) → 35/98 (35.71%) | 23 → 23 |
| ADR-B-04 | 16/44 (36.36%) → 16/44 (36.36%) | 7/44 (15.91%) → 7/44 (15.91%) | 21/88 (23.86%) → 21/88 (23.86%) | 19 → 19 |
| ADR-B-05 | 8/40 (20.00%) → 8/40 (20.00%) | 6/40 (15.00%) → 6/40 (15.00%) | 10/80 (12.50%) → 10/80 (12.50%) | 5 → 5 |
| ADR-B-06 | 6/45 (13.33%) → 6/45 (13.33%) | 5/45 (11.11%) → 5/45 (11.11%) | 2/90 (2.22%) → 2/90 (2.22%) | 1 → 1 |
| ADR-B-07 | 18/46 (39.13%) → 18/46 (39.13%) | 5/46 (10.87%) → 5/46 (10.87%) | 12/92 (13.04%) → 12/92 (13.04%) | 10 → 10 |
| ADR-B-08 | 20/40 (50.00%) → 10/40 (25.00%) | 7/40 (17.50%) → 7/40 (17.50%) | 24/80 (30.00%) → 5/80 (6.25%) | 15 → 2 |
| ADR-B-09 | 21/46 (45.65%) → 21/46 (45.65%) | 5/46 (10.87%) → 5/46 (10.87%) | 15/92 (16.30%) → 15/92 (16.30%) | 12 → 12 |
| ADR-B-10 | 26/55 (47.27%) → 26/55 (47.27%) | 4/55 (7.27%) → 4/55 (7.27%) | 40/110 (36.36%) → 40/110 (36.36%) | 26 → 26 |
| ADR-B-11 | 12/35 (34.29%) → 12/35 (34.29%) | 6/35 (17.14%) → 6/35 (17.14%) | 18/70 (25.71%) → 18/70 (25.71%) | 12 → 12 |
| ADR-B-12 | 21/43 (48.84%) → 21/43 (48.84%) | 7/43 (16.28%) → 7/43 (16.28%) | 22/86 (25.58%) → 22/86 (25.58%) | 13 → 13 |
| ADR-B-13 | 11/35 (31.43%) → 11/35 (31.43%) | 6/35 (17.14%) → 6/35 (17.14%) | 14/70 (20.00%) → 14/70 (20.00%) | 12 → 12 |

## Wynik i niepewności

- Bramka „poprawna ściśle najdłuższa” spełnia próg ≤18% w każdym dziale.
- Wskaźniki są kontrolą redakcyjną, nie dowodem prawidłowej odpowiedzi ani zatwierdzeniem przez specjalistę.
- Wszystkie 569 pytań pozostają `needs_review`; niczego nie oznaczono `verified`.
- Następna partia: ADR-B-10 i ADR-B-03, później działy nadal przekraczające 38% poprawnej najkrótszej oraz 38% słów absolutnych w dystraktorach; wyłącznie kurs podstawowy.

Wynik Quality Gate i scalenie zostaną odnotowane po potwierdzeniu PASS.
