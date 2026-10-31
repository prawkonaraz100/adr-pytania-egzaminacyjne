# Etap 4x227 — semantyczne luki pokrycia i odróżnienie pytań podobnych

Data: 31.10.2026. Zakres: wyłącznie kurs podstawowy ADR. Punkt wyjścia: `main` `3d84e2932dd2ae6c62ccbd027bc004169f10c471`, bank 651 pytań. Stan po tej partii: 652 pytania, `ADR-B-0001`–`ADR-B-0652`. Blob SHA `questions.jsonl`: `d024eaef2d8cc404101769dc64a407675977f64b`.

## 1. Dlaczego audyt pogłębiono

Etap 4x226 nie wykazał kompetencji z 0–2 pytaniami ani działu poniżej wewnętrznego celu liczebności. Głębsza kontrola semantyczna ujawniła jednak, że sama liczba pytań może zawyżać realną różnorodność sprawdzanej wiedzy: część czteropytaniowych kompetencji zawiera głównie parafrazy jednego faktu. Dlatego w 4x227 oceniono różnorodność tego, co kursant musi rozumieć, a nie tylko liczbę rekordów.

## 2. Potwierdzona luka i nowe pytanie ADR-B-0652

Kompetencja `ADR-B-02-K12` — „Klasa 8: materiały żrące” — miała 4 pytania (`0005`, `0161`, `0267`, `0625`). Wszystkie skupiały się na ogólnym rozpoznaniu klasy i zagrożenia. Nie sprawdzały drugiego elementu definicji klasy 8: substancja może przy wycieku poważnie uszkodzić lub zniszczyć inne towary albo środek transportu, nawet gdy nie powoduje trwałego uszkodzenia skóry.

Dodano `ADR-B-0652` do `ADR-B-02-K12`. Pytanie dotyczy właśnie tej odrębnej przesłanki z ADR 2.2.8.1.1. To potwierdzona luka zakresu, a nie zwiększenie licznika bez uzasadnienia.

### Audyt odpowiedzi A/B/C

| Opcja | Długość | Ocena |
|---|---:|---|
| A | 88 znaków | **Poprawna** — definicja klasy 8 obejmuje również poważne szkody w innych towarach lub środku transportu przy wycieku. |
| B | 89 znaków | Błędna — niesłusznie ogranicza klasę 8 wyłącznie do trwałego uszkodzenia skóry. |
| C | 76 znaków | Błędna — niesłusznie przypisuje takie uszkodzenie zawsze do klasy 9. |

Poprawna odpowiedź A nie jest najdłuższa. Nowe `explanation` ma 420 znaków i 5 zdań: praktyczny sens poprawnej odpowiedzi, wyjaśnienie obu mylących wariantów i krótka podstawa ADR. Źródło wskazane w rekordzie: ADR 2025, 2.2.8.1.1, Dz.U. 2025 poz. 642. Status nowego pytania: `needs_review`; nie oznaczono go jako `verified`.

## 3. Odróżnienie pytań semantycznie podobnych

Kontrola treści wewnątrz kompetencji potwierdziła następujące powtarzalne wzorce. Nie wszystkie są duplikatami; wpis oznacza, że pytania badają bardzo zbliżoną regułę i przy dalszym rozwoju należy pilnować odrębnych aspektów.

| Kompetencja | ID / liczba | Powtarzający się motyw | Decyzja |
|---|---|---|---|
| ADR-B-06-K04 — litera X | 0017, 0170, 0256, 0615 (4) | Co oznacza X i czy można użyć wody | ADR-B-0615 doprecyzowano: woda może być użyta wyłącznie po zgodzie ekspertów; pozostałe pytania pozostawiają podstawową definicję. |
| ADR-B-02-K12 — klasa 8 | 0005, 0161, 0267, 0625 (4) | Ogólne rozpoznanie klasy 8 | Dodano ADR-B-0652 o szkodach w innych towarach/pojeździe przy wycieku. |
| ADR-B-06-K06 — powtórzenie cyfry | 0051, 0192, 0217, 0635 (4) | Powtórzona cyfra wzmacnia to samo zagrożenie | Zestaw zawiera regułę ogólną oraz przykłady 33 i 88; obserwować, by kolejne pytania badały zastosowanie, nie tylko powtarzały definicję. |
| ADR-B-06-K08 — cyfra 8 | 0053, 0194, 0298, 0637 (4) | Działanie żrące i przykłady 80/88 | Częściowe nakładanie z K06; zachować rozróżnienie znaczenia cyfry i intensyfikacji przez jej powtórzenie. |
| ADR-B-11-K04 — najbardziej restrykcyjny kod tunelowy | 0064, 0086, 0263, 0432, 0574 (5) | Wybór ograniczenia dla wielu towarów | Różne scenariusze/kody; w kolejnych partiach unikać kolejnych parafraz tej samej reguły. |
| ADR-B-05-K05 — pożar przedziału ładunkowego | 0107, 0166, 0222, 0614 (4) | Nie gasić pożaru obejmującego ładunek ADR | Powtarzalny rdzeń bezpieczeństwa; scenariusze różnią się opisem, ale nie zasadą. |
| ADR-B-05-K06 — mały pożar poza ładunkiem | 0108, 0184, 0223, 0493 (4) | Gaśnica tylko, gdy działanie jest właściwe i bezpieczne | Różne części pojazdu; nie dodawać kolejnych parafraz bez nowego aspektu. |
| ADR-B-04-K03 — silnik przy załadunku/rozładunku | 0012, 0047, 0244, 0358, 0359, 0515 (6) | Wyłączenie silnika, gdy nie napędza urządzenia | Zestaw zawiera wyjątek napędu pompy i zwykłe przypadki; pilnować rozróżnienia wyjątku. |
| ADR-B-13-K07 — dostępność instrukcji | 0090, 0216, 0228, 0590, 0620 (5) | Instrukcje w kabinie i łatwa dostępność | Różne przeszkody w dostępie (schowek, język, ukrycie); unikać powtarzania tych samych okoliczności. |

Wskaźniki semantyczne są oceną redakcyjną, nie automatycznym rozstrzygnięciem prawnym. Nie usuwano żadnego pytania.

## 4. Korekta ADR-B-0615 — warunek zgody ekspertów

W obrębie ADR-B-06-K04 cztery pytania pytały o znaczenie litery X. Wcześniejsza wersja ADR-B-0615 nie odróżniała wyraźnie bezwzględnego zakazu wody od reguły ADR: dla substancji oznaczonych X woda może być użyta wyłącznie po uzyskaniu zgody ekspertów.

Zmieniono stem, warianty i explanation w `ADR-B-0615`, zachowując klucz B i status `needs_review`. Nowe opcje mają długości 73/61/66 znaków; poprawna B nie jest najdłuższa. Explanation ma 331 znaków i 4 zdania. Podstawa: ADR 5.3.2.3.1. Snapshoty sequential i legal-review zostały odświeżone.

## 5. Synchronizacja i metryki

- Bank: 652 rekordy; wszystkie `needs_review`, zero `verified`.
- Kompetencja ADR-B-02-K12: 5 pytań po dodaniu ADR-B-0652.
- Warianty i klucze egzaminów próbnych 001–005: `source_bank_head` zsynchronizowany z `d024eaef2d8cc404101769dc64a407675977f64b`.
- Snapshoty `review/sequential` i `review/legal-clauses`: ADR-B-0615 odświeżony, a ostatni zakres rozszerzony z 629–651 do 629–652.
- Manifest PAKIET-0628, kolejki 4x40/4x44, manifest próbki 4x135, README i dokumenty przekazania specjalistom zaktualizowane do SHA banku.
- Nie zmieniano pozostałych pytań, kluczy ani statusów. Nie stwierdzono potrzeby korekty wskaźnika „poprawna = najdłuższa”; nowa poprawna odpowiedź nie jest najdłuższa.
- Pełny Quality Gate i CI mają potwierdzić integralność na PR; lokalny test runner nie był dostępny.

## 6. Źródła

- ADR 2025, 2.2.8.1.1 — definicja klasy 8; Dz.U. 2025 poz. 642: https://dziennikustaw.gov.pl/DU/2025/642
- ADR 2025, 5.3.2.3.1 — znaczenie litery X i warunek użycia wody po zgodzie ekspertów: https://unece.org/adr-2025-files
- ADR 2025 — wydanie obowiązujące od 1 stycznia 2025, UNECE: https://unece.org/adr-2025-files

Wynik jest redakcyjnym uzupełnieniem pokrycia, nie formalną recenzją prawną. Niezależna recenzja specjalisty pozostaje wymagana.
