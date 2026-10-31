# Etap 4x232 — gazy palne klasy 2.1

Data: 31.10.2026. Zakres: wyłącznie kurs podstawowy ADR. Punkt wyjścia: świeży `main` `7f9e4731d3250b125cd1e7aa6e78ee0df62f81ce`, bank 656 pytań, blob SHA `940d22f1a3965796d24029e621b05253ff98ece4`.

## 1. Audyt luki

Kompetencja ADR-B-02-K02 „Klasa 2: gazy” miała cztery pytania: ogólne przypisanie gazów do klasy 2, rozpoznawanie gazu trującego 2.3 oraz dwa pytania o zieloną nalepkę 2.2. Nie było pytania sprawdzającego rozpoznanie gazu palnego 2.1. Dwa pytania o 2.2 były też zbliżone do siebie. Uzupełnienie obejmuje brakującą grupę zagrożenia 2.1 i porównuje ją z 2.2 oraz 2.3.

## 2. Nowe pytanie ADR-B-0657

Dodano ADR-B-0657 do ADR-B-02-K02. Pytanie odwołuje się do czerwonej nalepki z płomieniem i numerem 2.1; sprawdza rozpoznanie gazu palnego oraz praktyczne znaczenie ryzyka zapłonu.

| Opcja | Długość | Ocena |
|---|---:|---|
| A | 128 | **Poprawna** — gaz palny; trzeba uwzględnić ryzyko zapłonu i chronić przesyłkę przed źródłami zapłonu. |
| B | 140 | Błędna — myli klasę 2.1 z gazem niepalnym i nietrującym 2.2. |
| C | 115 | Błędna — myli klasę 2.1 z gazem trującym 2.3. |

Poprawna odpowiedź A nie jest najdłuższa ani najkrótsza. Explanation ma 356 znaków i 4 zdania: wyjaśnia ryzyko zapłonu, porównuje trzy grupy gazów i wskazuje, co kierowca powinien uwzględnić. Status: `needs_review`.

## 3. Źródła i zakres prawny

- ADR 2025, 2.2.2.1.2–2.2.2.1.5 — podział klasy 2 i kryteria dla gazów palnych, niepalnych/nietrujących oraz trujących.
- ADR 2025, 5.2.2.2.2 — wzory nalepek, w tym 2.1 (płomień na czerwonym tle), 2.2 (butla na zielonym tle) i 2.3 (czaszka na białym tle).
- Ogłoszenie: Dz.U. 2025 poz. 642 — https://dziennikustaw.gov.pl/DU/2025/642
- Sprostowanie: Dz.U. 2025 poz. 1575 — https://eli.gov.pl/api/acts/DU/2025/1575/text.pdf. Zakres sprostowania nie wskazuje przepisów 2.2.2.1 ani 5.2.2.2.2.
- Oficjalna strona Ministerstwa Infrastruktury udostępnia polskie tomy ADR 2025 i wskazuje, że źródłem prawa jest tekst ogłoszony w Dzienniku Ustaw: https://www.gov.pl/web/infrastruktura/towary-niebezpieczne

Pełne literalne porównanie polskiego tekstu urzędowego i niezależna recenzja specjalisty ADR pozostają otwarte; ledger dla 0657 nie jest zatwierdzeniem prawnym.

## 4. Materiały i synchronizacja

- Mapa: ADR-B-0657 przypisano do ADR-B-02-K02 (5 pytań w kompetencji).
- Lekcja i materiał instruktora ADR-B-02: dodano wyjaśnienie klasy 2.1 i ćwiczenie porównujące nalepki 2.1, 2.2 i 2.3.
- Bank: 657 rekordów ADR-B-0001–0657, ID ciągłe i unikalne; wszystkie `needs_review`, 0 `verified`.
- Blob SHA banku: `17633b89f1282d3dd25ddc51e81bc84b6c88c819`.
- Rozkład prawidłowych odpowiedzi: A=225, B=220, C=212.
- Wskaźnik „poprawna odpowiedź jest jedyną najdłuższą”: 72/657 = 10,96%; maksimum działu 13,95%.
- Warianty i klucze egzaminów próbnych 001–005 wskazują nowy blob SHA banku.
- Snapshoty dodano jako `review/sequential/657-657.json` i `review/legal-clauses/657-657.json`.
- Ledger rozszerzono do `review/legal-polish/stage4w4-literal-verification-ledger-0610-0657.json`; manifesty 0628/0638, kolejki i rejestr pozycji bez cytatu zaktualizowano do 657 rekordów.

## 5. Walidacja i ograniczenia wykonania

Ręcznie sprawdzono strukturę JSONL, ciągłość i unikalność ID, statusy, przypisanie kompetencji, rozkład odpowiedzi, długości A/B/C i explanation oraz synchronizację egzaminów, snapshotów i manifestów. Lokalny checkout i terminal repo nie były dostępne w tej sesji, więc lokalnego PASS nie deklaruję. Pełny Quality Gate CI na PR jest obowiązkową bramką przed scaleniem.

Nie zmieniono statusów prawnych; pytanie pozostaje `needs_review`. Zakres wyłącznie kurs podstawowy ADR, bez kursu cystern.
