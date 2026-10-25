# Etap 4v — partia 1b: kolejne 26 pytań z wyciekiem słów absolutnych

Punkt wyjścia: świeży `main` `5de172693006009d5bc06e58c9dc8bdda80ba221` po pierwszej podpartii (#285). Pytania: ADR-B-0036, ADR-B-0037, ADR-B-0040, ADR-B-0041, ADR-B-0044, ADR-B-0046, ADR-B-0050, ADR-B-0051, ADR-B-0057, ADR-B-0060, ADR-B-0062, ADR-B-0064, ADR-B-0065, ADR-B-0066, ADR-B-0068, ADR-B-0069, ADR-B-0070, ADR-B-0075, ADR-B-0076, ADR-B-0077, ADR-B-0082, ADR-B-0083, ADR-B-0084, ADR-B-0085, ADR-B-0090, ADR-B-0091.

Usunięto zbędne słowa absolutne z błędnych wariantów, zastępując je konkretnymi, nadal niepoprawnymi interpretacjami zasad dla kierowcy. Nie zmieniono kluczy odpowiedzi, treści poprawnych opcji ani statusu `needs_review`. Wyjaśnienia zachowano tam, gdzie nadal bezpośrednio odnoszą się do błędnego założenia; nie dokonywano recenzji prawnej oznaczającej `verified`. Odświeżono migawki audytu sekwencyjnego i klauzulowego oraz arkusze egzaminów próbnych zawierające te pytania.

| Metryka | Przed | Po |
|---|---:|---:|
| Ściśle najkrótsza poprawna | 256/569 (44.99%) | 256/569 (44.99%) |
| Ściśle najdłuższa poprawna | 70/569 | 70/569 |
| Słowa absolutne w dystraktorach | 355/1138 | 319/1138 |
| Słowa absolutne w poprawnych | 26/569 | 26/569 |
| Luka występowania słów absolutnych | 26.63 p.p. | 23.46 p.p. |
| Pytania z absolutnym słowem wyłącznie w dystraktorach | 253 | 227 |

W każdym dziale sprawdzono dotychczasowy limit 18% ściśle najdłuższej poprawnej; po korektach najdłuższa nie przekracza progu. Metryki krótszej i słów absolutnych są nadal **raportowe**, nie blokujące.

Quality Gate: wynik CI dla PR wymagany przed scaleniem. Następnie kolejna partia według świeżego `main`.
