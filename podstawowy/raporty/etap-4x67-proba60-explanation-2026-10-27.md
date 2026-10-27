# Etap 4x67 — uzupełniająca próba 60 wyjaśnień, bez powtarzania wcześniejszych prób

Data: 27.10.2026. Źródłowy `main`: `0850d4093ad6f37d3fe453b732e72fdbc6b782ab`. Przedmiot: wyłącznie kurs podstawowy ADR.

## Dobór próby
- Przeskanowano 20 raportów 4x51–4x66, wszystkie literalne wystąpienia identyfikatorów `ADR-B-NNNN` wykluczono zachowawczo, również te spoza tabel próby. [Rejestr źródeł i ID](etap-4x67-wykluczenia-prób.json).
- Lista wykluczeń: 551 oznaczeń, w tym fikcyjny `ADR-B-0610` występujący w raporcie jako przyszłe ID; 550 istniejących rekordów. Zostało 59 rekordów banku, które nigdzie nie pojawiły się w poprzednich raportach.
- Dodano dwóch kandydatów `ADR-B-0600` i `ADR-B-0605`, wspomnianych **wyłącznie** w 4x66 (karta kontroli przed wyjazdem, nie próba explanation). Nie występują w innych raportach 4x51–4x65, więc nie powtarzają poprzednich próbek wyjaśnień.
- Połącznie dostępnych było 61 ID. Użyto deterministycznego seeda **2026102767**, sortowania ID i mieszania Fisher–Yates z LCG: `state = (1664525 × state + 1013904223) mod 2^32`. Pobrano pierwsze 60 ID; pominięte ID: `ADR-B-0259`.

## Ocena języka
Każde z wybranych 60 explanation poddano kontroli długości, liczby zdań, długości zdań, początku tekstu, odwołania do ADR i uzasadnienia pomyłki. Sprawdzono podejrzane wyniki heurystyki: sam brak dosłownego słowa „błędna” nie oznacza braku wyjaśnienia, jeśli tekst wprost opisuje, dlaczego konkretna alternatywa nie działa.

| Lp. | ID | Dział | Znaki | Zdania | Najdłuższe zdanie (słowa) | Ocena |
|---:|---|---|---:|---:|---:|---|
| 1 | ADR-B-0351 | ADR-B-04 | 358 | 5 | 15 | Brak sygnału problemu; Bez potwierdzonej potrzeby zmiany |
| 2 | ADR-B-0474 | ADR-B-04 | 305 | 3 | 26 | Brak słowa kluczowego; sprawdzono opis błędnej opcji w treści; Bez potwierdzonej potrzeby zmiany |
| 3 | ADR-B-0366 | ADR-B-07 | 376 | 4 | 29 | Brak słowa kluczowego; sprawdzono opis błędnej opcji w treści; Bez potwierdzonej potrzeby zmiany |
| 4 | ADR-B-0531 | ADR-B-13 | 413 | 4 | 21 | Brak słowa kluczowego; sprawdzono opis błędnej opcji w treści; Bez potwierdzonej potrzeby zmiany |
| 5 | ADR-B-0209 | ADR-B-11 | 430 | 4 | 29 | Brak słowa kluczowego; sprawdzono opis błędnej opcji w treści; Bez potwierdzonej potrzeby zmiany |
| 6 | ADR-B-0296 | ADR-B-04 | 319 | 4 | 23 | Brak słowa kluczowego; sprawdzono opis błędnej opcji w treści; Bez potwierdzonej potrzeby zmiany |
| 7 | ADR-B-0009 | ADR-B-03 | 390 | 4 | 19 | Brak sygnału problemu; Bez potwierdzonej potrzeby zmiany |
| 8 | ADR-B-0447 | ADR-B-10 | 358 | 4 | 23 | Brak słowa kluczowego; sprawdzono opis błędnej opcji w treści; Bez potwierdzonej potrzeby zmiany |
| 9 | ADR-B-0331 | ADR-B-03 | 381 | 4 | 21 | Brak sygnału problemu; Bez potwierdzonej potrzeby zmiany |
| 10 | ADR-B-0333 | ADR-B-03 | 326 | 4 | 17 | Brak sygnału problemu; Bez potwierdzonej potrzeby zmiany |
| 11 | ADR-B-0490 | ADR-B-11 | 323 | 4 | 20 | Brak sygnału problemu; Bez potwierdzonej potrzeby zmiany |
| 12 | ADR-B-0371 | ADR-B-07 | 339 | 4 | 19 | Brak sygnału problemu; Bez potwierdzonej potrzeby zmiany |
| 13 | ADR-B-0329 | ADR-B-03 | 377 | 4 | 19 | Brak słowa kluczowego; sprawdzono opis błędnej opcji w treści; Bez potwierdzonej potrzeby zmiany |
| 14 | ADR-B-0459 | ADR-B-12 | 313 | 4 | 20 | Brak sygnału problemu; Bez potwierdzonej potrzeby zmiany |
| 15 | ADR-B-0538 | ADR-B-13 | 374 | 4 | 16 | Brak sygnału problemu; Bez potwierdzonej potrzeby zmiany |
| 16 | ADR-B-0098 | ADR-B-02 | 395 | 4 | 21 | Brak słowa kluczowego; sprawdzono opis błędnej opcji w treści; Bez potwierdzonej potrzeby zmiany |
| 17 | ADR-B-0396 | ADR-B-10 | 352 | 5 | 14 | Brak słowa kluczowego; sprawdzono opis błędnej opcji w treści; Bez potwierdzonej potrzeby zmiany |
| 18 | ADR-B-0206 | ADR-B-10 | 361 | 4 | 19 | Brak sygnału problemu; Bez potwierdzonej potrzeby zmiany |
| 19 | ADR-B-0536 | ADR-B-13 | 374 | 4 | 24 | Brak słowa kluczowego; sprawdzono opis błędnej opcji w treści; Bez potwierdzonej potrzeby zmiany |
| 20 | ADR-B-0238 | ADR-B-09 | 333 | 4 | 16 | Brak słowa kluczowego; sprawdzono opis błędnej opcji w treści; Bez potwierdzonej potrzeby zmiany |
| 21 | ADR-B-0224 | ADR-B-05 | 329 | 4 | 17 | Brak słowa kluczowego; sprawdzono opis błędnej opcji w treści; Bez potwierdzonej potrzeby zmiany |
| 22 | ADR-B-0141 | ADR-B-10 | 378 | 4 | 19 | Brak sygnału problemu; Bez potwierdzonej potrzeby zmiany |
| 23 | ADR-B-0139 | ADR-B-09 | 406 | 5 | 22 | Brak sygnału problemu; Bez potwierdzonej potrzeby zmiany |
| 24 | ADR-B-0406 | ADR-B-12 | 328 | 4 | 16 | Brak sygnału problemu; Bez potwierdzonej potrzeby zmiany |
| 25 | ADR-B-0176 | ADR-B-08 | 312 | 4 | 15 | Brak słowa kluczowego; sprawdzono opis błędnej opcji w treści; Bez potwierdzonej potrzeby zmiany |
| 26 | ADR-B-0286 | ADR-B-09 | 333 | 4 | 18 | Brak sygnału problemu; Bez potwierdzonej potrzeby zmiany |
| 27 | ADR-B-0276 | ADR-B-03 | 312 | 4 | 19 | Brak sygnału problemu; Bez potwierdzonej potrzeby zmiany |
| 28 | ADR-B-0395 | ADR-B-10 | 325 | 4 | 18 | Brak słowa kluczowego; sprawdzono opis błędnej opcji w treści; Bez potwierdzonej potrzeby zmiany |
| 29 | ADR-B-0605 | ADR-B-01 | 424 | 4 | 20 | Brak sygnału problemu; Bez potwierdzonej potrzeby zmiany |
| 30 | ADR-B-0372 | ADR-B-07 | 343 | 4 | 15 | Brak sygnału problemu; Bez potwierdzonej potrzeby zmiany |
| 31 | ADR-B-0359 | ADR-B-04 | 314 | 4 | 14 | Brak sygnału problemu; Bez potwierdzonej potrzeby zmiany |
| 32 | ADR-B-0428 | ADR-B-09 | 322 | 4 | 14 | Brak sygnału problemu; Bez potwierdzonej potrzeby zmiany |
| 33 | ADR-B-0600 | ADR-B-13 | 338 | 4 | 15 | Brak sygnału problemu; Bez potwierdzonej potrzeby zmiany |
| 34 | ADR-B-0161 | ADR-B-02 | 343 | 4 | 17 | Brak słowa kluczowego; sprawdzono opis błędnej opcji w treści; Bez potwierdzonej potrzeby zmiany |
| 35 | ADR-B-0441 | ADR-B-10 | 359 | 4 | 17 | Brak sygnału problemu; Bez potwierdzonej potrzeby zmiany |
| 36 | ADR-B-0330 | ADR-B-03 | 335 | 4 | 22 | Brak sygnału problemu; Bez potwierdzonej potrzeby zmiany |
| 37 | ADR-B-0316 | ADR-B-02 | 333 | 4 | 16 | Brak słowa kluczowego; sprawdzono opis błędnej opcji w treści; Bez potwierdzonej potrzeby zmiany |
| 38 | ADR-B-0570 | ADR-B-01 | 345 | 4 | 22 | Brak sygnału problemu; Bez potwierdzonej potrzeby zmiany |
| 39 | ADR-B-0165 | ADR-B-05 | 352 | 4 | 17 | Brak sygnału problemu; Bez potwierdzonej potrzeby zmiany |
| 40 | ADR-B-0521 | ADR-B-01 | 323 | 4 | 18 | Brak słowa kluczowego; sprawdzono opis błędnej opcji w treści; Bez potwierdzonej potrzeby zmiany |
| 41 | ADR-B-0450 | ADR-B-10 | 374 | 4 | 20 | Brak sygnału problemu; Bez potwierdzonej potrzeby zmiany |
| 42 | ADR-B-0114 | ADR-B-06 | 405 | 4 | 23 | Brak sygnału problemu; Bez potwierdzonej potrzeby zmiany |
| 43 | ADR-B-0571 | ADR-B-01 | 374 | 4 | 24 | Brak sygnału problemu; Bez potwierdzonej potrzeby zmiany |
| 44 | ADR-B-0317 | ADR-B-02 | 430 | 4 | 18 | Brak sygnału problemu; Bez potwierdzonej potrzeby zmiany |
| 45 | ADR-B-0446 | ADR-B-10 | 313 | 4 | 20 | Brak sygnału problemu; Bez potwierdzonej potrzeby zmiany |
| 46 | ADR-B-0028 | ADR-B-10 | 382 | 5 | 16 | Brak sygnału problemu; Bez potwierdzonej potrzeby zmiany |
| 47 | ADR-B-0005 | ADR-B-02 | 316 | 4 | 16 | Brak słowa kluczowego; sprawdzono opis błędnej opcji w treści; Bez potwierdzonej potrzeby zmiany |
| 48 | ADR-B-0381 | ADR-B-10 | 393 | 3 | 34 | Brak sygnału problemu; Bez potwierdzonej potrzeby zmiany |
| 49 | ADR-B-0278 | ADR-B-10 | 442 | 4 | 31 | Brak sygnału problemu; Bez potwierdzonej potrzeby zmiany |
| 50 | ADR-B-0374 | ADR-B-07 | 315 | 4 | 13 | Brak sygnału problemu; Bez potwierdzonej potrzeby zmiany |
| 51 | ADR-B-0266 | ADR-B-02 | 431 | 4 | 19 | Brak sygnału problemu; Bez potwierdzonej potrzeby zmiany |
| 52 | ADR-B-0240 | ADR-B-09 | 347 | 4 | 17 | Brak sygnału problemu; Bez potwierdzonej potrzeby zmiany |
| 53 | ADR-B-0476 | ADR-B-04 | 313 | 4 | 19 | Brak słowa kluczowego; sprawdzono opis błędnej opcji w treści; Bez potwierdzonej potrzeby zmiany |
| 54 | ADR-B-0325 | ADR-B-03 | 409 | 4 | 28 | Brak słowa kluczowego; sprawdzono opis błędnej opcji w treści; Bez potwierdzonej potrzeby zmiany |
| 55 | ADR-B-0115 | ADR-B-06 | 409 | 4 | 25 | Brak sygnału problemu; Bez potwierdzonej potrzeby zmiany |
| 56 | ADR-B-0271 | ADR-B-01 | 329 | 5 | 19 | Brak sygnału problemu; Bez potwierdzonej potrzeby zmiany |
| 57 | ADR-B-0273 | ADR-B-01 | 354 | 4 | 25 | Brak sygnału problemu; Bez potwierdzonej potrzeby zmiany |
| 58 | ADR-B-0089 | ADR-B-13 | 426 | 4 | 28 | Brak sygnału problemu; Bez potwierdzonej potrzeby zmiany |
| 59 | ADR-B-0589 | ADR-B-13 | 331 | 4 | 17 | Brak sygnału problemu; Bez potwierdzonej potrzeby zmiany |
| 60 | ADR-B-0508 | ADR-B-13 | 356 | 4 | 21 | Brak sygnału problemu; Bez potwierdzonej potrzeby zmiany |

## Wynik i ograniczenia
- Liczba ocenionych rekordów: **60 unikalnych ID**; żaden nie znajduje się w poprzednich próbach explanation 4x51–4x65.
- Wszystkie zawierają 3–5 zdań, 300–500 znaków i odwołanie do podstawy ADR; żadna kontrolowana długość zdania nie przekracza 35 słów.
- W 20 rekordach proste wyszukiwanie słów o błędach zwróciło potencjalny fałszywy alarm; opisy zawierają jednak zaprzeczenie mylącemu postępowaniu, odwołanie do konkretnej alternatywy albo kontrast z właściwą regułą.
- Nie stwierdzono na podstawie przeglądu tekstu jednozdaniowych ani przepisowych wyjaśnień wymagających mechanicznej poprawki. **0 zmian banku, kluczy i liter odpowiedzi.**
- Odbiór językowy oraz heurystyka nie stanowią niezależnego potwierdzenia poprawności prawnej. Wszystkie pytania nadal `needs_review`, 0 `verified`.

## Kontrola Quality Gate
Bank 609 pytań. Poprawna odpowiedź jest jedyną najdłuższą 72/609 = **11,82%**, poniżej limitu 18%; min. explanation 300 znaków. CI dla PR wymagany przed scaleniem. Nie ma potwierdzonej luki programu uzasadniającej dodanie ADR-B-0610. Wariantów egzaminu i pakietu recenzyjnego nie zmieniano, bo bank i przydziały działów pozostały identyczne.
