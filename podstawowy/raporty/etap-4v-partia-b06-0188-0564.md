# Etap 4v — partia 25 pytań z działu ADR-B-06

**Świeży main:** `544dcc44f13b50912cde0123ee0768d1c3b9f4af` (po PR #288). Pytania: ADR-B-0188, ADR-B-0189, ADR-B-0190, ADR-B-0191, ADR-B-0192, ADR-B-0193, ADR-B-0194, ADR-B-0217, ADR-B-0256, ADR-B-0281, ADR-B-0299, ADR-B-0303, ADR-B-0503, ADR-B-0504, ADR-B-0505, ADR-B-0506, ADR-B-0507, ADR-B-0543, ADR-B-0544, ADR-B-0547, ADR-B-0548, ADR-B-0561, ADR-B-0562, ADR-B-0563, ADR-B-0564.

## Zasady edycji

W 25 pytaniach zmodyfikowano błędne warianty na konkretne, wiarygodnie brzmiące, ale nieprawidłowe rozumowania. Usunięto część słów wskazujących odpowiedź z góry; tam, gdzie to potrzebne, jedna błędna odpowiedź jest krótsza, druga dłuższa od poprawnej, aby klucz nie wyróżniał się długością. **Nie zmieniono nawet brzmienia poprawnych wariantów**, kluczy, numerów, modułów, `verification_status`, podstaw prawnych ani przypisania do kompetencji. Wszystkie zmienione `explanation` mają 300–500 znaków i zachowują krótki przepis ADR na końcu. To kontrola redakcyjna, a nie formalna legalizacja pytań.

Po zmianie odświeżono migawki audytu sekwencyjnego i prawnego oraz warianty/klucze egzaminu próbnego, w których występowały zmienione pytania.

## Pomiar wszystkich 13 działów

Metodyka: `scripts/answer_leakage_metrics.py`; długości po `strip()`, ściśle najkrótsza i najdłuższa bez remisów, absoluty w dystraktorach według pełnych słów z regexu, mianownik = 2×liczba pytań.

| Dział | Poprawna najkrótsza przed → po | Poprawna najdłuższa przed → po | Absoluty w błędnych przed → po | Tylko w błędnych przed → po |
|---|---|---|---|---|
| GLOBAL | 223/569 (39.19%) → 205/569 (36.03%) | 81/569 (14.24%) → 80/569 (14.06%) | 270/1138 (23.73%) → 252/1138 (22.14%) | 190 → 175 |
| ADR-B-01 | 13/35 (37.14%) → 13/35 (37.14%) | 6/35 (17.14%) → 6/35 (17.14%) | 15/70 (21.43%) → 15/70 (21.43%) | 12 → 12 |
| ADR-B-02 | 13/56 (23.21%) → 13/56 (23.21%) | 9/56 (16.07%) → 9/56 (16.07%) | 24/112 (21.43%) → 24/112 (21.43%) | 15 → 15 |
| ADR-B-03 | 20/49 (40.82%) → 20/49 (40.82%) | 7/49 (14.29%) → 7/49 (14.29%) | 35/98 (35.71%) → 35/98 (35.71%) | 23 → 23 |
| ADR-B-04 | 16/44 (36.36%) → 16/44 (36.36%) | 7/44 (15.91%) → 7/44 (15.91%) | 21/88 (23.86%) → 21/88 (23.86%) | 19 → 19 |
| ADR-B-05 | 8/40 (20.00%) → 8/40 (20.00%) | 6/40 (15.00%) → 6/40 (15.00%) | 10/80 (12.50%) → 10/80 (12.50%) | 5 → 5 |
| ADR-B-06 | 24/45 (53.33%) → 6/45 (13.33%) | 6/45 (13.33%) → 5/45 (11.11%) | 20/90 (22.22%) → 2/90 (2.22%) | 16 → 1 |
| ADR-B-07 | 18/46 (39.13%) → 18/46 (39.13%) | 5/46 (10.87%) → 5/46 (10.87%) | 12/92 (13.04%) → 12/92 (13.04%) | 10 → 10 |
| ADR-B-08 | 20/40 (50.00%) → 20/40 (50.00%) | 7/40 (17.50%) → 7/40 (17.50%) | 24/80 (30.00%) → 24/80 (30.00%) | 15 → 15 |
| ADR-B-09 | 21/46 (45.65%) → 21/46 (45.65%) | 5/46 (10.87%) → 5/46 (10.87%) | 15/92 (16.30%) → 15/92 (16.30%) | 12 → 12 |
| ADR-B-10 | 26/55 (47.27%) → 26/55 (47.27%) | 4/55 (7.27%) → 4/55 (7.27%) | 40/110 (36.36%) → 40/110 (36.36%) | 26 → 26 |
| ADR-B-11 | 12/35 (34.29%) → 12/35 (34.29%) | 6/35 (17.14%) → 6/35 (17.14%) | 18/70 (25.71%) → 18/70 (25.71%) | 12 → 12 |
| ADR-B-12 | 21/43 (48.84%) → 21/43 (48.84%) | 7/43 (16.28%) → 7/43 (16.28%) | 22/86 (25.58%) → 22/86 (25.58%) | 13 → 13 |
| ADR-B-13 | 11/35 (31.43%) → 11/35 (31.43%) | 6/35 (17.14%) → 6/35 (17.14%) | 14/70 (20.00%) → 14/70 (20.00%) | 12 → 12 |

## Sprawdzenie bezpieczeństwa zmian

- Liczba pytań: 569 → 569; ID i kolejność bez zmian.
- Statusy: 569 `needs_review`, 0 `verified`; brak zmian kluczy i podstaw.
- Wskaźnik najdłuższej poprawnej nie przekracza 18% w żadnym dziale.
- Otwarty cel: poprawna najkrótsza ≤38% oraz absoluty w błędnych ≤38% w każdym dziale. Samo spełnienie metryk nie jest odbiorem eksperta ADR.
- Kolejne priorytety: B-07 (reszta), B-08, B-10, B-03 i pozostałe działy z wynikiem >38%. Nie rozpoczynać cystern.

Quality Gate musi uzyskać PASS w PR przed scaleniem, a wynik zostanie wpisany do Issue #10.
