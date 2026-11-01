# Etap 4x266 — ponowna ocena strony nawietrznej po zmianie wiatru

Data: 01.11.2026  
Zakres: wyłącznie kurs podstawowy ADR  
Baza: main `d56bc0431c08bd1a550a6ecd79f7bb4cdb315869`  
Gałąź: `stage4x266-wind-direction-change`  
Nowe ID: `ADR-B-0692`  
Kompetencja: `ADR-B-05-K04` — unikanie oparów i wybór strony nawietrznej

## Wybór luki

Kompetencja miała cztery pytania. Trzy sprawdzały głównie statyczne rozpoznanie strony nawietrznej przy niezmiennym kierunku wiatru; czwarte dotyczyło bezpiecznego ograniczania odpływu. Brakowało sytuacji, w której warunki zmieniają się już po oddaleniu od wycieku. Nowe pytanie sprawdza, czy kierowca ponownie oceni położenie chmury i przemieści się tak, aby nadal pozostawać po stronie nawietrznej.

## Dodane pytanie

- `ADR-B-0692`: po oddaleniu się od wycieku wiatr zmienia kierunek, a chmura oparów zaczyna przesuwać się w stronę kierowcy.
- Klucz: **B** — ponownie oddalić się i znaleźć miejsce po stronie nawietrznej, poza drogą przemieszczania się oparów.
- Explanation: **309 znaków, 4 zdania**; prosty opis praktycznej decyzji, mylących odpowiedzi i podstawy ADR.
- Długości A/B/C: **118/101/77** znaków; poprawna B nie jest ani najdłuższa, ani najkrótsza.
- Audyt A/B/C: A — błędna, bo dotychczasowe miejsce po zmianie wiatru może znaleźć się w drodze chmury; B — poprawna, bo utrzymuje kierowcę po stronie nawietrznej; C — błędna, bo kieruje go za chmurę, w obszar przemieszczania się oparów.
- Status: `needs_review`; nic nie oznaczono jako `verified`.

## Podstawa prawna — źródło oficjalne sprawdzone

- **ADR 2025, 5.4.3.4**, model instrukcji pisemnych, tom II, s. 270 (PDF s. 281): należy unikać wdychania oparów, dymu, pyłu i pary przez pozostawanie po stronie nawietrznej.
- Oficjalny polski tekst ADR 2025, Ministerstwo Infrastruktury: https://www.gov.pl/attachment/b7292c03-ac9d-4f80-9a29-c22f53d847b8
- Dz.U. 2025 poz. 642: https://dziennikustaw.gov.pl/DU/2025/642
- UNECE ADR 2025: https://unece.org/adr-2025-files

Właściwy fragment punktu został sprawdzony bezpośrednio w oficjalnym polskim PDF. Pełne porównanie wszystkich elementów pytania z tekstem Dz.U. oraz niezależna recenzja specjalisty pozostają pending.

## Synchronizacja #646

- Bank po dodaniu: **692** pytań, ADR-B-0001–0692; SHA banku zostanie wpisany po zatwierdzeniu commitu.
- Kompetencja `ADR-B-05-K04` otrzymała piąte pytanie.
- Klucze i warianty egzaminów próbnych 001–005 wymagają odświeżenia do nowego SHA banku.
- Snapshoty: `review/sequential/692-692.json`, `review/legal-clauses/692-692.json`; ledger, indeks specjalisty i manifest pakietu dołączone.
- Rozkład prawidłowych odpowiedzi po dodaniu: A=236/B=238/C=218.
- Globalny wskaźnik „poprawna = jedyna najdłuższa”: **72/692 = 10,40%**; maksimum działu pozostaje 13,95%.
- Quality Gate i pełne CI pozostają do potwierdzenia na PR. Lokalnego Quality Gate nie uruchamiano.

## Audyt A/B/C

| Opcja | Ocena | Uzasadnienie |
|---|---|---|
| A | Błędna | Po zmianie kierunku wiatru wcześniejsze miejsce może już nie być nawietrzne. |
| B | Poprawna | Ponowne odejście na stronę nawietrzną ogranicza ryzyko wdychania oparów. |
| C | Błędna | Przejście za chmurę prowadzi w obszar przemieszczania się oparów. |

Raport nie stanowi niezależnej akceptacji prawnej ani zatwierdzenia pytania.
