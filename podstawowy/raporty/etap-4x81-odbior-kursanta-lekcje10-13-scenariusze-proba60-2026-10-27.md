# Etap 4x81 — odbiór kursanta: lekcje B-10–13, scenariusze i próbka explanation

- Data: 27.10.2026.
- Punkt wejściowy: `main` `4549071d53ce2320c71b4b8d46f7bb86e29470d1` (PR #538 scalony, Quality Gate PASS).
- Zakres: wyłącznie kurs podstawowy ADR.

## 1. Kontrola ścieżki lekcja → pytania → scenariusze

| Lekcja | Pytania w dziale | Referencje w lekcji | Brakujące ID | Obce działy | Pełne scenariusze |
|---|---:|---:|---:|---:|---:|
| B-10 | 55 | 55 | 0 | 0 | 3 |
| B-11 | 43 | 43 | 0 | 0 | 3 |
| B-12 | 44 | 44 | 0 | 0 | 3 |
| B-13 | 47 | 47 | 0 | 0 | 3 |

W czterech lekcjach sprawdzono układ rozdziałów, „Typowe błędy kursantów”, „Sprawdź się”, wykaz pytań i bezpośrednie linki do wszystkich trzech scenariuszy działu. Każde ID banku z danego modułu występuje w wykazie lekcji; nie znaleziono brakujących ani błędnie przypisanych referencji. Terminy fachowe przy pierwszym użyciu mają objaśnienie inline lub odsyłacz do słowniczka. Nie znaleziono potwierdzonej luki tematycznej uzasadniającej dodanie pytania.

## 2. Przegląd scenariuszy

Sprawdzono wszystkie 12 scenariuszy działów B-10–B-13. Każdy zawiera:
- konkretną sytuację;
- cztery kroki działania;
- co najmniej trzy typowe błędy wraz z wyjaśnieniem, dlaczego są błędne;
- podstawę ADR, kryteria oceny, wniosek dla kursanta i pytanie do omówienia;
- istniejące `question_ids` wyłącznie z właściwego modułu.

Wynik kontroli strukturalnej i powiązań: **0 brakujących ID, 0 odwołań do innego działu, 0 brakujących kroków lub kryteriów**. Nie zmieniono treści scenariuszy, ponieważ nie stwierdzono potwierdzonego błędu ani braku.

## 3. Próbka 60 explanation

- Metoda: deterministyczne losowanie z puli 189 pytań działów B-10–B-13, seed `2026102781`.
- Liczebność: B-10 — 18, B-11 — 12, B-12 — 17, B-13 — 13.
- Przeczytano stem, opcje A/B/C, klucz i explanation; sprawdzono sens poprawnej odpowiedzi, omówienie błędnych opcji, język, podstawę ADR i długość zdań.
- Minimum explanation w próbce: 303 znaki; poniżej 200 znaków: 0; jednozdaniowe: 0; zdania ponad 35 słów według kontroli technicznej: 0.
- Nie stwierdzono potwierdzonej sprzeczności wewnętrznej wymagającej zmiany klucza lub wyjaśnienia. Przykłady z kodami tunelowymi, dokumentami w transporcie morsko-drogowym, ochroną przewozu i dokumentami kierowcy wyjaśniają, dlaczego błędne opcje nie wystarczają lub mylą różne obowiązki.
- Lista próby (ID): ADR-B-0211, ADR-B-0524, ADR-B-0403, ADR-B-0321, ADR-B-0228, ADR-B-0247, ADR-B-0402, ADR-B-0414, ADR-B-0435, ADR-B-0264, ADR-B-0274, ADR-B-0434, ADR-B-0588, ADR-B-0575, ADR-B-0490, ADR-B-0445, ADR-B-0601, ADR-B-0437, ADR-B-0203, ADR-B-0204, ADR-B-0277, ADR-B-0409, ADR-B-0030, ADR-B-0459, ADR-B-0028, ADR-B-0539, ADR-B-0511, ADR-B-0458, ADR-B-0519, ADR-B-0438, ADR-B-0066, ADR-B-0411, ADR-B-0451, ADR-B-0574, ADR-B-0121, ADR-B-0145, ADR-B-0589, ADR-B-0444, ADR-B-0405, ADR-B-0452, ADR-B-0033, ADR-B-0069, ADR-B-0086, ADR-B-0447, ADR-B-0248, ADR-B-0415, ADR-B-0206, ADR-B-0525, ADR-B-0384, ADR-B-0234, ADR-B-0068, ADR-B-0034, ADR-B-0037, ADR-B-0396, ADR-B-0304, ADR-B-0063, ADR-B-0322, ADR-B-0039, ADR-B-0577, ADR-B-0416.

To jest przegląd dydaktyczny i strukturalny, nie niezależna recenzja prawna. Brak flagi w próbce nie potwierdza prawidłowości przepisu.

## 4. Metryki banku po PR #538

- Liczba pytań: 609; unikalne ID: 609.
- Statusy: 609 `needs_review`, 0 `verified`.
- Poprawna odpowiedź jest jedyną najdłuższą: 73/609 = 11.99%.
- Najkrótsze explanation w banku: 300 znaków; poniżej 200 znaków: 0.
- ADR-B-10: 4/55 = 7.27% poprawnych odpowiedzi jako jedynych najdłuższych.
- ADR-B-11: 6/43 = 13.95% poprawnych odpowiedzi jako jedynych najdłuższych.
- ADR-B-12: 6/44 = 13.64% poprawnych odpowiedzi jako jedynych najdłuższych.
- ADR-B-13: 5/47 = 10.64% poprawnych odpowiedzi jako jedynych najdłuższych.

## 5. Decyzje i ograniczenia

Nie zmieniano pytań, kluczy ani podstaw prawnych, ponieważ nie wykryto potwierdzonego błędu. Nie dodano nowych pytań: w badanym zakresie wszystkie pytania działów są powiązane z właściwą lekcją, a przegląd nie ujawnił brakującej kompetencji programu. Wszystkie rekordy pozostają `needs_review`; nie oznaczono niczego jako `verified`.

Testy lokalne nie były dostępne przez integrację GitHub; kontrolę danych wykonano na pobranej zawartości, a wymagany Quality Gate uruchomiono w CI przed scaleniem.
