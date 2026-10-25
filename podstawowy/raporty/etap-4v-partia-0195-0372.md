# Etap 4v — korekta wskazówek w 15 pytaniach ADR-B-07 (0195–0372)

**Źródło:** świeży main `4a6466a3897cfefcb0feaba5fa7b1940cba73532`. Zmienione ID: ADR-B-0195, ADR-B-0245, ADR-B-0246, ADR-B-0285, ADR-B-0290, ADR-B-0363, ADR-B-0364, ADR-B-0365, ADR-B-0366, ADR-B-0367, ADR-B-0368, ADR-B-0369, ADR-B-0370, ADR-B-0371, ADR-B-0372.

## Cel i charakter korekty

Dystraktory z absolutami lub niepotrzebnie naprowadzającą długością przeredagowano na konkretne błędne decyzje: podpis zamiast usunięcia naruszenia, odłożenie usterki, opieranie się na niewłaściwym dokumencie lub przerzucanie obowiązku na inną osobę. Tam, gdzie znaczenie poprawnej odpowiedzi pozostawało to samo, doprecyzowano jej brzmienie dla wyrównania długości opcji. W 15 rekordach dostosowano `explanation` do nowych wariantów A/B/C. Każde wyjaśnienie nadal kończy się podstawą ADR i nie stanowi niezależnej recenzji prawnej.

**Bez zmiany:** ID, modułu, klucza A/B/C, źródeł, wersji podstawy, weryfikacji `needs_review`; istniejące oceny prawne i statusy recenzji bez zmian. Odświeżono tylko migawki audytu i odpowiednie arkusze egzaminu próbnego.

## Wskaźniki skryptu `answer_leakage_metrics.py` przed → po

Definicje: najkrótsza/najdłuższa = ściśle, bez remisów, po usunięciu białych znaków; absoluty zgodnie z regexem skryptu; mianownik dla błędnych odpowiedzi = dwa dystraktory na pytanie.

| Dział | Poprawna najkrótsza | Poprawna najdłuższa | Absoluty w błędnych | Tylko w błędnych (pytania) |
|---|---|---|---|---|
| GLOBAL | 235/569 (41.30%) → 223/569 (39.19%) | 81/569 (14.24%) → 81/569 (14.24%) | 279/1138 (24.52%) → 270/1138 (23.73%) | 197 → 190 |
| ADR-B-01 | 13/35 (37.14%) → 13/35 (37.14%) | 6/35 (17.14%) → 6/35 (17.14%) | 15/70 (21.43%) → 15/70 (21.43%) | 12 → 12 |
| ADR-B-02 | 13/56 (23.21%) → 13/56 (23.21%) | 9/56 (16.07%) → 9/56 (16.07%) | 24/112 (21.43%) → 24/112 (21.43%) | 15 → 15 |
| ADR-B-03 | 20/49 (40.82%) → 20/49 (40.82%) | 7/49 (14.29%) → 7/49 (14.29%) | 35/98 (35.71%) → 35/98 (35.71%) | 23 → 23 |
| ADR-B-04 | 16/44 (36.36%) → 16/44 (36.36%) | 7/44 (15.91%) → 7/44 (15.91%) | 21/88 (23.86%) → 21/88 (23.86%) | 19 → 19 |
| ADR-B-05 | 8/40 (20.00%) → 8/40 (20.00%) | 6/40 (15.00%) → 6/40 (15.00%) | 10/80 (12.50%) → 10/80 (12.50%) | 5 → 5 |
| ADR-B-06 | 24/45 (53.33%) → 24/45 (53.33%) | 6/45 (13.33%) → 6/45 (13.33%) | 20/90 (22.22%) → 20/90 (22.22%) | 16 → 16 |
| ADR-B-07 | 30/46 (65.22%) → 18/46 (39.13%) | 5/46 (10.87%) → 5/46 (10.87%) | 21/92 (22.83%) → 12/92 (13.04%) | 17 → 10 |
| ADR-B-08 | 20/40 (50.00%) → 20/40 (50.00%) | 7/40 (17.50%) → 7/40 (17.50%) | 24/80 (30.00%) → 24/80 (30.00%) | 15 → 15 |
| ADR-B-09 | 21/46 (45.65%) → 21/46 (45.65%) | 5/46 (10.87%) → 5/46 (10.87%) | 15/92 (16.30%) → 15/92 (16.30%) | 12 → 12 |
| ADR-B-10 | 26/55 (47.27%) → 26/55 (47.27%) | 4/55 (7.27%) → 4/55 (7.27%) | 40/110 (36.36%) → 40/110 (36.36%) | 26 → 26 |
| ADR-B-11 | 12/35 (34.29%) → 12/35 (34.29%) | 6/35 (17.14%) → 6/35 (17.14%) | 18/70 (25.71%) → 18/70 (25.71%) | 12 → 12 |
| ADR-B-12 | 21/43 (48.84%) → 21/43 (48.84%) | 7/43 (16.28%) → 7/43 (16.28%) | 22/86 (25.58%) → 22/86 (25.58%) | 13 → 13 |
| ADR-B-13 | 11/35 (31.43%) → 11/35 (31.43%) | 6/35 (17.14%) → 6/35 (17.14%) | 14/70 (20.00%) → 14/70 (20.00%) | 12 → 12 |

## Ograniczenia i dalsze działania

Ta partia eliminuje część skrótu „poprawna najkrótsza” oraz wyciek leksykalny, doprecyzowując obowiązki uczestników. Globalny cel najkrótszej ≤38% nie został jeszcze osiągnięty. Wszystkie działy zachowują dotychczasowy wymóg najdłuższej ≤18%. Kontynuować kolejno B-06, B-08, B-10 i B-03 na świeżym `main` w kolejnych PR-ach. Odczyt i zatwierdzenie literalnego polskiego ADR 2025 przez niezależnego eksperta nadal pozostaje otwarte; niczego nie oznaczono jako `verified`.

Quality Gate: wynik zostanie potwierdzony na PR przed scaleniem.
