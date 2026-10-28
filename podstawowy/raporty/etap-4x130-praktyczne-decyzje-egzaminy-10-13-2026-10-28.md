# Etap 4x130 — praktyczne decyzje kierowcy B-10–B-13 i synchronizacja egzaminów

- Punkt wyjścia: świeży `main` `c67dd75c483630535c2d3b55af98a975e85c00aa`, po scaleniu PR #592 (etap 4x129).
- Zakres: wyłącznie kurs podstawowy ADR.

## Zmiany w lekcjach

| Lekcja | Scenariusz decyzyjny | Co kursant ma zrobić |
|---|---|---|
| B-10 — Transport kombinowany | Kontener po odcinku morskim | Sprawdzić dokumenty dla odcinka drogowego, porównać dane i oznakowanie, ustalić czy wymagany jest certyfikat pakowania, wyjaśnić braki przed wyjazdem. |
| B-11 — Tunele | Tunel z ograniczeniem | Odczytać kod tunelowy i kategorię tunelu, uwzględnić postać przewozu i ładunek mieszany, wybrać dozwoloną trasę. |
| B-12 — Ochrona przewozu | Odbiorca bez potwierdzonego uprawnienia | Nie wydawać ładunku na podstawie samego numeru zlecenia, zweryfikować uprawnienie, nie ujawniać zbędnych informacji, zgłosić naruszenie. |
| B-13 — Dokumenty | Brak danych w dokumencie | Porównać dokument z ładunkiem, nie zgadywać braków, zgłosić rozbieżność i osobno sprawdzić instrukcje pisemne. |

Każda sekcja zawiera kroki kierowcy, typowy błąd z prostym uzasadnieniem, punkty ADR do sprawdzenia oraz pytania do omówienia. Pełne scenariusze mapy pozostają bez zmian.

## Warianty egzaminu próbnego 001–005 — odświeżenie z aktualnego banku

Wykryto, że same numery ID nie wystarczają do potwierdzenia synchronizacji klucza: przy zmianach tekstu opcji w banku stary klucz może wskazywać inną literę. Dlatego odtworzono opcje arkuszy i explanation kluczy na podstawie aktualnych rekordów banku, zachowując 30 ID na wariant i ich rozdział między wariantami. Zmieniono kolejność opcji tak, aby litera klucza wskazywała aktualny tekst poprawnej odpowiedzi, z odświeżonymi wyjaśnieniami i podstawami.

- Blob banku źródłowego: `36985d2be9667dad581f241d68f7df76ea47e0d5`.
- Każdy arkusz: 30 pytań, 13 działów, po 2–3 pytania z działu.
- Wszystkie warianty: A/B/C = 10/10/10; najdłuższa seria tej samej litery ≤3.
- ID: 150 unikalnych pozycji łącznie; 30 unikalnych ID w każdym wariancie; brak powtórzeń między wariantami.
- Synchronizacja stem/opcji/klucza/explanation/ścieżki lekcji: 0 rozbieżności w kontroli przed PR.
- Wskaźnik „poprawna = jedyna najdłuższa” w wariantach: 001 0/30, 002 3/30 (10,00%), 003 0/30, 004 1/30 (3,33%), 005 0/30.
- Explanation w kluczach: minimum 301 znaków.
- Wszystkie arkusze nadal mają `publication_authorized: false`; to materiały do treningu wewnętrznego, nie oficjalny egzamin.

## Kontrola banku i referencji

- Bank: 609 pytań; duplikaty ID: 0.
- Explanation poniżej 200 znaków: 0; najkrótsze explanation: 300.
- Status `verified`: 0; statusów nie zmieniano.
- „Poprawna = jedyna najdłuższa” globalnie: 69/609 = 11.33%; wszystkie działy pozostają poniżej 18%.
- ADR-B-01: 6/45 = 13.33%.
- ADR-B-02: 7/56 = 12.50%.
- ADR-B-03: 4/49 = 8.16%.
- ADR-B-04: 6/46 = 13.04%.
- ADR-B-05: 5/43 = 11.63%.
- ADR-B-06: 6/45 = 13.33%.
- ADR-B-07: 6/48 = 12.50%.
- ADR-B-08: 3/42 = 7.14%.
- ADR-B-09: 5/46 = 10.87%.
- ADR-B-10: 4/55 = 7.27%.
- ADR-B-11: 6/43 = 13.95%.
- ADR-B-12: 5/44 = 11.36%.
- ADR-B-13: 6/47 = 12.77%.
- Mapa praktyczna: 39 scenariuszy; nie dodano duplikatów ani nowych pytań.

## Podstawy ADR do niezależnej recenzji

- B-10: ADR 1.1.4.2, 5.4.1.
- B-11: ADR 3.2 tabela A, kolumna 15; 8.6.3.
- B-12: ADR 1.10.1.4 i 1.10.3.2.
- B-13: ADR 5.4.1.1.1 i 5.4.3.1–5.4.3.4.

Źródła: ADR 2025, Dz.U. 2025 poz. 642 oraz sprostowanie Dz.U. 2025 poz. 1575. Nie oznaczono żadnego pytania jako `verified`; wymagany jest PASS CI i późniejsza recenzja specjalisty.
