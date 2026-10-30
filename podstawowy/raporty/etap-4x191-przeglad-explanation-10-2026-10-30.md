# Etap 4x191 — drugi przegląd 10 explanation (partia 32)

Data: 2026-10-30. Punkt wyjścia: świeży `main`, commit `54763cd550ffaf43057ac62be6d62ef4a18455f1`, bank 651 pytań.

## Wybrane rekordy

ADR-B-0274, ADR-B-0323, ADR-B-0468, ADR-B-0497, ADR-B-0578, ADR-B-0645, ADR-B-0169, ADR-B-0335, ADR-B-0374 i ADR-B-0417.

Wybrano krótkie lub skrótowe wyjaśnienia, których nie obejmowały partie drugiego przeglądu 4x156–4x190. Zakres wyłącznie kurs podstawowy ADR; pominięto zagadnienia specjalistyczne cystern.

## Redakcja

Zmieniono wyłącznie pole `explanation` w dziesięciu rekordach. Każde wyjaśnienie ma 4 zdania i 338–414 znaków. Tekst najpierw tłumaczy praktyczny sens poprawnej odpowiedzi, następnie wyjaśnia błędne warianty, a na końcu wskazuje podstawę ADR.

Nie zmieniono treści pytań, opcji A/B/C, kluczy, źródeł ani statusów. Nie stwierdzono potwierdzonego błędu merytorycznego wymagającego zmiany pytania lub klucza. Wszystkie rekordy pozostają `needs_review`; nie nadano `verified`.

## Synchronizacja i kontrola

Odświeżono istniejące snapshoty `review/sequential` i `review/legal-clauses` dla wszystkich dziesięciu ID:
- ADR-B-0169 — 151-180
- ADR-B-0274 — 274-276
- ADR-B-0323 — 323-324
- ADR-B-0335 — 325-344
- ADR-B-0374 — 363-380
- ADR-B-0417 — 417-436
- ADR-B-0468 — 461-470
- ADR-B-0497 — 495-502
- ADR-B-0578 — 570-579
- ADR-B-0645 — 629-651

Zsynchronizowano `source_bank_head` w wariantach i kluczach egzaminów próbnych 001–005. Żadne z wybranych pytań nie występuje w kluczach odpowiedzi wariantów 001–005. Zaktualizowano referencje SHA w manifestach i dokumentach pakietu recenzyjnego oraz manifeście próbkowym.

## Status

Bank: 651 pytań, wszystkie `needs_review`, zero `verified`. Zakres wyłącznie kurs podstawowy ADR. Redakcja dydaktyczna nie zastępuje niezależnej recenzji prawnej specjalisty; kurs cystern pozostaje poza zakresem.
