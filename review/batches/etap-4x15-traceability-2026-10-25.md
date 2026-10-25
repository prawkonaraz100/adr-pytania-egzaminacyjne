# Etap 4x15 — śledzenie powiązań lekcja–bank–instruktor–scenariusz

- Punkt wyjścia: świeży `main`, commit `ec9d6a86ead70e6153db4f3aab800e345db32019`.
- Zakres: kurs podstawowy ADR.

## Kontrola przed dodaniem testu

- Bank: 609 pytań, 609 unikalnych ID.
- Scenariusze: 39, po 3 dla każdego działu.
- Każdy z 193 odnośników `question_ids` w scenariuszach wskazuje istniejące pytanie z tego samego działu; brak brakujących i międzydziałowych referencji.
- Przejrzano 13 plików instruktorskich: wszystkie ID pytań istnieją i należą do właściwego modułu.
- Przejrzano 13 lekcji: każda wymienia trzy identyfikatory scenariuszy przypisane do jej modułu; odwołania do ID pytań przechodzą istniejącą kontrolę `test_lesson_question_references.py`.

## Zmiana

Dodano `tests/test_learning_traceability.py`, który blokuje PR, jeśli:
1. lekcja lub materiał instruktora zawiera ID pytania, którego nie ma w banku albo które należy do innego działu;
2. scenariusz odwołuje się do nieistniejącego pytania lub pytania z innego działu;
3. nie ma dokładnie 39 scenariuszy, po 3 w każdym z 13 modułów;
4. lekcja albo materiał instruktora nie odsyła do wszystkich trzech scenariuszy swojego działu.

Test uruchamia się automatycznie przez istniejące `python -m unittest discover -s tests -v` w Quality Gate. Nie modyfikuje treści pytań ani kluczy.

## Wyniki jakości banku — bez zmian

- 609 `needs_review`, 0 `verified`, 0 formalnych zatwierdzeń.
- Minimum explanation: 300 znaków; 0 poniżej 200.
- „Poprawna = jedyna najdłuższa” per dział: B-01 15,56%; B-02 14,29%; B-03 14,29%; B-04 15,22%; B-05 13,95%; B-06 11,11%; B-07 12,50%; B-08 14,29%; B-09 8,70%; B-10 7,27%; B-11 13,95%; B-12 15,91%; B-13 8,51%.

## Ograniczenia

Test sprawdza integralność powiązań i strukturę plików, nie to, czy odpowiedź jest prawnie poprawna, czy scenariusz w pełni pokrywa kompetencję, ani czy zajęcia praktyczne rzeczywiście się odbyły. Wszystkie pytania pozostają `needs_review`.
