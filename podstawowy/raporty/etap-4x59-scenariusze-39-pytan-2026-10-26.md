# Etap 4x59 — przegląd 39 scenariuszy i pytania decyzyjne

Data: 26.10.2026. Bazowy main: `8b4a1429ca482225a9f0b68615924d798aec6e86`. Kurs: wyłącznie ADR podstawowy.

## Potwierdzony stan

- 39 scenariuszy, po trzy w każdym z 13 działów.
- Każdy ma konkretną sytuację, co najmniej cztery kroki działania kierowcy, typowe błędy, podsumowanie dlaczego, podstawę ADR, kryteria oceny i istniejące `question_ids` z właściwego działu.
- **Stwierdzony brak dydaktyczny:** nie było pytania do samodzielnego rozwiązania sytuacji; kursant mógł od razu czytać gotową listę kroków.
- Dodano 39 pól `learner_question`, każde dopasowane do odrębnej sytuacji. Nie zmieniano prawnych instrukcji ani odpowiedzi.
- Zmieniono instrukcję w `SCENARIUSZE.md`: sytuacja → własna decyzja na pytanie → porównanie kroków, błędów, uzasadnienia i pytań z banku.
- Dodano test blokujący obecność pytania, kroków, uzasadnienia, błędów i referencji do banku.

## Zakres 13 działów

| Dział | Scenariusze | Dodane pytania kursanta | Braki powiązań |
|---|---:|---:|---:|
| ADR-B-01 | 3 | 3 | 0 |
| ADR-B-02 | 3 | 3 | 0 |
| ADR-B-03 | 3 | 3 | 0 |
| ADR-B-04 | 3 | 3 | 0 |
| ADR-B-05 | 3 | 3 | 0 |
| ADR-B-06 | 3 | 3 | 0 |
| ADR-B-07 | 3 | 3 | 0 |
| ADR-B-08 | 3 | 3 | 0 |
| ADR-B-09 | 3 | 3 | 0 |
| ADR-B-10 | 3 | 3 | 0 |
| ADR-B-11 | 3 | 3 | 0 |
| ADR-B-12 | 3 | 3 | 0 |
| ADR-B-13 | 3 | 3 | 0 |

## Bezpieczeństwo i granice

Scenariusze są symulacjami; nie należy używać prawdziwych towarów niebezpiecznych. Podstawy ADR wskazane w rekordach pozostają przedmiotem niezależnej recenzji. Brak podstaw do dodania nowych pytań i zmiany klucza. Bank 609 pytań, 609 `needs_review`, 0 `verified`. Wskaźnik „poprawna = jedyna najdłuższa”: 72/609 = 11,82%; minimalne explanation: 300 znaków.
