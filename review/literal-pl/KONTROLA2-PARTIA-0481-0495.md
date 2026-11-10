# Kontrola druga – partia ADR-B-0481–0495 (porównanie dosłowne z polskim tekstem ADR 2025)

Data: 2026-11-10, ok. 02:30 (czas polski, CET).
Przedmiot: pierwsza kontrola ChatGPT (PR #897, scalony; main **20b0ebb9f**; `review/literal-pl/PARTIA-0481-0495.md` + `.json` + `tests/test_literal_review_0481_0495.py`, wynik 2 OK / 13 POPRAW / 0 BLOKUJ) oraz rekordy 0481–0495 na main (bank blob **ba829d36…**, 780 pytań; #897 banku nie zmienia).
Źródło: Dz.U. 2025 poz. 642 (skany PDF), OCR tesseract `-l pol`; strony wg nagłówka „Dziennik Ustaw — NNN —”. Na **obrazie strony PDF** sprawdzone: s. 1339 (tabela 8.6.4 – wiersz D/E), s. 1325 (8.1.5.2–8.1.5.3 z przypisami 2–4, „A1B1E1K1-P1”), s. 1305 (tabela 7.5.2.1 – 2.1/5.1), s. 976 (wskazówki dodatkowe 2.1–2.3), s. 58 (1.4.3.3 (i) „Zarezerwowany”, (j) – przewóz luzem). Pozostałe strony wg nagłówków OCR: s. 35 (DPPL), s. 40 (napełniający), s. 44 (przewóz luzem), s. 57 (1.4.3.1), s. 59 (1.4.3.7.1 (d)), s. 107 (1.9.5.2), s. 129 (2.2.1.1.5), s. 972 (5.4.1.4.2), s. 975 (instrukcje pisemne), s. 1291 (7.3.1.3), s. 1338 (8.6.3–8.6.4). Strony podane w #897 są poprawne. Sprostowanie poz. 1575 nie dotyczy punktów tej partii.
Status: kontrola robocza. **Żadne pytanie nie jest oznaczone jako zweryfikowane**; wszystkie pozostają `needs_review`.

## Podsumowanie

- Werdykty kontroli drugiej: **OK 0, POPRAW 15, BLOKUJ 0** (#897: 2 OK – 0484 i 0490 nie są OK; 0495 też nie, niżej).
- **BŁĘDNY KLUCZ – 0488**: klucz A „Przy przewozie luzem kod D/E wyklucza wyłącznie tunele kategorii E”. Tabela 8.6.4 (s. 1339, obraz strony): „D/E – **Przewóz luzem lub w cysternie**: zakaz przewozu przez tunele kategorii D i E; Inny przewóz: zakaz przewozu przez tunele kategorii E.” Poprawna była C. Pytanie było sprzeczne z 0033, 0084, 0208 i 0576. #897 pisze „klucz A jest prawidłowy dla przewozu luzem” i cytuje tabelę niedokładnie („przewóz w cysternie wyklucza tunele D i E, a inny przewóz – tunel E” – pominięte „luzem”). Przeredagowane z kluczem A = „tunele D i E”.
- **10 pytań → nowy element z tej samej kompetencji, niecysternowy**:
  - 0481 – 1.4.3.7.1 (d) (ii) zawory i otwory inspekcyjne = temat cysternowy → napełniający przy załadunku luzem upewnia się, że przestrzegany jest dział 7.3 (1.4.3.3 (j));
  - 0484 = **0681** (nalepka 8 → łopata, osłona, pojemnik) i **0734** (nalepka 9 → to samo) – #897: OK → wyposażenie dobiera się do nalepek całego ładunku (8.1.5.1): 2.2 + 3 → płyn do płukania oczu wymagany;
  - 0485 ≈ **0077/0171** (maska ucieczkowa dla każdego członka załogi) → przykład odpowiedniej maski z przypisu 3 do 8.1.5.3 (pochłaniacz zespolony gaz/pył A1B1E1K1-P1 lub A2B2E2K2-P2);
  - 0486 – odwrotność starej 0484 / 0681 / 0734 (ten sam przypis 4, gaz 2.2 – przypadek oczywisty), błędny „pojemnik do zbierania uwolnionego gazu” → materiał stały z samą nalepką 6.1: maski tak, łopata/osłona/pojemnik nie (przypis 4 nie wymienia 6.1);
  - 0487 = 0033, 0576, **0084** (D/E w sztukach przesyłek → E) → DPPL („duży pojemnik do przewozu luzem”) to opakowanie, a nie przewóz luzem (1.2.1) → inny przewóz → zakaz tunelu E (para kontrastowa z 0488);
  - 0489 = **0539** (B/D w sztukach przesyłek → D i E, nie C) – przeoczone w #897 → kod D bez ukośnika: zakaz D i E przy każdym sposobie przewozu (w odróżnieniu od D/E);
  - 0490 – kod B1000C to materiały wybuchowe klasy 1 (zakres kursu specjalistycznego) i kod z 8.6.4, a nie kategoria tunelu (cel 11-K01) – #897: OK → trzy główne zagrożenia przy określaniu kategorii tunelu (1.9.5.2.1);
  - 0491 – zgodność grup klasy 1 (7.5.2.2) = zakres kursu specjalistycznego, pytanie „gdzie szukać”, klucz jedyną najkrótszą → tabela 7.5.2.1 dopuszcza ładowanie razem nalepek 2.1 i 5.1;
  - 0493 = 0184 / 0108 (05-K06 = dokładnie 6) → nowy aspekt tej samej kompetencji: pożar opony, który objął całe koło i nadkole, nie jest już mały ani początkowy – nie gasić, choć ładunek się nie pali (inaczej niż 0702 – przejście na ładunek, 0743 – dym);
  - 0494 = **0612** (do odpływu tylko przez opary → oddalić się) – przeoczone w #897 – oraz 0163/0100 (05-K04 = dokładnie 6) → nowy aspekt: strona nawietrzna osiągalna tylko przez kałużę – nie wchodzić na uwolnione materiały, obejść.
- **5 pytań przeredagowanych w tym samym podtemacie**: 0482 (1.4.3.1.2 przy (d) – przypadek pozytywny, uzupełnia 0479), 0483 (przypis 2 – płyn do płukania oczu przy 2.3), 0488 (błędny klucz), 0492 (uwaga 1 do 7.5.2.1), 0495 (podklasa 1.2).
- **Żaden zamiennik nie jest cysternowy**: w 0487/0488 cysterna występuje tylko jako dystraktor/kontrast w wyjaśnieniu kodu D/E; tematem jest DPPL i przewóz luzem.
- Wszędzie ta sama litera klucza, ten sam `module_id`, `image` = null; przypisania w `kompetencje.json` bez zmian (02-K01 = 7, **05-K04 = 6**, **05-K06 = 6**, 07-K05 = 16, 08-K07 = 8, 09-K01 = 12, 11-K01 = 7, 11-K02 = 9; każda kompetencja teoretyczna ≥ 6).
- **Wady formy starych wersji**: opcje > 80 zn. – 0481 A (84), 0482 A (82), 0483 A (94), 0486 A (92), 0488 B (111), 0489 C (81), 0492 B/C (94/90), 0493 A (93); średniki – 0483 B, 0486 C, 0490 A/B/C; kropki na końcu opcji – 0492 A/B/C; słowa absolutne – 0482 A „automatycznie … wszystkie”, 0485 A „niezależnie”, C „Każdy”, 0486 A „każdej”, 0488 A „wyłącznie”, B „niezależnie”, 0489 C „wyłącznie”, 0490 A „wszystkie … niezależnie”, 0491 A/C „wyłącznie”, 0492 A „tylko”, 0493 A „Nigdy”, B „Zawsze”, C „Tylko”, 0494 A „Zawsze … niezależnie”, C „tylko”, 0495 C „wyłącznie”; klucz jedyną najkrótszą – 0485, 0491; opcje-absurdy – 0483 C (25 zn.), 0486 B (35 zn.), 0495 C („zagrożenie żrące”); w wyjaśnieniach „automatycznie” (0488), warunek spoza przepisu „gdy wymagają tego przepisy” (0481), polecenia „Nie przenoś…/Nie rozszerzaj…” zamiast wyjaśnienia (0487, 0488).

## Błędy / różnice względem raportu ChatGPT (#897)

1. **0488 – przeoczony błędny klucz** (wyżej). To najpoważniejszy błąd partii: pytanie uczyło odwrotnie niż tabela 8.6.4.
2. **0484 nie jest OK** – duplikat 0681 i 0734 (te same trzy przedmioty z przypisu 4 dla nalepek 8 i 9).
3. **0490 nie jest OK** – kod B1000C dotyczy wyłącznie materiałów wybuchowych klasy 1 (kurs specjalistyczny), a kompetencja 11-K01 dotyczy kategorii tuneli; średniki we wszystkich opcjach, A „wszystkie … niezależnie”.
4. **0495 nie jest OK** – C „wyłącznie” i absurdalny dystraktor „zagrożenie żrące”; wyjaśnienie z mylącym zdaniem o materiałach żrących.
5. **Przeoczone duplikaty**: 0489 = 0539 (B/D w sztukach przesyłek – #897 widzi tylko długość C), 0494 = 0612 (#897 podaje tylko 0163), 0485 ≈ 0077/0171 (#897 widzi tylko długości).
6. **Zakres kursu**: 0491 (7.5.2.2 – grupy zgodności klasy 1) i 0490 (B1000C) to materiał kursu specjalistycznego klasy 1 – #897 tego nie zauważa.
7. **0481 – temat cysternowy** (zawory i otwory inspekcyjne po rozładunku) – #897 proponuje tylko doprecyzowanie, czy chodzi o „cysternę, pojazd czy kontener”.
8. **Test znowu bez FIRST_PASS_BANK_SHA**: `tests/test_literal_review_0481_0495.py` ma jedną stałą EXPECTED_BANK_SHA, używaną dla manifestu (2 asercje) i dla banku – polecenie partii 32 (pkt c) wymagało OD RAZU dwóch stałych. Przy wdrożeniu: dodać FIRST_PASS_BANK_SHA = ba829d36… (obie asercje `manifest["bank_blob_sha"]`), EXPECTED_BANK_SHA → nowy SHA.
9. **Słusznie w #897**: strony Dz.U. (59, 57, 1325, 1339, 1305–1306, 1305/972, 975, 129) – tym razem wszystkie poprawne; 0487 = 0033/0576; 0493 = 0184/0108; 0494 ≈ 0163; 0486 – błędny „pojemnik do zbierania uwolnionego gazu”; 0483 C myli płyn z ochroną oczu; 0485 i 0491 – klucz jedyną najkrótszą; 0492 – opcje > 80 zn.; similarity.py przy 0,25 – 2 pary (0150/0495, 0495/0621) – zgodne z moim uruchomieniem repozytoryjnego skryptu na main; licznik 300 → 285.

## Duplikaty – sprawdzenie w całym banku (780) i między sobą

Przeszukano cały bank po temacie (1.4.3.1–1.4.3.7, napełniający, 7.3, zawory, płyn do płukania oczu, łopata/osłona/pojemnik, maska ucieczkowa, pochłaniacz/EN 14387, kody D, D/E, B/D, B1000C, luzem + tunel, DPPL, 1.9.5.2, kategorie tuneli, 7.5.2.1–7.5.2.4, 2.1 + 5.1, oddzielne dokumenty / 5.4.1.4.2, pożar opon/hamulców/silnika, kanalizacja, strona nawietrzna, gaz duszący 2.2, podklasy 1.1–1.6) oraz skryptami `check_near_duplicates.py` (0,60 i 0,40), `check_cross_module_duplicates.py` (0,80 i 0,50), `similarity.py` (0,45; dodatkowo 0,25) na kopii po poprawkach.
- `similarity.py --threshold 0.25` po poprawkach: 0199/0491 = 0,364 (3 + 8 vs 2.1 + 5.1 – inne nalepki, inny odruch „utleniacz + gaz palny”), 0483/0484 = 0,360 (sama 2.3 → bez płynu vs 2.2 + 3 → płyn wymagany – para kontrastowa), 0483/0486 = 0,333, 0084/0489 = 0,320 (D/E vs D bez ukośnika), 0184/0493 = 0,320 (mały pożar hamulca vs duży pożar opony), 0426/0491 = 0,286, 0083/0489 = 0,250. `check_near_duplicates.py --threshold 0.40` – brak par z partią. (Pierwsza wersja 0487 miała 0,440 z 0488 – stem przeredagowany, para zniknęła poniżej 0,25.)
- **0481 nowa** (napełniający – 1.4.3.3 (j), dział 7.3) vs 0290 ((h) – duże nalepki na kontenerze luzem), 0139/0173/0292/0556–0559 (09-K09 – kiedy wolno przewozić luzem) – inny element (kto i za co odpowiada).
- **0482** (1.4.3.1.2 przy (d) – wolno polegać) vs **0479** ((b) – nie wolno) – dwie strony tego samego punktu, celowo; vs 0373 ((a)), 0378 ((e)) – inne litery.
- **0483** (2.3 – bez płynu) / **0484 nowa** (2.2 + 3 – płyn wymagany) / 0225 (użycie płynu po awarii) – inne elementy. **0485 nowa** (typ maski) vs 0077 (które nalepki), 0171 (maska vs aparat), 0254 (6.1 jako dodatkowa), 0230 (użycie maski – 05-K08). **0486 nowa** (6.1 – bez łopaty) vs 0681/0734 (8, 9 – z łopatą).
- **0487 nowa** (DPPL → E) vs **0488** (luzem → D i E), 0033/0084/0576 (sztuki przesyłek), 0604 (cysterna), 0208 (znaczenie zapisu) – DPPL nigdzie w kontekście tuneli. **0489 nowa** (kod D) vs 0539 (B/D), 0574/0771 (kod najbardziej restrykcyjny), 0322 (paliwo) – inna reguła.
- **0490 nowa** (1.9.5.2.1 – trzy zagrożenia) – w banku brak pytania o 1.9.5.2.1; 0430 (C vs D), 0207 (B), 0031 (A) – inne elementy.
- **0491 nowa** (2.1 + 5.1) vs 0199 (3 + 8), 0324 (5.2 + 1), 0424–0428 (klasa 1) – inna para nalepek. **0492** – jedyne pytanie o uwagę 1 do 7.5.2.1; 0538 (5.4.1.4.2 – przesyłka w dwóch pojazdach) – inna część punktu.
- **0493 nowa** (pożar już nie mały) vs 0108, 0184, 0223, 0702, 0743, 0640, 0695 – inne kryterium. **0494 nowa** (kałuża na drodze do strony nawietrznej) vs 0106, 0183, 0221, 0692, 0741, 0178 („nie dotykając przesyłki”), 0612 – inny element tego samego zalecenia.
- **0495** (1.2) vs 0126 (1.1), 0150 (1.1 vs 1.4), 0496–0498 (1.3, 1.5, 1.6 – partia 34) – inna podklasa.

## Ustalenia dla poszczególnych pytań (cytaty, strony Dz.U., klucze)

### ADR-B-0481 – POPRAW (07-K05, C) – NOWY ELEMENT, NIECYSTERNOWY
- 1.4.3.3 (s. 58, obraz strony): „(h) przygotowując towary niebezpieczne do przewozu zapewnić, aby na cysternach, na pojazdach oraz na kontenerach do przewozu luzem zostały umieszczone nalepki ostrzegawcze, znaki i tablice barwy pomarańczowej zgodnie z działem 5.3; (i) (Zarezerwowany) (j) w przypadku załadunku towarów niebezpiecznych luzem do pojazdów lub kontenerów, upewnić się, że przestrzegane są odpowiednie przepisy działu 7.3.” 1.2.1 (s. 40): napełniający napełnia „… pojazdy, kontenery wielkie lub kontenery małe do przewozu luzem”. 7.3.1.3 (s. 1291) – pyłoszczelność i zamknięcie. Klucz C ✔.

### ADR-B-0482 – POPRAW (07-K05, C) – przeredagowane
- 1.4.3.1.1 (d) (s. 57): „po załadunku towarów niebezpiecznych do kontenera, spełnić wymagania dotyczące oznakowania, umieszczania nalepek ostrzegawczych, znaków oraz tablic barwy pomarańczowej zgodnie z działem 5.3”; 1.4.3.1.2 (s. 57): „W przypadku wymagań podanych w 1.4.3.1.1 (a), (d) i (e), załadowca może polegać na informacjach i danych udostępnionych mu przez innych uczestników przewozu.” Klucz C ✔.

### ADR-B-0483 – POPRAW (08-K07, B) – przeredagowane
- 8.1.5.2 (s. 1325): „płyn do płukania oczu ²”; „dla każdego członka załogi pojazdu … ochrona oczu (np. okulary ochronne)”; przypis 2: „Nie jest wymagany w przypadku nalepek ostrzegawczych o numerach 1, 1.4, 1.5, 1.6, 2.1, 2.2 i 2.3.” Klucz B ✔.

### ADR-B-0484 – POPRAW (08-K07, C) – NOWY ELEMENT (#897: OK; duplikat 0681/0734)
- 8.1.5.1 (s. 1325): „Elementy wyposażenia powinny być dobrane odpowiednio do numerów nalepek ostrzegawczych właściwych dla załadowanych towarów. Numery nalepek ostrzegawczych mogą być odczytane z dokumentu przewozowego.” + przypis 2 (jw. – nie wymienia nalepki 3). Klucz C ✔. Do oceny specjalisty.

### ADR-B-0485 – POPRAW (08-K07, C) – NOWY ELEMENT (≈ 0077/0171)
- 8.1.5.3 (s. 1325): „maska ucieczkowa ³ dla każdego członka załogi pojazdu … w przypadku numerów nalepek ostrzegawczych 2.3 lub 6.1”; przypis 3: „Na przykład, maska ucieczkowa z pochłaniaczem zespolonym do gazu/pyłu typu A1B1E1K1-P1 lub A2B2E2K2-P2, podobna do określonej w EN 14387:2004 + A1:2008.” (OCR: „AIBIEIKI-P1”, obraz strony – A1B1E1K1-P1). Klucz C ✔.

### ADR-B-0486 – POPRAW (08-K07, C) – NOWY ELEMENT
- 8.1.5.3 (s. 1325): „łopata ⁴; osłona otworów kanalizacyjnych ⁴; pojemnik do zbierania pozostałości ⁴”; przypis 4: „Wymagane jest tylko w przypadku materiałów stałych i materiałów ciekłych, oznakowanych nalepkami ostrzegawczymi o numerach 3, 4.1, 4.3, 8 lub 9.” Klucz C ✔.

### ADR-B-0487 – POPRAW (11-K02, A) – NOWY ELEMENT (duplikat 0033/0576/0084)
- 8.6.4 (s. 1339): D/E – „Przewóz luzem lub w cysternie: zakaz przewozu przez tunele kategorii D i E; Inny przewóz: zakaz przewozu przez tunele kategorii E.” 1.2.1 (s. 35): „Duży pojemnik do przewozu luzem (DPPL, ang. IBC) oznacza opakowanie przenośne …”; (s. 44): „Przewóz luzem oznacza przewóz nieopakowanych materiałów stałych lub przedmiotów … Określenie to nie dotyczy towarów opakowanych oraz materiałów przewożonych w cysternach.” Klucz A ✔. Do oceny specjalisty.

### ADR-B-0488 – POPRAW (11-K02, A) – BŁĘDNY KLUCZ, przeredagowane
- 8.6.4 (s. 1339, obraz strony) – jw. Stary klucz A („wyłącznie tunele kategorii E”) sprzeczny z tabelą. Nowy klucz A „Tuneli kategorii D i E, bo tak 8.6.4 określa ten kod przy przewozie luzem” ✔.

### ADR-B-0489 – POPRAW (11-K02, B) – NOWY ELEMENT (duplikat 0539)
- 8.6.4 (s. 1339): „D – Zakaz przewozu przez tunele kategorii D i E.” (jeden zakaz, bez rozróżnienia sposobu przewozu); D/E – jw. Klucz B ✔.

### ADR-B-0490 – POPRAW (11-K01, C) – NOWY ELEMENT (#897: OK; klasa 1 / kod zamiast kategorii)
- 1.9.5.2.1 (s. 107): „Określenie kategorii tunelu powinno być dokonane z uwzględnieniem trzech głównych zagrożeń, które mogą spowodować liczne ofiary lub poważne uszkodzenia konstrukcji tunelu: (a) wybuchu; (b) uwolnienia gazu trującego lub lotnej cieczy trującej; (c) pożaru.” 1.9.5.2.2 (s. 107–108) – kategorie A–E, każda kolejna obejmuje towary poprzedniej. Klucz C ✔.

### ADR-B-0491 – POPRAW (09-K01, B) – NOWY ELEMENT spoza klasy 1
- 7.5.2.1 (s. 1305, obraz strony): „Sztuki przesyłek zaopatrzone w różne nalepki ostrzegawcze mogą zostać załadowane do tego samego pojazdu lub kontenera, tylko wtedy, gdy jest to dozwolone na podstawie poniższej tabeli…”; wiersz „2.1, 2.2, 2.3” × kolumna „5.1” = X („Ładowanie razem jest dozwolone”). Klucz B ✔.

### ADR-B-0492 – POPRAW (09-K01, C) – przeredagowane
- 7.5.2.1 uwaga 1 (s. 1305): „Na przesyłki, które nie mogą być załadowane razem do tego samego pojazdu lub kontenera, należy sporządzić oddzielne dokumenty przewozowe, zgodnie z 5.4.1.4.2.” 5.4.1.4.2 (s. 972): „…odrębne dokumenty przewozowe powinny być sporządzone we wszystkich przypadkach, gdy przesyłki lub ich części nie mogą być załadowane razem do tego samego pojazdu ze względu na zakazy podane w 7.5.2.” Klucz C ✔.

### ADR-B-0493 – POPRAW (05-K06, C) – NOWY ASPEKT (duplikat 0184/0108; kompetencja = 6)
- 5.4.3.4 (s. 975): „Jeżeli jest to właściwe i bezpieczne, użyć gaśnic w celu ugaszenia małego lub będącego w fazie początkowej pożaru, obejmującego opony, hamulce lub przedział silnika”; „Oddalić się od miejsca wypadku lub zagrożenia, poinformować inne osoby…”. Klucz C ✔.

### ADR-B-0494 – POPRAW (05-K04, C) – NOWY ASPEKT (duplikat 0612, ≈ 0163; kompetencja = 6)
- 5.4.3.4 (s. 975): „Nie wchodzić na uwolnione materiały, nie dotykać ich, unikać wdychania oparów, dymu, pyłu i pary poprzez pozostawanie po stronie nawietrznej”. Klucz C ✔.

### ADR-B-0495 – POPRAW (02-K01, B) – przeredagowane (#897: OK)
- 2.2.1.1.5 (s. 129): „Podklasa 1.1 … zagrożenie wybuchem masowym (wybuch masowy jest to taki wybuch, który praktycznie obejmuje natychmiast cały ładunek). Podklasa 1.2 Materiały i przedmioty, które stwarzają zagrożenie rozrzutem, ale nie wybuchem masowym. Podklasa 1.3 … zagrożenie pożarem i małe zagrożenie wybuchem lub rozrzutem…”. Klucz B ✔.

## Wskaźniki

- „Poprawna = jedyna najdłuższa”: **32/780 = 4,10% bez zmian**, maksimum działu **7,87%** bez zmian – tych linii w `docs/POKRYCIE-KURSU.md`, `podstawowy/README.md`, `PAKIET-ZAMKNIECIE-0780.md` **nie zmieniać** (tylko SHA tam, gdzie występuje).
- „Poprawna = jedyna najkrótsza”: **162 → 158/780**; ADR-B-07 18,5% → **16,7%**, ADR-B-08 30,2% → **28,3%**, ADR-B-09 24,2% → **22,6%**, ADR-B-11 13,0% → **10,9%**; ADR-B-02 i ADR-B-05 bez zmian; maksimum działu 31,5% (bez zmian); wszystkie działy ≤ 38%.
- Wszystkie 15 wyjaśnień: 5 zdań, 467–599 znaków, maks. 33 słowa w zdaniu, na końcu „Podstawa: ADR …”; opcje 54–79 znaków; bez słów absolutnych i średników w opcjach; klucz nigdzie nie jest jedyną najdłuższą ani jedyną najkrótszą.

## Egzaminy, kolejki, snapshoty (pułapki CI)

- Egzaminy próbne – w `questions`: **0489 – wariant-001/klucz-001, 0495 – wariant-003/klucz-003, 0482 – wariant-005/klucz-005**. Na listach `excluded_question_ids` są ID z partii (002: 0489; 003: 0489; 004: 0489, 0495; 005: 0489, 0495) – tych list **nie zmieniać**. Pozostałe pliki egzaminów – tylko SHA.
- `review/specialist/KOLEJKA-PRIORYTETOWA-4X40.json` zawiera **0489 i 0490**, `4X44` – **0482 i 0495** („question” + „legal_basis”).
- Snapshoty: `review/sequential/` i `review/legal-clauses/` – pliki **477-482.json** (0481, 0482), **483-494.json** (0483–0494), **495-502.json** (0495); clause, answer_review A/B/C, notes_on_conditions ≥ 25 zn.
- Ledger `review/legal-polish/stage4w4-literal-verification-ledger-0001-0609.json`: `source_references` z nowych sources (zmienia się 13: wszystkie poza 0493 i 0494).
- Rejestry `REJESTR-AKTUALNY-0001-0765.md` i `-0001-0780.md`: po 15 wierszy.
- SHA banku ba829d36… występuje w **36 plikach** poza historycznymi raportami `review/literal-pl/`: **35 zamienianych wprost** (docs/POKRYCIE-KURSU.md, docs/STAN-KONCOWY-…, podstawowy/README.md, review/README.md, podstawowy/raporty/etap-4x135-wykluczenia-proby.json, 8 plików review/specialist, 10 plików egzaminów, tests/test_literal_review_0301_0315 … 0466_0480 (12; w 0421_0435, 0436_0450 i 0451_0465 – EXPECTED_BANK_SHA **oraz** literał w `test_second_pass_artifacts_and_bank_sha`; stałe FIRST_PASS_BANK_SHA z innym SHA zostają)) + `tests/test_literal_review_0481_0495.py` – **specjalnie**: zamiast `EXPECTED_BANK_SHA = "ba829d36…"` dwie linie `FIRST_PASS_BANK_SHA = "ba829d36…"` i `EXPECTED_BANK_SHA = "<nowy>"`; obie asercje `manifest["bank_blob_sha"]` (w `test_report_scope_counts_and_printed_page_headers` i `test_no_bank_or_exam_artifacts_are_in_scope`) → FIRST_PASS_BANK_SHA; test `test_bank_is_unchanged_and_all_batch_questions_remain_unverified` → `test_bank_has_expected_sha_after_second_pass_and_batch_remains_unverified`; docstring „; report-only, with the bank unchanged.” → „; report-only; after the second pass the bank has the expected SHA.”.
- Oczekiwany SHA banku: **ba829d36bc7e1c04aeab108d826bfae33938422f → f2cea3f46167e3f99d4c5c7b91658744eba1d8c7**.

## Test na kopii repo

`test_p33.sh` (kopia /tmp/b33 z main **20b0ebb9f** = po scaleniu #897, bez commitów i pushu): `apply_poprawki.py` → „Changed (15): ADR-B-0481 … ADR-B-0495”, blob **f2cea3f46167e3f99d4c5c7b91658744eba1d8c7**; po synchronizacji (`sync_p33_test.py`; razem 45 zmienionych plików, w tym bank i `tools/apply_poprawki.py`, + nowy POPRAWKI) wszystkie 14 skryptów CI = 0 i `python3 -m unittest discover -s tests` – **207 testów OK**.

## Licznik

Po wdrożeniu partii 33 (obie kontrole 0481–0495): **285 pytań bez porównania dosłownego po obu kontrolach** (0496–0780); kontrola pierwsza partii 34 (0496–0510): 285 → 270.

## Do zapamiętania na kolejne partie
- 0496–0498 (podklasy 1.3, 1.5, 1.6) – porównać z 0126 (1.1), 0150 (1.1/1.4) i nową 0495 (1.2); sprawdzić słowa absolutne i średniki („Nie; …” w 0497).
- Kody tunelowe: po partii 33 w 11-K02 są 0032, 0033, 0083, 0084, 0576, 0604 (D/E i E) + 0487 (DPPL), 0488 (luzem), 0489 (kod D) – kolejne pytania o D/E w sztukach przesyłek to duplikaty.
- 0247 i 0770 dublują się wzajemnie (1.1.4.2.1 akapit ostatni) – przy partii 52 (0766–0780).
- 0071/0072 (0,909) i 0632 (≈ stara 0297) – przy właściwych partiach (bez zmian).
