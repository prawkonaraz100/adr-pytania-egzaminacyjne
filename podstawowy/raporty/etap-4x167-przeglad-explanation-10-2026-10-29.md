# Etap 4x167 — drugi przegląd explanation, partia 8

Data: 2026-10-29. Punkt wyjścia: świeży `main` po scaleniu PR #635, bank 651 pytań. Raporty 4x156–4x166 sprawdzono; wcześniej poprawione rekordy pominięto.

## Zakres i redakcja

Poprawiono 10 wyjaśnień: ADR-B-0086, 0180, 0225, 0252, 0291, 0304, 0355, 0395, 0464 i 0550. Każde ma 2–5 zdań i 320–386 znaków. Wyjaśnienia rozpoczynają się od praktycznego powodu poprawnej odpowiedzi, omawiają mylące warianty i kończą się krótką podstawą ADR.

Zmieniono wyłącznie pole `explanation`. Nie zmieniano pytań, opcji, kluczy, źródeł ani statusów. Nie stwierdzono potwierdzonego błędu uzasadniającego zmianę klucza; nie dodano nowych pytań.

## Synchronizacja i kontrola

Zsynchronizowano snapshoty audytu sekwencyjnego i prawnego dla rekordów partii, manifesty i materiały recenzyjne wskazujące aktualny bank oraz pięć wariantów egzaminu i klucze. Scalenie dopiero po pełnym PASS Quality Gate CI. Wszystkie pytania pozostają `needs_review`; nic nie oznaczono jako `verified`. Niezależna weryfikacja prawna specjalisty pozostaje wymagana. Tylko kurs podstawowy ADR; bez kursu cystern.
