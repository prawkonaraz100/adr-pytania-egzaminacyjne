# Etap 4x272 — praktyczne znaczenie litery X na tablicy ADR

Data: 01.11.2026  
Zakres: wyłącznie kurs podstawowy ADR  
Baza: main `fca622a186cb2a1845c94b571d37c9d28e3f3591`  
Gałąź: `stage4x272-fire-extinguisher-accessibility`  
Nowe ID: `ADR-B-0698`  
Kompetencja: `ADR-B-06-K04` — znaczenie litery X przed numerem rozpoznawczym zagrożenia

## Wybór luki

Kompetencja miała cztery pytania (ADR-B-0017, 0170, 0256 i 0615), z których wszystkie sprawdzały przede wszystkim rozpoznanie znaczenia litery X. Brakowało sytuacji, w której kierowca musi przekazać ratownikom praktyczną konsekwencję oznaczenia. Nowe pytanie sprawdza odczyt X i komunikację ostrzeżenia, bez przypisywania kierowcy prawa do decydowania o użyciu środka gaśniczego.

## Dodane pytanie

- `ADR-B-0698`: kierowca odczytuje X423 i przekazuje ratownikom ostrzeżenie przed niebezpieczną reakcją materiału z wodą.
- Klucz: **B** — materiał reaguje niebezpiecznie z wodą; jej użycie wymaga zgody specjalistów.
- Explanation: **381 znaków, 5 zdań**; praktyczna decyzja, pułapki odpowiedzi i podstawa ADR.
- Długości A/B/C: **118/126/110** znaków; poprawna B jest najdłuższa, ale nie jest to oczywisty sygnał długościowy. Globalny wskaźnik po dodaniu: 73/698 = 10,46%.
- Audyt A/B/C: A — błędnie sprowadza X do nasilenia zagrożenia i dopuszcza samodzielną ocenę wody; B — prawidłowo przekazuje ostrzeżenie i warunek zgody specjalistów; C — błędnie utożsamia X z brakiem palności.
- Status: `needs_review`; nic nie oznaczono jako `verified`.

## Podstawa prawna — źródło oficjalne sprawdzone

- **ADR 2025, 5.3.2.3.1**, tom II, s. 251: numer rozpoznawczy zagrożenia poprzedzony literą X oznacza, że materiał reaguje niebezpiecznie z wodą; woda może być stosowana jedynie za zgodą specjalistów.
- Oficjalny polski tekst ADR 2025, Ministerstwo Infrastruktury: https://www.gov.pl/attachment/b4638c72-30e3-4bff-afd1-1b9ba4100e70
- Dz.U. 2025 poz. 642: https://dziennikustaw.gov.pl/DU/2025/642
- UNECE ADR 2025: https://unece.org/adr-2025-files

Właściwy fragment punktu 5.3.2.3.1 został sprawdzony bezpośrednio w oficjalnym polskim tekście ADR 2025. Pełne porównanie wszystkich elementów pytania z tekstem Dz.U. oraz niezależna recenzja specjalisty pozostają pending.

## Synchronizacja #646

- Bank: 698 rekordów, `ADR-B-0001…0698`, wszystkie `needs_review`, 0 `verified`.
- Blob SHA banku: `e81ce0f9d620ab270c41bf0d09903d4aad43dc8e`.
- Odświeżono klucze i warianty egzaminów próbnych 001–005, każdy `source_bank_head` wskazuje nowy blob.
- Utworzono snapshot sekwencyjny i prawny dla pytania 0698 (pliki nazywają się 697-697 z powodu zachowania istniejącej ścieżki; batch wewnątrz snapshotu: 698-698).
- Pozostałe manifesty, kolejki, rejestry specjalisty, metryki i testy regresyjne wymagają synchronizacji w ramach tej gałęzi; PR nie jest gotowy do scalenia, dopóki CI nie potwierdzi kompletności.

