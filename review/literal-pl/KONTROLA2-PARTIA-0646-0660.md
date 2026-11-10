# Kontrola druga – partia 44 (ADR-B-0646–0660)

Data: 10.11.2026 (Europe/Warsaw). Podstawa: main 17c58e8af (po scaleniu #919), bank blob `6dc2b850f70d300ef3c214708b3283933934301c`. Źródło prawa: Dz.U. 2025 poz. 642 (+ sprostowanie poz. 1575); strony według nagłówka „Dziennik Ustaw — NNN —”; tabele i wzory sprawdzone na obrazach stron (s. 517, 945, 976, 977).

## Wynik

- **OK 0 / POPRAW 15 / BLOKUJ 0** – werdykty POPRAW z #919 potwierdzone (wszystkie 15).
- 10 nowych elementów z tych samych kompetencji (0646–0652, 0655, 0656, 0660) i 5 przeredagowań z zachowaniem tematu (0653, 0654, 0657, 0658, 0659). Bez cystern. Litery kluczy, module_id, kompetencje i pole image bez zmian; wszystko `needs_review`; nic nie oznaczono jako verified; brak nowych pytań.
- Zamienników z #919 NIE przejęto (powody niżej).
- Nowy blob banku: `835ba93341ece797cd831d85defa4d147da0942e` (plik questions-b44-835ba933.jsonl).
- Licznik: po partii 44 pozostaje **120** pytań bez porównania dosłownego po obu kontrolach (0661–0780).

| ID | Kompetencja | Klucz | #919 | Kontrola 2 | Decyzja | Długości A/B/C |
|---|---|---|---|---|---|---|
| ADR-B-0646 | 05-K13 | B | POPRAW | POPRAW | NOWY ELEMENT (stare = 0651; organizacja kursu) | 80/75/66 |
| ADR-B-0647 | 05-K13 | A | POPRAW | POPRAW | NOWY ELEMENT (stare = 0015/0169, 8.1.4.5) | 75/79/68 |
| ADR-B-0648 | 05-K14 | C | POPRAW | POPRAW | NOWY ELEMENT (stare = 0113/0187/0626) | 75/62/73 |
| ADR-B-0649 | 05-K14 | A | POPRAW | POPRAW | NOWY ELEMENT (stare = 0110/0167/0745/0631) | 78/79/72 |
| ADR-B-0650 | 05-K15 | B | POPRAW | POPRAW | NOWY ELEMENT (stare = 0050/0590/0620/0716) | 75/73/70 |
| ADR-B-0651 | 05-K15 | C | POPRAW | POPRAW | NOWY ELEMENT (stare = 0646) | 78/71/75 |
| ADR-B-0652 | 02-K12 | A | POPRAW | POPRAW | NOWY ELEMENT (stare ≈ 0005/0161/0267/0730) | 72/64/80 |
| ADR-B-0653 | 06-K08 | A | POPRAW | POPRAW | PRZEREDAGOWANIE (temat 886 zachowany) | 62/67/61 |
| ADR-B-0654 | 06-K06 | A | POPRAW | POPRAW | PRZEREDAGOWANIE (temat 99 zachowany) | 68/78/67 |
| ADR-B-0655 | 02-K14 | C | POPRAW | POPRAW | NOWY ELEMENT (stare = 0127/0128/0610) | 78/65/78 |
| ADR-B-0656 | 01-K04 | A | POPRAW | POPRAW | NOWY ELEMENT (stare = lustro 0720/0091, 1.1.3.1 (c); treść podpowiadała warunki) | 72/79/69 |
| ADR-B-0657 | 02-K02 | A | POPRAW | POPRAW | PRZEREDAGOWANIE (temat 2.1 zachowany) | 70/75/66 |
| ADR-B-0658 | 02-K03 | A | POPRAW | POPRAW | PRZEREDAGOWANIE (temat zachowany) | 80/80/75 |
| ADR-B-0659 | 01-K01 | A | POPRAW | POPRAW | PRZEREDAGOWANIE (temat zachowany; podstawa „art. 2 Umowy ADR” zastąpiona) | 75/75/74 |
| ADR-B-0660 | 07-K07 | A | POPRAW | POPRAW | NOWY ELEMENT (stare = 0567–0569/0713/0758; podstawa niepełna) | 69/70/69 |

## Błędy w raporcie #919

1. **Wszystkie opcje wszystkich 15 zamienników mają średnik i kropkę na końcu** – a test #919 tego WYMAGA (`assertIn(";", option)`, `option.endswith(".")`), wbrew zasadom formy. Przy wdrożeniu te dwie asercje usuwamy.
2. **Zamienniki dublujące bank**: 0651 (4.2 – utrzymywać w stanie suchym) = 0361/0155; 0652 (korozja metali) = 0267; 0659 (jednostka transportowa) = 0147/0709.
3. **Zamienniki błędne lub nieprecyzyjne**: 0655 – twierdzi, że wielkość opakowania nigdy nie zmienia grupy w klasie 3 (błąd: 2.2.3.1.4, lepkie ciecze w III grupie przy opakowaniach ≤ 450 l); 0657 – mieszanina trująca i palna to grupa TF, nie „T” (2.2.2.1.3); 0650 – raport 1.8.5 to obowiązek przewoźnika/nadawcy, nie praktyczna czynność kierowcy (05-K15).
4. **exact_quote / gazette_pages opisują tematy zamienników, nie pytania pierwotne** (0650 s. 87 = 1.8.5.3; 0651 s. 977; 0654 – cytat 90; 0656 – cytat 1.1.3.1 (d), choć pytanie było o (c); 0657 – 2.2.2.1.3; 0658 – 2.2.3.1.1 bez definicji 1.2.1 s. 46).
5. Błędne odwołanie do duplikatu: 0657 „0095” – to pytanie o klasę 4.2.
6. Test #919: jedna stała `EXPECTED_BANK_SHA` dla manifestu i banku (wbrew poleceniu – dwie stałe); `counts` porównywane ze stałą EXPECTED_COUNTS, a nie przeliczane z rekordów.
7. Słusznie: wszystkie 15 POPRAW; 0646 = 0651; 0647 ≈ 0015; 0659 – podstawa „art. 2 Umowy ADR” spoza Dz.U. 2025 poz. 642; licznik 135 → 120; „Kodeks cywilny, Dz.U. 2026 poz. 795” – akt istnieje (t.j. KC, obwieszczenie Marszałka Sejmu z 27.05.2026, ogłoszone 17.06.2026; sprawdzone w ELI Sejmu).
8. Dodatkowo (0660): szkoda w przesyłce w przewozie krajowym podlega w pierwszej kolejności ustawie Prawo przewozowe (art. 65, t.j. Dz.U. 2024 poz. 1262; KC art. 775 – przepisy szczególne), więc sama podstawa KC 471/474 była niepełna. Nowe 0660 dotyczy przyczynienia się poszkodowanego (KC 362) w szkodzie poza umową przewozu. Ta sama uwaga dotyczy 0713 – do oceny specjalisty (prawnik).

## Szczegóły

### ADR-B-0646 (05-K13, klucz B) – NOWY ELEMENT (stare = 0651; organizacja kursu)

- #919: zgoda (= 0651, organizacja kursu); zamiennik (kolejność uruchomienia gaśnicy) – średniki, kropki.
- Nowa treść: Na ćwiczeniu kursant gasi gaśnicą proszkową małą tacę z płonącym olejem, która udaje początkowy pożar hamulca. Stoi z wiatrem w plecy w bezpiecznej odległości. Gdzie powinien kierować strumień proszku?
- Klucz: Na podstawę ognia, czyli na palący się materiał, omiatając ją z boku na bok
- Cytaty i strony Dz.U.: Wzór 5.4.3.4 (s. 975): „Jeżeli jest to właściwe i bezpieczne, użyć gaśnic w celu ugaszenia małego lub będącego w fazie początkowej pożaru, obejmującego opony, hamulce lub przedział silnika;”; 8.2.2.3.8 (s. 1328) – ćwiczenia praktyczne z gaszenia. PSP (KM PSP Szczecin, gov.pl, „Jak gasić gaśnicą?”): „omiataj podstawę ognia krótkimi, kontrolowanymi ruchami lewo–prawo”. Nowe: gdzie kierować strumień proszku – na podstawę ognia.
- Uwagi: Wzór s. 975; 8.2.2.3.8 s. 1328; zalecenia PSP (KM PSP Szczecin, gov.pl). Odrębne od 0640/0641 (plomba, strona nawietrzna) i 0015/0169 (mocowanie). Do oceny specjalisty (instruktor ochrony przeciwpożarowej).

### ADR-B-0647 (05-K13, klucz A) – NOWY ELEMENT (stare = 0015/0169, 8.1.4.5)

- #919: zgoda (= 0015/0169); zamiennik (pozycja pionowa gaśnicy, syfon) – średniki, kropki.
- Nowa treść: Kierowca ugasił gaśnicą mały, początkowy pożar hamulca naczepy. Płomieni już nie widać, ale bęben hamulcowy jest bardzo gorący i lekko dymi. Służby są już powiadomione. Co powinien teraz zrobić?
- Klucz: Zostać w bezpiecznej odległości z gaśnicą i obserwować, czy ogień nie wraca
- Cytaty i strony Dz.U.: Wzór 5.4.3.4 (s. 975): „Jeżeli jest to właściwe i bezpieczne, użyć gaśnic w celu ugaszenia małego lub będącego w fazie początkowej pożaru, obejmującego opony, hamulce lub przedział silnika;”; PSP: „Po ugaszeniu kontroluj miejsce – możliwa ponowna zapłonność”. Nowe: po ugaszeniu gorącego hamulca – dozór z gaśnicą, możliwy ponowny zapłon.
- Uwagi: Wzór s. 975; 8.2.2.3.8 s. 1328; zalecenia PSP (ponowny zapłon). Odrębne od 0493/0702/0742/0743 (przerwać gaszenie) i 0108/0184/0695. Do oceny specjalisty (instruktor ochrony przeciwpożarowej).

### ADR-B-0648 (05-K14, klucz C) – NOWY ELEMENT (stare = 0113/0187/0626)

- #919: zgoda; zamiennik (zadławienie) – temat słuszny, średniki, kropki; napisany od nowa.
- Nowa treść: Na postoju kolega kierowcy krztusi się kęsem kanapki. Nie może mówić, a jego kaszel stał się nieskuteczny. Miejsce jest bezpieczne. Co według wytycznych ERC 2025 trzeba zrobić najpierw?
- Klucz: Wykonać do 5 uderzeń między łopatki, a gdy nie pomogą, uciskać nadbrzusze
- Cytaty i strony Dz.U.: 8.2.2.3.2 (e) (s. 1327): „czynności, które należy podjąć po zaistnieniu wypadku (pierwsza pomoc, …)”; 8.2.2.3.8 (s. 1328). ERC Guidelines 2025 First Aid – zadławienie dorosłego: kaszel; do 5 uderzeń między łopatki; do 5 uciśnięć nadbrzusza; bez wymiatania palcem na ślepo; 112.
- Uwagi: 8.2.2.3.2 (e) s. 1327; 8.2.2.3.8 s. 1328; ERC Guidelines 2025 First Aid. Odrębne od 0642/0643/0715 (RKO, AED) i 0748 (pozycja boczna). Do oceny specjalisty (instruktor pierwszej pomocy).

### ADR-B-0649 (05-K14, klucz A) – NOWY ELEMENT (stare = 0110/0167/0745/0631)

- #919: zgoda; zamiennik (uraz szyi) – temat słuszny, średniki, kropki; napisany od nowa.
- Nowa treść: Po kolizji drogowej kierowca drugiego auta siedzi przytomny w fotelu i skarży się na ból karku. Miejsce jest bezpieczne, nic się nie pali ani nie wycieka. Co według wytycznych ERC 2025 trzeba zrobić?
- Klucz: Zachęcić go, by nie ruszał głową i trzymał szyję w wygodnej, stabilnej pozycji
- Cytaty i strony Dz.U.: 8.2.2.3.2 (e) (s. 1327); 8.2.2.3.8 (s. 1328). ERC Guidelines 2025 First Aid – cervical spinal motion restriction: wypadek drogowy → podejrzenie urazu; przytomny – ograniczyć ruchy szyi, zachęcić do utrzymania wygodnej, stabilnej pozycji; nie wymuszać zmiany pozycji.
- Uwagi: 8.2.2.3.2 (e) s. 1327; 8.2.2.3.8 s. 1328; ERC Guidelines 2025 First Aid. Odrębne od 0712 (krwotok), 0748 (pozycja boczna). Do oceny specjalisty (instruktor pierwszej pomocy).

### ADR-B-0650 (05-K15, klucz B) – NOWY ELEMENT (stare = 0050/0590/0620/0716)

- #919: zgoda; zamiennik (raport 1.8.5) – obowiązek przewoźnika, poza 05-K15; strona 87 dotyczy zamiennika, nie pytania.
- Nowa treść: Po kolizji z pękniętego kanistra z nalepką 8 wycieka ciecz. Pomocnik chce spłukać rozlew wodą z butelki, bo uważa, że żrąca ciecz grozi jedynie poparzeniem przy dotknięciu. Co podają instrukcje pisemne?
- Klucz: Że mogą gwałtownie reagować z wodą, a uwolnione mogą wydzielać żrące pary
- Cytaty i strony Dz.U.: Wzór 5.4.3.4, dodatkowe wskazówki (s. 977, obraz strony), nalepka 8 „Materiały żrące”: „Zagrożenie poparzeniem chemicznym. Mogą gwałtownie reagować ze sobą, z wodą lub z innymi materiałami. Uwolnione materiały mogą wydzielać żrące pary. Zagrożenie w przypadku przedostania się do środowiska wodnego lub kanalizacji.” Kolumna (3) pusta.
- Uwagi: Wzór s. 977 (obraz strony sprawdzony). Odrębne od 0050/0590/0620/0716 (sam znak i rodzaj zagrożenia klasy 8).

### ADR-B-0651 (05-K15, klucz C) – NOWY ELEMENT (stare = 0646)

- #919: zgoda (= 0646); zamiennik (4.2 – utrzymywać w stanie suchym) = 0361/0155.
- Nowa treść: Po kolizji z rozbitego kartonu z nalepką 6.2 wycieka płyn w stronę rowu z wodą, przy którym pasie się bydło. Kolega uważa, że materiał zakaźny grozi jedynie ludziom, którzy go dotkną. Co podają instrukcje pisemne?
- Klucz: Że grozi groźna choroba ludzi lub zwierząt oraz skażenie wody i kanalizacji
- Cytaty i strony Dz.U.: Wzór 5.4.3.4, dodatkowe wskazówki (s. 977, obraz strony), nalepka 6.2 „Materiały zakaźne”: „Zagrożenie zakażeniem. Może spowodować groźną chorobę u ludzi lub u zwierząt. Zagrożenie w przypadku przedostania się do środowiska wodnego lub kanalizacji.”
- Uwagi: Wzór s. 977 (obraz strony sprawdzony). Odrębne od rozpoznania nalepki 6.2 (klasa 6.2) i 0644/0645 (nalepki 2.2, 9).

### ADR-B-0652 (02-K12, klucz A) – NOWY ELEMENT (stare ≈ 0005/0161/0267/0730)

- #919: zgoda; zamiennik (korozja metali) = 0267.
- Nowa treść: Kierowca odbiera kanistry z UN 2797 CIECZ AKUMULATOROWA ZASADOWA. Magazynier twierdzi, że to zasada, a nie kwas, więc ADR nie traktuje jej jako materiału żrącego. Jak ADR klasyfikuje tę ciecz?
- Klucz: Jako materiał żrący klasy 8, bo ta klasa obejmuje też materiały zasadowe
- Cytaty i strony Dz.U.: 2.2.8.1.1 (s. 264) – definicja materiałów żrących; 2.2.8.1.4.1 (s. 264): „C1 - C4 Materiały kwaśne”, „C5 - C8 Materiały zasadowe”; tabela A (s. 517, obraz strony): UN 2796 – 8, C1, II; UN 2797 CIECZ AKUMULATOROWA ZASADOWA – 8, C5, II, nalepka 8.
- Uwagi: 2.2.8.1.1 i 2.2.8.1.4.1 s. 264; tabela A s. 517 (obraz strony). Odrębne od 0005/0161/0730 (definicja), 0267 (korozja metali), 0050 (nalepka 8).

### ADR-B-0653 (06-K08, klucz A) – PRZEREDAGOWANIE (temat 886 zachowany)

- #919: zgoda co do POPRAW; zamiennik X886 zbędny – temat 886 zachowany, poprawiona forma.
- Nowa treść: W górnym polu tablicy pomarańczowej jest numer 886. Ratownik pyta, czy to ten sam materiał co przy numerze 86, tylko przewożony w większej ilości. Co według 5.3.2.3.2 oznacza numer 886?
- Klucz: Materiał silnie żrący i trujący, bo cyfra 8 jest tu powtórzona
- Cytaty i strony Dz.U.: 5.3.2.3.1 (s. 956) – podwojenie cyfry = nasilenie; 5.3.2.3.2 (s. 959): „86 materiał żrący lub słabo żrący, trujący”, „886 materiał silnie żrący trujący”, „X886 materiał silnie żrący trujący, który reaguje niebezpiecznie z wodą”.
- Uwagi: 5.3.2.3.1 s. 956; 5.3.2.3.2 s. 959. Pokrewne 0637 (83), 0756 (86), 0194 (88). Odrębne od 0217 (X przed numerem).

### ADR-B-0654 (06-K06, klucz A) – PRZEREDAGOWANIE (temat 99 zachowany)

- #919: zgoda co do POPRAW; zamiennik 90 zbędny – temat 99 zachowany, poprawiona forma.
- Nowa treść: W górnym polu tablicy pomarańczowej jest numer 99. Kolega mówi, że to bardzo silne ryzyko samorzutnej reakcji, bo cyfra 9 jest powtórzona. Co według 5.3.2.3.2 oznacza numer 99?
- Klucz: Różne materiały niebezpieczne przewożone w podwyższonej temperaturze
- Cytaty i strony Dz.U.: 5.3.2.3.1 (s. 956) – zestawienia o znaczeniu specjalnym (m.in. 22, 323, 333, 362, X362, 382, X382, 423, 44, 446, 462, 482, 539, 90 i 99); 5.3.2.3.2 (s. 959): „90 materiał zagrażający środowisku; różne materiały niebezpieczne”, „99 różne materiały niebezpieczne przewożone w podwyższonej temperaturze.”
- Uwagi: 5.3.2.3.1 s. 956; 5.3.2.3.2 s. 959. Odrębne od 0051/0754 (powtórzenie cyfry), 0635 (333), 0653 (886).

### ADR-B-0655 (02-K14, klucz C) – NOWY ELEMENT (stare = 0127/0128/0610)

- #919: zgoda; zamiennik BŁĘDNY – w klasie 3 pojemność opakowania ma znaczenie (2.2.3.1.4, lepkie ciecze III grupy ≤ 450 l).
- Nowa treść: Kierowca wiezie UN 2796 KWAS SIARKOWY zawierający nie więcej niż 51% kwasu w kanistrach 10 l i w beczce 200 l. Kolega twierdzi, że w beczce ten kwas ma wyższą grupę pakowania niż w kanistrach. Co wynika z ADR?
- Klucz: Obie mają II grupę, bo grupa zależy od zagrożenia, nie od wielkości opakowania
- Cytaty i strony Dz.U.: 2.1.1.3 (s. 119): „…zalicza się do grup pakowania odpowiednio do stopnia stwarzanego przez nie zagrożenia: I grupa pakowania: materiały stwarzające duże zagrożenie; II … średnie; III … małe”; 3.2.1, objaśnienie kolumny (4) (s. 308); 2.2.8.1.4.2 (s. 265); tabela A (s. 517, obraz): UN 2796 KWAS SIARKOWY ≤ 51% – 8, C1, II.
- Uwagi: 2.1.1.3 s. 119; 2.2.8.1.4.2 s. 265; kolumna (4) s. 308; tabela A s. 517 (obraz strony). Odrębne od 0127 (I/II/III), 0128 (kolumna 3a), 0610 (kolumna 5).

### ADR-B-0656 (01-K04, klucz A) – NOWY ELEMENT (stare = lustro 0720/0091, 1.1.3.1 (c); treść podpowiadała warunki)

- #919: zgoda; zamiennik (1.1.3.1 (d)) – temat słuszny, opcja A urwana, średniki; exact_quote cytuje (d), choć pytanie było o (c).
- Nowa treść: Po wypadku straż pożarna prowadzi akcję ratowniczą. Na jej polecenie i pod jej nadzorem pomoc drogowa holuje uszkodzoną ciężarówkę z beczkami ADR z jezdni na pobliski bezpieczny plac. Czy do tego holowania stosuje się przepisy ADR?
- Klucz: Nie, to przewóz nadzorowany przez władze i konieczny w akcji ratowniczej
- Cytaty i strony Dz.U.: 1.1.3.1 (d) (s. 23): „przewozu wykonywanego przez właściwe władze w ramach działań ratowniczych lub przewozu nadzorowanego przez te władze, jeżeli przewóz ten jest konieczny ze względu na prowadzone działania ratownicze, w szczególności: – przewozu i holowania pojazdów przewożących towary niebezpieczne, w przypadku, gdy pojazdy te uczestniczyły w wypadku lub są uszkodzone;”
- Uwagi: 1.1.3.1 (d) s. 23. Odrębne od 0720/0091 (1.1.3.1 (c)), 0689 (1.1.3.1 (a)). Do oceny specjalisty (zakres pojęcia „nadzorowany przez władze”).

### ADR-B-0657 (02-K02, klucz A) – PRZEREDAGOWANIE (temat 2.1 zachowany)

- #919: zgoda co do POPRAW; zamiennik nieprecyzyjny (mieszanina trująca i palna to grupa TF, nie „T”); „0095” to pytanie o 4.2, nie 2.1.
- Nowa treść: Przed załadunkiem kierowca widzi na butli nalepkę z czerwonym tłem, płomieniem i cyfrą 2 w dolnym rogu, czyli wzór 2.1. Jakie zagrożenie wskazuje ta nalepka?
- Klucz: Gaz palny, który po ulotnieniu może się zapalić od iskry lub płomienia
- Cytaty i strony Dz.U.: 5.2.2.2.2 (s. 945, obraz strony): nalepka nr 2.1 „Gazy palne” – płomień czarny lub biały, tło czerwone, cyfra „2” w dolnym rogu; 2.2.2.1.3 UWAGA 1 (s. 155); wzór 5.4.3.4 (s. 976, obraz): nalepka 2.1 – „Zagrożenie pożarem. Zagrożenie wybuchem. … Zagrożenie wybuchem w przypadku ogrzania”.
- Uwagi: 5.2.2.2.2 s. 945 (obraz strony); 2.2.2.1.3 s. 155; wzór s. 976. Odrębne od 0221 (wskazówki 2.1), 0491 (załadunek), 0541 (2.2), 0151 (2.3).

### ADR-B-0658 (02-K03, klucz A) – PRZEREDAGOWANIE (temat zachowany)

- #919: zgoda co do POPRAW; zamiennik (prężność par) – zbędny, definicji temperatury zapłonu w banku nie ma; cytat 2.2.3.1.1 zamiast 1.2.1 (s. 46).
- Nowa treść: Karta charakterystyki cieczy przewożonej w kanistrach podaje temperaturę zapłonu 45 °C. Kolega uważa, że to temperatura, w której ciecz sama się zapala. Co według definicji z 1.2.1 oznacza temperatura zapłonu?
- Klucz: Najniższą temperaturę, w której para cieczy tworzy z powietrzem mieszaninę palną
- Cytaty i strony Dz.U.: 1.2.1 (s. 46): „Temperatura zapłonu oznacza najniższą temperaturę cieczy, w której jej para tworzy z powietrzem mieszaninę palną.”; 2.2.3.1.1 (s. 165) – kryterium 60 °C.
- Uwagi: 1.2.1 s. 46; 2.2.3.1.1 s. 165. Pokrewne 0722 (zastosowanie kryterium 60 °C). Odrębne od 0154/0187 (nalepka 3).

### ADR-B-0659 (01-K01, klucz A) – PRZEREDAGOWANIE (temat zachowany; podstawa „art. 2 Umowy ADR” zastąpiona)

- #919: zgoda co do POPRAW; zamiennik (jednostka transportowa) = 0147/0709.
- Nowa treść: Przewoźnik szuka w ADR przepisów o oznakowaniu sztuk przesyłek, a osobno przepisów o wyposażeniu pojazdu i obowiązkach załogi. Jak według 1.1.1 i 1.1.2 podzielono te zagadnienia między załączniki A i B?
- Klucz: Oznakowanie przesyłek jest w załączniku A, a pojazd i załoga w załączniku B
- Cytaty i strony Dz.U.: 1.1.1 (s. 22): „Załączniki A i B do ADR składają się z 9 części. Załącznik A zawiera części od 1 do 7, a załącznik B części 8 i 9.”; 1.1.2.1 (s. 22): „W rozumieniu artykułu 2 ADR, załącznik A określa: …”; 1.1.2.3 (s. 22): „W rozumieniu artykułu 2 ADR, załącznik B określa wymagania dotyczące konstrukcji, wyposażenia i używania pojazdów … – wymagania dotyczące załogi pojazdu, wyposażenia, postępowania i dokumentacji;”
- Uwagi: 1.1.1, 1.1.2.1, 1.1.2.3 s. 22. Odrębne od 0147/0709 (jednostka transportowa), 0639 (definicje 1.2.1).

### ADR-B-0660 (07-K07, klucz A) – NOWY ELEMENT (stare = 0567–0569/0713/0758; podstawa niepełna)

- #919: zgoda; zamiennik (KC 362) – temat słuszny, średniki; napisany od nowa. Dz.U. 2026 poz. 795 – ISTNIEJE.
- Nowa treść: Kierowca cofał na placu firmy bez osoby kierującej i uszkodził rower. Właściciel zostawił go w oznakowanej strefie manewrów, mimo że kierowca wcześniej go ostrzegał. Jak zachowanie właściciela może wpłynąć na odszkodowanie?
- Klucz: Odszkodowanie może zostać odpowiednio zmniejszone według okoliczności
- Cytaty i strony Dz.U.: 8.2.2.3.2 (k) (s. 1327): „ogólne informacje na temat odpowiedzialności cywilnej;”. Kodeks cywilny, t.j. Dz.U. 2026 poz. 795 (obwieszczenie z 27.05.2026, ogłoszone 17.06.2026 – ISTNIEJE), art. 362: „Jeżeli poszkodowany przyczynił się do powstania lub zwiększenia szkody, obowiązek jej naprawienia ulega odpowiedniemu zmniejszeniu stosownie do okoliczności, a zwłaszcza do stopnia winy obu stron.”
- Uwagi: 8.2.2.3.2 (k) s. 1327; KC art. 362 (Dz.U. 2026 poz. 795, ISAP/ELI). Odrębne od 0567–0569 (KC 435–436), 0713/0758 (KC 471/474). Do oceny specjalisty (prawnik).

## Wskaźniki

- „Poprawna = jedyna najdłuższa”: **21/780 = 2,69%** bez zmian; maksimum działu 5,66% bez zmian (3 pliki z wskaźnikiem – tylko SHA).
- „Poprawna = jedyna najkrótsza”: 94 → **88/780**; ADR-B-01 16,7% → 14,8%; ADR-B-02 11,2% → 7,9%; ADR-B-06 12,1% → 9,1%; ADR-B-05 18,4% i ADR-B-07 14,8% bez zmian; każdy dział ≤ 38% (maks. 18,4%).
- Żadna opcja nowych rekordów nie kończy się kropką, nie ma średnika ani słów absolutnych, wszystkie ≤ 80 zn.; klucz nigdy nie jest jedyną najdłuższą ani jedyną najkrótszą.
- similarity.py: cały bank – main **7 par ≥ 0,45 / 156 ≥ 0,25**; po poprawkach **7 / 159**. Pary z partią: main **1 / 9**; po poprawkach **1 / 12**. Najwyższe: 0637/0653 = 0,556 (83 vs 886 – rodzina numerów rozpoznawczych zagrożenia, różne numery), 0217/0653 = 0,375 (44 vs 886), 0635/0654 = 0,364 (333 vs 99), 0541/0657 = 0,350 (nalepka 2.2 vs 2.1 – różne nalepki), 0650/0651 = 0,303 (nalepka 8 vs 6.2). Wyszukiwanie po temacie w całym banku – brak duplikatów.
- Kompetencje: 05-K13, 05-K14, 05-K15 nadal po 5; pozostałe kompetencje partii po 6; kompetencje.json bez zmian.

## Synchronizacja (test na kopii repo)

- review/sequential/ i review/legal-clauses/: 629-654.json (tylko 0646–0654), 655-655 … 660-660.json – snapshoty; w legal-clauses clause, answer_review A/B/C, notes_on_conditions.
- Ledger: review/legal-polish/stage4w4-literal-verification-ledger-0610-0678.json (15 wpisów).
- Egzaminy 001–005: ŻADEN wariant nie zawiera 0646–0660 – zmienia się tylko SHA (10 plików). Kolejki 4X40/4X44 – tylko SHA.
- SHA 6dc2b850… → 835ba933… w 47 plikach; zostaje tylko w review/literal-pl/ i jako FIRST_PASS_BANK_SHA w tests/test_literal_review_0646_0660.py.
- REJESTR-AKTUALNY-0001-0765.md i 0001-0780.md – 15 wierszy.
- Lekcje i instruktor: ADR-B-01 (0656 → 1.1.3.1 (d) – nowa sekcja; stara sekcja 1.1.3.1 (c) wskazuje 0720; 0659 – podstawa 1.1.1, 1.1.2.1, 1.1.2.3), ADR-B-02 (0652 – podstawa + 2.2.8.1.4.1; 0655 – nowa sekcja o grupie i wielkości opakowania; stara sekcja tabeli A wskazuje 0127/0128/0610), ADR-B-07 (0660 → KC art. 362).

## Wynik testu

Git worktree z main 17c58e8af + POPRAWKI + synchronizacja: 14 skryptów CI zielonych (validate, coverage, check_mock_exam_variants, answer_leakage_metrics, answer_length_bias --threshold 0.16 --strict, check_explanation_quality --minimum 300, check_near_duplicates 0.60, check_cross_module_duplicates 0.80, similarity, check_explanation_heuristics, release_gate --report, check_sequential_audit, check_legal_clause_review, course_consistency); `python3 -m unittest discover -s tests` – **244/244 OK**. Blob banku po zastosowaniu: `835ba93341ece797cd831d85defa4d147da0942e`.

## Do pakietu dla specjalistów

- 0646, 0647 – technika gaszenia i dozór po ugaszeniu (zalecenia PSP, poza tekstem ADR) – instruktor ochrony przeciwpożarowej.
- 0648, 0649 – zadławienie, ograniczenie ruchów szyi (ERC 2025 First Aid) – instruktor pierwszej pomocy.
- 0656 – zakres 1.1.3.1 (d) („przewóz nadzorowany przez te władze”).
- 0660 i 0713 – relacja KC do ustawy Prawo przewozowe (art. 65, lex specialis) – prawnik.