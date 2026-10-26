# Etap 4x43 — aktualność pakietu recenzyjnego

Data: 2026-10-26. Punkt wyjścia main: 039955c23554a27b259fac66f49b6241a3d6de3c.

## Potwierdzona rozbieżność

Po scaleniu etapu 4x42 bank miał blob SHA `8a16afb47c5d5a9e460092b7e474b4a3e8a5a8d9`, ale bieżące nagłówki w instrukcji recenzji i przekazaniu specjalisty nadal wskazywały wcześniejszy snapshot `99c06e736c0e5812e97d4ff02567dbf741629434` i etap 4x29. Mogło to spowodować pracę recenzenta na nieaktualnym stanie dokumentacji. Bank sam w sobie nie zmienił się w 4x42.

## Poprawki

- `review/specialist/INSTRUKCJA-RECENZJI.md`: zaktualizowano SHA banku i link do najnowszego raportu 4x42.
- `review/specialist/PRZEKAZANIE-ETAP4.md`: odświeżono bieżący snapshot, punkt wyjścia main, SHA banku oraz informację o 150 odnośnikach `lesson_path` w kluczach.
- `review/specialist/REJESTR-AKTUALNY-0001-0609.md`: zaktualizowano nagłówek i wskazanie najnowszego raportu; rekordy i statusy pytań bez zmian.
- `review/README.md`: zaktualizowano etykietę bieżącego etapu, bank SHA i odnośnik do raportu 4x42.
- `tests/test_review_packet_integrity.py`: dodano test blokujący, który porównuje bank SHA z manifestem oraz sprawdza, czy cztery bieżące dokumenty recenzji podają tę samą migawkę, liczbę 609 i statusy; przekazanie musi też odsyłać do raportu 4x42 i zawierać informację o `lesson_path`.

## Stan prawny i liczby

- Bank: 609 pytań; 609 `needs_review`, 0 `verified`, 0 formalnych zatwierdzeń.
- Nierozstrzygnięte porównania literalne: 376 — liczba zachowana z manifestu, bez deklarowania dodatkowej weryfikacji prawnej.
- Pozycje bez zapisanego dosłownego fragmentu MI: 121.
- Kolejka priorytetowa: 20 pytań, wszystkie oczekują na porównanie z urzędowym tekstem.
- Scenariusze: 39; egzaminy próbne: 5 wariantów i 5 kluczy.
- Brak zmian w banku, kluczach, odpowiedziach i statusach `verification_status`.

## Testy

Próba lokalnego klonowania nadal jest zablokowana przez DNS w środowisku wykonawczym. Nie deklaruję lokalnego PASS. Pełny Quality Gate CI na PR musi przejść przed scaleniem.

## Ograniczenia

Ta zmiana naprawia aktualność i identyfikowalność pakietu, nie rozstrzyga poprawności merytorycznej ani prawnej pytań. Do `verified` może przejść wyłącznie rekord z rzeczywistym dowodem urzędowym i autentyczną recenzją specjalisty.
