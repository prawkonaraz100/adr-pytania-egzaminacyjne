# Etap 4x74 — screening niejasnych pytań, lekcje B-01–04 i próba 60 wyjaśnień

Data: 27.10.2026. Punkt wyjścia: świeży main `1a8f14b0de78f2e39a48cf5bf5712fb74a539232`, CI PASS [run 40444166060](https://github.com/prawkonaraz100/adr-pytania-egzaminacyjne/actions/runs/40444166060). Wyłącznie kurs podstawowy.

## Bank i Quality Gate
- 609 pytań; 609 `needs_review`, 0 `verified`.
- Poprawna odpowiedź jedyną najdłuższą: **73/609 = 11.99%**, limit 18%.
- Najkrótsze explanation: 300 znaków. Krótsze niż 200 znaków: 0.
- Rozkład modułowy: ADR-B-01: 13.33% (6/45); ADR-B-02: 14.29% (8/56); ADR-B-03: 14.29% (7/49); ADR-B-04: 13.04% (6/46); ADR-B-05: 11.63% (5/43); ADR-B-06: 11.11% (5/45); ADR-B-07: 12.50% (6/48); ADR-B-08: 11.90% (5/42); ADR-B-09: 8.70% (4/46); ADR-B-10: 7.27% (4/55); ADR-B-11: 13.95% (6/43); ADR-B-12: 13.64% (6/44); ADR-B-13: 10.64% (5/47).

## Screening 609 treści pytań

Zastosowano filtry długości pytania (>175 znaków), występowania więcej niż jednej negacji i skrótów LQ/EQ/MEMU/DGSA/RID/IMDG/EX/II/EX/III. To heurystyka **wysokiej czułości, nie potwierdzenie błędu**. Łącznie oznaczono **91** rekordów. Czytano kontekst i nie odwracano odpowiedzi wyłącznie z powodu wystąpienia „nie” lub technicznego skrótu.

Lista ID do dalszego ręcznego przeglądu:
- ADR-B-0029 — ADR-B-10
- ADR-B-0033 — ADR-B-11
- ADR-B-0078 — ADR-B-09
- ADR-B-0085 — ADR-B-11
- ADR-B-0091 — ADR-B-01
- ADR-B-0093 — ADR-B-01
- ADR-B-0119 — ADR-B-10
- ADR-B-0140 — ADR-B-10
- ADR-B-0142 — ADR-B-10
- ADR-B-0149 — ADR-B-01
- ADR-B-0198 — ADR-B-08
- ADR-B-0199 — ADR-B-09
- ADR-B-0201 — ADR-B-09
- ADR-B-0202 — ADR-B-09
- ADR-B-0203 — ADR-B-10
- ADR-B-0204 — ADR-B-10
- ADR-B-0206 — ADR-B-10
- ADR-B-0209 — ADR-B-11
- ADR-B-0241 — ADR-B-03
- ADR-B-0260 — ADR-B-01
- ADR-B-0261 — ADR-B-01
- ADR-B-0263 — ADR-B-11
- ADR-B-0271 — ADR-B-01
- ADR-B-0273 — ADR-B-01
- ADR-B-0277 — ADR-B-10
- ADR-B-0278 — ADR-B-10
- ADR-B-0294 — ADR-B-03
- ADR-B-0318 — ADR-B-03
- ADR-B-0320 — ADR-B-10
- ADR-B-0321 — ADR-B-10
- ADR-B-0322 — ADR-B-11
- ADR-B-0324 — ADR-B-09
- ADR-B-0328 — ADR-B-03
- ADR-B-0383 — ADR-B-10
- ADR-B-0384 — ADR-B-10
- ADR-B-0385 — ADR-B-10
- ADR-B-0386 — ADR-B-10
- ADR-B-0387 — ADR-B-10
- ADR-B-0388 — ADR-B-10
- ADR-B-0398 — ADR-B-10
- ADR-B-0402 — ADR-B-12
- ADR-B-0429 — ADR-B-09
- ADR-B-0443 — ADR-B-10
- ADR-B-0444 — ADR-B-10
- ADR-B-0446 — ADR-B-10
- ADR-B-0447 — ADR-B-10
- ADR-B-0448 — ADR-B-10
- ADR-B-0462 — ADR-B-03
- ADR-B-0473 — ADR-B-04
- ADR-B-0479 — ADR-B-07
- ADR-B-0487 — ADR-B-11
- ADR-B-0494 — ADR-B-05
- ADR-B-0500 — ADR-B-02
- ADR-B-0501 — ADR-B-02
- ADR-B-0507 — ADR-B-06
- ADR-B-0508 — ADR-B-13
- ADR-B-0509 — ADR-B-08
- ADR-B-0511 — ADR-B-10
- ADR-B-0512 — ADR-B-11
- ADR-B-0513 — ADR-B-01
- ADR-B-0514 — ADR-B-03
- ADR-B-0515 — ADR-B-04
- ADR-B-0516 — ADR-B-05
- ADR-B-0517 — ADR-B-07
- ADR-B-0519 — ADR-B-12
- ADR-B-0522 — ADR-B-01
- ADR-B-0523 — ADR-B-13
- ADR-B-0526 — ADR-B-01
- ADR-B-0527 — ADR-B-01
- ADR-B-0528 — ADR-B-01
- ADR-B-0530 — ADR-B-13
- ADR-B-0532 — ADR-B-13
- ADR-B-0533 — ADR-B-13
- ADR-B-0534 — ADR-B-01
- ADR-B-0535 — ADR-B-01
- ADR-B-0536 — ADR-B-13
- ADR-B-0539 — ADR-B-11
- ADR-B-0540 — ADR-B-11
- ADR-B-0550 — ADR-B-06
- ADR-B-0551 — ADR-B-08
- ADR-B-0565 — ADR-B-06
- ADR-B-0572 — ADR-B-01
- ADR-B-0573 — ADR-B-01
- ADR-B-0579 — ADR-B-13
- ADR-B-0587 — ADR-B-13
- ADR-B-0601 — ADR-B-13
- ADR-B-0602 — ADR-B-11
- ADR-B-0605 — ADR-B-01
- ADR-B-0607 — ADR-B-01
- ADR-B-0608 — ADR-B-01
- ADR-B-0609 — ADR-B-01

| ID | Obserwacja i decyzja |
|---|---|
| ADR-B-0173 | Pytanie «Co wynika?» i odpowiedź zaczynająca się od «Nie» mogą być językowo niezgrabne; brak podstaw do samodzielnego zmienienia klucza. |
| ADR-B-0240 | Pytanie «Kiedy może odstąpić?» z odpowiedzią «Nie; ...» ma problem formy; wymagany osobny audyt rekordu i snapshotów. |
| ADR-B-0501 | Dwa wystąpienia negacji nie tworzą automatycznie podwójnego zaprzeczenia; kontekst dotyczy niespełnionego warunku. |
| ADR-B-0607 | Sformułowanie o braku zaświadczenia i braku wyłączenia jest złożone; kandydat do uproszczenia wraz z synchronizacją wariantów i audytów. |
| ADR-B-0579 | «Nie zawiera» i «nie zachodzi wyjątek» wyjaśniają wymaganie; bez potwierdzenia błędu prawnego nie zmieniono odpowiedzi. |

**Potwierdzone merytoryczne błędy ADR możliwe do korekty na podstawie samego screeningu: 0.** Nie zmieniano banku, poprawnych liter ani explanation tylko na podstawie heurystyki. Wskazane niejasności leksykalne wymagające powiązanych aktualizacji zapisano do dalszego przeglądu.

## Przegląd lekcji 01–04

| Lekcja | Wynik | Potwierdzona poprawka |
|---|---|---|
| B-01 | Wyjaśnienia numeru UN, LQ, EQ oraz obliczenia 1.1.3.6 już poprzedzają ćwiczenia i podsumowanie. | Nie zmieniano bez potwierdzonej potrzeby. |
| B-02 | Wprowadzenie do odczytu klasy powielało ogólną instrukcję „wyjaśnij rozbieżność” zamiast wskazać kroki. | Zmieniono na konkretną czynność: porównanie przesyłki z dokumentem i tabelą A, wyjaśnienie różnic przed przewozem. Treść prawna bez zmiany. |
| B-03 | Rozdzielono znak zagrożenia dla środowiska, odpady i postępowanie przy wycieku. Objaśnione limity 5 l / 5 kg oraz znaczenie opakowania. | Nie stwierdzono potwierdzonego błędu do zmiany. |
| B-04 | Suchy zapis „ADR wymaga wyłączenia silnika” nie wyjaśniał kierowcy sensu praktycznego. | Zastąpiono instrukcją „wyłącz silnik”, dodano uzasadnienie bezpieczeństwa i rozróżnienie wyjątku dotyczącego napędzania urządzeń (ADR 8.3.6). |

Nie dodano numerowanych pytań: screening nie potwierdził nowej luki programu z kompletną podstawą prawną. Wydania urzędowe do późniejszej weryfikacji specjalisty: ADR 2025 Dz.U. poz. 642 i sprostowanie Dz.U. poz. 1575.

## Próba 60 explanation — rotacja, pełna jawność

Algorytm: seed `2026102774`, posortowane ID, LCG `state=(1664525×state+1013904223) mod 2^32`, Fisher–Yates. Priorytet rekordów niewystępujących w pliku wykluczeń etapów 4x51–4x66 i tabelach prób 4x71–4x72. W tej próbie **54** ID są spoza tak zdefiniowanego zbioru, a pozostałe 6 to rotacja. Nie deklarujemy bezpodstawnie, że są niewidziane w każdym raporcie aż do 4x73.

| ID | Dział | Znaki | Zdania* | Najdłuższe zdanie (słowa)* | Wynik |
|---|---|---:|---:|---:|---|
| ADR-B-0259 | ADR-B-01 | 304 | 4 | 19 | bez potwierdzonej potrzeby zmiany |
| ADR-B-0333 | ADR-B-03 | 326 | 4 | 17 | bez potwierdzonej potrzeby zmiany |
| ADR-B-0098 | ADR-B-02 | 395 | 4 | 21 | bez potwierdzonej potrzeby zmiany |
| ADR-B-0330 | ADR-B-03 | 335 | 4 | 22 | bez potwierdzonej potrzeby zmiany |
| ADR-B-0406 | ADR-B-12 | 328 | 4 | 16 | bez potwierdzonej potrzeby zmiany |
| ADR-B-0441 | ADR-B-10 | 359 | 4 | 17 | bez potwierdzonej potrzeby zmiany |
| ADR-B-0447 | ADR-B-10 | 358 | 4 | 23 | bez potwierdzonej potrzeby zmiany |
| ADR-B-0271 | ADR-B-01 | 329 | 5 | 19 | bez potwierdzonej potrzeby zmiany |
| ADR-B-0428 | ADR-B-09 | 322 | 4 | 14 | bez potwierdzonej potrzeby zmiany |
| ADR-B-0366 | ADR-B-07 | 376 | 4 | 29 | bez potwierdzonej potrzeby zmiany |
| ADR-B-0161 | ADR-B-02 | 343 | 4 | 17 | bez potwierdzonej potrzeby zmiany |
| ADR-B-0325 | ADR-B-03 | 409 | 4 | 28 | bez potwierdzonej potrzeby zmiany |
| ADR-B-0538 | ADR-B-13 | 374 | 4 | 16 | bez potwierdzonej potrzeby zmiany |
| ADR-B-0450 | ADR-B-10 | 374 | 4 | 20 | bez potwierdzonej potrzeby zmiany |
| ADR-B-0316 | ADR-B-02 | 333 | 4 | 16 | bez potwierdzonej potrzeby zmiany |
| ADR-B-0359 | ADR-B-04 | 314 | 4 | 14 | bez potwierdzonej potrzeby zmiany |
| ADR-B-0005 | ADR-B-02 | 316 | 4 | 16 | bez potwierdzonej potrzeby zmiany |
| ADR-B-0286 | ADR-B-09 | 333 | 4 | 18 | bez potwierdzonej potrzeby zmiany |
| ADR-B-0224 | ADR-B-05 | 329 | 4 | 17 | bez potwierdzonej potrzeby zmiany |
| ADR-B-0165 | ADR-B-05 | 352 | 4 | 17 | bez potwierdzonej potrzeby zmiany |
| ADR-B-0115 | ADR-B-06 | 409 | 4 | 25 | bez potwierdzonej potrzeby zmiany |
| ADR-B-0009 | ADR-B-03 | 390 | 4 | 19 | bez potwierdzonej potrzeby zmiany |
| ADR-B-0396 | ADR-B-10 | 352 | 5 | 14 | bez potwierdzonej potrzeby zmiany |
| ADR-B-0446 | ADR-B-10 | 313 | 4 | 20 | bez potwierdzonej potrzeby zmiany |
| ADR-B-0206 | ADR-B-10 | 361 | 4 | 19 | bez potwierdzonej potrzeby zmiany |
| ADR-B-0141 | ADR-B-10 | 378 | 4 | 19 | bez potwierdzonej potrzeby zmiany |
| ADR-B-0589 | ADR-B-13 | 331 | 4 | 17 | bez potwierdzonej potrzeby zmiany |
| ADR-B-0459 | ADR-B-12 | 313 | 4 | 20 | bez potwierdzonej potrzeby zmiany |
| ADR-B-0276 | ADR-B-03 | 312 | 4 | 19 | bez potwierdzonej potrzeby zmiany |
| ADR-B-0571 | ADR-B-01 | 374 | 4 | 24 | bez potwierdzonej potrzeby zmiany |
| ADR-B-0371 | ADR-B-07 | 339 | 4 | 19 | bez potwierdzonej potrzeby zmiany |
| ADR-B-0028 | ADR-B-10 | 382 | 5 | 16 | bez potwierdzonej potrzeby zmiany |
| ADR-B-0351 | ADR-B-04 | 358 | 5 | 15 | bez potwierdzonej potrzeby zmiany |
| ADR-B-0381 | ADR-B-10 | 393 | 3 | 34 | bez potwierdzonej potrzeby zmiany |
| ADR-B-0474 | ADR-B-04 | 305 | 3 | 26 | bez potwierdzonej potrzeby zmiany |
| ADR-B-0531 | ADR-B-13 | 413 | 4 | 21 | bez potwierdzonej potrzeby zmiany |
| ADR-B-0372 | ADR-B-07 | 343 | 4 | 15 | bez potwierdzonej potrzeby zmiany |
| ADR-B-0536 | ADR-B-13 | 374 | 4 | 24 | bez potwierdzonej potrzeby zmiany |
| ADR-B-0570 | ADR-B-01 | 345 | 4 | 22 | bez potwierdzonej potrzeby zmiany |
| ADR-B-0114 | ADR-B-06 | 405 | 4 | 23 | bez potwierdzonej potrzeby zmiany |
| ADR-B-0521 | ADR-B-01 | 323 | 4 | 18 | bez potwierdzonej potrzeby zmiany |
| ADR-B-0238 | ADR-B-09 | 333 | 4 | 16 | bez potwierdzonej potrzeby zmiany |
| ADR-B-0329 | ADR-B-03 | 377 | 4 | 19 | bez potwierdzonej potrzeby zmiany |
| ADR-B-0139 | ADR-B-09 | 406 | 5 | 22 | bez potwierdzonej potrzeby zmiany |
| ADR-B-0176 | ADR-B-08 | 312 | 4 | 15 | bez potwierdzonej potrzeby zmiany |
| ADR-B-0273 | ADR-B-01 | 354 | 4 | 25 | bez potwierdzonej potrzeby zmiany |
| ADR-B-0278 | ADR-B-10 | 442 | 4 | 31 | bez potwierdzonej potrzeby zmiany |
| ADR-B-0209 | ADR-B-11 | 430 | 4 | 29 | bez potwierdzonej potrzeby zmiany |
| ADR-B-0296 | ADR-B-04 | 319 | 4 | 23 | bez potwierdzonej potrzeby zmiany |
| ADR-B-0395 | ADR-B-10 | 325 | 4 | 18 | bez potwierdzonej potrzeby zmiany |
| ADR-B-0476 | ADR-B-04 | 313 | 4 | 19 | bez potwierdzonej potrzeby zmiany |
| ADR-B-0331 | ADR-B-03 | 381 | 4 | 21 | bez potwierdzonej potrzeby zmiany |
| ADR-B-0266 | ADR-B-02 | 431 | 4 | 19 | bez potwierdzonej potrzeby zmiany |
| ADR-B-0374 | ADR-B-07 | 315 | 4 | 13 | bez potwierdzonej potrzeby zmiany |
| ADR-B-0189 | ADR-B-06 | 390 | 4 | 20 | bez potwierdzonej potrzeby zmiany |
| ADR-B-0354 | ADR-B-04 | 322 | 4 | 18 | bez potwierdzonej potrzeby zmiany |
| ADR-B-0309 | ADR-B-02 | 317 | 4 | 16 | bez potwierdzonej potrzeby zmiany |
| ADR-B-0545 | ADR-B-06 | 382 | 4 | 19 | bez potwierdzonej potrzeby zmiany |
| ADR-B-0170 | ADR-B-06 | 302 | 4 | 16 | bez potwierdzonej potrzeby zmiany |
| ADR-B-0601 | ADR-B-13 | 362 | 4 | 20 | bez potwierdzonej potrzeby zmiany |

*Prosta segmentacja zdań i liczenie słów służą do wskazania kandydatów, nie oceny prawa. Wszystkie 60 wyjaśnień mają 2–5 segmentów w tej metodzie, 300–500 znaków oraz brak zdań powyżej 35 słów. Przegląd otwarć i zakończeń potwierdził opis praktycznej decyzji oraz krótką podstawę ADR. Nie znaleziono tu potwierdzonej konieczności nadpisania explanation — **0 zmian**. Dalsza niezależna kontrola A/B/C i polskiego brzmienia przepisu pozostaje otwarta.

## Synchronizacja i bezpieczeństwo zmian
- Bank `questions.jsonl` **nie został zmieniony**: brak zmian ID, kluczy, dystraktorów i statusów.
- Arkusze egzaminów i klucze nie wymagają regeneracji z powodu samych zmian językowych w B-02 i B-04.
- Pakiet recenzyjny i liczba pytań pozostają bez zmian; lista flag w tym raporcie jest dodatkową kolejką przeglądu.
- Formalny release pozostaje zablokowany dla wszystkich `needs_review`. Nie dotykano kursu cystern.

