# Etap 4x28 — końcowa kontrola spójności kursu podstawowego

- Data: 2026-10-26.
- Świeży `main` na starcie: `ebcfb4421893fcb2c6feb8aab66c94f5f2f43f09`.
- Zakres: wyłącznie kurs podstawowy ADR; bez zmian statusów weryfikacji prawnej.

## 1. Spójność krzyżowa ID pytań

Porównano `podstawowy/questions.jsonl` z 13 lekcjami, 13 materiałami instruktora i mapą scenariuszy. ID sprawdzano względem `module_id` w banku, nie tylko względem wzorca tekstowego.

| Dział | Pytania w banku | Unikalne ID w lekcji | Brakujące ID | ID z innego działu | ID w materiale instruktora | Scenariusze |
|---|---:|---:|---:|---:|---:|---:|
| B-01 | 45 | 45 | 0 | 0 | 15 | 3 |
| B-02 | 56 | 56 | 0 | 0 | 10 | 3 |
| B-03 | 49 | 49 | 0 | 0 | 9 | 3 |
| B-04 | 46 | 46 | 0 | 0 | 12 | 3 |
| B-05 | 43 | 43 | 0 | 0 | 10 | 3 |
| B-06 | 45 | 45 | 0 | 0 | 7 | 3 |
| B-07 | 48 | 48 | 0 | 0 | 14 | 3 |
| B-08 | 42 | 42 | 0 | 0 | 11 | 3 |
| B-09 | 46 | 46 | 0 | 0 | 11 | 3 |
| B-10 | 55 | 55 | 0 | 0 | 10 | 3 |
| B-11 | 43 | 43 | 0 | 0 | 17 | 3 |
| B-12 | 44 | 44 | 0 | 0 | 11 | 3 |
| B-13 | 47 | 47 | 0 | 0 | 18 | 3 |
| **Razem** | **609** | **609** | **0** | **0** | **155** | **39** |

Wszystkie 39 scenariuszy mają niepuste `question_ids`; każde ID istnieje w banku i należy do modułu scenariusza. Brak pustych powiązań, błędnych przypisań i powtórzonych ID scenariuszy. Każda lekcja obejmuje wszystkie ID pytań swojego modułu. Nie znaleziono błędnego odnośnika wymagającego poprawki.

## 2. Terminologia

Sprawdzono użycie kluczowych pojęć w banku, lekcjach, scenariuszach i słowniczku, w tym: numer UN, LQ/EQ, jednostka transportowa, kod tunelowy, dokument przewozowy, instrukcje pisemne, pojazdy EX/II oraz świadectwo dopuszczenia pojazdu.

- **Ujednolicenie nazwy dokumentu kierowcy:** podstawowa nazwa w słowniczku pozostaje „Zaświadczenie kierowcy ADR”; dodano przy niej objaśnienie, że w banku spotyka się również wariant „zaświadczenie ADR kierowcy”. Nie zmienia to znaczenia prawnego ani odpowiedzi.
- Formy „instrukcja pisemna/instrukcje pisemne” są różnicą liczby gramatycznej, a nie dwoma dokumentami.
- Nie znaleziono potwierdzonej sprzeczności terminologicznej wymagającej zmiany merytoryki pytań.

## 3. Losowa próba 60 wyjaśnień

- Metoda: deterministyczne losowanie wewnątrz każdego modułu, ziarno `4282026`.
- Próba: 5 pytań z B-01, B-02, B-03, B-04, B-07, B-09, B-10 i B-13; 4 pytania z pozostałych pięciu modułów. Łącznie 60 pytań, proporcjonalnie do wielkości działów.
- ID próby:
  - B-01: ADR-B-0534, ADR-B-0123, ADR-B-0312, ADR-B-0529, ADR-B-0149
  - B-02: ADR-B-0542, ADR-B-0095, ADR-B-0160, ADR-B-0502, ADR-B-0267
  - B-03: ADR-B-0463, ADR-B-0242, ADR-B-0464, ADR-B-0341, ADR-B-0462
  - B-04: ADR-B-0297, ADR-B-0012, ADR-B-0347, ADR-B-0361, ADR-B-0362
  - B-05: ADR-B-0593, ADR-B-0110, ADR-B-0109, ADR-B-0232
  - B-06: ADR-B-0052, ADR-B-0548, ADR-B-0545, ADR-B-0258
  - B-07: ADR-B-0135, ADR-B-0020, ADR-B-0569, ADR-B-0479, ADR-B-0196
  - B-08: ADR-B-0419, ADR-B-0422, ADR-B-0056, ADR-B-0423
  - B-09: ADR-B-0291, ADR-B-0239, ADR-B-0240, ADR-B-0173, ADR-B-0425
  - B-10: ADR-B-0385, ADR-B-0395, ADR-B-0439, ADR-B-0447, ADR-B-0452
  - B-11: ADR-B-0488, ADR-B-0489, ADR-B-0435, ADR-B-0308
  - B-12: ADR-B-0067, ADR-B-0274, ADR-B-0408, ADR-B-0458
  - B-13: ADR-B-0216, ADR-B-0508, ADR-B-0579, ADR-B-0599, ADR-B-0069

### Wynik oceny języka

| Kryterium | Wynik |
|---|---:|
| Wyjaśnienia ocenione | 60/60 |
| Długość najkrótszego w próbie | 300 znaków |
| Wyjaśnienia poniżej 200 znaków | 0 |
| Wyjaśnienia poza zakresem 2–5 zdań | 0 |
| Wyjaśnienia rozpoczynające się od samego numeru przepisu | 0 |
| Wyjaśnienia bez wskazanej podstawy ADR | 0 |
| Potwierdzone przypadki wymagające przepisania w tej próbie | 0 |

Przegląd próby nie wykazał wyjaśnienia, które wymagałoby przepisania. W wybranych odpowiedziach wyjaśniono sens poprawnej opcji, wskazano, dlaczego pozostałe warianty mylą, i podano podstawę. To kontrola języka i struktury próby, nie pełna niezależna weryfikacja prawna 609 pytań.

## 4. Wskaźniki banku

| Dział | Pytań | Poprawna odpowiedź jest jedyną najdłuższą | Wskaźnik |
|---|---:|---:|---:|
| B-01 | 45 | 6 | 13,33% |
| B-02 | 56 | 8 | 14,29% |
| B-03 | 49 | 7 | 14,29% |
| B-04 | 46 | 6 | 13,04% |
| B-05 | 43 | 6 | 13,95% |
| B-06 | 45 | 5 | 11,11% |
| B-07 | 48 | 6 | 12,50% |
| B-08 | 42 | 5 | 11,90% |
| B-09 | 46 | 4 | 8,70% |
| B-10 | 55 | 4 | 7,27% |
| B-11 | 43 | 6 | 13,95% |
| B-12 | 44 | 6 | 13,64% |
| B-13 | 47 | 4 | 8,51% |
| **Łącznie** | **609** | **73** | **11,99%** |

- Najkrótsze wyjaśnienie w całym banku: 300 znaków.
- Wyjaśnienia poniżej 200 znaków: 0.
- Pytania `needs_review`: 609; `verified`: 0.
- Klucze egzaminów próbnych 001–005 nie były modyfikowane, bo ta kontrola nie wymagała zmiany pytań ani ich przypisania.

## 5. Ścieżka kursanta

`podstawowy/README.md` już zawiera kolejność nauki: lekcja → pytania działu → czytanie wyjaśnień po każdej odpowiedzi → trzy scenariusze → egzaminy próbne 001–005 i osobne klucze. Wyjaśnia też, że scenariusze są symulacjami, a egzaminy materiałem treningowym, nie oficjalnym testem. Nie dublowano tych informacji w kolejnym pliku startowym.

## 6. Zabezpieczenie przed regresją

Rozszerzono `tests/test_lesson_question_references.py` o test, który blokuje zmianę, jeśli choć jedno pytanie z banku przestanie być wymienione w lekcji przypisanej do jego modułu. Dotychczasowe testy sprawdzają istnienie ID, zgodność modułu i scenariusze; nowy test dopina brakującą kontrolę pełnego pokrycia banku przez lekcje.

## Status i ograniczenia

- Potwierdzone błędne odnośniki: **0 znalezionych, 0 poprawionych**.
- Wyjaśnienia przepisane w próbie 60: **0** (nie znaleziono potwierdzonego problemu).
- Dodano: test regresyjny pełnego pokrycia lekcji oraz doprecyzowanie aliasu nazwy zaświadczenia ADR w słowniczku.
- Wszystkie pytania pozostają `needs_review`; nie nadano statusu `verified`.
- Pełna zgodność prawna wszystkich treści wymaga nadal niezależnej recenzji specjalisty ADR. Nie rozpoczęto żadnego innego kursu.
