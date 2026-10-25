# Etap 4x12 — słowniczek i czytelność lekcji, partia B-05–08

- Punkt wyjścia: świeży main `951b9783b093894d77afb3000b7ec955fcc49092`; bank 609 pytań.
- Słowniczek `podstawowy/SLOWNICZEK.md` zawiera 90 haseł. W każdej lekcji B-05–08 dodano widoczny odsyłacz do niego bezpośrednio pod tytułem, przed pierwszym rozdziałem.
- Blokujący test `tests/test_learner_glossary.py` pozostaje w Quality Gate i sprawdza słownik oraz istnienie odsyłacza we wszystkich 13 lekcjach. Pozostałe lekcje mają już istniejący odsyłacz na końcu; zostanie przeniesiony na początek w ich partii.
- Ręcznie przeczytano oba pozostałe kandydaty heurystyki z B-05–08: **ADR-B-0136** i **ADR-B-0186** — oba to fałszywe alarmy. ADR-B-0136 wyjaśnia, dlaczego przypadkowy pasażer nie jest członkiem załogi dopuszczonym na mocy ADR 8.3.1; ADR-B-0186 wyjaśnia, dlaczego świadków należy ostrzec zamiast angażażować w przenoszenie uszkodzonych przesyłek. W B-06 i B-08 nie było innych kandydatów w aktualnym wyniku heurystyki.
- Nie stwierdzono potwierdzonego braku dydaktycznego, który wymagałby przepisywania explanation. Bank, odpowiedzi i klucze bez zmian; statusy pozostają `needs_review`.
- Wskaźniki bez zmian: B-05 13,95%, B-06 11,11%, B-07 12,50%, B-08 14,29%; wszystkie ≤16%. Explanation minimum 300 znaków.

## Pliki
- `podstawowy/lekcje/ADR-B-05.md` … `ADR-B-08.md`
- Słowniczek i test z poprzedniej partii bez zmian.

Nie zmieniano podstaw prawnych ani pytań bez potwierdzonej rozbieżności.
