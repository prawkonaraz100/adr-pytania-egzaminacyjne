# Etap 4r, punkt 1 — kontrola długości poprawnych odpowiedzi

- Audyt wykonano na świeżym `main`: `4eab0123f59238067c8500ce4046bc1d830fd0cd`.
- Bank: 566 pytań; wszystkie statusy pozostają bez zmian.
- Wskaźnik oznacza wyłącznie przypadki, w których poprawna opcja jest **ściśle dłuższa** od każdej błędnej; remisy nie są liczone.
- Wynik globalny: **79/566 = 13.96%**, poniżej 18%.
- Wszystkie działy już spełniają próg 18%; nie zmieniano treści odpowiedzi bez potwierdzonej potrzeby.

## Wyniki per dział

| Dział | Przypadki | Odsetek | Limit 18% |
|---|---:|---:|---|
| ADR-B-01 | 6/35 | 17.14% | PASS |
| ADR-B-02 | 10/56 | 17.86% | PASS |
| ADR-B-03 | 8/49 | 16.33% | PASS |
| ADR-B-04 | 5/44 | 11.36% | PASS |
| ADR-B-05 | 6/40 | 15.00% | PASS |
| ADR-B-06 | 4/45 | 8.89% | PASS |
| ADR-B-07 | 3/43 | 6.98% | PASS |
| ADR-B-08 | 7/40 | 17.50% | PASS |
| ADR-B-09 | 8/46 | 17.39% | PASS |
| ADR-B-10 | 4/55 | 7.27% | PASS |
| ADR-B-11 | 6/35 | 17.14% | PASS |
| ADR-B-12 | 6/43 | 13.95% | PASS |
| ADR-B-13 | 6/35 | 17.14% | PASS |

## Decyzja

Wprowadzono do Quality Gate tryb `--strict`, który blokuje przekroczenie limitu zarówno globalnie, jak i w dowolnym dziale. Poprzednie `--strict-global` sprawdzało tylko wskaźnik globalny i mogło przepuścić pojedynczy dział ponad limitem. Dodano test regresyjny: zestaw testowy, w którym wskaźnik globalny mieści się w progu, lecz jeden dział go przekracza, musi przejść `--strict-global` i oblać `--strict`.

B-02 (17.86%) i B-09 (17.39%) są blisko progu, ale nie przekraczają go. Nie wydłużano sztucznie dystraktorów, bo nie ma tu naruszenia kryterium. Kontrola pozostaje automatyczna w kolejnych PR-ach.

Żadne pytanie nie zmieniło klucza, wyjaśnienia, podstawy prawnej ani `verification_status`; nie nadano statusu `verified`.
