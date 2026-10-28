# Etap 4x115 — próbka 40, jakość dystraktorów i synchronizacja kursu

- Data: 2026-10-28.
- Punkt wyjścia: `main` `033ce0df135451dc50836c6602f1eb4ac5b15625`, bank blob SHA `04d7246d074d6f12fc46e91b4b47fc0e2364f0f0`.
- Bank po redakcji: 609 pytań, blob SHA `5d902f8ceae765eb7cd2da1a89982667f01d7ce5`; wszystkie statusy `needs_review`.
- Zakres: wyłącznie kurs podstawowy ADR.

## 1. Próba i powtarzalność

Seed: `41152026`; LCG + Fisher–Yates. Pula po wykluczeniu 503 ID zapisanych w manifestach etapów 4x107–4x114 liczyła 106 pytań. Wylosowano 40 unikalnych ID, nieobecnych w zarejestrowanych próbkach tych etapów.

ID próbki: `ADR-B-0591`, `ADR-B-0466`, `ADR-B-0518`, `ADR-B-0504`, `ADR-B-0065`, `ADR-B-0289`, `ADR-B-0442`, `ADR-B-0185`, `ADR-B-0040`, `ADR-B-0397`, `ADR-B-0531`, `ADR-B-0134`, `ADR-B-0217`, `ADR-B-0424`, `ADR-B-0091`, `ADR-B-0177`, `ADR-B-0340`, `ADR-B-0402`, `ADR-B-0101`, `ADR-B-0405`, `ADR-B-0404`, `ADR-B-0275`, `ADR-B-0272`, `ADR-B-0368`, `ADR-B-0446`, `ADR-B-0318`, `ADR-B-0017`, `ADR-B-0264`, `ADR-B-0533`, `ADR-B-0225`, `ADR-B-0331`, `ADR-B-0357`, `ADR-B-0159`, `ADR-B-0176`, `ADR-B-0260`, `ADR-B-0229`, `ADR-B-0095`, `ADR-B-0487`, `ADR-B-0407`, `ADR-B-0279`.

Manifest z pełną listą ID wykluczonych, seedem i ograniczeniem dowodowym: [etap-4x115-wykluczenia-proby.json](etap-4x115-wykluczenia-proby.json).

## 2. Wynik przeglądu

Sprawdzono 40 pytań pod kątem zrozumiałości explanation, wiarygodności dystraktorów, jednoznaczności i zgodności z kluczem.

- **32 pytania** pozostawiono bez zmian: wyjaśnienia były już zrozumiałe i zawierały sens odpowiedzi, typową pomyłkę oraz podstawę ADR.
- **8 pytań** miało potwierdzone słabości dystraktorów; poprawiono **16 błędnych opcji** oraz wyjaśnienia. W ADR-B-0264 doprecyzowano też sytuacyjny stem, aby odróżnić brak kodu tunelowego od obowiązku stosowania znaków drogowych.
- Nie zmieniono ID, poprawnych liter ani podstaw prawnych. Nie dodano pytań i nie zmieniono statusów weryfikacji.
- Zmienione explanation mają 270–401 znaków, 2–5 zdań i wprost tłumaczą, czemu mylące odpowiedzi są błędne.

| ID | Potwierdzona słabość | Co poprawiono |
|---|---|---|
| ADR-B-0065 | Dwa dystraktory o kodzie „(-)” były niepowiązane z typowymi pomyłkami. | Zastąpiono je myleniem kodu z zakazem dla kategorii E i wymogiem zgody zarządcy. |
| ADR-B-0217 | B i C nie wiązały się z realnym błędem w odczycie podwójnej cyfry. | Wprowadzono pomyłkę dotyczącą wzmocnienia zagrożenia i interpretacji dwóch cyfr jako dwóch zagrożeń. |
| ADR-B-0264 | Pytanie powtarzało definicję kodu „(-)” i miało oczywiste dystraktory. | Zmieniono na sytuację, w której znak drogowy ogranicza wjazd mimo braku przypisanego kodu tunelowego. |
| ADR-B-0446 | A i B sugerowały nieograniczony wyjątek na podstawie badania technicznego albo IMDG. | Urealniono pomyłki dotyczące daty budowy i spełnienia wymagań innej gałęzi transportu. |
| ADR-B-0185 | A i B sugerowały oczywiste utrudnianie dostępu do dokumentów. | Zmieniono na odmowę dostępu z powodu poufności i poleganie wyłącznie na pamięci mimo dostępnego dokumentu. |
| ADR-B-0424 | A i B sprowadzały wspólny załadunek do jednego niewłaściwego kryterium. | Zmieniono na mylenie czytelnego oznakowania i różnic w dokumentach z oceną dopuszczalności wspólnego załadunku. |
| ADR-B-0318 | A i C były zbyt skrajne wobec procedury klasyfikacji odpadu. | Urealniono błędy: poleganie wyłącznie na nazwie oraz wybór pozycji ogólnej bez analizy dostępnych danych. |
| ADR-B-0340 | A i C pomijały rzeczywiste kryteria klasyfikacji. | Zmieniono na mylenie dodatkowego zagrożenia środowiskowego i widocznej nalepki z kryteriami klasyfikacji. |

## 3. Synchronizacja i kontrola

- Warianty egzaminu 001–005: po 30 pytań, A/B/C = 10/10/10, bez powtórzeń; treść zmienionych opcji zsynchronizowano w wariantach 002, 003 i 005, gdzie występują ADR-B-0340, ADR-B-0065 i ADR-B-0424. Wszystkie warianty wskazują nowy bank blob SHA.
- Klucze 001–005: po 30 odpowiedzi; zachowano litery po uwzględnieniu kolejności opcji w arkuszu, zaktualizowano explanation dla zmienionych pytań i SHA źródła. Preflight potwierdził zgodność tekstu poprawnej opcji we wszystkich 150 pozycjach.
- Migawki `review/sequential/` i `review/legal-clauses/` odświeżono dla wszystkich 8 zmienionych ID. Status niezależnej recenzji i porównania urzędowego tekstu pozostaje otwarty.
- Sprawdzono 13 lekcji i 39 scenariuszy: brak nieistniejących ID i brak odwołań do pytań z niewłaściwego działu.

## 4. Quality Gate — preflight

- Bank: 609 pytań, duplikaty ID: 0; 609 `needs_review`, 0 `verified`.
- Poprawna odpowiedź jest jedyną najdłuższą: 73/609 = 11.99%; maksimum działu 14.29%.
- Najkrótsze explanation: 270 znaków; poniżej 200 znaków: 0.

| Dział | Liczba pytań | Klucz A/B/C | Poprawna jedyną najdłuższa | Min. explanation |
|---|---:|---:|---:|---:|
| ADR-B-01 | 45 | 17/17/11 | 6/45 (13.33%) | 300 |
| ADR-B-02 | 56 | 21/19/16 | 8/56 (14.29%) | 300 |
| ADR-B-03 | 49 | 16/21/12 | 5/49 (10.20%) | 300 |
| ADR-B-04 | 46 | 15/18/13 | 6/46 (13.04%) | 301 |
| ADR-B-05 | 43 | 18/14/11 | 5/43 (11.63%) | 300 |
| ADR-B-06 | 45 | 16/14/15 | 6/45 (13.33%) | 296 |
| ADR-B-07 | 48 | 18/18/12 | 6/48 (12.50%) | 304 |
| ADR-B-08 | 42 | 12/12/18 | 5/42 (11.90%) | 303 |
| ADR-B-09 | 46 | 13/15/18 | 5/46 (10.87%) | 301 |
| ADR-B-10 | 55 | 19/18/18 | 4/55 (7.27%) | 308 |
| ADR-B-11 | 43 | 12/13/18 | 6/43 (13.95%) | 270 |
| ADR-B-12 | 44 | 14/13/17 | 6/44 (13.64%) | 303 |
| ADR-B-13 | 47 | 15/15/17 | 5/47 (10.64%) | 308 |

Preflight wykonano na danych pobranych z GitHub. Testy w lokalnym checkout nie były dostępne w tym trybie pracy; scalanie wymaga pełnego PASS GitHub Actions. Nie nadano statusu `verified`.
