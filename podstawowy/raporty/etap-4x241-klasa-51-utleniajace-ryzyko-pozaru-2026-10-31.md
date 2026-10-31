# Etap 4x241 — klasa 5.1: utleniacz i ryzyko pożaru sąsiedniego ładunku

Data: 31.10.2026. Zakres: wyłącznie kurs podstawowy ADR. Punkt wyjścia: świeży `main` `9f239c8ac957826c470fcedf7ee59c070409f595`, bank 665 pytań, ostatnie ID ADR-B-0665.

## 1. Luka pokrycia

Kompetencja ADR-B-02-K07 („Klasa 5.1: materiały utleniające”) miała cztery pytania: ADR-B-0044, 0156, 0266 i 0270. Trzy sprawdzały definicję lub ogólne rozpoznanie właściwości utleniających, a jedno rozpoznanie nalepki. Brakowało scenariusza praktycznego pokazującego, dlaczego utleniacz jest zagrożeniem także wtedy, gdy sam nie płonie.

## 2. Nowe pytanie ADR-B-0666

Dodano ADR-B-0666 do ADR-B-02-K07. Scenariusz: podczas załadunku zaczyna palić się sąsiedni karton, a pracownik błędnie uznaje, że niepłonący ładunek 5.1 jest obojętny. Kursant ma rozpoznać, że materiał klasy 5.1 może spowodować lub nasilić spalanie innego materiału, i uwzględnić klasę w informacji przekazywanej ratownikom.

| Opcja | Długość | Ocena |
|---|---:|---|
| A | 166 | **Poprawna** — utleniacz nie musi sam być palny, ale może nasilać spalanie innego ładunku; należy przekazać informację o klasie i stosować instrukcje awaryjne. |
| B | 166 | Błędna — myli brak własnego płomienia z brakiem wpływu na pożar. |
| C | 138 | Błędna — myli klasę 5.1 z samopalnością i proponuje niebezpieczne ręczne przenoszenie przesyłki. |

Explanation: 479 znaków, 4 zdania. Prawidłowa A ma długość równą B i nie jest jedyną najdłuższą.

## 3. Podstawa prawna i źródła

- ADR 2025, 2.2.51.1.1 — materiały klasy 5.1 nie muszą same być palne, ale mogą, zwykle przez wydzielanie tlenu, powodować lub nasilać spalanie innych materiałów.
- ADR 2025, 5.4.3.4 — określa wzór instrukcji pisemnych przewożonych w kabinie i wykorzystywanych w razie wypadku lub sytuacji awaryjnej.
- Tekst ADR 2025 UNECE: https://unece.org/adr-2025-files — tekst angielski punktów 2.2.51.1.1 i 5.4.3.4 sprawdzony.
- Akt ogłoszony: Dz.U. 2025 poz. 642 — https://dziennikustaw.gov.pl/DU/2025/642.
- Ministerstwo Infrastruktury publikuje polskie tomy ADR 2025 jako materiały pomocnicze i wskazuje, że źródłem prawa jest tekst ogłoszony w Dzienniku Ustaw: https://www.gov.pl/web/infrastruktura/towary-niebezpieczne.

Ograniczenie: pełne literalne porównanie polskiego tekstu ogłoszonego w Dz.U. i niezależna recenzja specjalisty ADR pozostają otwarte. Pytanie nie zaleca doboru środka gaśniczego ani samodzielnego przemieszczania ładunku.

## 4. Materiały i synchronizacja

- Mapa: ADR-B-0666 przypisano do ADR-B-02-K07; kompetencja ma teraz 5 pytań.
- Lekcja i materiał instruktora ADR-B-02: dodano scenariusz utleniacza klasy 5.1 przy pożarze sąsiedniego ładunku oraz ćwiczenie na fikcyjnym planie załadunku.
- Bank: 666 rekordów ADR-B-0001–0666, ID ciągłe i unikalne; wszystkie `needs_review`, 0 `verified`.
- Blob SHA banku: `b7b582add191eace25bf493fed5f71dda55f392e`.
- Rozkład prawidłowych odpowiedzi A/B/C: 229/224/213.
- „Poprawna odpowiedź jest jedyną najdłuższą”: 72/666 = 10,81%; maksimum działu 13,95% (poniżej progu 18%).
- Warianty i klucze egzaminów próbnych 001–005 wskazują nowy SHA.
- Snapshoty: `review/sequential/666-666.json`, `review/legal-clauses/666-666.json`.
- Ledger: `review/legal-polish/stage4w4-literal-verification-ledger-0610-0666.json`; kolejki główna i zagnieżdżona, oba manifesty, indeks specjalisty i lista pozycji bez cytatu MI zsynchronizowane.

## 5. Walidacja

Przed PR ręcznie sprawdzono strukturę JSONL, liczbę rekordów, ciągłość i unikalność ID, statusy, przypisanie kompetencji, długość explanation, długości A/B/C, rozkład odpowiedzi, wskaźnik „poprawna = najdłuższa”, snapshoty i SHA egzaminów. Pełny Quality Gate CI musi przejść na PR przed scaleniem. Nie deklaruję lokalnego uruchomienia testów, ponieważ w tej sesji nie mam lokalnego checkoutu repo.

ADR-B-0666 pozostaje `needs_review`; brak formalnej recenzji specjalisty. Zakres wyłącznie kurs podstawowy ADR, bez cystern.
