# Etap 4x135 — głębokość kompetencji i pytania ADR-B-0610–0620

**Data:** 28.10.2026. **Bazowy main:** `391bfe32402769b017821300fe37e9361947700a`. Zakres: tylko kurs podstawowy.

## Wynik audytu kompetencji

Skrypt porównał podobieństwo treści pytań wewnątrz każdej kompetencji teoretycznej; następnie odczytano ręcznie wskazane pary i cel kompetencji. Podobieństwo słów to sygnał do kontroli, nie dowód duplikatu: np. ADR-B-0071/0072 badają różne progi DMC, a ADR-B-0330/0337 różne klasy odpadów.

- Kompetencje teoretyczne: 104.
- Kompetencje z dokładnie 3 pytaniami: **20**.
- Kompetencje z dokładnie 4 pytaniami: **33**.
- Szczegółowo sprawdzona grupa niskiej liczebności: **53 kompetencje**. Minimum liczby pytań nie oznacza automatycznie niezależności merytorycznej.

### Kompetencje z potwierdzonym ryzykiem powtórzeń lub wąskiego pokrycia

| Kompetencja | Przykładowe ID | Ocena i działanie |
|---|---|---|
| B-02-K03, klasa 3 | 0288 / 0542 | Ta sama nalepka rozpoznawana dwukrotnie; w obrębie kompetencji pozostałe pytania badają też klasę i źródło zapłonu. Do dalszego odchudzenia po niezależnym przeglądzie. |
| B-03-K04, ochrona kanalizacji | 0100 / 0163 / 0242 | Powtarza się zasada „tylko jeśli bezpiecznie”. Dodano 0612 — co zrobić, gdy podejście do odpływu naraża kierowcę. |
| B-03-K05, unikanie skażenia | 0101 / 0178 / 0295 | Trzy podobne reakcje na rozlew. Dodano 0613 — sytuacja z drażniącymi oparami i brakiem sprzętu ochronnego. |
| B-04-K02, otwieranie przesyłek | 0011 / 0243 / 0357 | Wąska reguła powtórzona w podobnych pytaniach. Zachować jako regułę krytyczną, ale przy kolejnej redakcji różnicować kontekst bez tworzenia nieistniejących wyjątków. |
| B-05-K03, alarmowanie służb | 0220 / 0594 | Częściowe nakładanie; rozróżnia je nieznana przyczyna awarii. Dalsza kontrola redakcyjna. |
| B-05-K04, opary/strona nawietrzna | 0183 / 0221 | Podobny schemat, ale odmienny kierunek wiatru i pozycja kierowcy. Zachować, kontrolować w kolejnej próbce. |
| B-05-K05, pożar ładowni | 0222 / 0614 | Dodano 0614: nawet pozornie mały pożar przedziału ładunkowego nie jest do samodzielnego gaszenia. |
| B-05-K06, mały pożar opon/hamulców | 0223 / 0493 | Podobne scenariusze opon i hamulców; to nadal ta sama kompetencja, ale warto rozdzielić decyzję o ewakuacji i granice użycia gaśnicy. |
| B-06-K04, litera X | 0017 / 0170 / 0256 | Powtarza się interpretacja reakcji z wodą. Dodano 0615 — zastosowanie oznaczenia w decyzji kierowcy i przekazaniu informacji służbom. |
| B-06-K06, powtórzona cyfra | 0051 / 0192 | Reguła ogólna i przykład „33” są bliskie. Dodano 0616 — zastosowanie zasady i przypomnienie, że numer zagrożenia nie zastępuje numeru UN. |
| B-06-K08, cyfra 8 | 0053 / 0194 / 0298 | Trzy przykłady znaczenia 8/80/88, ale wąski zakres. Wymaga dalszego sprawdzenia niezależności. |
| B-09-K04, strzałki kierunkowe | 0058 / 0172 / 0286 | Pytania o ustawienie są bliskie. Dodano 0617 o odrębnym wymaganiu rozmieszczenia strzałek na dwóch przeciwległych pionowych bokach. |
| B-09-K05, piętrzenie | 0059 / 0078 / 0237 | Dwa pytania powtarzają zakaz piętrzenia opakowań nieprzystosowanych; 0078 bada uszkodzenie dolnego opakowania. Dodano 0618 o uginaniu się opakowania pod ciężarem. |
| B-10-K02, wpis 1.1.4.2.1 | 0061 / 0277 / 0395 | Powtarza się wymagany wpis. Istnieje też pytanie o warunek jego zastosowania, ale kompetencja nadal wymaga odchudzenia. |
| B-13-K07, instrukcje dostępne w kabinie | 0228 / 0590 | Zbliżone przypadki niedostępnego schowka. Dodano 0620 o odrębnym wymogu języka zrozumiałego dla całej załogi. |

## Dodane pytania

| ID | Kompetencja | Nowy aspekt | Podstawa do recenzji |
|---|---|---|---|
| ADR-B-0610 | B-02-K14 | Kolumna 5 tabeli A — wymagane nalepki | ADR 3.2.1, kol. 5 |
| ADR-B-0611 | B-02-K04 | Rozróżnienie klas 4.1 i 4.2 | ADR 2.2.41.1.1; 2.2.42.1.1 |
| ADR-B-0612 | B-03-K04 | Bezpieczna reakcja, gdy nie można osłonić odpływu | ADR 5.4.3.4 |
| ADR-B-0613 | B-03-K05 | Rozlew nieznanej substancji i opary | ADR 5.4.3.4 |
| ADR-B-0614 | B-05-K05 | Pożar ładowni nawet przy niewielkich płomieniach | ADR 5.4.3.4 |
| ADR-B-0615 | B-06-K04 | Litera X i reakcja z wodą | ADR 5.3.2.3.1 |
| ADR-B-0616 | B-06-K06 | Powtórzona cyfra i dalsza identyfikacja towaru | ADR 5.3.2.3.1 |
| ADR-B-0617 | B-09-K04 | Umiejscowienie strzałek kierunkowych | ADR 5.2.1.10.1; 7.5.1.5 |
| ADR-B-0618 | B-09-K05 | Uginające się opakowanie przy piętrzeniu | ADR 7.5.7.1–7.5.7.2 |
| ADR-B-0619 | B-01-K03 | Okres ważności zaświadczenia kierowcy | ADR 8.2.2.8.2 |
| ADR-B-0620 | B-13-K07 | Język instrukcji zrozumiały dla każdego członka załogi | ADR 5.4.3.2 |

## Metryki

- Bank: **620** pytań; wszystkie `needs_review`, 0 `verified`.
- A/B/C: 209/210/201.
- „Poprawna = jedyna najdłuższa”: **69/620 = 11.13%**; maksimum działu 13.95%.
- Explanation: minimum 280, maksimum 498 znaków.
- Liczebność działów: ADR-B-01 46; ADR-B-02 58; ADR-B-03 51; ADR-B-04 46; ADR-B-05 44; ADR-B-06 47; ADR-B-07 48; ADR-B-08 42; ADR-B-09 48; ADR-B-10 55; ADR-B-11 43; ADR-B-12 44; ADR-B-13 48.
- Nowe ID mają podstawę prawną do kontroli, audyt A/B/C i status `needs_review`; nie zmieniono żadnego rekordu na `verified`.

## Ograniczenia i testy

To audyt redakcyjny, nie niezależne zatwierdzenie prawne. Każdą podstawę należy porównać z pełnym tekstem ADR 2025 w Dz.U. 2025 poz. 642 i sprostowaniem poz. 1575. Próba lokalnego checkoutu nie powiodła się, ponieważ środowisko nie mogło rozwiązać hosta `github.com`; testy jednostkowe i Quality Gate muszą zostać potwierdzone przez CI na PR. Warianty egzaminu zachowują 30 pytań; migawka źródłowego banku została zaktualizowana, a nowe ID zostaną wprowadzone do arkuszy i lekcji w kolejnym PR.
