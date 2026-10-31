# Etap 4x221 — drugi przegląd explanation (partia 62)

Data: 2026-10-31. Bazowy `main`: `b003c2668042e8e6fef7eb88866e7e41a41b9d6f`.

## Zakres

ADR-B-0226, ADR-B-0265, ADR-B-0326, ADR-B-0344, ADR-B-0359, ADR-B-0377, ADR-B-0461, ADR-B-0587, ADR-B-0594 i ADR-B-0602.

Wybrano kolejne krótkie lub wymagające prostszego objaśnienia po wykluczeniu zakresów wcześniejszych partii 4x156–4x220. Zmieniono wyłącznie pole `explanation`; treść pytań, opcje, klucze i podstawy prawne zachowano. Wyjaśnienia mają 2–5 zdań i 317–365 znaków: najpierw sens poprawnej odpowiedzi, potem wyjaśnienie błędnych wariantów, na końcu krótka podstawa ADR.

## Kontrola statusów i zakresu

Wszystkie 10 rekordów zachowuje `verification_status = needs_review`; nie nadano `verified`. Nie wprowadzono zmian merytorycznych pytań ani kluczy — była to redakcja dydaktyczna explanation. Zakres wyłącznie kurs podstawowy ADR; bez kursu cystern.

## Synchronizacja — regresja #646

- Bank: 651 rekordów; blob SHA `6325f89fa002e33a441503d5145330cc974582fd`.
- Warianty egzaminów próbnych 001–005 i klucze 001–005 odświeżono do bieżącego blobu; explanation w kluczach zsynchronizowano dla pytań występujących w danym arkuszu.
- Snapshoty `review/sequential` i `review/legal-clauses` zsynchronizowano dla wszystkich 10 ID; w snapshotach sekwencyjnych ustawiono `editorial_read_through.explanation=true`.
- SHA w pakiecie recenzyjnym, kolejkach i indeksach zaktualizowano. Historyczne SHA etapów 4x219 i 4x220 zachowano w ich wpisach.

## Kontrole i status

Praca prowadzona przez GitHub/CI; nie deklaruję lokalnego uruchomienia testów bez lokalnego checkoutu. Pełny Quality Gate `structure-and-tests` musi zakończyć się PASS na końcowym SHA PR przed scaleniem.
