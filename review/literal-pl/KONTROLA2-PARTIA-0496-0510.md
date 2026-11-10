# Kontrola druga – partia ADR-B-0496–0510 (porównanie dosłowne z polskim tekstem ADR 2025)

Data: 2026-11-10, ok. 04:40 (czas polski, CET).
Przedmiot: pierwsza kontrola ChatGPT (PR #899, scalony; main **f90d105a4**; `review/literal-pl/PARTIA-0496-0510.md` + `.json` + `tests/test_literal_review_0496_0510.py`, wynik 4 OK / 11 POPRAW / 0 BLOKUJ) oraz rekordy 0496–0510 na main (bank blob **f2cea3f4…**, 780 pytań; #899 banku nie zmienia).
Źródło: Dz.U. 2025 poz. 642 (skany PDF), OCR tesseract `-l pol`; strony wg nagłówka „Dziennik Ustaw — NNN —”. Na **obrazie strony PDF** sprawdzone: s. 290 (2.2.9.1.13 – „100 °C”, „240 °C”). Pozostałe strony wg nagłówków OCR: s. 10 (art. 1 (a) Umowy – „pojazd”), s. 129 (2.2.1.1.5), s. 187 (2.2.43.1.1–2.2.43.1.3), s. 273 (2.2.9.1.2, 2.2.9.1.4, 2.2.9.1.6), s. 275 (2.2.9.1.7.2), s. 305 (3.1.2.8.1–3.1.2.8.1.2), s. 463 (tabela A UN 2211), s. 621 (tabela A UN 3551/3552), s. 955 (5.3.2.2.2), s. 956 (5.3.2.3.1), s. 957 (30, 336, 339), s. 959 (99), s. 961 (5.4.1.1.1 (a), (b)), s. 1325 (8.1.5.2). Sprostowanie poz. 1575 dotyczy w tej partii tylko pisowni nazwy UN 3551 („organiczny”) – bez wpływu na pytania.
Status: kontrola robocza. **Żadne pytanie nie jest oznaczone jako zweryfikowane**; wszystkie pozostają `needs_review`.

## Podsumowanie

- Werdykty kontroli drugiej: **OK 0, POPRAW 15, BLOKUJ 0** (#899: 4 OK – 0496, 0498, 0499, 0500 nie są OK).
- **NIEJEDNOZNACZNY KLUCZ – 0505**: „numer zagrożenia zawiera cyfrę 9. Które zagrożenie ta cyfra **ogólnie** sygnalizuje?” → „ryzyko samorzutnej gwałtownej reakcji”. Według 5.3.2.3.1 (s. 956) numery **90 i 99** mają znaczenie specjalne (5.3.2.3.2: 90 – materiał zagrażający środowisku, różne materiały niebezpieczne; 99 – różne materiały niebezpieczne w podwyższonej temperaturze), czyli „9” na początku numeru wskazuje klasę 9, a nie samorzutną reakcję. Dystraktor „klasa 9” byłby wtedy częściowo prawdziwy. Przeredagowane na numer **339** (końcowa 9) z uwagą do cyfry 9 (wybuch, rozkład, polimeryzacja). #899 tego nie zauważa.
- **BŁĘDNE STRONY Dz.U. w #899 (6 pytań)**: 0503–0506 – 5.3.2.3.1 (lista cyfr 2–9, uwaga, „zero”, „X”) stoi na **s. 956**, nie 957 (na 957 są dopiero numery 22–423 z 5.3.2.3.2); 0507 – zdanie „Numer rozpoznawczy zagrożenia powinien znajdować się w górnej części tablicy, a numer UN w jej części dolnej” jest na **s. 955**, nie 956; 0508 – 5.4.1.1.1 (a) „numer UN poprzedzony literami „UN”” jest na **s. 961**, nie 962.
- **Raport #899 wewnętrznie sprzeczny**: 0496 w tabeli „OK”, w sekcji szczegółowej „POPRAW” (manifest: OK).
- **Przeoczone duplikaty**: 0507 = **0016** (UN w dolnej części) i **0190** (górne pole = numer rozpoznawczy zagrożenia) – ten sam fakt, tylko w scenariuszu; 0508 = **0577** (brak liter „UN” → dopisać przed numerem) i **0037**; 0510 = **0155** (4.3 – nie używać wody) i **0006** (4.3 – w kontakcie z wodą gaz palny); 0509 ≈ **0023** (klin dla każdego pojazdu jednostki, dobrany do masy i średnicy koła).
- **Poza kompetencją kierowcy**: 0500, 0501, 0502 – warunki konstrukcyjne producenta baterii sodowo-jonowych (badania typu 38.3, zabezpieczenie przed zwarciem zewnętrznym, ochrona przed prądem wstecznym – 2.2.9.1.7.2 (a), (c), (d)). Trzy szablonowe pytania o kolejne litery jednego punktu; kierowca tego nie sprawdza. W 0501 opcje B i C nie są „warunkami” (pytanie „którego warunku nie spełnia?”).
- **7 pytań → nowy element z tej samej kompetencji, niecysternowy**:
  - 0500 (02-K13) → próg materiałów o podwyższonej temperaturze: ciecz 100 °C, materiał stały 240 °C (2.2.9.1.13; s. 290, obraz strony);
  - 0501 (02-K13) → azbest = M1, materiał groźny przy wdychaniu drobnego pyłu (2.2.9.1.2, 2.2.9.1.4; s. 273);
  - 0502 (02-K13) → M3 – materiały wydzielające pary palne: polimery z cieczą zapalną o temperaturze zapłonu ≤ 55 °C, UN 2211 kulki polimeryczne ekspandujące (2.2.9.1.2, 2.2.9.1.6; s. 273; tabela A s. 463);
  - 0507 (06-K03) → zero dopisywane po jednej cyfrze („80”) (5.3.2.3.1; s. 956) – w banku brak pytania o tę regułę;
  - 0508 (13-K01) → mieszanina z nazwą I.N.O. i przepisem 274: najwyżej dwa składniki decydujące o zagrożeniu, bez nazwy handlowej (3.1.2.8.1.2, 3.1.2.8.1.1; s. 305) – 0226 pyta tylko o nawias i nazwę chemiczną;
  - 0509 (08-K04) → naczepa jest pojazdem (art. 1 (a) Umowy ADR, s. 10) i potrzebuje własnego klina z 8.1.5.2 (s. 1325);
  - 0510 (02-K06) → w tym samym podtemacie, ale nowy element 2.2.43.1.3: gazy z 4.3 tworzą z powietrzem mieszaniny, które zapalają się łatwo od zwykłych źródeł zapłonu, także od niezabezpieczonych źródeł światła (s. 187).
- **8 pytań przeredagowanych w tym samym podtemacie**: 0496 (1.3), 0497 (1.5), 0498 (1.6 + uwaga – wybuch pojedynczego przedmiotu), 0499 (UN 3551/3552), 0503 (cyfra 3, numer 30), 0504 (cyfra 5 – ocena błędnego przekonania), 0505 (cyfra 9 → numer 339), 0506 (cyfra 6 w numerze 336 – ocena błędnego przekonania). Seria 0503–0506 + 0543–0545 („cyfra N oznacza…”) zróżnicowana formą.
- **Żaden zamiennik nie jest cysternowy** (0510 – zamknięte nadwozie furgonu; 0507 – numer 80 bez wskazania cysterny).
- Wszędzie ta sama litera klucza, ten sam `module_id`, `image` = null; przypisania w `kompetencje.json` bez zmian (02-K01 = 7, 02-K06 = 8, 02-K13 = 8, 06-K03 = 11, 08-K04 = **6**, 13-K01 = 8; minimum kompetencji teoretycznych = 6).
- **Wady formy starych wersji**: opcje > 80 zn. – 0497 C (84), 0501 B (105), 0502 B (88), 0503 A (97), 0504 A (93), 0505 A (92), 0506 A (91), 0507 A (104), 0509 A (83), 0510 A/B/C (85/93/87); średniki – 0497 A/B/C, 0499 C, 0500 A/B/C, 0501 B, 0502 A/B/C, 0503 C; kropka na końcu – 0496 B; słowa absolutne – 0496 A „zawsze”, 0497 B „każdy … automatycznie”, 0499 A/B „zawsze”, A „niezależnie”, 0500 A „zawsze”, B „wyłącznie”, 0501 C „tylko”, 0502 B „wyłącznie”; klucz jedyną najdłuższą – 0497; klucz jedyną najkrótszą – 0499, 0500, 0508, 0509; klucz powtarza treść – 0504 B „Cyfra 5 oznacza…”, 0505 C, 0506 C; „np.” w opcji 0503 A i w wyjaśnieniu 0502; „zwykle oznacza” (0504); 0498 „skrajnie mało wrażliwych” (ADR: „skrajnie niewrażliwe”); 0496 C „ograniczonym ryzykiem wybuchu/rozrzutu” (ADR: „małe zagrożenie wybuchem lub rozrzutem”); 0509 – każda opcja „Sprawdzić, czy…” (każdą rzecz da się sprawdzić – klucz nieostry); 0507 C absurd (linia pionowa); 0510 B absurd (klasa 8).

## Błędy / różnice względem raportu ChatGPT (#899)

1. **0505 – niejednoznaczny klucz** (90/99) – wyżej.
2. **Strony Dz.U.**: 0503–0506 → 956 (nie 957), 0507 → 955 (nie 956), 0508 → 961 (nie 962). Test `tests/test_literal_review_0496_0510.py` utrwala błędne strony (EXPECTED_PAGES) – raportu #899 i testu nie przepisujemy, ale sekcja „Kontrola druga” w .md ma to odnotować.
3. **0496 – sprzeczność** OK (tabela, manifest) / POPRAW (sekcja). Rzeczywiście: POPRAW (A „zawsze”, B z kropką, C „ograniczonym … wybuchu/rozrzutu”, średnik w wyjaśnieniu).
4. **0498, 0499, 0500 nie są OK** (0498 – „skrajnie mało wrażliwych”, nieczytelne „jakie zagrożenie masowe”, dystraktor „utleniające”; 0499 – „zawsze”, „niezależnie”, średnik, klucz jedyną najkrótszą; 0500 – warunek producenta, „zawsze”, „wyłącznie”, średniki, klucz jedyną najkrótszą).
5. **Przeoczone duplikaty**: 0507 = 0016/0190 (#899 widzi tylko 0298), 0508 = 0577/0037, 0510 = 0155/0006, 0509 ≈ 0023.
6. **Zakres kursu**: 0500–0502 to wymagania konstrukcyjne dla producenta – #899 każe tylko skrócić opcje.
7. **Test znowu bez FIRST_PASS_BANK_SHA** (trzeci raz z rzędu, mimo wyraźnego polecenia partii 33 pkt c): `tests/test_literal_review_0496_0510.py` ma jedną stałą EXPECTED_BANK_SHA = f2cea3f4… używaną w dwóch asercjach manifestu (`test_report_scope_counts_and_printed_page_headers`, `test_no_question_bank_or_exam_files_are_changed_by_report`) i w teście banku. Przy wdrożeniu: FIRST_PASS_BANK_SHA = f2cea3f4… (obie asercje manifestu), EXPECTED_BANK_SHA = nowy SHA.
8. **Słusznie w #899**: klucze wszystkich 15 pytań merytorycznie poprawne (poza niejednoznacznością 0505); strony 129, 275, 1325, 187; długości opcji > 80 zn. (0497, 0501, 0502, 0503–0507, 0509, 0510); 0508 – klucz jedyną najkrótszą; seria 0503–0506 szablonowa; similarity.py: przy 0,45 – 2 pary (0505/0545 = 0,538, 0217/0503 = 0,462), przy 0,25 – 17 par – zgodne z moim uruchomieniem na main; licznik 285 → 270.

## Duplikaty – sprawdzenie w całym banku (780) i między sobą

Przeszukano cały bank po temacie (podklasy 1.1–1.6, kody klasyfikacyjne, baterie sodowo-/litowo-jonowe, UN 3551/3552/3480, 38.3, azbest, PCB/dioksyny, pary palne, polimery/UN 2211, podwyższona temperatura/100 °C/240 °C, suchy lód, cyfry 2–9 numeru rozpoznawczego, X, zero, 30/33/336/339/80/88/90/99, górne/dolne pole tablicy, litery „UN”, nazwa techniczna, I.N.O., przepis 274, kliny/naczepa/przyczepa, 4.3/woda/źródła zapłonu/iskry/lampy) oraz skryptami `check_near_duplicates.py` (0,60 i 0,40), `check_cross_module_duplicates.py` (0,80 i 0,50), `similarity.py` (0,45; dodatkowo 0,25) na kopii po poprawkach.
- `similarity.py --threshold 0.25` po poprawkach: 0504/0506 = 0,368 (cyfra 5 w 50 vs cyfra 6 w 336 – inne cyfry), 0217/0504 = 0,294, 0217/0506 = 0,294 (44 – materiał stopiony), 0503/0543 = 0,263 (cyfra 3 vs 2), 0504/0635 i 0506/0635 = 0,263 (powtórzenie cyfry). Przy 0,45 – brak par z partią (stare 0505/0545 i 0217/0503 zniknęły). `check_near_duplicates.py --threshold 0.40` – brak par z partią; `check_cross_module_duplicates.py --threshold 0.50` – brak. (Pierwsze wersje: 0505/0507 = 0,636 i 0495/0496 = 0,417 – treści przeredagowane, pary zniknęły.)
- **0496–0498** (1.3, 1.5, 1.6) vs 0126 (1.1), 0150 (1.1/1.4), 0495 (1.2), 0316 (litera grupy zgodności) – inne podklasy.
- **0499** (3551 vs 3552) vs 0162 (nalepka 9A dla UN 3551), 0673 (litowo-jonowe 3480/3481) – inny element.
- **0500 nowa** (progi 100/240 °C) vs 0288 (olej podgrzany powyżej temperatury zapłonu → klasa 3), 0356 (znak – instrukcje pisemne), 0654 (numer 99), 0217 (44) – inny element. **0501 nowa** (azbest – M1) – w banku brak. **0502 nowa** (M3 – UN 2211) – w banku brak; 0315 (PCB – M2) – inna grupa.
- **0503–0506** vs 0543 (2), 0544 (4), 0545 (7), 0194 (88), 0256 (80/X80), 0217 (44), 0635 (powtórzenie), 0653 (886), 0654 (99), 0051 – inne cyfry/numery. **0507 nowa** (zero) – w banku brak pytania o tę regułę.
- **0508 nowa** (najwyżej dwa składniki, bez nazwy handlowej) vs 0226 (nawias + nazwa chemiczna), 0598 (brak nazwy przewozowej) – inny element 3.1.2.8.
- **0509 nowa** (naczepa = pojazd) vs 0023 (klin dla każdego pojazdu – pamięciowo), 0699 (rozmiar klina), 0251 (każda nalepka), 0352 (przyczepa bez hamulców – 8.3.7), 0761 (1.1.3.6) – inny element.
- **0510 nowa** (2.2.43.1.3 – zapłon od zwykłych źródeł) vs 0006 (definicja), 0155 (nie używać wody), 0153, 0265, 0269, 0674–0676 (grupy pakowania), ogólne o źródłach zapłonu 0102, 0738, 0663 (bez klasy 4.3) – inny element.

## Ustalenia dla poszczególnych pytań (cytaty, strony Dz.U., klucze)

### ADR-B-0496 – POPRAW (02-K01, C) – przeredagowane (#899: OK/POPRAW – sprzecznie)
- 2.2.1.1.5 (s. 129): „Podklasa 1.3 Materiały i przedmioty stwarzające zagrożenie pożarem i małe zagrożenie wybuchem lub rozrzutem lub oba te zagrożenia, ale które nie stwarzają zagrożenia wybuchem masowym: (a) przy spalaniu których wydziela się znaczne ciepło promieniowania; lub (b) które zapalają się jeden od drugiego i wywołują mały wybuch lub rozrzut lub oba te efekty razem.” Kod 1.3G występuje w tabeli A. Klucz C ✔.

### ADR-B-0497 – POPRAW (02-K01, C) – przeredagowane
- 2.2.1.1.5 (s. 129): „Podklasa 1.5 Materiały bardzo mało wrażliwe stwarzające zagrożenie wybuchem masowym, które są na tyle niewrażliwe, że istnieje małe prawdopodobieństwo ich zainicjowania lub przejścia od palenia do detonacji w normalnych warunkach przewozu.” Klucz C ✔.

### ADR-B-0498 – POPRAW (02-K01, A) – przeredagowane (#899: OK)
- 2.2.1.1.5 (s. 129): „Podklasa 1.6 Przedmioty skrajnie niewrażliwe, które nie stwarzają zagrożenia wybuchem masowym. … UWAGA: Zagrożenie ze strony przedmiotów zaklasyfikowanych do podklasy 1.6 ograniczone jest do wybuchu pojedynczego przedmiotu.” Klucz A ✔.

### ADR-B-0499 – POPRAW (02-K13, C) – przeredagowane (#899: OK)
- 2.2.9.1.7.2 (s. 275): „… powinny mieć przypisane numery UN 3551 lub 3552, stosownie do sytuacji.” Tabela A (s. 621): UN 3551 „BATERIE SODOWO-JONOWE (AKUMULATORY SODOWO-JONOWE) zawierające elektrolit organiczny”; UN 3552 „… W URZĄDZENIACH lub … ZAPAKOWANE Z URZĄDZENIAMI zawierające elektrolit organiczny”. Klucz C ✔.

### ADR-B-0500 – POPRAW (02-K13, C) – NOWY ELEMENT (#899: OK; warunek producenta)
- 2.2.9.1.13 (s. 290, obraz strony): „Materiały o podwyższonej temperaturze obejmują materiały, które są przewożone lub nadawane do przewozu w stanie ciekłym w temperaturze 100 °C lub wyższej … Obejmują one również materiały stałe, które są przewożone lub nadawane do przewozu w temperaturze 240 °C lub wyższej. UWAGA: Materiały o podwyższonej temperaturze mogą być zaklasyfikowane do klasy 9 tylko wówczas, jeżeli nie spełniają kryteriów żadnej innej klasy.” Klucz C ✔.

### ADR-B-0501 – POPRAW (02-K13, A) – NOWY ELEMENT
- 2.2.9.1.2 (s. 273): „M1 Materiały, które wdychane w postaci drobnego pyłu, mogą zagrażać zdrowiu; M2 Materiały i przedmioty, które w razie pożaru mogą tworzyć dioksyny; M3 Materiały wydzielające pary palne”. 2.2.9.1.4 (s. 273): „… obejmują azbest i zawierające go mieszaniny.” Klucz A ✔.

### ADR-B-0502 – POPRAW (02-K13, C) – NOWY ELEMENT
- 2.2.9.1.6 (s. 273): „Materiały wydzielające pary palne obejmują polimery zawierające materiały zapalne ciekłe o temperaturze zapłonu nieprzekraczającej 55 °C.” 2.2.9.1.2: „M6 Materiał zagrażające środowisku wodnemu, ciekły; M7 … stały”. Tabela A (s. 463): „2211 KULKI POLIMERYCZNE EKSPANDUJĄCE wydzielające pary palne | 9 | M3”. Klucz C ✔.

### ADR-B-0503 – POPRAW (06-K03, C) – przeredagowane (strona 956, nie 957)
- 5.3.2.3.1 (s. 956): „3 zapalność materiałów ciekłych (pary) i gazów lub samonagrzewanie się materiałów ciekłych; 4 zapalność materiałów stałych lub samonagrzewanie się materiałów stałych; … 8 działanie żrące”. 5.3.2.3.2 (s. 957): „30 materiał zapalny ciekły (temperatura zapłonu od 23 °C do 60 °C włącznie), lub … lub materiał samonagrzewający się ciekły”. Klucz C ✔.

### ADR-B-0504 – POPRAW (06-K03, B) – przeredagowane (strona 956)
- 5.3.2.3.1 (s. 956): „2 emisja gazu spowodowana ciśnieniem lub reakcją chemiczną; … 5 działanie utleniające (wzmagające palenie); … 9 ryzyko samorzutnej i gwałtownej reakcji”. Klucz B ✔.

### ADR-B-0505 – POPRAW (06-K03, C) – NIEJEDNOZNACZNY KLUCZ, przeredagowane (strona 956)
- 5.3.2.3.1 (s. 956): „9 ryzyko samorzutnej i gwałtownej reakcji. UWAGA: Ryzyko samorzutnej i gwałtownej reakcji określone cyfrą 9 oznacza możliwość wystąpienia wybuchu, rozkładu lub polimeryzacji, z wydzieleniem znacznej ilości ciepła, gazów palnych i/lub trujących … Następujące zestawienia cyfr mają znaczenie specjalne: … 90 i 99”. 5.3.2.3.2 (s. 957): „339 materiał łatwo zapalny ciekły, który może samorzutnie powodować gwałtowną reakcję”. Klucz C ✔.

### ADR-B-0506 – POPRAW (06-K03, C) – przeredagowane (strona 956)
- 5.3.2.3.1 (s. 956): „6 działanie trujące lub ryzyko zakażenia … Powtórzenie cyfry wskazuje na nasilenie oznaczonego tą cyfrą zagrożenia.” 5.3.2.3.2 (s. 957): „336 materiał łatwo zapalny ciekły trujący”. Klucz C ✔.

### ADR-B-0507 – POPRAW (06-K03, B) – NOWY ELEMENT (duplikat 0016/0190; strona 955, nie 956)
- 5.3.2.3.1 (s. 956): „Numer rozpoznawczy zagrożenia składa się z dwóch lub trzech cyfr. … Jeżeli zagrożenie stwarzane przez dany materiał może być w sposób wystarczający określone jedną cyfrą, to po tej cyfrze dodaje się zero.” 5.3.2.3.2 (s. 959): „99 różne materiały niebezpieczne przewożone w podwyższonej temperaturze”. Klucz B ✔.

### ADR-B-0508 – POPRAW (13-K01, A) – NOWY ELEMENT (duplikat 0577/0037; strona 961, nie 962)
- 3.1.2.8.1.2 (s. 305): „Jeżeli mieszanina towarów niebezpiecznych … opisane są za pomocą jednej z nazw „ogólnych” lub „I.N.O.”, dla której ma zastosowanie przepis szczególny 274 …, to należy podać nazwy najwyżej dwóch składników decydujących o zagrożeniu (zagrożeniach) stwarzanych przez taką mieszaninę … Jeżeli sztuka przesyłki zawierająca mieszaninę oznakowana jest nalepką ostrzegawczą wskazującą zagrożenie dodatkowe, to jedna z dwóch nazw technicznych umieszczonych w nawiasach powinna być nazwą składnika powodującego konieczność stosowania tej nalepki.” 3.1.2.8.1.1 (s. 305): „Nie powinny być używane do tego celu nazwy handlowe.” Klucz A ✔.

### ADR-B-0509 – POPRAW (08-K04, C) – NOWY ELEMENT (≈ 0023; kompetencja = 6)
- 8.1.5.2 (s. 1325): „klin pod koła, dla każdego pojazdu, o odpowiednim rozmiarze w stosunku do dopuszczalnej masy całkowitej pojazdu oraz średnicy jego kół”. Art. 1 (a) Umowy ADR (s. 10): „określenie „pojazd” oznacza pojazdy samochodowe, pojazdy członowe, przyczepy i naczepy”. Klucz C ✔.

### ADR-B-0510 – POPRAW (02-K06, A) – przeredagowane, nowy element 2.2.43.1.3 (duplikat 0155/0006)
- 2.2.43.1.1 (s. 187): „Tytuł klasy 4.3 obejmuje materiały, które reagując z wodą wydzielają gazy palne mogące tworzyć z powietrzem mieszaniny wybuchowe”. 2.2.43.1.3 (s. 187): „Mieszaniny takie zapalają się łatwo od wszystkich zwykłych źródeł zapłonu, np. od otwartego płomienia, narzędzi iskrzących lub niezabezpieczonych źródeł światła. Wytworzona fala detonacyjna może zagrozić ludziom i środowisku naturalnemu.” Klucz A ✔.

## Wskaźniki

- „Poprawna = jedyna najdłuższa”: **32/780 = 4,10% → 31/780 = 3,97%**, maksimum działu **7,87% → 6,74%** (ADR-B-02: 7/89 → 6/89) – **zmienić** linie w `docs/POKRYCIE-KURSU.md`, `podstawowy/README.md` i `review/specialist/PAKIET-ZAMKNIECIE-0780.md`.
- „Poprawna = jedyna najkrótsza”: **158 → 149/780**; ADR-B-02 20,2% → **12,4%**, ADR-B-08 28,3% → **26,4%**, ADR-B-13 27,8% → **25,9%**; ADR-B-06 bez zmian (24,2%); maksimum działu 31,5% (bez zmian); wszystkie działy ≤ 38%.
- Wszystkie 15 wyjaśnień: 4–5 zdań, 368–538 znaków, maks. 30 słów w zdaniu, na końcu „Podstawa: ADR …”; opcje 56–74 znaki; bez słów absolutnych i średników w opcjach; klucz nigdzie nie jest jedyną najdłuższą ani jedyną najkrótszą.

## Egzaminy, kolejki, snapshoty (pułapki CI)

- Egzaminy próbne – w `questions`: **0509 – wariant-002/klucz-002, 0503 – wariant-005/klucz-005**. Na listach `excluded_question_ids`: 0509 (003, 004, 005) – tych list **nie zmieniać**. Pozostałe pliki egzaminów – tylko SHA.
- `review/specialist/KOLEJKA-PRIORYTETOWA-4X40.json` zawiera **0497, 0501, 0508, 0510**, `4X44` – **0496, 0498** („question” + „legal_basis”).
- Snapshoty: `review/sequential/` i `review/legal-clauses/` – pliki **495-502.json** (0496–0502), **503-506.json** (0503–0506), **507-509.json** (0507–0509), **510-512.json** (0510); clause, answer_review A/B/C, notes_on_conditions ≥ 25 zn.
- Ledger `review/legal-polish/stage4w4-literal-verification-ledger-0001-0609.json`: `source_references` z nowych sources (zmienia się 14: wszystkie poza 0504, gdzie zostaje „ADR 2025, 5.3.2.3.1”).
- Rejestry `REJESTR-AKTUALNY-0001-0765.md` i `-0001-0780.md`: po 15 wierszy.
- SHA banku f2cea3f4… występuje w **37 plikach** poza historycznymi raportami `review/literal-pl/`: **36 zamienianych wprost** (docs/POKRYCIE-KURSU.md, docs/STAN-KONCOWY-…, podstawowy/README.md, review/README.md, podstawowy/raporty/etap-4x135-wykluczenia-proby.json, 8 plików review/specialist, 10 plików egzaminów, tests/test_literal_review_0301_0315 … 0481_0495 (13; w 0481_0495 tylko EXPECTED_BANK_SHA – FIRST_PASS_BANK_SHA = ba829d36… zostaje)) + `tests/test_literal_review_0496_0510.py` – **specjalnie** (FIRST_PASS_BANK_SHA / EXPECTED_BANK_SHA, rename testu banku, docstring).
- Oczekiwany SHA banku: **f2cea3f46167e3f99d4c5c7b91658744eba1d8c7 → f732aa354f959e2ba17bf870d901d2fe51aa0426**.

## Test na kopii repo

`test_p34.sh` (kopia /tmp/b34 z main **f90d105a4** = po scaleniu #899, bez commitów i pushu): `apply_poprawki.py` → „Changed (15): ADR-B-0496 … ADR-B-0510”, blob **f732aa354f959e2ba17bf870d901d2fe51aa0426**; po synchronizacji (`sync_p34_test.py`; razem 49 zmienionych plików, w tym bank i `tools/apply_poprawki.py`, + nowy POPRAWKI) wszystkie 14 skryptów CI = 0 i `python3 -m unittest discover -s tests` – **212 testów OK**.

## Licznik

Po wdrożeniu partii 34 (obie kontrole 0496–0510): **270 pytań bez porównania dosłownego po obu kontrolach** (0511–0780); kontrola pierwsza partii 35 (0511–0525): 270 → 255.

## Do zapamiętania na kolejne partie
- 06-K03 (tablice): po partii 34 cyfry 2–9 mają po jednym pytaniu (0543, 0503, 0544, 0504, 0506, 0545, 0505 + 8 w 0194/0256), zero – 0507, X – 0017/0170/0256/0615/0698/0752, powtórzenie – 0635/0051 – kolejne pytania „co oznacza cyfra N” to duplikaty.
- 02-K13 (klasa 9): 0099, 0162, 0315, 0499–0502, 0673 – azbest, PCB, M3, podwyższona temperatura już są.
- 0247 i 0770 dublują się wzajemnie (1.1.4.2.1 akapit ostatni) – przy partii 52 (0766–0780).
- 0071/0072 (0,909) i 0632 (≈ stara 0297) – przy właściwych partiach (bez zmian).