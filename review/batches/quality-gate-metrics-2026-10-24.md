# Kontrola wskaźnika długości odpowiedzi i wyjaśnień — 24.10.2026

## Zakres 4m: ADR-B-0226–0240
Zakres jest objęty wyrównaniem w scalonym [PR #237](../../pull/237), z raportem [stage4m-balance-0226-0240.md](stage4m-balance-0226-0240.md). Nie tworzono duplikatu.

## Wskaźnik na świeżym main
Bank: 545 pytań. Liczę wyłącznie przypadki, gdy poprawna odpowiedź jest **jedyną ściśle najdłuższą**; remisy nie są liczone jako trafienie.

- Globalnie: **90/545 = 16,51%** (cel ≤40% spełniony).
- Poprawna odpowiedź jest najdłuższa z remisem włącznie w 110/545 = 20,18%; z tego 20 pytań to remisy.
- Wskaźnik ścisły według działu:

| Dział | Ściśle najdłuższa / wszystkie | Wynik |
|---|---:|---:|
| ADR-B-01 | 6/35 | 17,14% |
| ADR-B-02 | 12/56 | 21,43% |
| ADR-B-03 | 10/49 | 20,41% |
| ADR-B-04 | 5/44 | 11,36% |
| ADR-B-05 | 6/40 | 15,00% |
| ADR-B-06 | 4/35 | 11,43% |
| ADR-B-07 | 3/43 | 6,98% |
| ADR-B-08 | 8/36 | 22,22% |
| ADR-B-09 | 10/39 | 25,64% |
| ADR-B-10 | 4/55 | 7,27% |
| ADR-B-11 | 9/35 | 25,71% |
| ADR-B-12 | 6/43 | 13,95% |
| ADR-B-13 | 7/35 | 20,00% |

Wszystkie działy pozostają poniżej celu 40%. Najwyższy wskaźnik ma ADR-B-11: 25,71%, następnie ADR-B-09: 25,64%.

## Kontrola explanation
Na świeżym main wszystkie 545 wyjaśnień mają co najmniej 200 znaków (minimum 248), a kontrola mechaniczna nie wykryła wyjaśnień jednozdaniowych. To nie potwierdza sama w sobie, że tekst jest naturalny i dydaktyczny. Pełny przegląd jakości języka pod kątem suchych parafraz przepisów pozostaje osobnym zadaniem.

## Zaostrzenie Quality Gate
Proponowany próg globalny: **18%** (obecny wynik 16,51%, niewielki margines). Dodatkowa kontrola wymaga minimum 200 znaków w każdym explanation. Kontrole nie zmieniają statusu needs_review i nie zastępują recenzji prawnej.
