# Etap 4r — próbkowy przegląd „oczami kursanta”

- Data: 25.10.2026.
- Świeży `main` przed zmianami: `72c0d1e4d21267eed5ded09713a775e957047c48`.
- Bank: 566 pytań; statusy bez zmian.
- Seed LCG 32-bit (1664525, 1013904223): `202610250010`; Fisher–Yates osobno w każdym dziale, po 4 rekordy, z wykluczeniem wszystkich ID wymienionych w raporcie 4q.
- Próbka: 52 pytań, dokładnie 4 z każdego z 13 działów; żadnego powtórzenia z próbką 4q.

## Kryteria i wynik

Każde wyjaśnienie oceniono względem pięciu kryteriów: (1) najpierw prosty sens i powód poprawności, (2) odniesienie do obu błędnych opcji, (3) krótka podstawa ADR na końcu, (4) język zrozumiały dla kursanta bez wcześniejszej wiedzy, (5) brak powtarzanego pustego szablonu i widocznej sprzeczności z pytaniem. Wszystkie 52 próbki mają 300–500 znaków i kończą się podstawą ADR. Nie znaleziono powtarzalnego szablonu typu „Ta odpowiedź jest błędna, ponieważ…”. Jedno potwierdzone uproszczenie dotyczyło niewyjaśnionego pojęcia „klasa 7” w ADR-B-0342; poprawiono wyjaśnienie i zachowano klucz, źródło oraz status. Nie znaleziono podstaw do innych zmian merytorycznych w tej próbce.

## Wynik dla każdego pytania

| Dział | ID | Długość wyjaśnienia | Ocena |
|---|---|---:|---|
| ADR-B-01 | ADR-B-0521 | 323 | PASS — sens odpowiedzi, obie błędne możliwości i podstawa na końcu; brak zauważonego szablonu lub niezrozumiałego terminu blokującego sens. |
| ADR-B-01 | ADR-B-0529 | 334 | PASS — sens odpowiedzi, obie błędne możliwości i podstawa na końcu; brak zauważonego szablonu lub niezrozumiałego terminu blokującego sens. |
| ADR-B-01 | ADR-B-0273 | 304 | PASS — sens odpowiedzi, obie błędne możliwości i podstawa na końcu; brak zauważonego szablonu lub niezrozumiałego terminu blokującego sens. |
| ADR-B-01 | ADR-B-0272 | 392 | PASS — sens odpowiedzi, obie błędne możliwości i podstawa na końcu; brak zauważonego szablonu lub niezrozumiałego terminu blokującego sens. |
| ADR-B-02 | ADR-B-0315 | 322 | PASS — sens odpowiedzi, obie błędne możliwości i podstawa na końcu; brak zauważonego szablonu lub niezrozumiałego terminu blokującego sens. |
| ADR-B-02 | ADR-B-0094 | 318 | PASS — sens odpowiedzi, obie błędne możliwości i podstawa na końcu; brak zauważonego szablonu lub niezrozumiałego terminu blokującego sens. |
| ADR-B-02 | ADR-B-0309 | 317 | PASS — sens odpowiedzi, obie błędne możliwości i podstawa na końcu; brak zauważonego szablonu lub niezrozumiałego terminu blokującego sens. |
| ADR-B-02 | ADR-B-0289 | 301 | PASS — sens odpowiedzi, obie błędne możliwości i podstawa na końcu; brak zauważonego szablonu lub niezrozumiałego terminu blokującego sens. |
| ADR-B-03 | ADR-B-0468 | 357 | PASS — sens odpowiedzi, obie błędne możliwości i podstawa na końcu; brak zauważonego szablonu lub niezrozumiałego terminu blokującego sens. |
| ADR-B-03 | ADR-B-0342 | 326 | POPRAWIONO — wyjaśniono, że klasa 7 oznacza materiały promieniotwórcze; doprecyzowano sens reguły i obu dystraktorów. |
| ADR-B-03 | ADR-B-0179 | 336 | PASS — sens odpowiedzi, obie błędne możliwości i podstawa na końcu; brak zauważonego szablonu lub niezrozumiałego terminu blokującego sens. |
| ADR-B-03 | ADR-B-0007 | 327 | PASS — sens odpowiedzi, obie błędne możliwości i podstawa na końcu; brak zauważonego szablonu lub niezrozumiałego terminu blokującego sens. |
| ADR-B-04 | ADR-B-0279 | 325 | PASS — sens odpowiedzi, obie błędne możliwości i podstawa na końcu; brak zauważonego szablonu lub niezrozumiałego terminu blokującego sens. |
| ADR-B-04 | ADR-B-0297 | 327 | PASS — sens odpowiedzi, obie błędne możliwości i podstawa na końcu; brak zauważonego szablonu lub niezrozumiałego terminu blokującego sens. |
| ADR-B-04 | ADR-B-0011 | 366 | PASS — sens odpowiedzi, obie błędne możliwości i podstawa na końcu; brak zauważonego szablonu lub niezrozumiałego terminu blokującego sens. |
| ADR-B-04 | ADR-B-0346 | 339 | PASS — sens odpowiedzi, obie błędne możliwości i podstawa na końcu; brak zauważonego szablonu lub niezrozumiałego terminu blokującego sens. |
| ADR-B-05 | ADR-B-0219 | 356 | PASS — sens odpowiedzi, obie błędne możliwości i podstawa na końcu; brak zauważonego szablonu lub niezrozumiałego terminu blokującego sens. |
| ADR-B-05 | ADR-B-0166 | 326 | PASS — sens odpowiedzi, obie błędne możliwości i podstawa na końcu; brak zauważonego szablonu lub niezrozumiałego terminu blokującego sens. |
| ADR-B-05 | ADR-B-0165 | 320 | PASS — sens odpowiedzi, obie błędne możliwości i podstawa na końcu; brak zauważonego szablonu lub niezrozumiałego terminu blokującego sens. |
| ADR-B-05 | ADR-B-0187 | 318 | PASS — sens odpowiedzi, obie błędne możliwości i podstawa na końcu; brak zauważonego szablonu lub niezrozumiałego terminu blokującego sens. |
| ADR-B-06 | ADR-B-0550 | 325 | PASS — sens odpowiedzi, obie błędne możliwości i podstawa na końcu; brak zauważonego szablonu lub niezrozumiałego terminu blokującego sens. |
| ADR-B-06 | ADR-B-0132 | 364 | PASS — sens odpowiedzi, obie błędne możliwości i podstawa na końcu; brak zauważonego szablonu lub niezrozumiałego terminu blokującego sens. |
| ADR-B-06 | ADR-B-0549 | 315 | PASS — sens odpowiedzi, obie błędne możliwości i podstawa na końcu; brak zauważonego szablonu lub niezrozumiałego terminu blokującego sens. |
| ADR-B-06 | ADR-B-0257 | 303 | PASS — sens odpowiedzi, obie błędne możliwości i podstawa na końcu; brak zauważonego szablonu lub niezrozumiałego terminu blokującego sens. |
| ADR-B-07 | ADR-B-0019 | 322 | PASS — sens odpowiedzi, obie błędne możliwości i podstawa na końcu; brak zauważonego szablonu lub niezrozumiałego terminu blokującego sens. |
| ADR-B-07 | ADR-B-0118 | 327 | PASS — sens odpowiedzi, obie błędne możliwości i podstawa na końcu; brak zauważonego szablonu lub niezrozumiałego terminu blokującego sens. |
| ADR-B-07 | ADR-B-0195 | 368 | PASS — sens odpowiedzi, obie błędne możliwości i podstawa na końcu; brak zauważonego szablonu lub niezrozumiałego terminu blokującego sens. |
| ADR-B-07 | ADR-B-0246 | 329 | PASS — sens odpowiedzi, obie błędne możliwości i podstawa na końcu; brak zauważonego szablonu lub niezrozumiałego terminu blokującego sens. |
| ADR-B-08 | ADR-B-0553 | 327 | PASS — sens odpowiedzi, obie błędne możliwości i podstawa na końcu; brak zauważonego szablonu lub niezrozumiałego terminu blokującego sens. |
| ADR-B-08 | ADR-B-0023 | 360 | PASS — sens odpowiedzi, obie błędne możliwości i podstawa na końcu; brak zauważonego szablonu lub niezrozumiałego terminu blokującego sens. |
| ADR-B-08 | ADR-B-0024 | 315 | PASS — sens odpowiedzi, obie błędne możliwości i podstawa na końcu; brak zauważonego szablonu lub niezrozumiałego terminu blokującego sens. |
| ADR-B-08 | ADR-B-0075 | 317 | PASS — sens odpowiedzi, obie błędne możliwości i podstawa na końcu; brak zauważonego szablonu lub niezrozumiałego terminu blokującego sens. |
| ADR-B-09 | ADR-B-0079 | 417 | PASS — sens odpowiedzi, obie błędne możliwości i podstawa na końcu; brak zauważonego szablonu lub niezrozumiałego terminu blokującego sens. |
| ADR-B-09 | ADR-B-0027 | 405 | PASS — sens odpowiedzi, obie błędne możliwości i podstawa na końcu; brak zauważonego szablonu lub niezrozumiałego terminu blokującego sens. |
| ADR-B-09 | ADR-B-0425 | 305 | PASS — sens odpowiedzi, obie błędne możliwości i podstawa na końcu; brak zauważonego szablonu lub niezrozumiałego terminu blokującego sens. |
| ADR-B-09 | ADR-B-0554 | 321 | PASS — sens odpowiedzi, obie błędne możliwości i podstawa na końcu; brak zauważonego szablonu lub niezrozumiałego terminu blokującego sens. |
| ADR-B-10 | ADR-B-0119 | 316 | PASS — sens odpowiedzi, obie błędne możliwości i podstawa na końcu; brak zauważonego szablonu lub niezrozumiałego terminu blokującego sens. |
| ADR-B-10 | ADR-B-0446 | 313 | PASS — sens odpowiedzi, obie błędne możliwości i podstawa na końcu; brak zauważonego szablonu lub niezrozumiałego terminu blokującego sens. |
| ADR-B-10 | ADR-B-0390 | 349 | PASS — sens odpowiedzi, obie błędne możliwości i podstawa na końcu; brak zauważonego szablonu lub niezrozumiałego terminu blokującego sens. |
| ADR-B-10 | ADR-B-0439 | 333 | PASS — sens odpowiedzi, obie błędne możliwości i podstawa na końcu; brak zauważonego szablonu lub niezrozumiałego terminu blokującego sens. |
| ADR-B-11 | ADR-B-0435 | 365 | PASS — sens odpowiedzi, obie błędne możliwości i podstawa na końcu; brak zauważonego szablonu lub niezrozumiałego terminu blokującego sens. |
| ADR-B-11 | ADR-B-0430 | 338 | PASS — sens odpowiedzi, obie błędne możliwości i podstawa na końcu; brak zauważonego szablonu lub niezrozumiałego terminu blokującego sens. |
| ADR-B-11 | ADR-B-0490 | 323 | PASS — sens odpowiedzi, obie błędne możliwości i podstawa na końcu; brak zauważonego szablonu lub niezrozumiałego terminu blokującego sens. |
| ADR-B-11 | ADR-B-0064 | 323 | PASS — sens odpowiedzi, obie błędne możliwości i podstawa na końcu; brak zauważonego szablonu lub niezrozumiałego terminu blokującego sens. |
| ADR-B-12 | ADR-B-0415 | 362 | PASS — sens odpowiedzi, obie błędne możliwości i podstawa na końcu; brak zauważonego szablonu lub niezrozumiałego terminu blokującego sens. |
| ADR-B-12 | ADR-B-0455 | 318 | PASS — sens odpowiedzi, obie błędne możliwości i podstawa na końcu; brak zauważonego szablonu lub niezrozumiałego terminu blokującego sens. |
| ADR-B-12 | ADR-B-0409 | 339 | PASS — sens odpowiedzi, obie błędne możliwości i podstawa na końcu; brak zauważonego szablonu lub niezrozumiałego terminu blokującego sens. |
| ADR-B-12 | ADR-B-0275 | 323 | PASS — sens odpowiedzi, obie błędne możliwości i podstawa na końcu; brak zauważonego szablonu lub niezrozumiałego terminu blokującego sens. |
| ADR-B-13 | ADR-B-0088 | 332 | PASS — sens odpowiedzi, obie błędne możliwości i podstawa na końcu; brak zauważonego szablonu lub niezrozumiałego terminu blokującego sens. |
| ADR-B-13 | ADR-B-0037 | 308 | PASS — sens odpowiedzi, obie błędne możliwości i podstawa na końcu; brak zauważonego szablonu lub niezrozumiałego terminu blokującego sens. |
| ADR-B-13 | ADR-B-0530 | 318 | PASS — sens odpowiedzi, obie błędne możliwości i podstawa na końcu; brak zauważonego szablonu lub niezrozumiałego terminu blokującego sens. |
| ADR-B-13 | ADR-B-0533 | 359 | PASS — sens odpowiedzi, obie błędne możliwości i podstawa na końcu; brak zauważonego szablonu lub niezrozumiałego terminu blokującego sens. |

## Kontrola 13 lekcji — po jednym akapicie na lekcję

- **ADR-B-01:** Wprowadzenie definiuje zakres ADR i rozróżnia szkolenie pracownika od uprawnień kierowcy; skróty LQ/EQ/1.1.3.6 są zapowiedziane jako różne mechanizmy, a dalej objaśniane.
- **ADR-B-02:** Lekcja wyjaśnia klasę, numer UN i tabelę A przed szczegółami klas; klasyfikacje są specjalistyczne, ale opisane przykładami i odsyłaczami.
- **ADR-B-03:** Znak środowiskowy opisano przez rybę/drzewo, a wyciek przez bezpieczne działania; czytelny przykład praktyczny, z zastrzeżeniem, by nie działać w rozlewie.
- **ADR-B-04:** Zakaz palenia, e-papierosów, otwierania opakowań i zasady postoju podano jako odrębne sytuacje; tekst daje jasne przykłady kierowcy.
- **ADR-B-05:** Cele nauki koncentrują się na bezpieczeństwie własnym, wezwaniu służb i rozróżnieniu pożaru ładowni od małego pożaru pojazdu; podkreślono granice samodzielnej pomocy.
- **ADR-B-06:** Lekcja od początku rozdziela numer UN, nalepkę i tablicę; przykład z numerami na tablicy ułatwia praktyczny odczyt.
- **ADR-B-07:** Tabela uczestników przekłada obowiązki na nadawcę, przewoźnika i odbiorcę; przykłady pokazują, że kierowca nie odpowiada za wszystko, ale nie może ignorować widocznej niezgodności.
- **ADR-B-08:** Tabela wyposażenia i gaśnic jest praktyczna; potwierdzony problem pierwszego użycia skrótu DMC bez rozwinięcia poprawiono na „dopuszczalnej masy całkowitej (DMC)”.
- **ADR-B-09:** Lekcja rozpoczyna od kontroli przed załadunkiem i daje konkretny przykład niesprawnego sprzętu; wspólny załadunek i mocowanie są powiązane z decyzją, kiedy przerwać pracę.
- **ADR-B-10:** ADR, RID i IMDG są rozwinięte osobno; przykład kontenera po rejsie pokazuje, że morski etap nie zwalnia automatycznie z kontroli drogowej.
- **ADR-B-11:** Kategorie tuneli A–E i kod (-) opisano językiem praktycznych decyzji o trasie; tekst ostrzega, że kategoria ADR nie uchyla innych znaków drogowych.
- **ADR-B-12:** Na początku wyjaśniono, że „ochrona/security” dotyczy kradzieży i nieuprawnionego użycia, a nie mocowania; dalsze reguły mają kontekst praktyczny.
- **ADR-B-13:** Lista pól dokumentu pokazuje, co porównać z rzeczywistym ładunkiem; ostrzeżenie, by nie uzupełniać braków z pamięci, jest czytelne dla początkującego.

Lekcje są szkicami do niezależnej recenzji, nie zatwierdzonym materiałem szkoleniowym. W próbie nawigacyjnej wszystkie mają cele nauki, przykłady praktyczne i odsyłacze do ID z banku. Potwierdzono jedno lokalne uproszczenie językowe w lekcji B-08: skrót DMC pojawiał się w celach nauki przed rozwinięciem. Rozwinięto go przy pierwszym użyciu. Długie pliki zawierają też sekcje robocze/historię redakcyjną; to problem nawigacji znany z 4q, ale nie usuwano historii ani nie przebudowywano całej struktury bez osobnego zadania.

## Zmienione elementy

- `ADR-B-0342`: wyjaśnienie mówi teraz wprost, że klasa 7 oznacza materiały promieniotwórcze; tłumaczy szczególną zasadę pierwszeństwa i odrzuca błędne pomijanie klasy oraz wybór według samej masy składników. Podstawa nadal: ADR 2.1.3.5.3(a).
- `podstawowy/lekcje/ADR-B-08.md`: pierwsze użycie DMC rozwinięto jako „dopuszczalna masa całkowita (DMC)”.
- Zaktualizowano wyłącznie snapshoty audytu sekwencyjnego i A/B/C dla ADR-B-0342, aby odpowiadały dokładnemu tekstowi wyjaśnienia.

## Wskaźnik „poprawna = najdłuższa”

W tej partii próbki nie zmieniano opcji odpowiedzi. Późniejszy PR #271 dopasował osiem dystraktorów w działach B-02, B-03 i B-09. Aktualny licznik ścisły wynosi **71/566 = 12,54% globalnie**; wszystkie działy pozostają poniżej 18%, a B-02, B-03 i B-09 spadły odpowiednio do 12,50%, 12,24% i 10,87%. Quality Gate kontroluje oba poziomy.

## Ograniczenia

To redakcyjna próbka, nie pełna kontrola prawna. Wszystkie rekordy pozostają `needs_review`; nie nadano statusu `verified`. Wymagana jest niezależna recenzja ADR i kontrola z polskim tekstem urzędowym wraz ze sprostowaniem.
