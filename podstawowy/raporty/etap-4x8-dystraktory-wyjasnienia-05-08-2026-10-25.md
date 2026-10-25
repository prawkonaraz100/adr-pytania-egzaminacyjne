# Etap 4x8 — jakość dystraktorów i wyjaśnień, B-05–08

## Zakres
- Punkt wyjścia: świeży `main` `e2d6e09d073227f25c33ac9a71d30f4bc4de86bb`.
- Sprawdzono 178 pytań w modułach B-05–B-08 (B-05: 43, B-06: 45, B-07: 48, B-08: 42).
- Kontrola skryptowa długości wyjaśnień, długości zdań, początku od przepisu i oczywistych formuł odpowiedzi wykryła jeden wyraźny dystraktor do poprawy. Pozostałe wyjaśnienia w tych modułach spełniają minimum 300 znaków i już odnoszą się do błędnych odpowiedzi.

## Potwierdzona poprawka
- **ADR-B-0220** — zastąpiono oczywisty dystraktor „kolor kabiny” dwoma wiarygodnymi błędami: podaniem wyłącznie telefonu firmy albo samego numeru UN bez informacji o lokalizacji i okolicznościach. Zachowano ID i poprawną literę A. Explanation tłumaczy, że te dane mogą być przydatne, ale nie zastępują opisu zdarzenia. Podstawa: ADR 5.4.3.4.
- Zsynchronizowano migawki w `review/sequential/219-228.json` i `review/legal-clauses/219-228.json`; status pozostaje `needs_review`.
- Klucze egzaminów 001–005 nie wymagają zmiany.

## Uzupełnienia lekcji
Dodano „Najczęstsze błędy kursantów” do B-05–B-08:
- B-05: alarmowanie, rozpoznawanie wycieku, samodzielne gaszenie i użycie dokumentów.
- B-06: numer UN a klasa, nalepki a duże znaki, tablice pomarańczowe i kompletność oznakowania.
- B-07: obowiązki uczestników, uszkodzone opakowania, szkolenie do zadań i polecenia przełożonych.
- B-08: dobór gaśnic, pojemność, dostępność wyposażenia i dokumenty pojazdu.
Każda sekcja odsyła do słowniczka i wskazuje podstawę ADR.

## Lista sprawdzonych pytań
Wszystkie rekordy, których `module_id` to ADR-B-05, ADR-B-06, ADR-B-07 lub ADR-B-08 (178 ID; bez zmiany numeracji).

## Preflight Quality Gate
- Bank: 609 pytań; duplikaty ID: 0.
- „Poprawna odpowiedź jest jedyną najdłuższą”: 82/609 = 13.46% (limit 18%).
- Najkrótsze explanation: 300 znaków; poniżej 200 znaków: 0.
- Status: 609 `needs_review`, 0 `verified`.
- Nie zmieniono poprawnych liter ani nie oznaczono pytań jako `verified`.

## Ograniczenia
Heurystyki wskazują kandydatów, a nie potwierdzają prawnej poprawności. Zmieniono tylko jedno potwierdzone dydaktycznie pytanie; pełna recenzja prawna specjalisty nadal jest wymagana.