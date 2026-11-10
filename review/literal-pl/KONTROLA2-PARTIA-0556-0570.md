# Kontrola druga – partia ADR-B-0556–0570 (porównanie dosłowne z polskim tekstem ADR 2025)

Data: 2026-11-10 (czas polski, CET).
Przedmiot: pierwsza kontrola ChatGPT (PR #907, scalony; main **ce5e12b50**; `review/literal-pl/PARTIA-0556-0570.md` + `.json` + `tests/test_literal_review_0556_0570.py`, wynik 0 OK / 15 POPRAW / 0 BLOKUJ, licznik 225 → 210) oraz rekordy 0556–0570 na main (bank blob **7f2be64b…**, 780 pytań; #907 banku nie zmienia).
Źródła: Dz.U. 2025 poz. 642 (OCR `-l pol`; strony wg nagłówka „Dziennik Ustaw — NNN —”): s. 27–28 (1.1.3.6.3 przypis a, 1.1.3.6.4), s. 43 (1.2.1 – pojazd odkryty / przykryty opończą), s. 44 (1.2.1 – niebezpieczna reakcja), s. 950 (5.3.1.1.1), s. 951 (5.3.1.1.6, 5.3.1.1.7, 5.3.1.2, 5.3.1.4.1), s. 952 (5.3.1.6.1, 5.3.1.7.1), s. 953 (5.3.1.7.1 c.d.), s. 1291 (7.3.1.1, 7.3.1.3, 7.3.1.8), s. 1292 (7.3.1.12, 7.3.1.13, **7.3.2**), s. 1296 (7.3.3.1 – VC1, VC2), s. 1304 (7.5.1.2 – istotne wady (a)–(c)), s. 1344 (9.1.3.2, 9.1.3.3). **Kodeks cywilny – t.j. Dz.U. 2026 poz. 795** (tekst publiczny, pobrany z api.sejm.gov.pl/eli/acts/DU/2026/795/text.pdf): art. 361 (s. 36), art. 415 (s. 42), art. 430 (s. 43), art. 435 i 436 (s. 44), art. 471 (s. 49).
Status: kontrola robocza. **Żadne pytanie nie jest oznaczone jako zweryfikowane**; wszystkie pozostają `needs_review`; `review/approvals.jsonl` pusty.

## Podsumowanie

- Werdykty kontroli drugiej: **OK 0, POPRAW 15, BLOKUJ 0** – zgoda z #907 co do werdyktów, ale nie co do rozwiązań (patrz niżej).
- **0564 – klucz wieloznaczny, #907 tego nie zauważył**, choć sam zacytował 5.3.1.1.6 („powinny być zdjęte lub zakryte”): w banku B „Zakryć błędną kartką” jest zgodne z ADR, a kluczem jest C „Usunąć…”. Nowe 0564: klucz „Zdjąć ją albo zakryć”.
- **0565 – temat cysternowy/tablic pomarańczowych (5.3.2.1.7) w kompetencji 06-K09 (duże nalepki 5.3.1)** – #907 nie zgłosił. Zamiennik niecysternowy: rozkładane panele z dużymi nalepkami (5.3.1.1.7).
- **Duplikaty – #907 rozstrzygnął tylko parę 0557/0559 (wewnątrz partii)**; faktycznie dublują istniejące: 0557 = **0139, 0173** (sprawdzić tabelę A / kolumnę 17 przed przewozem luzem); 0559 = **0139** (brak dopuszczenia luzem – nie wolno); 0560 = **0138** (niezgodność stanu pojazdu – wstrzymać załadunek); 0561 = **0132** (+ 0546 po partii 37 – duże nalepki na bokach i czołach kontenera); 0566 = **0551 + 0553** (po partii 37) i **0198**; 0567 = **0758** (KC 415 – szkoda z winy); 0568 = **0660, 0713** (KC 471); 0569 – ogólnik „oceń według przepisów” pokrywający 0660/0713/0758. 0570 = **0272** (wynik 1.1.3.6.4 przy kat. 2 + kat. 3) – #907 to wskazał słusznie.
- **0563 – nietrafiony przepis**: w banku 5.3.1.1.5 (klasy wielokrotne); #907 wskazał 5.3.1.6.1, ale ten punkt dotyczy **kontenerów do przewozu luzem** (i cystern), a nie zwykłego kontenera ze sztukami przesyłek – #907 tego nie zaznaczył. Nowe 0563 – próżny nieoczyszczony **kontener do przewozu luzem** (5.3.1.6.1).
- **KC – „tekst niezałączony / do sprawdzenia” (0567–0569) to błąd**: tekst jednolity KC (Dz.U. 2026 poz. 795) jest publiczny; sprawdzony dosłownie (cytaty niżej). Nowe źródło `KC-2026-PL` z URL ELI.
- **Strona Dz.U. – 1 błąd**: 0556 – 7.3.2 stoi na **s. 1292** (#907: tylko 1291). Pozostałe strony #907 poprawne.
- **Zamienniki zaproponowane przez #907 nie nadają się do wdrożenia**: 0570 (×20) – wieloznaczne, bo nie podano, czy materiał jest w przypisie a, a wyjaśnienie nie kończy się „Podstawa: ADR …”; 0559 (VC2) – opcja „Wyłącznie… niezależnie” (słowa absolutne).
- **Wady formy, których #907 nie zgłosił**: średniki „Nie; …” – 0556 C, 0559 C, 0563 C; słowa absolutne – 0557 C „wyłącznie”, 0565 B „niezależnie”, 0567 B „Zawsze… wyłącznie”, C „automatycznie”, 0569 treść „automatycznie… każdą”, A „nigdy”, B „Każde… automatycznie”, 0570 C „niezależnie”; kropki na końcu opcji – 0561, 0565 B/C, 0567–0569; „nalepki dużego formatu” (kalka z „placards”; ADR: „duże nalepki ostrzegawcze”) – 0561–0564. Słusznie zgłoszone: 0562 – klucz B jedyną najkrótszą; ogólnikowe klucze 0556–0560, 0566–0569.
- **similarity.py – liczby w #907 opisane mylnie**: #907 podaje „1 para ≥ 0,45 / 4 pary ≥ 0,25” jak dla całego banku, a to tylko pary z udziałem partii. Cały bank na main: **9 par ≥ 0,45** i **166 par ≥ 0,25** (z partią: 1 – 0272/0570 = 0,462, i 4).
- **Test #907 – dobrze: ma obie stałe** (FIRST_PASS_BANK_SHA i EXPECTED_BANK_SHA, obie = 7f2be64b…). Po wdrożeniu zmienia się tylko EXPECTED_BANK_SHA.
- **Licznik 225 → 210 – poprawny.**
- **11 pytań → nowy element tej samej kompetencji, niecysternowy**: 0557 (7.3.1.8 – pył na zewnętrznych powierzchniach), 0559 (7.3.1.12 – odpady reagujące ze sobą), 0560 (7.5.1.2 (b) – pęknięte naroże mocujące), 0561 (5.3.1.4.1 – pojazd do przewozu luzem: boki i tył), 0563 (5.3.1.6.1 – próżny nieoczyszczony kontener do przewozu luzem), 0565 (5.3.1.1.7 – rozkładane panele), 0566 (9.1.3.3 – język świadectwa dopuszczenia; 9.1.3.2 – uznawanie), 0567 (KC 436 § 1 / 435 § 1 – zasada ryzyka), 0568 (KC 361 § 2 – straty i utracone korzyści), 0569 (KC 430 – odpowiedzialność za podwładnego), 0570 (1.1.3.6.4 – kat. 1 ×50 dla materiału spoza przypisu a).
- **4 pytania przeredagowane w tym samym podtemacie**: 0556 (VC1 – odkryta wywrotka bez opończy), 0558 (7.3.1.3 – pył przez szparę klapy), 0562 (wyblakła duża nalepka wzoru 3 – wymienić), 0564 (stara nalepka wzoru 8 – zdjąć albo zakryć).
- Wszędzie ta sama litera klucza i ten sam `module_id`; przypisania w `kompetencje.json` bez zmian (01-K06 = 9, 06-K09 = 13, 07-K07 = 6, 08-K08 = 8, 09-K08 = 7, 09-K09 = 7; minimum = 6). Klasa 1 (5.3.1.5.1) odrzucona jako zamiennik 0561 – poza zakresem kursu podstawowego.

## Błędy / różnice względem raportu ChatGPT (#907)

1. **0564 – klucz wieloznaczny** (B „zakryć” zgodne z 5.3.1.1.6) – nie zgłoszony.
2. **0565 – temat 5.3.2.1.7 (tablice, cysterna) poza kompetencją 06-K09** – nie zgłoszony.
3. **Przeoczone duplikaty**: 0557 = 0139/0173; 0559 = 0139; 0560 = 0138; 0561 = 0132 (+0546); 0566 = 0551/0553 (+0198); 0567 = 0758; 0568 = 0660/0713; 0569 ogólnik. #907 rozstrzygnął tylko 0557/0559 wewnątrz partii i 0570/0272.
4. **0563 – 5.3.1.6.1 nie dotyczy zwykłego kontenera** – nie zaznaczone.
5. **KC „tekst niezałączony”** – tekst publiczny, sprawdzony (Dz.U. 2026 poz. 795).
6. **Strona 0556 – 7.3.2 na s. 1292** (nie tylko 1291) – `gazette_pages` i `EXPECTED_PAGES` do poprawy.
7. **Zamienniki #907 wadliwe** (0570 wieloznaczny i bez „Podstawa”; 0559 ze słowami absolutnymi).
8. **Przeoczone wady formy** (średniki, słowa absolutne, kropki, „dużego formatu”).
9. **Liczby similarity.py opisane jako całobankowe**, a to pary z partią (cały bank: 9 / 166).
10. **Słusznie w #907**: werdykty POPRAW 15/15; 0557/0559 dublują się; 0570 ≈ 0272; 0562 klucz jedyną najkrótszą; 0558 – 7.3.3/7.5.7.1 to nie trafne przepisy, właściwy 7.3.1.3; 0563 – 5.3.1.1.5 to nie trafny przepis; obie stałe SHA w teście; licznik 225 → 210; strony 27–28, 43, 950–953, 1291, 1296, 1304, 1344.

## Duplikaty – sprawdzenie w całym banku (780) i między sobą

Przeszukano cały bank po temacie (przewóz luzem 7.3.1.1–7.3.1.13, VC1/VC2/VC3, BK, kolumna 17, pył/pozostałości na zewnątrz, pyłoszczelność, odpady, istotne wady 7.5.1.2 / 7.3.1.13, duże nalepki 5.3.1.1.1–5.3.1.7.4, kontener do przewozu luzem, rozkładane panele, świadectwo dopuszczenia 9.1.2–9.1.3.5, KC 361/415/430/435/436/471, 1.1.3.6.3–1.1.3.6.4) oraz każde pytanie z każdym pytaniem jego kompetencji w `kompetencje.json`; skrypty na kopii po poprawkach:
- `similarity.py --threshold 0.45`: main – 9 par (z partią 1: 0272/0570 = 0,462); po poprawkach – **8 par, żadna z partią**. `--threshold 0.25`: po poprawkach 169 par, z partią 7, największa 0557/0558 = 0,364 (różne punkty: 7.3.1.8 vs 7.3.1.3), 0271/0570 = 0,320 (0271: ×20 dla materiału z przypisu a; 0570: ×50 dla materiału spoza przypisu – przepisy uzupełniające się, nie duplikat), 0561/0563 = 0,292, 0323/0570 = 0,280, 0272/0570 = 0,263, 0139/0556 = 0,250, 0547/0561 = 0,250.
- `check_near_duplicates.py --threshold 0.40` i `check_cross_module_duplicates.py --threshold 0.50` – brak par z partią.
- **0556** vs 0139 (brak dopuszczenia luzem), 0557/0559 (stare), 0173 – brak pytania o znaczenie VC1 (opończa).
- **0557** vs 0558, 0202, 0436 – brak pytania o 7.3.1.8.
- **0558** vs 0557 (nowe – pył na zewnątrz), 0436 – brak drugiego pytania o 7.3.1.3.
- **0559** – brak pytania o 7.3.1.12 (zakazy 7.5.2 dotyczą sztuk przesyłek, inne pytania banku).
- **0560** vs 0555 (partia 37 – lit. (c) zawiasy), 0475 (otwór w dachu – lit. (a)), 0138 – lit. (b) bez pytania.
- **0561** vs 0132, 0546 (kontenery – boki i czoła), 0133 (5.3.1.3) – brak pytania o pojazd do przewozu luzem.
- **0562** vs 0546 (partia 37 – teraz UN 3480/9A), 0549 (wymiary) – jedyne pytanie o trwałość dużej nalepki.
- **0563** vs 0548 (partia 37 – teraz kontener mały), 0564 – brak pytania o 5.3.1.6.1.
- **0564** – jedyne pytanie o 5.3.1.1.6.
- **0565** – brak pytania o 5.3.1.1.7.
- **0566** vs 0137, 0198, 0551, 0552, 0553 – brak pytania o język świadectwa.
- **0567** vs 0758 (415, wina) – brak pytania o zasadę ryzyka 436.
- **0568** vs 0660, 0713 (471) – brak pytania o zakres szkody 361 § 2.
- **0569** – brak pytania o 430.
- **0570** vs 0271, 0272, 0323 – brak pytania o mnożnik 50.

## Szczegóły – cytaty (dosłownie z Dz.U.) i rozstrzygnięcia

### ADR-B-0556 – POPRAW (09-K09, C) – przeredagowane (#907: strona 1291 → 1291–1292)
- 7.3.1.1 (s. 1291): „Towary niebezpieczne mogą być przewożone luzem w kontenerach do przewozu luzem, w kontenerach lub w pojazdach jedynie w następujących przypadkach: … (b) jeżeli taki sposób przewozu jest wyraźnie dozwolony na podstawie przepisu szczególnego oznaczonego kodem VC lub odniesienia do konkretnego przepisu w kolumnie (17) tabeli A w dziale 3.2 oraz spełnione są wymagania tego przepisu …”. 7.3.3.1 (s. 1296): „VC1 Przewóz luzem dozwolony jest w pojazdach przykrytych opończą, kontenerach przykrytych opończą lub kontenerach do przewozu luzem przykrytych opończą.” 1.2.1 (s. 43): „Pojazd przykryty opończą oznacza pojazd odkryty wyposażony w opończę do ochrony załadowanego towaru.” Klucz C ✔. (Stare źródło 7.3.2 – s. 1292.)

### ADR-B-0557 – POPRAW (09-K09, A) – NOWY ELEMENT (= 0139/0173)
- 7.3.1.8 (s. 1291): „Podczas przewozu, na zewnętrznych powierzchniach kontenera do przewozu luzem, kontenera i nadwozia pojazdu nie powinny występować żadne niebezpieczne pozostałości.” Klucz A ✔.

### ADR-B-0558 – POPRAW (09-K09, B) – przeredagowane (stare źródło 7.3.3; 7.5.7.1)
- 7.3.1.3 (s. 1291): „Kontenery do przewozu luzem, kontenery i nadwozia pojazdów powinny być pyłoszczelne oraz zamknięte w taki sposób, aby w normalnych warunkach przewozu obejmujących oddziaływania wibracji, zmiany temperatury, wilgotności lub ciśnienia, ich zawartość nie wydostała się na zewnątrz.” Klucz B ✔.

### ADR-B-0559 – POPRAW (09-K09, C) – NOWY ELEMENT (= 0139; = 0557 stare)
- 7.3.1.12 (s. 1292): „Materiały, np. odpady, które mogą reagować ze sobą niebezpiecznie, a także materiały różnych klas i towary niepodlegające ADR, które mogą reagować ze sobą niebezpiecznie, nie powinny być ładowane razem do tego samego kontenera lub pojazdu. Za niebezpieczne reakcje uważa się: (a) spalanie lub wydzielanie znacznych ilości ciepła; (b) wydzielanie gazów palnych lub trujących; …”. Klucz C ✔.

### ADR-B-0560 – POPRAW (09-K08, B) – NOWY ELEMENT (= 0138)
- 7.5.1.2 (s. 1304): „Elementami konstrukcyjnymi jednostki transportowej cargo … są, np. … słupki naroża i naroża mocujące … Za istotne wady uważa się: … (b) jakiekolwiek odkształcenie konstrukcji lub uszkodzenie elementów służących do podnoszenia lub przemieszczania, uniemożliwiające właściwe pozycjonowanie urządzenia przeładunkowego oraz założenie i zamocowanie kontenera na podwoziu, wagonie, pojeździe lub w ładowni statku”. Klucz B ✔. (Lit. (a) – otwór w dachu – już w 0475; lit. (c) – w 0555.)

### ADR-B-0561 – POPRAW (06-K09, A) – NOWY ELEMENT (= 0132, 0546)
- 5.3.1.4.1 (s. 951, sekcja „Umieszczanie dużych nalepek ostrzegawczych na … pojazdach do przewozu luzem …”): „Duże nalepki ostrzegawcze powinny być umieszczone na obu bokach i z tyłu pojazdu.” 5.3.1.2 (s. 951): „Duże nalepki ostrzegawcze powinny być umieszczone na obu bokach i obu czołach kontenera …”. Klucz A ✔. (Stare źródło 5.3.1.1.4 – klasa 9, nietrafne.)

### ADR-B-0562 – POPRAW (06-K09, B) – przeredagowane (klucz był jedyną najkrótszą)
- 5.3.1.1.1 (s. 950): „Duże nalepki ostrzegawcze powinny być odporne na warunki atmosferyczne i zapewniać trwałość oznakowania podczas całego przewozu.” 5.3.1.7.1 (s. 952–953): „Symbol i linia wewnątrz dużej nalepki ostrzegawczej powinny odpowiadać pod względem koloru wzorowi nalepki wymaganemu dla klasy …”. Klucz B ✔.

### ADR-B-0563 – POPRAW (06-K09, C) – NOWY ELEMENT (5.3.1.6.1 – tylko kontener do przewozu luzem)
- 5.3.1.6.1 (s. 952): „Próżne nieoczyszczone i nieodgazowane pojazdy-cysterny, … a także próżne nieoczyszczone pojazdy i kontenery do przewozu luzem, powinny być nadal zaopatrzone w duże nalepki ostrzegawcze wymagane dla ostatniego ładunku.” 5.3.1.1.6 (s. 951) – patrz 0564. Klucz C ✔. Pytanie nie dotyczy cysterny (kontener do przewozu luzem, materiał stały klasy 9).

### ADR-B-0564 – POPRAW (06-K09, C) – przeredagowane (stary klucz wieloznaczny)
- 5.3.1.1.6 (s. 951): „Duże nalepki ostrzegawcze, które nie dotyczą przewożonych towarów lub ich pozostałości, powinny być zdjęte lub zakryte.” Klucz C („Zdjąć ją albo zakryć”) ✔.

### ADR-B-0565 – POPRAW (06-K09, A) – NOWY ELEMENT (stary temat 5.3.2.1.7 – tablice / cysterna)
- 5.3.1.1.7 (s. 951): „Jeżeli duże nalepki ostrzegawcze umieszczone są w rozkładanych panelach, to panele te powinny być tak zaprojektowane i zabezpieczone, aby zapobiec ich rozkładaniu się lub obluzowaniu ich zamocowania podczas przewozu (w szczególności w wyniku wstrząsów lub niezamierzonych działań).” Klucz A ✔.

### ADR-B-0566 – POPRAW (08-K08, B) – NOWY ELEMENT (= 0551/0553/0198)
- 9.1.3.3 (s. 1344): „Świadectwo dopuszczenia powinno być wystawione w języku lub w jednym z języków urzędowych państwa wystawiającego. Jeżeli nie jest to język angielski, francuski lub niemiecki, to tytuł świadectwa i uwagi zawarte w punkcie 11 powinny być również w języku angielskim, francuskim lub niemieckim.” 9.1.3.2 (s. 1344): „Świadectwo dopuszczenia wystawione przez właściwą władzę jednej z Umawiających się Stron ADR dla pojazdu zarejestrowanego na jej terytorium, powinno być uznawane przez właściwe władze pozostałych Umawiających się Stron ADR przez cały okres jego ważności.” Klucz B ✔.

### ADR-B-0567 – POPRAW (07-K07, A) – NOWY ELEMENT (= 0758)
- KC art. 436 § 1 (s. 44): „Odpowiedzialność przewidzianą w artykule poprzedzającym ponosi również samoistny posiadacz mechanicznego środka komunikacji poruszanego za pomocą sił przyrody.” Art. 435 § 1: „… ponosi odpowiedzialność za szkodę na osobie lub mieniu, wyrządzoną komukolwiek przez ruch przedsiębiorstwa lub zakładu, chyba że szkoda nastąpiła wskutek siły wyższej albo wyłącznie z winy poszkodowanego lub osoby trzeciej, za którą nie ponosi odpowiedzialności.” Pieszy – nie zderzenie pojazdów (436 § 2 nie dotyczy). Klucz A ✔.

### ADR-B-0568 – POPRAW (07-K07, B) – NOWY ELEMENT (= 0660/0713)
- KC art. 361 (s. 36): „§ 1. Zobowiązany do odszkodowania ponosi odpowiedzialność tylko za normalne następstwa działania lub zaniechania, z którego szkoda wynikła. § 2. W powyższych granicach, w braku odmiennego przepisu ustawy lub postanowienia umowy, naprawienie szkody obejmuje straty, które poszkodowany poniósł, oraz korzyści, które mógłby osiągnąć, gdyby mu szkody nie wyrządzono.” Klucz B ✔.

### ADR-B-0569 – POPRAW (07-K07, C) – NOWY ELEMENT (ogólnik)
- KC art. 430 (s. 43): „Kto na własny rachunek powierza wykonanie czynności osobie, która przy wykonywaniu tej czynności podlega jego kierownictwu i ma obowiązek stosować się do jego wskazówek, ten jest odpowiedzialny za szkodę wyrządzoną z winy tej osoby przy wykonywaniu powierzonej jej czynności.” Brak zwolnienia przez brak winy w wyborze (to art. 429 – inna sytuacja). Klucz C ✔.

### ADR-B-0570 – POPRAW (01-K06, A) – NOWY ELEMENT (= 0272)
- 1.1.3.6.4 (s. 28): „… suma: – ilości materiałów i przedmiotów należących do kategorii transportowej 1 pomnożona przez „50”; – ilości materiałów i przedmiotów należących do kategorii transportowej 1, o których mowa w przypisie a do tabeli podanej w 1.1.3.6.3, pomnożona przez „20”; – ilości … kategorii transportowej 2 pomnożona przez „3”; oraz – ilości … kategorii transportowej 3, nie powinna przekraczać „1000”.” 8 × 50 + 500 = 900 ✔ (B: 508 bez mnożników; C: 660 przy ×20 – materiał spoza przypisu a).

## Wskaźniki

- „Poprawna = jedyna najdłuższa”: **29/780 = 3,72% – bez zmian**, maksimum działu **6,74%** – bez zmian (liczby w docs/README bez zmian).
- „Poprawna = jedyna najkrótsza”: **129 → 122/780**; ADR-B-06 24,2% → **21,2%**, ADR-B-08 22,6% → **20,8%**, ADR-B-09 17,7% → **11,3%**; ADR-B-01 (20,4%) i ADR-B-07 (14,8%) bez zmian; maksimum działu 26,4% (bez zmian); wszystkie działy ≤ 38%.
- 15 nowych wyjaśnień: 4–5 zdań, ≥ 300 znaków, ≤ 35 słów w zdaniu, na końcu „Podstawa: ADR …”; w KC – słowo „przepis” zamiast „art.” (dzielnik zdań CI tnie po „art.”); opcje ≤ 80 znaków; bez słów absolutnych, średników i kropek w opcjach; klucz nigdzie nie jest jedyną najdłuższą ani jedyną najkrótszą.

## Egzaminy, kolejki, snapshoty (pułapki CI)

- Egzaminy próbne – w `questions`: **0556 – wariant-002/klucz-002; 0564 – wariant-003/klucz-003; 0559 – wariant-004/klucz-004**. Na listach `excluded_question_ids`: wariant-003 – 0556; wariant-004 – 0556, 0564; wariant-005 – 0556, 0559, 0564 – **nie zmieniać**. Pozostałe pliki egzaminów – tylko SHA.
- Kolejki 4X40 i 4X44 – żadnego ID z partii (tylko SHA).
- Snapshoty `review/sequential/` i `review/legal-clauses/`: **546-560.json** (tylko 0556–0560), **561-566.json**, **567-569.json**, **570-579.json** (tylko 0570); clause, answer_review A/B/C, notes_on_conditions ≥ 25 zn.
- Ledger `review/legal-polish/stage4w4-literal-verification-ledger-0001-0609.json`: `source_references` – zmienia się **15**.
- Rejestry `REJESTR-AKTUALNY-0001-0765.md` i `-0001-0780.md`: po **15 wierszy**.
- SHA banku 7f2be64b… występuje w **40 plikach** poza historycznymi raportami `review/literal-pl/` (tam nie zmieniać, w tym `PARTIA-0556-0570.json` → `bank_blob_sha` zostaje) i poza `tests/test_literal_review_0556_0570.py`: docs/POKRYCIE-KURSU.md, docs/STAN-KONCOWY-BANKU-ADR-PODSTAWOWY-2026-11-03.md, podstawowy/README.md, review/README.md, podstawowy/raporty/etap-4x135-wykluczenia-proby.json, 10 plików egzaminów, review/specialist: INSTRUKCJA-RECENZJI.md, PRZEKAZANIE-ETAP4.md, PAKIET-0628-MANIFEST.json, PAKIET-0780-MANIFEST.json, KOLEJKA-PRIORYTETOWA-4X40.json, KOLEJKA-PRIORYTETOWA-4X44.json, REJESTR-AKTUALNY-0001-0765.md, REJESTR-AKTUALNY-0001-0780.md, tests/test_literal_review_0301_0315 … 0541_0555 (17 plików; w 0541_0555 zmienia się tylko EXPECTED_BANK_SHA – FIRST_PASS_BANK_SHA 73aa25f2… zostaje).
- `tests/test_literal_review_0556_0570.py`: tylko **EXPECTED_BANK_SHA → nowy** (FIRST_PASS_BANK_SHA = 7f2be64b… zostaje – asercja manifestu); `test_bank_remains_unchanged_and_unverified` → `test_bank_after_second_pass_and_unverified`; docstring; `EXPECTED_PAGES` i `gazette_pages` w .json – 0556: [1291, 1292]; nowy `test_second_pass_artifacts_and_bank_sha`. Licznik 225/210, counts 0/15/0 i bank_changed = false zostają.
- Scenariusze `podstawowy/praktyka/` odwołują się do 0562, 0567, 0570 – tematy nadal zgodne, bez zmian.
- Oczekiwany SHA banku: **7f2be64ba60fef44ab136bdf59cbb4bdd949c172 → b240a96d8c9d0bae561d132b0a6bc8f705ee7ca2**.

## Test na kopii repo

`test_p38.sh` – git worktree `/tmp/b38` z main ce5e12b50 (bez commitów i pushu): `tools/apply_poprawki.py` z dopisanym `POPRAWKI-KONTROLA2-0556-0570.jsonl` → „Changed (15): ADR-B-0556 … ADR-B-0570”, blob **b240a96d…**; synchronizacja (`sync_p38_test.py`: snapshoty i legal-clauses 15 ID, ledger 15, egzaminy 002/003/004, rejestry 2 × 15 wierszy, SHA w 40 plikach, test 0556_0570, PARTIA-0556-0570.json/.md); wszystkie **14 skryptów CI** – kod 0; `python3 -m unittest discover -s tests` – **Ran 226 tests – OK**.