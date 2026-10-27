# Etap 4x70 — korekta spójności odpowiedzi ADR-B-0497

Data: 27.10.2026. Punkt bazowy: świeży `main` `9584094163ff4bebb77d266699312a2e91bb74c0`. Zakres: wyłącznie kurs podstawowy ADR.

## Potwierdzona sprzeczność

Pytanie **ADR-B-0497** pytało, czy mała wrażliwość materiałów podklasy 1.5 oznacza brak zagrożenia wybuchem masowym. Poprawna merytorycznie odpowiedź C kończyła się informacją, że zagrożenie nadal istnieje, ale zaczynała się od słowa **„Tak”** — co zaprzeczało treści pytania i własnemu dalszemu wyjaśnieniu.

ADR 2025, **2.2.1.1.5**, definiuje podklasę 1.5 jako materiały bardzo mało wrażliwe, które nadal stwarzają zagrożenie wybuchem masowym. Zatem odpowiedź na pytanie „czy niska wrażliwość oznacza brak zagrożenia?” brzmi „Nie”. Źródło prawa: [Dz.U. 2025 poz. 642 — ADR 2025](https://dziennikustaw.gov.pl/DU/2025/642), z uwzględnieniem [sprostowania Dz.U. 2025 poz. 1575](https://eli.gov.pl/eli/DU/2025/1575/ogl/pol/pdf). Pomocnicza wersja tekstu ADR 2025 jest dostępna na [portalu Ministerstwa Infrastruktury](https://www.gov.pl/web/infrastruktura/towary-niebezpieczne); źródłem prawa pozostaje tekst ogłoszony w Dzienniku Ustaw.

## Zmiana

- **Przed:** „Tak; materiały 1.5 są mało wrażliwe, ale nadal grozi im wybuch masowy”.
- **Po:** „Nie; materiały 1.5 są mało wrażliwe, ale nadal stwarzają zagrożenie wybuchem masowym”.
- Zachowano ID `ADR-B-0497`, moduł B-02, poprawną literę C, treść pytania i podstawę prawną. Explanation już tłumaczyło różnicę między małą wrażliwością a skutkami wybuchu, więc nie wymagało zmiany.
- Status pozostaje `needs_review`. To korekta potwierdzonej sprzeczności logicznej, nie formalne zatwierdzenie przez specjalistę.

## Egzaminy próbne i pakiet recenzyjny

Pytanie `ADR-B-0497` nie występuje w arkuszach 001–005, więc nie trzeba zmieniać ich pytań ani kluczy. Zaktualizowano natomiast ich metadane źródła banku, aby wszystkie wskazywały bieżący blob. Odświeżono migawkę pakietu recenzyjnego, indeks specjalisty, kolejki priorytetowe oraz migawki audytu sekwencyjnego i A/B/C dla pytania.

## Metryki preflight

- Bank: 609 pytań, duplikaty ID: 0.
- „Poprawna = jedyna najdłuższa”: 73/609 = 11.99% globalnie.
- B-02: 8/56 = 14.29%.
- Najkrótsze explanation: 300 znaków; poniżej 200: 0.
- Statusy: 609 `needs_review`, 0 `verified`.
- Warianty egzaminu 001–005 pozostają zsynchronizowane z bankiem; `ADR-B-0497` w arkuszach: nie.

## Ograniczenia

Nie zmieniono statusu prawnego żadnego pytania. Pełna niezależna recenzja tekstu urzędowego oraz A/B/C nadal jest wymagana.
