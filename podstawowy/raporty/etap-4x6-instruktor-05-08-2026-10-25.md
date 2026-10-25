# Etap 4x6 — spójność materiałów instruktora B-05–B-08

Punkt wyjścia: świeży `main` `094d285a45e11e24c832d6fbcd89265f3c6de821`. Zakres: kurs podstawowy ADR.

## Zmiany

Materiały instruktora B-05–B-08 uzupełniono o prowadzenie wszystkich trzech scenariuszy z aktualnej mapy, sytuację, kroki, kryteria oceny, typowe błędy z prostym wyjaśnieniem, granice bezpieczeństwa, pytania kontrolne i wskazówki do dodatkowego omówienia.

| Dział | Scenariusze | Kompetencje z mapy | Liczba unikalnych pytań w scenariuszach | Kontrola ID |
|---|---|---|---:|---|
| ADR-B-05 | SC-ADR-B-05, SC-ADR-B-05-02, SC-ADR-B-05-03 | ADR-B-05-K01, ADR-B-05-K02, ADR-B-05-K03, ADR-B-05-K04, ADR-B-05-K05, ADR-B-05-K06, ADR-B-05-K07, ADR-B-05-K08, ADR-B-05-K09, ADR-B-05-K10, ADR-B-05-K11, ADR-B-05-K12, ADR-B-05-K13, ADR-B-05-K14, ADR-B-05-K15 | 9 | PASS |
| ADR-B-06 | SC-ADR-B-06, SC-ADR-B-06-02, SC-ADR-B-06-03 | ADR-B-06-K01, ADR-B-06-K02, ADR-B-06-K03, ADR-B-06-K04, ADR-B-06-K05, ADR-B-06-K06, ADR-B-06-K07, ADR-B-06-K08, ADR-B-06-K09 | 6 | PASS |
| ADR-B-07 | SC-ADR-B-07, SC-ADR-B-07-02, SC-ADR-B-07-03 | ADR-B-07-K01, ADR-B-07-K02, ADR-B-07-K03, ADR-B-07-K04, ADR-B-07-K05, ADR-B-07-K06, ADR-B-07-K07 | 9 | PASS |
| ADR-B-08 | SC-ADR-B-08, SC-ADR-B-08-02, SC-ADR-B-08-03 | ADR-B-08-K01, ADR-B-08-K02, ADR-B-08-K03, ADR-B-08-K04, ADR-B-08-K05, ADR-B-08-K06, ADR-B-08-K07, ADR-B-08-K08 | 8 | PASS |

## Ważne uwagi

- Wskazano ID do dodatkowego omówienia, ale nie nazywamy ich „najtrudniejszymi”: brak telemetrii wyników kursantów w repo.
- Zestawiono ID kompetencji i ich referencje ADR z `podstawowy/kompetencje.json`; bez źródłowego potwierdzenia nie zmieniano przepisów ani pytań.
- Bank: 609 pytań; 609 `needs_review`, 0 `verified`. Żadne pytanie ani status nie został zmieniony.
- Nie uruchomiono lokalnych testów: dostępny jest odczyt i zapis przez GitHub, bez lokalnego checkoutu repo. Pełny CI Quality Gate musi przejść przed scaleniem.
- Materiały wymagają niezależnej recenzji prawnej i instruktorskiej.
