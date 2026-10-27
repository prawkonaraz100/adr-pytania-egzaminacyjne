# Etap 4x99 — synchronizacja tytułów i question_ids w materiałach B-02

- Data: 2026-10-27.
- Punkt wejścia: świeży `main` po PR #556, commit `174ba28fbc384111448c10cd515caf67d7e673d5`.
- Zakres: synchronizacja scenariuszy B-02 między mapą JSON, indeksem `SCENARIUSZE.md`, lekcją i materiałami instruktora.

## Znalezione rozbieżności

Po zmianach 4x98 tytuły i opisy w `scenariusze-13-dzialow.json` były aktualne, ale starsze wersje pozostały w innych artefaktach:
- `SC-ADR-B-02-02`: indeks tabelaryczny nadal wymieniał `ADR-B-0004`, choć bieżący scenariusz ma `ADR-B-0005`, `ADR-B-0006`, `ADR-B-0510`; lekcja i instruktor nadal używały starego tytułu i sytuacji.
- `SC-ADR-B-02-03`: indeks, lekcja i instruktor nadal obiecywały ćwiczenie grup pakowania, chociaż scenariusz ćwiczy rozpoznawanie klas 3, 8 i 4.3.

## Poprawki

- Zsynchronizowano wiersze tabeli w `podstawowy/praktyka/SCENARIUSZE.md`: tytuły i listy `question_ids` odpowiadają teraz rekordom JSON.
- Zaktualizowano scenariusze wymienione w lekcji B-02, aby kursant widział nowe sytuacje i tytuły.
- Przepisano instruktaż dla obu scenariuszy: kolejność prowadzenia, kryteria obserwacji, typowe błędy i wyjaśnienia, pytania kontrolne oraz granice bezpieczeństwa.
- Dodano blokujący test `tests/test_stage4x99_scenario_index_sync.py`, który porównuje tytuły i ID między JSON, indeksem, lekcją i przewodnikiem instruktora.

## Kontrole

- Bank niezmieniony: 609 unikalnych pytań, 609 `needs_review`, 0 `verified`.
- Explanation minimum 300 znaków.
- „Poprawna = jedyna najdłuższa”: 73/609 = 11,99%; maksimum działu 14,29%.
- 39 scenariuszy, po 3 na każdy dział; wszystkie pytania istnieją i należą do właściwego modułu.
- Egzaminy próbne i klucze 001–005 bez zmian.

Zmiany dotyczą spójności materiałów dydaktycznych, nie merytoryki pytań. Nie oznaczono niczego jako `verified`.
