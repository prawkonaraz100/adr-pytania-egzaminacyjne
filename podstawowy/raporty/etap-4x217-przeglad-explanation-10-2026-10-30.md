# Etap 4x217 — drugi przegląd explanation (partia 58)

Data: 2026-10-30. Bazowy main: `df44a275e5759292b4c03736806f94cc37d62b44`.

## Zakres

ADR-B-0562, ADR-B-0393, ADR-B-0460, ADR-B-0561, ADR-B-0444, ADR-B-0553, ADR-B-0385, ADR-B-0470, ADR-B-0549 i ADR-B-0485.

Wybrano kolejne krótkie lub zbyt skrótowe wyjaśnienia, których ID nie występują w raportach drugiego przeglądu 4x156–4x216. Zakres wyłącznie kurs podstawowy ADR.

## Redakcja

Zmieniono wyłącznie pole `explanation`. Każde wyjaśnienie ma 2–5 zdań i 300–500 znaków; najpierw wyjaśnia praktyczny sens poprawnej odpowiedzi, następnie wskazuje, dlaczego błędne odpowiedzi mogą mylić, a na końcu podaje krótką podstawę ADR. Nie zmieniono pytań, opcji A/B/C, kluczy, źródeł ani statusów.

Szczególną ostrożność zachowano przy:
- ADR-B-0385 — nie rozszerzano wyjątku z 1.1.4.2.1(c) poza warunki wskazane w przepisie;
- ADR-B-0444 — data historyczna cysterny nie została przedstawiona jako bezwarunkowe zwolnienie; pozostają warunki badań i kontroli;
- ADR-B-0460 — klasa 3 sama nie przesądza o towarze dużego ryzyka; trzeba odczytać tabelę i właściwe progi;
- ADR-B-0470 — mniejszy znak środowiskowy opisano jako wyjątek zależny od pojemności i dostępnej powierzchni.

## Synchronizacja

- Bank: 651 rekordów; blob `questions.jsonl`: `4b843273ac549c0201b2a5985d01f17d09cdf8bc`.
- Warianty egzaminów próbnych 001–005 i klucze 001–005 wskazują aktualny blob banku; wyjaśnienia kluczy sprawdzono i odświeżono, jeśli dane ID występują w danym wariancie.
- Snapshoty `review/sequential` i `review/legal-clauses` zsynchronizowano dla wszystkich 10 ID; w snapshotach sekwencyjnych `editorial_read_through.explanation=true`.
- SHA pakietu recenzyjnego, kolejek specjalisty, manifestów i indeksów zaktualizowano.

## Kontrole i status

Pełny Quality Gate i CI muszą zakończyć się PASS przed scaleniem. Praca prowadzona przez GitHub/CI; nie deklaruje się lokalnego uruchomienia testów bez lokalnego checkoutu.

Bank: 651 `needs_review`, zero `verified`. Redakcja dydaktyczna nie stanowi niezależnej recenzji prawnej specjalisty. Wyłącznie kurs podstawowy ADR; bez kursu cystern.
