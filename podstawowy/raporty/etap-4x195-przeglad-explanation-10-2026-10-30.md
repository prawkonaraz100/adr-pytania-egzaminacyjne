# Etap 4x195 — drugi przegląd 10 explanation (partia 36)

Data: 2026-10-30. Punkt wyjścia: świeży `main`, commit `4bb4b745344220343ec83aa35e70fb72f68bcff3`, bank 651 pytań.

## Wybrane rekordy

ADR-B-0012, ADR-B-0100, ADR-B-0264, ADR-B-0327, ADR-B-0640, ADR-B-0011, ADR-B-0027, ADR-B-0109, ADR-B-0364 i ADR-B-0358.

Wybrano kolejne krótkie lub skrótowe wyjaśnienia, których nie obejmowały etapy 4x156–4x194. Zakres wyłącznie kurs podstawowy ADR; bez kursu cystern.

## Redakcja

Zmieniono wyłącznie pole `explanation` w dziesięciu rekordach. Wyjaśnienia mają 338–408 znaków i po 4 zdania. Każde najpierw wyjaśnia praktyczny sens poprawnej odpowiedzi, następnie objaśnia mylące lub błędne warianty, a na końcu wskazuje krótką podstawę ADR.

Nie zmieniono treści pytań, opcji A/B/C, kluczy, źródeł ani statusów. Nie stwierdzono potwierdzonego błędu merytorycznego wymagającego zmiany pytania lub klucza. Wszystkie rekordy pozostają `needs_review`; nie nadano `verified`.

## Synchronizacja i kontrola

Odświeżono snapshoty `review/sequential` i `review/legal-clauses` dla wszystkich dziesięciu ID:
- ADR-B-0011, ADR-B-0012 i ADR-B-0027 — 001-030
- ADR-B-0100 i ADR-B-0109 — 091-120
- ADR-B-0264 — 262-264
- ADR-B-0327 — 325-344
- ADR-B-0358 — 345-362
- ADR-B-0364 — 363-380
- ADR-B-0640 — 629-651

W snapshotach sekwencyjnych ustawiono `editorial_read_through.explanation = true`; sprawdzenie po zapisie potwierdziło, że wszystkie 10 tekstów w snapshotach sekwencyjnych i prawnych jest identycznych z bankiem.

Zsynchronizowano `source_bank_head` we wszystkich wariantach i kluczach egzaminów próbnych 001–005. Klucz 004 zawiera ADR-B-0109 i ADR-B-0011, więc odświeżono w nim także oba pola explanation. CI wykryło również wcześniejszą niespójność explanation ADR-B-0537 w kluczu 005 i snapshotach audytu; zsynchronizowano klucz oraz snapshoty sequential/legal z niezmienionym rekordem banku (bez zmiany pytania ani klucza). Zaktualizowano aktualny SHA banku w manifestach i dokumentach pakietu recenzyjnego.

## Kontrola różnic

Porównanie z bazowym `main` potwierdziło, że dla każdego z 10 wybranych rekordów zmieniło się wyłącznie pole `explanation`. Bank nadal zawiera 651 pytań, wszystkie ze statusem `needs_review`, zero `verified`. Wszystkie 5 wariantów i 5 kluczy egzaminów ma aktualny blob banku oraz po 30 pytań/odpowiedzi.

## Status

Redakcja dydaktyczna nie zastępuje niezależnej recenzji prawnej specjalisty ADR. Kurs cystern pozostaje poza zakresem.
