# Etap 4x233 — temperatura zapłonu cieczy klasy 3

Data: 31.10.2026. Zakres: wyłącznie kurs podstawowy ADR. Punkt wyjścia: świeży `main` `44e8a20ccc70a385a03c7d712d3bcbbe9d7c7ddd`, bank 657 pytań, blob SHA `17633b89f1282d3dd25ddc51e81bc84b6c88c819`.

## 1. Audyt luki

Kompetencja ADR-B-02-K03 „Klasa 3: materiały ciekłe zapalne” miała cztery pytania. Sprawdzały ogólne przypisanie benzyny do klasy 3, reakcję na palenie papierosa podczas przeładunku oraz rozpoznawanie czerwonej nalepki z płomieniem i cyfrą 3 (dwa podobne pytania). Brakowało sprawdzenia, czy kursant rozumie pojęcie temperatury zapłonu i potrafi odróżnić je od temperatury wrzenia oraz samozapłonu.

## 2. Nowe pytanie ADR-B-0658

Dodano ADR-B-0658 do ADR-B-02-K03. Scenariusz odwołuje się do karty charakterystyki cieczy, w której podano temperaturę zapłonu 45°C. Pytanie sprawdza definicję, a nie samodzielną klasyfikację konkretnej substancji.

| Opcja | Długość | Ocena |
|---|---:|---|
| A | 142 | **Poprawna** — najniższa temperatura, przy której para cieczy może utworzyć z powietrzem mieszaninę palną; do zapłonu potrzebne jest źródło zapłonu. |
| B | 143 | Błędna — myli temperaturę zapłonu z wrzeniem i intensywnym parowaniem. |
| C | 150 | Błędna — myli temperaturę zapłonu z temperaturą samozapłonu. |

Poprawna odpowiedź A nie jest najdłuższa. Explanation ma 311 znaków i 3 zdania: najpierw wyjaśnia znaczenie parametru, potem odróżnia go od wrzenia i samozapłonu, a na końcu wskazuje podstawę ADR. Status: `needs_review`.

## 3. Źródła i zakres prawny

- ADR 2025, 1.2.1 — definicja temperatury zapłonu: najniższa temperatura cieczy, w której jej para tworzy z powietrzem mieszaninę palną.
- ADR 2025, 2.2.3.1.1 — kryteria klasy 3. Oprócz temperatury zapłonu nie wyższej niż 60°C przepis obejmuje także kryteria dotyczące stanu ciekłego i prężności pary; zawiera też wyjątki, m.in. dla określonych paliw oraz materiałów przewożonych w stanie podgrzanym.
- Ogłoszenie: Dz.U. 2025 poz. 642 — https://dziennikustaw.gov.pl/DU/2025/642
- Sprostowanie: Dz.U. 2025 poz. 1575 — https://eli.gov.pl/api/acts/DU/2025/1575/text.pdf
- Ministerstwo Infrastruktury udostępnia polskie tomy ADR 2025 i wyjaśnia, że źródłem prawa jest tekst ogłoszony w Dzienniku Ustaw: https://www.gov.pl/web/infrastruktura/towary-niebezpieczne

**Granica pytania:** wartość temperatury zapłonu sama w sobie nie wystarcza do pełnej klasyfikacji każdej cieczy. Przepis 2.2.3.1.1 zawiera dalsze kryteria, uwagi i wyjątki; przy klasyfikacji konkretnego towaru trzeba sprawdzić wszystkie właściwe warunki oraz pozycję w tabeli A. Pełne literalne porównanie polskiego tekstu urzędowego i niezależna recenzja specjalisty ADR pozostają otwarte.

## 4. Materiały i synchronizacja

- Mapa: ADR-B-0658 przypisano do ADR-B-02-K03 (5 pytań w kompetencji).
- Lekcja i materiał instruktora ADR-B-02: dodano proste omówienie temperatury zapłonu oraz ćwiczenie odróżniania jej od wrzenia i samozapłonu.
- Bank: 658 rekordów ADR-B-0001–0658, ID ciągłe i unikalne; wszystkie `needs_review`, 0 `verified`.
- Blob SHA banku: `9b107642362dc3871d4434304dbfaba14ab3d3b6`.
- Rozkład prawidłowych odpowiedzi: A=226, B=220, C=212.
- Wskaźnik „poprawna odpowiedź jest jedyną najdłuższą”: 72/658 = 10,94%; maksimum działu 13,95%.
- Warianty i klucze egzaminów próbnych 001–005 wskazują nowy blob SHA banku.
- Snapshoty dodano jako `review/sequential/658-658.json` i `review/legal-clauses/658-658.json`.
- Ledger rozszerzono do `review/legal-polish/stage4w4-literal-verification-ledger-0610-0658.json`; manifesty 0628/0638, kolejki i rejestr pozycji bez cytatu zaktualizowano do 658 rekordów.

## 5. Walidacja i ograniczenia wykonania

Ręcznie sprawdzono strukturę JSONL, ciągłość i unikalność ID, statusy, przypisanie kompetencji, rozkład odpowiedzi, długości A/B/C i explanation oraz synchronizację egzaminów, snapshotów i manifestów. Lokalny checkout i terminal repo nie były dostępne w tej sesji, więc lokalnego PASS nie deklaruję. Pełny Quality Gate CI na PR jest obowiązkową bramką przed scaleniem.

Nie zmieniono statusów prawnych; pytanie pozostaje `needs_review`. Zakres wyłącznie kurs podstawowy ADR, bez kursu cystern.
