# ETAP 4x3 — zgodność banku z podręcznikiem: ADR-B-01–04

- Data: 25.10.2026.
- Punkt wyjścia: `main` po scaleniu ETAPU 4x2, commit `3df29e95e4e9a42cc38208b362437829ce561570`.
- Zakres audytu: wszystkie pytania przypisane do B-01–B-04; tylko kurs podstawowy.
- Metoda: dla każdego rekordu porównano treść pytania, klucz i explanation z odpowiednim fragmentem lekcji oraz podstawą wskazaną w źródłach pytania. Poniższa mapa jest śladem audytu do ponownej kontroli, a nie oznaczeniem pytań jako zweryfikowanych.

## ADR-B-01 — 45 pytań

| ID pytania | Wymagana wiedza / pytanie | Fragment lekcji | Odniesienie źródłowe |
|---|---|---|---|
| `ADR-B-0001` | Jakie szkolenie powinien otrzymać pracownik nadawcy, którego obowiązki dotyczą przewozu towarów niebezpiecznych? | § 3. Szkolenie a zaświadczenie kierowcy | ADR 2025, 1.3.2 |
| `ADR-B-0002` | Czy przewóz niewielkiej ilości towarów niebezpiecznych automatycznie zwalnia kierowcę ze wszystkich wymagań ADR? | § 3. Szkolenie a zaświadczenie kierowcy | ADR 2025, 1.1.3 |
| `ADR-B-0003` | Do czego służy zaświadczenie ADR kierowcy? | § 3. Szkolenie a zaświadczenie kierowcy | ADR 2025, 8.2.1 |
| `ADR-B-0040` | Kiedy pracownik przedsiębiorstwa wykonujący obowiązki związane z ADR powinien odbyć odpowiednie przeszkolenie? | § 3. Szkolenie a zaświadczenie kierowcy | ADR 2025, 1.3.1 |
| `ADR-B-0041` | Dlaczego szkolenie pracowników dotyczące ADR trzeba okresowo uzupełniać? | § 3. Szkolenie a zaświadczenie kierowcy | ADR 2025, 1.3.2.4 |
| `ADR-B-0091` | Firma kupuje paletę farb zaklasyfikowanych jako towary niebezpieczne w ADR z przeznaczeniem do dalszej sprzedaży. Czy automatycznie korzysta z wyłączenia 1.1.3.1(a) dla osób prywatnych? | § 3. Szkolenie a zaświadczenie kierowcy | ADR 2025, 1.1.3.1 (a) |
| `ADR-B-0092` | Nowy pracownik magazynu nie przeszedł jeszcze szkolenia ADR odpowiedniego do zadań. Co przewiduje 1.3.1, zanim ukończy szkolenie? | § 3. Szkolenie a zaświadczenie kierowcy | ADR 2025, 1.3.1 |
| `ADR-B-0093` | Przedsiębiorca twierdzi, że oznakowanie LQ zawsze oznacza wyłączenie na podstawie 1.1.3.6. Czy ma rację? | § 3. Szkolenie a zaświadczenie kierowcy | ADR 2025, 3.4; 1.1.3.6 |
| `ADR-B-0123` | Co oznacza określenie „towary niebezpieczne” w umowie ADR? | § 1 i § 5. Zakres ADR, jednostka transportowa, tabela A | ADR 2025, Umowa ADR, art. 1(b) |
| `ADR-B-0124` | Nadawca chce przewieźć nowy materiał niebezpieczny. Co powinien ustalić przed wyborem sposobu przewozu? | § 1 i § 5. Zakres ADR, jednostka transportowa, tabela A | ADR 2025, 2.1.1; 3.2 tabela A |
| `ADR-B-0125` | W której kolumnie tabeli A ADR znajduje się numer UN materiału? | § 1 i § 5. Zakres ADR, jednostka transportowa, tabela A | ADR 2025, 3.2.1, tabela A kol. (1) |
| `ADR-B-0147` | Do pracy przy przewozie ADR skierowano ciągnik samochodowy z naczepą. Jak ADR traktuje taki zestaw przy wymaganiach odnoszących się do jednostki transportowej? | § 1 i § 5. Zakres ADR, jednostka transportowa, tabela A | ADR 2025, 1.2.1, definicja transport unit |
| `ADR-B-0148` | Kierowca ma aktualne zaświadczenie ADR, ale nie ma prawa jazdy odpowiedniej kategorii na prowadzony zestaw. Co z tego wynika? | § 3. Szkolenie a zaświadczenie kierowcy | ADR 2025, 8.2.1; prawo krajowe o uprawnieniach do kierowania |
| `ADR-B-0149` | Jak sprawdza się limit ilości ograniczonej (LQ) dla konkretnego numeru UN? | § 4.2–4.3. LQ i EQ | ADR 2025, 3.2 tabela A kol. (7a); 3.4.1 |
| `ADR-B-0259` | Wszystkie towary na jednostce transportowej zaliczono do kategorii transportowej 3. Jaki limit ilości z tabeli ADR 1.1.3.6.3 obowiązuje co do zasady dla tej kategorii? | § 3. Szkolenie a zaświadczenie kierowcy | ADR 2025, 1.1.3.6.3 |
| `ADR-B-0260` | Towar ma w kolumnie 7b tabeli A kod EQ „E0”. Jak należy ocenić możliwość zastosowania wyłączenia dla ilości wyłączonych? | § 4.2–4.3. LQ i EQ | ADR 2025, 3.5.1.2 |
| `ADR-B-0261` | Towar niebezpieczny dopuszczony do przewozu jako LQ umieszczono w zwykłym odpowiednim opakowaniu zewnętrznym z opakowaniami wewnętrznymi. Ile może wynosić co do zasady maksymalna masa brutto takiej sztuki przesyłki zgodnie z ADR 3.4.2? | § 4.2–4.3. LQ i EQ | ADR 2025, 3.4.2 |
| `ADR-B-0271` | W jednostce transportowej przewożone są towary kategorii transportowej 2 w ilości 100 jednostek i kategorii 3 w ilości 600 jednostek (ilości obliczone według ADR). Ile wynosi suma punktów według 1.1.3.6.4? | § 3. Szkolenie a zaświadczenie kierowcy | ADR 2025, 1.1.3.6.4 |
| `ADR-B-0272` | Jednostka transportowa przewozi 200 jednostek kategorii transportowej 2 i 500 jednostek kategorii 3. Co wynika z samego wyniku obliczenia 1.1.3.6.4? | § 3. Szkolenie a zaświadczenie kierowcy | ADR 2025, 1.1.3.6.4 |
| `ADR-B-0273` | Na sztuce przesyłki przewożonej na zasadach LQ jest znak w kształcie rombu z czarną górą i dołem oraz białym środkiem. Który opis jest poprawny? | § 4.2–4.3. LQ i EQ | ADR 2025, 3.4.7.1 |
| `ADR-B-0301` | Kierowca realizuje przewóz towarów niebezpiecznych, dla którego wymagane jest zaświadczenie ADR. Co musi wykazać, aby uzyskać takie zaświadczenie? | § 3. Szkolenie a zaświadczenie kierowcy | ADR 2025, 8.2.1.1 |
| `ADR-B-0312` | Co obejmuje definicja „przewozu” w ADR 1.2.1, oprócz przemieszczania pojazdu z towarem niebezpiecznym? | § 1 i § 5. Zakres ADR, jednostka transportowa, tabela A | ADR 2025, 1.2.1 |
| `ADR-B-0313` | Osoba prywatna przewozi niebezpieczny produkt w opakowaniu detalicznym do własnego użytku domowego. Jaki warunek jest istotny dla wyłączenia z ADR 1.1.3.1(a)(i)? | § 3. Szkolenie a zaświadczenie kierowcy | ADR 2025, 1.1.3.1(a)(i) |
| `ADR-B-0314` | Gdzie w tabeli A ADR 2025 należy szukać nazwy przewozowej odpowiadającej konkretnemu numerowi UN? | § 1 i § 5. Zakres ADR, jednostka transportowa, tabela A | ADR 2025, 3.2.1, objaśnienie kolumny (2) |
| `ADR-B-0323` | W jednej jednostce transportowej przewożone są razem towary kategorii transportowej 2 i 3. Jak należy ocenić zwolnienie ilościowe z ADR 1.1.3.6? | § 3. Szkolenie a zaświadczenie kierowcy | ADR 2025, 1.1.3.6.4 |
| `ADR-B-0513` | Nowy pracownik terminalu zaczyna obsługiwać dokumenty towarów niebezpiecznych. Nie odbył jeszcze szkolenia ADR odpowiedniego do swoich obowiązków. Jak może wykonywać te zadania do czasu wymaganego przeszkolenia? | § 3. Szkolenie a zaświadczenie kierowcy | ADR 2025, 1.3.1 |
| `ADR-B-0520` | Inspektor właściwej władzy prosi pracodawcę o dokumentację szkolenia ADR 1.3 pracownika kompletującego przesyłki. Jak powinien postąpić pracodawca? | § 3. Szkolenie a zaświadczenie kierowcy | ADR 2025, 1.3.3 |
| `ADR-B-0521` | Pracownik przechodzi do nowego przedsiębiorstwa i ma wykonywać czynności podlegające szkoleniu ADR 1.3. Co należy sprawdzić przy rozpoczęciu zatrudnienia? | § 3. Szkolenie a zaświadczenie kierowcy | ADR 2025, 1.3.3 |
| `ADR-B-0522` | Pracownik terminalu obsługuje drogowo-morski łańcuch transportowy z towarami niebezpiecznymi. Jakie szkolenie funkcjonalne dotyczące innych gałęzi transportu przewiduje ADR? | § 3. Szkolenie a zaświadczenie kierowcy | ADR 2025, 1.3.2.2 |
| `ADR-B-0526` | Kierowca ma przewieźć 1 050 sztuk przesyłek z towarami niebezpiecznymi w ilościach wyłączonych EQ w jednym pojeździe. Jak należy ocenić liczbę sztuk według ADR 3.5.5? | § 4.2–4.3. LQ i EQ | ADR 2025, 3.5.5 |
| `ADR-B-0527` | Wraz z przesyłkami w ilościach wyłączonych EQ przewoźnik otrzymał list przewozowy. Jaka informacja dotycząca EQ powinna znaleźć się co najmniej w jednym z dokumentów towarzyszących? | § 4.2–4.3. LQ i EQ | ADR 2025, 3.5.6 |
| `ADR-B-0528` | Magazynier umieszcza przesyłki oznaczone EQ w opakowaniu zbiorczym. Oznaczenia wewnętrznych sztuk nie są widoczne. Jakie dodatkowe oznakowanie opakowania zbiorczego przewiduje ADR 3.5.4.3? | § 4.2–4.3. LQ i EQ | ADR 2025, 3.5.4.3 |
| `ADR-B-0529` | Pracownik punktu przeładunkowego ma kontakt z niebezpiecznymi substancjami podczas typowych obowiązków. Jaki element szkolenia odpowiada wymaganiu ADR 1.3.2.3? | § 3. Szkolenie a zaświadczenie kierowcy | ADR 2025, 1.3.2.3 |
| `ADR-B-0534` | Na terminalu połączono kilka opakowań LQ w opakowanie zbiorcze. Oznaczenia LQ poszczególnych sztuk są niewidoczne. Jak powinno być oznakowane opakowanie zbiorcze? | § 4.2–4.3. LQ i EQ | ADR 2025, 3.4.11 |
| `ADR-B-0535` | Nadawca przekazuje przewoźnikowi partię towarów w ilościach ograniczonych LQ. Jaką informację powinien przed przewozem przekazać mu w możliwej do udokumentowania formie? | § 4.2–4.3. LQ i EQ | ADR 2025, 3.4.12 |
| `ADR-B-0570` | Kierowca ma 100 jednostek kategorii transportowej 2 i 600 kategorii 3 w sztukach przesyłek. Ile wynosi wynik ADR 1.1.3.6.4? | § 3. Szkolenie a zaświadczenie kierowcy | ADR 2025, 1.1.3.6.4 |
| `ADR-B-0571` | W pojeździe przewożono 250 jednostek kategorii transportowej 2 i 300 kategorii 3. Czy obliczony wynik przekracza próg 1000? | § 3. Szkolenie a zaświadczenie kierowcy | ADR 2025, 1.1.3.6.4 |
| `ADR-B-0572` | Magazyn przygotował 990 sztuk przesyłek EQ w jednym pojeździe. Co jeszcze należy ocenić oprócz liczby sztuk? | § 4.2–4.3. LQ i EQ | ADR 2025, 3.5.1–3.5.6 |
| `ADR-B-0573` | Dokumenty przesyłek w ilościach wyłączonych EQ nie podają liczby sztuk przesyłek. Co należy zrobić przed rozpoczęciem przewozu? | § 4.2–4.3. LQ i EQ | ADR 2025, 3.5.6 |
| `ADR-B-0595` | Osoba prywatna przewozi niewielką ilość produktu niebezpiecznego do własnego użytku. Czy sam prywatny cel automatycznie zwalnia ją z ADR? | § 3. Szkolenie a zaświadczenie kierowcy | ADR 2025, 1.1.3.1(a) |
| `ADR-B-0605` | Sztuka przesyłki jest oznaczona jako przewóz w ilościach ograniczonych (LQ), ale opakowanie zewnętrzne waży 32 kg brutto. Czy samo oznaczenie LQ wystarcza? | § 4.2–4.3. LQ i EQ | ADR 2025, 3.4.2 |
| `ADR-B-0606` | Kierowca ocenia przewóz według wyłączenia ilościowego z ADR 1.1.3.6 i sprawdza tylko masę całego ładunku. Czy to wystarcza? | § 3. Szkolenie a zaświadczenie kierowcy | ADR 2025, 1.1.3.6.3–1.1.3.6.4 |
| `ADR-B-0607` | Kierowca ma ważne prawo jazdy, ale nie ma zaświadczenia ADR. Przewóz przekracza warunki wyłączenia, przy których zaświadczenie nie jest wymagane. Czy może rozpocząć jazdę? | § 3. Szkolenie a zaświadczenie kierowcy | ADR 2025, 8.2.1.1 |
| `ADR-B-0608` | W tabeli A ADR przy danym numerze UN wskazano warunek, który zabrania przewozu tej substancji w opisanej postaci. Nadawca mimo to przygotował dokumenty. Co powinien zrobić przewoźnik? | § 1 i § 5. Zakres ADR, jednostka transportowa, tabela A | ADR 2025, 2.1; 3.2, tabela A |
| `ADR-B-0609` | Przesyłki LQ są prawidłowo zapakowane, ale kierowca chce usunąć oznaczenie ilości ograniczonych z opakowania, aby wyglądało jak zwykła przesyłka. Czy może? | § 4.2–4.3. LQ i EQ | ADR 2025, 3.4.7.1 |

### Uzupełnienia w lekcji B-01
- ADR 1.3: dodano zapisy szkolenia, sprawdzenie wcześniejszego szkolenia przy zmianie przedsiębiorstwa, szkolenie uzupełniające, nadzór do czasu przeszkolenia oraz zakres szkolenia w łańcuchu wielogałęziowym.
- ADR 1.2.1 / 8.2: doprecyzowano znaczenie jednostki transportowej, szeroką definicję przewozu, rozdzielenie prawa jazdy i zaświadczenia ADR oraz sprawdzanie wymagań szczególnych dla klasy 7.
- LQ/EQ: dodano kolumny 7a/7b tabeli A, limit 1000 sztuk EQ, wymagane informacje w dokumentach EQ, oznakowanie OVERPACK, obowiązek informacyjny nadawcy LQ oraz czytelność znaku LQ.
- Doprecyzowano, że próg 1.1.3.6 nie jest jedynym warunkiem zgodności i że kategorie oraz jednostki trzeba sprawdzać osobno.

### Poprawki merytoryczne w banku
Nie znaleziono w tej partii potwierdzonej sprzeczności wymagającej zmiany treści pytania, klucza lub explanation. Nie zmieniono banku ani statusów.

## ADR-B-02 — 56 pytań

| ID pytania | Wymagana wiedza / pytanie | Fragment lekcji | Odniesienie źródłowe |
|---|---|---|---|
| `ADR-B-0004` | Do której klasy ADR należą materiały ciekłe zapalne, takie jak benzyna? | § 2 i § 4. Klasy ADR oraz rozpoznawanie nalepek | ADR 2025, 2.2.3.1.1 |
| `ADR-B-0005` | Jakie zagrożenie oznacza klasa 8 ADR? | § 2 i § 4. Klasy ADR oraz rozpoznawanie nalepek | ADR 2025, 2.2.8.1.1 |
| `ADR-B-0006` | Która cecha jest charakterystyczna dla materiałów klasy 4.3 ADR? | § 2 i § 4. Klasy ADR oraz rozpoznawanie nalepek | ADR 2025, 2.2.43.1.1 |
| `ADR-B-0042` | Do której klasy ADR zalicza się gazy? | § 2. Klasa 1 | ADR 2025, 2.2.2.1.1 |
| `ADR-B-0043` | Jaka klasa ADR dotyczy materiałów zakaźnych? | § 2 i § 4. Klasy ADR oraz rozpoznawanie nalepek | ADR 2025, 2.2.62.1.1 |
| `ADR-B-0044` | Co jest głównym zagrożeniem materiałów klasy 5.1? | § 2 i § 4. Klasy ADR oraz rozpoznawanie nalepek | ADR 2025, 2.2.51.1.1 |
| `ADR-B-0094` | Która klasa ADR obejmuje materiały stałe zapalne? | § 2 i § 4. Klasy ADR oraz rozpoznawanie nalepek | ADR 2025, 2.2.41.1.1 |
| `ADR-B-0095` | Która klasa ADR dotyczy materiałów zdolnych do samozapalenia? | § 2 i § 4. Klasy ADR oraz rozpoznawanie nalepek | ADR 2025, 2.2.42.1.1 |
| `ADR-B-0096` | Do której klasy ADR zalicza się nadtlenki organiczne? | § 2 i § 4. Klasy ADR oraz rozpoznawanie nalepek | ADR 2025, 2.2.52.1.1 |
| `ADR-B-0097` | Która klasa ADR oznacza materiały trujące? | § 2 i § 4. Klasy ADR oraz rozpoznawanie nalepek | ADR 2025, 2.2.61.1.1 |
| `ADR-B-0098` | Do jakiej klasy ADR zaliczono materiały promieniotwórcze? | § 4. Klasa 7 i ograniczenia szkoleniowe | ADR 2025, 2.2.7.1 |
| `ADR-B-0099` | Jaką klasę zagrożenia ADR przedstawiają nalepki ostrzegawcze wzoru 9 i 9A, jeżeli są wymagane dla towaru? | § 4. Nalepki i oznakowanie | ADR 2025, 2.2.9.1.1; 5.2.2.2.2 |
| `ADR-B-0126` | Co oznacza podklasa 1.1 materiałów i przedmiotów wybuchowych? | § 2. Klasa 1 | ADR 2025, 2.2.1.1.5 |
| `ADR-B-0127` | Która grupa pakowania, tam gdzie ADR stosuje grupy I, II i III, oznacza wysoki stopień zagrożenia? | § 3. Grupa pakowania | ADR 2025, 2.1.1.3 |
| `ADR-B-0128` | Gdzie w tabeli A ADR podany jest numer klasy zagrożenia przypisany materiałowi? | § 1. Tabela A i dane towaru | ADR 2025, 3.2.1 tabela A kol. (3a) |
| `ADR-B-0150` | Co odróżnia zagrożenie wybuchem masowym w podklasie 1.1 od podklasy 1.4? | § 2. Klasa 1 | ADR 2025, 2.2.1.1.5 |
| `ADR-B-0151` | Na przesyłce znajduje się nalepka 2.3. Jakiego podstawowego zagrożenia należy się spodziewać? | § 4. Nalepki i oznakowanie | ADR 2025, 5.2.2.2.2, wzór nr 2.3; 2.2.2 |
| `ADR-B-0152` | Podczas przeładunku cieczy zapalnej klasy 3 ktoś chce zapalić papierosa obok pojazdu. Jaka jest prawidłowa reakcja? | § 2 i § 4. Klasy ADR oraz rozpoznawanie nalepek | ADR 2025, 2.2.3; 8.3.5 |
| `ADR-B-0153` | Jakie rozróżnienie między klasą 4.1 a 4.3 jest prawidłowe? | § 2 i § 4. Klasy ADR oraz rozpoznawanie nalepek | ADR 2025, 2.2.41.1.1; 2.2.43.1.1 |
| `ADR-B-0154` | Dlaczego materiał samonagrzewający się z klasy 4.2 wymaga zachowania ostrożności podczas przewozu? | § 2 i § 4. Klasy ADR oraz rozpoznawanie nalepek | ADR 2025, 2.2.42.1.1 |
| `ADR-B-0155` | Po rozszczelnieniu opakowania klasy 4.3 świadek proponuje polanie wycieku wodą. Jak powinien zareagować kierowca? | § 2 i § 4. Klasy ADR oraz rozpoznawanie nalepek | ADR 2025, 2.2.43.1.1; 5.4.3.4 |
| `ADR-B-0156` | Czy materiał klasy 5.1 może zwiększać intensywność pożaru innego materiału? | § 2 i § 4. Klasy ADR oraz rozpoznawanie nalepek | ADR 2025, 2.2.51.1.1 |
| `ADR-B-0157` | Która odpowiedź właściwie rozróżnia klasy 5.1 i 5.2? | § 2 i § 4. Klasy ADR oraz rozpoznawanie nalepek | ADR 2025, 2.2.51; 2.2.52 |
| `ADR-B-0158` | Co należy rozpoznać po nalepce ostrzegawczej 6.1? | § 4. Nalepki i oznakowanie | ADR 2025, 5.2.2.2.2 wzór nr 6.1; 2.2.61.1.1 |
| `ADR-B-0159` | Jaka różnica między klasą 6.2 a 6.1 jest prawidłowa? | § 2 i § 4. Klasy ADR oraz rozpoznawanie nalepek | ADR 2025, 2.2.62.1.1; 2.2.61.1.1 |
| `ADR-B-0160` | Kierowca ukończył wyłącznie kurs podstawowy ADR. Czy uprawnia go to automatycznie do każdego przewozu materiałów promieniotwórczych klasy 7? | § 4. Klasa 7 i ograniczenia szkoleniowe | ADR 2025, 8.2.1.4; 8.5 przepis szczególny S12 |
| `ADR-B-0161` | Jakie zagrożenie powinien brać pod uwagę kierowca widząc nalepkę klasy 8? | § 4. Nalepki i oznakowanie | ADR 2025, 2.2.8.1.1; 5.2.2.2.2 wzór nr 8 |
| `ADR-B-0162` | Nalepka ostrzegawcza 9A może być wymagana podczas przewozu jakich baterii, zgodnie z odpowiednią pozycją ADR 2025? | § 1. Tabela A i dane towaru | ADR 2025, 5.2.2.2.2 (model nr 9A); 3.2 tabela A: UN 3551, UN 3552; 2.2.9.1.7.2 |
| `ADR-B-0218` | Na opakowaniu towaru niebezpiecznego wymagane są dwie różne nalepki ostrzegawcze: zagrożenia głównego i dodatkowego. Co powinien z tego wywnioskować kierowca? | § 1. Tabela A i dane towaru | ADR 2025, 5.2.2.1.1; 3.2.1 tabela A kolumna (5) |
| `ADR-B-0265` | Na opakowaniu wymagane jest ostrzeżenie klasy 4.3. Jakie zagrożenie powinien rozpoznać kierowca? | § 2 i § 4. Klasy ADR oraz rozpoznawanie nalepek | ADR 2025, 2.2.43.1.1 |
| `ADR-B-0266` | Opis towaru ADR wskazuje klasę 5.1 i odpowiednią nalepkę. Jakie zagrożenie należy uwzględnić? | § 2 i § 4. Klasy ADR oraz rozpoznawanie nalepek | ADR 2025, 2.2.51.1.1 |
| `ADR-B-0267` | Na sztuce przesyłki wymagana jest nalepka klasy 8. Co oznacza rozpoznawane zagrożenie? | § 2 i § 4. Klasy ADR oraz rozpoznawanie nalepek | ADR 2025, 2.2.8.1.1 |
| `ADR-B-0268` | Sztuka przesyłki ma nalepkę wzoru 4.1: białe tło z pionowymi czerwonymi pasami i symbolem płomienia. Jaką klasę oznacza? | § 4. Nalepki i oznakowanie | ADR 2025, 5.2.2.2.2 |
| `ADR-B-0269` | Na wymaganej nalepce wzoru 4.3 widzisz płomień na niebieskim tle. Którą klasę rozpoznajesz? | § 4. Nalepki i oznakowanie | ADR 2025, 5.2.2.2.2 |
| `ADR-B-0270` | Na sztuce przesyłki widnieje nalepka z czarnym płomieniem nad okręgiem na żółtym tle. Jaki wzór nalepki opisano? | § 4. Nalepki i oznakowanie | ADR 2025, 5.2.2.2.2 |
| `ADR-B-0284` | Na nalepce widoczny jest symbol butli gazowej na zielonym tle i numer 2 u dołu. Jaką grupę zagrożeń oznacza ten wzór? | § 4. Nalepki i oznakowanie | ADR 2025, 5.2.2.2.2 |
| `ADR-B-0288` | Na nalepce zagrożenia jest biały symbol płomienia na czerwonym tle oraz cyfra 3 na dole. Jaką klasę przedstawia ten wzór? | § 4. Nalepki i oznakowanie | ADR 2025, 5.2.2.2.2 |
| `ADR-B-0289` | Nalepka wzoru 6.1 ma symbol czaszki ze skrzyżowanymi piszczelami. Jakie zagrożenie rozpoznaje kierowca? | § 4. Nalepki i oznakowanie | ADR 2025, 5.2.2.2.2 |
| `ADR-B-0302` | W dokumentacji transportowej wskazano klasę 4.2. Jakiego rodzaju zagrożenie powinien rozpoznać kierowca? | § 2 i § 4. Klasy ADR oraz rozpoznawanie nalepek | ADR 2025, 2.2.42.1.1 |
| `ADR-B-0307` | W przewozie ADR znajduje się nadtlenek organiczny klasy 5.2. Dlaczego nie należy narażać go na niekontrolowane ogrzewanie? | § 2 i § 4. Klasy ADR oraz rozpoznawanie nalepek | ADR 2025, 2.2.52.1.2, 2.2.52.1.4 |
| `ADR-B-0309` | Materiał zawiera drobnoustroje, które mogą powodować choroby u ludzi albo zwierząt. Jaką klasę ADR należy sprawdzić przy klasyfikacji? | § 2 i § 4. Klasy ADR oraz rozpoznawanie nalepek | ADR 2025, 2.2.62.1.1 |
| `ADR-B-0311` | Przewóz dotyczy materiału zakaźnego, w którym patogen może powodować chorobę tylko u zwierząt. Które rozróżnienie klasy 6.2 należy wziąć pod uwagę? | § 2 i § 4. Klasy ADR oraz rozpoznawanie nalepek | ADR 2025, 2.2.62.1.2 |
| `ADR-B-0315` | Nowe regulacje ADR 2025 wymieniają baterie sodowo-jonowe z elektrolitem organicznym jako UN 3551. Do której klasy należą zgodnie z wykazem? | § 4. Baterie sodowo-jonowe | ADR 2025, 2.2.9.1.7.2; tabela A UN 3551 |
| `ADR-B-0316` | W klasyfikacji ADR klasy 1 podklasa 1.1 oznacza zagrożenie jakiego rodzaju? | § 2. Klasa 1 | ADR 2025, 2.2.1.1.5 (podklasa 1.1) |
| `ADR-B-0317` | Przy rozpoznawaniu materiału promieniotwórczego klasy 7 w ADR, co należy sprawdzić zgodnie z definicją w 2.2.7.1.1? | § 2. Klasa 1 | ADR 2025, 2.2.7.1.1 oraz 2.2.7.2.2.1–2.2.7.2.2.6 |
| `ADR-B-0495` | Przesyłka klasy 1 ma podklasę 1.2. Jakie zagrożenie odróżnia ją od podklasy 1.1? | § 2. Klasa 1 | ADR 2025, 2.2.1.1.5, podklasa 1.2 |
| `ADR-B-0496` | Materiał wybuchowy klasy 1 ma podklasę 1.3. Które połączenie zagrożeń odpowiada ADR? | § 2. Klasa 1 | ADR 2025, 2.2.1.1.5, podklasa 1.3 |
| `ADR-B-0497` | Podklasa 1.5 obejmuje bardzo mało wrażliwe materiały wybuchowe. Czy brak wrażliwości oznacza brak zagrożenia wybuchem masowym? | § 2. Klasa 1 | ADR 2025, 2.2.1.1.5, podklasa 1.5 |
| `ADR-B-0498` | Podklasa 1.6 dotyczy skrajnie mało wrażliwych przedmiotów wybuchowych. Jakie zagrożenie masowe określa definicja? | § 2. Klasa 1 | ADR 2025, 2.2.1.1.5, podklasa 1.6 |
| `ADR-B-0499` | Bateria sodowo-jonowa z elektrolitem organicznym została umieszczona w urządzeniu, a inna identyczna bateria przewożona jest osobno. Które rozróżnienie UN wskazuje ADR 2025? | § 4. Baterie sodowo-jonowe | ADR 2025, 2.2.9.1.7.2; 2.2.9.3 UN 3551, 3552 |
| `ADR-B-0500` | Producent ma nowy typ baterii sodowo-jonowej objętej 2.2.9.1.7.2. Czy wystarczy, że jej ogniwa spełniają badania 38.3, a typ całej baterii nie został poddany wymaganym badaniom? | § 4. Baterie sodowo-jonowe | ADR 2025, 2.2.9.1.7.2(a) i uwaga |
| `ADR-B-0501` | Nowy projekt ogniwa sodowo-jonowego przewidziany do wpisu UN 3551 nie zapobiega zewnętrznemu zwarciu. Którego warunku 2.2.9.1.7.2 nie spełnia? | § 4. Baterie sodowo-jonowe | ADR 2025, 2.2.9.1.7.2(c) |
| `ADR-B-0502` | Bateria sodowo-jonowa z równolegle połączonymi ogniwami nie ma rozwiązania chroniącego przed niebezpiecznym przepływem wstecznym prądu. Czy spełnia 2.2.9.1.7.2? | § 4. Baterie sodowo-jonowe | ADR 2025, 2.2.9.1.7.2(d) |
| `ADR-B-0510` | Kierowca przed rozładunkiem dostrzega mokre opakowanie z nalepką klasy 4.3. Pracownik proponuje polewać je wodą, żeby usunąć zabrudzenia. Jakie zagrożenie należy uwzględnić? | § 2 i § 4. Klasy ADR oraz rozpoznawanie nalepek | ADR 2025, 2.2.43.1.1 |
| `ADR-B-0541` | Na pokazanym schemacie nalepki ADR kierowca widzi zielony romb, symbol butli i cyfrę 2. Który rodzaj zagrożenia przedstawia wzór nalepki 2.2? | § 4. Nalepki i oznakowanie | ADR 2025, 5.2.2.2.2; 2.2.2.1.2 |
| `ADR-B-0542` | Na autorskim schemacie nalepki widoczny jest czerwony romb z białym płomieniem i cyfrą 3. Jaką klasę towarów niebezpiecznych reprezentuje ten wzór? | § 4. Nalepki i oznakowanie | ADR 2025, 5.2.2.2.2; 2.2.3.1.1 |

### Uzupełnienia w lekcji B-02
- Klasa 1: dodano proste rozróżnienie podklas 1.1, 1.2, 1.3, 1.5 i 1.6; podkreślono, że niska wrażliwość nie oznacza braku zagrożenia.
- Tabela A: uzupełniono lokalizację numeru UN, nazwy, klasy, grupy pakowania, nalepek, limitu LQ, kodu EQ, kodu tunelowego i informacji o nadzorze.
- Nalepki: dopisano rolę zagrożenia dodatkowego, znaczenie wzorów 2.3 i 6.1 oraz odrębność nalepki 9A.
- Baterie sodowo-jonowe: dopisano UN 3551/3552 i warunki dotyczące badań typu oraz ochrony przed zwarciem, z zastrzeżeniem sprawdzenia konkretnego wpisu ADR.
- Klasa 7: podkreślono, że podstawowe rozpoznanie nie zastępuje wymagań szkoleniowych i przepisów szczególnych.

### Poprawki merytoryczne w banku
Nie znaleziono potwierdzonej sprzeczności wymagającej zmiany pytania, klucza lub explanation. Nie zmieniono banku ani statusów.

## ADR-B-03 — 49 pytań

| ID pytania | Wymagana wiedza / pytanie | Fragment lekcji | Odniesienie źródłowe |
|---|---|---|---|
| `ADR-B-0007` | Jaki symbol znajduje się na znaku dla materiałów zagrażających środowisku? | § 1. Znak środowiskowy | ADR 2025, 5.2.1.8 |
| `ADR-B-0008` | W dokumencie przewozowym ADR dla odpadu niebezpiecznego niebędącego odpadem promieniotwórczym dodano słowo „ODPAD” przed prawidłową nazwą przewozową. Co to oznacza? | § 3. Dokument przewozowy odpadu | ADR 2025, 5.4.1.1.3.1 |
| `ADR-B-0009` | Podczas rozładunku sztuk przesyłek ADR stwierdzono, że zawartość jednego opakowania wyciekła i zabrudziła pojazd. Co należy zrobić przed ponownym załadunkiem? | § 2. Wyciek i oczyszczenie | ADR 2025, 7.5.8.1 |
| `ADR-B-0045` | Jak postąpić ze znakiem dla materiału zagrażającego środowisku na sztuce przesyłki, gdy przepisy ADR wymagają takiego znaku? | § 1. Znak środowiskowy | ADR 2025, 5.2.1.8 |
| `ADR-B-0046` | Czy przy przewozie odpadów niebezpiecznych słowo „ODPAD” zastępuje numer UN w dokumencie ADR? | § 3. Dokument przewozowy odpadu | ADR 2025, 5.4.1.1.1 (a); 5.4.1.1.3.1 |
| `ADR-B-0100` | Po awarii z opakowania wypływa ciecz niebezpieczna w kierunku kratki kanalizacyjnej. Kiedy załoga może próbować zapobiec jej wpłynięciu do kanalizacji? | § 1–2. Środowisko i reakcja na wyciek | ADR 2025, 5.4.3.4 |
| `ADR-B-0101` | Zauważasz kałużę nieznanej substancji po uszkodzeniu opakowania ADR. Jak powinien zachować się kierowca? | § 1–2. Środowisko i reakcja na wyciek | ADR 2025, 5.4.3.4 |
| `ADR-B-0129` | Nadawca nie zna dokładnego składu odpadu bez nieproporcjonalnych kosztów. Czy może zawsze nadać grupę pakowania III? | § 3. Odpady i szczególne reguły klasyfikacji | ADR 2025, 2.1.3.5.5 |
| `ADR-B-0163` | Wycieka towar niebezpieczny, a kierowca ma wymagane wyposażenie do osłonięcia odpływu. Kiedy może spróbować osłonić kratkę kanalizacyjną? | § 1–2. Środowisko i reakcja na wyciek | ADR 2025, 5.4.3.4 |
| `ADR-B-0177` | Po rozładunku ADR w skrzyni ładunkowej wykryto pozostałości wycieku. Na miejscu nie ma możliwości bezpiecznego czyszczenia. Co przewiduje ADR 7.5.8.1? | § 2. Wyciek i oczyszczenie | ADR 2025, 7.5.8.1 |
| `ADR-B-0178` | Podczas awarii opakowania ADR kierowca zauważa pary unoszące się przy drzwiach ładowni. Jak ograniczyć ryzyko skażenia? | § 1–2. Środowisko i reakcja na wyciek | ADR 2025, 5.4.3.4 |
| `ADR-B-0179` | Do przewozu zgłoszono odpad ADR. Nadawca chce w dokumencie przewozowym podać samo słowo „ODPAD”, bez identyfikacji materiału. Co jest prawidłowe? | § 3. Dokument przewozowy odpadu | ADR 2025, 5.4.1.1.1; 5.4.1.1.3.1 |
| `ADR-B-0241` | Po rozładunku pusty, nieoczyszczony kontener ADR jedzie zgodnie z 7.5.8.1 do najbliższego odpowiedniego miejsca czyszczenia. Jaka dodatkowa informacja jest wymagana w dokumencie przewozowym? | § 3. Dokument przewozowy odpadu | ADR 2025, 5.4.1.1.6.3(b); 7.5.8.1 |
| `ADR-B-0242` | Po wycieku ADR substancja zbliża się do kanalizacji. Kiedy załoga może próbować ograniczyć jej odpływ? | § 1–2. Środowisko i reakcja na wyciek | ADR 2025, 5.4.3.4 |
| `ADR-B-0276` | Na sztuce przesyłki ADR widnieje znak rombu z czarną sylwetką martwej ryby i drzewa na jasnym tle. Co on oznacza? | § 1. Znak środowiskowy | ADR 2025, 5.2.1.8.3 |
| `ADR-B-0294` | Przewożony jest odpad zawierający towary niebezpieczne (inny niż odpad promieniotwórczy). Co należy zrobić z prawidłową nazwą przewozową w dokumencie, jeśli słowo „ODPAD” nie jest już jej częścią? | § 3. Dokument przewozowy odpadu | ADR 2025, 5.4.1.1.3.1 |
| `ADR-B-0295` | Po uszkodzeniu opakowania ADR na drodze pojawił się rozlew i opary. Jak powinien zachować się nieprzeszkolony członek załogi? | § 1–2. Środowisko i reakcja na wyciek | ADR 2025, 5.4.3.4 |
| `ADR-B-0318` | Odpadu przewożonego jako towar niebezpieczny nie da się dokładnie opisać pod względem składu. Co dopuszcza ADR 2.1.3.5.5 przy jego klasyfikacji, jeśli spełniono warunki tego przepisu? | § 3. Odpady i szczególne reguły klasyfikacji | ADR 2025, 2.1.3.5.5 |
| `ADR-B-0325` | Z powodu nieznanego składu odpadu nadawca ma wątpliwości co do poziomu zagrożenia. Którą zasadę stosuje w ramach ADR 2.1.3.5.5? | § 3. Odpady i szczególne reguły klasyfikacji | ADR 2025, 2.1.3.5.5 |
| `ADR-B-0326` | Odpad o nieznanym dokładnie składzie zawiera substancję klasy 4.3. Czy wolno zastosować uproszczoną procedurę ADR 2.1.3.5.5? | § 3. Odpady i szczególne reguły klasyfikacji | ADR 2025, 2.1.3.5.5 |
| `ADR-B-0327` | Nadawca chce sklasyfikować nieznany dokładnie odpad jako UN 3077 lub 3082 w grupie III. Kiedy dopuszcza to ADR 2.1.3.5.5? | § 3. Odpady i szczególne reguły klasyfikacji | ADR 2025, 2.1.3.5.5 |
| `ADR-B-0328` | W odpadzie o nieustalonym dokładnie składzie można wykazać, że jego właściwości nie odpowiadają poziomowi grupy pakowania I. Jakie domyślne rozwiązanie dopuszcza ADR 2.1.3.5.5 przy spełnieniu pozostałych warunków? | § 3. Odpady i szczególne reguły klasyfikacji | ADR 2025, 2.1.3.5.5 |
| `ADR-B-0329` | Odpad ma nieznany dokładnie skład, ale wiadomo, że zawiera materiał zakazany do przewozu według przepisów klasyfikacyjnych. Czy 2.1.3.5.5 pozwala nadać mu dowolny numer UN? | § 3. Odpady i szczególne reguły klasyfikacji | ADR 2025, 2.1.3.5.5 |
| `ADR-B-0330` | Nieznany dokładnie odpad zawiera materiał należący do klasy 5.2. Co z procedurą 2.1.3.5.5? | § 3. Odpady i szczególne reguły klasyfikacji | ADR 2025, 2.1.3.5.3; 2.1.3.5.5 |
| `ADR-B-0331` | Dokładna analiza mieszaniny nie jest możliwa bez nieproporcjonalnych kosztów lub wysiłku. Co przewiduje ADR 2.1.3.5.2? | § 3. Odpady i szczególne reguły klasyfikacji | ADR 2025, 2.1.3.5.2 |
| `ADR-B-0332` | W mieszaninie występują różne zagrożenia, a jedno z nich dotyczy substancji klasy 2. Jaki przepis określa szczególną kolejność pierwszeństwa? | § 3. Odpady i szczególne reguły klasyfikacji | ADR 2025, 2.1.3.5.3 |
| `ADR-B-0333` | Dla mieszaniny zagrożenia należą do klas niewymienionych w szczególnej liście ADR 2.1.3.5.3. Co wskazuje ADR 2.1.3.5.4? | § 3. Odpady i szczególne reguły klasyfikacji | ADR 2025, 2.1.3.5.4 |
| `ADR-B-0334` | Dla określonego odpadu możliwa jest zarówno ogólna pozycja i.n.o., jak i bardziej szczegółowa właściwa pozycja zbiorcza. Co nakazuje ADR 2.1.3.6? | § 3. Odpady i szczególne reguły klasyfikacji | ADR 2025, 2.1.3.6 |
| `ADR-B-0335` | Nadawca zna fizykochemiczne właściwości składników odpadu, ale nie pełne proporcje. Które dane może wykorzystać w ramach 2.1.3.5.5? | § 3. Odpady i szczególne reguły klasyfikacji | ADR 2025, 2.1.3.5.5 |
| `ADR-B-0336` | Kto jest wskazany w ADR 2.1.3.5.5 jako podmiot, którego wiedza może stanowić podstawę przypisania odpadu do UN i grupy pakowania? | § 3. Odpady i szczególne reguły klasyfikacji | ADR 2025, 2.1.3.5.5 |
| `ADR-B-0337` | Nieznany dokładnie odpad zawiera materiały zakaźne klasy 6.2. Czy procedura 2.1.3.5.5 obejmuje taki odpad? | § 3. Odpady i szczególne reguły klasyfikacji | ADR 2025, 2.1.3.5.3; 2.1.3.5.5 |
| `ADR-B-0338` | Odpad o nieznanym dokładnie składzie zawiera materiał samozapalny klasy 4.2 o właściwościach piroforycznych. Jak traktować procedurę 2.1.3.5.5? | § 3. Odpady i szczególne reguły klasyfikacji | ADR 2025, 2.1.3.5.3; 2.1.3.5.5 |
| `ADR-B-0339` | Podczas klasyfikacji odpadu z nieznanym dokładnie składem ktoś proponuje skorzystać z 2.1.3.5.5 mimo występowania materiałów wybuchowych klasy 1. Co jest prawidłowe? | § 3. Odpady i szczególne reguły klasyfikacji | ADR 2025, 2.1.3.5.3; 2.1.3.5.5 |
| `ADR-B-0340` | Występujące w mieszaninie zagrożenie spełnia warunki substancji samoreaktywnej klasy 4.1. Czy można zignorować specjalne pierwszeństwo z 2.1.3.5.3? | § 3. Odpady i szczególne reguły klasyfikacji | ADR 2025, 2.1.3.5.3 |
| `ADR-B-0341` | Kto ma prawo samodzielnie zastąpić klasyfikację ADR odpadu przypadkowym numerem UN z innego towaru? | § 3. Odpady i szczególne reguły klasyfikacji | ADR 2025, 2.1.3.5.5 |
| `ADR-B-0342` | W odpadzie występuje ryzyko klasy 7 i inne zagrożenie, a rozpatrywana sytuacja nie podlega wyjątkom z 2.1.3.5.3(a). Która odpowiedź oddaje zasadę pierwszeństwa? | § 3. Odpady i szczególne reguły klasyfikacji | ADR 2025, 2.1.3.5.3(a) |
| `ADR-B-0343` | Czy dla odpadu o nieznanym dokładnie składzie samo zakwalifikowanie jako odpadu usuwa konieczność ustalenia właściwej grupy pakowania? | § 3. Odpady i szczególne reguły klasyfikacji | ADR 2025, 2.1.3.5.5 |
| `ADR-B-0344` | Przy klasyfikacji odpadu rozważana jest ogólna pozycja i.n.o., choć dostępna jest odpowiednia pozycja specyficzna i.n.o. Co wynika z ADR 2.1.3.6? | § 3. Odpady i szczególne reguły klasyfikacji | ADR 2025, 2.1.3.6 |
| `ADR-B-0461` | Pojedyncze opakowanie zawiera 4 litry cieczy spełniającej kryteria zagrożenia dla środowiska wodnego. Kiedy może działać wyjątek od znaku środowiskowego? | § 1. Znak środowiskowy | ADR 2025, 5.2.1.8.1 |
| `ADR-B-0462` | Opakowanie kombinowane ma butelki wewnętrzne z materiałem niebezpiecznym dla środowiska, każda zawiera 6 litrów. Czy sam fakt użycia opakowania kombinowanego uruchamia wyjątek 5.2.1.8.1? | § 1. Znak środowiskowy | ADR 2025, 5.2.1.8.1 |
| `ADR-B-0463` | W opakowaniu pojedynczym przewozi się dokładnie 5 kg netto stałego materiału zagrażającego środowisku wodnemu. Jak rozumieć ilościowy warunek wyjątku od znaku? | § 1. Znak środowiskowy | ADR 2025, 5.2.1.8.1 |
| `ADR-B-0464` | Na sztuce przesyłki wymagany jest znak materiału niebezpiecznego dla środowiska. Gdzie powinien być umieszczony względem oznaczenia numeru UN? | § 1. Znak środowiskowy | ADR 2025, 5.2.1.8.2 |
| `ADR-B-0465` | Materiał klasy 3 spełnia także kryteria zagrożenia dla środowiska, a wyjątki 5.2.1.8.1 nie mają zastosowania. Który dodatkowy wpis zwykle należy zamieścić w dokumencie ADR? | § 3. Dokument przewozowy odpadu | ADR 2025, 5.4.1.1.18 |
| `ADR-B-0466` | Towar ma numer UN 3077 i spełnia kryteria zagrożenia środowiskowego. Czy 5.4.1.1.18 wymaga dla niego dodatkowego wpisu ENVIRONMENTALLY HAZARDOUS? | § 3. Dokument przewozowy odpadu | ADR 2025, 5.4.1.1.18 |
| `ADR-B-0467` | W morsko-drogowym łańcuchu przewozu dokument dla materiału niebezpiecznego dla środowiska zawiera określenie MARINE POLLUTANT. Jak ocenić je w zakresie 5.4.1.1.18? | § 3. Dokument przewozowy odpadu | ADR 2025, 5.4.1.1.18 |
| `ADR-B-0468` | Pojazd wymaga nalepek wielkiego formatu i przewozi towary zagrażające środowisku wodnemu. Kiedy znak środowiskowy według 5.3.6 może być dodatkowo wymagany na jednostce? | § 1. Znak środowiskowy | ADR 2025, 5.3.6.1 |
| `ADR-B-0469` | Jaki standardowy minimalny wymiar znaku środowiskowego przewiduje ADR 5.3.6.2 dla oznakowania kontenera, bez zastosowania szczególnego zmniejszenia wymiarów? | § 1. Znak środowiskowy | ADR 2025, 5.3.6.2 |
| `ADR-B-0470` | Kontener-cysterna ma pojemność 2500 l i niewystarczającą powierzchnię na standardowy znak środowiskowy. Co dopuszcza 5.3.6.2? | § 1. Znak środowiskowy | ADR 2025, 5.3.6.2 |
| `ADR-B-0514` | Po rozładunku ADR załadowca odkrywa, że z jednej sztuki przesyłki wyciekła niebezpieczna ciecz na podłogę kontenera. Planowany jest kolejny załadunek. Kiedy kontener może zostać ponownie załadowany? | § 2. Wyciek i oczyszczenie | ADR 2025, 7.5.8.1 |

### Uzupełnienia w lekcji B-03
- Znak środowiskowy: dodano warunkowość wyjątków ilościowych, różnice zależne od opakowania, umiejscowienie znaku oraz odrębne wymagania dla jednostek transportowych.
- Dokumentacja: dodano wpis „ENVIRONMENTALLY HAZARDOUS”, warunki związane z „MARINE POLLUTANT” oraz ostrzeżenie, że znak na opakowaniu, nalepka klasy i wpis w dokumencie nie są zamiennikami.
- Odpady: rozszerzono granice uproszczonej klasyfikacji nieznanego składu, wyjątki i pierwszeństwo klasyfikacji, stosowanie reguł dla mieszanin oraz wybór pozycji bardziej szczegółowej zamiast ogólnej i.n.o.
- Pusty nieoczyszczony kontener/opakowanie: dodano potrzebę sprawdzenia wpisu dokumentu przy przewozie do miejsca czyszczenia.

### Poprawki merytoryczne w banku
Nie znaleziono potwierdzonej sprzeczności wymagającej zmiany pytania, klucza lub explanation. Nie zmieniono banku ani statusów.

## ADR-B-04 — 46 pytań

| ID pytania | Wymagana wiedza / pytanie | Fragment lekcji | Odniesienie źródłowe |
|---|---|---|---|
| `ADR-B-0010` | Czy podczas czynności ładunkowych ADR wolno palić e-papierosa w pobliżu pojazdu? | § 1. Zakazy załogi, pojazd i kontrola przed załadunkiem | ADR 2025, 8.3.5 |
| `ADR-B-0011` | Czy kierowca może samowolnie otworzyć sztukę przesyłki zawierającą towar niebezpieczny? | § 1. Zakazy załogi, pojazd i kontrola przed załadunkiem | ADR 2025, 8.3.3 |
| `ADR-B-0012` | Co do zasady należy zrobić z silnikiem podczas załadunku lub rozładunku towarów niebezpiecznych? | § 1. Zakazy załogi, pojazd i kontrola przed załadunkiem | ADR 2025, 8.3.6 |
| `ADR-B-0047` | Co kierowca powinien zrobić z silnikiem podczas załadunku ADR, jeżeli nie jest potrzebny do napędzania urządzeń? | § 1. Zakazy załogi, pojazd i kontrola przed załadunkiem | ADR 2025, 8.3.6 |
| `ADR-B-0048` | Jak powinna postąpić załoga w sprawie otwierania sztuk przesyłek zawierających towary niebezpieczne podczas przewozu objętego ADR 8.3.3? | § 1. Zakazy załogi, pojazd i kontrola przed załadunkiem | ADR 2025, 8.3.3 |
| `ADR-B-0102` | Podczas awarii wyczuwalny jest zapach oparów palnego towaru. Jak postępować z możliwymi źródłami zapłonu? | § 2. Rozlew, opary i instrukcje | ADR 2025, 5.4.3.4 |
| `ADR-B-0103` | Podczas rozładunku ADR drugi członek załogi zaczyna korzystać z e-papierosa. Co należy zrobić? | § 1. Zakazy załogi, pojazd i kontrola przed załadunkiem | ADR 2025, 8.3.5 |
| `ADR-B-0130` | Po uszkodzeniu opakowania ADR na jezdni jest rozlew nieznanej cieczy. Co ogranicza narażenie kierowcy? | § 2. Rozlew, opary i instrukcje | ADR 2025, 5.4.3.4 |
| `ADR-B-0131` | Kiedy szczególne wymagania nadzoru pojazdu z 8.4 ADR mają zastosowanie? | § 3. Postój i nadzór | ADR 2025, 8.4.1; 8.5; 3.2 tabela A kol. (19) |
| `ADR-B-0164` | Po awarii materiału ADR wyczuwalne są palne opary. Dlaczego nie należy używać e-papierosa w pobliżu wycieku? | § 2. Rozlew, opary i instrukcje | ADR 2025, 5.4.3.4 |
| `ADR-B-0180` | Po kolizji opakowanie z materiałem żrącym pękło. Nie ma pewności, czy rękawice kierowcy chronią przed tym materiałem. Co należy zrobić? | § 2. Rozlew, opary i instrukcje | ADR 2025, 5.4.3.4 |
| `ADR-B-0181` | W przewozie objętym wymaganiami 8.4 ADR kierowca nie znajduje chronionego depozytu ani właściwego terenu zakładu. Co powinien zrobić? | § 3. Postój i nadzór | ADR 2025, 8.4.1 |
| `ADR-B-0243` | Czy członek załogi ADR może otworzyć sztukę przesyłki z towarem niebezpiecznym podczas przewozu? | § 1. Zakazy załogi, pojazd i kontrola przed załadunkiem | ADR 2025, 8.3.3 |
| `ADR-B-0244` | Podczas załadunku ADR silnik pojazdu pracuje, chociaż nie napędza żadnego urządzenia. Co należy zrobić? | § 1. Zakazy załogi, pojazd i kontrola przed załadunkiem | ADR 2025, 8.3.6 |
| `ADR-B-0279` | Podczas załadunku ADR pracownik korzysta z papierosa elektronicznego obok pojazdu. Czy jest to zgodne z ADR? | § 1. Zakazy załogi, pojazd i kontrola przed załadunkiem | ADR 2025, 8.3.5 |
| `ADR-B-0280` | Podczas rozładunku ADR kierowca widzi osobę palącą wewnątrz pojazdu. Jak ocenia to ADR 8.3.5? | § 1. Zakazy załogi, pojazd i kontrola przed załadunkiem | ADR 2025, 8.3.5 |
| `ADR-B-0296` | Podczas awarii ADR kierowca chce sprawdzić ładunek, używając papierosa elektronicznego i przełączając urządzenia elektryczne. Co powinien zrobić? | § 2. Rozlew, opary i instrukcje | ADR 2025, 5.4.3.4 |
| `ADR-B-0297` | Po kolizji pojazdu ADR w pobliżu zbiera się tłum, a na drodze są opary. Co załoga powinna zrobić, jeżeli można to zrobić bezpiecznie? | § 2. Rozlew, opary i instrukcje | ADR 2025, 5.4.3.4 |
| `ADR-B-0310` | Towary i ich ilości powodują zastosowanie nadzoru nad pojazdem z ADR 8.4.1. Gdzie w pierwszej kolejności można bez dozoru zaparkować pojazd? | § 3. Postój i nadzór | ADR 2025, 8.4.1 |
| `ADR-B-0345` | Pojazd ADR objęty 8.4.1 stoi bez dozoru na ogólnodostępnym parkingu, choć dostępny jest bezpieczny teren zakładu. Co jest właściwe? | § 3. Postój i nadzór | ADR 2025, 8.4.1 |
| `ADR-B-0346` | Nie ma zabezpieczonej bazy ani terenu zakładu. Dostępny jest parking dozorowany przez obsługę. Jaki dodatkowy warunek dotyczy osoby dozorującej? | § 3. Postój i nadzór | ADR 2025, 8.4.1(a) |
| `ADR-B-0347` | Przy przewozie wymagającym nadzoru 8.4.1 dostępny jest parking z dozorcą spełniający wymogi lit. (a). Czy można zamiast niego wybrać zwykły parking z lit. (b)? | § 3. Postój i nadzór | ADR 2025, 8.4.1(a)–(b) |
| `ADR-B-0348` | W przewozie objętym 8.4.1 nie ma zabezpieczonej bazy, parkingu dozorowanego ani odpowiedniego parkingu publicznego. Gdzie można rozważyć postój? | § 3. Postój i nadzór | ADR 2025, 8.4.1(c) |
| `ADR-B-0349` | Który teren odpowiada warunkowi lit. (c) w 8.4.1, gdy wcześniejsze rodzaje parkingów nie są dostępne? | § 3. Postój i nadzór | ADR 2025, 8.4.1(c) |
| `ADR-B-0350` | Jak sprawdzić, czy dany przewóz podlega szczególnemu nadzorowi na podstawie 8.4.1? | § 3. Postój i nadzór | ADR 2025, 8.4.1; 3.2 tabela A kol. (19) |
| `ADR-B-0351` | Pojazd przewożący towary niebezpieczne zaparkowano na płaskim terenie. Jakie podstawowe zabezpieczenie postojowe wymaga ADR 8.3.7? | § 1. Zakazy załogi, pojazd i kontrola przed załadunkiem | ADR 2025, 8.3.7 |
| `ADR-B-0352` | Przyczepa przewożąca towary niebezpieczne nie ma własnego urządzenia hamującego. Co wymaga ADR 8.3.7 podczas postoju? | § 1. Zakazy załogi, pojazd i kontrola przed załadunkiem | ADR 2025, 8.3.7; 8.1.5.2 |
| `ADR-B-0353` | Na parkingu kierowca pojazdu ADR chce użyć przenośnej lampy, której metalowa część może wytwarzać iskry. Co stanowi ADR 8.3.4? | § 1. Zakazy załogi, pojazd i kontrola przed załadunkiem | ADR 2025, 8.3.4 |
| `ADR-B-0354` | Podczas awarii towary niebezpieczne rozlały się obok pojazdu. Kierowca chce wejść w kałużę, aby odczytać etykietę. Co wskazuje instrukcja pisemna? | § 2. Rozlew, opary i instrukcje | ADR 2025, 5.4.3.4 |
| `ADR-B-0355` | W czasie wypadku przy ładunku ADR gromadzą się opary. Gdzie w miarę możliwości powinna przebywać załoga? | § 2. Rozlew, opary i instrukcje | ADR 2025, 5.4.3.4 |
| `ADR-B-0356` | Po kontakcie z wyciekiem ADR część odzieży została skażona. Jakie działanie przewiduje instrukcja pisemna? | § 2. Rozlew, opary i instrukcje | ADR 2025, 5.4.3.4 |
| `ADR-B-0357` | Kierowca chce otworzyć opakowanie ADR, aby sprawdzić, czy nie pojawił się wyciek. Co przewiduje 8.3.3? | § 1. Zakazy załogi, pojazd i kontrola przed załadunkiem | ADR 2025, 8.3.3 |
| `ADR-B-0358` | W czasie rozładunku pompa musi pracować z napędu silnika pojazdu. Kiedy może on pozostać włączony? | § 1. Zakazy załogi, pojazd i kontrola przed załadunkiem | ADR 2025, 8.3.6 |
| `ADR-B-0359` | Przy załadunku ADR silnik pozostaje włączony tylko dla klimatyzacji, nie napędza urządzeń przeładunkowych. Jak postąpić? | § 1. Zakazy załogi, pojazd i kontrola przed załadunkiem | ADR 2025, 8.3.6 |
| `ADR-B-0360` | Podczas przeładunku ADR ktoś pali poza kabiną, lecz bezpośrednio przy pojeździe. Jak należy ocenić sytuację? | § 1. Zakazy załogi, pojazd i kontrola przed załadunkiem | ADR 2025, 8.3.5 |
| `ADR-B-0361` | Po awarii kierowca rozważa włączenie urządzenia elektrycznego w pobliżu palnych oparów. Co nakazuje instrukcja pisemna ADR? | § 2. Rozlew, opary i instrukcje | ADR 2025, 5.4.3.4 |
| `ADR-B-0362` | Po wypadku jednostki ADR na miejscu pojawia się służba ratownicza. Co załoga powinna mieć łatwo dostępne dla ratowników? | § 2. Rozlew, opary i instrukcje | ADR 2025, 5.4.3.4 |
| `ADR-B-0471` | Przewóz towarów niebezpiecznych objęty ADR odbywa się ciężarówką; znajomy kierowcy chce jechać na wolnym fotelu, nie będąc członkiem załogi. Czy jest to dozwolone? | § 1. Zakazy załogi, pojazd i kontrola przed załadunkiem | ADR 2025, 8.3.1 |
| `ADR-B-0472` | W pojeździe ADR załoga ma gaśnicę zgodną z wymaganiami, ale nie wie, jak jej użyć. Czego dodatkowo wymaga ADR? | § 1. Zakazy załogi, pojazd i kontrola przed załadunkiem | ADR 2025, 8.3.2 |
| `ADR-B-0473` | Pojazd ADR z układem ABS ciągnie przyczepę o maksymalnej masie ponad 3,5 t. Co 8.3.8 wymaga od połączeń elektrycznych, o których mowa w 9.2.2.6, podczas przewozu? | § 1. Zakazy załogi, pojazd i kontrola przed załadunkiem | ADR 2025, 8.3.8 |
| `ADR-B-0474` | Przed załadunkiem ADR kontrola dokumentów ujawnia niespełnienie wymagań przez kierowcę lub pojazd. Jak należy postąpić w ramach 7.5.1.2? | § 1. Zakazy załogi, pojazd i kontrola przed załadunkiem | ADR 2025, 7.5.1.2 |
| `ADR-B-0475` | Przed załadunkiem kontenera pojawia się uszkodzenie jego ściany mogące naruszyć ochronę opakowań. Jak stosuje się 7.5.1.2? | § 1. Zakazy załogi, pojazd i kontrola przed załadunkiem | ADR 2025, 7.5.1.2 |
| `ADR-B-0476` | Podczas rozładunku ADR wykryto uszkodzone wyposażenie pojazdu sprzeczne z wymaganiami. Jaką zasadę 7.5.1.3 należy rozważyć? | § 1. Zakazy załogi, pojazd i kontrola przed załadunkiem | ADR 2025, 7.5.1.3 |
| `ADR-B-0515` | W trakcie rozładunku sztuk przesyłek ADR pracownik prosi kierowcę o pozostawienie uruchomionego silnika dla ogrzania kabiny. Silnik nie napędza urządzenia rozładunkowego. Jak postąpić? | § 1. Zakazy załogi, pojazd i kontrola przed załadunkiem | ADR 2025, 8.3.6 |
| `ADR-B-0580` | Przy danym przewozie mają zastosowanie wymagania ADR dotyczące nadzoru i postoju. Kierowca planuje przerwę. Co powinien zrobić? | § 3. Postój i nadzór | ADR 2025, 8.4; 8.5 |
| `ADR-B-0581` | Dyspozytor proponuje pozostawienie pojazdu bez nadzoru na zwykłym parkingu, mimo że dla tego przewozu stosuje się ADR 8.4. Jak postąpić? | § 3. Postój i nadzór | ADR 2025, 8.4; 8.5 |

### Uzupełnienia w lekcji B-04
- Załoga i pojazd: dopisano zakaz przewozu pasażerów niebędących członkami załogi, umiejętność użycia gaśnic, wymagania wobec przenośnych lamp i połączeń elektrycznych w określonym zestawie z ABS.
- Kontrola załadunku/rozładunku: dodano zasadę wstrzymania czynności przy niezgodności pojazdu, wyposażenia lub dokumentów, z odwołaniem do ADR 7.5.1.2–7.5.1.3.
- Postój: rozpisano kolejność alternatyw ADR 8.4.1, warunki osoby dozorującej, wymagania dla miejsca odosobnionego oraz rozdzielenie nadzoru od hamulca postojowego i klina.

### Poprawki merytoryczne w banku
Nie znaleziono potwierdzonej sprzeczności wymagającej zmiany pytania, klucza lub explanation. Nie zmieniono banku ani statusów.

## Quality Gate — dane banku przed i po tej partii

- Liczba pytań: 609; liczba ID unikalnych: 609.
- Statusy: 609 `needs_review`, 0 `verified`.
- Poprawna odpowiedź jest jedyną najdłuższą: 86/609 = 14.12% (limit 18%).
- Najkrótsze explanation: 300 znaków; explanation krótsze niż 200 znaków: 0.
- Wyjaśnienia poza zakresem 2–5 zdań: 0. Wymóg CI ma pozostać PASS; ten audyt nie modyfikuje explanation.
- Zmiany dotyczą wyłącznie lekcji i raportu. Bank, klucze odpowiedzi, ID oraz statusy nie zostały zmienione.

## Granice audytu

Pokrycie treści sprawdzono na podstawie pytań i wskazanych źródeł ADR. Nie jest to niezależna opinia prawna ani formalna recenzja egzaminacyjna. Wszelkie szczegółowe wyjątki należy przed publikacją porównać z urzędowym ADR 2025, Dz.U. 2025 poz. 642 wraz ze sprostowaniem poz. 1575. Wszystkie pytania pozostają `needs_review`.
