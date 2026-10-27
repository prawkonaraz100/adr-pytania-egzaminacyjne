# Etap 4x72 — przegląd dystraktorów, lekcji B-10–13, próba 60 i kontrola egzaminu

Data: 27.10.2026. Punkt wyjścia: świeży `main` `f25348cb6d08e40cae96432a78c4479edbb18c96`. Wyłącznie kurs podstawowy.

## Stan początkowy i metoda

CI na bazowym main: [PASS](https://github.com/prawkonaraz100/adr-pytania-egzaminacyjne/actions/runs/40438382859). Bank 609 rekordów `needs_review`, 0 `verified`, 609 unikalnych ID, minimum explanation 300 znaków; jedyna najdłuższa poprawna odpowiedź: 73/609 = 11,99%.

Odczytano cały bank i błędne opcje A/B/C. Filtr szukał m.in. „wszystkie/żadna z powyższych”, losowych osób jako podmiotów obowiązku, dowolnych czynności bez warunków i oczywiście fałszywych uzasadnień. Wstępnie zaznaczono 16 opcji — to sygnał do redakcji, nie dowód błędu prawnego.

## Potwierdzona korekta i podstawa

| ID | Opcja | Przed | Po | Uzasadnienie |
|---|---|---|---|---|
| ADR-B-0050 | C | „Po francusku, bo ADR opracowano w Genewie” | „W języku urzędowym kraju rozpoczęcia przewozu, nawet gdy załoga go nie rozumie” | Stara opcja była żartobliwa i oczywiście fałszywa. Nowa przedstawia realistyczne pomylenie języka urzędowego z językiem zrozumiałym dla załogi. ADR 2025 5.4.3.2 wymaga języka, który każdy członek załogi umie czytać i rozumie. |

Zaktualizowano explanation ADR-B-0050 (312 znaków; sens, obie błędne możliwości, końcowa podstawa ADR). Nie zmieniono ID, poprawnej litery B, statusu ani materiału prawnego. Wariant próbnego egzaminu 004 miał pytanie pod numerem 17 z przetasowanymi opcjami: zaktualizowano wariant oraz odpowiadający klucz. Wszystkie warianty 001–005 otrzymały nowy SHA źródłowego banku `61c592059335983d672d973cb180a71c472b5500`, bez zmiany ID i proporcji działów. Jako dodatkowe źródło kontrolne wykorzystano wersję ADR 2025 5.4.3.2 opublikowaną przez UNECE i dostępne krajowe materiały urzędowe; nie oznacza to formalnej recenzji specjalisty.

## Pozostałe flagi do specjalistycznego przeglądu

- `ADR-B-0003` — sprawdzić wiarygodność dystraktorów i literalną podstawę ADR przed zmianą; samo użycie słowa „dowolny”, „zawsze” albo nietypowej osoby nie wystarcza do uznania błędu prawnego.
- `ADR-B-0283` — sprawdzić wiarygodność dystraktorów i literalną podstawę ADR przed zmianą; samo użycie słowa „dowolny”, „zawsze” albo nietypowej osoby nie wystarcza do uznania błędu prawnego.
- `ADR-B-0320` — sprawdzić wiarygodność dystraktorów i literalną podstawę ADR przed zmianą; samo użycie słowa „dowolny”, „zawsze” albo nietypowej osoby nie wystarcza do uznania błędu prawnego.
- `ADR-B-0333` — sprawdzić wiarygodność dystraktorów i literalną podstawę ADR przed zmianą; samo użycie słowa „dowolny”, „zawsze” albo nietypowej osoby nie wystarcza do uznania błędu prawnego.
- `ADR-B-0336` — sprawdzić wiarygodność dystraktorów i literalną podstawę ADR przed zmianą; samo użycie słowa „dowolny”, „zawsze” albo nietypowej osoby nie wystarcza do uznania błędu prawnego.
- `ADR-B-0344` — sprawdzić wiarygodność dystraktorów i literalną podstawę ADR przed zmianą; samo użycie słowa „dowolny”, „zawsze” albo nietypowej osoby nie wystarcza do uznania błędu prawnego.
- `ADR-B-0378` — sprawdzić wiarygodność dystraktorów i literalną podstawę ADR przed zmianą; samo użycie słowa „dowolny”, „zawsze” albo nietypowej osoby nie wystarcza do uznania błędu prawnego.
- `ADR-B-0387` — sprawdzić wiarygodność dystraktorów i literalną podstawę ADR przed zmianą; samo użycie słowa „dowolny”, „zawsze” albo nietypowej osoby nie wystarcza do uznania błędu prawnego.
- `ADR-B-0441` — sprawdzić wiarygodność dystraktorów i literalną podstawę ADR przed zmianą; samo użycie słowa „dowolny”, „zawsze” albo nietypowej osoby nie wystarcza do uznania błędu prawnego.
- `ADR-B-0448` — sprawdzić wiarygodność dystraktorów i literalną podstawę ADR przed zmianą; samo użycie słowa „dowolny”, „zawsze” albo nietypowej osoby nie wystarcza do uznania błędu prawnego.
- `ADR-B-0454` — sprawdzić wiarygodność dystraktorów i literalną podstawę ADR przed zmianą; samo użycie słowa „dowolny”, „zawsze” albo nietypowej osoby nie wystarcza do uznania błędu prawnego.
- `ADR-B-0499` — sprawdzić wiarygodność dystraktorów i literalną podstawę ADR przed zmianą; samo użycie słowa „dowolny”, „zawsze” albo nietypowej osoby nie wystarcza do uznania błędu prawnego.
- `ADR-B-0530` — sprawdzić wiarygodność dystraktorów i literalną podstawę ADR przed zmianą; samo użycie słowa „dowolny”, „zawsze” albo nietypowej osoby nie wystarcza do uznania błędu prawnego.
- `ADR-B-0536` — sprawdzić wiarygodność dystraktorów i literalną podstawę ADR przed zmianą; samo użycie słowa „dowolny”, „zawsze” albo nietypowej osoby nie wystarcza do uznania błędu prawnego.

## Próbka 60 explanation — rotacja

**Seed:** `2026102772`; sortowanie ID leksykograficznie, generator LCG `state=(1664525*state+1013904223) mod 2^32`, Fisher–Yates, pierwszych 60 rekordów. Raport 4x69 dokumentuje już tylko 20 ID niewystępujących we wcześniejszych raportach, a 4x71 wykonał kolejną próbę. **Nie istnieje 60 nowych ID nieobecnych w próbach 4x51–4x71**. Zastosowano więc powtórną próbę rotacyjną zamiast fikcyjnie deklarować 60 nowych. To ograniczenie metodyczne.

| ID | Dział | Znaki | Zdania przed podstawą* | Maks. słów/zdanie* | Wynik |
|---|---|---:|---:|---:|---|
| ADR-B-0454 | ADR-B-10 | 398 | 3 | 21 | bez potwierdzonej potrzeby zmiany |
| ADR-B-0073 | ADR-B-08 | 388 | 3 | 19 | bez potwierdzonej potrzeby zmiany |
| ADR-B-0191 | ADR-B-06 | 345 | 3 | 27 | bez potwierdzonej potrzeby zmiany |
| ADR-B-0452 | ADR-B-10 | 316 | 3 | 17 | bez potwierdzonej potrzeby zmiany |
| ADR-B-0015 | ADR-B-05 | 366 | 3 | 18 | bez potwierdzonej potrzeby zmiany |
| ADR-B-0353 | ADR-B-04 | 379 | 3 | 21 | bez potwierdzonej potrzeby zmiany |
| ADR-B-0559 | ADR-B-09 | 338 | 3 | 15 | bez potwierdzonej potrzeby zmiany |
| ADR-B-0265 | ADR-B-02 | 336 | 3 | 20 | bez potwierdzonej potrzeby zmiany |
| ADR-B-0232 | ADR-B-05 | 405 | 3 | 19 | bez potwierdzonej potrzeby zmiany |
| ADR-B-0105 | ADR-B-05 | 344 | 3 | 21 | bez potwierdzonej potrzeby zmiany |
| ADR-B-0496 | ADR-B-02 | 300 | 2 | 20 | bez potwierdzonej potrzeby zmiany |
| ADR-B-0058 | ADR-B-09 | 334 | 3 | 18 | bez potwierdzonej potrzeby zmiany |
| ADR-B-0579 | ADR-B-13 | 374 | 3 | 19 | bez potwierdzonej potrzeby zmiany |
| ADR-B-0066 | ADR-B-12 | 342 | 3 | 20 | bez potwierdzonej potrzeby zmiany |
| ADR-B-0123 | ADR-B-01 | 351 | 3 | 21 | bez potwierdzonej potrzeby zmiany |
| ADR-B-0089 | ADR-B-13 | 426 | 3 | 27 | bez potwierdzonej potrzeby zmiany |
| ADR-B-0390 | ADR-B-10 | 349 | 3 | 20 | bez potwierdzonej potrzeby zmiany |
| ADR-B-0557 | ADR-B-09 | 337 | 3 | 15 | bez potwierdzonej potrzeby zmiany |
| ADR-B-0057 | ADR-B-08 | 330 | 3 | 17 | bez potwierdzonej potrzeby zmiany |
| ADR-B-0465 | ADR-B-03 | 334 | 3 | 22 | bez potwierdzonej potrzeby zmiany |
| ADR-B-0006 | ADR-B-02 | 376 | 4 | 14 | bez potwierdzonej potrzeby zmiany |
| ADR-B-0186 | ADR-B-05 | 346 | 3 | 14 | bez potwierdzonej potrzeby zmiany |
| ADR-B-0563 | ADR-B-06 | 339 | 3 | 17 | bez potwierdzonej potrzeby zmiany |
| ADR-B-0035 | ADR-B-12 | 334 | 3 | 15 | bez potwierdzonej potrzeby zmiany |
| ADR-B-0455 | ADR-B-12 | 318 | 3 | 23 | bez potwierdzonej potrzeby zmiany |
| ADR-B-0208 | ADR-B-11 | 381 | 3 | 21 | bez potwierdzonej potrzeby zmiany |
| ADR-B-0405 | ADR-B-12 | 438 | 3 | 21 | bez potwierdzonej potrzeby zmiany |
| ADR-B-0599 | ADR-B-13 | 348 | 3 | 25 | bez potwierdzonej potrzeby zmiany |
| ADR-B-0486 | ADR-B-08 | 348 | 3 | 18 | bez potwierdzonej potrzeby zmiany |
| ADR-B-0113 | ADR-B-05 | 311 | 3 | 14 | bez potwierdzonej potrzeby zmiany |
| ADR-B-0497 | ADR-B-02 | 357 | 3 | 21 | bez potwierdzonej potrzeby zmiany |
| ADR-B-0385 | ADR-B-10 | 336 | 3 | 15 | bez potwierdzonej potrzeby zmiany |
| ADR-B-0508 | ADR-B-13 | 356 | 3 | 21 | bez potwierdzonej potrzeby zmiany |
| ADR-B-0144 | ADR-B-12 | 328 | 3 | 16 | bez potwierdzonej potrzeby zmiany |
| ADR-B-0392 | ADR-B-10 | 319 | 2 | 21 | bez potwierdzonej potrzeby zmiany |
| ADR-B-0308 | ADR-B-11 | 303 | 3 | 16 | bez potwierdzonej potrzeby zmiany |
| ADR-B-0167 | ADR-B-05 | 301 | 3 | 13 | bez potwierdzonej potrzeby zmiany |
| ADR-B-0490 | ADR-B-11 | 323 | 3 | 20 | bez potwierdzonej potrzeby zmiany |
| ADR-B-0135 | ADR-B-07 | 339 | 3 | 13 | bez potwierdzonej potrzeby zmiany |
| ADR-B-0092 | ADR-B-01 | 354 | 3 | 23 | bez potwierdzonej potrzeby zmiany |
| ADR-B-0577 | ADR-B-13 | 318 | 3 | 17 | bez potwierdzonej potrzeby zmiany |
| ADR-B-0356 | ADR-B-04 | 341 | 3 | 18 | bez potwierdzonej potrzeby zmiany |
| ADR-B-0055 | ADR-B-07 | 330 | 3 | 14 | bez potwierdzonej potrzeby zmiany |
| ADR-B-0425 | ADR-B-09 | 305 | 3 | 16 | bez potwierdzonej potrzeby zmiany |
| ADR-B-0437 | ADR-B-10 | 319 | 3 | 18 | bez potwierdzonej potrzeby zmiany |
| ADR-B-0578 | ADR-B-13 | 357 | 3 | 21 | bez potwierdzonej potrzeby zmiany |
| ADR-B-0228 | ADR-B-13 | 342 | 3 | 19 | bez potwierdzonej potrzeby zmiany |
| ADR-B-0499 | ADR-B-02 | 425 | 3 | 33 | bez potwierdzonej potrzeby zmiany |
| ADR-B-0243 | ADR-B-04 | 377 | 3 | 18 | bez potwierdzonej potrzeby zmiany |
| ADR-B-0487 | ADR-B-11 | 302 | 3 | 25 | bez potwierdzonej potrzeby zmiany |
| ADR-B-0156 | ADR-B-02 | 312 | 3 | 23 | bez potwierdzonej potrzeby zmiany |
| ADR-B-0411 | ADR-B-12 | 315 | 3 | 18 | bez potwierdzonej potrzeby zmiany |
| ADR-B-0081 | ADR-B-09 | 352 | 3 | 20 | bez potwierdzonej potrzeby zmiany |
| ADR-B-0155 | ADR-B-02 | 333 | 3 | 17 | bez potwierdzonej potrzeby zmiany |
| ADR-B-0506 | ADR-B-06 | 355 | 3 | 16 | bez potwierdzonej potrzeby zmiany |
| ADR-B-0575 | ADR-B-11 | 317 | 3 | 16 | bez potwierdzonej potrzeby zmiany |
| ADR-B-0196 | ADR-B-07 | 373 | 3 | 20 | bez potwierdzonej potrzeby zmiany |
| ADR-B-0078 | ADR-B-09 | 359 | 3 | 15 | bez potwierdzonej potrzeby zmiany |
| ADR-B-0317 | ADR-B-02 | 430 | 3 | 18 | bez potwierdzonej potrzeby zmiany |
| ADR-B-0026 | ADR-B-09 | 327 | 3 | 14 | bez potwierdzonej potrzeby zmiany |

*Heurystyka nie dzieli kropkami numerów przepisów. Wynik jest filtrem redakcyjnym i kontrolą treści, nie niezależną oceną specjalisty. Dwa flagowane rekordy (ADR-B-0452 i ADR-B-0392) mają wyjaśnienia ograniczające zastosowanie wyjątku i nie stanowią jednozdaniowego cytatu przepisu. Nie zmieniono ich bez wykazanej wady.

## Scenariusze i lekcje

Sprawdzono strukturę wszystkich 39 scenariuszy: 39/39 z wieloetapowymi krokami, co najmniej jednym istniejącym powiązanym ID właściwego działu, podstawą ADR oraz podsumowaniem dla kursanta; nie znaleziono braków strukturalnych wymagających korekty. Lekcje B-10–B-13 obejmują odpowiednio: ADR/RID/IMDG i dokumenty kombinowane; kategorie tuneli i kod D/E; plan ochrony i progi towarów dużego ryzyka; dokumenty przewozowe, instrukcje pisemne i ich praktyczne zastosowanie. Weryfikacja struktury nie dowodzi poprawności prawnej wszystkich twierdzeń. Nie zmieniono merytoryki tych lekcji bez potwierdzonego błędu.

## Luki programu, status publikacji, dalsza kontrola

W tej partii nie udowodniono nowej luki programu wymagającej ADR-B-0610. Nie dopisywano pytań na podstawie przypuszczenia. Warianty egzaminu pozostają treningowe (`publication_authorized=false`). Pakiet 609 pytań nie został zatwierdzony; wszystkie pytania pozostają `needs_review`. Kolejny sensowny krok: odrębna recenzja pozostałych 14 wskazanych ID przez specjalistę, z literalnym sprawdzeniem przepisów, i dopiero ewentualna korekta opcji wraz z synchronizacją egzaminów i audytów.
