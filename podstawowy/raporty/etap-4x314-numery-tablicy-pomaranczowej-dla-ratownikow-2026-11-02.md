# Etap 4x314 — numery z tablicy pomarańczowej dla ratowników

2026-11-02. Bazowy main `bd40bd146fbca3e6c325285c25e55a293b25c9d1`; gałąź `stage4x314-emergency-services-cargo-information`.

- Dodano ADR-B-0740 do `ADR-B-05-K03`: przekazywanie służbom informacji o zdarzeniu i ładunku z czytelnej tablicy pomarańczowej.
- Kompetencja wzrosła z 5 do 6 pytań; kompetencje teorii z mniej niż 6 pytaniami: **40** (3 praktyczne pominięte).
- Bank: 740 pytań (ADR-B-0001–0740), 740 `needs_review`, 0 `verified`; SHA `9a04009ad8e65d597c70d3e337f861c672f840f3`.
- Moduł ADR-B-05: 78 pytań.
- Rozkład kluczy A/B/C: 248/264/228.
- „Poprawna odpowiedź jest jedyną najdłuższą”: **81/740 = 10,95%**; maksimum działu **14,61%**. Długości opcji ADR-B-0740: A=105, B=89, C=103; poprawna B nie jest najdłuższa.
- Explanation: 405 znaków, 4 zdania. Wyjaśnia, że górny numer tablicy oznacza zagrożenie, a dolny numer UN identyfikuje towar; przypomina o bezpiecznym odczycie i przekazaniu danych.
- Podstawa: ADR 2025, 5.3.2.2.2 i 5.4.3.4. Status `needs_review`; pełne literalne porównanie i niezależna recenzja pozostają otwarte.
- Odświeżono klucze i warianty 001–005, snapshoty sequential/legal 740, ledger, pakiety, kolejki prawne, rejestr specjalisty, coverage, lekcję B-05, README i testy liczebności.

## Pytanie ADR-B-0740

Kierowca po kolizji zgłasza zdarzenie służbom z bezpiecznego miejsca. Nie może wrócić po dokumenty, ale widzi z daleka czytelną tablicę pomarańczową z dwoma numerami. Co powinien przekazać?

A. Podać tylko numer z górnej części, bo dolny dotyczy dokumentów przewozowych, a nie identyfikacji ładunku.

B. Podać oba numery: górny wskazuje zagrożenie, a dolny jest numerem UN przewożonego towaru.

C. Podać wyłącznie numer rejestracyjny pojazdu i poczekać z informacją o ładunku do odczytania dokumentów.

Tablica pomarańczowa może przekazać ratownikom dwa ważne oznaczenia: u góry numer rozpoznawczy zagrożenia, a na dole numer UN towaru. Oba pomagają rozpoznać rodzaj zagrożenia i przewożoną substancję, dlatego nie pomijaj żadnego z nich. Nie ograniczaj zgłoszenia do numeru rejestracyjnego i nie wracaj po dokumenty, jeśli oznaczałoby to wejście w strefę zagrożenia. Podstawa: ADR 2025, 5.3.2.2.2 i 5.4.3.4.

## Audyt A/B/C i źródła

- A — błędna: dolna część tablicy zawiera numer UN i również przekazuje ważną informację o ładunku.
- B — poprawna: numer rozpoznawczy zagrożenia znajduje się u góry, a numer UN na dole tablicy pomarańczowej.
- C — błędna: sam numer rejestracyjny nie identyfikuje przewożonego towaru; dostępne informacje o ładunku powinny trafić do ratowników.
- Źródło: Dz.U. 2025 poz. 642, ADR 2025, 5.3.2.2.2 i 5.4.3.4 — https://eli.gov.pl/api/acts/DU/2025/642/text.pdf.
- Nie oznaczono żadnego pytania jako `verified`.
