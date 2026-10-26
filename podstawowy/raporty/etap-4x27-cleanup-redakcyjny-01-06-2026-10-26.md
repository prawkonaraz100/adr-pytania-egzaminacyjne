# Etap 4x27 — sprzątanie redakcyjne B-01–06

- Punkt wyjścia: świeży `main` po PR #464, commit `3c4b3c473fe1151c9a505c40341569e381de0473`.
- Cel: usunąć powtarzające się odsyłacze do jednego scenariusza i wyeliminować etykiety etapów/statusy „szkic” z materiałów instruktora.

## Zmiany

| Plik | Zmiana |
|---|---|
| Lekcje B-01–04 | Usunięto pojedynczą linię „Scenariusz z pracy kierowcy” — na końcu każdej lekcji pozostaje pełna lista wszystkich trzech scenariuszy. |
| Lekcje B-05–06 | Jak wyżej; nie usunięto żadnego z trzech identyfikatorów scenariuszy. |
| Instruktor B-01–02 | Zmieniono nagłówek „Synchronizacja … — etap 4x26” na neutralny „Prowadzenie zajęć: lekcja i scenariusze”. |
| Instruktor B-03–06 | Jak wyżej; ponadto zastąpiono etykiety „szkic do niezależnej recenzji” neutralną informacją, że materiał wymaga niezależnej recenzji. |

## Zachowanie materiału

- Nie zmieniono pytań, odpowiedzi, wyjaśnień, podstaw ADR ani statusów w banku.
- Nie usunięto treści scenariuszy; wyłącznie usunięto redundantny odsyłacz do jednego scenariusza, który sugerował niepełną ścieżkę nauki.
- Pełne trzy scenariusze na dział pozostają wymienione na końcu lekcji i w mapie JSON.
- Wszystkie pytania nadal `needs_review`; nie nadano statusu `verified`.

## Testy

Wymagany PASS Quality Gate CI na PR. Testy lokalne nie zostały uruchomione w środowisku GitHub.
