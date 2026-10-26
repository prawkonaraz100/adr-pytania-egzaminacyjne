# Etap 4x20 — ręczny audyt explanation ADR-B-0401–0450

- Punkt wyjścia: świeży `main` po PR #388, commit `0d08cc2899ee78f689523cfd829ddf083a1b584d`.
- Zakres: wszystkie 50 pytań ADR-B-0401–ADR-B-0450.
- Metoda: skryptowe wskazanie skrótów i potencjalnie trudnych sformułowań oraz ręczny przegląd pod kątem zrozumiałości dla początkującego kursanta.

## Wynik

Ręcznie sprawdzono 50/50 wyjaśnień. Poprawiono 2 potwierdzone braki objaśnienia:

| ID | Zmiana |
|---|---|
| ADR-B-0417 | Rozwinięto DMC jako „dopuszczalna masa całkowita pojazdu”; wyjaśniono, że liczba gaśnic i łączna pojemność to osobne wymagania. |
| ADR-B-0434 | Rozwinięto numer UN jako czterocyfrowy identyfikator towaru niebezpiecznego i zachowano rozróżnienie kolumn tabeli A. |

Pozostałe 48 wyjaśnień pozostawiono bez zmian; przykładowo ADR-B-0418–0420 już rozwijają skrót DMC, a pozostałe wyjaśnienia wystarczająco jasno wskazują, dlaczego błędne warianty nie spełniają wymogu. Nie zmieniono pytań, opcji, poprawnych liter, modułów ani statusów. Wszystkie rekordy pozostają `needs_review`.

## Lista sprawdzonych ID

ADR-B-0401, ADR-B-0402, ADR-B-0403, ADR-B-0404, ADR-B-0405, ADR-B-0406, ADR-B-0407, ADR-B-0408, ADR-B-0409, ADR-B-0410, ADR-B-0411, ADR-B-0412, ADR-B-0413, ADR-B-0414, ADR-B-0415, ADR-B-0416, ADR-B-0417, ADR-B-0418, ADR-B-0419, ADR-B-0420, ADR-B-0421, ADR-B-0422, ADR-B-0423, ADR-B-0424, ADR-B-0425, ADR-B-0426, ADR-B-0427, ADR-B-0428, ADR-B-0429, ADR-B-0430, ADR-B-0431, ADR-B-0432, ADR-B-0433, ADR-B-0434, ADR-B-0435, ADR-B-0436, ADR-B-0437, ADR-B-0438, ADR-B-0439, ADR-B-0440, ADR-B-0441, ADR-B-0442, ADR-B-0443, ADR-B-0444, ADR-B-0445, ADR-B-0446, ADR-B-0447, ADR-B-0448, ADR-B-0449, ADR-B-0450

## Kontrola wskaźników

- Bank: 609 pytań; duplikaty ID: 0.
- Explanation poniżej 200 znaków: 0; najkrótsze: 300 znaków.
- Zmienione explanation: 358 i 411 znaków.
- Poprawna odpowiedź jako jedyna najdłuższa: 73/609 = 11.99%.
- Wskaźnik per dział:
  - ADR-B-01: 6/45 = 13.33%
  - ADR-B-02: 8/56 = 14.29%
  - ADR-B-03: 7/49 = 14.29%
  - ADR-B-04: 6/46 = 13.04%
  - ADR-B-05: 6/43 = 13.95%
  - ADR-B-06: 5/45 = 11.11%
  - ADR-B-07: 6/48 = 12.5%
  - ADR-B-08: 5/42 = 11.9%
  - ADR-B-09: 4/46 = 8.7%
  - ADR-B-10: 4/55 = 7.27%
  - ADR-B-11: 6/43 = 13.95%
  - ADR-B-12: 6/44 = 13.64%
  - ADR-B-13: 4/47 = 8.51%

## Synchronizacja audytu i egzaminów

Zsynchronizowano snapshoty dla ADR-B-0417 i ADR-B-0434 w `review/sequential/417-436.json` i `review/legal-clauses/417-436.json`. Odświeżono `source_bank_head` w wariantach i kluczach egzaminów próbnych 001–005 oraz wyjaśnienia i klucze zgodnie z aktualnym bankiem. Warianty zachowują 30 pytań, wszystkie 13 działów, A/B/C = 10/10/10 i maksymalną serię tej samej litery równą 1.

## Ograniczenia

To przegląd redakcyjny, nie formalna akceptacja prawna. Żadnego pytania nie oznaczono jako `verified`.
