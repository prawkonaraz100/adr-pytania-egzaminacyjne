# Etap 4x12 — słowniczek i czytelność lekcji, partia B-01–04

- Punkt wyjścia: świeży main `ef07c7f984ddaa1dd0e2466c796d34afb5c183fc`; bank 609 pytań, statusy `needs_review`.
- Rozbudowano `podstawowy/SLOWNICZEK.md` do 90 haseł (pierwotne definicje zachowane, dopisano definicje skrótów, dokumentów, typów pojazdów, opakowań, załadunku i zasad ochrony).
- W B-01–04 dodano widoczny odsyłacz do słowniczka bezpośrednio pod tytułem, przed pierwszym rozdziałem.
- Dodano blokujący test `tests/test_learner_glossary.py`: sprawdza ustalony zestaw terminów w słowniczku oraz odsyłacz na początku wszystkich 13 lekcji. Test pilnuje pokrycia słownika, nie ocenia samodzielnie poprawności prawnej definicji.
- Bank bez zmian: 609 pytań; nie zmieniono odpowiedzi ani statusów. Explanation minimum 300 znaków. Wskaźnik długości odpowiedzi: B-01 15,56%, B-02 14,29%, B-03 14,29%, B-04 15,22% — wszystkie poniżej 16%.

## Ręczny przegląd kandydatów heurystyki w tej partii

Przeanalizowano kandydaty z B-01–04 z aktualnej listy:
- **ADR-B-0147:** fałszywy alarm — wyjaśnia różnicę między zestawem ciągnik+naczepa a dwiema niezależnymi jednostkami.
- **ADR-B-0529:** fałszywy alarm — pokazuje, dlaczego szkolenie bezpieczeństwa musi przygotować do rozpoznania zagrożeń, a nie do zadań administracyjnych.
- **ADR-B-0534:** fałszywy alarm — objaśnia, co zrobić, gdy znaki LQ są zasłonięte przez opakowanie zbiorcze, i dlaczego inne dane ich nie zastępują.
- **ADR-B-0349:** fałszywy alarm — wskazuje cel doboru miejsca postoju i przykłady miejsc, które nie spełniają warunku.
- **ADR-B-0357:** fałszywy alarm — odrzuca rękawice i odczekanie jako pozorne wyjątki od zakazu otwierania sztuk przesyłek.
- B-02 i B-03: brak pozostałych kandydatów po odtworzeniu aktualnej heurystyki.

Nie znaleziono potwierdzonego problemu dydaktycznego wymagającego przepisania tych pięciu wyjaśnień. To ocena językowa, nie formalna akceptacja prawna. Raport 4x11 podaje 11 kandydatów pozostałych, lecz odtworzenie sygnałów z aktualnego skryptu na bieżącym banku daje 13; rozbieżność zostanie opisana w raporcie końcowym na podstawie aktualnego wyniku.

## Pliki
- `podstawowy/SLOWNICZEK.md`
- `podstawowy/lekcje/ADR-B-01.md` … `ADR-B-04.md`
- `tests/test_learner_glossary.py`

Nie zmieniano pytań, opcji, poprawnych liter ani statusów weryfikacji.
