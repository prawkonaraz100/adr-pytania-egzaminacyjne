# Kontrola druga – partia 45 (ADR-B-0661–0675)

Main 8244275df (po scaleniu #921), bank blob `835ba93341ece797cd831d85defa4d147da0942e`. Źródło: Dz.U. 2025 poz. 642 (+ sprostowanie poz. 1575); strony według nagłówka „Dziennik Ustaw — NNN —”. Nic nie oznaczono jako verified.

**Wynik: OK 0 / POPRAW 15 / BLOKUJ 0.** Pięć nowych elementów z tej samej kompetencji (0663, 0666, 0672, 0674, 0675), dziesięć przeredagowań z zachowaniem tematu (0661, 0662, 0664, 0665, 0667, 0668, 0669, 0670, 0671, 0673). Bez cystern; litery kluczy, moduły i kompetencje bez zmian; liczba pytań 780 bez zmian.

**Pozostało pytań bez porównania dosłownego: 105** (0676–0780).

| ID | Kompetencja | Klucz | Decyzja |
|---|---|---|---|
| 0661 | 02-K04 | B | Przeredagowanie: DPPL, próg TSP 50 °C |
| 0662 | 08-K08 | B | Przeredagowanie: niezgodność VIN w polu 3 świadectwa |
| 0663 | 07-K06 | C | Nowy element: wyjątek 1.1.3.6.2 wobec 8.3.1 |
| 0664 | 07-K06 | B | Przeredagowanie: zachowanie połączenia elektrycznego ABS |
| 0665 | 02-K05 | B | Przeredagowanie: materiał piroforyczny a samonagrzewający |
| 0666 | 02-K07 | A | Nowy element: oczyszczenie skrzyni przed załadunkiem |
| 0667 | 02-K08 | A | Przeredagowanie: postępowanie awaryjne przy temperaturze awaryjnej |
| 0668 | 02-K10 | A | Przeredagowanie: zakres zastosowania instrukcji P650 |
| 0669 | 02-K11 | B | Przeredagowanie: kategoria III-ŻÓŁTA i moc dawki |
| 0670 | 02-K09 | B | Przeredagowanie: rozsypany proszek klasy 6.1 |
| 0671 | 02-K02 | B | Przeredagowanie: ochrona zaworu ramą |
| 0672 | 13-K05 | B | Nowy element: dokument przewozowy zamiast instrukcji pisemnych |
| 0673 | 02-K13 | B | Przeredagowanie: UN 3481 – bateria zapakowana z urządzeniem |
| 0674 | 02-K06 | B | Nowy element: ochrona bębnów przed kontaktem z wodą |
| 0675 | 02-K06 | A | Nowy element: warunek V1 dla pojazdu |

## Uwagi z kontroli drugiej

- Poprzedni raport #921 miał zamienniki dublujące pytania 0352 i 0599; kryteria laboratoryjne w 0666/0670; wadliwe lub niejednoznaczne dystraktory w 0661, 0667, 0669, 0674 i 0675.
- Instrukcja P650 rozpoczyna się na stronie Dz.U. 819 (nie 820).
- 7.1.7.3.4 definiuje temperaturę kontrolowaną i awaryjną (s. 1285); obowiązek rozpoczęcia postępowania awaryjnego wynika z 7.1.7.4.3 (s. 1286).
- Wskaźnik „poprawna = jedyna najdłuższa”: 21/780 = 2,69%, maksimum działu 5,66%. „Poprawna = jedyna najkrótsza”: 88/780, każdy dział ≤ 38%.
- similarity.py: cały bank – przy 0,45: 7 par; przy 0,25: 158 par. Po poprawkach partia nie wnosi nowych par ponad próg 0,45; para 0675/0676 ma podobieństwo 0,325.
- W kopii kontrolnej wszystkie 14 skryptów CI przechodziło, unittest 248/248.

Szczegółowe cytaty ADR, treści pytań i odpowiedzi oraz uzasadnienia A/B/C są zachowane w niezależnym raporcie kontroli drugiej dostarczonym dla tej partii. Wszystkie rekordy pozostają `needs_review`; brak zatwierdzeń eksperckich.
