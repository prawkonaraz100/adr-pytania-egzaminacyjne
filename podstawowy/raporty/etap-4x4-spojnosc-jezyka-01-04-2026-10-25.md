# ETAP 4x4 — kontrola spójności i języka kursanta: B-01–B-04

- Data: 25.10.2026.
- Bazowy `main`: `596fdad80a33f2bf4577e2a05400f781ec3dc499`.
- Audyt obejmuje wszystkie 196 pytań przypisanych do B-01–B-04, ich trzy opcje, klucz, explanation i podane referencje prawne oraz treść czterech lekcji.
- Nie traktowano samej zgodności numeru przepisu w banku jako niezależnego potwierdzenia prawnego. Poprawki merytoryczne wprowadzono wyłącznie tam, gdzie wymaganie było już określone w źródle ADR 2025 wskazanym w pytaniu i dało się je doprecyzować bez zmiany sensu.

## Wynik kontroli

- Liczba pytań w zakresie: 196; duplikaty ID w całym banku: 0.
- Wskaźnik „poprawna odpowiedź jest jedyną najdłuższą”: 86/609 = 14.12% (limit 18%).
- Explanation w całym banku: minimum 300, maksimum 457 znaków; poniżej 200: 0; powyżej 500: 0; poza zakresem 2–5 zdań: 0.
- Statusy: 609 `needs_review`, 0 `verified`. Nie zmieniano statusów.
- Zmiany banku: wyłącznie redakcja dystraktorów i dopasowanie explanation w ADR-B-0571 oraz ADR-B-0352; bez zmiany ID, `module_id` ani klucza.
- Wariantów egzaminów próbnych nie trzeba regenerować: żadne ID ani przypisanie do działu nie zostało zmienione.

## Znalezione problemy i poprawki

1. **B-01 / ADR-B-0571 — obliczenie 1.1.3.6.4.** Wcześniejszy dystraktor A podawał jedynie sumę 550, co było łatwą do odrzucenia odpowiedzią. Zmieniono go na realistyczny błąd rachunkowy: użycie mnożnika 2 zamiast 3 daje 800. Explanation teraz wyjaśnia zarówno wynik 1050, jak i źródło pomyłki. Podstawa: ADR 1.1.3.6.4.
2. **B-04 / ADR-B-0352 — klin pod koło.** Dystraktory o dwóch osobach w przyczepie i otwieraniu drzwi były absurdalne i nie testowały rozumienia wymogu. Zmieniono je na wiarygodne, lecz błędne uogólnienia (dwa kliny zawsze / klin tylko na pochyłości), a explanation dopasowano do nowych opcji. Podstawa: ADR 8.3.7 i 8.1.5.2.
3. **B-01 — brakowało konkretnych zasad LQ/EQ w jednym miejscu.** Dopisano limit LQ dla opakowania wewnętrznego z kolumny 7a tabeli A, zasadniczy limit 30 kg brutto dla zwykłego opakowania zewnętrznego, oznakowanie opakowania zbiorczego (3.4.11), informację nadawcy o całkowitej masie brutto LQ (3.4.12), limit 1000 sztuk EQ (3.5.5), wymagany wpis i liczbę sztuk (3.5.6) oraz oznakowanie OVERPACK/EQ, gdy znaki wewnętrzne nie są widoczne (3.5.4.3).
4. **B-01 — szkolenie.** Wskazano ADR 1.3.2.3 dla szkolenia bezpieczeństwa i 1.3.2.4 dla uzupełniania wiedzy; doprecyzowano, że zakres szkolenia zależy od zadań pracownika.
5. **B-01 — identyfikacja towaru i przewóz prywatny.** Doprecyzowano, że numer UN znajduje się w kolumnie 1, a nazwa i opis w kolumnie 2 tabeli A (ADR 3.2.1). Uściślono, że wyłączenie 1.1.3.1(a)(i) dotyczy opakowań detalicznych do osobistego lub domowego użytku zabezpieczonych przed wyciekiem w normalnych warunkach; dla niektórych cieczy występują dodatkowe limity.
6. **B-02 — mapa podstaw klasyfikacji.** Dodano krótką mapę punktów ADR dla klas 1–9, wzorów nalepek oraz baterii sodowo-jonowych UN 3551/3552. Doprecyzowano odniesienia do szczegółowych kryteriów klasy 7 i podpunktów 2.2.9.1.7.2(a), (c), (d). Wskazano, że wymagania badań typu trzeba sprawdzać dla konkretnej pozycji i odpowiednich kryteriów ONZ; nie rozszerzono uprawnień kursu podstawowego do każdego przewozu klasy 7.
7. **B-03 — progi i wymiary znaku środowiskowego.** Dopisano limity wyjątku od znaku: do 5 l cieczy i do 5 kg netto ciał stałych w odpowiednim opakowaniu, z pozostałymi warunkami 5.2.1.8.1. Dopisano wymiar standardowy 250 × 250 mm oraz warunkową możliwość zmniejszenia do co najmniej 100 × 100 mm dla cysterny o pojemności do 3000 l, gdy spełnione są warunki ADR 5.3.6.2. Dodano odwołanie do 5.3.6.1 i ADR 2.1.3.5.3(a).
8. **B-04 — wyposażenie postoju.** Połączono wymaganie użycia klina z wymaganiem wyposażenia, wskazując ADR 8.3.7 i 8.1.5.2.

Nie znaleziono potwierdzonej sprzeczności wymagającej zmiany klucza odpowiedzi ani zmiany przypisania pytania do działu. Nie uznano tego za dowód formalnej weryfikacji prawnej; cały bank pozostaje `needs_review`.

## Pełna lista pytań sprawdzonych

Poniższa tabela zapisuje wszystkie ID w zakresie, skrócony temat, część lekcji używaną w porównaniu i podstawę prawną wskazaną przez rekord banku. Dla B-01–B-04 żadne ID nie zostało przeniesione między działami.

## ADR-B-01 — 45 pytań

| ID | Pytanie / kompetencja sprawdzana | Fragment podręcznika porównany | Podstawa zapisana w banku |
|---|---|---|---|
| `ADR-B-0001` | Jakie szkolenie powinien otrzymać pracownik nadawcy, którego obowiązki dotyczą przewozu towarów niebezpiecznych? | § 3 — Szkolenie a zaświadczenie kierowcy | 1.3.2 |
| `ADR-B-0002` | Czy przewóz niewielkiej ilości towarów niebezpiecznych automatycznie zwalnia kierowcę ze wszystkich wymagań ADR? | § 4.1–4.4 — Wyłączenia, LQ/EQ i obliczenia | 1.1.3 |
| `ADR-B-0003` | Do czego służy zaświadczenie ADR kierowcy? | § 1 i § 5 — Zakres ADR, numer UN i tabela A | 8.2.1 |
| `ADR-B-0040` | Kiedy pracownik przedsiębiorstwa wykonujący obowiązki związane z ADR powinien odbyć odpowiednie przeszkolenie? | § 3 — Szkolenie a zaświadczenie kierowcy | 1.3.1 |
| `ADR-B-0041` | Dlaczego szkolenie pracowników dotyczące ADR trzeba okresowo uzupełniać? | § 3 — Szkolenie a zaświadczenie kierowcy | 1.3.2.4 |
| `ADR-B-0091` | Firma kupuje paletę farb zaklasyfikowanych jako towary niebezpieczne w ADR z przeznaczeniem do dalszej sprzedaży. Czy au… | § 3 — Szkolenie a zaświadczenie kierowcy | 1.1.3.1 (a) |
| `ADR-B-0092` | Nowy pracownik magazynu nie przeszedł jeszcze szkolenia ADR odpowiedniego do zadań. Co przewiduje 1.3.1, zanim ukończy s… | § 3 — Szkolenie a zaświadczenie kierowcy | 1.3.1 |
| `ADR-B-0093` | Przedsiębiorca twierdzi, że oznakowanie LQ zawsze oznacza wyłączenie na podstawie 1.1.3.6. Czy ma rację? | § 3 — Szkolenie a zaświadczenie kierowcy | 3.4; 1.1.3.6 |
| `ADR-B-0123` | Co oznacza określenie „towary niebezpieczne” w umowie ADR? | § 1 i § 5 — Zakres ADR, numer UN i tabela A | Umowa ADR, art. 1(b) |
| `ADR-B-0124` | Nadawca chce przewieźć nowy materiał niebezpieczny. Co powinien ustalić przed wyborem sposobu przewozu? | § 1 i § 5 — Zakres ADR, numer UN i tabela A | 2.1.1; 3.2 tabela A |
| `ADR-B-0125` | W której kolumnie tabeli A ADR znajduje się numer UN materiału? | § 1 i § 5 — Zakres ADR, numer UN i tabela A | 3.2.1, tabela A kol. (1) |
| `ADR-B-0147` | Do pracy przy przewozie ADR skierowano ciągnik samochodowy z naczepą. Jak ADR traktuje taki zestaw przy wymaganiach odno… | § 1 i § 5 — Zakres ADR, numer UN i tabela A | 1.2.1, definicja transport unit |
| `ADR-B-0148` | Kierowca ma aktualne zaświadczenie ADR, ale nie ma prawa jazdy odpowiedniej kategorii na prowadzony zestaw. Co z tego wy… | § 1 i § 5 — Zakres ADR, numer UN i tabela A | 8.2.1; prawo krajowe o uprawnieniach do kierowania |
| `ADR-B-0149` | Jak sprawdza się limit ilości ograniczonej (LQ) dla konkretnego numeru UN? | § 4.1–4.4 — Wyłączenia, LQ/EQ i obliczenia | 3.2 tabela A kol. (7a); 3.4.1 |
| `ADR-B-0259` | Wszystkie towary na jednostce transportowej zaliczono do kategorii transportowej 3. Jaki limit ilości z tabeli ADR 1.1.3… | § 3 — Szkolenie a zaświadczenie kierowcy | 1.1.3.6.3 |
| `ADR-B-0260` | Towar ma w kolumnie 7b tabeli A kod EQ „E0”. Jak należy ocenić możliwość zastosowania wyłączenia dla ilości wyłączonych? | § 4.1–4.4 — Wyłączenia, LQ/EQ i obliczenia | 3.5.1.2 |
| `ADR-B-0261` | Towar niebezpieczny dopuszczony do przewozu jako LQ umieszczono w zwykłym odpowiednim opakowaniu zewnętrznym z opakowani… | § 4.1–4.4 — Wyłączenia, LQ/EQ i obliczenia | 3.4.2 |
| `ADR-B-0271` | W jednostce transportowej przewożone są towary kategorii transportowej 2 w ilości 100 jednostek i kategorii 3 w ilości 6… | § 3 — Szkolenie a zaświadczenie kierowcy | 1.1.3.6.4 |
| `ADR-B-0272` | Jednostka transportowa przewozi 200 jednostek kategorii transportowej 2 i 500 jednostek kategorii 3. Co wynika z samego … | § 3 — Szkolenie a zaświadczenie kierowcy | 1.1.3.6.4 |
| `ADR-B-0273` | Na sztuce przesyłki przewożonej na zasadach LQ jest znak w kształcie rombu z czarną górą i dołem oraz białym środkiem. K… | § 4.1–4.4 — Wyłączenia, LQ/EQ i obliczenia | 3.4.7.1 |
| `ADR-B-0301` | Kierowca realizuje przewóz towarów niebezpiecznych, dla którego wymagane jest zaświadczenie ADR. Co musi wykazać, aby uz… | § 1 i § 5 — Zakres ADR, numer UN i tabela A | 8.2.1.1 |
| `ADR-B-0312` | Co obejmuje definicja „przewozu” w ADR 1.2.1, oprócz przemieszczania pojazdu z towarem niebezpiecznym? | § 1 i § 5 — Zakres ADR, numer UN i tabela A | 1.2.1 |
| `ADR-B-0313` | Osoba prywatna przewozi niebezpieczny produkt w opakowaniu detalicznym do własnego użytku domowego. Jaki warunek jest is… | § 3 — Szkolenie a zaświadczenie kierowcy | 1.1.3.1(a)(i) |
| `ADR-B-0314` | Gdzie w tabeli A ADR 2025 należy szukać nazwy przewozowej odpowiadającej konkretnemu numerowi UN? | § 1 i § 5 — Zakres ADR, numer UN i tabela A | 3.2.1, objaśnienie kolumny (2) |
| `ADR-B-0323` | W jednej jednostce transportowej przewożone są razem towary kategorii transportowej 2 i 3. Jak należy ocenić zwolnienie … | § 3 — Szkolenie a zaświadczenie kierowcy | 1.1.3.6.4 |
| `ADR-B-0513` | Nowy pracownik terminalu zaczyna obsługiwać dokumenty towarów niebezpiecznych. Nie odbył jeszcze szkolenia ADR odpowiedn… | § 3 — Szkolenie a zaświadczenie kierowcy | 1.3.1 |
| `ADR-B-0520` | Inspektor właściwej władzy prosi pracodawcę o dokumentację szkolenia ADR 1.3 pracownika kompletującego przesyłki. Jak po… | § 3 — Szkolenie a zaświadczenie kierowcy | 1.3.3 |
| `ADR-B-0521` | Pracownik przechodzi do nowego przedsiębiorstwa i ma wykonywać czynności podlegające szkoleniu ADR 1.3. Co należy sprawd… | § 3 — Szkolenie a zaświadczenie kierowcy | 1.3.3 |
| `ADR-B-0522` | Pracownik terminalu obsługuje drogowo-morski łańcuch transportowy z towarami niebezpiecznymi. Jakie szkolenie funkcjonal… | § 3 — Szkolenie a zaświadczenie kierowcy | 1.3.2.2 |
| `ADR-B-0526` | Kierowca ma przewieźć 1 050 sztuk przesyłek z towarami niebezpiecznymi w ilościach wyłączonych EQ w jednym pojeździe. Ja… | § 4.1–4.4 — Wyłączenia, LQ/EQ i obliczenia | 3.5.5 |
| `ADR-B-0527` | Wraz z przesyłkami w ilościach wyłączonych EQ przewoźnik otrzymał list przewozowy. Jaka informacja dotycząca EQ powinna … | § 4.1–4.4 — Wyłączenia, LQ/EQ i obliczenia | 3.5.6 |
| `ADR-B-0528` | Magazynier umieszcza przesyłki oznaczone EQ w opakowaniu zbiorczym. Oznaczenia wewnętrznych sztuk nie są widoczne. Jakie… | § 4.1–4.4 — Wyłączenia, LQ/EQ i obliczenia | 3.5.4.3 |
| `ADR-B-0529` | Pracownik punktu przeładunkowego ma kontakt z niebezpiecznymi substancjami podczas typowych obowiązków. Jaki element szk… | § 3 — Szkolenie a zaświadczenie kierowcy | 1.3.2.3 |
| `ADR-B-0534` | Na terminalu połączono kilka opakowań LQ w opakowanie zbiorcze. Oznaczenia LQ poszczególnych sztuk są niewidoczne. Jak p… | § 4.1–4.4 — Wyłączenia, LQ/EQ i obliczenia | 3.4.11 |
| `ADR-B-0535` | Nadawca przekazuje przewoźnikowi partię towarów w ilościach ograniczonych LQ. Jaką informację powinien przed przewozem p… | § 4.1–4.4 — Wyłączenia, LQ/EQ i obliczenia | 3.4.12 |
| `ADR-B-0570` | Kierowca ma 100 jednostek kategorii transportowej 2 i 600 kategorii 3 w sztukach przesyłek. Ile wynosi wynik ADR 1.1.3.6… | § 3 — Szkolenie a zaświadczenie kierowcy | 1.1.3.6.4 |
| `ADR-B-0571` | W pojeździe przewożono 250 jednostek kategorii transportowej 2 i 300 kategorii 3. Czy obliczony wynik przekracza próg 10… | § 3 — Szkolenie a zaświadczenie kierowcy | 1.1.3.6.4 |
| `ADR-B-0572` | Magazyn przygotował 990 sztuk przesyłek EQ w jednym pojeździe. Co jeszcze należy ocenić oprócz liczby sztuk? | § 4.1–4.4 — Wyłączenia, LQ/EQ i obliczenia | 3.5.1–3.5.6 |
| `ADR-B-0573` | Dokumenty przesyłek w ilościach wyłączonych EQ nie podają liczby sztuk przesyłek. Co należy zrobić przed rozpoczęciem pr… | § 4.1–4.4 — Wyłączenia, LQ/EQ i obliczenia | 3.5.6 |
| `ADR-B-0595` | Osoba prywatna przewozi niewielką ilość produktu niebezpiecznego do własnego użytku. Czy sam prywatny cel automatycznie … | § 3 — Szkolenie a zaświadczenie kierowcy | 1.1.3.1(a) |
| `ADR-B-0605` | Sztuka przesyłki jest oznaczona jako przewóz w ilościach ograniczonych (LQ), ale opakowanie zewnętrzne waży 32 kg brutto… | § 4.1–4.4 — Wyłączenia, LQ/EQ i obliczenia | 3.4.2 |
| `ADR-B-0606` | Kierowca ocenia przewóz według wyłączenia ilościowego z ADR 1.1.3.6 i sprawdza tylko masę całego ładunku. Czy to wystarc… | § 3 — Szkolenie a zaświadczenie kierowcy | 1.1.3.6.3–1.1.3.6.4 |
| `ADR-B-0607` | Kierowca ma ważne prawo jazdy, ale nie ma zaświadczenia ADR. Przewóz przekracza warunki wyłączenia, przy których zaświad… | § 4.1–4.4 — Wyłączenia, LQ/EQ i obliczenia | 8.2.1.1 |
| `ADR-B-0608` | W tabeli A ADR przy danym numerze UN wskazano warunek, który zabrania przewozu tej substancji w opisanej postaci. Nadawc… | § 1 i § 5 — Zakres ADR, numer UN i tabela A | 2.1; 3.2, tabela A |
| `ADR-B-0609` | Przesyłki LQ są prawidłowo zapakowane, ale kierowca chce usunąć oznaczenie ilości ograniczonych z opakowania, aby wygląd… | § 4.1–4.4 — Wyłączenia, LQ/EQ i obliczenia | 3.4.7.1 |

## ADR-B-02 — 56 pytań

| ID | Pytanie / kompetencja sprawdzana | Fragment podręcznika porównany | Podstawa zapisana w banku |
|---|---|---|---|
| `ADR-B-0004` | Do której klasy ADR należą materiały ciekłe zapalne, takie jak benzyna? | § 2 — Klasy i podklasy ADR | 2.2.3.1.1 |
| `ADR-B-0005` | Jakie zagrożenie oznacza klasa 8 ADR? | § 2 — Klasy i podklasy ADR | 2.2.8.1.1 |
| `ADR-B-0006` | Która cecha jest charakterystyczna dla materiałów klasy 4.3 ADR? | § 2 — Klasy i podklasy ADR | 2.2.43.1.1 |
| `ADR-B-0042` | Do której klasy ADR zalicza się gazy? | § 2 — Klasy i podklasy ADR | 2.2.2.1.1 |
| `ADR-B-0043` | Jaka klasa ADR dotyczy materiałów zakaźnych? | § 2 — Klasy i podklasy ADR | 2.2.62.1.1 |
| `ADR-B-0044` | Co jest głównym zagrożeniem materiałów klasy 5.1? | § 2 — Klasy i podklasy ADR | 2.2.51.1.1 |
| `ADR-B-0094` | Która klasa ADR obejmuje materiały stałe zapalne? | § 2 — Klasy i podklasy ADR | 2.2.41.1.1 |
| `ADR-B-0095` | Która klasa ADR dotyczy materiałów zdolnych do samozapalenia? | § 2 — Klasy i podklasy ADR | 2.2.42.1.1 |
| `ADR-B-0096` | Do której klasy ADR zalicza się nadtlenki organiczne? | § 2 — Klasy i podklasy ADR | 2.2.52.1.1 |
| `ADR-B-0097` | Która klasa ADR oznacza materiały trujące? | § 2 — Klasy i podklasy ADR | 2.2.61.1.1 |
| `ADR-B-0098` | Do jakiej klasy ADR zaliczono materiały promieniotwórcze? | § 2 — Klasy i podklasy ADR | 2.2.7.1 |
| `ADR-B-0099` | Jaką klasę zagrożenia ADR przedstawiają nalepki ostrzegawcze wzoru 9 i 9A, jeżeli są wymagane dla towaru? | § 4 — Nalepki i oznakowanie | 2.2.9.1.1; 5.2.2.2.2 |
| `ADR-B-0126` | Co oznacza podklasa 1.1 materiałów i przedmiotów wybuchowych? | § 2 — Klasy i podklasy ADR | 2.2.1.1.5 |
| `ADR-B-0127` | Która grupa pakowania, tam gdzie ADR stosuje grupy I, II i III, oznacza wysoki stopień zagrożenia? | § 1 i § 3 — Tabela A, klasyfikacja i grupa pakowania | 2.1.1.3 |
| `ADR-B-0128` | Gdzie w tabeli A ADR podany jest numer klasy zagrożenia przypisany materiałowi? | § 1 i § 3 — Tabela A, klasyfikacja i grupa pakowania | 3.2.1 tabela A kol. (3a) |
| `ADR-B-0150` | Co odróżnia zagrożenie wybuchem masowym w podklasie 1.1 od podklasy 1.4? | § 2 — Klasy i podklasy ADR | 2.2.1.1.5 |
| `ADR-B-0151` | Na przesyłce znajduje się nalepka 2.3. Jakiego podstawowego zagrożenia należy się spodziewać? | § 4 — Nalepki i oznakowanie | 5.2.2.2.2, wzór nr 2.3; 2.2.2 |
| `ADR-B-0152` | Podczas przeładunku cieczy zapalnej klasy 3 ktoś chce zapalić papierosa obok pojazdu. Jaka jest prawidłowa reakcja? | § 2 — Klasy i podklasy ADR | 2.2.3; 8.3.5 |
| `ADR-B-0153` | Jakie rozróżnienie między klasą 4.1 a 4.3 jest prawidłowe? | § 2 — Klasy i podklasy ADR | 2.2.41.1.1; 2.2.43.1.1 |
| `ADR-B-0154` | Dlaczego materiał samonagrzewający się z klasy 4.2 wymaga zachowania ostrożności podczas przewozu? | § 2 — Klasy i podklasy ADR | 2.2.42.1.1 |
| `ADR-B-0155` | Po rozszczelnieniu opakowania klasy 4.3 świadek proponuje polanie wycieku wodą. Jak powinien zareagować kierowca? | § 2 — Klasy i podklasy ADR | 2.2.43.1.1; 5.4.3.4 |
| `ADR-B-0156` | Czy materiał klasy 5.1 może zwiększać intensywność pożaru innego materiału? | § 2 — Klasy i podklasy ADR | 2.2.51.1.1 |
| `ADR-B-0157` | Która odpowiedź właściwie rozróżnia klasy 5.1 i 5.2? | § 2 — Klasy i podklasy ADR | 2.2.51; 2.2.52 |
| `ADR-B-0158` | Co należy rozpoznać po nalepce ostrzegawczej 6.1? | § 4 — Nalepki i oznakowanie | 5.2.2.2.2 wzór nr 6.1; 2.2.61.1.1 |
| `ADR-B-0159` | Jaka różnica między klasą 6.2 a 6.1 jest prawidłowa? | § 2 — Klasy i podklasy ADR | 2.2.62.1.1; 2.2.61.1.1 |
| `ADR-B-0160` | Kierowca ukończył wyłącznie kurs podstawowy ADR. Czy uprawnia go to automatycznie do każdego przewozu materiałów promien… | § 2 — Klasy i podklasy ADR | 8.2.1.4; 8.5 przepis szczególny S12 |
| `ADR-B-0161` | Jakie zagrożenie powinien brać pod uwagę kierowca widząc nalepkę klasy 8? | § 4 — Nalepki i oznakowanie | 2.2.8.1.1; 5.2.2.2.2 wzór nr 8 |
| `ADR-B-0162` | Nalepka ostrzegawcza 9A może być wymagana podczas przewozu jakich baterii, zgodnie z odpowiednią pozycją ADR 2025? | § 4 — Nalepki i oznakowanie | 5.2.2.2.2 (model nr 9A); 3.2 tabela A: UN 3551, UN 3552; 2.2.9.1.7.2 |
| `ADR-B-0218` | Na opakowaniu towaru niebezpiecznego wymagane są dwie różne nalepki ostrzegawcze: zagrożenia głównego i dodatkowego. Co … | § 1 i § 3 — Tabela A, klasyfikacja i grupa pakowania | 5.2.2.1.1; 3.2.1 tabela A kolumna (5) |
| `ADR-B-0265` | Na opakowaniu wymagane jest ostrzeżenie klasy 4.3. Jakie zagrożenie powinien rozpoznać kierowca? | § 2 — Klasy i podklasy ADR | 2.2.43.1.1 |
| `ADR-B-0266` | Opis towaru ADR wskazuje klasę 5.1 i odpowiednią nalepkę. Jakie zagrożenie należy uwzględnić? | § 4 — Nalepki i oznakowanie | 2.2.51.1.1 |
| `ADR-B-0267` | Na sztuce przesyłki wymagana jest nalepka klasy 8. Co oznacza rozpoznawane zagrożenie? | § 4 — Nalepki i oznakowanie | 2.2.8.1.1 |
| `ADR-B-0268` | Sztuka przesyłki ma nalepkę wzoru 4.1: białe tło z pionowymi czerwonymi pasami i symbolem płomienia. Jaką klasę oznacza? | § 4 — Nalepki i oznakowanie | 5.2.2.2.2 |
| `ADR-B-0269` | Na wymaganej nalepce wzoru 4.3 widzisz płomień na niebieskim tle. Którą klasę rozpoznajesz? | § 4 — Nalepki i oznakowanie | 5.2.2.2.2 |
| `ADR-B-0270` | Na sztuce przesyłki widnieje nalepka z czarnym płomieniem nad okręgiem na żółtym tle. Jaki wzór nalepki opisano? | § 4 — Nalepki i oznakowanie | 5.2.2.2.2 |
| `ADR-B-0284` | Na nalepce widoczny jest symbol butli gazowej na zielonym tle i numer 2 u dołu. Jaką grupę zagrożeń oznacza ten wzór? | § 4 — Nalepki i oznakowanie | 5.2.2.2.2 |
| `ADR-B-0288` | Na nalepce zagrożenia jest biały symbol płomienia na czerwonym tle oraz cyfra 3 na dole. Jaką klasę przedstawia ten wzór… | § 4 — Nalepki i oznakowanie | 5.2.2.2.2 |
| `ADR-B-0289` | Nalepka wzoru 6.1 ma symbol czaszki ze skrzyżowanymi piszczelami. Jakie zagrożenie rozpoznaje kierowca? | § 4 — Nalepki i oznakowanie | 5.2.2.2.2 |
| `ADR-B-0302` | W dokumentacji transportowej wskazano klasę 4.2. Jakiego rodzaju zagrożenie powinien rozpoznać kierowca? | § 2 — Klasy i podklasy ADR | 2.2.42.1.1 |
| `ADR-B-0307` | W przewozie ADR znajduje się nadtlenek organiczny klasy 5.2. Dlaczego nie należy narażać go na niekontrolowane ogrzewani… | § 2 — Klasy i podklasy ADR | 2.2.52.1.2, 2.2.52.1.4 |
| `ADR-B-0309` | Materiał zawiera drobnoustroje, które mogą powodować choroby u ludzi albo zwierząt. Jaką klasę ADR należy sprawdzić przy… | § 2 — Klasy i podklasy ADR | 2.2.62.1.1 |
| `ADR-B-0311` | Przewóz dotyczy materiału zakaźnego, w którym patogen może powodować chorobę tylko u zwierząt. Które rozróżnienie klasy … | § 2 — Klasy i podklasy ADR | 2.2.62.1.2 |
| `ADR-B-0315` | Nowe regulacje ADR 2025 wymieniają baterie sodowo-jonowe z elektrolitem organicznym jako UN 3551. Do której klasy należą… | § 4 — Baterie sodowo-jonowe i zagrożenia szczególne | 2.2.9.1.7.2; tabela A UN 3551 |
| `ADR-B-0316` | W klasyfikacji ADR klasy 1 podklasa 1.1 oznacza zagrożenie jakiego rodzaju? | § 2 — Klasy i podklasy ADR | 2.2.1.1.5 (podklasa 1.1) |
| `ADR-B-0317` | Przy rozpoznawaniu materiału promieniotwórczego klasy 7 w ADR, co należy sprawdzić zgodnie z definicją w 2.2.7.1.1? | § 2 — Klasy i podklasy ADR | 2.2.7.1.1 oraz 2.2.7.2.2.1–2.2.7.2.2.6 |
| `ADR-B-0495` | Przesyłka klasy 1 ma podklasę 1.2. Jakie zagrożenie odróżnia ją od podklasy 1.1? | § 2 — Klasy i podklasy ADR | 2.2.1.1.5, podklasa 1.2 |
| `ADR-B-0496` | Materiał wybuchowy klasy 1 ma podklasę 1.3. Które połączenie zagrożeń odpowiada ADR? | § 2 — Klasy i podklasy ADR | 2.2.1.1.5, podklasa 1.3 |
| `ADR-B-0497` | Podklasa 1.5 obejmuje bardzo mało wrażliwe materiały wybuchowe. Czy brak wrażliwości oznacza brak zagrożenia wybuchem ma… | § 2 — Klasy i podklasy ADR | 2.2.1.1.5, podklasa 1.5 |
| `ADR-B-0498` | Podklasa 1.6 dotyczy skrajnie mało wrażliwych przedmiotów wybuchowych. Jakie zagrożenie masowe określa definicja? | § 2 — Klasy i podklasy ADR | 2.2.1.1.5, podklasa 1.6 |
| `ADR-B-0499` | Bateria sodowo-jonowa z elektrolitem organicznym została umieszczona w urządzeniu, a inna identyczna bateria przewożona … | § 4 — Baterie sodowo-jonowe i zagrożenia szczególne | 2.2.9.1.7.2; 2.2.9.3 UN 3551, 3552 |
| `ADR-B-0500` | Producent ma nowy typ baterii sodowo-jonowej objętej 2.2.9.1.7.2. Czy wystarczy, że jej ogniwa spełniają badania 38.3, a… | § 4 — Baterie sodowo-jonowe i zagrożenia szczególne | 2.2.9.1.7.2(a) i uwaga |
| `ADR-B-0501` | Nowy projekt ogniwa sodowo-jonowego przewidziany do wpisu UN 3551 nie zapobiega zewnętrznemu zwarciu. Którego warunku 2.… | § 4 — Baterie sodowo-jonowe i zagrożenia szczególne | 2.2.9.1.7.2(c) |
| `ADR-B-0502` | Bateria sodowo-jonowa z równolegle połączonymi ogniwami nie ma rozwiązania chroniącego przed niebezpiecznym przepływem w… | § 4 — Baterie sodowo-jonowe i zagrożenia szczególne | 2.2.9.1.7.2(d) |
| `ADR-B-0510` | Kierowca przed rozładunkiem dostrzega mokre opakowanie z nalepką klasy 4.3. Pracownik proponuje polewać je wodą, żeby us… | § 4 — Nalepki i oznakowanie | 2.2.43.1.1 |
| `ADR-B-0541` | Na pokazanym schemacie nalepki ADR kierowca widzi zielony romb, symbol butli i cyfrę 2. Który rodzaj zagrożenia przedsta… | § 4 — Nalepki i oznakowanie | 5.2.2.2.2; 2.2.2.1.2 |
| `ADR-B-0542` | Na autorskim schemacie nalepki widoczny jest czerwony romb z białym płomieniem i cyfrą 3. Jaką klasę towarów niebezpiecz… | § 4 — Nalepki i oznakowanie | 5.2.2.2.2; 2.2.3.1.1 |

## ADR-B-03 — 49 pytań

| ID | Pytanie / kompetencja sprawdzana | Fragment podręcznika porównany | Podstawa zapisana w banku |
|---|---|---|---|
| `ADR-B-0007` | Jaki symbol znajduje się na znaku dla materiałów zagrażających środowisku? | § 1 — Znak środowiskowy, wymiary i wpis w dokumencie | 5.2.1.8 |
| `ADR-B-0008` | W dokumencie przewozowym ADR dla odpadu niebezpiecznego niebędącego odpadem promieniotwórczym dodano słowo „ODPAD” przed… | § 3 — Odpady i klasyfikacja | 5.4.1.1.3.1 |
| `ADR-B-0009` | Podczas rozładunku sztuk przesyłek ADR stwierdzono, że zawartość jednego opakowania wyciekła i zabrudziła pojazd. Co nal… | § 2 — Wyciek, opary, oczyszczenie i instrukcje | 7.5.8.1 |
| `ADR-B-0045` | Jak postąpić ze znakiem dla materiału zagrażającego środowisku na sztuce przesyłki, gdy przepisy ADR wymagają takiego zn… | § 1 — Znak środowiskowy, wymiary i wpis w dokumencie | 5.2.1.8 |
| `ADR-B-0046` | Czy przy przewozie odpadów niebezpiecznych słowo „ODPAD” zastępuje numer UN w dokumencie ADR? | § 3 — Odpady i klasyfikacja | 5.4.1.1.1 (a); 5.4.1.1.3.1 |
| `ADR-B-0100` | Po awarii z opakowania wypływa ciecz niebezpieczna w kierunku kratki kanalizacyjnej. Kiedy załoga może próbować zapobiec… | § 2 — Wyciek, opary, oczyszczenie i instrukcje | 5.4.3.4 |
| `ADR-B-0101` | Zauważasz kałużę nieznanej substancji po uszkodzeniu opakowania ADR. Jak powinien zachować się kierowca? | § 2 — Wyciek, opary, oczyszczenie i instrukcje | 5.4.3.4 |
| `ADR-B-0129` | Nadawca nie zna dokładnego składu odpadu bez nieproporcjonalnych kosztów. Czy może zawsze nadać grupę pakowania III? | § 3 — Odpady i klasyfikacja | 2.1.3.5.5 |
| `ADR-B-0163` | Wycieka towar niebezpieczny, a kierowca ma wymagane wyposażenie do osłonięcia odpływu. Kiedy może spróbować osłonić krat… | § 2 — Wyciek, opary, oczyszczenie i instrukcje | 5.4.3.4 |
| `ADR-B-0177` | Po rozładunku ADR w skrzyni ładunkowej wykryto pozostałości wycieku. Na miejscu nie ma możliwości bezpiecznego czyszczen… | § 2 — Wyciek, opary, oczyszczenie i instrukcje | 7.5.8.1 |
| `ADR-B-0178` | Podczas awarii opakowania ADR kierowca zauważa pary unoszące się przy drzwiach ładowni. Jak ograniczyć ryzyko skażenia? | § 2 — Wyciek, opary, oczyszczenie i instrukcje | 5.4.3.4 |
| `ADR-B-0179` | Do przewozu zgłoszono odpad ADR. Nadawca chce w dokumencie przewozowym podać samo słowo „ODPAD”, bez identyfikacji mater… | § 3 — Odpady i klasyfikacja | 5.4.1.1.1; 5.4.1.1.3.1 |
| `ADR-B-0241` | Po rozładunku pusty, nieoczyszczony kontener ADR jedzie zgodnie z 7.5.8.1 do najbliższego odpowiedniego miejsca czyszcze… | § 2 — Wyciek, opary, oczyszczenie i instrukcje | 5.4.1.1.6.3(b); 7.5.8.1 |
| `ADR-B-0242` | Po wycieku ADR substancja zbliża się do kanalizacji. Kiedy załoga może próbować ograniczyć jej odpływ? | § 2 — Wyciek, opary, oczyszczenie i instrukcje | 5.4.3.4 |
| `ADR-B-0276` | Na sztuce przesyłki ADR widnieje znak rombu z czarną sylwetką martwej ryby i drzewa na jasnym tle. Co on oznacza? | § 1 — Znak środowiskowy, wymiary i wpis w dokumencie | 5.2.1.8.3 |
| `ADR-B-0294` | Przewożony jest odpad zawierający towary niebezpieczne (inny niż odpad promieniotwórczy). Co należy zrobić z prawidłową … | § 3 — Odpady i klasyfikacja | 5.4.1.1.3.1 |
| `ADR-B-0295` | Po uszkodzeniu opakowania ADR na drodze pojawił się rozlew i opary. Jak powinien zachować się nieprzeszkolony członek za… | § 2 — Wyciek, opary, oczyszczenie i instrukcje | 5.4.3.4 |
| `ADR-B-0318` | Odpadu przewożonego jako towar niebezpieczny nie da się dokładnie opisać pod względem składu. Co dopuszcza ADR 2.1.3.5.5… | § 3 — Odpady i klasyfikacja | 2.1.3.5.5 |
| `ADR-B-0325` | Z powodu nieznanego składu odpadu nadawca ma wątpliwości co do poziomu zagrożenia. Którą zasadę stosuje w ramach ADR 2.1… | § 3 — Odpady i klasyfikacja | 2.1.3.5.5 |
| `ADR-B-0326` | Odpad o nieznanym dokładnie składzie zawiera substancję klasy 4.3. Czy wolno zastosować uproszczoną procedurę ADR 2.1.3.… | § 3 — Odpady i klasyfikacja | 2.1.3.5.5 |
| `ADR-B-0327` | Nadawca chce sklasyfikować nieznany dokładnie odpad jako UN 3077 lub 3082 w grupie III. Kiedy dopuszcza to ADR 2.1.3.5.5… | § 3 — Odpady i klasyfikacja | 2.1.3.5.5 |
| `ADR-B-0328` | W odpadzie o nieustalonym dokładnie składzie można wykazać, że jego właściwości nie odpowiadają poziomowi grupy pakowani… | § 3 — Odpady i klasyfikacja | 2.1.3.5.5 |
| `ADR-B-0329` | Odpad ma nieznany dokładnie skład, ale wiadomo, że zawiera materiał zakazany do przewozu według przepisów klasyfikacyjny… | § 3 — Odpady i klasyfikacja | 2.1.3.5.5 |
| `ADR-B-0330` | Nieznany dokładnie odpad zawiera materiał należący do klasy 5.2. Co z procedurą 2.1.3.5.5? | § 3 — Odpady i klasyfikacja | 2.1.3.5.3; 2.1.3.5.5 |
| `ADR-B-0331` | Dokładna analiza mieszaniny nie jest możliwa bez nieproporcjonalnych kosztów lub wysiłku. Co przewiduje ADR 2.1.3.5.2? | § 3 — Odpady i klasyfikacja | 2.1.3.5.2 |
| `ADR-B-0332` | W mieszaninie występują różne zagrożenia, a jedno z nich dotyczy substancji klasy 2. Jaki przepis określa szczególną kol… | § 3 — Odpady i klasyfikacja | 2.1.3.5.3 |
| `ADR-B-0333` | Dla mieszaniny zagrożenia należą do klas niewymienionych w szczególnej liście ADR 2.1.3.5.3. Co wskazuje ADR 2.1.3.5.4? | § 3 — Odpady i klasyfikacja | 2.1.3.5.4 |
| `ADR-B-0334` | Dla określonego odpadu możliwa jest zarówno ogólna pozycja i.n.o., jak i bardziej szczegółowa właściwa pozycja zbiorcza.… | § 3 — Odpady i klasyfikacja | 2.1.3.6 |
| `ADR-B-0335` | Nadawca zna fizykochemiczne właściwości składników odpadu, ale nie pełne proporcje. Które dane może wykorzystać w ramach… | § 3 — Odpady i klasyfikacja | 2.1.3.5.5 |
| `ADR-B-0336` | Kto jest wskazany w ADR 2.1.3.5.5 jako podmiot, którego wiedza może stanowić podstawę przypisania odpadu do UN i grupy p… | § 3 — Odpady i klasyfikacja | 2.1.3.5.5 |
| `ADR-B-0337` | Nieznany dokładnie odpad zawiera materiały zakaźne klasy 6.2. Czy procedura 2.1.3.5.5 obejmuje taki odpad? | § 3 — Odpady i klasyfikacja | 2.1.3.5.3; 2.1.3.5.5 |
| `ADR-B-0338` | Odpad o nieznanym dokładnie składzie zawiera materiał samozapalny klasy 4.2 o właściwościach piroforycznych. Jak traktow… | § 3 — Odpady i klasyfikacja | 2.1.3.5.3; 2.1.3.5.5 |
| `ADR-B-0339` | Podczas klasyfikacji odpadu z nieznanym dokładnie składem ktoś proponuje skorzystać z 2.1.3.5.5 mimo występowania materi… | § 3 — Odpady i klasyfikacja | 2.1.3.5.3; 2.1.3.5.5 |
| `ADR-B-0340` | Występujące w mieszaninie zagrożenie spełnia warunki substancji samoreaktywnej klasy 4.1. Czy można zignorować specjalne… | § 3 — Odpady i klasyfikacja | 2.1.3.5.3 |
| `ADR-B-0341` | Kto ma prawo samodzielnie zastąpić klasyfikację ADR odpadu przypadkowym numerem UN z innego towaru? | § 3 — Odpady i klasyfikacja | 2.1.3.5.5 |
| `ADR-B-0342` | W odpadzie występuje ryzyko klasy 7 i inne zagrożenie, a rozpatrywana sytuacja nie podlega wyjątkom z 2.1.3.5.3(a). Któr… | § 3 — Odpady i klasyfikacja | 2.1.3.5.3(a) |
| `ADR-B-0343` | Czy dla odpadu o nieznanym dokładnie składzie samo zakwalifikowanie jako odpadu usuwa konieczność ustalenia właściwej gr… | § 3 — Odpady i klasyfikacja | 2.1.3.5.5 |
| `ADR-B-0344` | Przy klasyfikacji odpadu rozważana jest ogólna pozycja i.n.o., choć dostępna jest odpowiednia pozycja specyficzna i.n.o.… | § 3 — Odpady i klasyfikacja | 2.1.3.6 |
| `ADR-B-0461` | Pojedyncze opakowanie zawiera 4 litry cieczy spełniającej kryteria zagrożenia dla środowiska wodnego. Kiedy może działać… | § 1 — Znak środowiskowy, wymiary i wpis w dokumencie | 5.2.1.8.1 |
| `ADR-B-0462` | Opakowanie kombinowane ma butelki wewnętrzne z materiałem niebezpiecznym dla środowiska, każda zawiera 6 litrów. Czy sam… | § 1 — Znak środowiskowy, wymiary i wpis w dokumencie | 5.2.1.8.1 |
| `ADR-B-0463` | W opakowaniu pojedynczym przewozi się dokładnie 5 kg netto stałego materiału zagrażającego środowisku wodnemu. Jak rozum… | § 1 — Znak środowiskowy, wymiary i wpis w dokumencie | 5.2.1.8.1 |
| `ADR-B-0464` | Na sztuce przesyłki wymagany jest znak materiału niebezpiecznego dla środowiska. Gdzie powinien być umieszczony względem… | § 1 — Znak środowiskowy, wymiary i wpis w dokumencie | 5.2.1.8.2 |
| `ADR-B-0465` | Materiał klasy 3 spełnia także kryteria zagrożenia dla środowiska, a wyjątki 5.2.1.8.1 nie mają zastosowania. Który doda… | § 1 — Znak środowiskowy, wymiary i wpis w dokumencie | 5.4.1.1.18 |
| `ADR-B-0466` | Towar ma numer UN 3077 i spełnia kryteria zagrożenia środowiskowego. Czy 5.4.1.1.18 wymaga dla niego dodatkowego wpisu E… | § 1 — Znak środowiskowy, wymiary i wpis w dokumencie | 5.4.1.1.18 |
| `ADR-B-0467` | W morsko-drogowym łańcuchu przewozu dokument dla materiału niebezpiecznego dla środowiska zawiera określenie MARINE POLL… | § 1 — Znak środowiskowy, wymiary i wpis w dokumencie | 5.4.1.1.18 |
| `ADR-B-0468` | Pojazd wymaga nalepek wielkiego formatu i przewozi towary zagrażające środowisku wodnemu. Kiedy znak środowiskowy według… | § 1 — Znak środowiskowy, wymiary i wpis w dokumencie | 5.3.6.1 |
| `ADR-B-0469` | Jaki standardowy minimalny wymiar znaku środowiskowego przewiduje ADR 5.3.6.2 dla oznakowania kontenera, bez zastosowani… | § 1 — Znak środowiskowy, wymiary i wpis w dokumencie | 5.3.6.2 |
| `ADR-B-0470` | Kontener-cysterna ma pojemność 2500 l i niewystarczającą powierzchnię na standardowy znak środowiskowy. Co dopuszcza 5.3… | § 1 — Znak środowiskowy, wymiary i wpis w dokumencie | 5.3.6.2 |
| `ADR-B-0514` | Po rozładunku ADR załadowca odkrywa, że z jednej sztuki przesyłki wyciekła niebezpieczna ciecz na podłogę kontenera. Pla… | § 2 — Wyciek, opary, oczyszczenie i instrukcje | 7.5.8.1 |

## ADR-B-04 — 46 pytań

| ID | Pytanie / kompetencja sprawdzana | Fragment podręcznika porównany | Podstawa zapisana w banku |
|---|---|---|---|
| `ADR-B-0010` | Czy podczas czynności ładunkowych ADR wolno palić e-papierosa w pobliżu pojazdu? | § 1 — Zasady załogi, palenie, silnik i opakowania | 8.3.5 |
| `ADR-B-0011` | Czy kierowca może samowolnie otworzyć sztukę przesyłki zawierającą towar niebezpieczny? | § 1 — Zasady załogi, palenie, silnik i opakowania | 8.3.3 |
| `ADR-B-0012` | Co do zasady należy zrobić z silnikiem podczas załadunku lub rozładunku towarów niebezpiecznych? | § 1 — Zasady załogi, palenie, silnik i opakowania | 8.3.6 |
| `ADR-B-0047` | Co kierowca powinien zrobić z silnikiem podczas załadunku ADR, jeżeli nie jest potrzebny do napędzania urządzeń? | § 1 — Zasady załogi, palenie, silnik i opakowania | 8.3.6 |
| `ADR-B-0048` | Jak powinna postąpić załoga w sprawie otwierania sztuk przesyłek zawierających towary niebezpieczne podczas przewozu obj… | § 1 — Zasady załogi, palenie, silnik i opakowania | 8.3.3 |
| `ADR-B-0102` | Podczas awarii wyczuwalny jest zapach oparów palnego towaru. Jak postępować z możliwymi źródłami zapłonu? | § 2 — Uszkodzenie, wyciek i bezpieczeństwo | 5.4.3.4 |
| `ADR-B-0103` | Podczas rozładunku ADR drugi członek załogi zaczyna korzystać z e-papierosa. Co należy zrobić? | § 1 — Zasady załogi, palenie, silnik i opakowania | 8.3.5 |
| `ADR-B-0130` | Po uszkodzeniu opakowania ADR na jezdni jest rozlew nieznanej cieczy. Co ogranicza narażenie kierowcy? | § 2 — Uszkodzenie, wyciek i bezpieczeństwo | 5.4.3.4 |
| `ADR-B-0131` | Kiedy szczególne wymagania nadzoru pojazdu z 8.4 ADR mają zastosowanie? | § 3 — Bezpieczny postój i nadzór | 8.4.1; 8.5; 3.2 tabela A kol. (19) |
| `ADR-B-0164` | Po awarii materiału ADR wyczuwalne są palne opary. Dlaczego nie należy używać e-papierosa w pobliżu wycieku? | § 2 — Uszkodzenie, wyciek i bezpieczeństwo | 5.4.3.4 |
| `ADR-B-0180` | Po kolizji opakowanie z materiałem żrącym pękło. Nie ma pewności, czy rękawice kierowcy chronią przed tym materiałem. Co… | § 2 — Uszkodzenie, wyciek i bezpieczeństwo | 5.4.3.4 |
| `ADR-B-0181` | W przewozie objętym wymaganiami 8.4 ADR kierowca nie znajduje chronionego depozytu ani właściwego terenu zakładu. Co pow… | § 3 — Bezpieczny postój i nadzór | 8.4.1 |
| `ADR-B-0243` | Czy członek załogi ADR może otworzyć sztukę przesyłki z towarem niebezpiecznym podczas przewozu? | § 1 — Zasady załogi, palenie, silnik i opakowania | 8.3.3 |
| `ADR-B-0244` | Podczas załadunku ADR silnik pojazdu pracuje, chociaż nie napędza żadnego urządzenia. Co należy zrobić? | § 1 — Zasady załogi, palenie, silnik i opakowania | 8.3.6 |
| `ADR-B-0279` | Podczas załadunku ADR pracownik korzysta z papierosa elektronicznego obok pojazdu. Czy jest to zgodne z ADR? | § 1 — Zasady załogi, palenie, silnik i opakowania | 8.3.5 |
| `ADR-B-0280` | Podczas rozładunku ADR kierowca widzi osobę palącą wewnątrz pojazdu. Jak ocenia to ADR 8.3.5? | § 1 — Zasady załogi, palenie, silnik i opakowania | 8.3.5 |
| `ADR-B-0296` | Podczas awarii ADR kierowca chce sprawdzić ładunek, używając papierosa elektronicznego i przełączając urządzenia elektry… | § 2 — Uszkodzenie, wyciek i bezpieczeństwo | 5.4.3.4 |
| `ADR-B-0297` | Po kolizji pojazdu ADR w pobliżu zbiera się tłum, a na drodze są opary. Co załoga powinna zrobić, jeżeli można to zrobić… | § 2 — Uszkodzenie, wyciek i bezpieczeństwo | 5.4.3.4 |
| `ADR-B-0310` | Towary i ich ilości powodują zastosowanie nadzoru nad pojazdem z ADR 8.4.1. Gdzie w pierwszej kolejności można bez dozor… | § 3 — Bezpieczny postój i nadzór | 8.4.1 |
| `ADR-B-0345` | Pojazd ADR objęty 8.4.1 stoi bez dozoru na ogólnodostępnym parkingu, choć dostępny jest bezpieczny teren zakładu. Co jes… | § 3 — Bezpieczny postój i nadzór | 8.4.1 |
| `ADR-B-0346` | Nie ma zabezpieczonej bazy ani terenu zakładu. Dostępny jest parking dozorowany przez obsługę. Jaki dodatkowy warunek do… | § 3 — Bezpieczny postój i nadzór | 8.4.1(a) |
| `ADR-B-0347` | Przy przewozie wymagającym nadzoru 8.4.1 dostępny jest parking z dozorcą spełniający wymogi lit. (a). Czy można zamiast … | § 3 — Bezpieczny postój i nadzór | 8.4.1(a)–(b) |
| `ADR-B-0348` | W przewozie objętym 8.4.1 nie ma zabezpieczonej bazy, parkingu dozorowanego ani odpowiedniego parkingu publicznego. Gdzi… | § 3 — Bezpieczny postój i nadzór | 8.4.1(c) |
| `ADR-B-0349` | Który teren odpowiada warunkowi lit. (c) w 8.4.1, gdy wcześniejsze rodzaje parkingów nie są dostępne? | § 3 — Bezpieczny postój i nadzór | 8.4.1(c) |
| `ADR-B-0350` | Jak sprawdzić, czy dany przewóz podlega szczególnemu nadzorowi na podstawie 8.4.1? | § 3 — Bezpieczny postój i nadzór | 8.4.1; 3.2 tabela A kol. (19) |
| `ADR-B-0351` | Pojazd przewożący towary niebezpieczne zaparkowano na płaskim terenie. Jakie podstawowe zabezpieczenie postojowe wymaga … | § 1 — Zasady załogi, palenie, silnik i opakowania | 8.3.7 |
| `ADR-B-0352` | Przyczepa przewożąca towary niebezpieczne nie ma własnego urządzenia hamującego. Co wymaga ADR 8.3.7 podczas postoju? | § 1 — Zasady załogi, palenie, silnik i opakowania | 8.3.7; 8.1.5.2 |
| `ADR-B-0353` | Na parkingu kierowca pojazdu ADR chce użyć przenośnej lampy, której metalowa część może wytwarzać iskry. Co stanowi ADR … | § 3 — Bezpieczny postój i nadzór | 8.3.4 |
| `ADR-B-0354` | Podczas awarii towary niebezpieczne rozlały się obok pojazdu. Kierowca chce wejść w kałużę, aby odczytać etykietę. Co ws… | § 2 — Uszkodzenie, wyciek i bezpieczeństwo | 5.4.3.4 |
| `ADR-B-0355` | W czasie wypadku przy ładunku ADR gromadzą się opary. Gdzie w miarę możliwości powinna przebywać załoga? | § 2 — Uszkodzenie, wyciek i bezpieczeństwo | 5.4.3.4 |
| `ADR-B-0356` | Po kontakcie z wyciekiem ADR część odzieży została skażona. Jakie działanie przewiduje instrukcja pisemna? | § 2 — Uszkodzenie, wyciek i bezpieczeństwo | 5.4.3.4 |
| `ADR-B-0357` | Kierowca chce otworzyć opakowanie ADR, aby sprawdzić, czy nie pojawił się wyciek. Co przewiduje 8.3.3? | § 1 — Zasady załogi, palenie, silnik i opakowania | 8.3.3 |
| `ADR-B-0358` | W czasie rozładunku pompa musi pracować z napędu silnika pojazdu. Kiedy może on pozostać włączony? | § 1 — Zasady załogi, palenie, silnik i opakowania | 8.3.6 |
| `ADR-B-0359` | Przy załadunku ADR silnik pozostaje włączony tylko dla klimatyzacji, nie napędza urządzeń przeładunkowych. Jak postąpić? | § 1 — Zasady załogi, palenie, silnik i opakowania | 8.3.6 |
| `ADR-B-0360` | Podczas przeładunku ADR ktoś pali poza kabiną, lecz bezpośrednio przy pojeździe. Jak należy ocenić sytuację? | § 1 — Zasady załogi, palenie, silnik i opakowania | 8.3.5 |
| `ADR-B-0361` | Po awarii kierowca rozważa włączenie urządzenia elektrycznego w pobliżu palnych oparów. Co nakazuje instrukcja pisemna A… | § 2 — Uszkodzenie, wyciek i bezpieczeństwo | 5.4.3.4 |
| `ADR-B-0362` | Po wypadku jednostki ADR na miejscu pojawia się służba ratownicza. Co załoga powinna mieć łatwo dostępne dla ratowników? | § 2 — Uszkodzenie, wyciek i bezpieczeństwo | 5.4.3.4 |
| `ADR-B-0471` | Przewóz towarów niebezpiecznych objęty ADR odbywa się ciężarówką; znajomy kierowcy chce jechać na wolnym fotelu, nie będ… | § 1 — Zasady załogi, palenie, silnik i opakowania | 8.3.1 |
| `ADR-B-0472` | W pojeździe ADR załoga ma gaśnicę zgodną z wymaganiami, ale nie wie, jak jej użyć. Czego dodatkowo wymaga ADR? | § 1 — Zasady załogi, palenie, silnik i opakowania | 8.3.2 |
| `ADR-B-0473` | Pojazd ADR z układem ABS ciągnie przyczepę o maksymalnej masie ponad 3,5 t. Co 8.3.8 wymaga od połączeń elektrycznych, o… | § 1 — Zasady załogi, palenie, silnik i opakowania | 8.3.8 |
| `ADR-B-0474` | Przed załadunkiem ADR kontrola dokumentów ujawnia niespełnienie wymagań przez kierowcę lub pojazd. Jak należy postąpić w… | § 2 — Uszkodzenie, wyciek i bezpieczeństwo | 7.5.1.2 |
| `ADR-B-0475` | Przed załadunkiem kontenera pojawia się uszkodzenie jego ściany mogące naruszyć ochronę opakowań. Jak stosuje się 7.5.1.… | § 2 — Uszkodzenie, wyciek i bezpieczeństwo | 7.5.1.2 |
| `ADR-B-0476` | Podczas rozładunku ADR wykryto uszkodzone wyposażenie pojazdu sprzeczne z wymaganiami. Jaką zasadę 7.5.1.3 należy rozważ… | § 2 — Uszkodzenie, wyciek i bezpieczeństwo | 7.5.1.3 |
| `ADR-B-0515` | W trakcie rozładunku sztuk przesyłek ADR pracownik prosi kierowcę o pozostawienie uruchomionego silnika dla ogrzania kab… | § 1 — Zasady załogi, palenie, silnik i opakowania | 8.3.6 |
| `ADR-B-0580` | Przy danym przewozie mają zastosowanie wymagania ADR dotyczące nadzoru i postoju. Kierowca planuje przerwę. Co powinien … | § 3 — Bezpieczny postój i nadzór | 8.4; 8.5 |
| `ADR-B-0581` | Dyspozytor proponuje pozostawienie pojazdu bez nadzoru na zwykłym parkingu, mimo że dla tego przewozu stosuje się ADR 8.… | § 3 — Bezpieczny postój i nadzór | 8.4; 8.5 |


## Zakończenie

- Lekcje zaktualizowano bez datowanych dopisków ani nagłówków roboczych.
- Nie zmieniono kluczy ani `module_id`; zmieniono tylko dwa dystraktory i odpowiadające im explanation.
- Egzaminy próbne 001–003 zachowują referencje do istniejących pytań; nie wymagały regeneracji.
- Wymagane pozostają PASS CI oraz niezależna recenzja specjalisty. Niczego nie oznaczono jako `verified`.
