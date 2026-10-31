# Etap 4x240 — klasa 4.2: materiały piroforyczne i samonagrzewające się

Data: 31.10.2026. Zakres: wyłącznie kurs podstawowy ADR. Punkt wyjścia: świeży `main` `ca055775d4fdd014b0b90f3351fd81b0227a0c1f`, bank 664 pytań, ostatnie ID ADR-B-0664.

## 1. Luka pokrycia

Kompetencja ADR-B-02-K05 („Klasa 4.2: materiały samonagrzewające się / samozapalne”) miała cztery pytania: ADR-B-0095, 0154, 0302 i 0621. Sprawdzały one ogólne rozpoznanie klasy lub zagrożenia, ale nie uczyły wystarczająco jasno rozróżniać materiałów piroforycznych od samonagrzewających się. Dodano pytanie o praktyczne znaczenie różnicy ilości i czasu zapłonu.

## 2. Nowe pytanie ADR-B-0665

Dodano ADR-B-0665 do ADR-B-02-K05. Scenariusz opisuje małą ilość materiału zapalającą się po kontakcie z powietrzem w ciągu kilku minut. Kursant ma rozpoznać piroforyczność i odróżnić ją od samonagrzewania oraz klasy 4.3.

| Opcja | Długość | Ocena |
|---|---:|---|
| A | 167 | Błędna — opisuje typowe zachowanie materiału samonagrzewającego się, a nie szybki zapłon małej ilości. |
| B | 166 | **Poprawna** — piroforyczne mogą zapalić się w małej ilości po kontakcie z powietrzem w ciągu pięciu minut. |
| C | 144 | Błędna — opisuje klasę 4.3, czyli wydzielanie palnego gazu w kontakcie z wodą. |

Explanation: 453 znaki, 4 zdania. Prawidłowa odpowiedź B nie jest najdłuższa. Status pozostaje `needs_review`.

## 3. Podstawa prawna i źródła

- ADR 2025, 2.2.42.1.1 — definicje materiałów piroforycznych (zapłon nawet małych ilości w kontakcie z powietrzem w ciągu pięciu minut) oraz samonagrzewających się (samoczynne nagrzewanie bez dopływu energii; zapłon zwykle w dużych ilościach i po długim czasie).
- ADR 2025, 2.2.42.1.3 — mechanizm samonagrzewania: stopniowa reakcja z tlenem wytwarza ciepło; gdy powstaje go więcej, niż jest odprowadzane, temperatura rośnie i może doprowadzić do samozapłonu.
- ADR 2025, 2.2.42.1.8(a) — materiały piroforyczne zalicza się do I grupy pakowania.
- Tekst ADR 2025 UNECE (tom I): https://unece.org/adr-2025-files — treść punktów 2.2.42.1.1, 2.2.42.1.3 i 2.2.42.1.8(a) sprawdzona.
- Akt ogłoszony: Dz.U. 2025 poz. 642 — https://dziennikustaw.gov.pl/DU/2025/642.
- Ministerstwo Infrastruktury publikuje polskie tomy ADR 2025 jako materiały pomocnicze i wyraźnie wskazuje, że źródłem prawa jest tekst ADR ogłoszony w Dzienniku Ustaw: https://www.gov.pl/web/infrastruktura/towary-niebezpieczne.

Ograniczenie: pełne literalne porównanie polskiego tekstu ogłoszonego w Dz.U. oraz niezależna recenzja specjalisty ADR pozostają otwarte. Ledger i snapshoty nie są zatwierdzeniem prawnym.

## 4. Materiały i synchronizacja

- Mapa: ADR-B-0665 przypisano do ADR-B-02-K05; kompetencja ma teraz 5 pytań.
- Lekcja i materiał instruktora ADR-B-02: dodano rozróżnienie piroforyczności i samonagrzewania, wraz z ćwiczeniem na fikcyjnych kartach klasyfikacyjnych. Nie wykonuje się prób na rzeczywistych materiałach.
- Bank: 665 rekordów ADR-B-0001–0665, ID ciągłe i unikalne; wszystkie `needs_review`, 0 `verified`.
- Blob SHA banku: `c7c55c480fa872b1ec9ea008fb1e6d049f7fae96`.
- Rozkład prawidłowych odpowiedzi A/B/C: 228/224/213.
- „Poprawna odpowiedź jest jedyną najdłuższą”: 72/665 = 10,83%; maksimum działu: 13,95% (poniżej progu 18%).
- Warianty i klucze egzaminów próbnych 001–005 zaktualizowano do bieżącego SHA banku.
- Snapshoty: `review/sequential/665-665.json`, `review/legal-clauses/665-665.json`.
- Ledger: `review/legal-polish/stage4w4-literal-verification-ledger-0610-0665.json`; kolejki główna i zagnieżdżona, manifest, indeks specjalisty i lista pozycji bez cytatu MI zostały zsynchronizowane.

## 5. Walidacja

Przed PR ręcznie sprawdzono strukturę JSONL, liczbę rekordów, ciągłość i unikalność ID, statusy, przypisanie kompetencji, długość explanation, długości A/B/C, rozkład odpowiedzi, wskaźnik „poprawna = najdłuższa”, snapshoty oraz SHA wariantów/kluczy. Pełny Quality Gate CI musi przejść na PR przed scaleniem. Nie deklaruję lokalnego uruchomienia testów, ponieważ w tej sesji nie mam lokalnego checkoutu repo.

Brak zmiany statusu prawnego: ADR-B-0665 pozostaje `needs_review`. Zakres wyłącznie kurs podstawowy ADR, bez kursu cystern.
