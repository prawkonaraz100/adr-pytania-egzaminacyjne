# Etap 4x12 — słowniczek i czytelność lekcji, partia B-09–13

- Punkt wyjścia: świeży main `31e1a5fb94a48b91ad6a44a779fa0fc360e2cde9`; bank 609 pytań.
- Słowniczek `podstawowy/SLOWNICZEK.md` zawiera 90 haseł. W każdej lekcji B-09–13 dodano widoczny odsyłacz do niego bezpośrednio pod tytułem, przed pierwszym rozdziałem.
- Blokujący test `tests/test_learner_glossary.py` sprawdza ustalony zestaw terminów i istnienie odsyłacza w 13/13 lekcji.
- Ręcznie przejrzano 6 kandydatów z B-09–13:
  - **ADR-B-0086:** fałszywy alarm — wyjaśnia wybór najbardziej restrykcyjnego kodu tunelowego z uwzględnieniem wyłączeń i sposobu przewozu.
  - **ADR-B-0248:** fałszywy alarm — wskazuje dokładne miejsce znalezienia kodu tunelowego i odróżnia je od numeru UN oraz nazwy nadawcy.
  - **ADR-B-0067:** fałszywy alarm — tłumaczy, dlaczego identyfikacja członka załogi wymaga właściwego dokumentu, a cudzy dokument lub list przewozowy nie identyfikuje drugiej osoby.
  - **ADR-B-0120:** fałszywy alarm — wyjaśnia cel weryfikacji odbiorcy i dlaczego sam telefon/e-mail nie potwierdza tożsamości.
  - **ADR-B-0402:** fałszywy alarm — opisuje, że plan ochrony powinien wskazywać środki odpowiadające rozpoznanym zagrożeniom.
  - **ADR-B-0403:** fałszywy alarm — opisuje potrzebę jasnej ścieżki zgłoszenia incydentu i reakcji.
- Nie znaleziono potwierdzonej wady językowej wymagającej przepisywania tych explanation. Nie zmieniano banku ani statusów.
- Wskaźniki bez zmian: B-09 8,70%, B-10 7,27%, B-11 13,95%, B-12 15,91%, B-13 8,51%; wszystkie ≤16%. Explanation minimum 300 znaków.

## Spójność licznika heurystyki
Raport 4x11 podaje 11 kandydatów po rozszerzeniu sygnałów, ale ponowne odtworzenie funkcji z bieżącego `scripts/check_explanation_heuristics.py` na banku z main wskazało 13 ID. Wszystkie 13 przeczytano ręcznie; nie traktowano braku słowa-sygnału jako błędu automatycznego. Wynik końcowy należy więc podawać jako 13/13 przeczytanych w tym odtworzeniu, a nie bez sprawdzenia powtarzać starszą liczbę 11.

## Pliki
- `podstawowy/lekcje/ADR-B-09.md` … `ADR-B-13.md`
- `podstawowy/SLOWNICZEK.md` — bez zmian w tej partii.
- `tests/test_learner_glossary.py` — bez zmian.

Nie zmieniono odpowiedzi, kluczy, podstaw prawnych ani statusów `needs_review`.
