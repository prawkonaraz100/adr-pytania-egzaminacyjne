# Etap 4x255 — ochrona kanalizacji: dodatkowe wyposażenie ADR

Data: 31.10.2026  
Zakres: wyłącznie kurs podstawowy ADR  
Baza: main po PR #724, bank 680 pytań; nowy ID: ADR-B-0681  
Kompetencja: ADR-B-03-K04 — ochrona kanalizacji i wód podczas wypadku

## Dlaczego wybrano tę lukę

Mapa wskazywała cztery pytania w K04, ale dotychczasowe pozycje koncentrowały się na ogólnej zasadzie bezpiecznego reagowania na wyciek. Brakowało sprawdzenia, czy kursant zna konkretne dodatkowe wyposażenie przewidziane dla towarów oznakowanych nalepką 8, potrzebne do ograniczenia skutków wycieku i ochrony odpływów.

## Dodane pytanie

- **ADR-B-0681** — pojazd przewozi towar ADR oznakowany nalepką nr 8; kursant wskazuje wymagane dodatkowe wyposażenie.
- Klucz: **A** — łopata, osłona kanalizacyjna i pojemnik do zebrania pozostałości.
- Explanation: **325 znaków, 4 zdania**; wyjaśnia praktyczny cel zestawu, odróżnia go od gaśnicy i płynu do płukania oczu oraz przypomina o sprawdzeniu wyposażenia przed wyjazdem.
- Długości A/B/C: **65/66/72** znaków. Poprawna odpowiedź nie jest najdłuższa.
- Status: needs_review; niczego nie oznaczono jako verified.

## Podstawa i ograniczenia

- ADR 2025, **8.1.5.2** — dodatkowe wyposażenie wymagane dla towarów oznakowanych nalepkami 3, 4.1, 4.3, 8 i 9; dla nalepki 8 obejmuje łopatę, osłonę kanalizacyjną i pojemnik do zbierania pozostałości.
- ADR 2025, **5.4.3.4** — działania załogi w razie wypadku lub awarii należy podejmować tylko wtedy, gdy jest to bezpieczne i wykonalne.
- Źródło prawa: ADR 2025 ogłoszony w Dz.U. 2025 poz. 642: https://dziennikustaw.gov.pl/DU/2025/642 .
- Pomocnicze potwierdzenie odczytu wykazu wyposażenia: oficjalne wytyczne brytyjskiego Department for Transport: https://www.gov.uk/government/publications/adr/adr-instructions-in-writing . Nie zastępują one polskiego źródła prawa.

Dokładny polski tekst ustępu 8.1.5.2 nie został pobrany i porównany literalnie; pełne porównanie pytania A/B/C oraz niezależna recenzja specjalisty pozostają otwarte. Pytanie nie zachęca kierowcy do podejmowania działań ratowniczych za wszelką cenę.

## Synchronizacja #646 — stan po dodaniu pytania

- Bank: **681** pytań ADR-B-0001–0681; wszystkie needs_review, 0 verified.
- Blob SHA `12a8dd403a927c9995348124e4a3e67e4a63ac00`.
- Rozkład A/B/C: **234/231/216**; „poprawna = jedyna najdłuższa”: **72/681 = 10,57%**, poniżej Quality Gate 18%.
- Zaktualizowano mapę kompetencji, lekcję i materiał instruktora B-03, snapshoty sequential/legal oraz ledger źródeł. Synchronizacja egzaminów 001–005 i pakietu recenzyjnego następuje w kolejnym commicie.
