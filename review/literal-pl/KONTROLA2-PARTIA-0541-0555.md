# Kontrola druga – partia ADR-B-0541–0555 (porównanie dosłowne z polskim tekstem ADR 2025)

Data: 2026-11-10, ok. 08:20 (czas polski, CET).
Przedmiot: pierwsza kontrola ChatGPT (PR #905, scalony; main **e46d36eaf**; `review/literal-pl/PARTIA-0541-0555.md` + `.json` + `tests/test_literal_review_0541_0555.py`, wynik 7 OK / 8 POPRAW / 0 BLOKUJ) oraz rekordy 0541–0555 na main (bank blob **73aa25f2…**, 780 pytań; #905 banku nie zmienia).
Źródło: Dz.U. 2025 poz. 642 (skany PDF), OCR tesseract `-l pol`; strony wg nagłówka „Dziennik Ustaw — NNN —”. Na **obrazie strony PDF** sprawdzone: s. 942 (5.2.2.2, 5.2.2.2.1, 5.2.2.2.1.1.3), s. 943 (5.2.2.2.1.3–5.2.2.2.1.7 – bez wzorów), s. 944 (początek tabeli 5.2.2.2.2 – klasa 1), **s. 945 (wzory nr 2.1, 2.2, 2.3 i 3)**, s. 946 (wzory 4.1, 4.2, 4.3, 5.1), s. 611 (tabela A, UN 3480 – nalepka 9A). Pozostałe strony wg nagłówków OCR: s. 37 (1.2.1 – kontener mały), s. 154 (2.2.2.1.2), s. 165 (2.2.3.1.1), s. 377 (tabela A, UN 1230 – 3+6.1), s. 950 (5.3.1.1.1–5.3.1.1.5), s. 951 (5.3.1.1.6, 5.3.1.1.7, 5.3.1.2), s. 952 (5.3.1.7.1 – romb, 250 mm × 250 mm, linia 12,5 mm), s. 953 (5.3.1.7.1 – cyfry 25 mm; 5.3.1.7.3; 5.3.1.7.4), s. 956 (5.3.2.3.1), s. 957 (5.3.2.3.2 – numery 23 i 70), s. 1304 (7.5.1.1, 7.5.1.2 z istotnymi wadami (a)–(c)), s. 1324 (8.1.2.1, 8.1.2.2), s. 1331 (8.2.2.8.3), s. 1343 (9.1.2 UWAGA), s. 1344 (9.1.2.3, 9.1.3.1–9.1.3.4). Sprostowanie poz. 1575 – bez wpływu na tę partię.
Status: kontrola robocza. **Żadne pytanie nie jest oznaczone jako zweryfikowane**; wszystkie pozostają `needs_review`.

## Podsumowanie

- Werdykty kontroli drugiej: **OK 0, POPRAW 15, BLOKUJ 0** (#905: 7 OK – 0541, 0542, 0545, 0549, 0553, 0554 nie są OK; 0543 i 0544 – zgoda co do POPRAW).
- **0549 – #905 podał w tabeli „Klucz A prawidłowy”, a w banku klucz to B** („Nie; oznakowanie musi odpowiadać wymaganiom ADR…”). Werdykt OK wydano więc dla klucza, którego w banku nie ma.
- **Strony Dz.U. – 3 błędy**: 0541 i 0542 – wzory nalepek 2.1, 2.2, 2.3 i 3 stoją w tabeli 5.2.2.2.2 na **s. 945** (obraz strony), nie na 942/943 (s. 943 to 5.2.2.2.1.3–5.2.2.2.1.7 bez rysunków); 0549 – zdanie o wymiarach 250 mm × 250 mm stoi na **s. 952**, na s. 953 jest tylko dalsza część 5.3.1.7.1 (cyfry 25 mm). Ponadto dla 0541/0542 #905 podaje 5.2.2.2.1.1.3 – to przepis o **zmniejszaniu wymiarów** nalepki, bez związku z pytaniem; cytat „koloru, symboli i formatu” pochodzi z 5.2.2.2.1 (s. 942). #905 zostawił „sprawdzenie obrazu PDF” jako otwarte – sprawdziłem (s. 945): zielone tło + butla = 2.2 „Gazy niepalne i nietrujące”; czerwone tło + płomień + cyfra 3 = wzór 3; rysunki SVG w `assets/adr-original/` są zgodne z wzorami.
- **Duplikaty – #905 wskazał tylko „kandydatów”, nie rozstrzygnął żadnego; faktycznie 6 pytań dubluje istniejące**: 0546 = **0562** (nieczytelna/uszkodzona duża nalepka – wymienić); 0548 = **0563** (rozładowany nieoczyszczony kontener – nalepki zostają; ta sama treść, ten sam błędny przepis 5.3.1.1.5); 0550 ≈ **0133** (duże nalepki kontenera zasłonięte – ADR: 5.3.1.3, nalepki na pojeździe; klucz 0550 „usunąć przeszkodę” nie jest rozwiązaniem z ADR); 0552 = **0137** (dla jakich pojazdów świadectwo dopuszczenia; 9.1.2 UWAGA); 0555 = **0020, 0054, 0078, 0517, 0584** (uszkodzona sztuka przesyłki – nie ładować, 1.4.3.1.1 (b); 7.5.1.2 tego nie reguluje – #905 słusznie wytknął złą podstawę); 0551 ≈ **0566** (świadectwo „ważne i dostępne podczas przewozu”, 8.1.2.2/9.1.3.1). Przy 0546, 0548, 0552 i 0555 #905 zalecał tylko korektę długości – brak `proposed_replacement`.
- **Polskie brzmienie**: „nalepki dużego formatu” (0546–0550, także 0132, 0561–0564) to kalka z „placards” – polski tekst ADR: **„duże nalepki ostrzegawcze”** (5.3.1). #905 tego nie zgłosił (jak „OVERPACK” w partii 36). Uwaga na partię 38: 0561–0564 używają „nalepek dużego formatu”, a 0561 podaje 5.3.1.1.4 (klasa 9) dla nalepek na czołach kontenera – właściwy przepis to 5.3.1.2; 0563 = 0548 (stara wersja) z błędnym 5.3.1.1.5 (właściwy: 5.3.1.1.6); 0566 po tej partii pokrywa się z nowymi 0551/0553.
- **Wady formy, których #905 nie zgłosił**: treść podaje odpowiedź – 0541 („Który rodzaj zagrożenia przedstawia wzór nalepki 2.2?” – tylko klucz B zawiera „2.2”), 0542 (opcja A powtarza opis z treści „czerwonym rombem z płomieniem”); 0542 – zdanie po „Podstawa: ADR …” (podstawa nie na końcu); 0554 C = **81 zn.** (> 80; #905: „OK, 63/78/81”); 0545 – „szkoleniowy schemat” bez rysunku; kropki na końcu opcji – 0541 (wszystkie), 0543 A, 0544 B, 0545 (wszystkie), 0552 C; średnik w opcji – 0548 C, 0549 B, 0552 B; słowa absolutne – 0552 treść „każdy… automatycznie”, A „niezależnie”, C „wyłącznie”; klucze ogólnikowe („sprawdzić wymagania ADR i umieścić komplet” – 0547; „odpowiadać wymaganiom ADR dotyczącym wzoru” – 0549; „obowiązek zależy od rodzaju pojazdu” – 0552); 0547 – klucz „komplet nalepek” jest wręcz sprzeczny z 5.3.1.1.5 (nalepkę zagrożenia dodatkowego można pominąć); 0553 – w banku źródło 9.1.3.1, a reguła o ważności to 9.1.3.4 (#905 podał 9.1.3.4 w tabeli, ale nie zgłosił rozbieżności); 0553 – „Kontynuować przewóz” przy „przed wyjazdem”; 0548 – źródło 5.3.1.1.5 (klasy wielokrotne) zamiast 5.3.1.1.6.
- **Jakość raportu #905**: w `.json` pole `exact_quote` jest **puste (null) w 6 rekordach** (0547, 0549, 0550, 0552, 0554, 0555), a w pozostałych to 2–4 słowa („emisja gazu”, „jednego roku”) – to nie jest porównanie dosłowne; brak wyniku `similarity.py` (polecenie: „URUCHOM similarity.py, opisz próg i wynik”); brak `proposed_replacement` przy duplikatach.
- **Test #905 znowu ma tylko EXPECTED_BANK_SHA** (polecenie 36 punkt c: „OD RAZU z DWIEMA stałymi”). Ta sama stała służy manifestowi i bankowi – po wdrożeniu jedna asercja musi być czerwona. Naprawiamy w PR wdrożenia.
- **Licznik 240 → 225 – poprawny** (po partii 36 zostało 240; partia 37 = 15).
- **7 pytań → nowy element z tej samej kompetencji, niecysternowy**:
  - 0546 (06-K09) → kontener z bateriami UN 3480 (9A): duża nalepka **wzoru 9**, bo wzoru 9A nie stosuje się jako dużej nalepki; na obu bokach i obu czołach (5.3.1.1.4 s. 950; 5.3.1.2 s. 951; tabela A s. 611) – w banku brak pytania o 5.3.1.1.4 (0561 tylko błędnie cytuje ten punkt);
  - 0547 (06-K09) → 5.3.1.1.5 na konkretnym przykładzie: UN 1230 (3+6.1) + ciecz klasy 8 → nalepki 3, 6.1 i 8; zagrożenia dodatkowego nie pomija się, gdy nie wskazuje go inna nalepka (s. 950);
  - 0548 (06-K09) → kontener o pojemności do 3 m³ (kontener mały): wystarczą zwykłe nalepki z 5.2.2.2, jeżeli są widoczne z zewnątrz pojazdu (5.3.1.7.3 s. 953; 1.2.1 s. 37);
  - 0550 (06-K09) → kontrastowe podłoże lub obwódka dużej nalepki na kontenerze tego samego koloru (5.3.1.1.1 s. 950);
  - 0551 (08-K08) → świadectwa dopuszczenia w kabinie **dla każdego pojazdu jednostki** (ciągnik i naczepa) (8.1.2.2 (a) s. 1324);
  - 0552 (08-K08) → wygląd świadectwa: A4, białe, z różowym paskiem po przekątnej; karta plastikowa to wzór zaświadczenia kierowcy (9.1.3.3 s. 1344; 8.2.2.8.3 s. 1331);
  - 0555 (09-K08) → istotne wady kontenera: złamany zawias i podarta uszczelka drzwi – kontener niezdatny, załadunek nie powinien się odbyć (7.5.1.2 (c) s. 1304) – w banku brak pytania o wady (a)–(c).
- **8 pytań przeredagowanych w tym samym podtemacie**: 0541 (2.2 – bez numeru wzoru w treści i w opcjach), 0542 (wzór 3 vs 2.1 – rozróżnienie po cyfrze; 4.1 – pasy), 0543 (cyfra 2 w numerze 23), 0544 (cyfra 4), 0545 (cyfra 7 w numerze 70; bez „schematu”), 0549 (konkretnie: 200 mm za mało, minimum 250 mm × 250 mm; wyjątki 5.3.1.7.3, 5.3.1.7.4), 0553 (9.1.3.4 – nowy okres od daty wygaśnięcia przy badaniu w ciągu miesiąca; po wygaśnięciu – zakaz używania), 0554 (pozostałości niezgodne – C ≤ 80 zn.).
- **Żaden zamiennik nie jest cysternowy** (kontenery ze sztukami przesyłek, ciągnik z naczepą bez wskazania cysterny, kontener na kartony). Tematy 5.3.2.3.1 (cyfry 2, 4, 7) nie dublują 0503 (3), 0504 (5), 0505 (9), 0053/0637 (8), 0507 (zero), 0051/0635 (powtórzenie), 0017/0170/0615/0698/0752 (X) – każda cyfra to odrębny element.
- Wszędzie ta sama litera klucza, ten sam `module_id`, `image` bez zmian (0541, 0542 – rysunki SVG zostają); przypisania w `kompetencje.json` bez zmian (02-K02 = **6**, 02-K03 = **6**, 06-K03 = 11, 06-K09 = 13, 08-K08 = 8, 09-K08 = 7; minimum kompetencji teoretycznych = 6).

## Błędy / różnice względem raportu ChatGPT (#905)

1. **0549 – błędny klucz w raporcie** („Klucz A prawidłowy”; w banku B). Werdykt OK nieuprawniony.
2. **Strony Dz.U. – 3 błędy** (0541, 0542 → 945; 0549 → 952 i 953) + nietrafiony przepis 5.2.2.2.1.1.3 przy 0541/0542. Test #905 utrwala błędne strony w `EXPECTED_PAGES` – trzeba poprawić `.json` i test.
3. **Test #905 ma tylko EXPECTED_BANK_SHA** – drugi raz z rzędu wbrew poleceniu. Dodać FIRST_PASS_BANK_SHA = 73aa25f2… (manifest) i EXPECTED_BANK_SHA = nowy (bank).
4. **0541, 0542, 0545, 0549, 0553, 0554 nie są OK**: 0541/0542 – treść lub opcja podaje odpowiedź, 0542 „Podstawa” nie na końcu; 0545 – kropki, „schemat” bez rysunku; 0549 – średnik, klucz ogólnikowy; 0553 – źródło 9.1.3.1 zamiast 9.1.3.4, ≈ 0566; 0554 – C 81 zn.
5. **Przeoczone/nierozstrzygnięte duplikaty**: 0546 = 0562; 0548 = 0563; 0550 ≈ 0133; 0552 = 0137; 0555 = 0020/0054/0078/0517/0584; 0551 ≈ 0566. Kandydaci #905 (0546/0562, 0548/0563, 0552/0137) to **rzeczywiste duplikaty**, nie „bliskość do oceny”.
6. **„nalepki dużego formatu”** → polskie „duże nalepki ostrzegawcze” (5.3.1) – nie zgłoszone.
7. **Raport bez cytatów i bez similarity.py**: `exact_quote` = null w 6 rekordach, w pozostałych 2–4 słowa; brak opisu progu i wyniku `similarity.py`.
8. **Słusznie w #905**: klucze 14 pytań merytorycznie poprawne (poza błędnym opisem 0549); 0555 – 7.5.1.2 nie reguluje uszkodzonej sztuki przesyłki; 0553 – właściwy punkt to 9.1.3.4; 0548 – właściwy punkt to 5.3.1.1.6; 0547 – wskazanie 5.3.1.1.5; opcje > 80 zn. w 0543, 0544, 0546, 0547, 0548, 0550, 0551, 0552, 0555; strony 154, 165, 950, 951, 956, 1304, 1324, 1344; licznik 240 → 225.
9. **Zaległość z #904** (CI jej nie wykrywa): `docs/STAN-KONCOWY-BANKU-ADR-PODSTAWOWY-2026-11-03.md` – **2× stary SHA f732aa35…** (wiersz tabeli „Git blob SHA” i punkt o egzaminach) oraz **nieaktualne wskaźniki w tej samej tabeli**: „Poprawna odpowiedź jedyną najdłuższą | **85/780 = 10,90%**” (aktualnie 29/780 = 3,72%) i „Najwyższy wskaźnik w pojedynczym dziale | **15,22%**” (aktualnie 6,74%). Pozostałe miejsca z #904 sprawdzone – aktualne: legal-clauses 0511–0540 (clause, answer_review, snapshoty), rejestry 0765/0780 (29 wierszy), ledger, egzaminy, POKRYCIE/README (29/780 = 3,72%), test 0526_0540 (dwie stałe), PARTIA-0526-0540.json (255/240).

## Duplikaty – sprawdzenie w całym banku (780) i między sobą

Przeszukano cały bank po temacie (nalepki 2.1/2.2/2.3/3/4.1/9/9A, 5.2.2.2.2, 2.2.2.1, 2.2.3.1.1, numery rozpoznawcze 5.3.2.3.1/5.3.2.3.2 – 26 pytań, duże nalepki 5.3.1.1.1–5.3.1.1.7, 5.3.1.2, 5.3.1.3, 5.3.1.5, 5.3.1.7.1–5.3.1.7.4, kontener mały, 250 mm, świadectwo dopuszczenia 8.1.2.2, 9.1.2, 9.1.3.1–9.1.3.5, zaświadczenie kierowcy, 7.5.1.1–7.5.1.6, pozostałości, wystające części, zawiasy/uszczelnienia, uszkodzone sztuki przesyłki/1.4.3.1.1 (b)) oraz każde pytanie z każdym pytaniem jego kompetencji w `kompetencje.json`; skrypty `similarity.py` (0,45 i 0,25), `check_near_duplicates.py` (0,60 i 0,40), `check_cross_module_duplicates.py` (0,80 i 0,50) na kopii po poprawkach.
- `similarity.py --threshold 0.45`: main – 9 par, żadna z partią; po poprawkach – te same 9 par (pierwsza wersja moich 0543/0545 dała 0,571 i 0217/0543 0,462 – treści przebudowane). `--threshold 0.25`: main – 174 pary, w tym 10 z partią (największa 0545/0635 = 0,400, 0548/0563 = 0,375 – rzeczywisty duplikat); po poprawkach – 166 par, z partią tylko 0541/0542 = 0,300 (dwie różne nalepki) i 0436/0555 = 0,296 (wystające części vs wady drzwi – różne elementy 7.5.1.2). `check_near_duplicates.py --threshold 0.40` i `check_cross_module_duplicates.py --threshold 0.50` – brak par z partią.
- **0541** vs 0042, 0151 (2.3), 0284 (2.2 – uduszenie), 0355, 0657 (2.1) – brak drugiego pytania o rozpoznanie nalepki 2.2.
- **0542** vs 0004 (klasa 3 = ciecze zapalne – odwrotny kierunek), 0657 (2.1) – nowe ujęcie: rozróżnienie 3 vs 2.1 po cyfrze.
- **0543/0544/0545** vs 0017, 0051, 0053, 0170, 0192, 0194, 0217 (44), 0256, 0298, 0503–0507, 0615, 0616, 0635, 0637, 0653, 0654, 0698, 0752, 0754, 0756 – cyfry 2, 4 i 7 nie mają osobnych pytań (0217 pyta o cały numer 44).
- **0546 nowa** vs 0077, 0099, 0162 (nalepka 9A na sztukach), 0561 – brak pytania o 5.3.1.1.4.
- **0547 nowa** vs 0189 (nalepki na sztuce – 6.1+3), 0564 – brak pytania o 5.3.1.1.5.
- **0548 nowa** vs 0133, 0469, 0527 – brak pytania o 5.3.1.7.3 / kontener mały.
- **0549** vs 0255 (tablica pomarańczowa – wymiary cyfr), 0469 (znak środowiskowy 250 mm) – brak pytania o wymiary dużej nalepki.
- **0550 nowa** – brak pytania o kontrastowe podłoże (5.3.1.1.1).
- **0551 nowa** vs 0239 (zaświadczenie kierowcy), 0566 (ogólnik) – brak pytania o świadectwo dla każdego pojazdu jednostki.
- **0552 nowa** vs 0662 (VIN, pole 3), 0137, 0198 – brak pytania o wygląd świadectwa.
- **0553** vs 0198 (uznawanie przez inne państwa; 9.1.3.4 tylko w źródłach), 0566 – brak pytania o liczenie okresu ważności.
- **0554** vs 0138, 0560 (ogólnie: niezgodność → wstrzymać), 0436 (wystające części), 0202 – brak drugiego pytania o pozostałości niezgodne.
- **0555 nowa** vs 0230, 0436, 0476 (7.5.1.3) – brak pytania o istotne wady (a)–(c).

## Szczegóły – cytaty (dosłownie z Dz.U.) i rozstrzygnięcia

### ADR-B-0541 – POPRAW (02-K02, B; rysunek 2.2) – przeredagowane (#905: OK; strona 945, nie 942/943)
- 5.2.2.2.2 (s. 945, obraz strony), wiersz 2.2: „Gazy niepalne i nietrujące | Butla do gazu: czarny lub biały | Zielone | 2 (czarny lub biały)”. Wiersz 2.1: „Gazy palne | Płomień: czarny lub biały … | Czerwone | 2”. Wiersz 2.3: „Gazy trujące | Czaszka i piszczele: czarny | Białe | 2 (czarny)”. Klucz B ✔. Rysunek `adr-b-0541-label-2-2.svg` zgodny (zielone tło, biała butla, cyfra 2).

### ADR-B-0542 – POPRAW (02-K03, A; rysunek 3) – przeredagowane (#905: OK; strona 945)
- 5.2.2.2.2 (s. 945, obraz strony): „Zagrożenie klasy 3: Materiały zapalne ciekłe | 3 | Płomień: czarny lub biały | Czerwone | 3 (czarny lub biały)”; wzór 2.1 – „Płomień … | Czerwone | 2”; (s. 946) wzór 4.1 – „Płomień: czarny | Białe z siedmioma czerwonymi pionowymi pasami | 4 (czarny)”. 2.2.3.1.1 (s. 165): „Tytuł klasy 3 obejmuje materiały i przedmioty zawierające materiały tej klasy, które: – są ciekłe zgodnie z kryterium podanym w (a) w definicji „materiału ciekłego” w rozdziale 1.2.1 …”. Klucz A ✔.

### ADR-B-0543 – POPRAW (06-K03, A) – przeredagowane
- 5.3.2.3.1 (s. 956): „Numer rozpoznawczy zagrożenia składa się z dwóch lub trzech cyfr. Cyfry te oznaczają następujące zagrożenia: 2 – emisja gazu spowodowana ciśnieniem lub reakcją chemiczną; 3 – zapalność materiałów ciekłych (pary) i gazów lub samonagrzewanie się materiałów ciekłych; 4 – zapalność materiałów stałych lub samonagrzewanie się materiałów stałych; 5 – działanie utleniające (wzmagające palenie) …”. 5.3.2.3.2 (s. 957): „23 gaz palny”. Klucz A ✔.

### ADR-B-0544 – POPRAW (06-K03, B) – przeredagowane
- 5.3.2.3.1 (s. 956): „4 – zapalność materiałów stałych lub samonagrzewanie się materiałów stałych”; „6 – działanie trujące lub ryzyko zakażenia”. Klucz B ✔.

### ADR-B-0545 – POPRAW (06-K03, C) – przeredagowane (#905: OK)
- 5.3.2.3.1 (s. 956): „7 – działanie promieniotwórcze”; „Jeżeli zagrożenie stwarzane przez dany materiał może być w sposób wystarczający określone jedną cyfrą, to po tej cyfrze dodaje się zero.” 5.3.2.3.2 (s. 957): „70 materiał promieniotwórczy”. Klucz C ✔.

### ADR-B-0546 – POPRAW (06-K09, B) – NOWY ELEMENT (= 0562)
- 5.3.1.1.4 (s. 950): „W przypadku materiałów klasy 9 duża nalepka ostrzegawcza powinna odpowiadać wzorowi nalepki nr 9 podanemu w 5.2.2.2.2; nalepki wzór nr 9A nie należy stosować jako dużej nalepki ostrzegawczej.” 5.3.1.2 (s. 951): „Duże nalepki ostrzegawcze powinny być umieszczone na obu bokach i obu czołach kontenera …”. Tabela A (s. 611, obraz strony): UN 3480 – klasa 9, M4, nalepka **9A**. Klucz B ✔.

### ADR-B-0547 – POPRAW (06-K09, A) – NOWY ELEMENT (klucz „komplet nalepek” sprzeczny z 5.3.1.1.5)
- 5.3.1.1.1 (s. 950): „Nalepki te powinny odpowiadać wzorom, których numery podano w kolumnie (5) i odpowiednio w kolumnie (6) tabeli A w dziale 3.2 …”. 5.3.1.1.5 (s. 950): „Kontenery … i pojazdy, zawierające towary należące do więcej niż jednej klasy, mogą nie być zaopatrzone w dużą nalepkę ostrzegawczą dotyczącą zagrożenia dodatkowego, jeżeli zagrożenie to wskazane jest przez inną dużą nalepkę ostrzegawczą dotyczącą zagrożenia dominującego lub dodatkowego.” Tabela A (s. 377): UN 1230 METANOL – 3, FT1, nalepki 3+6.1. Klucz A ✔.

### ADR-B-0548 – POPRAW (06-K09, C) – NOWY ELEMENT (= 0563)
- 5.3.1.7.3 (s. 953): „W przypadku cystern o pojemności nie większej niż 3 m³ oraz w przypadku kontenerów małych, mogą być użyte nalepki ostrzegawcze zgodne z 5.2.2.2. Jeżeli nalepki te nie są widoczne z zewnątrz pojazdu, to duże nalepki ostrzegawcze zgodne z 5.3.1.7.1 powinny być umieszczone na obu bokach i z tyłu pojazdu.” 1.2.1 (s. 37): „Kontener mały oznacza kontener o pojemności wewnętrznej nie większej niż 3 m³.” Klucz C ✔. (Dotychczasowy temat: 5.3.1.1.6 (s. 951) „Duże nalepki ostrzegawcze, które nie dotyczą przewożonych towarów lub ich pozostałości, powinny być zdjęte lub zakryte.” – zostaje w 0563.)

### ADR-B-0549 – POPRAW (06-K09, B) – przeredagowane (#905: OK, „klucz A”; strony 952–953)
- 5.3.1.7.1 (s. 952): „Duża nalepka ostrzegawcza powinna mieć kształt kwadratu ustawionego pod kątem 45° (kształt rombu). Minimalne wymiary powinny wynosić 250 mm x 250 mm (do krawędzi nalepki). Linia wewnątrz rombu … 12,5 mm.” (s. 953): „… numery te powinny być zapisane cyframi o wysokości nie mniejszej niż 25 mm.” 5.3.1.7.4 (s. 953): „… w przypadku klas 1 i 7 … wymiary każdego boku nalepki mogą być zmniejszone do 100 mm.” Klucz B ✔.

### ADR-B-0550 – POPRAW (06-K09, A) – NOWY ELEMENT (≈ 0133)
- 5.3.1.1.1 (s. 950): „Duże nalepki ostrzegawcze powinny być umieszczone na podłożu o kontrastowym kolorze lub otoczone linią przerywaną lub ciągłą. Duże nalepki ostrzegawcze powinny być odporne na warunki atmosferyczne i zapewniać trwałość oznakowania podczas całego przewozu.” 5.3.1.7.1 (s. 952–953): „Symbol i linia wewnątrz dużej nalepki ostrzegawczej powinny odpowiadać pod względem koloru wzorowi nalepki wymaganemu dla klasy …”. Klucz A ✔. (Dotychczasowy temat – 5.3.1.3 (s. 951): „Jeżeli duże nalepki umieszczone na kontenerach … nie są widoczne z zewnątrz przewożącego je pojazdu, to takie same duże nalepki ostrzegawcze powinny być umieszczone na obu bokach i z tyłu tego pojazdu.” – jest w 0133.)

### ADR-B-0551 – POPRAW (08-K08, C) – NOWY ELEMENT (≈ 0566)
- 8.1.2.2 (s. 1324): „W przypadkach, gdy przepisy ADR wymagają sporządzenia następujących dokumentów, powinny być one również przewożone w kabinie kierowcy jednostki transportowej: (a) świadectwo dopuszczenia określone w 9.1.3, dla każdej jednostki transportowej lub każdego wchodzącego w jej skład pojazdu”. Klucz C ✔.

### ADR-B-0552 – POPRAW (08-K08, B) – NOWY ELEMENT (= 0137)
- 9.1.3.3 (s. 1344): „Wymiary świadectwa wynoszą 210 x 297 mm (format A4). Tekst może być umieszczony na obu stronach. Świadectwo powinno być koloru białego, z różowym paskiem biegnącym po przekątnej.” 8.2.2.8.3 (s. 1331): „[Zaświadczenie] Powinno być wykonane z tworzywa sztucznego, a jego wymiary powinny być zgodne z ISO 7810:2003 ID-1.” Klucz B ✔. (Dotychczasowy temat – 9.1.2 UWAGA (s. 1343) i 9.1.3.1 – jest w 0137.)

### ADR-B-0553 – POPRAW (08-K08, C) – przeredagowane (#905: OK; źródło 9.1.3.1 → 9.1.3.4)
- 9.1.3.4 (s. 1344): „Ważność świadectwa dopuszczenia powinna wygasać nie później niż po upływie jednego roku od daty badania technicznego poprzedzającego jego wystawienie. Jednakże następny okres ważności świadectwa powinien być liczony od daty wygaśnięcia jego ważności, pod warunkiem, że badanie techniczne zostało przeprowadzone w ciągu jednego miesiąca przed lub po tej dacie. Po upływie terminu ważności świadectwa dopuszczenia, pojazd nie powinien być używany do przewozu towarów niebezpiecznych, do czasu wystawienia dla tego pojazdu nowego świadectwa dopuszczenia.” Klucz C ✔.

### ADR-B-0554 – POPRAW (09-K08, A) – przeredagowane (#905: OK; C 81 zn.)
- 7.5.1.2 (s. 1304): „Jednostka transportowa cargo powinna być sprawdzona w celu zapewnienia, że jest ona konstrukcyjnie zdatna do użytku i nie zawiera żadnych pozostałości niezgodnych z przewożonym towarem …”; „… to załadunek nie powinien się odbyć, jeżeli: … oględziny pojazdu … wskazują, że … pojazd … nie spełniają wymagań obowiązujących przepisów.” Klucz A ✔.

### ADR-B-0555 – POPRAW (09-K08, B) – NOWY ELEMENT (= 0020/0054/0078/0517/0584)
- 7.5.1.2 (s. 1304): „Konstrukcyjnie zdatna do użytku jednostka transportowa cargo jest jednostką transportową cargo, która nie ma poważnych wad elementów konstrukcyjnych. … Za istotne wady uważa się: … (c) zatarte, skręcone, złamane, brakujące lub niedziałające w inny sposób zawiasy drzwi, uszczelnienia drzwi i okucia.” Klucz B ✔.

## Wskaźniki

- „Poprawna = jedyna najdłuższa”: **29/780 = 3,72% – bez zmian** (w partii żadne pytanie nie było i nie jest jedyną najdłuższą), maksimum działu **6,74%** – bez zmian. `docs/POKRYCIE-KURSU.md` i `podstawowy/README.md` – bez zmian liczb; `docs/STAN-KONCOWY-…` – zaległe 85/780 = 10,90% i 15,22% → 29/780 = 3,72% i 6,74%.
- „Poprawna = jedyna najkrótsza”: **133 → 129/780**; ADR-B-08 26,4% → **22,6%**, ADR-B-09 21,0% → **17,7%**, ADR-B-02 (12,4%) i ADR-B-06 (24,2%) bez zmian; maksimum działu 26,4% (bez zmian); wszystkie działy ≤ 38%.
- 15 nowych wyjaśnień: 4–5 zdań, 386–498 znaków, maks. 28 słów w zdaniu, na końcu „Podstawa: ADR …”; opcje 38–78 znaków; bez słów absolutnych, średników i kropek w opcjach; klucz nigdzie nie jest jedyną najdłuższą ani jedyną najkrótszą.

## Egzaminy, kolejki, snapshoty (pułapki CI)

- Egzaminy próbne – w `questions`: **0544 – wariant-002/klucz-002; 0554 – wariant-003/klucz-003; 0547 – wariant-005/klucz-005**. Na listach `excluded_question_ids`: wariant-003 – 0544; wariant-004 – 0544, 0554; wariant-005 – 0544, 0554 – **nie zmieniać**. Pozostałe pliki egzaminów – tylko SHA.
- `review/specialist/KOLEJKA-PRIORYTETOWA-4X44.json` zawiera **0541, 0542** („question” + „legal_basis”); 4X40 – żadnego ID z partii (tylko SHA).
- Snapshoty: `review/sequential/` i `review/legal-clauses/` – pliki **541-542.json**, **543-545.json**, **546-560.json** (w 546-560 tylko 0546–0555); clause, answer_review A/B/C, notes_on_conditions ≥ 25 zn.
- Ledger `review/legal-polish/stage4w4-literal-verification-ledger-0001-0609.json`: `source_references` z nowych sources – zmienia się **13** (wszystkie poza 0544 i 0554).
- Rejestry `REJESTR-AKTUALNY-0001-0765.md` i `-0001-0780.md`: po **15 wierszy**.
- SHA banku 73aa25f2… występuje w **38 plikach** poza historycznymi raportami `review/literal-pl/` i poza `tests/test_literal_review_0541_0555.py`: docs/POKRYCIE-KURSU.md, podstawowy/README.md, review/README.md, podstawowy/raporty/etap-4x135-wykluczenia-proby.json, review/specialist: INSTRUKCJA-RECENZJI.md, PRZEKAZANIE-ETAP4.md, PAKIET-0628-MANIFEST.json, PAKIET-0780-MANIFEST.json, KOLEJKA-PRIORYTETOWA-4X40.json, KOLEJKA-PRIORYTETOWA-4X44.json, REJESTR-AKTUALNY-0001-0765.md, REJESTR-AKTUALNY-0001-0780.md, 10 plików egzaminów, tests/test_literal_review_0301_0315 … 0526_0540 (16 plików; w 0511_0525 i 0526_0540 zmienia się tylko EXPECTED_BANK_SHA – FIRST_PASS_BANK_SHA f732aa35…/e0c67175… zostaje; w 0301_0315 element zbioru dopuszczalnych blobów). Do tego zaległość: **f732aa35… → nowy** w docs/STAN-KONCOWY-BANKU-ADR-PODSTAWOWY-2026-11-03.md (2×) + wskaźniki w tej tabeli.
- `tests/test_literal_review_0541_0555.py`: EXPECTED_BANK_SHA = 73aa25f2… → **dwie stałe**: FIRST_PASS_BANK_SHA = 73aa25f2… (asercja manifestu `bank_blob_sha`), EXPECTED_BANK_SHA = nowy (bank); `test_report_and_bank_unchanged` → `test_report_and_bank_after_second_pass`; docstring; `EXPECTED_PAGES` i `gazette_pages` w .json – poprawione strony; nowy `test_second_pass_artifacts_and_bank_sha`. Licznik 240/225, counts 7/8/0 i bank_changed = false zostają.
- Oczekiwany SHA banku: **73aa25f2ae5fed6f40b1948dfb917f082c08b58e → 7f2be64ba60fef44ab136bdf59cbb4bdd949c172**.

## Test na kopii repo

`test_p37.sh` – git worktree `/tmp/b37` z main e46d36eaf (bez commitów i pushu): `tools/apply_poprawki.py` z dopisanym `POPRAWKI-KONTROLA2-0541-0555.jsonl` → „Changed (15): ADR-B-0541 … ADR-B-0555”, blob **7f2be64b…**; synchronizacja (`sync_p37_test.py`: snapshoty i legal-clauses 15 ID, ledger 13, egzaminy 002/003/005, kolejka 4X44, rejestry 2 × 15 wierszy, SHA w 38 plikach + STAN-KONCOWY, test 0541_0555, PARTIA-0541-0555.json/.md); wszystkie **14 skryptów CI** – kod 0; `python3 -m unittest discover -s tests` – **Ran 223 tests – OK**.