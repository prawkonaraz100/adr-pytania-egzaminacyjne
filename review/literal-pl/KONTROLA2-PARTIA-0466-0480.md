# Kontrola druga – partia ADR-B-0466–0480 (porównanie dosłowne z polskim tekstem ADR 2025)

Data: 2026-11-10, ok. 00:30 (czas polski, CET).
Przedmiot: pierwsza kontrola ChatGPT (PR #894 + korekta stron PR #895, scalone; main **93991ba94**; `review/literal-pl/PARTIA-0466-0480.md` + `.json` + `tests/test_literal_review_0466_0480.py`, wynik 1 OK / 14 POPRAW / 0 BLOKUJ) oraz rekordy 0466–0480 na main (bank blob **e560a389…**, 780 pytań; #894/#895 banku nie zmieniają).
Źródło: Dz.U. 2025 poz. 642 (skany PDF), OCR tesseract `-l pol`; strony wg nagłówka „Dziennik Ustaw — NNN —”. Na **obrazie strony PDF** sprawdzona s. 966 (5.4.1.1.18 – nagłówek „– 966 –”; OCR odczytał go jako „066”). Pozostałe strony wg nagłówków OCR: s. 57 (1.4.2.3, 1.4.3.1), s. 58–59 (1.4.3.7), s. 937–938 (5.2.1.8), s. 950–952 (5.3.1.1.1, 5.3.1.2, 5.3.1.4, 5.3.1.5), s. 960 (5.3.6), s. 975 (instrukcje pisemne), s. 1304 (7.5.1), s. 1332 (8.3), s. 1333 (8.4.1), s. 1336–1337 (S14–S24). Sprostowanie poz. 1575 nie dotyczy punktów tej partii.
Status: kontrola robocza. **Żadne pytanie nie jest oznaczone jako zweryfikowane**; wszystkie pozostają `needs_review`.

## Podsumowanie

- Werdykty kontroli drugiej: **OK 0, POPRAW 15, BLOKUJ 0** (#894: 1 OK – 0469 nie jest OK, niżej).
- **7 pytań → nowy element z tej samej kompetencji, niecysternowy**:
  - 0470 – temat cysternowy (kontener-cysterna ≤ 3 000 l, znak 100 × 100 mm) → pojazd z samymi sztukami przesyłek UN 3082 nie ma dużych nalepek, więc 5.3.6.1 nie wymaga znaku na pojeździe (5.3.1.5);
  - 0471 = 0136/0196 (8.3.1 – pasażer) → S14: nadzór 8.4 przy jakiejkolwiek ilości, bez wyjątku zamkniętego przedziału (inaczej niż S15 w 0347);
  - 0473 = 0664 (8.3.8 – złącza ABS) → S17: liczy się masa całkowita w pojeździe (2 × 600 kg = 1 200 kg > 1 000 kg);
  - 0474 ≈ 0138/0560 (niezgodność pojazdu/wyposażenia → nie ładować) i 0239 (kontrola dokumentów kierowcy) → 7.5.1.2: istotna wada konstrukcyjna kontenera wielkiego (pęknięty słupek naroża, lit. (a));
  - 0475 ≈ 0436 (uszkodzenia ścian/podłogi kontenera) → 7.5.1.2: kontener wielki bez wymaganej odporności na warunki atmosferyczne (dziura w dachu, klasa 4.3);
  - 0478 ≈ 0477 (1.4.3.7.2 dla rozładowcy = ta sama norma co 1.4.2.3.3 dla odbiorcy: „korzysta z usług innych … zastosować odpowiednie środki”) → 1.4.3.7.1 (e): rozładowca zapewnia wymagane oczyszczenie i odkażenie (1.4.3.7.2 w wyjaśnieniu);
  - 0479 ≈ 0482 (ten sam punkt 1.4.3.1.2 – polegać na danych innych uczestników) i 0378 (zakazy ładowania razem) + **błędne odesłanie w kluczu** („1.4.3.1.2(a), (d) i (e)” – litery należą do 1.4.3.1.1) → nowy aspekt tego samego punktu: granica 1.4.3.1.2 – przy 1.4.3.1.1 (b) (sprawdzenie opakowań) nie można polegać na danych nadawcy.
- **8 pytań** (0466, 0467, 0468, 0469, 0472, 0476, 0477, 0480) ma właściwy podtemat, ale wady formy/treści → przeredagowane w tym samym podtemacie. **0466 – nie-polskie brzmienie** („dodatkowy wpis ENVIRONMENTALLY HAZARDOUS” w treści i wyjaśnieniu; polski 5.4.1.1.18: „ZAGRAŻAJĄCY ŚRODOWISKU” lub „MARINE POLLUTANT / ENVIRONMENTALLY HAZARDOUS”) – poprawione. **0477 (07-K04 = dokładnie 6)** – tylko przeredagowanie, temat 1.4.2.3.3 zostaje.
- **Żaden zamiennik nie jest cysternowy** (w treści i opcjach nowych elementów brak „cystern”); 0469 przeredagowane na pojazd do przewozu luzem (wywrotka), nie na cysternę.
- Wszędzie ta sama litera klucza, ten sam `module_id`, `image` = null; przypisania w `kompetencje.json` bez zmian (03-K01 = 13, 04-K05 = 11, 04-K06 = 15, **07-K04 = 6**, 07-K05 = 16; każda kompetencja teoretyczna ≥ 6, minimum 6).
- **Wady formy starych wersji**: opcje > 80 zn. – 0468 A (81), 0470 A/B (81/81), 0471 B (98), 0474 B (88), 0479 A/B (102/92), 0480 B (84); średniki – 0466 C, 0471 C, 0477 B, 0479 A/B; kropki na końcu opcji – 0479 A/B; słowa absolutne – 0466 A „zawsze … niezależnie”, B „tylko”, 0467 B „zawsze”, C „wyłącznie”, 0468 A „wyłącznie”, B „nigdy … tylko”, 0470 B „całkowicie … każdej”, 0471 A „tylko”, 0472 A „wyłącznie”, 0476 B „Każdy”, 0477 A „wszystkie … automatycznie”, 0478 B „automatycznie … wszystkie”, 0479 A „wszystkie”; klucz jedyną najkrótszą – 0466, 0467, 0472, 0477, 0478, 0479; klucz odsyła sam do siebie – 0467 („na warunkach 5.4.1.1.18”), 0468 („jeśli 5.3.6.1 ma zastosowanie”), 0480 („zgodnie z wymaganiami ADR 1.4.3.7.1(d)(i)”); zmyślone warunki w dystraktorach – 0466 B (tunel), 0467 B („numer faktury”), C (klasa 7); opcje-szablony – 0469 (wszystkie trzy z dopiskiem „— wymiar standardowy bez zastosowania zmniejszenia”); w wyjaśnieniach polecenia „Sprawdź…/zweryfikuj” zamiast wyjaśnienia (0467, 0468, 0469, 0470), „automatycznie” (0467, 0477, 0478).

## Błędy / różnice względem raportu ChatGPT (#894/#895)

1. **Błędna strona Dz.U. dla 5.4.1.1.18 (0466, 0467): „066” zamiast 966.** #895 miał poprawić strony według drukowanego nagłówka, ale przepisano błędny odczyt OCR („Dziennik Ustaw — 066 —”, w OCR oznaczony „[nr strony wyliczony]”). Na obrazie strony PDF (część 20, s. 16) nagłówek to „– 966 –”. Pozostałe strony (960, 1332, 1304, 57, 59) – poprawne.
2. **0469 nie jest OK**: pytanie abstrakcyjne, wszystkie opcje z identycznym dopiskiem, wyjaśnienie nie mówi, skąd są liczby (100 × 100 mm to minimum na sztuce przesyłki z 5.2.1.8.3, a 50 × 50 mm nie ma podstawy), polecenie „zweryfikuj znak” zamiast wyjaśnienia.
3. **Przeoczone duplikaty / bliskie powtórzenia**: 0474 (#894: „nie jest duplikatem 0138, 0560 ani 0239”) – klucz 0474 „wstrzymać załadunek do usunięcia niezgodności” = klucz 0138 („Wstrzymać załadunek, dopóki ta niezgodność nie zostanie usunięta”) i 0560; 0478 ≈ 0477 (ta sama norma dla innej roli, oba „zlecenie nie zwalnia”); 0479 ≈ 0482 (ten sam punkt 1.4.3.1.2). **0470 – temat cysternowy** tylko skrócony zamiast zastąpienia.
4. **Propozycje zastępcze z wadami**: 0475 (załoga nie gasi pożaru przedziału ładunkowego) **dubluje 0107, 0166, 0614, 0641** (oraz 0702, 0742, 0222) – duplikat we własnej propozycji; 0471 (S21) – materiały promieniotwórcze klasy 7 to zakres kursu specjalistycznego (8.2.1.4; por. 0160), opcje z kropkami; 0473 (S17) – kierunek dobry, ale B „wyłącznie”, kropki w opcjach, wyjaśnienie bez sedna (liczy się suma w pojeździe – tego uczy nowa 0473).
5. **Przeoczone błędy treści**: 0466 – brzmienie „wpisu ENVIRONMENTALLY HAZARDOUS” (#894 widzi tylko długości i średnik); 0479 – błędne odesłanie „1.4.3.1.2(a), (d) i (e)” w kluczu (#894 pisze, że klucz „nie wskazuje obowiązków (a), (d) i (e)”, a on je wskazuje – przy złym punkcie); klucze odsyłające same do siebie w 0467 i 0480; zmyślone warunki 0466 B, 0467 B/C; słowa absolutne w 0466, 0467, 0468, 0470, 0476, 0477, 0478.
6. **Test bez FIRST_PASS_BANK_SHA**: `tests/test_literal_review_0466_0480.py` ma jedną stałą EXPECTED_BANK_SHA, używaną i dla manifestu, i dla banku (polecenie wymagało od razu dwóch stałych). Przy wdrożeniu trzeba dodać FIRST_PASS_BANK_SHA = e560a389… (manifest) i ustawić EXPECTED_BANK_SHA na nowy SHA (bank).
7. **Znowu bez repozytoryjnego similarity.py** („Uruchomiono tę samą logikę…” – własna implementacja). Na kopii po poprawkach `similarity.py --threshold 0.25`: pary z partią – 0345/0473 = 0,391 (S16 próg 500 kg vs S17 suma w pojeździe – inne przepisy i inna reguła), 0464/0468 = 0,350 (znak na kanistrze vs na kontenerze), 0464/0470 = 0,292, 0463/0470 = 0,259. `check_near_duplicates.py --threshold 0.40` – brak par z partią.
8. **Słusznie w #894**: 0471 = 0136/0196; 0473 = 0664; 0475 ≈ 0436; 0476 – brak warunku „braki mogące mieć negatywny wpływ na bezpieczeństwo lub ochronę”; 0477 – klucz ogólnikowy i ograniczenie 07-K04 = 6 (tylko przeredagowanie); 0478 – klucz ogólnikowy; 0468 – klucz tautologiczny, A 81 zn.; 0470, 0474, 0479, 0480 – długości opcji; cytaty dosłowne; licznik 315 → 300.

## Duplikaty – sprawdzenie w całym banku (780) i między sobą

Przeszukano cały bank po temacie (5.4.1.1.18, ZAGRAŻAJĄCY ŚRODOWISKU, MARINE POLLUTANT, UN 3077/3082, 5.3.6, duże nalepki, 5.3.1.5, 250/100 mm, 8.3.1 pasażer, 8.3.2/gaśnice, 8.3.8/ABS, 8.4, S1–S24, 1 000 kg, 7.5.1.1–7.5.1.3, uszkodzenia kontenera, zawiasy/naroża/odporność na warunki atmosferyczne, instrukcje pisemne – pożar ładunku, opony/hamulce/silnik, 1.4.2.3, 1.4.3.1, polegać na danych, 1.4.3.7, oczyszczenie/odkażenie, 7.5.8, pozostałości na zewnątrz) oraz skryptami `check_near_duplicates.py` (0,60 i 0,40), `check_cross_module_duplicates.py` (0,80), `similarity.py` (0,45; dodatkowo 0,25) na kopii po poprawkach.
- **0466** (wyłączenie UN 3077/3082 z dodatkowego zapisu) vs **0465** (brzmienie zapisu dla UN 1993), **0467** (sam „MARINE POLLUTANT” w łańcuchu morskim – UN 1263, nie UN 1993 jak w 0465) – trzy różne zdania 5.4.1.1.18.
- **0468** (kontener z dużymi nalepkami → znak środowiskowy na kontenerze) vs **0470 nowa** (pojazd z samymi sztukami przesyłek → bez dużych nalepek, bez znaku na pojeździe) – dwie strony warunku 5.3.6.1; vs 0464 (znak na kanistrze oprócz nalepki 9), 0045 (miejsce znaku), 0132/0299/0561 (miejsca dużych nalepek – dział 06) – inne elementy. **0469** (250 × 250 mm na pojeździe) vs 0007/0276 (symbol, tło) – inny element; 100 × 100 mm z kontenera-cysterny już nie występuje.
- **0471 nowa** (S14 – bez wyjątku) vs 0347 (S15 – wyjątek zamkniętego przedziału), 0345 (S16 – próg 500 kg), 0131/0350 (kiedy 8.4 / limit 1.1.3.6) – inna reguła. **0473 nowa** (S17 – suma w pojeździe) vs 0345 (S16 – 400 kg poniżej progu) – inny przepis i inna reguła (sumowanie), similarity 0,391.
- **0472** (8.3.2 – wiedza załogi) vs 0015 (montaż gaśnic), 0108/0184/0493/0695 (kiedy wolno gasić – 5.4.3.4), 8.1.4 (liczba/pojemność gaśnic) – inny element.
- **0474 nowa** (istotna wada konstrukcyjna – słupek naroża) i **0475 nowa** (odporność na warunki atmosferyczne) vs 0436 (wystające części), 0554 (pozostałości), 0138/0560 (ogólna niezgodność), 0239 (zaświadczenie kierowcy), 0202 (7.5.1.1) – w banku brak pytań o konstrukcyjną zdatność i odporność na warunki atmosferyczne. **0476** – jedyne pytanie o 7.5.1.3.
- **0477** (odbiorca – 1.4.2.3.3) vs 0195 (zwrot kontenera – 1.4.2.3.2), 0118/0246/0757 (1.4.2.3.1), 0377 (definicja), 0365 (nadawca – 1.4.2.1.2). **0478 nowa** (rozładowca zapewnia oczyszczenie i odkażenie – 1.4.3.7.1 (e)) vs 0372 (lit. (f) – nalepki po oczyszczeniu), 0009/0080/0177/0240/0514/0706/0769 (7.5.8.1 – kiedy i gdzie czyścić) – inny element (kto). **0479** (granica 1.4.3.1.2 – (b)) vs 0482 (polega na danych przy (d)), 0378 ((e)), 0373 ((a)), 0020/0054/0245/0517/0584 (uszkodzone opakowanie – czy wydać) – inny aspekt. **0480** ((d) (i) – pozostałości na zewnątrz) vs 0481 ((d) (ii) – zawory) – różne litery.

## Ustalenia dla poszczególnych pytań (cytaty, strony Dz.U., klucze)

### ADR-B-0466 – POPRAW (03-K01, C) – przeredagowane (nie-polskie brzmienie)
- 5.4.1.1.18 (s. 966): „…dokument przewozowy powinien zawierać dodatkowy zapis „ZAGRAŻAJĄCY ŚRODOWISKU” lub „MARINE POLLUTANT / ENVIRONMENTALLY HAZARDOUS”. Tego dodatkowego zapisu nie stosuje się do UN 3077 i UN 3082 oraz w przypadku wyłączeń podanych w 5.2.1.8.1.” Klucz C „Nie, 5.4.1.1.18 wyłącza z tego dodatkowego zapisu UN 3077 i UN 3082” ✔.

### ADR-B-0467 – POPRAW (03-K01, A) – przeredagowane
- 5.4.1.1.18 (s. 966): „W przypadku przewozu w łańcuchu transportowym obejmującym przewóz morski dopuszcza się stosowanie zapisu „MARINE POLLUTANT” (zgodnie z przepisem 5.4.1.4.3 Kodeksu IMDG).” Klucz A ✔ (UN 1263 – inny materiał niż UN 1993 w 0465).

### ADR-B-0468 – POPRAW (03-K01, C) – przeredagowane
- 5.3.6.1 (s. 960): „Jeżeli wymagane jest umieszczenie dużej nalepki ostrzegawczej, zgodnie z przepisami rozdziału 5.3.1, to kontenery, … i pojazdy zawierające materiały zagrażające środowisku, spełniające kryteria podane w 2.2.9.1.10 powinny być oznakowane znakiem dla materiałów zagrażających środowisku, podanym w 5.2.1.8.3.” 5.3.1.2 (s. 951) – duże nalepki na kontenerach. Klucz C ✔.

### ADR-B-0469 – POPRAW (03-K01, C) – przeredagowane (#894: OK)
- 5.3.6.2 (s. 960): „…z wyjątkiem tego, że minimalne wymiary powinny wynosić 250 mm × 250 mm.” 5.2.1.8.3 (s. 938): „Minimalne wymiary powinny wynosić 100 mm × 100 mm…” (sztuka przesyłki). Wywrotka luzem – duże nalepki wg 5.3.1.4.1 (s. 951). Klucz C „250 mm × 250 mm, czyli więcej niż na sztuce przesyłki” ✔.

### ADR-B-0470 – POPRAW (03-K01, A) – NOWY ELEMENT, NIECYSTERNOWY
- 5.3.6.1 (s. 960) – jw. (warunek: wymagane duże nalepki); 5.3.1.5 (s. 952) „Umieszczanie dużych nalepek ostrzegawczych na pojazdach przewożących wyłącznie sztuki przesyłek”: 5.3.1.5.1 – klasa 1 (poza 1.4S), 5.3.1.5.2 – klasa 7. Pojazd z samymi kanistrami UN 3082 dużych nalepek nie ma → znak z 5.3.6.1 nie jest wymagany na pojeździe (na kanistrach – tak, 5.2.1.8.1). Klucz A ✔. Do oceny specjalisty.

### ADR-B-0471 – POPRAW (04-K06, C) – NOWY ELEMENT (duplikat 0136/0196)
- 8.5 S14 (s. 1336): „Przepisy działu 8.4 dotyczące nadzorowania pojazdów mają zastosowanie do pojazdów przewożących jakąkolwiek ilość tych materiałów.” S15 (s. 1336) – „Jednakże, przepisy działu 8.4 nie muszą być stosowane w przypadku, gdy przedział ładunkowy jest zamknięty…”; S16 (s. 1337) – 500 kg. UN 1017 chlor – kolumna (19) S14 (tabela A). Klucz C ✔.

### ADR-B-0472 – POPRAW (04-K05, C) – przeredagowane
- 8.3.2 (s. 1332): „Członkowie załogi pojazdu powinni wiedzieć, jak należy używać środków do gaszenia pożaru.” Instrukcje pisemne (5.4.3.4, s. 975): gaśnice – mały/początkowy pożar opon, hamulców, przedziału silnika; „Członkowie załogi pojazdu nie powinni gasić pożaru obejmującego przedział ładunkowy”. Klucz C (brzmienie przepisu, „środki do gaszenia pożaru”) ✔.

### ADR-B-0473 – POPRAW (04-K06, C) – NOWY ELEMENT (duplikat 0664)
- 8.5 S17 (s. 1337): „…mają zastosowanie w przypadku, gdy masa całkowita tych materiałów w pojeździe przekracza 1 000 kg.” S18 (s. 1337) – 2 000 kg; 8.4.1 (s. 1333). Klucz C ✔.

### ADR-B-0474 – POPRAW (04-K05, A) – NOWY ELEMENT, NIECYSTERNOWY (≈ 0138/0560/0239)
- 7.5.1.2 (s. 1304): „Jednostka transportowa cargo powinna być sprawdzona w celu zapewnienia, że jest ona konstrukcyjnie zdatna do użytku…”; „Elementami konstrukcyjnymi … są, np. … słupki naroża i naroża mocujące…”; „Za istotne wady uważa się: (a) wygięcie, pęknięcie lub złamanie elementów konstrukcyjnych…”. Klucz A ✔. Do oceny specjalisty.

### ADR-B-0475 – POPRAW (04-K05, C) – NOWY ELEMENT, NIECYSTERNOWY (≈ 0436)
- 7.5.1.2 (s. 1304): „…a kontener wielki nie jest uszkodzony w stopniu mającym wpływ na jego odporność na warunki atmosferyczne, o ile jest to wymagane.” Klasa 4.3 – w zetknięciu z wodą wydziela gazy palne (2.2.43.1.1). Klucz C ✔. Do oceny specjalisty.

### ADR-B-0476 – POPRAW (04-K05, C) – przeredagowane
- 7.5.1.3 (s. 1304): „Jeżeli w ADR nie postanowiono inaczej, to rozładunek nie powinien się odbyć, jeżeli kontrola, o której mowa powyżej, ujawniła braki mogące mieć negatywny wpływ na jego bezpieczeństwo lub ochronę.” 7.5.1.2 – kontrola obejmuje „wyposażenie używane podczas załadunku i rozładunku”. Klucz C ✔.

### ADR-B-0477 – POPRAW (07-K04, B) – przeredagowane (07-K04 = 6 – temat zostaje)
- 1.4.2.3.3 (s. 57): „Jeżeli odbiorca korzysta z usług innych uczestników przewozu (w zakresie rozładunku, czyszczenia, odkażania, itp.), to powinien zastosować odpowiednie środki w celu zapewnienia zgodności z wymaganiami ADR podanymi w 1.4.2.3.1 i 1.4.2.3.2.” Klucz B ✔.

### ADR-B-0478 – POPRAW (07-K05, C) – NOWY ELEMENT (≈ 0477)
- 1.4.3.7.1 (s. 58–59): „…rozładowca powinien w szczególności: … (e) zapewnić, aby zostało wykonane wymagane oczyszczenie i odkażenie pojazdów lub kontenerów” (s. 59); 1.4.3.7.2 (s. 59): „…powinien zastosować odpowiednie środki w celu zapewnienia zgodności z wymaganiami ADR.” Klucz C ✔.

### ADR-B-0479 – POPRAW (07-K05, C) – NOWY ASPEKT (≈ 0482/0378; błędne odesłanie w kluczu)
- 1.4.3.1.2 (s. 57): „W przypadku wymagań podanych w 1.4.3.1.1 (a), (d) i (e), załadowca może polegać na informacjach i danych udostępnionych mu przez innych uczestników przewozu.” 1.4.3.1.1 (b) (s. 57): „…sprawdzić czy opakowania nie są uszkodzone…”. Klucz C ✔.

### ADR-B-0480 – POPRAW (07-K05, A) – przeredagowane
- 1.4.3.7.1 (d) (s. 58–59): „bezpośrednio po rozładunku cysterny, pojazdu lub kontenera: (i) usunąć wszystkie niebezpieczne pozostałości towarów, które podczas czynności rozładunkowych przylgnęły do zewnętrznej powierzchni cysterny, pojazdu lub kontenera” (lit. (i) na s. 59). Klucz A ✔.

## Wskaźniki

- „Poprawna = jedyna najdłuższa”: **32/780 = 4,10% bez zmian**, maksimum działu **7,87%** bez zmian – tych linii w `docs/POKRYCIE-KURSU.md`, `podstawowy/README.md`, `PAKIET-ZAMKNIECIE-0780.md` **nie zmieniać** (tylko SHA tam, gdzie występuje).
- „Poprawna = jedyna najkrótsza”: **168 → 162/780**; ADR-B-03 18,3% → **15,0%** (9/60), ADR-B-04 8,0% → **6,0%** (3/50), ADR-B-07 24,1% → **18,5%** (10/54); maksimum działu 31,5% (bez zmian); wszystkie działy ≤ 38%.
- Wszystkie 15 wyjaśnień: 5 zdań, 458–525 znaków, maks. 31 słów w zdaniu, na końcu „Podstawa: ADR …”; opcje 53–78 znaków; bez słów absolutnych i średników w opcjach; klucz nigdzie nie jest jedyną najdłuższą ani jedyną najkrótszą.

## Egzaminy, kolejki, snapshoty (pułapki CI)

- Egzaminy próbne – w `questions`: **0478 – wariant-001/klucz-001, 0476 – wariant-002/klucz-002, 0479 i 0480 – wariant-004/klucz-004, 0473 – wariant-005/klucz-005**. Na listach `excluded_question_ids` są ID z partii (002: 0478; 003: 0476, 0478; 004: 0476, 0478; 005: 0476, 0478, 0479, 0480) – tych list **nie zmieniać**. Pozostałe pliki egzaminów – tylko SHA.
- `review/specialist/KOLEJKA-PRIORYTETOWA-4X44.json` zawiera **0473 i 0474** („question” + „legal_basis”); `4X40` – brak ID z partii.
- Snapshoty: `review/sequential/` i `review/legal-clauses/` – pliki **461-470.json** (0466–0470), **471-476.json** (0471–0476), **477-482.json** (0477–0480); clause, answer_review A/B/C, notes_on_conditions ≥ 25 zn.
- Ledger `review/legal-polish/stage4w4-literal-verification-ledger-0001-0609.json`: `source_references` z nowych sources (zmienia się 13: wszystkie poza 0466 i 0467).
- Rejestry `REJESTR-AKTUALNY-0001-0765.md` i `-0001-0780.md`: po 15 wierszy.
- SHA banku e560a389… występuje w **35 plikach** poza historycznymi raportami `review/literal-pl/`: **34 zamieniane wprost** (docs/POKRYCIE-KURSU.md, docs/STAN-KONCOWY-…, podstawowy/README.md, review/README.md, podstawowy/raporty/etap-4x135-wykluczenia-proby.json, 8 plików review/specialist, 10 plików egzaminów, tests/test_literal_review_0301_0315 … 0451_0465 (11; w 0421_0435, 0436_0450 i 0451_0465 – EXPECTED_BANK_SHA **oraz** literał w `test_second_pass_artifacts_and_bank_sha`; stałe FIRST_PASS_BANK_SHA z innym SHA zostają)) + `tests/test_literal_review_0466_0480.py` – **specjalnie**: dodać `FIRST_PASS_BANK_SHA = "e560a389…"` (dla `manifest["bank_blob_sha"]`), `EXPECTED_BANK_SHA` → nowy SHA (dla banku), test `test_bank_is_unchanged_and_all_batch_questions_remain_unverified` → `test_bank_has_expected_sha_after_second_pass_and_batch_remains_unverified`, docstring „; report-only, bank unchanged.” → „; report-only; after the second pass the bank has the expected SHA.”, EXPECTED_PAGES 0466/0467 „066” → „966”.
- Poprawka stron w raporcie #894: `PARTIA-0466-0480.json` (0466, 0467: `gazette_page` „066” → „966”, `gazette_page_header` „Dziennik Ustaw — 966 — Poz. 642”) i tabela w `PARTIA-0466-0480.md` („| 066 |” → „| 966 |”, 2 wiersze).
- Oczekiwany SHA banku: **e560a3892b2b76217bf4ff9a977a1a4c2771eff8 → ba829d36bc7e1c04aeab108d826bfae33938422f**.

## Test na kopii repo

`test_p32.sh` (kopia /tmp/b32 z main **93991ba94** = po scaleniu #894 i #895, bez commitów i pushu): `apply_poprawki.py` → „Changed (15): ADR-B-0466 … ADR-B-0480”, blob **ba829d36bc7e1c04aeab108d826bfae33938422f**; po synchronizacji (`sync_p32_test.py`, 46 zmienionych plików + nowy POPRAWKI) wszystkie 14 skryptów CI = 0 i `python3 -m unittest discover -s tests` – **202 testy OK**.

## Licznik

Po wdrożeniu partii 32 (obie kontrole 0466–0480): **300 pytań bez porównania dosłownego po obu kontrolach** (0481–0780); kontrola pierwsza partii 33 (0481–0495): 300 → 285.

## Do zapamiętania na kolejne partie
- 0481 ((d) (ii) – zawory) i 0482 (1.4.3.1.2 przy (d)) – porównać z nowymi 0478 (1.4.3.7.1 (e)), 0479 (granica 1.4.3.1.2 – (b)) i 0480 ((d) (i)); 0482 to teraz pozytywny przypadek 1.4.3.1.2 – sprawdzić, czy nie dubluje 0373/0378.
- 0247 i 0770 dublują się wzajemnie (1.1.4.2.1 akapit ostatni) – przy partii 52 (0766–0780).
- 0071/0072 (0,909) i 0632 (≈ stara 0297) – przy właściwych partiach (bez zmian).