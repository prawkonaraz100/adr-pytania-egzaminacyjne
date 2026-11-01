# Etap 4x270 — udostępnienie dokumentów bez powrotu do strefy zagrożenia

Data: 01.11.2026  
Zakres: wyłącznie kurs podstawowy ADR  
Baza: main `7d092da5523008ab860aa27a0e299b2f9414946a`  
Gałąź: `stage4x270-safe-access-to-transport-documents`  
Nowe ID: `ADR-B-0696`  
Kompetencja: `ADR-B-05-K07` — dokumenty dla służb ratowniczych

## Wybór luki

Kompetencja miała cztery pytania (ADR-B-0109, 0185, 0229 i 0630), które powtarzały obowiązek udostępnienia dokumentów przewozowych lub informacji o ładunku ratownikom. Brakowało scenariusza pokazującego granicę tego obowiązku: dokument został w kabinie, do której zbliża się dym, a kierowca znajduje się już w bezpiecznym miejscu. Pytanie sprawdza, czy kursant przekaże ratownikom znane dane i wskaże położenie dokumentu, zamiast wracać do strefy zagrożenia.

## Dodane pytanie

- `ADR-B-0696`: po awarii dokument przewozowy pozostał w kabinie, do której zbliża się dym; przyjeżdżają ratownicy.
- Klucz: **C** — pozostać w bezpiecznym miejscu, podać znane dane i wskazać położenie dokumentu.
- Explanation: **401 znaków, 4 zdania**; wyjaśnia dostępność dokumentów, warunek bezpieczeństwa, mylące odpowiedzi i podstawę ADR.
- Długości A/B/C: **95/77/89** znaków; poprawna C jest pośrodku — nie jest ani najdłuższa, ani najkrótsza.
- Audyt A/B/C: A — błędna, bo wymaga wejścia w dym; B — błędna, bo zataja dostępne informacje; C — poprawna, bo przekazuje ratownikom dane i lokalizację dokumentu bez narażania kierowcy.
- Status: `needs_review`; nic nie oznaczono jako `verified`.

## Podstawa prawna — źródło oficjalne sprawdzone

- **ADR 2025, 5.4.3.4**, model instrukcji pisemnych, tom II, s. 270 (PDF s. 281): dokumenty przewozowe mają być łatwo dostępne dla służb ratowniczych po ich przybyciu; działania z instrukcji wykonuje się tylko, jeśli jest to możliwe i bezpieczne.
- Oficjalny polski tekst ADR 2025, Ministerstwo Infrastruktury: https://www.gov.pl/attachment/b7292c03-ac9d-4f80-9a29-c22f53d847b8
- Dz.U. 2025 poz. 642: https://dziennikustaw.gov.pl/DU/2025/642
- UNECE ADR 2025: https://unece.org/adr-2025-files

Właściwe fragmenty punktu zostały sprawdzone w oficjalnym polskim tekście ADR 2025. Pełne porównanie wszystkich elementów pytania z tekstem Dz.U. oraz niezależna recenzja specjalisty pozostają pending.

## Synchronizacja #646

- Bank po dodaniu: **696** pytań, ADR-B-0001–0696; SHA banku: `004cd974f7a402fa47407c6268ae7202b5ceb466`.
- Kompetencja `ADR-B-05-K07` otrzymała piąte pytanie.
- Klucze i warianty egzaminów próbnych 001–005 odświeżono do SHA bieżącego banku: `afaf8c6083b2057c5443f38f30f0c12f0d7d5b7b`.
- Snapshoty: `review/sequential/696-696.json`, `review/legal-clauses/696-696.json`; ledger, indeks specjalisty i manifest pakietu dołączone.
- Rozkład prawidłowych odpowiedzi po dodaniu: A=237/B=240/C=219.
- Globalny wskaźnik „poprawna = jedyna najdłuższa”: **72/696 = 10,34%**.
- Quality Gate i pełne CI pozostają do potwierdzenia na PR. Lokalnego Quality Gate nie uruchamiano.

## Audyt A/B/C

| Opcja | Ocena | Uzasadnienie |
|---|---|---|
| A | Błędna | Wymaga powrotu kierowcy do kabiny objętej dymem, choć jest już w bezpiecznym miejscu. |
| B | Błędna | Nie wolno zatajać informacji, które kierowca może przekazać bez ryzyka. |
| C | Poprawna | Kierowca pozostaje w bezpiecznym miejscu, przekazuje znane dane i wskazuje dokument ratownikom. |

Raport nie stanowi niezależnej akceptacji prawnej ani zatwierdzenia pytania.
