# Kontrola druga – partia ADR-B-0616–0630 (porównanie dosłowne z polskim tekstem ADR 2025)

Data: 2026-11-10 (czas polski, CET).
Przedmiot: pierwsza kontrola ChatGPT (PR #915, scalony; main **0599f0720**; `review/literal-pl/PARTIA-0616-0630.md` + `.json` + `tests/test_literal_review_0616_0630.py`, podsumowanie 5 OK / 10 POPRAW / 0 BLOKUJ, licznik 165 → 150) oraz rekordy 0616–0630 na main (bank blob **7c6b46d4…**, 780 pytań; #915 banku nie zmienia).
Źródła: Dz.U. 2025 poz. 642 (OCR `-l pol`, przy tabelach i nalepkach obraz strony PDF – s. 517, 946, 948, 1109; strony wg nagłówka „Dziennik Ustaw — NNN —”): s. 182 (2.2.42.1.1), s. 196 (2.2.52.1.4), s. 214 (2.2.61.1.1), s. 264 (2.2.8.1.1, 2.2.8.1.4.1 – C11), s. 517 (tabela A – UN 2794), s. 712 (4.1.1.5.3), s. 935 (5.2.1.1–5.2.1.2), s. 938–939 (5.2.1.10.1–5.2.1.10.2 (f)), s. 939–940 (5.2.2.1.6), s. 946 (wzory nalepek 4.1–4.3), s. 948 (wzory nalepek 7A–7C), s. 961 (5.4.1.1.1 (c)), s. 963 (5.4.1.1.3.3), s. 974 (5.4.3.1–5.4.3.2), s. 975 (wzór instrukcji pisemnych – pierwsza strona), s. 1109 (6.5.2.2.2 – znak piętrzenia DPPL), s. 1308–1309 (7.5.7.1, 7.5.7.2, 7.5.7.4), s. 1324 (8.1.2.1 (b)), s. 1330 (8.2.2.8.2 (a)–(b)).
Status: kontrola robocza. **Żadne pytanie nie jest oznaczone jako zweryfikowane**; wszystkie pozostają `needs_review`; `review/approvals.jsonl` pusty.

## Podsumowanie

- Werdykty kontroli drugiej: **OK 0, POPRAW 15, BLOKUJ 0**.
- **Żaden z 5 werdyktów OK w #915 nie jest OK** (0616, 0618, 0619, 0626, 0628 – szczegóły niżej). ChatGPT nadal zawyża OK.
- **#915 – liczniki spójne** (5/10 w .md, .json i rekordach; licznik 165 → 150 poprawny). **Strony Dz.U. w #915 – poprawne** (0616 [955, 961], 0617 [939], 0618 [1308, 1309], 0619 [1330], 0620 [974], 0621 [182], 0622 [196], 0623 [214], 0624 [234], 0625 [264], 0626 [975], 0627 [939], 0628 [1308], 0629 [962], 0630 [975]).
- **#915 – test ma wreszcie DWIE stałe SHA** (FIRST_PASS_BANK_SHA i EXPECTED_BANK_SHA = 7c6b46d4…) – zgodnie z poleceniem. Ale `test_bank_is_unchanged_and_batch_records_remain_unverified` sprawdza bank względem OBU stałych – przy wdrożeniu asercję z FIRST_PASS trzeba usunąć.
- **#915 – brak zamienników**: żaden z 10 rekordów POPRAW nie ma `proposed_replacement`, wszystkie mają tylko `reason_no_safe_candidate` – wbrew poleceniu („reason_no_safe_candidate NIE wystarcza”). Test #915 akceptuje `proposed_replacement or reason_no_safe_candidate`, więc to przepuszcza – wbrew poleceniu, które wymagało sprawdzenia pól stem/options/correct_option/explanation/sources.
- **Duplikaty pominięte w #915**: 0617 = 0058/0172/0286/0682; 0618 ≈ 0078/0683; 0619 ≈ 0301; 0621 ≈ 0665/0724; 0623 ≈ 0158; 0624 = 0729; 0625 ≈ 0161; 0626 ≈ 0113/0187/0642/0648; 0628 = 0079; 0630 ≈ 0109.
- **15 pytań → nowy element tej samej kompetencji, niecysternowy**: 0616 (5.2.1.1–5.2.1.2 – rozmazany numer UN), 0617 (5.2.1.10.2 (f) – puszki 400 ml bez strzałek), 0618 (znak „nie piętrzyć” DPPL, 7.5.7.2), 0619 (8.2.2.8.2 (b) – egzamin ponad 12 miesięcy wcześniej), 0620 (karty charakterystyki nie zastępują instrukcji pisemnych), 0621 (nalepka 4.2), 0622 (nadtlenek a rogówka), 0623 (mała dawka, przenikanie przez skórę), 0624 (nalepka 7C – III-ŻÓŁTA), 0625 (UN 2794 – klasa 8, C11), 0626 (przytomny kolega w oparach – zawołać na stronę nawietrzną), 0627 (nalepki 3 i 6.1 na jednej stronie, w pobliżu), 0628 (7.5.7.4 – mocowanie kontenera na pojeździe), 0629 („PRZEWÓZ ZGODNIE Z 4.1.1.5.3”), 0630 (zagrożenie dodatkowe z dokumentu przewozowego przy nieczytelnych nalepkach).
- Litery kluczy, moduły i kompetencje bez zmian; nowych ID brak; bez tematów cysternowych. Kompetencje zachowują ≥ 6 pytań (wszystkie 15 – po 6; przypisania bez zmian).

## Błędy / różnice względem raportu ChatGPT (#915)

| ID | #915 | Kontrola 2 | Różnica |
|---|---|---|---|
| 0616 | OK | POPRAW – nowy element | kropki na końcu opcji; źródło 5.3.2.3.1 (tablica barwy pomarańczowej) poza kompetencją 06-K01 (numer UN na sztuce przesyłki) |
| 0617 | POPRAW | POPRAW – nowy element | zgoda; także = 0058/0172/0286/0682 (strzałki) – pominięte; brak zamiennika (tylko reason_no_safe_candidate); B 84 zn. z „Wyłącznie”, „;” w C |
| 0618 | OK | POPRAW – nowy element | kropki na końcu opcji; uginające się dolne opakowanie ≈ 0078/0683 |
| 0619 | OK | POPRAW – nowy element | A 82 zn. z „wyłącznie”, „;” w C; ogólnik 5 lat ≈ 0301 |
| 0620 | POPRAW | POPRAW – nowy element | zgoda (= 0050/0590/0716); brak zamiennika; B 94 zn., „każdy” w C |
| 0621 | POPRAW | POPRAW – nowy element | zgoda (= 0095/0154), także ≈ 0665/0724 – pominięte; brak zamiennika; C 107 zn., odwołanie do liter opcji w wyjaśnieniu |
| 0622 | POPRAW | POPRAW – nowy element | zgoda (= 0096/0157); brak zamiennika; B/C > 80 zn. |
| 0623 | POPRAW | POPRAW – nowy element | zgoda (= 0097), także ≈ 0158 – pominięte; brak zamiennika; półpauza „—” w C |
| 0624 | POPRAW | POPRAW – nowy element | zgoda (= 0098), także = 0729 – pominięte; brak zamiennika; klucz jedyną najdłuższą, A/B/C > 80, „wyłącznie” |
| 0625 | POPRAW | POPRAW – nowy element | zgoda (= 0005), także ≈ 0161 – pominięte; brak zamiennika; A/B/C > 80 zn. |
| 0626 | OK | POPRAW – nowy element | A/B/C > 80 zn., „zawsze” w A, „;” w C, klucz jedyną najkrótszą; ≈ 0113/0187/0642/0648 |
| 0627 | POPRAW | POPRAW – nowy element | zgoda (= 0115); brak zamiennika; „wszystkie” w A, „kolumna 5” bez nawiasów |
| 0628 | OK | POPRAW – nowy element | kropki, B/C > 80 zn., „wszystkie” w C; = 0079 (pasy odkształcają opakowania), ≈ 0236 |
| 0629 | POPRAW | POPRAW – nowy element | zgoda (temat „ODPAD” 5.4.1.1.3.1 wyczerpany); brak zamiennika; A/C > 100 zn., klucz jedyną najkrótszą |
| 0630 | POPRAW | POPRAW – nowy element | zgoda (= 0185, ≈ 0105/0165), także ≈ 0109 – pominięte; brak zamiennika; A/C > 100 zn., „wyłącznie”, klucz jedyną najkrótszą |

## Duplikaty – sprawdzenie w całym banku (780) i między sobą

- Stare rekordy: 0616 – źródło poza kompetencją; 0617 = 0058, 0172, 0286, 0682; 0618 ≈ 0078, 0683; 0619 ≈ 0301; 0620 = 0050, 0590, 0716; 0621 = 0095, 0154, ≈ 0665, 0724; 0622 = 0096, 0157; 0623 = 0097, ≈ 0158; 0624 = 0098, 0729; 0625 = 0005, ≈ 0161; 0626 ≈ 0113, 0187, 0642, 0648; 0627 = 0115; 0628 = 0079, ≈ 0236; 0629 – „ODPAD” wyczerpany (0008/0046/0179/0294/0680); 0630 = 0185, ≈ 0105, 0109, 0165.
- Nowe rekordy – sprawdzone ręcznie z najbliższymi tematami: 0616 vs 0114/0188/0281/0689/0750 (wysokość, klatka, opakowanie zbiorcze) i 0562 (wyblakła nalepka); 0617 vs 0682 (wyjątek (b) 120 ml) i 0766 (750 ml); 0618 vs 0059/0078/0237/0683/0767; 0619 vs 0301 (przypadek (a)) i 0148/0607; 0620 vs 0050/0590/0716 (język) i 0090/0780 (miejsce); 0621 vs 0095/0154/0302/0665/0724 (definicje) i 0541/0657 (inne nalepki); 0622 vs 0307 (inicjatory rozkładu); 0623 vs 0289/0670/0727; 0624 vs 0669 (kategoria z TI); 0625 vs 0267/0652/0730; 0627 vs 0189/0303/0688/0751; 0628 vs 0026/0235/0236/0703/0764 (mocowanie sztuk przesyłek); 0629 vs 0318 (5.4.1.1.3.2) i 0732; 0630 vs 0229 (ilość z dokumentu) i 0523 (zapis 3 (6.1)).
- Odrzucone kandydatury (temat zajęty): 5.2.1.4 (DPPL – dwie strony) ≈ 0303; 8.1.2.2 → 0146/0551/0588; luki przy 7.5.7.1 → 0236/0703; 5.4.1.1.3.2 → 0318; maska ucieczkowa → 0230; limit czasowy klasy 7 → 0295; język dokumentu 5.4.1.4.1 → 0533; 5.4.1.1.18 → 0465.
- `similarity.py`: cały bank – main **8 par ≥ 0,45 / 165 par ≥ 0,25**; po poprawkach **7 / 154**. Pary z udziałem partii: main **1 ≥ 0,45 / 11 ≥ 0,25** (zgodnie z #915; 0185/0630 = 0,467); po poprawkach **0 / 0** (wcześniejsze robocze brzmienia 0619 i 0630 dawały 0,480 z 0301 i 0229 – treść przeredagowana).
- `check_near_duplicates.py --threshold 0.60`: 0 nieprzejrzanych par; `check_cross_module_duplicates.py --threshold 0.80`: PASS.
- Uwagi na później (poza tą partią): 0632 (partia 43) – wcześniejsza notatka „= 0297” nie potwierdza się (0297: wyciek 6.2 i ręcznik); bliższe są pytania o osoby postronne (0035/0111/0186/0213/0701/0775) – do rozstrzygnięcia w partii 43; 0708 (moduł 10) = 0714.

## Szczegóły – cytaty (dosłownie z Dz.U.) i rozstrzygnięcia

### ADR-B-0616 – POPRAW (06-K01, C) – NOWY ELEMENT (#915: OK)
5.2.1.1 (s. 935): „Jeżeli inne przepisy ADR nie stanowią inaczej, to każda sztuka przesyłki powinna być oznakowana w sposób czytelny i trwały numerami UN zawartych w niej towarów niebezpiecznych, poprzedzonymi literami „UN”.” 5.2.1.2 (s. 935): „Oznakowanie wszystkich sztuk przesyłek wymagane przepisami niniejszego działu: (a) powinno być dobrze widoczne i czytelne; (b) powinno być odporne na zewnętrzne warunki atmosferyczne, nie wykazując przy tym znaczącej utraty swoich funkcji.” Nowe pytanie: numer UN napisany zmywalnym markerem rozmazał się w deszczu → oznakowanie trzeba poprawić przed przewozem. Pokrewne 0562 (wyblakła nalepka) – do oceny specjalisty. Opcje 69/72/71 zn.

### ADR-B-0617 – POPRAW (09-K04, A) – NOWY ELEMENT (= 0058/0172/0286/0682)
5.2.1.10.2 (s. 939) – strzałki z 5.2.1.10.1 nie są wymagane m.in. na „(f) opakowaniach zewnętrznych zawierających towary niebezpieczne w hermetycznie zamkniętych opakowaniach wewnętrznych o pojemności nie większej niż 500 ml każde.” Nowe pytanie: puszki 400 ml hermetycznie zamknięte, bez materiału chłonnego → strzałki niewymagane (wyjątek (f), nie (b)). Odrębne od 0682 (wyjątek (b) 120 ml) i 0766 (750 ml). Opcje 72/76/70 zn.

### ADR-B-0618 – POPRAW (09-K05, B) – NOWY ELEMENT (#915: OK)
6.5.2.2.2 (s. 1109, obraz strony): rysunki „DPPL przeznaczony do piętrzenia” (z „… kg max”) i „DPPL nie przeznaczony do piętrzenia” (przekreślony kwadrat). 7.5.7.2 (s. 1309): „Sztuki przesyłek nie powinny być piętrzone, jeżeli ich konstrukcja nie przewiduje piętrzenia.” Nowe pytanie: DPPL ze znakiem przekreślonego kwadratu, kolega chce postawić drugi DPPL na nim i spiąć pasami → nie. Opcje 79/79/77 zn.

### ADR-B-0619 – POPRAW (01-K03, C) – NOWY ELEMENT (#915: OK)
8.2.2.8.2 (b) (s. 1330): „w okresie wcześniejszym niż 12 miesięcy przed datą wygaśnięcia ważności zaświadczenia, właściwa władza powinna wydać nowe zaświadczenie ważne przez okres 5 lat, liczony od daty złożenia z wynikiem pozytywnym egzaminu z zakresu ukończonego kursu doskonalącego.” Nowe pytanie: egzamin 10.03.2026, stare ważne do 30.06.2027 → nowe do 10.03.2031. Pokrewne 0301 (przypadek (a)) – tu przypadek (b); treść przeredagowana tak, by similarity z 0301 < 0,25. Do oceny specjalisty. Opcje 67/72/68 zn.

### ADR-B-0620 – POPRAW (13-K07, C) – NOWY ELEMENT (= 0050/0590/0716)
5.4.3.1 (s. 974): „W kabinie kierowcy, w miejscu łatwo dostępnym, powinny być przewożone instrukcje pisemne w formie podanej w 5.4.3.4, stanowiące pomoc w razie zaistnienia wypadku podczas przewozu.”; 5.4.3.2 (s. 974); wzór 5.4.3.4 (s. 975); 8.1.2.1 (b) (s. 1324). Nowe pytanie: karty charakterystyki zamiast instrukcji pisemnych → nie. Opcje 71/69/69 zn.

### ADR-B-0621 – POPRAW (02-K05, A) – NOWY ELEMENT (= 0095/0154, ≈ 0665/0724)
5.2.2.2.2 (s. 946, obraz strony) – wzór nalepki 4.2: górna połowa biała, dolna czerwona, płomień czarny, cyfra „4”; 2.2.42.1.1 (s. 182): materiały piroforyczne i samonagrzewające się (klasa 4.2). Nowe pytanie: rozpoznanie nalepki 4.2 vs 4.1 (białe tło z siedmioma czerwonymi pasami) i 4.3 (tło niebieskie). Opcje 61/66/60 zn.

### ADR-B-0622 – POPRAW (02-K08, B) – NOWY ELEMENT (= 0096/0157)
2.2.52.1.4 (s. 196): „Niektóre nadtlenki organiczne mogą powodować poważne uszkodzenia rogówki, nawet przy krótkotrwałym kontakcie oraz mogą działać żrąco na skórę.” Nowe pytanie: krople nadtlenku a oczy bez okularów → możliwe poważne uszkodzenie rogówki. Opcje 79/73/63 zn.

### ADR-B-0623 – POPRAW (02-K09, C) – NOWY ELEMENT (= 0097, ≈ 0158)
2.2.61.1.1 (s. 214): materiały, „które (…) mogą w wyniku jednorazowego lub krótkotrwałego działania w stosunkowo małych dawkach - spowodować uszczerbek na zdrowiu lub śmierć człowieka w wyniku ich wdychania, przenikania przez skórę lub połknięcia.” Wzór 5.4.3.4 (s. 975): nie dotykać uwolnionych materiałów. Nowe pytanie: wycieranie kropli 6.1 gołą dłonią → nie. Opcje 66/58/58 zn.

### ADR-B-0624 – POPRAW (02-K11, A) – NOWY ELEMENT (= 0098/0729)
5.2.2.2.2 (s. 948, obraz strony) – wzory nalepek 7A (I-BIAŁA, jeden pasek), 7B (II-ŻÓŁTA, dwa paski), 7C (III-ŻÓŁTA, trzy paski, ramka „TRANSPORT INDEX”). Nowe pytanie: rozpoznanie kategorii z nalepki 7C. Bez wymagań kursu specjalistycznego klasy 7 – tylko rozpoznanie nalepki. Opcje 60/62/57 zn.

### ADR-B-0625 – POPRAW (02-K12, B) – NOWY ELEMENT (= 0005, ≈ 0161)
Tabela A (s. 517, obraz strony): „2794 AKUMULATORY MOKRE NAPEŁNIONE KWASEM elektryczne” – klasa 8, kod C11, nalepka 8; 2.2.8.1.4.1 (s. 264): „C11 Przedmioty”; 2.2.8.1.1 (s. 264) – tytuł klasy 8. Nowe pytanie: akumulatory z kwasem to klasa 8, nie 9 ani 4.3. Opcje 61/54/51 zn.

### ADR-B-0626 – POPRAW (05-K11, C) – NOWY ELEMENT (#915: OK)
Wzór 5.4.3.4 (s. 975): „Nie wchodzić na uwolnione materiały, nie dotykać ich, unikać wdychania oparów, dymu, pyłu i pary poprzez pozostawanie po stronie nawietrznej;” oraz „Oddalić się od miejsca wypadku lub zagrożenia, poinformować inne osoby o konieczności oddalenia się od tego miejsca oraz stosować się do zaleceń służb ratowniczych;”. Nowe pytanie: przytomny kolega w oparach → zawołać, by sam wyszedł na stronę nawietrzną. Pokrewne pytaniom „nie wchodzić w strefę” (0113/0187/0642/0648) – do oceny specjalisty. Opcje 67/59/62 zn.

### ADR-B-0627 – POPRAW (06-K02, A) – NOWY ELEMENT (= 0115)
5.2.2.1.6 (s. 939–940): „każda nalepka ostrzegawcza powinna być: (a) umieszczona na tej samej stronie sztuki przesyłki, jeżeli pozwala na to wielkość tej sztuki (…) (c) umieszczona w pobliżu innych nalepek ostrzegawczych, jeżeli wymaga się więcej niż jednej nalepki ostrzegawczej.” Nowe pytanie: nalepki 3 i 6.1 na przedniej i tylnej ściance → nie. Opcje 62/67/61 zn.

### ADR-B-0628 – POPRAW (09-K02, B) – NOWY ELEMENT (#915: OK)
7.5.7.4 (s. 1309): „Przepisy podane w 7.5.7.1 mają również zastosowanie do załadunku, mocowania i rozładunku kontenerów, kontenerów-cystern, cystern przenośnych i MEGC na pojazdach i z pojazdów.”; 7.5.7.1 (s. 1308). Nowe pytanie: kontener z zamocowanymi beczkami, niezablokowany na naczepie → trzeba go zamocować. Tylko kontener ogólny – bez tematu cystern. Opcje 78/78/69 zn.

### ADR-B-0629 – POPRAW (03-K02, B) – NOWY ELEMENT (temat „ODPAD” wyczerpany)
5.4.1.1.3.3 (s. 963): „W przypadku przewozu zgodnie z 4.1.1.5.3, w dokumencie przewozowym należy umieścić następującą informację: „Przewóz zgodnie z 4.1.1.5.3”.”; 4.1.1.5.3 (s. 712): „W przypadku przewozu odpadów, innych niż przedmioty, opakowania wewnętrzne o różnych rozmiarach i kształtach, zawierające materiały ciekłe lub stałe, mogą być pakowane razem w jedno opakowanie zewnętrzne, pod warunkiem spełnienia następujących wymagań”. Nowe pytanie: puszki odpadów w jednej beczce → zapis „PRZEWÓZ ZGODNIE Z 4.1.1.5.3”. Odrębne od 0318 (5.4.1.1.3.2) i 0732. Opcje 63/64/65 zn.

### ADR-B-0630 – POPRAW (05-K07, B) – NOWY ELEMENT (= 0185, ≈ 0105/0109/0165)
Wzór 5.4.3.4 (s. 975): „Zapewnić przybyłym ratownikom łatwy dostęp do dokumentów przewozowych;”; 5.4.1.1.1 (c) (s. 961): przy więcej niż jednym numerze wzoru nalepki „numery następujące po pierwszym numerze powinny być podane w nawiasach.” Nowe pytanie: nalepki osmalone, ratownik pyta o działanie trujące → dokument przewozowy, zapis 3 (6.1). Pokrewne 0229 (ilość z dokumentu) i 0523 (zapis 3 (6.1)); treść przeredagowana tak, by similarity z 0229 < 0,25. Opcje 68/70/74 zn.

## Wskaźniki

- Wszystkie 15 rekordów: wyjaśnienie ≥ 300 zn., 2–5 zdań, maks. 35 słów w zdaniu, koniec „Podstawa: ADR …”; opcje ≤ 80 zn.; bez słów absolutnych, średników, kropek na końcu opcji, „np.”, „min.”, „kol.”, „odpowiedź A/B/C”.
- Klucz nie jest jedyną najdłuższą ani jedyną najkrótszą w żadnym z 15 rekordów.
- „Poprawna = jedyna najdłuższa”: **24/780 = 3,08% → 23/780 = 2,95%**; maksimum działu **6,74% → 5,66%** (ADR-B-02: 6/89 → 5/89). **Aktualizacja w 4 miejscach / 3 plikach**: `docs/POKRYCIE-KURSU.md`, `docs/STAN-KONCOWY-BANKU-ADR-PODSTAWOWY-2026-11-03.md` (dwa wiersze tabeli), `podstawowy/README.md`.
- „Poprawna = jedyna najkrótsza”: 109 → 104/780; maks. działu 26,4% → 24,1% (ADR-B-05) – poniżej 38%. Działy: 02: 12,4% → 11,2%; 03: 13,3% → 11,7%; 05: 26,4% → 24,1%; 06: 19,7% → 18,2%.
- Rozkład liter kluczy bez zmian.

## Egzaminy, kolejki, snapshoty (pułapki CI)

- Egzaminy próbne: wariant 001 – 0621, 0626, 0629, 0630; wariant 002 – 0622; wariant 003 – 0623, 0628; wariant 004 – 0624; wariant 005 – 0625 (`wariant-00N.json`: stem, options; `klucz-00N.json`: explanation, legal_basis; litery bez zmian). `excluded_question_ids` w 002–005 bez zmian.
- Kolejki `KOLEJKA-PRIORYTETOWA-4X40.json` / `4X44.json`: żadnego ID z partii – zmienia się tylko `source_bank_blob_sha`.
- Snapshoty `review/sequential/` i `review/legal-clauses/`: **610-620.json** (0616–0620), **621-628.json** (0621–0628), **629-654.json** (0629–0630).
- Ledger `review/legal-polish/stage4w4-literal-verification-ledger-0610-0678.json` (0616–0630): `source_references` – 15 ID.
- Rejestry `REJESTR-AKTUALNY-0001-0765.md` i `-0001-0780.md`: po 15 wierszy.
- SHA banku 7c6b46d4… w **45 plikach** poza historycznymi raportami `review/literal-pl/` i poza `tests/test_literal_review_0616_0630.py` – w tym 21 testów `test_literal_review_0301_0315 … 0601_0615` (w 0571_0585, 0586_0600, 0601_0615 tylko EXPECTED_BANK_SHA; ich FIRST_PASS zostają).
- Lekcje: `podstawowy/lekcje/ADR-B-03.md` (scenariusz „opis odpadu w dokumencie — ADR-B-0629”) i `podstawowy/instruktor/ADR-B-03.md` (SC-ADR-B-03-03) – podstawa „ADR 5.4.1.1.3.1” → „ADR 5.4.1.1.3.1 i 5.4.1.1.3.3” (nowe 0629 dotyczy 5.4.1.1.3.3; temat scenariusza – opis odpadu w dokumencie – nadal zgodny). Pozostałe listy ID (lekcje 01, 02, 05, 06, 09, 13; instruktor 05; SC-ADR-B-05 z 0630, SC-ADR-B-03-03 z 0629) bez zmian – tematy zgodne.
- Oczekiwany SHA banku: **7c6b46d4134301f616cfc39d2b3e33e4318da428 → 8596a7a61cdc27c4f558af7197cdca9072090c4e**.

## Test na kopii repo

`test_p42.sh` – git worktree `/tmp/b42` z main 0599f0720 (bez commitów i pushu): `tools/apply_poprawki.py` z dopisanym `POPRAWKI-KONTROLA2-0616-0630.jsonl` → „Changed (15)”, blob **8596a7a61cdc27c4f558af7197cdca9072090c4e**; synchronizacja (`sync_p42_test.py`); wszystkie **14 skryptów CI** – kod 0; `python3 -m unittest discover -s tests` – **Ran 238 tests – OK**.

## Licznik

Pozostało **150** pytań bez porównania dosłownego po obu kontrolach (0631–0780).