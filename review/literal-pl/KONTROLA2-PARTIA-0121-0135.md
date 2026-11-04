# Kontrola druga — partia 9 (ADR-B-0121–0135)

Źródło: ADR 2025, Dz.U. 2025 poz. 642, z uwzględnieniem sprostowania poz. 1575. Kontrola druga wykonana niezależnie przez recenzenta; rozstrzygnięto punkty sporne na obrazach oficjalnego PDF.

**Wynik: 4 OK, 11 POPRAW, 0 BLOKUJ.** Klucze wszystkich 15 pytań pozostają prawidłowe i nie ulegają zmianie. Każde pytanie zachowuje `needs_review`, bez autoryzacji specjalisty.

**OK:** ADR-B-0123, 0126, 0127, 0132.

**POPRAW:** ADR-B-0121, 0122, 0124, 0125, 0128, 0129, 0130, 0131, 0133, 0134, 0135. Pełne zatwierdzone rekordy: `POPRAWKI-KONTROLA2-0121-0135.jsonl`. Poprawki zapisano do `podstawowy/questions.jsonl` na gałęzi, bez zmian kluczy.

## Sporne odczyty i podstawy

- **0127:** obraz Dz.U. s. 119, ADR 2.1.1.3: „III grupa pakowania: materiały stwarzające małe zagrożenie.” Odczyt „[II” był błędem OCR; klucz B prawidłowy, werdykt OK.
- **0125, 0128:** obrazy Dz.U. s. 307–308, ADR 3.2.1, objaśnienia kolumn (1), (3a), (4) oraz nagłówek tabeli A s. 315 potwierdzają klucze C. W obu przypadkach poprawiono oczywiste podpowiedzi w opcjach.
- **0124:** poprawiona podstawa na ADR 2.1.2.1 i 3.2.1, zamiast 2.1.1.
- **0131:** poprawiono dystraktor oraz odniesienia do ADR 8.4.1, 8.5 i tabeli A kol. (19).

## Jakość i stan

Wskaźnik „poprawna = jedyna najdłuższa”: **81/780 = 10,38%**, maksimum działu **15,22%**. Licznik bez porównania dosłownego pozostaje **618/780** (ta partia została porównana w kontroli pierwszej). Żaden rekord nie jest `verified`; `checked_at` i `reviewer` pozostają null.

Kontrola druga nie jest równoznaczna z niezależnym dopuszczeniem banku do publikacji. Pełne odnośniki do podstaw i oceny pytań znajdują się w `PARTIA-0121-0135.json` oraz `PARTIA-0121-0135.md`.
