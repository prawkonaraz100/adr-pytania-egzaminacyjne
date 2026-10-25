# Etap 4u — wariant 003 egzaminu próbnego

- Świeży main: `5a123d05075bbdb8d4739033de222155e0913b4a`; 569 pytań kursu podstawowego.
- Dobór deterministyczny: `seed=2026102505`, ten sam algorytm kwot i LCG co `scripts/draft_mock_exam.py`, z wykluczeniem unii ID z arkuszy 001 i 002.
- 30 unikalnych pytań z 13 działów, bez powtórzeń z poprzednich arkuszy. Nowe pytania w arkuszu: ADR-B-0566, ADR-B-0560.
- Czas treningu: 60 min; próg: 20/30 (2/3). Nie jest to urzędowy egzamin ani materiał zatwierdzony do publikacji.

## Rozkład działów

| Dział | Liczba |
|---|---:|
| ADR-B-01 | 2 |
| ADR-B-02 | 3 |
| ADR-B-03 | 3 |
| ADR-B-04 | 2 |
| ADR-B-05 | 2 |
| ADR-B-06 | 3 |
| ADR-B-07 | 2 |
| ADR-B-08 | 2 |
| ADR-B-09 | 2 |
| ADR-B-10 | 3 |
| ADR-B-11 | 2 |
| ADR-B-12 | 2 |
| ADR-B-13 | 2 |

## Rozkład kluczy

| A | B | C | Razem |
|---:|---:|---:|---:|
| 10 | 13 | 7 | 30 |

Kontrola: wszystkie 30 ID istnieją w banku; 0 powtórek wewnątrz arkusza i 0 wspólnych ID z 001/002; wszystkie rekordy `needs_review`. Dopiero PASS pełnego Quality Gate pozwala scalić PR.
