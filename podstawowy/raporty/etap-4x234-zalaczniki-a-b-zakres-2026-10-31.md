# Etap 4x234 — zakres załączników A i B ADR

Data: 31.10.2026. Zakres: wyłącznie kurs podstawowy ADR. Punkt wyjścia: świeży `main` `867ba9110bd71cb95999537c17a541a0657769d6`, bank 658 pytań, blob SHA `9b107642362dc3871d4434304dbfaba14ab3d3b6`.

## 1. Audyt luki

Kompetencja ADR-B-01-K01 „Ramy prawne i definicje ADR” miała cztery pytania: definicję towarów niebezpiecznych, jednostkę transportową, zakres pojęcia przewozu oraz miejsce szukania wymagań dotyczących załogi i pojazdu. Brakowało prostego rozróżnienia ogólnego zakresu załączników A i B, przydatnego przy szukaniu właściwych wymagań.

## 2. Nowe pytanie ADR-B-0659

Dodano ADR-B-0659 do ADR-B-01-K01. Scenariusz dotyczy przewoźnika, który musi ustalić, gdzie szukać wymagań dotyczących opakowania i oznakowania towaru, a gdzie zasad dotyczących pojazdu i pracy załogi.

| Opcja | Długość | Ocena |
|---|---:|---|
| A | 107 | **Poprawna** — załącznik A dotyczy towarów i warunków przewozu, załącznik B pojazdów i operacji transportowych. |
| B | 159 | Błędna — odwraca zakres załączników A i B. |
| C | 159 | Błędna — błędnie ogranicza A do listy UN, a wymagania o towarach przenosi do B. |

Poprawna odpowiedź A nie jest najdłuższa. Explanation ma 426 znaków i 4 zdania: wyjaśnia zakres obu załączników, podaje przykłady, pokazuje praktyczną wskazówkę i kończy podstawą ADR. Status: `needs_review`.

## 3. Źródła i zakres prawny

- Umowa ADR, art. 2 — międzynarodowy przewóz podlega warunkom z załącznika A dla towarów oraz z załącznika B dla pojazdu i warunków jego używania.
- ADR 2025, 1.1.1 — struktura i zakres załączników. Annex A obejmuje przepisy ogólne oraz przepisy dotyczące niebezpiecznych przedmiotów i substancji; Annex B dotyczy wyposażenia transportowego i operacji transportowych.
- Ogłoszenie polskiego tekstu ADR 2025: Dz.U. 2025 poz. 642 — https://dziennikustaw.gov.pl/DU/2025/642
- Oficjalny opis ADR 2025 i podziału załączników A/B: UNECE, https://unece.org/transport/dangerous-goods/about-adr oraz https://unece.org/adr-2025-files
- Ministerstwo Infrastruktury udostępnia polskie tomy ADR 2025 i wskazuje, że źródłem prawa jest tekst ogłoszony w Dzienniku Ustaw: https://www.gov.pl/web/infrastruktura/towary-niebezpieczne

Pełne literalne porównanie polskiego tekstu urzędowego i niezależna recenzja specjalisty ADR pozostają otwarte. Pytanie sprawdza ogólny podział zakresu; nie zastępuje wyszukania konkretnego przepisu w odpowiedniej części ADR.

## 4. Materiały i synchronizacja

- Mapa: ADR-B-0659 przypisano do ADR-B-01-K01 (5 pytań w kompetencji).
- Lekcja i materiał instruktora ADR-B-01: dodano rozróżnienie zakresu załączników i ćwiczenie wyszukiwania wymagań.
- Bank: 659 rekordów ADR-B-0001–0659, ID ciągłe i unikalne; wszystkie `needs_review`, 0 `verified`.
- Blob SHA banku: `edef07df45541eeea77726bb1d6f93d00d853627`.
- Rozkład prawidłowych odpowiedzi: A=227, B=220, C=212.
- Wskaźnik „poprawna odpowiedź jest jedyną najdłuższą”: 72/659 = 10,93%; maksimum działu 13,95%.
- Warianty i klucze egzaminów próbnych 001–005 wskazują nowy blob SHA banku.
- Snapshoty dodano jako `review/sequential/659-659.json` i `review/legal-clauses/659-659.json`.
- Ledger rozszerzono do `review/legal-polish/stage4w4-literal-verification-ledger-0610-0659.json`; manifesty 0628/0638, kolejki i rejestr pozycji bez cytatu zaktualizowano do 659 rekordów.

## 5. Walidacja i ograniczenia wykonania

Ręcznie sprawdzono strukturę JSONL, ciągłość i unikalność ID, statusy, przypisanie kompetencji, rozkład odpowiedzi, długości A/B/C i explanation oraz synchronizację egzaminów, snapshotów i manifestów. Lokalny checkout i terminal repo nie były dostępne w tej sesji, więc lokalnego PASS nie deklaruję. Pełny Quality Gate CI na PR jest obowiązkową bramką przed scaleniem.

Nie zmieniono statusów prawnych; pytanie pozostaje `needs_review`. Zakres wyłącznie kurs podstawowy ADR, bez kursu cystern.
