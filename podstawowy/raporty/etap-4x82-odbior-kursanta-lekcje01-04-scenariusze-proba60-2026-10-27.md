# Etap 4x82 — odbiór kursanta: lekcje B-01–04, scenariusze i próbka explanation

- Data: 27.10.2026.
- Punkt wejściowy: `main` `98d6e7b2fbb56295ece570daacb967ff09798b8a` (po PR #539 i PASS CI).
- Zakres: wyłącznie kurs podstawowy ADR.

## 1. Kontrola ścieżki lekcja → pytania → scenariusze

| Lekcja | Pytania w dziale | Referencje w lekcji | Brakujące ID | Obce działy | Pełne scenariusze |
|---|---:|---:|---:|---:|---:|
| B-01 | 45 | 45 | 0 | 0 | 3 |
| B-02 | 56 | 56 | 0 | 0 | 3 |
| B-03 | 49 | 49 | 0 | 0 | 3 |
| B-04 | 46 | 46 | 0 | 0 | 3 |

Sprawdzono wykazy pytań, odwołania do słowniczka, rozdział „Typowe błędy kursantów”, sekcję „Sprawdź się” i bezpośrednie linki do trzech pełnych scenariuszy. Wszystkie 196 pytań B-01–B-04 mają odwołanie w lekcji właściwego działu; brakujące i błędnie przypisane ID: 0.

## 2. Przegląd scenariuszy

Sprawdzono 12 scenariuszy B-01–B-04. Każdy ma konkretną sytuację, cztery kroki, trzy typowe błędy z wyjaśnieniem, podstawę ADR, kryteria oceny, wniosek dla kursanta i pytanie do omówienia. Wszystkie `question_ids` istnieją i należą do modułu scenariusza.

Wynik kontroli strukturalnej: **0 brakujących ID, 0 odwołań do obcego działu, 0 brakujących kroków/kryteriów**. Nie znaleziono potwierdzonego błędu w scenariuszach, więc nie zmieniano ich treści ani podstaw prawnych.

## 3. Próbka 60 explanation

- Metoda: deterministyczne losowanie z puli 196 pytań B-01–B-04, seed `2026102782`.
- Przeczytano treść pytania, opcje A/B/C, klucz i explanation; sprawdzono, czy wyjaśnienie uzasadnia poprawną odpowiedź, omawia mylące alternatywy, używa języka dla początkującego i kończy się podstawą ADR.
- Minimum explanation w próbce: 300 znaków; poniżej 200 znaków: 0; jednozdaniowe: 0; zdania ponad 35 słów według kontroli technicznej: 0.
- Próbka nie ujawniła potwierdzonej sprzeczności z podręcznikiem ani problemu wymagającego zmiany klucza.
- Lista próby (ID): ADR-B-0008, ADR-B-0288, ADR-B-0001, ADR-B-0333, ADR-B-0103, ADR-B-0302, ADR-B-0331, ADR-B-0311, ADR-B-0605, ADR-B-0094, ADR-B-0355, ADR-B-0360, ADR-B-0003, ADR-B-0289, ADR-B-0004, ADR-B-0152, ADR-B-0279, ADR-B-0243, ADR-B-0500, ADR-B-0581, ADR-B-0045, ADR-B-0124, ADR-B-0040, ADR-B-0318, ADR-B-0157, ADR-B-0178, ADR-B-0609, ADR-B-0006, ADR-B-0361, ADR-B-0273, ADR-B-0362, ADR-B-0571, ADR-B-0046, ADR-B-0467, ADR-B-0572, ADR-B-0475, ADR-B-0468, ADR-B-0580, ADR-B-0100, ADR-B-0513, ADR-B-0092, ADR-B-0522, ADR-B-0501, ADR-B-0350, ADR-B-0244, ADR-B-0126, ADR-B-0161, ADR-B-0470, ADR-B-0526, ADR-B-0044, ADR-B-0359, ADR-B-0125, ADR-B-0261, ADR-B-0465, ADR-B-0466, ADR-B-0297, ADR-B-0270, ADR-B-0495, ADR-B-0301, ADR-B-0528.

## 4. Metryki banku i rozkład długości

- Bank: 609 pytań; unikalne ID: 609.
- Status: 609 `needs_review`, 0 `verified`.
- Poprawna odpowiedź jest jedyną najdłuższą w 73/609 = 11.99%; najkrótsze explanation 300 znaków; poniżej 200 znaków: 0.
- ADR-B-01: 6/45 = 13.33% poprawnych odpowiedzi jako jedynych najdłuższych.
- ADR-B-02: 8/56 = 14.29% poprawnych odpowiedzi jako jedynych najdłuższych.
- ADR-B-03: 7/49 = 14.29% poprawnych odpowiedzi jako jedynych najdłuższych.
- ADR-B-04: 6/46 = 13.04% poprawnych odpowiedzi jako jedynych najdłuższych.

## 5. Decyzja

Nie wprowadzono zmian do lekcji, scenariuszy ani banku, ponieważ nie znaleziono potwierdzonej luki programu, brakującego pytania, sprzeczności wewnętrznej ani usterki językowej w próbie. Nie dodano pytań: brak podstaw do uznania, że treść wymaga dopisania na podstawie tej kontroli. Wszystkie pytania pozostają `needs_review`; niczego nie oznaczono jako `verified`.

Testów lokalnych nie można uruchomić z poziomu integracji GitHub; wymagany Quality Gate zostanie wykonany przez CI na PR. Kontrola w raporcie jest strukturalna i dydaktyczna, a nie niezależną recenzją prawną.
