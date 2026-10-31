# Etap 4x238 — przenośne urządzenia oświetleniowe załogi

Data: 31.10.2026. Zakres: wyłącznie kurs podstawowy ADR. Punkt wyjścia: świeży `main` `4b07c2015a8078f1cdfc02e9c9c992681798b2cb`, bank 662 pytań, blob SHA `67da7457c1494d9e770324f42a6a30ef4e117567`.

## 1. Audyt luki

Kompetencja ADR-B-07-K06 „Kierowca/załoga: obowiązki w drodze” zawierała cztery pytania. Trzy dotyczyły zakazu przewożenia pasażerów spoza załogi (ADR 8.3.1), a jedno znajomości używania gaśnic (8.3.2). Nie sprawdzały odrębnego wymogu dotyczącego przenośnego oświetlenia, który kierowca może wykorzystać podczas kontroli pojazdu po zmroku. Dodano więc scenariusz, który odróżnia zwykłą metalową latarkę mogącą wywołać iskrę od urządzenia spełniającego 8.3.4.

## 2. Nowe pytanie ADR-B-0663

Dodano ADR-B-0663 do ADR-B-07-K06. Kierowca po zmroku chce sprawdzić oznakowanie pojazdu, ale ma latarkę z metalową obudową mogącą wywołać iskrę. Pytanie sprawdza, czy kursant rozumie, że bateria, krótki czas użycia ani odsunięcie od przesyłek nie zastępują wymogu dotyczącego samego urządzenia.

| Opcja | Długość | Ocena |
|---|---:|---|
| A | 152 | Błędna — sprawna bateria i użycie poza pojazdem nie usuwają ryzyka iskry od metalowej powierzchni. |
| B | 126 | Błędna — krótki czas użycia i odsunięcie od przesyłek nie są wyjątkami od 8.3.4. |
| C | 136 | **Poprawna** — należy wybrać urządzenie, którego metalowa powierzchnia nie może spowodować iskry. |

Poprawna odpowiedź C nie jest ani najdłuższa, ani najkrótsza. Explanation ma 329 znaków i 4 zdania: wyjaśnia wymóg, wskazuje mylące założenia i podaje podstawę ADR. Status: `needs_review`.

## 3. Podstawa prawna i źródła

- ADR 2025, 8.3.4: używane przenośne urządzenie oświetleniowe nie może mieć powierzchni metalowej mogącej spowodować iskrę krzesaną.
- Źródło prawa: Dz.U. 2025 poz. 642 — https://dziennikustaw.gov.pl/DU/2025/642.
- Pomocniczy polski tekst ADR 2025 udostępniony przez Ministerstwo Infrastruktury, tom II, s. 627 (strona PDF 638): https://www.gov.pl/attachment/b7292c03-ac9d-4f80-9a29-c22f53d847b8. Na stronie 627 dział 8.3 i punkt 8.3.4 podają wymóg dotyczący metalowych powierzchni latarki. MI zastrzega, że pliki pomocnicze nie stanowią źródła prawa; źródłem jest tekst ogłoszony w Dzienniku Ustaw.
- UNECE publikuje ADR 2025 (ECE/TRANS/352) jako wydanie obowiązujące od 1 stycznia 2025 r.: https://unece.org/adr-2025-files.

Punkt 8.3.4 sprawdzono w polskim materiale ADR 2025 udostępnionym przez MI. Pełne literalne porównanie z wiążącym tekstem ogłoszonym w Dzienniku Ustaw oraz niezależna recenzja specjalisty ADR pozostają otwarte. Ledger nie jest zatwierdzeniem prawnym.

## 4. Materiały i synchronizacja

- Mapa: ADR-B-0663 przypisano do ADR-B-07-K06 (5 pytań w kompetencji).
- Lekcja i materiał instruktora ADR-B-07: dodano praktyczne ćwiczenie wyboru latarki i rozpoznawania ryzyka iskry.
- Bank: 663 rekordy ADR-B-0001–0663, ID ciągłe i unikalne; wszystkie `needs_review`, 0 `verified`.
- Blob SHA banku: `a626f744ed85432679ad0790a465eae854de9704`.
- Rozkład prawidłowych odpowiedzi: A=228, B=222, C=213.
- Wskaźnik „poprawna odpowiedź jest jedyną najdłuższą”: 72/663 = 10,86%; maksimum działu 13,95%.
- Warianty i klucze egzaminów próbnych 001–005 wskazują nowy blob SHA banku.
- Snapshoty dodano jako `review/sequential/663-663.json` i `review/legal-clauses/663-663.json`.
- Ledger rozszerzono do `review/legal-polish/stage4w4-literal-verification-ledger-0610-0663.json`; manifesty 0628/0638, zagnieżdżone kolejki, rejestr pytań oraz lista 133 pozycji bez zapisanego cytatu MI zaktualizowano.

## 5. Walidacja i ograniczenia wykonania

Ręcznie sprawdzono 663 rekordy JSONL, ciągłość i unikalność ID, statusy, przypisanie kompetencji, rozkład A/B/C, długości odpowiedzi i explanation oraz SHA wariantów/kluczy, snapshotów i manifestów. Lokalny checkout i terminal repo nie były dostępne w tej sesji, więc lokalnego PASS nie deklaruję. Pełny Quality Gate CI na PR jest obowiązkową bramką przed scaleniem.

Nie zmieniono statusów prawnych; pytanie pozostaje `needs_review`. Zakres wyłącznie kurs podstawowy ADR, bez kursu cystern.
