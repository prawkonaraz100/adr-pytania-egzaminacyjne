# Etap 4x6 — spójność materiałów instruktora B-09–B-13

Punkt wyjścia: świeży `main` `7908571ebf313524ee37d3cc8882e6865a31b9c7`. Zakres: kurs podstawowy ADR.

## Zmiany

Materiały instruktora B-09–B-13 uzupełniono o sposób prowadzenia wszystkich trzech scenariuszy, opis sytuacji, kroki, kryteria oceny, typowe błędy z prostym wyjaśnieniem, granice bezpieczeństwa, pytania kontrolne oraz pytania do dodatkowego omówienia. Zestawiono ID kompetencji i podstawy ADR z mapą `podstawowy/kompetencje.json`.

| Dział | Scenariusze | Kompetencje z mapy | Liczba unikalnych pytań w scenariuszach | Kontrola ID |
|---|---|---|---:|---|
| ADR-B-09 | SC-ADR-B-09, SC-ADR-B-09-02, SC-ADR-B-09-03 | ADR-B-09-K01, ADR-B-09-K02, ADR-B-09-K03, ADR-B-09-K04, ADR-B-09-K05, ADR-B-09-K06, ADR-B-09-K07, ADR-B-09-K08, ADR-B-09-K09 | 6 | PASS |
| ADR-B-10 | SC-ADR-B-10, SC-ADR-B-10-02, SC-ADR-B-10-03 | ADR-B-10-K01, ADR-B-10-K02, ADR-B-10-K03, ADR-B-10-K04, ADR-B-10-K05 | 5 | PASS |
| ADR-B-11 | SC-ADR-B-11, SC-ADR-B-11-02, SC-ADR-B-11-03 | ADR-B-11-K01, ADR-B-11-K02, ADR-B-11-K03, ADR-B-11-K04, ADR-B-11-K05, ADR-B-11-K06, ADR-B-11-K07 | 14 | PASS |
| ADR-B-12 | SC-ADR-B-12, SC-ADR-B-12-02, SC-ADR-B-12-03 | ADR-B-12-K01, ADR-B-12-K02, ADR-B-12-K03, ADR-B-12-K04, ADR-B-12-K05, ADR-B-12-K06 | 7 | PASS |
| ADR-B-13 | SC-ADR-B-13, SC-ADR-B-13-02, SC-ADR-B-13-03 | ADR-B-13-K01, ADR-B-13-K02, ADR-B-13-K03, ADR-B-13-K04, ADR-B-13-K05, ADR-B-13-K06, ADR-B-13-K07, ADR-B-13-K08 | 18 | PASS |

## Uwagi

- Brak telemetrii wyników kursantów; kandydaci do dodatkowego omówienia nie są przedstawiani jako ranking empiryczny.
- Nie znaleziono potwierdzonej rozbieżności, która uzasadniałaby zmianę pytania lub przepisu. Nie zmieniono banku.
- Bank: 609 pytań, 609 `needs_review`, 0 `verified`.
- Testy lokalne nie zostały uruchomione, ponieważ nie ma lokalnego checkoutu repo w tym środowisku; wymagany jest pełny CI Quality Gate przed scaleniem.
- Materiały nie zastępują niezależnej recenzji prawnej i odbioru instruktorskiego.
