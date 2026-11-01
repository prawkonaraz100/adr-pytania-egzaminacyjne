# Etap 4x265 — powiadomienie służb ratowniczych bez zwłoki

Data: 01.11.2026  
Zakres: wyłącznie kurs podstawowy ADR  
Baza: main `0c4f2eccfb7e4bcdb98694694754a6793c487a94`  
Gałąź: `stage4x265-emergency-services-notification`  
Nowe ID: `ADR-B-0691`  
Kompetencja: `ADR-B-05-K03` — powiadomienie służb i informacje o ładunku

## Wybór luki

Kompetencja miała cztery pytania, które głównie sprawdzały, jakie informacje o zdarzeniu i ładunku przekazać ratownikom. Brakowało wyraźnego scenariusza decyzyjnego, w którym kierowca nie zna jeszcze przyczyny awarii, a dyspozytor przewoźnika prosi o oczekiwanie. Nowe pytanie sprawdza, czy kierowca powiadomi właściwe służby ratownicze bez odkładania zgłoszenia do czasu uzyskania zgody firmy lub pełnego wyjaśnienia zdarzenia.

## Dodane pytanie

- `ADR-B-0691`: po awarii kierowca jest w bezpiecznym miejscu, z pojazdu wydobywa się dym, a dyspozytor chce opóźnić wezwanie do czasu ustalenia przyczyny.
- Klucz: **B** — powiadomić właściwe służby ratownicze i przekazać dostępne dane o zdarzeniu oraz ładunku.
- Explanation: **391 znaków, 4 zdania**; proste wyjaśnienie praktycznej decyzji, mylących odpowiedzi i podstawy ADR.
- Długości A/B/C: **98/89/68** znaków; poprawna B nie jest ani najdłuższa, ani najkrótsza.
- Audyt A/B/C: A — błędne, bo uzależnia wezwanie służb od zgody przewoźnika; B — poprawne, bo realizuje obowiązek powiadomienia i przekazania dostępnych informacji; C — błędne, bo opóźnia zgłoszenie do zakończenia ustaleń.
- Status: `needs_review`; nic nie oznaczono jako `verified`.

## Podstawa prawna — źródło oficjalne sprawdzone

- **ADR 2025, 5.4.3.4**, model instrukcji pisemnych, tom II, s. 270 (PDF s. 281): załoga ma powiadomić właściwe służby ratownicze, przekazując możliwie wszystkie dostępne informacje o wypadku, awarii oraz towarach niebezpiecznych.
- Oficjalny polski tekst ADR 2025, Ministerstwo Infrastruktury: https://www.gov.pl/attachment/b7292c03-ac9d-4f80-9a29-c22f53d847b8
- Dz.U. 2025 poz. 642: https://dziennikustaw.gov.pl/DU/2025/642
- UNECE ADR 2025: https://unece.org/adr-2025-files

Tekst właściwego punktu został sprawdzony bezpośrednio w oficjalnym polskim PDF. Pełne porównanie wszystkich elementów pytania z tekstem Dz.U. oraz niezależna recenzja specjalisty pozostają pending.

## Synchronizacja #646

- Bank po dodaniu: **691** pytań, ADR-B-0001–0691; SHA banku: `13e6e673d26a2a97f0af2d52fd57d01dddd8f1e0`.
- Kompetencja `ADR-B-05-K03` otrzymała piąte pytanie.
- Klucze i warianty egzaminów próbnych 001–005 wymagają odświeżenia do nowego SHA banku.
- Snapshoty: `review/sequential/691-691.json`, `review/legal-clauses/691-691.json`; ledger, indeks specjalisty i manifest pakietu dołączone.
- Rozkład prawidłowych odpowiedzi po dodaniu: A=236/B=237/C=218.
- Globalny wskaźnik „poprawna = jedyna najdłuższa”: **72/691 = 10,42%**; maksimum działu pozostaje 13,95%.
- Quality Gate i pełne CI pozostają do potwierdzenia na PR. Lokalnego Quality Gate nie uruchamiano.

## Audyt A/B/C

| Opcja | Ocena | Uzasadnienie |
|---|---|---|
| A | Błędna | Wezwanie służb nie powinno zależeć od uprzedniej zgody dyspozytora przewoźnika. |
| B | Poprawna | ADR 5.4.3.4 wymaga powiadomienia właściwych służb i przekazania dostępnych informacji. |
| C | Błędna | Nie należy czekać na pełne ustalenie przyczyny i składu ładunku przed zgłoszeniem. |

Raport nie stanowi niezależnej akceptacji prawnej ani zatwierdzenia pytania.
