# Etap 4x249 — klasa 4.3: znaczenie I grupy pakowania

Data: 31.10.2026. Zakres: wyłącznie kurs podstawowy ADR. Punkt wyjścia: świeży main po scaleniu PR #717, commit `d7f348dcd5b4fcd454226d2d4e205c69eef0f4e6`, bank 673 pytania. Kolejne wolne ID: ADR-B-0674.

## 1. Luka pokrycia

Kompetencja ADR-B-02-K06 (klasa 4.3: reagujące z wodą) miała pięć pytań, ale skupiały się one głównie na rozpoznaniu klasy, nalepce 4.3 i zakazie polewania wycieku wodą. Brakowało pytania o odczyt grupy pakowania i jej znaczenie dla stopnia zagrożenia. Jest to praktyczna luka przy sprawdzaniu dokumentu przewozowego: kierowca powinien rozumieć, że grupa I oznacza duże zagrożenie, a nie rodzaj opakowania.

Przegląd Issue #10 dla etapów 4x227–4x248 nie wykazał wcześniejszego etapu poświęconego temu konkretnemu zagadnieniu klasy 4.3.

## 2. Nowe pytanie ADR-B-0674

Kierowca sprawdza dokument przewozowy materiału klasy 4.3 i widzi I grupę pakowania. Pytanie sprawdza, czy rozumie, że grupa I oznacza duże zagrożenie, a kryteria dla klasy 4.3 odnoszą się do energicznej reakcji z wodą i skłonności wydzielanego gazu do samozapłonu albo do bardzo szybkiego wydzielania gazu palnego.

| Opcja | Długość | Ocena |
|---|---:|---|
| A | 133 | Błędna — opisuje raczej słabszą reakcję, a nie kryteria I grupy pakowania. |
| B | 137 | **Poprawna** — I grupa oznacza duże zagrożenie; kryteria klasy 4.3 obejmują energiczną reakcję z wodą i możliwość samozapłonu gazu lub jego bardzo szybkie wydzielanie. |
| C | 147 | Błędna — grupa pakowania opisuje stopień zagrożenia, a nie rodzaj opakowania; nie można jej zastąpić samą nalepką klasy. |

Explanation: 350 znaków, 3 zdania. Najpierw wyjaśnia, dlaczego grupa I oznacza duże zagrożenie i jakie są kryteria klasy 4.3; następnie odróżnia grupę III i wyjaśnia, że grupa pakowania nie jest typem opakowania; na końcu wskazuje podstawę ADR. Poprawna B nie jest najdłuższą odpowiedzią.

## 3. Podstawa prawna i ograniczenia

- ADR 1.2.1 — definicja grupy pakowania i znaczenie: I = duże zagrożenie, II = średnie zagrożenie, III = małe zagrożenie.
- ADR 2.2.43.1.8(a) — I grupa pakowania dla klasy 4.3: materiał reaguje z wodą energicznie i gaz ma tendencję do samozapłonu albo reaguje łatwo z wodą, wydzielając gaz palny z szybkością co najmniej 10 l/kg w ciągu minuty.
- ADR 2.2.43.1.8(b)–(c) — kryteria grup II i III, oparte na szybkości wydzielania gazu palnego.

Brzmienie punktów sprawdzono w polskim ADR 2025 udostępnionym przez Ministerstwo Infrastruktury. MI zastrzega, że pliki PDF mają charakter pomocniczy, a źródłem prawa jest ADR ogłoszony w Dzienniku Ustaw (Dz.U. 2025 poz. 642). Literalne porównanie pytań i opcji z wiążącym tekstem Dz.U. oraz niezależna recenzja specjalisty pozostają otwarte.

Pytanie nie wymaga od kierowcy samodzielnego klasyfikowania materiału ani wykonywania prób z wodą. Dotyczy odczytu grupy pakowania już wskazanej w dokumentacji. Pytanie ma status `needs_review`; nie oznaczono go jako `verified`.

## 4. Kontrola banku

- Liczba pytań: 674; ID ADR-B-0001–ADR-B-0674 ciągłe i unikalne.
- Status: 674 `needs_review`, 0 `verified`.
- Blob SHA `questions.jsonl`: `841c502032f62580f23608820747827f70b00df0`.
- Rozkład poprawnych opcji: A=231, B=230, C=213.
- „Poprawna odpowiedź jest jedyną najdłuższą”: 72/674 = 10,68%; maksimum działu 13,95%.
- Kompetencja ADR-B-02-K06 została uzupełniona o ADR-B-0674; dział ADR-B-02 ma 77 pytań.

## 5. Synchronizacja

- Warianty i klucze egzaminów próbnych 001–005 wskazują SHA aktualnego banku.
- Dodano snapshoty `review/sequential/674-674.json` i `review/legal-clauses/674-674.json`.
- Dodano ADR-B-0674 do ledgeru literalnej weryfikacji i rejestru specjalisty.
- Zaktualizowano manifesty, kolejki recenzyjne, README, mapę pokrycia, lekcję, materiały instruktora i testy regresyjne.

Zmiana jest przygotowana na gałęzi `stage4x249-class43-packing-group-hazard-level`, utworzonej od świeżego main. Lokalny checkout nie był dostępny; wymagany jest PASS pełnego Quality Gate na PR przed scaleniem.
