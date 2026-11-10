# Kontrola druga – partia ADR-B-0526–0540 (porównanie dosłowne z polskim tekstem ADR 2025)

Data: 2026-11-10, ok. 07:20 (czas polski, CET).
Przedmiot: pierwsza kontrola ChatGPT (PR #903, scalony; main **cfd22cb9e**; `review/literal-pl/PARTIA-0526-0540.md` + `.json` + `tests/test_literal_review_0526_0540.py`, wynik 3 OK / 12 POPRAW / 0 BLOKUJ) oraz rekordy 0526–0540 na main (bank blob **e0c67175…**, 780 pytań; #903 banku nie zmienia).
Źródło: Dz.U. 2025 poz. 642 (skany PDF), OCR tesseract `-l pol`; strony wg nagłówka „Dziennik Ustaw — NNN —”. Na **obrazie strony PDF** sprawdzone: s. 692 (3.5.4.1, 3.5.4.2 z odsyłaczami * i **; stopka „675”), s. 693 (3.5.4.3, 3.5.5, 3.5.6; stopka „676”), s. 971 (5.4.1.4.1 – zdanie o języku na dole strony; stopka „266”), s. 1338 (8.6.3.1–8.6.3.3, 8.6.4 z tiretem o tunelach E), s. 1339 (tabela 8.6.4 – wiersze B/D, D/E). Pozostałe strony wg nagłówków OCR: s. 54 (1.3.2.2, 1.3.2.3), s. 688 (3.4.11, 3.4.12, 3.4.13 (a)), s. 689 (3.4.14, 3.4.15), s. 928 (5.1.2.1), s. 962 (5.4.1.1.1 (e), (f), akapit o kolejności, 5.4.1.1.3.1), s. 964 (5.4.1.1.5, 5.4.1.1.6.1, 5.4.1.1.6.2.1, 5.4.1.1.6.2.2), s. 972 (5.4.1.4.2). Sprostowanie poz. 1575 – bez wpływu na tę partię.
Status: kontrola robocza. **Żadne pytanie nie jest oznaczone jako zweryfikowane**; wszystkie pozostają `needs_review`.

## Podsumowanie

- Werdykty kontroli drugiej: **OK 0, POPRAW 15, BLOKUJ 0** (#903: 3 OK – 0526, 0537, 0539 nie są OK).
- **BŁĘDNE STRONY Dz.U. w #903 (10 pytań)** – znów numery **stopki ADR** zamiast nagłówka Dz.U.: 0526, 0527 (3.5.5, 3.5.6) – „676” to stopka, w Dz.U. **s. 693**; 0528 (3.5.4.3) – „675” to stopka (stopka s. 692), 3.5.4.3 stoi na **s. 693**; 0534, 0535 (3.4.11, 3.4.12) – „671” to stopka, w Dz.U. **s. 688**; 0540 – 3.4.13 na **s. 688**, 3.4.14 na **s. 689**, tiret 8.6.4 o tunelach E na **s. 1338** (nie 671 i 1339). Ponadto +1 strona: 0529 – 1.3.2.3 na **s. 54**, nie 55; 0530 – zdanie z 5.4.1.1.3.1 na **s. 962**, nie 963; 0533 – zdanie o języku z 5.4.1.4.1 na **s. 971**, nie 972 (obraz strony); 0539 – 8.6.3.2 na **s. 1338** (tabela 8.6.4 – s. 1339).
- **Duplikaty – #903 nie widzi żadnego, faktycznie 5 pytań dubluje istniejące**: 0527 = **0573** (3.5.6 – zapis i liczba sztuk EQ); 0530 = **0008, 0046, 0179, 0294, 0629, 0680** (wyraz „ODPAD” przed nazwą przewozową); 0537 = **0070** (ilość osobno dla każdego towaru), ≈ 0599 – #903: OK; 0539 ≈ **0064, 0086, 0263, 0432, 0574, 0771** (8.6.3.2 – kod najbardziej restrykcyjny; 0771: dwa kody i tunel C) – #903: OK, „nie stwierdzono duplikatu”; 0534 ≈ **0528** (ten sam schemat „opakowanie zbiorcze + znaki niewidoczne” dla LQ i EQ w tej samej kompetencji 01-K05).
- **Polskie brzmienie**: słusznie #903 wytknął „OVERPACK” (0528, 0534) i „SALVAGE PACKAGING” (0531) – polski tekst: „OPAKOWANIE ZBIORCZE” (3.4.11, 3.5.4.3, 5.1.2.1), „OPAKOWANIE AWARYJNE” (5.4.1.1.5). Uwaga na przyszłość: 0689 (5.1.2.1) też używa „OVERPACK” – do partii 46.
- **Wady formy**: opcje > 80 zn. – 0528 B (86), 0529 C (84), 0530 C (88), 0531 A/B (100/89), 0535 A/B/C (85/81/88), 0536 A/B (83/82), 0540 A (83); słowa absolutne w opcjach – 0526 B „wszystkie”, 0533 A „zawsze”, 0535 C „wyłącznie”, 0536 B „niezależnie”, 0540 A „żadnych”; klucz jedyną najkrótszą – 0529, 0530, 0531, 0533, 0534, 0535, 0536, 0538; klucz jedyną najdłuższą – 0532; dystraktory absurdalne – 0528 A (numer rejestracyjny), 0537 C (masa własna pojazdu); wyjaśnienie 0536 „A i B proponują…” (odwołanie do liter); wyjaśnienie 0532 „wskazać … ostatnią zawartość” (5.4.1.1.6.1 tego nie wymaga); 0539 „pojazd podlega ograniczeniom ADR” (nieostre – chodzi o tablice pomarańczowe); 0540 „z powodu masy ładunku wymaga oznakowania” (treść podaje wynik zamiast danych).
- **5 pytań → nowy element z tej samej kompetencji, niecysternowy**:
  - 0527 (01-K05) → treść znaku EQ: numer pierwszej lub jedynej nalepki z kolumny (5) i nazwa nadawcy lub odbiorcy, jeśli nie ma jej gdzie indziej (3.5.4.1, 3.5.4.2; s. 692, obraz strony);
  - 0530 (13-K08) → zapis „PRÓŻNE OPAKOWANIE, 3” dla próżnych nieoczyszczonych beczek zastępuje dane (a)–(f) (5.4.1.1.6.2.1; „PRÓŻNY POJAZD” – 5.4.1.1.6.2.2; s. 964) – w banku brak pytania o 5.4.1.1.6.2;
  - 0534 (01-K05) → opakowanie zbiorcze z samymi LQ: „OPAKOWANIE ZBIORCZE” + znak LQ; numery UN i nalepki z 5.1.2.1 tylko przy innych towarach niezapakowanych w LQ (3.4.11 akapit ostatni; s. 688);
  - 0537 (13-K02) → kod opakowania („4G”) jedynie jako uzupełnienie słownego określenia sztuki przesyłki (5.4.1.1.1 (e); s. 962);
  - 0539 (11-K03) → odczyt kodu (B/D) dla przewozu w sztukach przesyłek: zakaz tylko tuneli D i E, tunel C dozwolony (tabela 8.6.4, s. 1339; 8.6.3.1, s. 1338) – bez elementu 8.6.3.2 (6 pytań w banku).
- **10 pytań przeredagowanych w tym samym podtemacie**: 0526 (B bez „wszystkie”), 0528 („OPAKOWANIE ZBIORCZE” + znak EQ), 0529 (1.3.2.3 – pełny zakres: zagrożenia, bezpieczne postępowanie, procedury ratownicze), 0531 („OPAKOWANIE AWARYJNE”, treść nie podaje nazwy opakowania), 0532 („PRÓŻNE NIEOCZYSZCZONE” / „POZOSTAŁOŚCI OSTATNIEGO ŁADUNKU”, bez ilości (f)), 0533 (bez „zawsze”, zastrzeżenie umów), 0535 (masa brutto, przed przewozem, udokumentowanie), 0536 (konkretny zapis UN 1098 w złej kolejności), 0538 (dokumenty lub kopie dla każdej jednostki), 0540 (liczby 40 t / 10 t zamiast gotowego wniosku; zakrycie znaków jako dystraktor).
- **Żaden zamiennik nie jest cysternowy** (0530 – beczki; 0539 – beczki, wiersz cysternowy tylko jako dystraktor; 0534 – paleta LQ; 0527 – karton EQ; 0537 – skrzynie).
- Wszędzie ta sama litera klucza, ten sam `module_id`, `image` = null; przypisania w `kompetencje.json` bez zmian (01-K02 = 9, 01-K05 = 14, 11-K03 = **6**, 11-K05 = **6**, 13-K01 = 8, 13-K02 = **6**, 13-K08 = 10; minimum kompetencji teoretycznych = 6).

## Błędy / różnice względem raportu ChatGPT (#903)

1. **Strony Dz.U. – 10 błędów** (lista wyżej). 671/675/676 to numery **stopki ADR** (jak „604” w partii 35). Test #903 **utrwala błędne strony** w `EXPECTED_PAGES` – trzeba poprawić .json i test (s. niżej).
2. **Licznik**: #903 podał **270 → 255** (w .md, w .json `previous_uncompared` 270 / `remaining_without_comparison` 255 i w teście). Poprawnie po partii 35: **255 → 240** (polecenie mówiło wprost 255 → 240).
3. **Test #903 ma tylko EXPECTED_BANK_SHA** (polecenie: od razu dwie stałe). Ta sama stała służy manifestowi (`bank_blob_sha`) i bankowi – po wdrożeniu jeden z testów musi być czerwony. Trzeba dodać FIRST_PASS_BANK_SHA = e0c67175… (manifest) i EXPECTED_BANK_SHA = nowy (bank).
4. **0526, 0537, 0539 nie są OK**: 0526 – „wszystkie” w B; 0537 = 0070, C absurdalny; 0539 – duplikat tematu 8.6.3.2 (6 pytań), nieostre „pojazd podlega ograniczeniom ADR”.
5. **Przeoczone duplikaty**: 0527 = 0573; 0530 = 0008/0046/0179/0294/0629/0680; 0537 = 0070; 0539 ≈ 0064/0086/0263/0432/0574/0771; 0534 ≈ 0528. Przy 0527 i 0530 #903 zaleca tylko korektę – to duplikaty, potrzebny nowy element (brak `proposed_replacement`).
6. **duplicate_search**: #903 – 0 par przy 0,45 i 1 para (0526/0572 = 0,294) przy 0,25 – potwierdzam (razem 173 pary przy 0,25). Miara leksykalna nie wykryła żadnego z 5 duplikatów – wyszukiwanie po temacie jest obowiązkowe.
7. **Słusznie w #903**: klucze 15 pytań merytorycznie poprawne; cytaty dosłowne zgodne (3.5.5, 3.5.6, 3.5.4.3, 1.3.2.3, 5.4.1.1.3.1, 5.4.1.1.5, 5.4.1.1.6.1, 5.4.1.4.1, 3.4.11, 3.4.12, 5.4.1.1.1, (f), 5.4.1.4.2, 8.6.3.2, 3.4.13); „OVERPACK”/„SALVAGE PACKAGING” → polskie brzmienie; 0532 – dokładne zapisy; 0540 – „masa ładunku” vs masa maksymalna jednostki; strony 964 (0531, 0532), 962 (0536, 0537), 972 (0538); długości > 80 zn.
8. **Zaległości z wdrożenia #902 (partia 35)** – CI ich nie wykrywa: (a) `review/legal-clauses/510-512.json`, `513-519.json`, `520-525.json` – dla 0511–0524 `clause`, `answer_review` i `notes_on_conditions` opisują **stare** pytania (moje gotowe wartości z polecenia 35 nie zostały wpisane); (b) `REJESTR-AKTUALNY-0001-0765.md` i `-0780.md` – 14 wierszy 0511–0524 ze starą treścią i źródłami; (c) SHA **f732aa35…** został w 3 plikach: `docs/STAN-KONCOWY-BANKU-ADR-PODSTAWOWY-2026-11-03.md` (2×), `review/specialist/PAKIET-0780-MANIFEST.json` (7×), `review/specialist/REJESTR-AKTUALNY-0001-0780.md` (1×). Do nadrobienia w tym samym PR.

## Duplikaty – sprawdzenie w całym banku (780) i między sobą

Przeszukano cały bank po temacie (EQ/3.5, 1 000 sztuk, znak EQ, 3.5.6, opakowanie zbiorcze/OVERPACK/5.1.2.1, LQ 3.4.11–3.4.15, masa brutto LQ, 8 t / 12 t, 1.3.1–1.3.3, szkolenie z bezpieczeństwa, „ODPAD”/5.4.1.1.3, opakowania awaryjne, próżne nieoczyszczone/5.4.1.1.6, „PRZEWÓZ ZGODNY Z”, język dokumentu/5.4.1.4.1, instrukcje pisemne 5.4.3.2, kolejność (a)–(d), (k), 5.4.1.1.1 (e)/(f), kody opakowań, 5.4.1.4.2/7.5.2, kody tunelowe B/D, C/D, D/E, 8.6.3.1–8.6.3.3, 8.6.4) oraz skryptami `check_near_duplicates.py` (0,60 i 0,40), `check_cross_module_duplicates.py` (0,80 i 0,50), `similarity.py` (0,45; dodatkowo 0,25) na kopii po poprawkach.
- `similarity.py --threshold 0.25` po poprawkach – pary z partią: 0526/0572 = 0,294 (limit 1 000 sztuk vs pozostałe warunki EQ – inny element), 0522/0529 = 0,286 (1.3.2.2 przewóz kombinowany vs 1.3.2.3 bezpieczeństwo – inny punkt); razem 174 pary przy 0,25 (na main 173). Przy 0,45 – brak par z partią (pierwsza wersja 0540 dała 0,524 z 0209 – treść przebudowana). `check_near_duplicates.py --threshold 0.40` i `check_cross_module_duplicates.py --threshold 0.50` – brak par z partią.
- **0526** vs 0572, 0573 – 0572 pyta o warunki poza liczbą sztuk; brak drugiego pytania o limit 1 000.
- **0527 nowa** vs 0260 (E0), 0528, 0572, 0573 – brak pytania o treść znaku EQ.
- **0528** vs 0534 (po zmianie – inny element), 0689 (5.1.2.1, zwykłe towary) – inny dział.
- **0529** vs 0001, 0040, 0041, 0092, 0513, 0520–0522 – brak drugiego pytania o 1.3.2.3.
- **0530 nowa** vs 0241 („PRZEWÓZ ZGODNY Z 7.5.8.1”), 0245, 0334 (UN 3509), 0532 (5.4.1.1.6.1), 0565 – brak pytania o 5.4.1.1.6.2.1; 0532 i 0530 dotyczą dwóch różnych, alternatywnych zapisów (6.1 vs 6.2.1).
- **0531** – brak innych pytań o opakowania awaryjne.
- **0532** vs 0241, 0530 – inny zapis/punkt.
- **0533** vs 0050, 0589, 0620, 0716 (język instrukcji pisemnych 5.4.3.2) – inny punkt.
- **0534 nowa** vs 0528, 0605, 0609, 0689 – brak pytania o ostatni akapit 3.4.11.
- **0535** – brak innych pytań o 3.4.12.
- **0536** vs 0523, 0524, 0525 (pojedyncze elementy (c), (d), (k)) – inny element (kolejność).
- **0537 nowa** vs 0069, 0070, 0227, 0578, 0599 – brak pytania o kod opakowania.
- **0538** vs 0492 (7.5.2 – osobne dokumenty nie znoszą zakazu) – inny przypadek z 5.4.1.4.2.
- **0539 nowa** vs 0033 (D/E w sztukach → tylko E), 0208, 0248, 0064, 0086, 0263, 0432, 0574, 0771 – brak pytania o wiersz B/D.
- **0540** vs 0209 (5 t LQ → bez znaków, odwrotny wynik), 0512 (usunięcie znaków po rozładunku), 0772 (8.6.3.3 i kod całego ładunku), 0085 – 0540 to jedyne pytanie „znaki LQ wymagane → omijasz tunel E”.

## Ustalenia dla poszczególnych pytań (cytaty, strony Dz.U., klucze)

### ADR-B-0526 – POPRAW (01-K05, A) – przeredagowane (#903: OK; strona 693, nie 676)
- 3.5.5 (s. 693, obraz strony): „Liczba sztuk przesyłek w pojeździe lub kontenerze nie powinna być większa niż 1 000.” Klucz A ✔.

### ADR-B-0527 – POPRAW (01-K05, B) – NOWY ELEMENT (= 0573; strona 693, nie 676)
- 3.5.6 (s. 693) – dotychczasowy temat, jak w 0573. Nowy: 3.5.4.1 (s. 692, obraz strony): „Na znaku powinna być umieszczona pierwsza cyfra lub pojedynczy numer nalepki ostrzegawczej wskazany w kolumnie (5) tabeli A w dziale 3.2 dla każdego towaru zawartego w tej sztuce przesyłki. Jeżeli nazwa nadawcy lub odbiorcy nie jest umieszczona w innych miejscach sztuki przesyłki, to te informacje powinny być umieszczone na tym znaku.” Rys. 3.5.4.2: „* W tym miejscu powinien być umieszczony numer pierwszej lub pojedynczej nalepki ostrzegawczej …; ** … nazwa nadawcy lub odbiorcy …”; „Minimalne wymiary powinny wynosić 100 mm x 100 mm.” Klucz B ✔.

### ADR-B-0528 – POPRAW (01-K05, C) – przeredagowane (strona 693, nie 675)
- 3.5.4.3 (s. 693, obraz strony): „Jeżeli oznakowania wymagane dla wszystkich towarów niebezpiecznych nie są widoczne, to opakowanie zbiorcze należy: (a) oznakować napisem „OPAKOWANIE ZBIORCZE”. Litery napisu … co najmniej 12 mm wysokości. Napis powinien być sporządzony w języku urzędowym państwa pochodzenia. Jeżeli nie jest to język angielski, francuski lub niemiecki, to również w języku angielskim, francuskim lub niemieckim, jeżeli umowy … nie stanowią inaczej; oraz (b) umieścić znaki wymagane w niniejszym dziale.” Klucz C ✔.

### ADR-B-0529 – POPRAW (01-K02, A) – przeredagowane (strona 54, nie 55)
- 1.3.2.3 (s. 54): „Pracownicy powinni przejść szkolenie na temat zagrożeń stwarzanych przez towary niebezpieczne, odpowiednio do stopnia ryzyka utraty zdrowia lub narażenia, mogących być skutkiem wypadku przy przewozie takich towarów, z uwzględnieniem ich załadunku i rozładunku. Celem szkolenia powinno być zapoznanie pracowników z bezpiecznymi sposobami postępowania oraz z procedurami ratowniczymi.” Klucz A ✔.

### ADR-B-0530 – POPRAW (13-K08, B) – NOWY ELEMENT (= 0008/0046/0179/0294/0629/0680; strona 962, nie 963)
- 5.4.1.1.3.1 (s. 962) – dotychczasowy temat. Nowy: 5.4.1.1.6.2.1 (s. 964): „W przypadku próżnych nieoczyszczonych opakowań zawierających pozostałości towarów niebezpiecznych klas innych niż klasa 7 …, informacje podane w 5.4.1.1.1 (a), (b), (c), (d), (e) i (f) zastępuje się odpowiednio zapisami „PRÓŻNE OPAKOWANIE”, „PRÓŻNE NACZYNIE”, „PRÓŻNY DPPL” lub „PRÓŻNE OPAKOWANIE DUŻE”, uzupełnionymi następującą po nich informacją o ostatnio załadowanych towarach, podaną w 5.4.1.1.1 (c), np.: „PRÓŻNE OPAKOWANIE, 6.1 (3)”.” 5.4.1.1.6.2.2 (s. 964): „… „PRÓŻNY POJAZD”, „PRÓŻNY KONTENER” … uzupełnionymi … zapisami „OSTATNI ŁADUNEK:”.” Klucz B ✔.

### ADR-B-0531 – POPRAW (13-K08, C) – przeredagowane
- 5.4.1.1.5 (s. 964): „W przypadku przewozu towarów niebezpiecznych w opakowaniu awaryjnym zgodnie z 4.1.1.19 … po ich opisie w dokumencie przewozowym należy dodać zapis „OPAKOWANIE AWARYJNE”.” Klucz C ✔.

### ADR-B-0532 – POPRAW (13-K08, A) – przeredagowane
- 5.4.1.1.6.1 (s. 964): „W przypadku próżnych nieoczyszczonych jednostek ładunkowych zawierających pozostałości towarów niebezpiecznych klas innych niż klasa 7, przed lub po informacjach o towarze niebezpiecznym, wymaganych w 5.4.1.1.1 (a) do (d) i (k), wpisuje się zapis „PRÓŻNE NIEOCZYSZCZONE” lub „POZOSTAŁOŚCI OSTATNIEGO ŁADUNKU”. Przepis 5.4.1.1.1 (f) nie ma zastosowania.” Klucz A ✔.

### ADR-B-0533 – POPRAW (13-K08, B) – przeredagowane (strona 971, nie 972)
- 5.4.1.4.1 (s. 971, obraz strony): „Informacje zamieszczone w dokumencie powinny być zapisane w języku urzędowym państwa nadania, a jeżeli nie jest to język angielski, francuski lub niemiecki, to również w języku angielskim, francuskim lub niemieckim, jeżeli umowy międzynarodowe dla przewozu lub umowy zawarte między państwami uczestniczącymi w przewozie nie stanowią inaczej.” Klucz B ✔.

### ADR-B-0534 – POPRAW (01-K05, A) – NOWY ELEMENT (≈ 0528; strona 688, nie 671)
- 3.4.11 (s. 688): „… opakowanie zbiorcze należy: (a) oznakować napisem „OPAKOWANIE ZBIORCZE” … oraz (b) umieścić znaki wymagane w niniejszym dziale. Za wyjątkiem transportu lotniczego, pozostałe wymagania podane w 5.1.2.1 obowiązują jedynie wówczas, gdy w opakowaniu zbiorczym umieszczone są inne towary niebezpieczne, które nie są zapakowane w ilościach ograniczonych, i wyłącznie w odniesieniu do tych innych towarów niebezpiecznych.” 5.1.2.1 (s. 928) – „OPAKOWANIE ZBIORCZE”, numery UN i nalepki. Klucz A ✔.

### ADR-B-0535 – POPRAW (01-K05, B) – przeredagowane (strona 688, nie 671)
- 3.4.12 (s. 688): „Przed rozpoczęciem przewozu, nadawcy towarów niebezpiecznych zapakowanych w ilościach ograniczonych, powinni przekazać przewoźnikowi w udokumentowany sposób informacje o całkowitej masie brutto tak nadawanych towarów.” Klucz B ✔.

### ADR-B-0536 – POPRAW (13-K01, C) – przeredagowane
- 5.4.1.1.1 (s. 962): „Umiejscowienie i kolejność informacji wymaganych w dokumencie przewozowym są dowolne, z wyjątkiem informacji wymaganych w (a), (b), (c), (d) i (k) które powinny być podane w kolejności określonej powyżej (tj. (a), (b), (c), (d), (k)), bez żadnych dodatkowych informacji pomiędzy nimi, jeżeli nie są one dopuszczone w ADR. … „UN 1098 ALKOHOL ALLILOWY, 6.1 (3), I, (C/D)”.” Klucz C ✔.

### ADR-B-0537 – POPRAW (13-K02, A) – NOWY ELEMENT (= 0070; #903: OK)
- 5.4.1.1.1 (f) (s. 962) – dotychczasowy temat. Nowy: (e) (s. 962): „liczbę i określenie sztuk przesyłek, jeżeli występują; kod opakowania może być użyty jedynie jako uzupełnienie określenia sztuki przesyłki (np. jedna skrzynia (4G))”. Klucz A ✔.

### ADR-B-0538 – POPRAW (13-K08, B) – przeredagowane
- 5.4.1.4.2 (s. 972): „Jeżeli ze względu na wielkość ładunku przesyłka nie może być załadowana w całości do jednej jednostki transportowej, to należy sporządzić dla tej przesyłki odrębne dokumenty lub kopie jednego dokumentu, odpowiednio do ilości załadowanych jednostek transportowych. Ponadto, odrębne dokumenty przewozowe powinny być sporządzone we wszystkich przypadkach, gdy przesyłki lub ich części nie mogą być załadowane razem … ze względu na zakazy podane w 7.5.2.” Klucz B ✔.

### ADR-B-0539 – POPRAW (11-K03, B) – NOWY ELEMENT (≈ 0064/0086/0263/0432/0574/0771; #903: OK; 8.6.3.2 na s. 1338)
- 8.6.3.1 (s. 1338, obraz strony): „Kod ograniczeń przewozu przez tunele podany jest w nawiasie w dolnej części komórki.” Tabela 8.6.4 (s. 1339, obraz strony), wiersz B/D: „Przewóz w cysternie: zakaz przewozu przez tunele kategorii B, C, D i E; Inny przewóz: zakaz przejazdu przez tunele kategorii D i E.” 8.6.4 (s. 1338): „do jednostek transportowych, dla których, zgodnie z 5.3.2, wymagane jest oznakowanie tablicami barwy pomarańczowej, zgodnie z poniższą tabelą …”. Klucz B ✔.

### ADR-B-0540 – POPRAW (11-K05, C) – przeredagowane (strony 688, 689, 1338 – nie 671 i 1339)
- 3.4.13 (a) (s. 688): „Jednostki transportowe o masie maksymalnej powyżej 12 ton, przewożące towary niebezpieczne zapakowane w ilościach ograniczonych, powinny być oznakowane z przodu i z tyłu zgodnie z 3.4.15 …”. 3.4.14 (s. 689): „Znaki podane w 3.4.13, nie są wymagane, jeżeli całkowita masa brutto … nie przekracza 8 ton na jednostkę transportową.” 3.4.15 (s. 689): „Oznakowanie to należy usunąć lub zakryć, gdy nie są przewożone towary niebezpieczne zapakowane w ilościach ograniczonych.” 8.6.4 (s. 1338, obraz strony): „do jednostek transportowych, dla których, na podstawie 3.4.13, z zastrzeżeniem 3.4.14, wymagane jest oznakowanie, w przypadku tuneli kategorii E”. Klucz C ✔.

## Wskaźniki

- „Poprawna = jedyna najdłuższa”: **30/780 = 3,85% → 29/780 = 3,72%** (0532), maksimum działu **6,74%** (bez zmian) – **zmienić** linie w `docs/POKRYCIE-KURSU.md` i `podstawowy/README.md` (`review/specialist/PAKIET-ZAMKNIECIE-0780.md` to historyczny raport zamknięcia z własnym blobem – bez zmian, jak w #902).
- „Poprawna = jedyna najkrótsza”: **141 → 133/780**; ADR-B-01 25,9% → **20,4%**, ADR-B-13 25,9% → **16,7%**, ADR-B-11 bez zmian (10,9%); maksimum działu 26,4% (bez zmian); wszystkie działy ≤ 38%.
- 15 nowych wyjaśnień: po 5 zdań, 399–541 znaków, maks. 31 słów w zdaniu, na końcu „Podstawa: ADR …”; opcje 53–80 znaków; bez słów absolutnych i średników w opcjach; klucz nigdzie nie jest jedyną najdłuższą ani jedyną najkrótszą.

## Egzaminy, kolejki, snapshoty (pułapki CI)

- Egzaminy próbne – w `questions`: **0526, 0538, 0532 – wariant-004/klucz-004; 0537 – wariant-005/klucz-005**. Na liście `excluded_question_ids` wariantu 005: 0526, 0532, 0538 – **nie zmieniać**. Pozostałe pliki egzaminów – tylko SHA.
- `review/specialist/KOLEJKA-PRIORYTETOWA-4X40.json` zawiera **0530, 0534, 0537, 0536**; `4X44` zawiera **0528** („question” + „legal_basis”).
- Snapshoty: `review/sequential/` i `review/legal-clauses/` – pliki **526-533.json** (0526–0533), **534-538.json** (0534–0538), **539-540.json** (0539, 0540); clause, answer_review A/B/C, notes_on_conditions ≥ 25 zn. Zaległość #902: legal-clauses **510-512.json, 513-519.json, 520-525.json** – clause/answer_review/notes dla 0511–0524 (wartości z polecenia 35).
- Ledger `review/legal-polish/stage4w4-literal-verification-ledger-0001-0609.json`: `source_references` z nowych sources – zmienia się 8 (0527, 0530, 0531, 0534, 0536, 0537, 0539, 0540).
- Rejestry `REJESTR-AKTUALNY-0001-0765.md` i `-0001-0780.md`: po **29 wierszy** (15 z partii 36 + 14 zaległych z partii 35).
- SHA banku e0c67175… występuje w **36 plikach** poza historycznymi raportami `review/literal-pl/`: **35 zamienianych wprost** (docs/POKRYCIE-KURSU.md, podstawowy/README.md, review/README.md, podstawowy/raporty/etap-4x135-wykluczenia-proby.json, review/specialist: INSTRUKCJA-RECENZJI.md, PRZEKAZANIE-ETAP4.md, PAKIET-0628-MANIFEST.json, KOLEJKA-PRIORYTETOWA-4X40.json, KOLEJKA-PRIORYTETOWA-4X44.json, REJESTR-AKTUALNY-0001-0765.md, 10 plików egzaminów, tests/test_literal_review_0301_0315 … 0511_0525 (15 plików; w 0511_0525 tylko EXPECTED_BANK_SHA – FIRST_PASS_BANK_SHA = f732aa35… zostaje; w 0301_0315 zbiór dopuszczalnych blobów)) + `tests/test_literal_review_0526_0540.py` – **specjalnie** (niżej). Do tego zaległość #902: **f732aa35… → nowy** w docs/STAN-KONCOWY-BANKU-ADR-PODSTAWOWY-2026-11-03.md (2×), review/specialist/PAKIET-0780-MANIFEST.json (7×), review/specialist/REJESTR-AKTUALNY-0001-0780.md (1×).
- `tests/test_literal_review_0526_0540.py`: dodać FIRST_PASS_BANK_SHA = e0c67175… (asercja manifestu `bank_blob_sha`), EXPECTED_BANK_SHA = nowy (bank); `previous_uncompared` 270 → **255**, `remaining_without_comparison` 255 → **240** (także w PARTIA-0526-0540.json i w zdaniu licznika w .md); `EXPECTED_PAGES` i `gazette_pages`/`gazette_page` w .json – poprawione strony; `test_bank_unchanged_and_batch_unverified` → `test_bank_after_second_pass_keeps_780_records_unverified`; docstring; nowy `test_second_pass_artifacts_and_bank_sha`.
- Oczekiwany SHA banku: **e0c671756644994d18480feae5c08bc70ee0ffbd → 73aa25f2ae5fed6f40b1948dfb917f082c08b58e**.

## Test na kopii repo

`test_p36.sh` (kopia /tmp/b36 z main **cfd22cb9e** = po scaleniu #903, bez commitów i pushu): `apply_poprawki.py` → „Changed (15): ADR-B-0526 … ADR-B-0540”, blob **73aa25f2ae5fed6f40b1948dfb917f082c08b58e**; po synchronizacji (`sync_p36_test.py`; razem 55 zmienionych/nowych plików, w tym bank, `tools/apply_poprawki.py`, POPRAWKI i KONTROLA2) wszystkie 14 skryptów CI = 0 i `python3 -m unittest discover -s tests` – **221 testów OK**.

## Licznik

Po wdrożeniu partii 36 (obie kontrole 0526–0540): **240 pytań bez porównania dosłownego po obu kontrolach** (0541–0780); kontrola pierwsza partii 37 (0541–0555): 240 → 225.

## Do zapamiętania na kolejne partie
- ChatGPT nadal bierze **stopkę ADR** zamiast nagłówka Dz.U. (671/675/676 – tak jak 604 w partii 35) i myli o +1 (55, 963, 972). Test #903 utrwalił błędne strony – w poleceniu wymagać sprawdzenia, że żadna podana strona nie jest numerem stopki (stopka ≈ nagłówek − 17 w dziale 3, − 705 w dziale 5, − 705 w dziale 8).
- 11-K03, 11-K05 i 13-K02 mają dokładnie 6 pytań; 8.6.3.2 (kod najbardziej restrykcyjny) ma już 6 pytań w 11 – każde kolejne to duplikat. Temat „ODPAD” (5.4.1.1.3.1) ma 7 pytań – nie dokładać.
- 0689 (5.1.2.1) używa „OVERPACK” zamiast „OPAKOWANIE ZBIORCZE” – poprawić w partii 46 (0676–0690).
- 0247 i 0770 dublują się wzajemnie (1.1.4.2.1 akapit ostatni) – partia 52; 0632, 0071/0072 – przy właściwych partiach.