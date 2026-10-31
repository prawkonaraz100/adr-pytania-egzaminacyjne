# Etap 4x254 — oznaczenie odpadu w dokumencie przewozowym ADR

Data: 31.10.2026  
Zakres: wyłącznie kurs podstawowy ADR  
Baza: świeży `main` po PR #723, bank 679 pytań, ostatni ID `ADR-B-0679`  
Kompetencja: `ADR-B-03-K02` — odpady niebezpieczne w dokumencie przewozowym  
Nowe pytanie: `ADR-B-0680`

## Dlaczego wybrano tę lukę

Mapa kompetencji wskazywała cztery pytania w K02, ale wszystkie sprawdzały głównie odtworzenie zasady dodania słowa „ODPAD”. Nie było sytuacji, w której kursant musi odróżnić dokument przewozowy ADR od karty przekazania odpadu i zdecydować, co zrobić przed wyjazdem, gdy brakuje wymaganego elementu opisu.

## Dodane pytanie

- **ADR-B-0680** — przy odbiorze odpadu zawierającego towary niebezpieczne kierowca widzi brak słowa „ODPAD” przed prawidłową nazwą przewozową, choć nie jest ono częścią tej nazwy. Nadawca przekazuje również kartę przekazania odpadu.
- Klucz: **A** — wstrzymać wyjazd i uzyskać poprawiony dokument ADR od nadawcy; karta odpadu nie zastępuje dokumentu ADR.
- Explanation: **406 znaków, 4 zdania**; najpierw wyjaśnia wymóg oznaczenia odpadu, potem różnicę między dokumentami i zakaz samodzielnego dopisywania klasyfikacji, na końcu wskazuje podstawę ADR.
- Długości A/B/C: **93/111/99** znaków. Poprawna odpowiedź nie jest najdłuższa.
- Status: `needs_review`; nie zmieniono żadnego statusu na `verified`.

## Podstawa prawna

- ADR 2025, **5.4.1.1.3.1** — prawidłową nazwę przewozową odpadu zawierającego towary niebezpieczne (innego niż odpad promieniotwórczy) poprzedza się słowem „ODPAD”, chyba że termin ten jest już częścią nazwy przewozowej.
- ADR 2025, **5.4.1.1.1** — wymagane informacje w dokumencie przewozowym.
- ADR 2025, **1.4.2.2.3** — przewoźnik nie powinien rozpoczynać przewozu, gdy stwierdzone naruszenie wymagań nie zostało usunięte.
- Źródło urzędowe: ADR 2025, Dz.U. 2025 poz. 642; polski tom I udostępniony przez Ministerstwo Infrastruktury: https://www.gov.pl/web/infrastruktura/towary-niebezpieczne . Strona MI zaznacza, że pliki ADR mają charakter pomocniczy, a źródłem prawa jest Umowa ADR ogłoszona w Dzienniku Ustaw.

Pytanie nie sugeruje, że kierowca sam klasyfikuje odpad lub ma prawo samodzielnie uzupełniać opis przewozowy. Karta przekazania odpadu i dokument ADR pełnią różne funkcje. Pełne literalne porównanie pytania z urzędowym polskim tekstem oraz niezależna recenzja specjalisty pozostają otwarte.

## Synchronizacja #646

- Bank: **680** pytań ADR-B-0001–0680; SHA: `56f7aecb9962752407e5381e30f2d68f2fb3f0d8`.
- Kompetencja K02 ma 5 pytań; moduł ADR-B-03 ma 54 pytania.
- Zaktualizowano warianty i klucze egzaminów próbnych 001–005 do aktualnego SHA; zachowano dotychczasowe zestawy 30 pytań i kolejność odpowiedzi.
- Dodano snapshot sekwencyjny `review/sequential/680-680.json` i snapshot prawny `review/legal-clauses/680-680.json`.
- Dopisano ADR-B-0680 do rejestru źródeł prawnych, indeksu specjalisty i obu manifestów. Odświeżono obie kolejki priorytetowe oraz SHA w historycznym manifeście próbki.

## Metryki po dodaniu pytania

- Bank: **680** pytań; wszystkie `needs_review`, **0 verified**.
- Rozkład poprawnych odpowiedzi: **A=233, B=231, C=216**.
- Poprawna odpowiedź jest jedyną najdłuższą w **72/680 = 10,59%** rekordów (limit projektu: 18%).
- Liczebność modułu ADR-B-03: **54** pytania.

## Testy i status

Zmiana jest ograniczona do kursu podstawowego. Zaktualizowano testy regresyjne liczebności banku i mapy pokrycia; wymagany pełny PASS Quality Gate na PR przed scaleniem. Status prawny pozostaje roboczy i nie stanowi zatwierdzenia przez specjalistę.
