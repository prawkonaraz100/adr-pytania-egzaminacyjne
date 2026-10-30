# Etap 4x194 — drugi przegląd 10 explanation (partia 35)

Data: 2026-10-30. Punkt wyjścia: świeży `main`, commit `289595bf4255af94cf821ea5c3e5537feb0ede73`, bank 651 pytań.

## Wybrane rekordy

ADR-B-0419, ADR-B-0354, ADR-B-0383, ADR-B-0384, ADR-B-0389, ADR-B-0423, ADR-B-0132, ADR-B-0149, ADR-B-0350 i ADR-B-0356.

Wybrano jedne z najkrótszych i najbardziej skrótowych wyjaśnień spośród pytań nieobjętych drugim przeglądem 4x156–4x193. Przed wyborem porównano historię etapów 4x156–4x193 z aktualnym bankiem. Zakres wyłącznie kurs podstawowy ADR; bez kursu cystern.

## Redakcja

Zmieniono wyłącznie pole `explanation` w dziesięciu rekordach. Wyjaśnienia mają 335–372 znaki i 4–5 zdań. Każde najpierw tłumaczy praktyczny sens poprawnej odpowiedzi, następnie objaśnia, dlaczego pozostałe warianty są mylące lub błędne, i kończy się krótką podstawą ADR.

Nie zmieniono treści pytań, opcji A/B/C, kluczy, źródeł ani statusów. Nie stwierdzono potwierdzonego błędu merytorycznego wymagającego zmiany pytania lub klucza. Wszystkie rekordy pozostają `needs_review`; nie nadano `verified`.

## Synchronizacja i kontrola

Odświeżono istniejące snapshoty `review/sequential` i `review/legal-clauses` dla wszystkich dziesięciu ID:
- ADR-B-0132 i ADR-B-0149 — 121-150
- ADR-B-0350, ADR-B-0354 i ADR-B-0356 — 345-362
- ADR-B-0383, ADR-B-0384 i ADR-B-0389 — 381-398
- ADR-B-0419 i ADR-B-0423 — 417-436

W snapshotach sekwencyjnych ustawiono `editorial_read_through.explanation = true`, a w snapshotach prawnych zaktualizowano teksty wyjaśnień zgodnie z bankiem.

Zsynchronizowano `source_bank_head` we wszystkich wariantach i kluczach egzaminów próbnych 001–005. Klucz 003 zawiera dwa wybrane pytania (ADR-B-0383 i ADR-B-0149), więc odświeżono w nim także oba pola explanation. Zaktualizowano aktualny SHA banku w manifestach i dokumentach pakietu recenzyjnego.

## Kontrola różnic

Porównanie z bazowym `main` potwierdziło, że dla każdego z 10 wybranych rekordów zmieniło się wyłącznie pole `explanation`. Bank nadal zawiera 651 pytań, wszystkie ze statusem `needs_review`, zero `verified`. Wszystkie 5 wariantów i 5 kluczy egzaminów zawiera aktualny blob banku; każdy wariant i klucz ma po 30 pytań/odpowiedzi.

## Status

Redakcja dydaktyczna nie zastępuje niezależnej recenzji prawnej specjalisty ADR. Kurs cystern pozostaje poza zakresem.
