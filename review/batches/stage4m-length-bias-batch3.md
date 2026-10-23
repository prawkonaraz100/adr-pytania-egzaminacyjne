# Etap 4m — partia 3: poprawki długości w ADR-B-03, 04 i 07

23.10.2026. Świeży `main` po PR #160: 545 pytań (ADR-B-0001–0545), wszystkie `needs_review`, 0 `verified`, brak otwartych PR. Zmodyfikowano wyłącznie słownictwo opcji w **13 istniejących pytaniach**, bez zmiany klucza A/B/C, identyfikatora, przepisu źródłowego, pytania lub wyjaśnienia. Wszystkie migawki i oceny wariantów z `review/sequential/461-470.json`, `471-476.json`, `477-482.json` oraz odpowiadających `review/legal-clauses/` zaktualizowano.

## Porównanie wskaźnika

Miara: poprawna odpowiedź ma jednoznacznie większą liczbę znaków (po `trim`) niż obie błędne. Remis nie jest liczony jako jednoznacznie najdłuższa odpowiedź.

| Zakres | Przed | Po |
|---|---:|---:|
| Cały bank | 383/545 (70.3%) | 370/545 (67.9%) |
| ADR-B-03 | 40/49 | 35/49 |
| ADR-B-04 | 36/44 | 32/44 |
| ADR-B-07 | 34/43 | 30/43 |

Poprawione ID: `ADR-B-0461`, `ADR-B-0462`, `ADR-B-0463`, `ADR-B-0467`, `ADR-B-0468`, `ADR-B-0472`, `ADR-B-0473`, `ADR-B-0475`, `ADR-B-0476`, `ADR-B-0477`, `ADR-B-0478`, `ADR-B-0479`, `ADR-B-0482`.

## Zasady poprawiania

Dystraktory pozostają wariantami niezgodnymi z opisanymi warunkami ADR, lecz zamiast jawnych absurdów przybliżają inne, na pozór możliwe interpretacje. Poprawne warianty skrócono tam, gdzie pozwalał na to zachowany kontekst pytania. Zmiany wymagają dodatkowej recenzji specjalisty ADR — sama poprawa proporcji długości nie oznacza poprawności prawnej.

**Próg ≤40% nie został osiągnięty**. Kontrola CI dodana w partii 1 pozostaje ostrzeżeniem, a nie aktywną blokadą. Nie rozpoczęto innych kursów ani cystern.
