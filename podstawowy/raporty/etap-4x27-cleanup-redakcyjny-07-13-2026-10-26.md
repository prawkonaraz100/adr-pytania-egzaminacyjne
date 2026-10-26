# Etap 4x27 — sprzątanie redakcyjne B-07–13

- Punkt wyjścia: świeży `main` po PR #465, commit `710ad6b901f266783ed379682c2e73ad3b91373c`.
- Cel: usunąć redundantne pojedyncze odsyłacze do scenariusza z lekcji B-07–13 i ujednolicić nagłówki materiałów instruktora.

## Zmiany

| Pliki | Zmiana |
|---|---|
| Lekcje B-07–13 | Usunięto pojedynczą linię „Scenariusz z pracy kierowcy”; na końcu każdej lekcji nadal znajduje się komplet trzech scenariuszy. |
| Instruktor B-07–13 | Nagłówek „Synchronizacja z lekcją i scenariuszami — etap 4x26” zastąpiono neutralnym „Prowadzenie zajęć: lekcja i scenariusze”. |

## Zachowanie materiału

- Nie usunięto żadnego z trzech scenariuszy w żadnym dziale.
- Nie zmieniano banku, odpowiedzi, wyjaśnień, podstaw ADR ani statusów.
- Pełna ścieżka kursanta pozostaje: lekcja → pytania z wyjaśnieniami → trzy scenariusze → egzaminy próbne 001–005.
- Wszystkie pytania nadal mają status `needs_review`; nie nadano statusu `verified`.

## Testy

Wymagany PASS Quality Gate CI na PR. Testy lokalne nie zostały uruchomione w środowisku GitHub.
