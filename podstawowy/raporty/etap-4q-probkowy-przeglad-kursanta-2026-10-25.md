# Etap 4q — próbkowy przegląd wyjaśnień „oczami kursanta”

- Data przeglądu: 25.10.2026.
- Świeży `main` przed zmianami: `28abf1c9ac336b5d216a66d57ec871b7a8b3055a` (PR #272; wskaźniki zsynchronizowane).
- Bank: 566 pytań, wszystkie `needs_review`; brak `verified`.
- Losowanie: seed `202610250050`, generator Mulberry32, Fisher–Yates osobno w każdym dziale, pierwsze 5 pozycji z przetasowanej puli każdego działu.
- Próba: **65 pytań — 5 z każdego z 13 działów**, bez powtórzeń. Dokładne ID i seed zapisano w `etap-4q-probka.json`; test CI sprawdza istnienie ID i liczebność działów.

## Kryteria oceny

Każde z 65 wyjaśnień przeczytano w kontekście pytania i opcji A/B/C. Sprawdzono: (1) czy od razu wyjaśnia sens i dlaczego klucz jest poprawny, (2) czy osobno lub jednoznacznie odrzuca obie błędne opcje, (3) czy podstawa ADR jest na końcu, (4) czy język jest przystępny bez wcześniejszej wiedzy, (5) czy nie ma pustych, powtarzanych formuł ani widocznej sprzeczności z pytaniem.

**Wynik próbki:** 65/65 przechodzi redakcyjne kryteria minimalne; wszystkie wyjaśnienia kończą się krótką podstawą ADR. Nie stwierdzono powtarzalnego schematu „Ta odpowiedź jest błędna, ponieważ…” ani potwierdzonej nieprawdy w zakresie widocznym w próbie. Nie znaleziono potwierdzonego błędu wymagającego zmiany explanation, dlatego nie zmieniano treści pytań, kluczy, źródeł ani statusów. To wynik próbkowy, nie dowód poprawności całego banku ani opinia prawna.

## Wynik per dział

| Dział | Wynik | Uwaga dla kursanta |
|---|---|---|
| ADR-B-01 | 5/5 PASS | Wyjaśnienia tłumaczą limity, jednostkę transportową i szkolenie; przykłady pokazują, dlaczego nie wolno mieszać różnych wyłączeń. |
| ADR-B-02 | 5/5 PASS | Klasy i nalepki opisano przez konkretne zagrożenia; porównania z klasami mylącymi są zrozumiałe. |
| ADR-B-03 | 5/5 PASS | Jest praktyczny skutek wycieku i zasada, by nie zgadywać klasyfikacji odpadu; warunki i wyjątki są zaznaczone. |
| ADR-B-04 | 5/5 PASS | Wyjaśnienia przekładają zakazy na czynności kierowcy i odrzucają błędne działania z praktycznych sytuacji. |
| ADR-B-05 | 5/5 PASS | Priorytet bezpieczeństwa i granice samodzielnego działania są jasne; wyjaśnienia nie zachęcają do ryzykownej interwencji. |
| ADR-B-06 | 5/5 PASS | Rozróżniono nalepki, tablice i numery; wyjaśnienia wskazują, co kierowca ma sprawdzić. |
| ADR-B-07 | 5/5 PASS | Odpowiedzialność uczestników jest opisana konkretnie; nie sugeruje się, że jeden dokument zastępuje obowiązki innych. |
| ADR-B-08 | 5/5 PASS | Liczba gaśnic i łączna pojemność są rozdzielone, a wymogi pojazdu opisane z zastrzeżeniem zakresu. |
| ADR-B-09 | 5/5 PASS | Wyjaśnienia odnoszą zgodność załadunku i czystość do kolejnych działań; zgoda kierowcy nie zastępuje warunków ADR. |
| ADR-B-10 | 5/5 PASS | Różnice ADR/RID/IMDG i wyjątki przewozu łączonego są tłumaczone bez sugerowania automatycznego zwolnienia. |
| ADR-B-11 | 5/5 PASS | Kody tunelowe powiązano z kategorią tunelu i postacią przewozu; ostrzeżono przed czytaniem samej litery bez kontekstu. |
| ADR-B-12 | 5/5 PASS | Wymogi ochrony wyjaśniono przez identyfikację, nadzór i plan ochrony; nie użyto zbędnego żargonu bez kontekstu. |
| ADR-B-13 | 5/5 PASS | Wpisy dokumentu i dokument tożsamości rozróżniono praktycznie; podstawa ADR znajduje się na końcu. |

## Rekordy w próbce

| Dział | ID pytania | Długość explanation (znaki) | Ocena |
|---|---|---:|---|
| ADR-B-01 | ADR-B-0323 | 323 | PASS |
| ADR-B-01 | ADR-B-0147 | 334 | PASS |
| ADR-B-01 | ADR-B-0261 | 331 | PASS |
| ADR-B-01 | ADR-B-0529 | 334 | PASS |
| ADR-B-01 | ADR-B-0149 | 314 | PASS |
| ADR-B-02 | ADR-B-0043 | 304 | PASS |
| ADR-B-02 | ADR-B-0005 | 316 | PASS |
| ADR-B-02 | ADR-B-0161 | 343 | PASS |
| ADR-B-02 | ADR-B-0269 | 316 | PASS |
| ADR-B-02 | ADR-B-0162 | 340 | PASS |
| ADR-B-03 | ADR-B-0007 | 327 | PASS |
| ADR-B-03 | ADR-B-0332 | 427 | PASS |
| ADR-B-03 | ADR-B-0514 | 327 | PASS |
| ADR-B-03 | ADR-B-0340 | 346 | PASS |
| ADR-B-03 | ADR-B-0318 | 338 | PASS |
| ADR-B-04 | ADR-B-0353 | 315 | PASS |
| ADR-B-04 | ADR-B-0346 | 339 | PASS |
| ADR-B-04 | ADR-B-0047 | 343 | PASS |
| ADR-B-04 | ADR-B-0296 | 319 | PASS |
| ADR-B-04 | ADR-B-0358 | 343 | PASS |
| ADR-B-05 | ADR-B-0223 | 374 | PASS |
| ADR-B-05 | ADR-B-0221 | 336 | PASS |
| ADR-B-05 | ADR-B-0231 | 331 | PASS |
| ADR-B-05 | ADR-B-0232 | 405 | PASS |
| ADR-B-05 | ADR-B-0166 | 326 | PASS |
| ADR-B-06 | ADR-B-0565 | 367 | PASS |
| ADR-B-06 | ADR-B-0546 | 337 | PASS |
| ADR-B-06 | ADR-B-0217 | 382 | PASS |
| ADR-B-06 | ADR-B-0505 | 311 | PASS |
| ADR-B-06 | ADR-B-0561 | 351 | PASS |
| ADR-B-07 | ADR-B-0376 | 309 | PASS |
| ADR-B-07 | ADR-B-0021 | 355 | PASS |
| ADR-B-07 | ADR-B-0363 | 330 | PASS |
| ADR-B-07 | ADR-B-0482 | 416 | PASS |
| ADR-B-07 | ADR-B-0378 | 321 | PASS |
| ADR-B-08 | ADR-B-0176 | 312 | PASS |
| ADR-B-08 | ADR-B-0418 | 318 | PASS |
| ADR-B-08 | ADR-B-0075 | 317 | PASS |
| ADR-B-08 | ADR-B-0072 | 376 | PASS |
| ADR-B-08 | ADR-B-0419 | 324 | PASS |
| ADR-B-09 | ADR-B-0058 | 334 | PASS |
| ADR-B-09 | ADR-B-0428 | 322 | PASS |
| ADR-B-09 | ADR-B-0080 | 397 | PASS |
| ADR-B-09 | ADR-B-0429 | 324 | PASS |
| ADR-B-09 | ADR-B-0291 | 321 | PASS |
| ADR-B-10 | ADR-B-0439 | 333 | PASS |
| ADR-B-10 | ADR-B-0396 | 352 | PASS |
| ADR-B-10 | ADR-B-0440 | 316 | PASS |
| ADR-B-10 | ADR-B-0454 | 398 | PASS |
| ADR-B-10 | ADR-B-0387 | 311 | PASS |
| ADR-B-11 | ADR-B-0264 | 303 | PASS |
| ADR-B-11 | ADR-B-0539 | 347 | PASS |
| ADR-B-11 | ADR-B-0033 | 320 | PASS |
| ADR-B-11 | ADR-B-0085 | 376 | PASS |
| ADR-B-11 | ADR-B-0262 | 336 | PASS |
| ADR-B-12 | ADR-B-0400 | 314 | PASS |
| ADR-B-12 | ADR-B-0034 | 333 | PASS |
| ADR-B-12 | ADR-B-0035 | 334 | PASS |
| ADR-B-12 | ADR-B-0275 | 323 | PASS |
| ADR-B-12 | ADR-B-0399 | 352 | PASS |
| ADR-B-13 | ADR-B-0250 | 327 | PASS |
| ADR-B-13 | ADR-B-0533 | 359 | PASS |
| ADR-B-13 | ADR-B-0068 | 315 | PASS |
| ADR-B-13 | ADR-B-0508 | 317 | PASS |
| ADR-B-13 | ADR-B-0215 | 316 | PASS |

## Przegląd po jednym akapicie z każdej lekcji

Przejrzano wprowadzenie/akapit objaśniający i nawigację do przykładów praktycznych oraz powiązanych ID pytań w każdej lekcji. Wszystkie 13 lekcji mają prosty kontekst, cele albo wyjaśnienie tematu oraz odsyłacze do banku. Nie znaleziono potwierdzonego błędu merytorycznego na podstawie tego przeglądu, więc nie przepisano akapitów i nie zmieniano podstaw prawnych. Drobne uwagi są nawigacyjne, a nie blokujące: w B-02 tabela klas wymaga pracy na przykładzie UN; w B-08 tabela gaśnic wyraźnie zaznacza zakres i potrzebę sprawdzenia pełnego przepisu; w B-11 kody tunelowe pozostają techniczne i powinny być ćwiczone na przykładach.

| Lekcja | Ocena | Obserwacja |
|---|---|---|
| ADR-B-01 | PASS z uwagą | Początek definiuje ADR i pokazuje, że wyłączenia są różne; przykład pracownika od dokumentów odróżnia szkolenie 1.3 od zaświadczenia kierowcy 8.2. |
| ADR-B-02 | PASS | Cele, tabela klas, numer UN, grupa pakowania i przykłady pokazują, czego szukać w tabeli A. Dla początkującego rozbudowana tabela wymaga pracy z realnym przykładem UN. |
| ADR-B-03 | PASS | Przykład wycieku przy kanalizacji oraz scenariusz odpadu pokazują praktyczne decyzje; warunek bezpiecznego działania jest zaznaczony. |
| ADR-B-04 | PASS | Oddziela zakaz palenia, wyłączenie silnika i zakaz otwierania opakowań, podając przykłady kierowcy. |
| ADR-B-05 | PASS | Kolejność działań, granice gaszenia i pierwsza pomoc są przedstawione z naciskiem na niepodejmowanie ryzyka; ćwiczenia wymagają instruktora. |
| ADR-B-06 | PASS | Numer UN, numer zagrożenia, nalepki i tablice są odróżnione; scenariusze opierają się na rzeczywistych oznaczeniach. |
| ADR-B-07 | PASS | Tabela uczestników i przykłady pokazują, kto powinien usunąć konkretną niezgodność; kierowca ma zgłaszać widoczne problemy. |
| ADR-B-08 | PASS z uwagą | Tabela gaśnic jest czytelna i rozwinięto DMC. Autor sam zaznacza, że tabela nie wyczerpuje wszystkich wymagań — czytelnik musi sięgnąć do punktu ADR. |
| ADR-B-09 | PASS | Kontrola przed załadunkiem, wspólny załadunek i mocowanie opisano przez decyzje praktyczne, kiedy wstrzymać czynność. |
| ADR-B-10 | PASS | ADR, RID i IMDG są rozwinięte i porównane; przykłady portowe pokazują, że etap morski nie zwalnia automatycznie z ADR. |
| ADR-B-11 | PASS z uwagą | Kategorie, kody i sposób przewozu są pokazane na przykładach; temat jest techniczny, ale wyjaśnienie D/E ogranicza ryzyko mechanicznego zapamiętania. |
| ADR-B-12 | PASS | Termin „security” odróżniono od zabezpieczenia ładunku; scenariusze odbioru przez nieznaną firmę i postoju są zrozumiałe. |
| ADR-B-13 | PASS | Lista pól dokumentu i przykład kontroli pokazują, czego szukać; słusznie zaznaczono, że instrukcje pisemne nie zastępują dokumentu przewozowego. |

## Wskaźnik „poprawna = najdłuższa”

Na świeżym banku 71/566 = **12,54%** globalnie. Każdy dział pozostaje poniżej progu 18%; szczegóły egzekwuje `scripts/answer_length_bias.py --threshold 0.18 --strict`. Nie zmieniano żadnej opcji w tej partii.

## Ograniczenia i dalszy krok

To przegląd redakcyjny, nie pełna weryfikacja prawna. Wszystkie pytania pozostają `needs_review`; nie nadano `verified`. Następną luką jakościową jest kontrola pokrycia praktycznego: sprawdzić, czy trzy ćwiczenia mają mierzalne kryteria oceny i czy testy CI zapobiegają traktowaniu quizu jako zaliczenia praktyki.
