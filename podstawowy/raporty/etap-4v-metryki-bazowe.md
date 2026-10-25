# Etap 4v — metryki bazowe (2026-10-25)

Punkt odniesienia: main `e58d12043ff9c2050ec20711c48e8676f3e9d74d`, 569 pytań kursu podstawowego.

Metryka liczy **ściśle najkrótszą** i **ściśle najdłuższą** poprawną odpowiedź; remisy nie są wliczane. Słowa absolutne: `zawsze, nigdy, wyłącznie, tylko, jedynie, każdy, żaden, całkowicie, niezależnie, bez względu`; wielkość liter ignorowana, dopasowanie całego słowa/frazy. Odsetki słów: 569 poprawnych wariantów oraz 1138 dystraktorów, czyli dla dystraktorów mianownikiem są *warianty*, nie pytania.

- Poprawna ściśle najkrótsza: **256/569 = 44,99%**.
- Poprawna ściśle najdłuższa: **71/569 = 12,48%**.
- Absolutne słowa w poprawnych: **26/569 = 4,57%**.
- Absolutne słowa w dystraktorach: **375/1138 = 32,95%**.
- Różnica: **+28,38 punktu procentowego** po stronie dystraktorów.
- Pytania z absolutnym słowem wyłącznie w błędnych wariantach: **267** dla powyższej definicji (inna liczba niż 287 z analizy użytkownika; zależy od tokenizacji/wyrażeń i wersji banku).

| Dział | Pytań | Poprawna najkrótsza | Poprawna najdłuższa | Słowo absolutne: poprawne/dystraktory | Tylko dystraktory |
|---|---:|---:|---:|---|---:|
| 01 | 35 | 15 | 6 | 2/28 | 20 |
| 02 | 56 | 20 | 7 | 1/43 | 29 |
| 03 | 49 | 20 | 6 | 5/36 | 24 |
| 04 | 44 | 16 | 5 | 0/23 | 21 |
| 05 | 40 | 10 | 6 | 4/17 | 10 |
| 06 | 45 | 27 | 4 | 0/26 | 21 |
| 07 | 46 | 31 | 3 | 0/24 | 20 |
| 08 | 40 | 20 | 7 | 3/30 | 19 |
| 09 | 46 | 22 | 5 | 1/22 | 17 |
| 10 | 55 | 28 | 4 | 4/49 | 31 |
| 11 | 35 | 13 | 6 | 0/26 | 19 |
| 12 | 43 | 22 | 6 | 5/27 | 17 |
| 13 | 35 | 12 | 6 | 1/24 | 19 |

Quality Gate: **tylko raportowanie** dwóch nowych sygnałów, bez nowego progu blokującego. Dotychczasowy limit 18% dla najdłuższej odpowiedzi pozostaje bez zmian. Następnie redakcja dystraktorów w małych partiach, połączona z aktualizacją adekwatnych wyjaśnień i migawek audytu.
