# Etap 4x65 — kontrola lekcji 05–09, próbka 60 i scenariusze

Data 27.10.2026. Źródłowy main `0533c79b3105dd45668bfcd63a7d3319f62dd79a`. Wyłącznie podstawowy kurs ADR.

## Quality Gate i stan banku
- Główny CI [run #40411817532](https://github.com/prawkonaraz100/adr-pytania-egzaminacyjne/actions/runs/40411817532): **PASS**.
- Bank: 609 pytań, wszystkie `needs_review`, 0 `verified`.
- „Poprawna = jedyna najdłuższa”: **72/609 = 11,82%**, limit 18%. Explanation: minimum 300 znaków (według ostatniej kontroli na main).
- W trakcie audytu nie potwierdzono luki programu wymagającej nowego pytania. Nie zmieniano banku ani liter odpowiedzi.

## Nowa próbka 60 explanation
- Deterministyczny seed **2026102765**, generator LCG `state=(1664525×state+1013904223) mod 2^32`, Fisher–Yates po sortowaniu ID.
- Wykluczono wszystkie ID wymienione w raportach 4x51–4x64. W dostępnych raportach wykryto 489 różnych oznaczeń ID, z czego do banku pozostało do losowania 121 pytań. Wybrano 60 różnych ID bez ponownego wylosowania pytań z listy wykluczeń.
- W każdej próbce wyjaśnienie ma 3–5 zdań, minimum 300 znaków, najdłuższe zdanie nie przekracza 35 słów; żadne nie zaczyna się od cytatu przepisu, wszystkie zawierają argument o błędnej alternatywie i podają podstawę ADR. To przegląd dydaktyczny wsparty heurystyką, **nie** literalne porównanie przepisów ani akceptacja specjalisty.
- **0 potwierdzonych poprawek explanation** — brak podstaw do zmian tylko kosmetycznych.

| Lp. | ID | Ocena |
|---:|---|---|
| 1 | ADR-B-0265 | Przegląd języka: 3–5 zdań, uzasadnienie błędnych opcji i podstawa ADR obecne; bez potwierdzonej potrzeby zmiany |
| 2 | ADR-B-0250 | Przegląd języka: 3–5 zdań, uzasadnienie błędnych opcji i podstawa ADR obecne; bez potwierdzonej potrzeby zmiany |
| 3 | ADR-B-0227 | Przegląd języka: 3–5 zdań, uzasadnienie błędnych opcji i podstawa ADR obecne; bez potwierdzonej potrzeby zmiany |
| 4 | ADR-B-0427 | Przegląd języka: 3–5 zdań, uzasadnienie błędnych opcji i podstawa ADR obecne; bez potwierdzonej potrzeby zmiany |
| 5 | ADR-B-0019 | Przegląd języka: 3–5 zdań, uzasadnienie błędnych opcji i podstawa ADR obecne; bez potwierdzonej potrzeby zmiany |
| 6 | ADR-B-0431 | Przegląd języka: 3–5 zdań, uzasadnienie błędnych opcji i podstawa ADR obecne; bez potwierdzonej potrzeby zmiany |
| 7 | ADR-B-0607 | Przegląd języka: 3–5 zdań, uzasadnienie błędnych opcji i podstawa ADR obecne; bez potwierdzonej potrzeby zmiany |
| 8 | ADR-B-0348 | Przegląd języka: 3–5 zdań, uzasadnienie błędnych opcji i podstawa ADR obecne; bez potwierdzonej potrzeby zmiany |
| 9 | ADR-B-0493 | Przegląd języka: 3–5 zdań, uzasadnienie błędnych opcji i podstawa ADR obecne; bez potwierdzonej potrzeby zmiany |
| 10 | ADR-B-0166 | Przegląd języka: 3–5 zdań, uzasadnienie błędnych opcji i podstawa ADR obecne; bez potwierdzonej potrzeby zmiany |
| 11 | ADR-B-0175 | Przegląd języka: 3–5 zdań, uzasadnienie błędnych opcji i podstawa ADR obecne; bez potwierdzonej potrzeby zmiany |
| 12 | ADR-B-0433 | Przegląd języka: 3–5 zdań, uzasadnienie błędnych opcji i podstawa ADR obecne; bez potwierdzonej potrzeby zmiany |
| 13 | ADR-B-0383 | Przegląd języka: 3–5 zdań, uzasadnienie błędnych opcji i podstawa ADR obecne; bez potwierdzonej potrzeby zmiany |
| 14 | ADR-B-0387 | Przegląd języka: 3–5 zdań, uzasadnienie błędnych opcji i podstawa ADR obecne; bez potwierdzonej potrzeby zmiany |
| 15 | ADR-B-0594 | Przegląd języka: 3–5 zdań, uzasadnienie błędnych opcji i podstawa ADR obecne; bez potwierdzonej potrzeby zmiany |
| 16 | ADR-B-0495 | Przegląd języka: 3–5 zdań, uzasadnienie błędnych opcji i podstawa ADR obecne; bez potwierdzonej potrzeby zmiany |
| 17 | ADR-B-0264 | Przegląd języka: 3–5 zdań, uzasadnienie błędnych opcji i podstawa ADR obecne; bez potwierdzonej potrzeby zmiany |
| 18 | ADR-B-0569 | Przegląd języka: 3–5 zdań, uzasadnienie błędnych opcji i podstawa ADR obecne; bez potwierdzonej potrzeby zmiany |
| 19 | ADR-B-0277 | Przegląd języka: 3–5 zdań, uzasadnienie błędnych opcji i podstawa ADR obecne; bez potwierdzonej potrzeby zmiany |
| 20 | ADR-B-0152 | Przegląd języka: 3–5 zdań, uzasadnienie błędnych opcji i podstawa ADR obecne; bez potwierdzonej potrzeby zmiany |
| 21 | ADR-B-0078 | Przegląd języka: 3–5 zdań, uzasadnienie błędnych opcji i podstawa ADR obecne; bez potwierdzonej potrzeby zmiany |
| 22 | ADR-B-0451 | Przegląd języka: 3–5 zdań, uzasadnienie błędnych opcji i podstawa ADR obecne; bez potwierdzonej potrzeby zmiany |
| 23 | ADR-B-0579 | Przegląd języka: 3–5 zdań, uzasadnienie błędnych opcji i podstawa ADR obecne; bez potwierdzonej potrzeby zmiany |
| 24 | ADR-B-0506 | Przegląd języka: 3–5 zdań, uzasadnienie błędnych opcji i podstawa ADR obecne; bez potwierdzonej potrzeby zmiany |
| 25 | ADR-B-0146 | Przegląd języka: 3–5 zdań, uzasadnienie błędnych opcji i podstawa ADR obecne; bez potwierdzonej potrzeby zmiany |
| 26 | ADR-B-0466 | Przegląd języka: 3–5 zdań, uzasadnienie błędnych opcji i podstawa ADR obecne; bez potwierdzonej potrzeby zmiany |
| 27 | ADR-B-0593 | Przegląd języka: 3–5 zdań, uzasadnienie błędnych opcji i podstawa ADR obecne; bez potwierdzonej potrzeby zmiany |
| 28 | ADR-B-0586 | Przegląd języka: 3–5 zdań, uzasadnienie błędnych opcji i podstawa ADR obecne; bez potwierdzonej potrzeby zmiany |
| 29 | ADR-B-0256 | Przegląd języka: 3–5 zdań, uzasadnienie błędnych opcji i podstawa ADR obecne; bez potwierdzonej potrzeby zmiany |
| 30 | ADR-B-0337 | Przegląd języka: 3–5 zdań, uzasadnienie błędnych opcji i podstawa ADR obecne; bez potwierdzonej potrzeby zmiany |
| 31 | ADR-B-0473 | Przegląd języka: 3–5 zdań, uzasadnienie błędnych opcji i podstawa ADR obecne; bez potwierdzonej potrzeby zmiany |
| 32 | ADR-B-0314 | Przegląd języka: 3–5 zdań, uzasadnienie błędnych opcji i podstawa ADR obecne; bez potwierdzonej potrzeby zmiany |
| 33 | ADR-B-0472 | Przegląd języka: 3–5 zdań, uzasadnienie błędnych opcji i podstawa ADR obecne; bez potwierdzonej potrzeby zmiany |
| 34 | ADR-B-0226 | Przegląd języka: 3–5 zdań, uzasadnienie błędnych opcji i podstawa ADR obecne; bez potwierdzonej potrzeby zmiany |
| 35 | ADR-B-0272 | Przegląd języka: 3–5 zdań, uzasadnienie błędnych opcji i podstawa ADR obecne; bez potwierdzonej potrzeby zmiany |
| 36 | ADR-B-0121 | Przegląd języka: 3–5 zdań, uzasadnienie błędnych opcji i podstawa ADR obecne; bez potwierdzonej potrzeby zmiany |
| 37 | ADR-B-0111 | Przegląd języka: 3–5 zdań, uzasadnienie błędnych opcji i podstawa ADR obecne; bez potwierdzonej potrzeby zmiany |
| 38 | ADR-B-0261 | Przegląd języka: 3–5 zdań, uzasadnienie błędnych opcji i podstawa ADR obecne; bez potwierdzonej potrzeby zmiany |
| 39 | ADR-B-0268 | Przegląd języka: 3–5 zdań, uzasadnienie błędnych opcji i podstawa ADR obecne; bez potwierdzonej potrzeby zmiany |
| 40 | ADR-B-0601 | Przegląd języka: 3–5 zdań, uzasadnienie błędnych opcji i podstawa ADR obecne; bez potwierdzonej potrzeby zmiany |
| 41 | ADR-B-0470 | Przegląd języka: 3–5 zdań, uzasadnienie błędnych opcji i podstawa ADR obecne; bez potwierdzonej potrzeby zmiany |
| 42 | ADR-B-0216 | Przegląd języka: 3–5 zdań, uzasadnienie błędnych opcji i podstawa ADR obecne; bez potwierdzonej potrzeby zmiany |
| 43 | ADR-B-0411 | Przegląd języka: 3–5 zdań, uzasadnienie błędnych opcji i podstawa ADR obecne; bez potwierdzonej potrzeby zmiany |
| 44 | ADR-B-0526 | Przegląd języka: 3–5 zdań, uzasadnienie błędnych opcji i podstawa ADR obecne; bez potwierdzonej potrzeby zmiany |
| 45 | ADR-B-0391 | Przegląd języka: 3–5 zdań, uzasadnienie błędnych opcji i podstawa ADR obecne; bez potwierdzonej potrzeby zmiany |
| 46 | ADR-B-0258 | Przegląd języka: 3–5 zdań, uzasadnienie błędnych opcji i podstawa ADR obecne; bez potwierdzonej potrzeby zmiany |
| 47 | ADR-B-0530 | Przegląd języka: 3–5 zdań, uzasadnienie błędnych opcji i podstawa ADR obecne; bez potwierdzonej potrzeby zmiany |
| 48 | ADR-B-0556 | Przegląd języka: 3–5 zdań, uzasadnienie błędnych opcji i podstawa ADR obecne; bez potwierdzonej potrzeby zmiany |
| 49 | ADR-B-0591 | Przegląd języka: 3–5 zdań, uzasadnienie błędnych opcji i podstawa ADR obecne; bez potwierdzonej potrzeby zmiany |
| 50 | ADR-B-0489 | Przegląd języka: 3–5 zdań, uzasadnienie błędnych opcji i podstawa ADR obecne; bez potwierdzonej potrzeby zmiany |
| 51 | ADR-B-0482 | Przegląd języka: 3–5 zdań, uzasadnienie błędnych opcji i podstawa ADR obecne; bez potwierdzonej potrzeby zmiany |
| 52 | ADR-B-0397 | Przegląd języka: 3–5 zdań, uzasadnienie błędnych opcji i podstawa ADR obecne; bez potwierdzonej potrzeby zmiany |
| 53 | ADR-B-0349 | Przegląd języka: 3–5 zdań, uzasadnienie błędnych opcji i podstawa ADR obecne; bez potwierdzonej potrzeby zmiany |
| 54 | ADR-B-0592 | Przegląd języka: 3–5 zdań, uzasadnienie błędnych opcji i podstawa ADR obecne; bez potwierdzonej potrzeby zmiany |
| 55 | ADR-B-0105 | Przegląd języka: 3–5 zdań, uzasadnienie błędnych opcji i podstawa ADR obecne; bez potwierdzonej potrzeby zmiany |
| 56 | ADR-B-0603 | Przegląd języka: 3–5 zdań, uzasadnienie błędnych opcji i podstawa ADR obecne; bez potwierdzonej potrzeby zmiany |
| 57 | ADR-B-0088 | Przegląd języka: 3–5 zdań, uzasadnienie błędnych opcji i podstawa ADR obecne; bez potwierdzonej potrzeby zmiany |
| 58 | ADR-B-0504 | Przegląd języka: 3–5 zdań, uzasadnienie błędnych opcji i podstawa ADR obecne; bez potwierdzonej potrzeby zmiany |
| 59 | ADR-B-0512 | Przegląd języka: 3–5 zdań, uzasadnienie błędnych opcji i podstawa ADR obecne; bez potwierdzonej potrzeby zmiany |
| 60 | ADR-B-0534 | Przegląd języka: 3–5 zdań, uzasadnienie błędnych opcji i podstawa ADR obecne; bez potwierdzonej potrzeby zmiany |

## Przegląd lekcji B-05–B-09

| Lekcja | Odwołania do pytań | Scenariusze | Wynik |
|---|---:|---:|---|
| B-05 | 43 | 3 | Odwołania istnieją, są we właściwym dziale; słowniczek, przykłady, podsumowanie i podstawa ADR obecne |
| B-06 | 45 | 3 | Odwołania istnieją, są we właściwym dziale; słowniczek, przykłady, podsumowanie i podstawa ADR obecne |
| B-07 | 48 | 3 | Odwołania istnieją, są we właściwym dziale; słowniczek, przykłady, podsumowanie i podstawa ADR obecne |
| B-08 | 42 | 3 | Odwołania istnieją, są we właściwym dziale; słowniczek, przykłady, podsumowanie i podstawa ADR obecne |
| B-09 | 46 | 3 | Odwołania istnieją, są we właściwym dziale; słowniczek, przykłady, podsumowanie i podstawa ADR obecne |

- B-05: bezpieczeństwo po awarii, instrukcje pisemne, gaśnice, wezwanie pomocy i proste przykłady.
- B-06: oznakowanie przesyłek, tablice pomarańczowe, numer UN i numer zagrożenia.
- B-07: obowiązki nadawcy, przewoźnika, załadowcy i pakującego, przykłady z załadunku.
- B-08: wymagane wyposażenie załogi i pojazdu, DMC, gaśnice i dokumenty pojazdu.
- B-09: załadunek, oddzielanie, mocowanie, warunki przewozu luzem.

W każdej lekcji jest słowniczek, co najmniej trzy istniejące odsyłacze SC-ADR-B-XX, podsumowanie, odpowiednie pytania i podstawa prawna. Nie wykryto brakującego ID ani odwołania do innego działu. Nie stwierdzono potwierdzonych sprzeczności uprawniających do zmiany treści prawnej bez nowego źródła.

## Audyt 39 scenariuszy

Sprawdzono 39/39 obiektów w `podstawowy/praktyka/scenariusze-13-dzialow.json`. Każdy posiada sytuację, **4 kroki postępowania kierowcy**, powiązane istniejące `question_ids` ze swojego działu, co najmniej trzy typowe błędy, podstawę ADR i kryterium oceny. Brak nieistniejących i obcych ID, brak pustych kroków. Zawartość ma formę bezpiecznej symulacji szkoleniowej, nie dokumentuje przeprowadzonych zajęć praktycznych. Nie wykryto potwierdzonych braków wymagających zmiany.

## Decyzja i następny krok
Brak potwierdzonych błędów oznacza brak edycji pytań i lekcji. Nie regenerowano egzaminów i pakietu recenzyjnego, ponieważ bank, moduły i klucze pozostały niezmienione. Następny sensowny kierunek: audyt **ścieżki kierowcy przed rozpoczęciem przewozu** na styku B-01, B-06, B-08 i B-13 oraz wykrywanie ewentualnych luk, bez wymyślania nowych przepisów.
