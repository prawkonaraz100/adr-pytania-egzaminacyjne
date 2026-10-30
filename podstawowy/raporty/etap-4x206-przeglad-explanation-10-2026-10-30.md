# Etap 4x206 — drugi przegląd 10 explanation (partia 47)

Data: 2026-10-30. Punkt wyjścia: świeży `main` po etapie 4x205, commit `b88d79e1d803959b50e4cf5a9c60ab95fffb9125`, bank kursu podstawowego 651 pytań.

## Wybrane rekordy

ADR-B-0014, ADR-B-0046, ADR-B-0239, ADR-B-0261, ADR-B-0315, ADR-B-0331, ADR-B-0349, ADR-B-0398, ADR-B-0467 i ADR-B-0545.

Wybrano kolejne krótkie lub wymagające dopowiedzenia wyjaśnienia, które nie były objęte drugim przeglądem 4x156–4x205. Pytania dotyczą kursu podstawowego; nie włączono zagadnień kursu cystern.

## Redakcja

Zmieniono wyłącznie pole `explanation` w dziesięciu rekordach. Każde nowe wyjaśnienie ma 4 zdania i 338–431 znaków. Tekst najpierw tłumaczy praktyczny sens poprawnej odpowiedzi, następnie wyjaśnia, dlaczego błędne warianty są mylące lub niewłaściwe, a na końcu podaje krótką podstawę ADR.

Nie zmieniono treści pytań, opcji A/B/C, kluczy, źródeł ani statusów. Nie stwierdzono potwierdzonego błędu merytorycznego wymagającego zmiany pytania lub klucza. Wszystkie rekordy pozostają `needs_review`; nie nadano `verified`.

## Synchronizacja

Odświeżono snapshoty `review/sequential` i `review/legal-clauses` dla wszystkich 10 ID:
- ADR-B-0014 — 001-030
- ADR-B-0046 — 031-060
- ADR-B-0239 — 235-240
- ADR-B-0261 — 259-261
- ADR-B-0315 — 314-315
- ADR-B-0331 — 325-344
- ADR-B-0349 — 345-362
- ADR-B-0398 — 381-398
- ADR-B-0467 — 461-470
- ADR-B-0545 — 543-545

W snapshotach sekwencyjnych ustawiono `editorial_read_through.explanation = true`. Zsynchronizowano `source_bank_head` w wariantach i kluczach egzaminów próbnych 001–005; wyjaśnienia w kluczu 003 odświeżono dla ADR-B-0331 i ADR-B-0398. Warianty zachowują po 30 pytań, klucze po 30 odpowiedzi.

## Status

Bank: 651 pytań, wszystkie `needs_review`, zero `verified`. Redakcja dydaktyczna nie zastępuje niezależnej recenzji prawnej specjalisty. Zakres wyłącznie kurs podstawowy ADR; kurs cystern pozostaje poza zakresem.
