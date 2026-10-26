# Etap 4x44 — druga kolejka priorytetowa recenzji prawnej

Data: 2026-10-26. Punkt wyjścia main: 47df3f229c7762feeb8fcffd6964f004f7bdb2e2. Zakres: wyłącznie kurs podstawowy ADR.

## Potwierdzona potrzeba

Lista ETAP-4X24-POZYCJE-BEZ-CYTATU-MI.md ma 121 pytań bez zapisanego dosłownego fragmentu MI. Kolejka 4x40 obejmuje 20 z nich. Przygotowano drugą kolejkę 4x44 z 20 innymi ID, aby specjalista miał kolejną małą, uporządkowaną partię do porównania z urzędowym polskim tekstem ADR 2025 (Dz.U. 2025 poz. 642 i sprostowanie poz. 1575).

## Zakres kolejki

Plik: review/specialist/KOLEJKA-PRIORYTETOWA-4X44.json.

| ID | Dział | Powód priorytetu |
|---|---|---|
| ADR-B-0528 | B-01 | oznakowanie opakowania zbiorczego EQ; ADR 3.5.4.3 |
| ADR-B-0541 | B-02 | wzór nalepki klasy 2.2 |
| ADR-B-0542 | B-02 | wzór nalepki klasy 3 |
| ADR-B-0579 | B-13 | wymagane dane odbiorcy w dokumencie |
| ADR-B-0060 | B-09 | mocowanie ładunku i możliwe uszkodzenie opakowania |
| ADR-B-0319 | B-08 | typy pojazdów EX/II i EX/III |
| ADR-B-0379 | B-07 | obowiązki przewoźnika i przeciążenie |
| ADR-B-0427 | B-09 | wspólny załadunek materiałów wybuchowych |
| ADR-B-0428 | B-09 | grupy zgodności klasy 1 |
| ADR-B-0448 | B-10 | zakres wyjątku ADR 1.1.4.7.2 dla butli DOT |
| ADR-B-0473 | B-04 | połączenia elektryczne i ABS w zestawie |
| ADR-B-0495 | B-02 | definicja podklasy 1.2 |
| ADR-B-0496 | B-02 | definicja podklasy 1.3 |
| ADR-B-0498 | B-02 | definicja podklasy 1.6 |
| ADR-B-0525 | B-13 | kod tunelowy w dokumencie przewozowym |
| ADR-B-0453 | B-10 | specjalny zapis dokumentacyjny dla butli DOT |
| ADR-B-0474 | B-04 | kontrola przed załadunkiem |
| ADR-B-0482 | B-07 | obowiązki załadowcy dotyczące oznakowania |
| ADR-B-0600 | B-13 | dane nadawcy w dokumencie |
| ADR-B-0131 | B-04 | warunki zastosowania nadzoru pojazdu |

## Kontrole integralności

- Bank: 609 pytań, blob SHA 8a16afb47c5d5a9e460092b7e474b4a3e8a5a8d9.
- Lista bez cytatu MI: 121 ID.
- Kolejka 4x40: 20 ID; kolejka 4x44: 20 innych ID; brak nakładania się list.
- Każdy rekord kolejki ma zgodne z bankiem ID, dział, treść pytania i referencje źródłowe.
- Wszystkie wpisy 4x44 pozostają needs_review i official_gazette_comparison=pending; brak numerów stron i brak automatycznego zatwierdzenia.
- Łącznie kolejki obejmują 40/121 rekordów; 81 pozostaje poza obiema kolejkami.

## Metoda i ograniczenia

Priorytety to heurystyka pracy oparta na cechach treści (progi, wyjątki, klasy i oznakowanie, dokumenty, wymagania pojazdu). Nie jest to twierdzenie, że którekolwiek pytanie jest błędne. Nie zmieniono banku, odpowiedzi ani statusów; nie dodano verified. Każdy rekord wymaga sprawdzenia wszystkich opcji A/B/C, explanation i podstawy przez specjalistę na podstawie wiążącego polskiego tekstu.