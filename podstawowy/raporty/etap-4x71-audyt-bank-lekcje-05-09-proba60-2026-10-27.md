# Etap 4x71 — przegląd zgodności banku i lekcji B-05–09 (pierwsza partia)

Data: 27.10.2026. Punktem wyjścia jest świeży `main` `6a965a3908d7507f81e1c8ba0838c03ab476d8bf`. Zakres wyłącznie kurs podstawowy ADR.

## 1. Quality Gate i bank

- Główny CI na wejściowym HEAD: [PASS #40433396299](https://github.com/prawkonaraz100/adr-pytania-egzaminacyjne/actions/runs/40433396299).
- Bank: 609 pytań, 609 `needs_review`, 0 `verified`; unikalność ID: 609/609.
- „Poprawna = jedyna najdłuższa”: 73/609 = 11.99%; wymagany limit ≤18%.
- Minimalna długość explanation: 300 znaków; poniżej 200 znaków: 0.
- W tej partii nie zmieniono odpowiedzi, litery klucza ani statusu prawnego żadnego pytania.

## 2. Całobankowy screening sprzeczności A/B/C ↔ explanation

Dla wszystkich 609 rekordów odczytano treść pytania, `correct_option`, odpowiadającą jej opcję i explanation. Automatyczne filtry szukały pytań zaczynających się od „Czy”, odpowiedzi zaczynających się „Tak”/„Nie”, pytań z negacją i opcji „wszystkie/żadna”. Wykryto 24 par „Czy” + jawna odpowiedź „Tak/Nie” oraz 29 pytań z co najmniej jednym wzorcem wysokiego ryzyka.

Samo słowo „nie” w explanation nie jest dowodem sprzeczności z odpowiedzią „Tak”. Przykład: ADR-B-0027 odpowiada „Tak” na pytanie, czy zasady dotyczące żywności *mogą* mieć znaczenie, po czym wyjaśnia, że nie dotyczą automatycznie wszystkich przewozów. Nie należy mechanicznie odwracać klucza. Analogicznie w ADR-B-0084 stwierdzenie „Tak” ogranicza się do sztuk przesyłek i samego kodu tunelowego.

| ID do uwagi przy dalszej recenzji | Przyczyna | Decyzja |
|---|---|---|
| ADR-B-0027 | „Tak” i późniejszy zwrot „nie oznacza” opisują wyjątek, nie sprzeczność | Nie zmieniono |
| ADR-B-0084 | Kod D/E zależy od postaci przewozu; pozytywna odpowiedź jest warunkowa | Nie zmieniono |
| ADR-B-0452 | „Tak” dotyczy przewozu butli na badanie, nie jej ponownego napełniania | Nie zmieniono |
| ADR-B-0173 | Pytanie „Co wynika?” z opcją zaczynającą się „Nie” — możliwa niezgrabność językowa, nie ustalono błędu prawnego | Do odrębnej korekty po pełnej kontroli powiązanych snapshotów i arkuszy |
| ADR-B-0240 | Pytanie „Kiedy może odstąpić?” i odpowiedź „Nie; wyjątek...” — możliwa niezręczność konstrukcji | Do odrębnej korekty redakcyjnej po przeglądzie źródła |

**Potwierdzonych nowych sprzeczności logicznych na podstawie automatycznych flag: 0.** Nie jest to formalne zatwierdzenie merytoryczne 609 pytań ani literalne porównanie ze wszystkimi przepisami ADR.

## 3. Próbka 60 explanation: rotacja przy wyczerpanej puli

Seed `2026102771`, LCG `state=(1664525×state+1013904223) mod 2^32`, sortowanie ID i Fisher–Yates. Wykluczono 60 ID z próbki 4x67. Jednocześnie rejestr 4x67 dokumentuje **550** istniejących ID wymienionych w raportach 4x51–4x66 oraz dodatkową próbkę 60. Zatem nie jest możliwe wskazanie 60 nowych ID, które nigdy wcześniej nie wystąpiły w kontrolach. Wybrano kolejną rotacyjną próbkę 60 rekordów; wszystkie 60 były wcześniej wzmiankowane w starszych raportach. Nie opisujemy tej próbki jako całkowicie niepowtarzalnej.

Prosty podział przy skrótach przepisów, numeracji i kropkach w `ADR 5.4.3.4` często błędnie liczy wiele dodatkowych zdań; liczbę zdań dla lekcji należy sprawdzać po oddzieleniu końcowego `Podstawa:` i bez rozdzielania numerów punktów. Wśród 60 próbek nie znaleziono explanation poniżej 200 znaków ani bez odwołania do ADR. Automatyczny filtr oznaczył 0 pozycji do pogłębionego czytania (w szczególności tam, gdzie opis błędnej alternatywy jest sformułowany bez dosłownego „błędne”). To **kandydaci do oceny**, nie potwierdzone wady. Bez mechanicznego przepisania tekstu, którego sens i podstawa nie zostały obalone.

| ID | Dział | Znaki | Zdania przed podstawą (heurystyka) | Najdłuższe zdanie — słowa | Wynik |
|---|---|---:|---:|---:|---|
| ADR-B-0560 | ADR-B-09 | 369 | 3 | 20 | heurystyka bez sygnału |
| ADR-B-0559 | ADR-B-09 | 338 | 3 | 15 | heurystyka bez sygnału |
| ADR-B-0133 | ADR-B-06 | 337 | 3 | 23 | heurystyka bez sygnału |
| ADR-B-0410 | ADR-B-12 | 328 | 3 | 20 | heurystyka bez sygnału |
| ADR-B-0096 | ADR-B-02 | 305 | 3 | 15 | heurystyka bez sygnału |
| ADR-B-0440 | ADR-B-10 | 409 | 3 | 23 | heurystyka bez sygnału |
| ADR-B-0185 | ADR-B-05 | 339 | 3 | 15 | heurystyka bez sygnału |
| ADR-B-0146 | ADR-B-13 | 334 | 3 | 14 | heurystyka bez sygnału |
| ADR-B-0488 | ADR-B-11 | 300 | 2 | 23 | heurystyka bez sygnału |
| ADR-B-0553 | ADR-B-08 | 327 | 3 | 17 | heurystyka bez sygnału |
| ADR-B-0101 | ADR-B-03 | 309 | 3 | 15 | heurystyka bez sygnału |
| ADR-B-0518 | ADR-B-09 | 305 | 3 | 20 | heurystyka bez sygnału |
| ADR-B-0169 | ADR-B-05 | 358 | 3 | 19 | heurystyka bez sygnału |
| ADR-B-0360 | ADR-B-04 | 306 | 3 | 15 | heurystyka bez sygnału |
| ADR-B-0533 | ADR-B-13 | 359 | 3 | 31 | heurystyka bez sygnału |
| ADR-B-0007 | ADR-B-03 | 327 | 3 | 21 | heurystyka bez sygnału |
| ADR-B-0516 | ADR-B-05 | 341 | 3 | 19 | heurystyka bez sygnału |
| ADR-B-0087 | ADR-B-13 | 321 | 3 | 15 | heurystyka bez sygnału |
| ADR-B-0582 | ADR-B-12 | 331 | 3 | 17 | heurystyka bez sygnału |
| ADR-B-0268 | ADR-B-02 | 338 | 3 | 22 | heurystyka bez sygnału |
| ADR-B-0249 | ADR-B-12 | 355 | 3 | 16 | heurystyka bez sygnału |
| ADR-B-0071 | ADR-B-08 | 347 | 3 | 27 | heurystyka bez sygnału |
| ADR-B-0590 | ADR-B-13 | 353 | 3 | 16 | heurystyka bez sygnału |
| ADR-B-0554 | ADR-B-09 | 321 | 3 | 17 | heurystyka bez sygnału |
| ADR-B-0295 | ADR-B-03 | 318 | 3 | 19 | heurystyka bez sygnału |
| ADR-B-0597 | ADR-B-08 | 310 | 3 | 20 | heurystyka bez sygnału |
| ADR-B-0464 | ADR-B-03 | 325 | 3 | 20 | heurystyka bez sygnału |
| ADR-B-0298 | ADR-B-06 | 374 | 3 | 22 | heurystyka bez sygnału |
| ADR-B-0449 | ADR-B-10 | 358 | 3 | 19 | heurystyka bez sygnału |
| ADR-B-0587 | ADR-B-13 | 308 | 3 | 17 | heurystyka bez sygnału |
| ADR-B-0444 | ADR-B-10 | 330 | 3 | 20 | heurystyka bez sygnału |
| ADR-B-0389 | ADR-B-10 | 316 | 3 | 18 | heurystyka bez sygnału |
| ADR-B-0591 | ADR-B-11 | 352 | 3 | 19 | heurystyka bez sygnału |
| ADR-B-0572 | ADR-B-01 | 360 | 3 | 23 | heurystyka bez sygnału |
| ADR-B-0495 | ADR-B-02 | 333 | 3 | 18 | heurystyka bez sygnału |
| ADR-B-0422 | ADR-B-08 | 327 | 3 | 16 | heurystyka bez sygnału |
| ADR-B-0390 | ADR-B-10 | 349 | 3 | 20 | heurystyka bez sygnału |
| ADR-B-0301 | ADR-B-01 | 352 | 3 | 21 | heurystyka bez sygnału |
| ADR-B-0207 | ADR-B-11 | 350 | 3 | 19 | heurystyka bez sygnału |
| ADR-B-0158 | ADR-B-02 | 350 | 3 | 17 | heurystyka bez sygnału |
| ADR-B-0387 | ADR-B-10 | 379 | 3 | 24 | heurystyka bez sygnału |
| ADR-B-0173 | ADR-B-09 | 376 | 3 | 21 | heurystyka bez sygnału |
| ADR-B-0148 | ADR-B-01 | 369 | 3 | 16 | heurystyka bez sygnału |
| ADR-B-0432 | ADR-B-11 | 325 | 3 | 21 | heurystyka bez sygnału |
| ADR-B-0116 | ADR-B-07 | 320 | 3 | 14 | heurystyka bez sygnału |
| ADR-B-0026 | ADR-B-09 | 327 | 3 | 14 | heurystyka bez sygnału |
| ADR-B-0054 | ADR-B-07 | 361 | 3 | 16 | heurystyka bez sygnału |
| ADR-B-0373 | ADR-B-07 | 369 | 3 | 18 | heurystyka bez sygnału |
| ADR-B-0247 | ADR-B-10 | 318 | 3 | 15 | heurystyka bez sygnału |
| ADR-B-0379 | ADR-B-07 | 351 | 3 | 17 | heurystyka bez sygnału |
| ADR-B-0056 | ADR-B-08 | 312 | 3 | 18 | heurystyka bez sygnału |
| ADR-B-0398 | ADR-B-10 | 382 | 3 | 21 | heurystyka bez sygnału |
| ADR-B-0234 | ADR-B-13 | 311 | 3 | 15 | heurystyka bez sygnału |
| ADR-B-0108 | ADR-B-05 | 337 | 3 | 19 | heurystyka bez sygnału |
| ADR-B-0299 | ADR-B-06 | 319 | 3 | 18 | heurystyka bez sygnału |
| ADR-B-0044 | ADR-B-02 | 430 | 4 | 18 | heurystyka bez sygnału |
| ADR-B-0350 | ADR-B-04 | 365 | 3 | 17 | heurystyka bez sygnału |
| ADR-B-0581 | ADR-B-04 | 309 | 3 | 22 | heurystyka bez sygnału |
| ADR-B-0105 | ADR-B-05 | 344 | 3 | 21 | heurystyka bez sygnału |
| ADR-B-0039 | ADR-B-13 | 338 | 3 | 16 | heurystyka bez sygnału |

## 4. Lekcje B-05–B-09

- B-05: przegląd instrukcji pisemnych, awarii, zgłoszenia i ograniczeń działań własnych. Objaśnienia są umieszczone przy terminach, podsumowanie i scenariusze są obecne. Nie zmieniano przepisów.
- B-06: **potwierdzone powtórzenie** liczb 400 × 300 mm oraz 300 × 120 mm w dwóch sąsiednich fragmentach lekcji. Zwięźle odesłano do zachowanej sekcji „Wymiary tablic pomarańczowych” z pełnymi liczbami, obrzeżami i warunkami wyjątku (ADR 5.3.2.2.1). Nie zmieniono wartości ani sensu.
- B-07: podział obowiązków nadawcy, przewoźnika, pakującego, załadowcy i odbiorcy jest objaśniony przed scenariuszami; brak potwierdzonej sprzeczności wymagającej zmiany.
- B-08: kontrolowano opis DMC, zależność gaśnic od masy jednostki i różnicę wyposażenia pojazdu oraz załogi. Potrzebne jest literalne porównanie szczegółowych progów z urzędowym ADR w odbiorze specjalisty; nie zmieniano ich bez tego porównania.
- B-09: wspólny załadunek, mocowanie, przewóz luzem, pozostałości oraz kryteria przed załadunkiem. Nie zmieniono danych prawnych bez udokumentowanego błędu.

## 5. Scenariusze i pokrycie

Skontrolowano strukturalnie wszystkie 39 scenariuszy: kroki kierowcy, `question_ids`, `legal_basis`, `common_mistakes` i `assessment_criteria`. Każdy ma cztery kroki, powiązania do istniejących ID we właściwym module i wymienione pola; niezgodności strukturalne: 0. To nie zastępuje merytorycznej oceny każdego kroku przez instruktora i specjalistę ADR. Brak udokumentowanej nowej luki programu wymagającej tworzenia ADR-B-0610; nie zmieniano z tego powodu wariantów egzaminu ani pakietu recenzenta.

## 6. Wnioski i dalsza partia

Najważniejsza kolejna praca: przegląd języka pytań z negacją i odpowiedziami warunkowymi, kontrola szczegółowych progów i podstaw prawnych przez specjalistę oraz czytanie kolejnych partii lekcji. Korekt przepisów nie wykonuje się „na wyczucie”. Wszystkie rekordy pozostają `needs_review`.
