# Etap 4x78 — kontrola scenariuszy i rotacyjna próba wyjaśnień

Data: 27.10.2026. Punkt wyjścia: `c42f0edc1fbd6291896232ae559601e45b60558f`. Zakres: tylko kurs podstawowy.

## Stan potwierdzony

- CI dla świeżego `main`: **PASS** ([run #40455435153](https://github.com/prawkonaraz100/adr-pytania-egzaminacyjne/actions/runs/40455435153)).
- Bank: **609** pytań, `609 needs_review`, 0 `verified`; brak zmian w banku.
- Poprawna odpowiedź jako jedyna najdłuższa: **73/609 = 11.99%**; najmniejsze explanation 300 znaków. Działy: 01: 13.33%, 02: 14.29%, 03: 14.29%, 04: 13.04%, 05: 11.63%, 06: 11.11%, 07: 12.50%, 08: 11.90%, 09: 8.70%, 10: 7.27%, 11: 13.95%, 12: 13.64%, 13: 10.64%.

## Scenariusze — 39 pozycji

Przegląd struktury wszystkich 39 scenariuszy: co najmniej trzy kroki, opis sytuacji, typowe pomyłki, źródła ADR, kryteria oceny i odwołania do pytań. Odwołania do brakujących pytań lub innego działu: **0**. Pozycje z brakującym komponentem: **0**. Kontrola struktur i mapowań nie zastępuje prawnego sprawdzenia każdego przepisu.

**Potwierdzona niejasność scenariusza SC-ADR-B-05:** ostatni krok w scenariuszu awarii nakazywał sprawdzenie gaśnicy „przed wyjazdem”. Dla początkującego mieszało to chronologię: kontrolę przed trasą z reakcją po wypadku. Przeniesiono kontrolę sprzętu na początek instrukcji, a pozostałe kroki ułożono kolejno: bezpieczny postój, ostrzeżenie, silnik/instrukcje, wezwanie pomocy i sprawdzone dane. Merytorycznego obowiązku nie zmieniono. Referencje do oceny: ADR 8.1.4.5 i 5.4.3.4. Żadne pytanie ani litera odpowiedzi nie uległy zmianie.

## Rotacyjna kontrola 60 wyjaśnień

Seed: **2026102778**, pseudolosowanie LCG (parametry 1664525/1013904223, modulo 2³²), deterministyczne tasowanie Fisher–Yates. Zasada: wybrano 60 ID spośród 551 pozycji z rejestru `etap-4x67-wykluczenia-prób.json`, **aby nie powtarzać 59 pozycji z próby 4x76**. Nie jest możliwe stworzenie 60 nowych ID rozłącznych względem wszystkich prób 4x51–77: materiał poprzednich etapów obejmuje praktycznie cały bank. Wybrane 60 to świadomie **powtórki względem wcześniejszych prób**, nie nowo zbadane pytania.

Wykonano czytelnościowy screening pełnych explanation pod kątem: liczby zdań, długości zdań, suchego otwarcia od numeru przepisu, sygnału wyjaśnienia błędnych odpowiedzi i długości 200–500 znaków. Jest to test przesiewowy; heurystyka nie potwierdza samodzielnie błędu prawnego ani dydaktycznego. Wykryto **0** kandydatów do indywidualnego przeczytania; brak zmian samych kluczy i explanation bez potwierdzonego błędu.

| ID | Dział | Znaki | Zdania (heurystyka) | Maks. słowa/zdanie | Wynik |
|---|---|---:|---:|---:|---|
| ADR-B-0515 | ADR-B-04 | 322 | 4 | 26 | brak formalnego alarmu |
| ADR-B-0522 | ADR-B-01 | 364 | 4 | 21 | brak formalnego alarmu |
| ADR-B-0411 | ADR-B-12 | 315 | 4 | 18 | brak formalnego alarmu |
| ADR-B-0586 | ADR-B-13 | 381 | 4 | 24 | brak formalnego alarmu |
| ADR-B-0082 | ADR-B-09 | 460 | 4 | 24 | brak formalnego alarmu |
| ADR-B-0192 | ADR-B-06 | 303 | 4 | 19 | brak formalnego alarmu |
| ADR-B-0291 | ADR-B-09 | 325 | 4 | 19 | brak formalnego alarmu |
| ADR-B-0580 | ADR-B-04 | 322 | 4 | 16 | brak formalnego alarmu |
| ADR-B-0605 | ADR-B-01 | 424 | 4 | 20 | brak formalnego alarmu |
| ADR-B-0308 | ADR-B-11 | 303 | 4 | 16 | brak formalnego alarmu |
| ADR-B-0380 | ADR-B-07 | 349 | 4 | 22 | brak formalnego alarmu |
| ADR-B-0257 | ADR-B-06 | 342 | 4 | 18 | brak formalnego alarmu |
| ADR-B-0158 | ADR-B-02 | 350 | 4 | 17 | brak formalnego alarmu |
| ADR-B-0105 | ADR-B-05 | 344 | 4 | 21 | brak formalnego alarmu |
| ADR-B-0367 | ADR-B-07 | 404 | 5 | 18 | brak formalnego alarmu |
| ADR-B-0504 | ADR-B-06 | 333 | 4 | 15 | brak formalnego alarmu |
| ADR-B-0093 | ADR-B-01 | 397 | 4 | 18 | brak formalnego alarmu |
| ADR-B-0560 | ADR-B-09 | 369 | 4 | 20 | brak formalnego alarmu |
| ADR-B-0554 | ADR-B-09 | 321 | 4 | 17 | brak formalnego alarmu |
| ADR-B-0405 | ADR-B-12 | 438 | 4 | 21 | brak formalnego alarmu |
| ADR-B-0364 | ADR-B-07 | 347 | 4 | 27 | brak formalnego alarmu |
| ADR-B-0060 | ADR-B-09 | 400 | 4 | 21 | brak formalnego alarmu |
| ADR-B-0293 | ADR-B-07 | 351 | 4 | 17 | brak formalnego alarmu |
| ADR-B-0299 | ADR-B-06 | 319 | 4 | 18 | brak formalnego alarmu |
| ADR-B-0197 | ADR-B-08 | 424 | 4 | 27 | brak formalnego alarmu |
| ADR-B-0592 | ADR-B-11 | 307 | 4 | 14 | brak formalnego alarmu |
| ADR-B-0434 | ADR-B-11 | 411 | 4 | 21 | brak formalnego alarmu |
| ADR-B-0596 | ADR-B-08 | 335 | 4 | 20 | brak formalnego alarmu |
| ADR-B-0593 | ADR-B-05 | 354 | 3 | 24 | brak formalnego alarmu |
| ADR-B-0250 | ADR-B-13 | 351 | 4 | 16 | brak formalnego alarmu |
| ADR-B-0457 | ADR-B-12 | 360 | 4 | 20 | brak formalnego alarmu |
| ADR-B-0185 | ADR-B-05 | 339 | 4 | 15 | brak formalnego alarmu |
| ADR-B-0021 | ADR-B-07 | 355 | 4 | 22 | brak formalnego alarmu |
| ADR-B-0495 | ADR-B-02 | 333 | 4 | 18 | brak formalnego alarmu |
| ADR-B-0387 | ADR-B-10 | 379 | 4 | 24 | brak formalnego alarmu |
| ADR-B-0470 | ADR-B-03 | 305 | 3 | 26 | brak formalnego alarmu |
| ADR-B-0111 | ADR-B-05 | 318 | 4 | 15 | brak formalnego alarmu |
| ADR-B-0588 | ADR-B-13 | 338 | 4 | 22 | brak formalnego alarmu |
| ADR-B-0013 | ADR-B-05 | 300 | 4 | 16 | brak formalnego alarmu |
| ADR-B-0433 | ADR-B-11 | 318 | 4 | 18 | brak formalnego alarmu |
| ADR-B-0194 | ADR-B-06 | 309 | 4 | 15 | brak formalnego alarmu |
| ADR-B-0049 | ADR-B-05 | 307 | 4 | 17 | brak formalnego alarmu |
| ADR-B-0014 | ADR-B-05 | 382 | 4 | 18 | brak formalnego alarmu |
| ADR-B-0583 | ADR-B-07 | 342 | 4 | 20 | brak formalnego alarmu |
| ADR-B-0517 | ADR-B-07 | 335 | 4 | 16 | brak formalnego alarmu |
| ADR-B-0183 | ADR-B-05 | 320 | 4 | 17 | brak formalnego alarmu |
| ADR-B-0301 | ADR-B-01 | 352 | 4 | 21 | brak formalnego alarmu |
| ADR-B-0304 | ADR-B-12 | 356 | 4 | 24 | brak formalnego alarmu |
| ADR-B-0212 | ADR-B-12 | 368 | 4 | 25 | brak formalnego alarmu |
| ADR-B-0407 | ADR-B-12 | 311 | 4 | 14 | brak formalnego alarmu |
| ADR-B-0016 | ADR-B-06 | 378 | 4 | 24 | brak formalnego alarmu |
| ADR-B-0432 | ADR-B-11 | 325 | 4 | 21 | brak formalnego alarmu |
| ADR-B-0502 | ADR-B-02 | 303 | 4 | 17 | brak formalnego alarmu |
| ADR-B-0078 | ADR-B-09 | 359 | 4 | 15 | brak formalnego alarmu |
| ADR-B-0196 | ADR-B-07 | 373 | 4 | 20 | brak formalnego alarmu |
| ADR-B-0148 | ADR-B-01 | 369 | 4 | 16 | brak formalnego alarmu |
| ADR-B-0237 | ADR-B-09 | 341 | 4 | 16 | brak formalnego alarmu |
| ADR-B-0198 | ADR-B-08 | 361 | 4 | 20 | brak formalnego alarmu |
| ADR-B-0545 | ADR-B-06 | 382 | 4 | 19 | brak formalnego alarmu |
| ADR-B-0032 | ADR-B-11 | 322 | 4 | 18 | brak formalnego alarmu |

## Lekcje B-10–13 i program

Zachowano wyniki poprzedniego przeglądu 4x77: w B-10 wyjaśniono oznaczenie DOT, w B-11 kod tunelowy, w B-13 napis SALVAGE PACKAGING; B-12 nie miała potwierdzonej usterki. W obecnej partii nie dokonano kolejnej niezależnej literalnej kontroli prawnej tych rozdziałów. Nie zgłoszono potwierdzonej luki kompetencji z urzędową podstawą ADR, więc nie dodano pytań od 0610. Egzaminy i pakiet recenzyjny pozostają na banku 609 pytań: brak zmiany pytań i przypisania modułów, dlatego ich nie regenerowano.

## Granice odbioru

Nie przeprowadzono pełnego porównania wszystkich wskazanych punktów ADR 2025 z polskim tekstem Dz.U. 2025 poz. 642 i sprostowaniem poz. 1575. Nie nadano statusu `verified`. Po tej partii należy kontynuować pogłębiony ręczny audyt pozycji oznaczonych heurystycznie i niezależną weryfikację prawną.
