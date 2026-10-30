# Etap 4x179 — drugi przegląd 10 explanation (partia 20)

Data: 2026-10-30. Punkt wyjścia: `main` po PR #647, commit `5eee4bd0eb7a0d4d9f136ebe48c307735618e03d`; bank 651 pytań, wszystkie `needs_review`.

## Wybrane rekordy
ADR-B-0135, ADR-B-0199, ADR-B-0217, ADR-B-0242, ADR-B-0254, ADR-B-0328, ADR-B-0430, ADR-B-0559, ADR-B-0588 i ADR-B-0600.

Dobór wykonano spośród nieprzeglądanych w partiach 4x156–4x178 wyjaśnień o relatywnie najmniejszej długości. Pominięto pozycje dotyczące cystern jako odrębnego zakresu kursu. Nowe teksty mają 323–417 znaków i 3–4 zdania: praktyczne uzasadnienie poprawnej odpowiedzi, wyjaśnienie mylących wariantów i wskazanie podstawy ADR.

## Zakres zmian
- Zmieniono wyłącznie pole `explanation` w `podstawowy/questions.jsonl`.
- Zachowano treść pytań, warianty A/B/C, `correct_option`, źródła, podstawy prawne i statusy.
- Nie znaleziono i nie wprowadzono potwierdzonej korekty merytorycznej pytania ani klucza.
- Wszystkie rekordy pozostają `needs_review`; nie nadano `verified`.

## Walidacja i synchronizacja
Zmiana banku została zapisana na gałęzi `stage4x179-explanations-batch20`. Przed scaleniem wymagane jest pełne odświeżenie snapshotów audytu sekwencyjnego i przeglądu klauzul prawnych dla 10 ID oraz referencji blobu banku w wariantach i kluczach egzaminów próbnych 001–005. Pełny Quality Gate CI musi przejść przed scaleniem.

## Ograniczenia
Redakcja dydaktyczna nie stanowi niezależnej recenzji prawnej. Niezależny specjalista ADR nadal musi zweryfikować pytania i podstawy prawne. Zakres obejmuje wyłącznie kurs podstawowy; kurs cysterny pozostaje poza zakresem.

## Naprawa Quality Gate (30.10.2026)

Pierwszy przebieg CI wykazał:
- rozbieżne explanation w kluczach wariantów 004–005 dla ADR-B-0559, ADR-B-0430 i ADR-B-0254;
- nieaktualny SHA banku w manifeście pakietu specjalisty, obu kolejkach prawnych, dokumentach przekazania/rejestrze oraz manifeście próbki;
- nieaktualne explanation w snapshotach audytu sekwencyjnego i porównania klauzul prawnych.

Naprawiono synchronizację wszystkich pięciu kluczy 001–005 i sprawdzono zgodność wyjaśnień z bankiem po mapowaniu liter odpowiedzi. Zaktualizowano SHA w manifeście i kolejkach oraz plikach prowadzących pakiet specjalisty. Odświeżono snapshoty dla wszystkich dziesięciu ID:
- `review/sequential` i `review/legal-clauses`: 121-150, 181-210, 217-218, 241-246, 251-254, 325-344, 417-436, 546-560, 586-597, 598-609.

Żaden test ani próg Quality Gate nie został wyłączony lub poluzowany. Statusy wszystkich pytań pozostają `needs_review`; brak formalnej aprobaty prawnej.
