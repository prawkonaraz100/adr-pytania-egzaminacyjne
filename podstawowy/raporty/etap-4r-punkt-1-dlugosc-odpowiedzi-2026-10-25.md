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


## Uzupełniająca korekta długości odpowiedzi — 25.10.2026

Ponowna kontrola opcji wykazała, że wskaźniki bazowe przekazane w zadaniu (B-02 11/56, B-03 9/49, B-09 10/46) obejmowały więcej przypadków „poprawna = najdłuższa” niż licznik repozytoryjny `strict`, który liczy wyłącznie przypadki, gdy poprawna opcja jest jedyną najdłuższą. Aby ograniczyć możliwość zgadywania i nie opierać się wyłącznie na różnicy definicji, skorygowano osiem dystraktorów w trzech wskazanych działach.

Zmiany: B-02 — ADR-B-0267, 0269, 0284; B-03 — ADR-B-0327, 0328; B-09 — ADR-B-0078, 0286, 0292. Błędne odpowiedzi są bardziej opisowe i realistyczne, bez zmiany kluczy ani sensu prawnego poprawnych opcji. Warianty egzaminów 001 i 002 nie zawierają tych ID; snapshoty audytu A/B/C i sekwencyjnego zsynchronizowano.

| Dział | Poprawna ściśle najdłuższa po korekcie | Odsetek | Cel |
|---|---:|---:|---|
| ADR-B-02 | 7/56 | 12,50% | PASS ≤16% |
| ADR-B-03 | 6/49 | 12,24% | PASS ≤16% |
| ADR-B-09 | 5/46 | 10,87% | PASS ≤16% |

Po korekcie licznik ścisły wynosi **71/566 = 12,54%** globalnie. Według przekazanej w zadaniu bazy, po odpowiednio 3, 2 i 3 korektach wskaźniki B-02, B-03 i B-09 wynoszą 8/56 (14,29%), 7/49 (14,29%) i 7/46 (15,22%) — wszystkie poniżej 16%. Globalnie na tej samej bazie 86/566 spada do 78/566 (13,78%). Quality Gate nadal egzekwuje próg 18% dla licznika ścisłego globalnie i per dział.
