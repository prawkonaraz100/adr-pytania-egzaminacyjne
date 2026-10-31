# Etap 4x237 — zgodność VIN w świadectwie dopuszczenia pojazdu

Data: 31.10.2026. Zakres: wyłącznie kurs podstawowy ADR. Punkt wyjścia: świeży `main` `e86984561a3e2078cb373267e3c1a02f88c2bf6a`, bank 661 pytań, blob SHA `d7ad9711a2e5f5ced552ff6a4140455104536280`.

## 1. Audyt luki

Kompetencja ADR-B-08-K08 „Wyposażenie techniczne i wymagania pojazdu” zawierała siedem pytań. Sprawdzały one przede wszystkim typy pojazdów EX/II, EX/III, FL, AT i MEMU, obowiązek posiadania świadectwa oraz jego dostępność i ważność. Brakowało praktycznej kontroli, czy dane świadectwo odnosi się do tego konkretnego pojazdu, który kierowca ma prowadzić. To istotna różnica: świadectwo dla innego pojazdu tej samej firmy lub tego samego typu nie potwierdza zgodności kontrolowanego egzemplarza.

## 2. Nowe pytanie ADR-B-0662

Dodano ADR-B-0662 do ADR-B-08-K08. Scenariusz: kierowca porównuje świadectwo dopuszczenia z pojazdem i zauważa, że numer VIN w polu 3 różni się od numeru na tabliczce identyfikacyjnej, mimo zgodności typu pojazdu i przewoźnika. Poprawna decyzja to wstrzymanie wyjazdu ADR, wyjaśnienie rozbieżności i uzyskanie świadectwa dotyczącego właściwego pojazdu.

| Opcja | Długość | Ocena |
|---|---:|---|
| A | 144 | Błędna — traktuje świadectwo jak dokument zamienny dla całej floty o tym samym typie. |
| B | 130 | **Poprawna** — każe wstrzymać wyjazd i uzyskać świadectwo odnoszące się do konkretnego pojazdu. |
| C | 129 | Błędna — uznaje zgodność numeru rejestracyjnego za wystarczającą mimo innego VIN. |

Poprawna odpowiedź B nie jest ani najdłuższa, ani najkrótsza. Explanation ma 438 znaków i 4 zdania: najpierw wyjaśnia, dlaczego rozbieżność VIN uniemożliwia użycie dokumentu, potem wskazuje mylące założenia, a na końcu podaje podstawę ADR. Status: `needs_review`.

## 3. Podstawa prawna i źródła

- ADR 2025, 9.1.3.1: zgodność pojazdów wskazanych w przepisie potwierdza się świadectwem dopuszczenia wystawionym dla każdego pojazdu.
- ADR 2025, 9.1.3.3: świadectwo ma odpowiadać określonemu wzorowi.
- ADR 2025, 9.1.3.5: wzór zawiera osobne pola na numer identyfikacyjny pojazdu, numer rejestracyjny oraz oznaczenie pojazdu.
- Źródło prawa: Dz.U. 2025 poz. 642 — https://dziennikustaw.gov.pl/DU/2025/642.
- Pomocniczy polski tekst ADR 2025 opublikowany przez Ministerstwo Infrastruktury, tom II, s. 640 (strona PDF 650): https://www.gov.pl/attachment/b7292c03-ac9d-4f80-9a29-c22f53d847b8. Ministerstwo wyraźnie zastrzega, że pliki pomocnicze nie są źródłem prawa; źródłem jest tekst ogłoszony w Dzienniku Ustaw.
- Sprostowanie Dz.U. 2025 poz. 1575: https://eli.gov.pl/api/acts/DU/2025/1575/text.pdf. W sprawdzonym wykazie sprostowań nie wskazano 9.1.3.1, 9.1.3.3 ani 9.1.3.5.

Punkty 9.1.3.1, 9.1.3.3 i 9.1.3.5 sprawdzono w oficjalnym polskim materiale ADR 2025 udostępnionym przez MI. Pełne literalne porównanie z wiążącym tekstem ogłoszonym w Dzienniku Ustaw oraz niezależna recenzja specjalisty ADR pozostają otwarte. Ledger nie jest zatwierdzeniem prawnym.

## 4. Materiały i synchronizacja

- Mapa: ADR-B-0662 przypisano do ADR-B-08-K08 (8 pytań w kompetencji).
- Lekcja i materiał instruktora ADR-B-08: dodano praktyczne sprawdzenie VIN, numeru rejestracyjnego i oznaczenia pojazdu we wzorze świadectwa.
- Bank: 662 rekordy ADR-B-0001–0662, ID ciągłe i unikalne; wszystkie `needs_review`, 0 `verified`.
- Blob SHA banku: `67da7457c1494d9e770324f42a6a30ef4e117567`.
- Rozkład prawidłowych odpowiedzi: A=228, B=222, C=212.
- Wskaźnik „poprawna odpowiedź jest jedyną najdłuższą”: 72/662 = 10,88%; maksimum działu 13,95%.
- Warianty i klucze egzaminów próbnych 001–005 wskazują nowy blob SHA banku.
- Snapshoty dodano jako `review/sequential/662-662.json` i `review/legal-clauses/662-662.json`.
- Ledger rozszerzono do `review/legal-polish/stage4w4-literal-verification-ledger-0610-0662.json`; manifest i zagnieżdżone kolejki recenzyjne, rejestr pytań oraz lista 132 pozycji bez zapisanego cytatu MI zaktualizowano.

## 5. Walidacja i ograniczenia wykonania

Ręcznie sprawdzono 662 rekordy JSONL, ciągłość i unikalność ID, statusy, przypisanie kompetencji, rozkład A/B/C, długości odpowiedzi i explanation oraz zgodność SHA wariantów/kluczy, snapshotów i manifestu. Lokalny checkout i terminal repo nie były dostępne w tej sesji, więc lokalnego PASS nie deklaruję. Pełny Quality Gate CI na PR jest obowiązkową bramką przed scaleniem.

Nie zmieniono statusów prawnych; pytanie pozostaje `needs_review`. Zakres wyłącznie kurs podstawowy ADR, bez kursu cystern.
