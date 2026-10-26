# Następna luka jakościowa — blokujący odbiór dydaktyczny scenariuszy

- Data: 2026-10-26.
- Punkt bazowy: świeży `main` `b58a7a00c824f5eaa1d912ebaf03dd8f537c4853` po zakończeniu etapu 4x48.
- Zakres: tylko kurs podstawowy ADR.

## Uzasadnienie

Po uporządkowaniu liczby pytań w scenariuszach kolejną luką była ochrona ich wartości dydaktycznej przed przyszłym uproszczeniem do samej sytuacji i listy czynności. Dodano blokujący test, który wymaga dla każdego scenariusza sytuacji, co najmniej trzech konkretnych kroków, obserwowalnych kryteriów oceny, krótkiego wniosku dla kursanta, podstawy ADR i co najmniej dwóch typowych błędów. Gdy błędy są zapisane w formie obiektów `common_errors`, test wymaga też pola `why` z wyjaśnieniem, dlaczego dany błąd jest błędem.

## Wynik preflight na obecnych danych

- Scenariusze: 39; liczba brakujących wymaganych pól: 0.
- Scenariusze z mniej niż trzema krokami: 0.
- Scenariusze z mniej niż dwoma opisanymi błędami kursanta: 0.
- Pytania w banku: 609; wszystkie `needs_review`, 0 `verified`.
- Nie zmieniano banku, kluczy ani scenariuszy — ta partia utrwala kontrolę regresji.

## Ograniczenia

Lokalnych testów repozytorium nie można uruchomić przez GitHub Contents API. Wymagany jest pełny Quality Gate CI. Ten test sprawdza kompletność i strukturę dydaktyczną; nie orzeka o prawnej poprawności treści ADR.
