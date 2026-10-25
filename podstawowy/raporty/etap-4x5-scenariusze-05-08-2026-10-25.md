# Etap 4x5 — scenariusze praktyczne ADR-B-05–08

- Punkt wyjścia: świeży main `61a84ab1328b11f5341ed96a6b7f5e852abaea08`.
- Dodano 8 scenariuszy (po dwa na dział): awaria bez rozpoznanej przyczyny, pożar przy przestrzeni ładunkowej, rozbieżność tablicy pomarańczowej, zasłonięta nalepka, uszkodzone opakowanie i podział obowiązków, dostępność instrukcji pisemnych, kontrola gaśnic oraz wyposażenie osobiste całej załogi.
- Każdy scenariusz zawiera sytuację, co najmniej 4 kroki, co najmniej 2 błędy z wyjaśnieniem, podstawę ADR, pytania, kryteria oceny i granice bezpieczeństwa.
- Kontrola referencji przed PR: 8 nowych ID scenariuszy unikalnych; wszystkie powiązane pytania istnieją i należą do właściwego modułu. Bank i klucze bez zmian; brak statusów `verified` dodanych przez tę partię.
- Liczba scenariuszy po tej partii: 29; B-05–B-08 mają po trzy scenariusze.
- Testy lokalne nie zostały uruchomione w repozytorium roboczym; przed scaleniem wymagany jest PASS CI Quality Gate.
