# Etap 4x48 — raport zbiorczy

- Data: 2026-10-26.
- Punkt wyjścia: świeży `main` `45e88b3ebffc9ca74fe81a196e0c3691bac92d24`.
- Zakres: wyłącznie kurs podstawowy ADR.

## Wynik próbki explanation

- Próbka: 60 unikalnych ID, seed `2026102648`; wykluczono próbkę 4x45 (40 ID), 4x46 (60 ID) i 13 sygnałów z 4x47.
- Ręczny odbiór redakcyjny: 60 ocenionych, 0 przepisanych. Każde explanation miało 3–5 zdań, 300+ znaków, podstawę ADR i wyjaśniało, dlaczego kuszące błędne odpowiedzi nie pasują do sytuacji. Brak zmian nie oznacza zatwierdzenia prawnego.

## Scenariusze praktyczne

- 39 scenariuszy w 13 działach, po 3 na dział.
- W trzech PR-ach (#491–#493) zawężono listy `question_ids` do 1–3 pytań dopasowanych do sytuacji.
- Końcowa liczba linków do pytań: 108; minimum na scenariusz 1, maksimum 3.
- Brak brakujących ID i brak odwołań między działami.
- Materiały instruktorskie, scenariusze, odpowiedzi i klucze pozostają materiałami szkoleniowymi; nie są formalnym zatwierdzeniem prawnym.

## Wskaźnik „poprawna = jedyna najdłuższa”

- Globalnie: 72/609 = 11.82%.
- Najkrótsze explanation: 300 znaków; explanation poniżej 200 znaków: 0.
- Statusy: 609 `needs_review`, 0 `verified`.

| Dział | Pytań | Poprawna jedyną najdłuższą | Wskaźnik |
|---|---:|---:|---:|
| ADR-B-01 | 45 | 6 | 13.33% |
| ADR-B-02 | 56 | 7 | 12.50% |
| ADR-B-03 | 49 | 7 | 14.29% |
| ADR-B-04 | 46 | 6 | 13.04% |
| ADR-B-05 | 43 | 5 | 11.63% |
| ADR-B-06 | 45 | 5 | 11.11% |
| ADR-B-07 | 48 | 6 | 12.50% |
| ADR-B-08 | 42 | 5 | 11.90% |
| ADR-B-09 | 46 | 4 | 8.70% |
| ADR-B-10 | 55 | 4 | 7.27% |
| ADR-B-11 | 43 | 6 | 13.95% |
| ADR-B-12 | 44 | 6 | 13.64% |
| ADR-B-13 | 47 | 5 | 10.64% |

## Utrwalenie jakości w CI

Dodano blokującą kontrolę w `tests/test_course_consistency.py`: każdy scenariusz musi linkować 1–3 unikalne pytania, każde ID musi istnieć w banku i należeć do tego samego modułu. Zapobiega to ponownemu narastaniu list linków, które zacierały cel dydaktyczny scenariusza.

## Ograniczenia

Repozytoryjnych testów lokalnych nie można uruchomić przez GitHub Contents API. PR wymaga pełnego Quality Gate CI. Bank nie był zmieniany, dlatego warianty egzaminów i klucze nie wymagały regeneracji. Nie dodano pytań: nie stwierdzono potwierdzonej luki programu wymagającej nowego rekordu. Wszystkie pytania pozostają `needs_review`.
