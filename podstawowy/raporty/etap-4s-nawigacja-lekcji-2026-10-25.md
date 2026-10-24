# Etap 4s — czytelność nawigacji w 13 lekcjach ADR podstawowego

- Baza: `28abf1c9ac336b5d216a66d57ec871b7a8b3055a` (po scaleniu PR #273).
- Zakres: nagłówki i kolejność sekcji w 13 plikach `podstawowy/lekcje/ADR-B-01.md`–`ADR-B-13.md`.

## Potwierdzony problem

W każdej lekcji po głównych sekcjach występują materiały dopisywane etapami: „Utrwalanie przez scenariusz — przegląd etapu 2”, zadania instruktorskie, plany dydaktyczne, pojedyncze pytania i mapy powiązań. Te treści mogą być przydatne, ale ich historyczne nagłówki mieszają się z główną ścieżką dla kursanta. Przykładowo B-01 ma wiele dopisanych scenariuszy i plan instruktorski; B-02 zawiera serię scenariuszy oraz osobny plan prowadzącego; podobny wzorzec występuje w pozostałych lekcjach.

## Wprowadzona korekta

Dodano na początku każdej lekcji krótką sekcję „Jak korzystać z tej lekcji”, która wskazuje kolejność nauki, zachęca do rozumienia skrótów przez przykłady i wyjaśnia, że dalsze sekcje scenariuszowe/archiwalne są materiałem uzupełniającym, a nie kolejnymi równorzędnymi rozdziałami. Przypomniano też, że bank pytań jest `needs_review` i quiz nie potwierdza zaliczenia praktyki.

Nie usuwano historii, nie zmieniano treści prawnej, pytań, kluczy ani statusów. To mała, odwracalna poprawa nawigacji, nie pełna redakcja lub reorganizacja dokumentów.

## Test regresyjny

Dodano `tests/test_lesson_navigation.py`: wszystkie 13 lekcji muszą zawierać przewodnik, objaśnienie materiałów uzupełniających i przypomnienie statusu `needs_review`.

## Ograniczenia

Nie przeprowadzono odbioru instruktorskiego ani prawnego. Wszystkie 566 pytań pozostają `needs_review`, zero `verified`. Wskaźnik długości odpowiedzi nie ulega zmianie: 71/566 = 12,54%, poniżej progu 18% globalnie i w każdym dziale.
