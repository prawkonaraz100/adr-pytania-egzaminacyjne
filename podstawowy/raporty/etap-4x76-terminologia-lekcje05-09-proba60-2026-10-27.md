# Etap 4x76 — kontrola słownictwa banku i lekcji B-05–09 oraz rotacyjna próba 60

Data: 27.10.2026. Punkt wyjścia: świeży main `c51ddca17419fdcb1b4ab7916f0f750e77350b93` po PR #533. Ostatni Quality Gate main: PASS [run #40449427193](https://github.com/prawkonaraz100/adr-pytania-egzaminacyjne/actions/runs/40449427193). Zakres: **wyłącznie kurs podstawowy**.

## Bank i kontrola terminologii

609 unikalnych pytań ADR-B-0001–0609; 609 `needs_review`, 0 `verified`; żadnych zmian numeracji, kluczy odpowiedzi ani podstaw prawnych w tej partii. Odsetek, gdy poprawna odpowiedź jest jedyną najdłuższą: **73/609 = 11.99%** (limit 18%); najkrótsze explanation **300 znaków** (minimum 200).

Przeprowadzono pełne skanowanie pól `stem`, `options` i `explanation` wszystkich 609 pytań pod kątem słownictwa charakterystycznego dla ADR. Przykładowe wyniki, liczba rekordów zawierających frazę:

| Termin / wariant | Rekordy | Wniosek |
|---|---:|---|
| instrukcje pisemne vs pisemne instrukcje | 1 | W ADR-B-0049 występuje wariant szyku „pisemne instrukcje”; sens jest czytelny, ale forma nazwy dokumentu wymaga potwierdzenia urzędowego i kontroli snapshotów przed ewentualną zmianą pytania. |
| towar w sztukach przesyłek | 23 | Zwroty występują kontekstowo; nie wolno ich podmieniać mechanicznie bez uwzględnienia odmiany, liczby i definicji. |
| jednostka transportowa | 22 | Zwroty występują kontekstowo; nie wolno ich podmieniać mechanicznie bez uwzględnienia odmiany, liczby i definicji. |
| kategoria transportowa | 8 | Zwroty występują kontekstowo; nie wolno ich podmieniać mechanicznie bez uwzględnienia odmiany, liczby i definicji. |
| numer UN | 62 | Zwroty występują kontekstowo; nie wolno ich podmieniać mechanicznie bez uwzględnienia odmiany, liczby i definicji. |

Zestawienie to **screening terminologiczny**, a nie formalne literalne porównanie z każdym punktem polskiego ADR 2025. Nie znaleziono podstaw, aby automatycznie zamieniać np. „sztuka przesyłki” na „jednostka transportowa”: oznaczają różne rzeczy. Wszelkie sporne nazwy i wartości wymagają porównania konkretnego przepisu z [Dz.U. 2025 poz. 642](https://dziennikustaw.gov.pl/DU/2025/642) i [sprostowaniem poz. 1575](https://dziennikustaw.gov.pl/DU/2025/1575).

## Próba 60 explanation — jawne zasady doboru

W raporcie wykluczeń `etap-4x67-wykluczenia-prób.json` znajduje się 551 różnych ID pojawiających się w raportach 4x51–4x66. Pozostawało 59 niewymienionych tam ID, dlatego **nie da się utworzyć 60 całkowicie nowych względem tego okresu**. Do 59 dołączono rotacyjnie ADR-B-0001 (jedno jawne powtórzenie). Nie opisujemy próby jako rozłącznej względem wszystkich 4x51–4x75, bo późniejsze raporty też mogły wymieniać te pozycje.

Przeczytano wszystkie 60 explanation z bieżącego banku i porównano z odpowiedzią właściwą oraz dystraktorami. Przegląd wykazał, że wyjaśnienia przedstawiają sens właściwego zachowania i odnoszą się do błędnych kierunków wyboru; nie stwierdzono jednozdaniowego tekstu ani wyjaśnienia bez podstawy ADR. Jedna pozycja ADR-B-0098 ma zdanie graniczne ok. 36 słów — sens jest prosty, więc sama długość nie uzasadnia ingerencji w klucz/snapshoty. **Wyjaśnień przepisanych: 0; kandydatów do specjalistycznego przeglądu prawnego: 0 nowych na podstawie tej próby.**

| ID | Dział | Długość explanation | Wynik kontroli |
|---|---|---:|---|
| ADR-B-0005 | ADR-B-02 | 316 | Czytelne; brak potwierdzonej wady językowej wymagającej zmiany |
| ADR-B-0009 | ADR-B-03 | 390 | Czytelne; brak potwierdzonej wady językowej wymagającej zmiany |
| ADR-B-0028 | ADR-B-10 | 382 | Czytelne; brak potwierdzonej wady językowej wymagającej zmiany |
| ADR-B-0089 | ADR-B-13 | 426 | Czytelne; brak potwierdzonej wady językowej wymagającej zmiany |
| ADR-B-0098 | ADR-B-02 | 395 | Czytelne; jedno zdanie ok. 36 słów, nie wymaga zmiany wyłącznie z powodu heurystyki |
| ADR-B-0114 | ADR-B-06 | 405 | Czytelne; brak potwierdzonej wady językowej wymagającej zmiany |
| ADR-B-0115 | ADR-B-06 | 409 | Czytelne; brak potwierdzonej wady językowej wymagającej zmiany |
| ADR-B-0139 | ADR-B-09 | 406 | Czytelne; brak potwierdzonej wady językowej wymagającej zmiany |
| ADR-B-0141 | ADR-B-10 | 378 | Czytelne; brak potwierdzonej wady językowej wymagającej zmiany |
| ADR-B-0161 | ADR-B-02 | 343 | Czytelne; brak potwierdzonej wady językowej wymagającej zmiany |
| ADR-B-0165 | ADR-B-05 | 352 | Czytelne; brak potwierdzonej wady językowej wymagającej zmiany |
| ADR-B-0176 | ADR-B-08 | 312 | Czytelne; brak potwierdzonej wady językowej wymagającej zmiany |
| ADR-B-0206 | ADR-B-10 | 361 | Czytelne; brak potwierdzonej wady językowej wymagającej zmiany |
| ADR-B-0209 | ADR-B-11 | 430 | Czytelne; brak potwierdzonej wady językowej wymagającej zmiany |
| ADR-B-0224 | ADR-B-05 | 329 | Czytelne; brak potwierdzonej wady językowej wymagającej zmiany |
| ADR-B-0238 | ADR-B-09 | 333 | Czytelne; brak potwierdzonej wady językowej wymagającej zmiany |
| ADR-B-0240 | ADR-B-09 | 347 | Czytelne; brak potwierdzonej wady językowej wymagającej zmiany |
| ADR-B-0259 | ADR-B-01 | 304 | Czytelne; brak potwierdzonej wady językowej wymagającej zmiany |
| ADR-B-0266 | ADR-B-02 | 431 | Czytelne; brak potwierdzonej wady językowej wymagającej zmiany |
| ADR-B-0271 | ADR-B-01 | 329 | Czytelne; brak potwierdzonej wady językowej wymagającej zmiany |
| ADR-B-0273 | ADR-B-01 | 354 | Czytelne; brak potwierdzonej wady językowej wymagającej zmiany |
| ADR-B-0276 | ADR-B-03 | 312 | Czytelne; brak potwierdzonej wady językowej wymagającej zmiany |
| ADR-B-0278 | ADR-B-10 | 442 | Czytelne; brak potwierdzonej wady językowej wymagającej zmiany |
| ADR-B-0286 | ADR-B-09 | 333 | Czytelne; brak potwierdzonej wady językowej wymagającej zmiany |
| ADR-B-0296 | ADR-B-04 | 319 | Czytelne; brak potwierdzonej wady językowej wymagającej zmiany |
| ADR-B-0316 | ADR-B-02 | 333 | Czytelne; brak potwierdzonej wady językowej wymagającej zmiany |
| ADR-B-0317 | ADR-B-02 | 430 | Czytelne; brak potwierdzonej wady językowej wymagającej zmiany |
| ADR-B-0325 | ADR-B-03 | 409 | Czytelne; brak potwierdzonej wady językowej wymagającej zmiany |
| ADR-B-0329 | ADR-B-03 | 377 | Czytelne; brak potwierdzonej wady językowej wymagającej zmiany |
| ADR-B-0330 | ADR-B-03 | 335 | Czytelne; brak potwierdzonej wady językowej wymagającej zmiany |
| ADR-B-0331 | ADR-B-03 | 381 | Czytelne; brak potwierdzonej wady językowej wymagającej zmiany |
| ADR-B-0333 | ADR-B-03 | 326 | Czytelne; brak potwierdzonej wady językowej wymagającej zmiany |
| ADR-B-0351 | ADR-B-04 | 358 | Czytelne; brak potwierdzonej wady językowej wymagającej zmiany |
| ADR-B-0359 | ADR-B-04 | 314 | Czytelne; brak potwierdzonej wady językowej wymagającej zmiany |
| ADR-B-0366 | ADR-B-07 | 376 | Czytelne; brak potwierdzonej wady językowej wymagającej zmiany |
| ADR-B-0371 | ADR-B-07 | 339 | Czytelne; brak potwierdzonej wady językowej wymagającej zmiany |
| ADR-B-0372 | ADR-B-07 | 343 | Czytelne; brak potwierdzonej wady językowej wymagającej zmiany |
| ADR-B-0374 | ADR-B-07 | 315 | Czytelne; brak potwierdzonej wady językowej wymagającej zmiany |
| ADR-B-0381 | ADR-B-10 | 393 | Czytelne; brak potwierdzonej wady językowej wymagającej zmiany |
| ADR-B-0395 | ADR-B-10 | 325 | Czytelne; brak potwierdzonej wady językowej wymagającej zmiany |
| ADR-B-0396 | ADR-B-10 | 352 | Czytelne; brak potwierdzonej wady językowej wymagającej zmiany |
| ADR-B-0406 | ADR-B-12 | 328 | Czytelne; brak potwierdzonej wady językowej wymagającej zmiany |
| ADR-B-0428 | ADR-B-09 | 322 | Czytelne; brak potwierdzonej wady językowej wymagającej zmiany |
| ADR-B-0441 | ADR-B-10 | 359 | Czytelne; brak potwierdzonej wady językowej wymagającej zmiany |
| ADR-B-0446 | ADR-B-10 | 313 | Czytelne; brak potwierdzonej wady językowej wymagającej zmiany |
| ADR-B-0447 | ADR-B-10 | 358 | Czytelne; brak potwierdzonej wady językowej wymagającej zmiany |
| ADR-B-0450 | ADR-B-10 | 374 | Czytelne; brak potwierdzonej wady językowej wymagającej zmiany |
| ADR-B-0459 | ADR-B-12 | 313 | Czytelne; brak potwierdzonej wady językowej wymagającej zmiany |
| ADR-B-0474 | ADR-B-04 | 305 | Czytelne; brak potwierdzonej wady językowej wymagającej zmiany |
| ADR-B-0476 | ADR-B-04 | 313 | Czytelne; brak potwierdzonej wady językowej wymagającej zmiany |
| ADR-B-0490 | ADR-B-11 | 323 | Czytelne; brak potwierdzonej wady językowej wymagającej zmiany |
| ADR-B-0508 | ADR-B-13 | 356 | Czytelne; brak potwierdzonej wady językowej wymagającej zmiany |
| ADR-B-0521 | ADR-B-01 | 323 | Czytelne; brak potwierdzonej wady językowej wymagającej zmiany |
| ADR-B-0531 | ADR-B-13 | 413 | Czytelne; brak potwierdzonej wady językowej wymagającej zmiany |
| ADR-B-0536 | ADR-B-13 | 374 | Czytelne; brak potwierdzonej wady językowej wymagającej zmiany |
| ADR-B-0538 | ADR-B-13 | 374 | Czytelne; brak potwierdzonej wady językowej wymagającej zmiany |
| ADR-B-0570 | ADR-B-01 | 345 | Czytelne; brak potwierdzonej wady językowej wymagającej zmiany |
| ADR-B-0571 | ADR-B-01 | 374 | Czytelne; brak potwierdzonej wady językowej wymagającej zmiany |
| ADR-B-0589 | ADR-B-13 | 331 | Czytelne; brak potwierdzonej wady językowej wymagającej zmiany |
| ADR-B-0001 | ADR-B-01 | 325 | Czytelne; brak potwierdzonej wady językowej wymagającej zmiany |

## Lekcje B-05–09 — przegląd kursanta i zmiany

| Lekcja | Kontrola | Potwierdzona korekta redakcyjna |
|---|---|---|
| B-05 | Instrukcje pisemne, bezpieczeństwo po wypadku, informacje dla ratowników, sprzęt | Wyjaśniono „stronę nawietrzną” bezpośrednio przy pierwszym zaleceniu: to strona, skąd wieje wiatr; dzięki temu kursant rozumie, jak unikać oparów. |
| B-06 | Numer UN, numer zagrożenia, tablice i wymiary 40 × 30 cm / 300 × 120 mm, czytelność nalepek | Nie stwierdzono potwierdzonej nowej niespójności redakcyjnej wymagającej zmiany. |
| B-07 | Nadawca, przewoźnik, załadowca, dokumenty i role | Doprecyzowano „klasyfikację” prostymi słowami jako przypisanie towaru do odpowiedniej pozycji i zagrożenia ADR. |
| B-08 | DMC, minimum gaśnic, wymagana liczba i wyposażenie osobiste | Wyjaśniono, dlaczego jedna większa gaśnica nie zastępuje dwóch, jeżeli obowiązuje wymóg dwóch urządzeń. |
| B-09 | Wspólny załadunek, CV28, luzem, pakowanie i czyszczenie | Objaśniono CV28 bezpośrednio przy pierwszej wzmiance jako dodatkowy warunek załadunku wskazany dla danego towaru. |

W każdej z tych lekcji zachowano praktyczne scenariusze, pytania kontrolne, podsumowania i odwołania do banku. Nie zmieniono liczbowych progów ani merytoryki bez potwierdzenia brzmienia ADR. Lekcje B-05–09 oraz bank mogą nadal wymagać niezależnej weryfikacji specjalistycznej.

## Pokrycie programu i egzaminy

Nie stwierdzono w tej partii **potwierdzonej** nowej luki programu dającej podstawę do dodania pytania 0610. Liczba pytań i przypisania działów nie zmieniły się, więc nie regenerowano egzaminów próbnych 001–005 ani pakietu recenzyjnego tylko z powodu zmian redakcyjnych w lekcjach. Raport przeznaczony dla specjalisty zawiera punkty wrażliwe na brzmienie terminów; status wszystkich pytań pozostaje `needs_review`.

## Następny krok

Osobna partia 4x77 powinna objąć terminologię lekcji B-10–13 i potwierdzenie potencjalnych rozbieżności na poziomie pojedynczego punktu ADR, z zachowaniem niezmiennych kluczy, dopóki tekst urzędowy nie potwierdzi korekty.
