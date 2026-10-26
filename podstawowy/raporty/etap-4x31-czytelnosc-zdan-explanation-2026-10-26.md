# Etap 4x31 — czytelność zdań w explanation i regresja jakości

- Data: 2026-10-26.
- Świeży `main` na starcie: `53fff7a6962be26ab473feb07d14a315a9c0fbee`.
- Zakres: wyłącznie kurs podstawowy ADR.

## Kontrola całego banku

Skryptowy przegląd 609 explanation użył podziału na zdania z ochroną typowych polskich skrótów (np. „m.in.”), aby nie uznawać kropki wewnątrz skrótu za koniec zdania.

- 609 explanation sprawdzonych.
- Po poprawce wszystkie explanation mają 2–5 zdań.
- Jedno zdanie przekraczało limit 35 słów: ADR-B-0540 (38 słów).
- ADR-B-0319 było fałszywym alarmem w naiwnym liczniku, ponieważ skrót „m.in.” zawiera kropki. Po prawidłowym uwzględnieniu skrótu explanation ma 5 zdań, więc nie zmieniano go.
- Po poprawce nie ma zdań dłuższych niż 35 słów ani wyjaśnień poza zakresem 2–5 zdań.

## Poprawka ADR-B-0540

**Przed:** pierwsze zdanie łączyło warunek oznakowania LQ, dwa punkty ADR i skutek dla tunelu w jednym zdaniu liczącym 38 słów.

**Po:** wyjaśnienie rozdziela warunek oznakowania, skutek dla tunelu, ograniczenie zakresu i czynność kierowcy na krótsze zdania. Zachowano sens odpowiedzi C oraz podstawę ADR 3.4.13–3.4.14 i 8.6.4. Nie zmieniano stemu, opcji, poprawnej litery ani statusu `needs_review`.

## Quality Gate

Dodano blokujący test w `tests/test_explanation_quality.py` dla całego banku:
- każde explanation ma 2–5 zdań;
- żadne zdanie nie przekracza 35 słów;
- skróty takie jak „m.in.” są chronione przed fałszywym podziałem zdań.

Test pakietu recenzyjnego zaktualizowano tak, by sprawdzał SHA aktualnego banku osobno od historycznej migawki etapu 4x29. Dzięki temu przyszła legalna zmiana banku nie udaje, że poprzedni raport korzystał z nowego snapshotu.

## Synchronizacja egzaminów i pakietu

- Bank: 609 pytań, 609 `needs_review`, 0 `verified`.
- Nowy blob SHA banku: `99c06e736c0e5812e97d4ff02567dbf741629434`.
- Warianty i klucze 001–005 zaktualizowano do nowego SHA; 150 unikalnych ID, 30 pytań na wariant, A/B/C 10/10/10, maksymalna seria 3.
- Wskaźnik „poprawna = jedyna najdłuższa”: 73/609 = 11,99%; najwyższy dział 14,29%.
- Najkrótsze explanation: 300 znaków; poniżej 200: 0.
- Manifest i przekazanie specjaliście odzwierciedlają aktualny SHA; historyczny raport 4x29 pozostaje związany z wcześniejszą migawką.

## Status formalny

Nie zmieniano statusów weryfikacji prawnej i nie oznaczono niczego jako `verified`. Testy lokalne nie były uruchamiane; wymagany jest PASS Quality Gate CI przed scaleniem.
