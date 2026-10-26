# Etap 4x26 — raport końcowy kursu podstawowego

- Data: 26.10.2026.
- Punkt wyjścia: świeży `main` `ddb3021a01e182a7f6546d387ab587f44d8ba80f` po PR #457–#463.
- Zakres: redakcja 13 lekcji, synchronizacja 13 materiałów instruktora, kontrola scenariuszy i ponowna synchronizacja wariantów 001–005.

## 1. Lekcje i materiały instruktora

| Lekcja | Objaśnienia i przykłady dodane w tej partii | Zakres |
|---|---:|---|
| B-01 | 2 | kategoria transportowa; decyzja przed wyjazdem przy brakujących danych |
| B-02 | 5 | wybuch masowy, grupy zgodności, materiały utleniające, nadtlenki organiczne; rozbieżność oznakowania |
| B-03 | 2 | objaśnienie „i.n.o.”; wyciek i nieznany odpad |
| B-04 | 1 | wybór miejsca postoju i warunki nadzoru |
| B-05 | 1 | bezpieczna reakcja po awarii |
| B-06 | 2 | rozbieżność tablicy/dokumentu; odsyłacz do Tabeli A naprawiony po CI |
| B-07 | 1 | uszkodzone opakowanie i podział obowiązków |
| B-08 | 1 | kolejność kontroli wyposażenia |
| B-09 | 1 | przewóz luzem i kontrola przed załadunkiem |
| B-10 | 1 | dokumenty po odcinku morskim |
| B-11 | 1 | planowanie trasy przez tunel |
| B-12 | 1 | weryfikacja odbiorcy i naruszenie zabezpieczeń |
| B-13 | 1 | brakujące dane w dokumencie przewozowym |

Materiały instruktora dla wszystkich działów uzupełniono o prowadzenie trzech scenariuszy i pytania kontrolne. Nie zmieniono statusów prawnych; wszystkie pytania pozostają `needs_review`.

## 2. Scenariusze praktyczne

- JSON: `podstawowy/praktyka/scenariusze-13-dzialow.json` — 39 scenariuszy, dokładnie 3 na każdy z 13 działów.
- Markdown: `podstawowy/praktyka/SCENARIUSZE.md` — poprawiono nieaktualną wzmiankę o 9 scenariuszach i usunięto etykiety etapów z nagłówków.
- Kontrola pól: brakujące opisy, kroki, typowe błędy, podstawy ADR, question_ids lub kryteria oceny: 0. Nieistniejące ID albo ID przypisane do złego modułu: 0.
- Wszystkie scenariusze są symulacjami; nie stanowią dowodu wykonania ćwiczeń praktycznych.

## 3. Egzaminy próbne 001–005

Warianty i klucze ponownie zsynchronizowano z aktualnym bankiem. Bank nie zmienił się w trakcie redakcji lekcji, więc blob SHA pozostaje `ed0dee6e93f21cbb758c3d088a4d02e0aaed9fc4`.

| Wariant | Liczba pytań | Unikalne ID | Działy | A/B/C | Najdłuższa seria | Poprawna jedyną najdłuższą | Min. explanation |
|---|---:|---:|---:|---|---:|---:|---:|
| 001 | 30 | 30 | 13 | 10/10/10 | 3 | 0/30 (0.00%) | 305 znaków |
| 002 | 30 | 30 | 13 | 10/10/10 | 3 | 0/30 (0.00%) | 309 znaków |
| 003 | 30 | 30 | 13 | 10/10/10 | 3 | 0/30 (0.00%) | 301 znaków |
| 004 | 30 | 30 | 13 | 10/10/10 | 3 | 0/30 (0.00%) | 317 znaków |
| 005 | 30 | 30 | 13 | 10/10/10 | 3 | 0/30 (0.00%) | 304 znaków |

- Powtórzenia ID w ramach arkuszy: 0; między wariantami: 0.
- Brakujące ID w banku: 0; rozbieżności klucza względem banku: 0.
- Wszystkie arkusze zachowują `publication_authorized: false` i są wyłącznie materiałem treningowym.

## 4. Wskaźnik „poprawna = jedyna najdłuższa” w banku

- Bank: 609 pytań, unikalne ID: 609; minimum explanation: 300 znaków.
- Globalnie: 73/609 = 11.99%.
- Per dział:
  - ADR-B-01: 6/45 = 13.33%
  - ADR-B-02: 8/56 = 14.29%
  - ADR-B-03: 7/49 = 14.29%
  - ADR-B-04: 6/46 = 13.04%
  - ADR-B-05: 6/43 = 13.95%
  - ADR-B-06: 5/45 = 11.11%
  - ADR-B-07: 6/48 = 12.50%
  - ADR-B-08: 5/42 = 11.90%
  - ADR-B-09: 4/46 = 8.70%
  - ADR-B-10: 4/55 = 7.27%
  - ADR-B-11: 6/43 = 13.95%
  - ADR-B-12: 6/44 = 13.64%
  - ADR-B-13: 4/47 = 8.51%
- Statusy: 609 `needs_review`, 0 `verified`. Niczego nie oznaczono jako `verified`.

## 5. PR-y i CI

- PR #457 — B-01–02: PASS.
- PR #458 — B-03–04: PASS.
- PR #459 — B-05–06: pierwszy przebieg wykrył brak odsyłacza do Tabeli A; po poprawce CI PASS.
- PR #460 — B-07–08: PASS.
- PR #461 — B-09–10: PASS.
- PR #462 — B-11–12: PASS.
- PR #463 — B-13: PASS.
- Ta końcowa partia aktualizuje indeks scenariuszy, metadane egzaminów i raport; wymaga jeszcze PASS Quality Gate przed scaleniem.

## Ograniczenia

Testów lokalnych nie uruchomiono w środowisku GitHub; wynik CI na PR będzie potwierdzeniem. Nie wykonano niezależnej recenzji prawnej i nie zmieniono kluczy banku. Kurs podstawowy pozostaje w statusie `needs_review`; nie rozpoczęto kursu cystern ani innej specjalizacji.
