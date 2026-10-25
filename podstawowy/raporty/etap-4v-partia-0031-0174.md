# Etap 4v — partia 2: korekta 40 pytań ADR-B-0031–0174

**Punkt odniesienia:** świeży `main` `0dbd5c9ebea9ac8a1c9cb541bae5eb101d3c5df6` po scaleniu PR #286. Zakres: ADR-B-0031, ADR-B-0033, ADR-B-0059, ADR-B-0085, ADR-B-0093, ADR-B-0102, ADR-B-0105, ADR-B-0114, ADR-B-0119, ADR-B-0122, ADR-B-0123, ADR-B-0126, ADR-B-0129, ADR-B-0132, ADR-B-0133, ADR-B-0134, ADR-B-0136, ADR-B-0140, ADR-B-0142, ADR-B-0144, ADR-B-0145, ADR-B-0146, ADR-B-0147, ADR-B-0148, ADR-B-0149, ADR-B-0151, ADR-B-0153, ADR-B-0154, ADR-B-0155, ADR-B-0156, ADR-B-0157, ADR-B-0158, ADR-B-0159, ADR-B-0160, ADR-B-0161, ADR-B-0162, ADR-B-0165, ADR-B-0170, ADR-B-0173, ADR-B-0174. Wybrano kolejno 40 rekordów z wyrazami absolutnymi występującymi w odpowiedziach błędnych, lecz nie w poprawnej, według kolejności ID na świeżym `main`.

## Metoda

Zmieniono wyłącznie warianty odpowiedzi A/B/C: zamiast słów podpowiadających odpowiedź użyto konkretnych, nieprawidłowych, ale wiarygodnych interpretacji przepisów lub czynności kierowcy. Poprawne warianty doprecyzowano tylko co do zakresu już opisanego w pytaniu. Nie zmieniono kluczy, statusów `needs_review`, `explanation`, ID, podstaw prawnych ani ocen prawnych. Każde stare `explanation` zostało pozostawione, ponieważ nadal opisuje te same błędne rozumowania; nie jest to ponowna aprobata prawna. Zsynchronizowano migawki audytu sekwencyjnego i prawnego oraz arkusze próbne zawierające poprawione opcje. Status sprawdzenia z urzędowym polskim tekstem ADR 2025 i przez specjalistę pozostaje otwarty.

## Metryki przed i po

W tabeli kolejno: *najkrótsza poprawna*, *najdłuższa poprawna*, *absoluty w dystraktorach*, *absoluty w poprawnych* oraz *pytania z absolutem wyłącznie w dystraktorach*. Długość liczona po `trim()`, „najkrótsza/najdłuższa” tylko przy ścisłym porównaniu bez remisów. Absoluty zgodnie z `scripts/answer_leakage_metrics.py`; mianownik dla dystraktorów = 2 × liczba pytań.

| Dział | Przed: najkrótsza | Po: najkrótsza | Przed: najdłuższa | Po: najdłuższa | Absoluty błędne przed→po | Absoluty poprawne przed→po | Tylko błędne przed→po |
|---|---:|---:|---:|---:|---:|---:|---:|
| GLOBAL | 44.99% (256/569) | 41.30% (235/569) | 12.30% (70/569) | 14.24% (81/569) | 28.03% → 24.52% (319→279) | 4.57% → 4.57% (26→26) | 227→197 |
| ADR-B-01 | 42.86% (15/35) | 37.14% (13/35) | 14.29% (5/35) | 17.14% (6/35) | 28.57% → 21.43% (20→15) | 5.71% → 5.71% (2→2) | 15→12 |
| ADR-B-02 | 35.71% (20/56) | 23.21% (13/56) | 12.50% (7/56) | 16.07% (9/56) | 35.71% → 21.43% (40→24) | 1.79% → 1.79% (1→1) | 27→15 |
| ADR-B-03 | 40.82% (20/49) | 40.82% (20/49) | 12.24% (6/49) | 14.29% (7/49) | 35.71% → 35.71% (35→35) | 10.20% → 10.20% (5→5) | 23→23 |
| ADR-B-04 | 36.36% (16/44) | 36.36% (16/44) | 13.64% (6/44) | 15.91% (7/44) | 23.86% → 23.86% (21→21) | 0.00% → 0.00% (0→0) | 19→19 |
| ADR-B-05 | 25.00% (10/40) | 20.00% (8/40) | 15.00% (6/40) | 15.00% (6/40) | 16.25% → 12.50% (13→10) | 10.00% → 10.00% (4→4) | 7→5 |
| ADR-B-06 | 60.00% (27/45) | 53.33% (24/45) | 8.89% (4/45) | 13.33% (6/45) | 27.78% → 22.22% (25→20) | 0.00% → 0.00% (0→0) | 20→16 |
| ADR-B-07 | 67.39% (31/46) | 65.22% (30/46) | 6.52% (3/46) | 10.87% (5/46) | 25.00% → 22.83% (23→21) | 0.00% → 0.00% (0→0) | 19→17 |
| ADR-B-09 | 47.83% (22/46) | 45.65% (21/46) | 8.70% (4/46) | 10.87% (5/46) | 17.39% → 16.30% (16→15) | 2.17% → 2.17% (1→1) | 13→12 |
| ADR-B-10 | 50.91% (28/55) | 47.27% (26/55) | 7.27% (4/55) | 7.27% (4/55) | 40.00% → 36.36% (44→40) | 7.27% → 7.27% (4→4) | 28→26 |
| ADR-B-11 | 37.14% (13/35) | 34.29% (12/35) | 17.14% (6/35) | 17.14% (6/35) | 25.71% → 25.71% (18→18) | 0.00% → 0.00% (0→0) | 12→12 |
| ADR-B-12 | 51.16% (22/43) | 48.84% (21/43) | 13.95% (6/43) | 16.28% (7/43) | 27.91% → 25.58% (24→22) | 11.63% → 11.63% (5→5) | 15→13 |
| ADR-B-13 | 34.29% (12/35) | 31.43% (11/35) | 17.14% (6/35) | 17.14% (6/35) | 22.86% → 20.00% (16→14) | 2.86% → 2.86% (1→1) | 14→12 |

## Wynik i dalsze ryzyka

- Globalna ściśle najkrótsza poprawna: 256→235 na 569 pytań; nadal ponad celem 38%. Nie przedstawiamy tej partii jako ukończenia celu globalnego.
- Globalna ściśle najdłuższa poprawna: 70→81 na 569 pytań. Po partii wszystkie działy pozostają ≤18% dla tej metryki.
- Absoluty w dystraktorach 319→279, przy 26 w poprawnych; pytania z wyciekiem wyłącznie w dystraktorach 227→197.
- W skorygowanych 40 pytaniach nie pozostał wyraz absolutny wyłącznie w dystraktorze według reguły skryptu. Nadal wymagany jest osobny redakcyjny przegląd potencjalnego zgadywania z długości w działach 06, 07, 08, 10 i 12.
- **Quality Gate:** wymagany PASS obu końcowych przebiegów przed scaleniem; wynik zostanie zapisany w Issue #10. Raport ma charakter redakcyjny, nie zatwierdza prawa ADR.
