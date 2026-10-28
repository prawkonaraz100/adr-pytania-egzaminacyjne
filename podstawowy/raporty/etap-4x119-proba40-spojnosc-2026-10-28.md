# Etap 4x119 — próbka 40, odzyskanie unikalnych poprawek i kontrola spójności

- Data: 2026-10-28.
- Punkt wejścia: świeży `main` `f32658028db001698ca398ab5292221e8467886d` (po PR #578).
- Bank po przeniesieniu zmian: 609 pytań; blob `35549752d913c85daf1fc3c9492d9c04fce777a1`; wszystkie `needs_review`, zero `verified`.
- Seed próby: `41192026`; pula po wykluczeniach: 430; próba: 40 ID, bez powtórzeń.
- Wskaźnik „poprawna = jedyna najdłuższa”: 72/609 = 11,82%; maksimum działu 14,29%; minimum explanation 300 znaków; poniżej 200 znaków: 0.

## 1. PR #579 — rozstrzygnięcie

PR #579 zamknięto bez scalania po konflikcie z main po PR #578. Porównanie patchy wykazało jednak siedem ID z redakcyjnymi zmianami, których nie było w #578: ADR-B-0193, ADR-B-0197, ADR-B-0223, ADR-B-0458, ADR-B-0496, ADR-B-0505 i ADR-B-0577. Przeniesiono je na świeżą gałąź; zaktualizowano odpowiadające migawki w rejestrach `review/legal-clauses` i `review/sequential`, zachowując status `needs_review`. Nie zmieniono poprawnych liter.

## 2. Próba 40 — ręczny odbiór redakcyjny

Wszystkie poniższe pytania przeczytano pod kątem sensu poprawnej odpowiedzi, wyjaśnienia błędnych odpowiedzi, zrozumiałości dla początkującego, podstawy ADR oraz zgodności z lekcją/egzaminem. Nie stwierdzono potwierdzonej słabości redakcyjnej wymagającej zmiany treści w tej próbce; dlatego nie zmieniono żadnego z tych 40 pytań. To wynik przeglądu redakcyjnego, a nie potwierdzenie prawne.

| ID | Wynik | Uwagi |
|---|---|---|
| ADR-B-0032 | PASS redakcyjny | Wyjaśnienie podaje sens, odnosi się do błędnych odpowiedzi i wskazuje podstawę ADR. |
| ADR-B-0037 | PASS redakcyjny | Wyjaśnienie podaje sens, odnosi się do błędnych odpowiedzi i wskazuje podstawę ADR. |
| ADR-B-0042 | PASS redakcyjny | Wyjaśnienie podaje sens, odnosi się do błędnych odpowiedzi i wskazuje podstawę ADR. |
| ADR-B-0083 | PASS redakcyjny | Wyjaśnienie podaje sens, odnosi się do błędnych odpowiedzi i wskazuje podstawę ADR. |
| ADR-B-0088 | PASS redakcyjny | Wyjaśnienie podaje sens, odnosi się do błędnych odpowiedzi i wskazuje podstawę ADR. |
| ADR-B-0106 | PASS redakcyjny | Wyjaśnienie podaje sens, odnosi się do błędnych odpowiedzi i wskazuje podstawę ADR. |
| ADR-B-0116 | PASS redakcyjny | Wyjaśnienie podaje sens, odnosi się do błędnych odpowiedzi i wskazuje podstawę ADR. |
| ADR-B-0120 | PASS redakcyjny | Wyjaśnienie podaje sens, odnosi się do błędnych odpowiedzi i wskazuje podstawę ADR. |
| ADR-B-0160 | PASS redakcyjny | Wyjaśnienie podaje sens, odnosi się do błędnych odpowiedzi i wskazuje podstawę ADR. |
| ADR-B-0195 | PASS redakcyjny | Wyjaśnienie podaje sens, odnosi się do błędnych odpowiedzi i wskazuje podstawę ADR. |
| ADR-B-0216 | PASS redakcyjny | Wyjaśnienie podaje sens, odnosi się do błędnych odpowiedzi i wskazuje podstawę ADR. |
| ADR-B-0220 | PASS redakcyjny | Wyjaśnienie podaje sens, odnosi się do błędnych odpowiedzi i wskazuje podstawę ADR. |
| ADR-B-0253 | PASS redakcyjny | Wyjaśnienie podaje sens, odnosi się do błędnych odpowiedzi i wskazuje podstawę ADR. |
| ADR-B-0254 | PASS redakcyjny | Wyjaśnienie podaje sens, odnosi się do błędnych odpowiedzi i wskazuje podstawę ADR. |
| ADR-B-0281 | PASS redakcyjny | Wyjaśnienie podaje sens, odnosi się do błędnych odpowiedzi i wskazuje podstawę ADR. |
| ADR-B-0286 | PASS redakcyjny | Wyjaśnienie podaje sens, odnosi się do błędnych odpowiedzi i wskazuje podstawę ADR. |
| ADR-B-0303 | PASS redakcyjny | Wyjaśnienie podaje sens, odnosi się do błędnych odpowiedzi i wskazuje podstawę ADR. |
| ADR-B-0321 | PASS redakcyjny | Wyjaśnienie podaje sens, odnosi się do błędnych odpowiedzi i wskazuje podstawę ADR. |
| ADR-B-0323 | PASS redakcyjny | Wyjaśnienie podaje sens, odnosi się do błędnych odpowiedzi i wskazuje podstawę ADR. |
| ADR-B-0329 | PASS redakcyjny | Wyjaśnienie podaje sens, odnosi się do błędnych odpowiedzi i wskazuje podstawę ADR. |
| ADR-B-0341 | PASS redakcyjny | Wyjaśnienie podaje sens, odnosi się do błędnych odpowiedzi i wskazuje podstawę ADR. |
| ADR-B-0364 | PASS redakcyjny | Wyjaśnienie podaje sens, odnosi się do błędnych odpowiedzi i wskazuje podstawę ADR. |
| ADR-B-0371 | PASS redakcyjny | Wyjaśnienie podaje sens, odnosi się do błędnych odpowiedzi i wskazuje podstawę ADR. |
| ADR-B-0389 | PASS redakcyjny | Wyjaśnienie podaje sens, odnosi się do błędnych odpowiedzi i wskazuje podstawę ADR. |
| ADR-B-0409 | PASS redakcyjny | Wyjaśnienie podaje sens, odnosi się do błędnych odpowiedzi i wskazuje podstawę ADR. |
| ADR-B-0429 | PASS redakcyjny | Wyjaśnienie podaje sens, odnosi się do błędnych odpowiedzi i wskazuje podstawę ADR. |
| ADR-B-0440 | PASS redakcyjny | Wyjaśnienie podaje sens, odnosi się do błędnych odpowiedzi i wskazuje podstawę ADR. |
| ADR-B-0441 | PASS redakcyjny | Wyjaśnienie podaje sens, odnosi się do błędnych odpowiedzi i wskazuje podstawę ADR. |
| ADR-B-0445 | PASS redakcyjny | Wyjaśnienie podaje sens, odnosi się do błędnych odpowiedzi i wskazuje podstawę ADR. |
| ADR-B-0485 | PASS redakcyjny | Wyjaśnienie podaje sens, odnosi się do błędnych odpowiedzi i wskazuje podstawę ADR. |
| ADR-B-0516 | PASS redakcyjny | Wyjaśnienie podaje sens, odnosi się do błędnych odpowiedzi i wskazuje podstawę ADR. |
| ADR-B-0525 | PASS redakcyjny | Wyjaśnienie podaje sens, odnosi się do błędnych odpowiedzi i wskazuje podstawę ADR. |
| ADR-B-0527 | PASS redakcyjny | Wyjaśnienie podaje sens, odnosi się do błędnych odpowiedzi i wskazuje podstawę ADR. |
| ADR-B-0537 | PASS redakcyjny | Wyjaśnienie podaje sens, odnosi się do błędnych odpowiedzi i wskazuje podstawę ADR. |
| ADR-B-0540 | PASS redakcyjny | Wyjaśnienie podaje sens, odnosi się do błędnych odpowiedzi i wskazuje podstawę ADR. |
| ADR-B-0558 | PASS redakcyjny | Wyjaśnienie podaje sens, odnosi się do błędnych odpowiedzi i wskazuje podstawę ADR. |
| ADR-B-0559 | PASS redakcyjny | Wyjaśnienie podaje sens, odnosi się do błędnych odpowiedzi i wskazuje podstawę ADR. |
| ADR-B-0574 | PASS redakcyjny | Wyjaśnienie podaje sens, odnosi się do błędnych odpowiedzi i wskazuje podstawę ADR. |
| ADR-B-0600 | PASS redakcyjny | Wyjaśnienie podaje sens, odnosi się do błędnych odpowiedzi i wskazuje podstawę ADR. |
| ADR-B-0609 | PASS redakcyjny | Wyjaśnienie podaje sens, odnosi się do błędnych odpowiedzi i wskazuje podstawę ADR. |

## 3. Zgodność materiałów

- Bank: 609 unikalnych ID, brak zmiany liczby pytań.
- Egzaminy próbne 001–005: poprawne litery bez zmian; pole `source_bank_head` zaktualizowano do aktualnego blobu banku.
- Migawki audytu prawnego i sekwencyjnego dla siedmiu odzyskanych ID zsynchronizowano z nowym brzmieniem pytań i explanation.
- Przegląd nie nadaje statusu `verified`; pełne porównanie polskiego tekstu urzędowego i zatwierdzenie specjalisty pozostają wymagane.

## 4. Wynik i ograniczenia

- Poprawki przeniesione z zamkniętego PR #579: 7 pytań; poprawne litery bez zmian.
- Nowe zmiany w próbce 4x119: 0, ponieważ wszystkie 40 wyjaśnień spełniło kryteria redakcyjne.
- Statusy banku: 609 `needs_review`, 0 `verified`.
- Metryki: 11,82% globalnie; maksimum działu 14,29%; minimum explanation 300 znaków.
- Próba rozłączna z 4x114–4x118 i siedmioma odzyskanymi ID; wykluczono 179 unikalnych ID, pula liczy 430. Nie deklaruje się rozłączności z każdą wcześniejszą próbą 4x103–4x113.
