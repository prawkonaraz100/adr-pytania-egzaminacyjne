# Etap 4m — partia 4: wyrównanie długości ADR-B-06

Data 23.10.2026. **Fresh main:** 545 pytań (0001–0545), 545 needs_review, 0 verified, brak otwartych PR. Moduł ADR-B-06 liczy 35 pytań po PR #160.

## Wynik pomiaru

| Zakres | Przed | Po |
|---|---:|---:|
| Cały bank | 370/545 (67.9%) | 365/545 (67.0%) |
| ADR-B-06 | 19/35 (54.3%) | 14/35 (40.0%) |

**ADR-B-06 osiągnął lokalny próg 40%.** Nie oznacza to spełnienia celu globalnego ani 12 innych działów. Wskaźnik liczy wyłącznie ściśle najdłuższą poprawną odpowiedź, bez remisów.

## Poprawione rekordy

- `ADR-B-0503`: korekta wyłącznie długości i stylistyki istniejących wariantów A/B/C, bez zmiany klucza, numeracji lub źródeł ADR.
- `ADR-B-0504`: korekta wyłącznie długości i stylistyki istniejących wariantów A/B/C, bez zmiany klucza, numeracji lub źródeł ADR.
- `ADR-B-0507`: korekta wyłącznie długości i stylistyki istniejących wariantów A/B/C, bez zmiany klucza, numeracji lub źródeł ADR.
- `ADR-B-0543`: korekta wyłącznie długości i stylistyki istniejących wariantów A/B/C, bez zmiany klucza, numeracji lub źródeł ADR.
- `ADR-B-0544`: korekta wyłącznie długości i stylistyki istniejących wariantów A/B/C, bez zmiany klucza, numeracji lub źródeł ADR.

Każdą zmianę zsynchronizowano z istniejącą migawką w `review/sequential/503-506.json`, `507-509.json`, `543-545.json` oraz odpowiadającą oceną w `review/legal-clauses/`. Brak statusów verified. Źródła wskazane w rekordach (m.in. ADR 2025 5.3.2.3.1) nadal wymagają niezależnego dosłownego porównania z oficjalnym polskim Dz.U. 2025 poz. 642 i sprostowaniem 1575.

**Nie publikować**. Techniczny PASS CI sprawdza spójność danych, nie legalne zatwierdzenie A/B/C. Kolejne moduły ponad progiem muszą być poprawiane osobno.
