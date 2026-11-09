# Kontrola druga – partia ADR-B-0436–0450 (porównanie dosłowne z polskim tekstem ADR 2025)

Data: 2026-11-09, ok. 20:10 (czas polski, CET).
Przedmiot: pierwsza kontrola ChatGPT (PR #890, scalony; main **29d9dc65a**; `review/literal-pl/PARTIA-0436-0450.md` + `.json` + `tests/test_literal_review_0436_0450.py`, wynik 0 OK / 15 POPRAW / 0 BLOKUJ) oraz rekordy 0436–0450 na main (bank blob **fa4e3835…**, 780 pytań; #890 banku nie zmienia).
Źródło: Dz.U. 2025 poz. 642 (skany PDF), OCR tesseract `-l pol`; strony wg nagłówka „Dziennik Ustaw — NNN —”. Strona 30 (1.1.4.2.2–1.1.4.5.3) sprawdzona na **obrazie strony PDF** (część 01, strona 30). Sprostowanie poz. 1575 nie dotyczy punktów tej partii (1.1.4.2.3, 1.1.4.3, 1.1.4.5, 1.1.4.7, 1.4.3.1.1, 4.1.6.12, 7.5.1.2).
Status: kontrola robocza. **Żadne pytanie nie jest oznaczone jako zweryfikowane**; wszystkie pozostają `needs_review`.

## Podsumowanie

- Werdykty kontroli drugiej: **OK 0, POPRAW 15, BLOKUJ 0** (zgodnie z #890 co do liczby, ale #890 przeoczył 3 duplikaty i kilka wad – niżej).
- **4 pytania to duplikaty lub bliskie powtórzenia** → **nowy temat / element z tej samej kompetencji, niecysternowy**: 0436 = 0020/0517/0555/0584/0078 (uszkodzona sztuka przesyłki – nie ładować), 0438 ≈ 0437 (ta sama reguła 1.1.4.5.1, prom zamiast wagonu), 0443 = 0442 (druga strona tego samego zdania 1.1.4.5.3), 0446 = 0444 (ta sama przesłanka daty 1.1.4.3).
- **11 pytań** (0437, 0439, 0440, 0441, 0442, 0444, 0445, 0447, 0448, 0449, 0450) ma właściwy podtemat, ale wady formy/treści → przeredagowane w tym samym podtemacie.
- **Tematy cysternowe**: 0444 i 0445 (1.1.4.3, cysterny przenośne IMO) to istniejące pytania – przeredagowane w tym samym podtemacie, bez rozszerzania; **żaden zamiennik nie jest cysternowy** (0446 → butla DOT, 4.1.6.12 (c); butla to naczynie ciśnieniowe, nie cysterna/zbiornik).
- Wszędzie ta sama litera klucza, ten sam `module_id`, `image` = null; przypisania w `kompetencje.json` bez zmian (09-K08 = 7, 10-K04 = 11, 10-K05 = 19; każda kompetencja teoretyczna ≥ 6).
- **Wady formy starych wersji**: opcje > 80 zn. – 0437 A/B/C (91/116/103), 0438 B (82), 0441 A/B (101/88), 0442 A (84), 0446 B (85), 0447 B (82), 0449 A (83); średniki – 0439 A/B, 0440 A/B/C, 0444 A/B/C, 0446 C; słowa absolutne – 0438 B „wszystkie”, 0439 A „bezwzględnie”, B „dowolne”, 0440 B „każda”, „bezwzględnie”, 0441 B „każde”, 0442 A „automatycznie wszystkie … niezależnie”, B „nigdy”, 0443 A „zawsze … żadnego”, 0444 A „wszystkich”, 0445 A „tylko”, 0446 A „niezależnie”, 0447 C „automatycznie … wszystkich”, 0448 A „dowolnego”, B/C „wyłącznie”, 0449 A „dowolnych”, 0450 A „dowolne”, B „wyłącznie”; klucz jedyną najkrótszą – 0436, 0441, 0445, 0446, 0447, 0448, 0450; kropki na końcu opcji – 0437, 0446 A/B; w wyjaśnieniu 0450 „odpowiedzi A i B”; 0440 – klucz odsyła sam do siebie („na warunkach określonych w ADR 1.1.4.5.2”), wyjaśnienie: „transport kombinowany”, „przed wyjazdem sprawdź” (kierowca nie sprawdza umów państw); 0443 – wyjaśnienie ogólnikowe („stosuje się przewidziane w przepisie pierwszeństwo”, „trzeba sprawdzić zakres”).

## Błędy / różnice względem raportu ChatGPT (#890)

1. **Przeoczone duplikaty**: 0438 ≈ 0437 (#890: „temat promu jest odrębny od 0437”) – oba pytania pytają o to samo: jakie przepisy na odcinku, na którym pojazd jedzie innym środkiem transportu; 0443 = 0442 (#890: „różne elementy”) – oba testują jedno zdanie 1.1.4.5.3 (łącznie z niesprzecznym ADR / sprzecznego ADR nie stosuje się); 0446 – #890 sam pisze „bliskie powtórzenie przesłanki daty z 0444”, ale **nie dał propozycji zastępczej** (polecenie: przy duplikacie – proposed_replacement).
2. **Błędna strona**: 0441 – akapit drugi 1.1.4.5.2 („Umowy, o których mowa, powinny być zgłaszane przez Umawiającą się Stronę będącą inicjatorem…”) stoi na **Dz.U. s. 30**, nie 31 (obraz strony PDF: koniec s. 30, przed 1.1.4.5.3). 1.1.4.5.3 zaczyna się na s. 30, zdanie cytowane w #890 jest na s. 31 – to się zgadza.
3. **Propozycja zastępcza 0436 z wadami**: opcja B „Czy kontener ma aktualną tabliczkę CSC” nie jest jednoznacznie błędna (dla kontenerów wielkich ADR wymaga zgodności z CSC – 7.1.3), więc pytanie miałoby dwie bronione odpowiedzi; wyjaśnienie mówi o „barwie wnętrza” i „miejscu na oznakowanie”, których nie ma w opcjach; treść „co oprócz czystości” jest ogólnikowa. Pomysł (7.5.1.2 akapit 2 – wystające części podłogi/ścian) jest dobry – wykorzystałem go w poprawionej formie (konkretny przypadek, klucz A).
4. **Przeoczone wady formy**: 0441 – klucz jedyną najkrótszą (59 zn.); 0443 A „żadnego”; 0445 A „tylko”; 0446 A „niezależnie”; 0447 C „wszystkich”; 0440 B „każda”; 0450 – w wyjaśnieniu „odpowiedzi A i B” (odwołanie do liter opcji). 0440: #890 każe „usunąć wskazówkę długościową”, ale jej nie ma (A 67 / B 66 / C 70) – za to przeoczył, że klucz A odsyła sam do siebie.
5. **Brak przeszukania skryptem repozytorium**: #890 „Nie uruchamiano repozytoryjnego similarity.py” (własny Jaccard). Na kopii po poprawkach uruchomiłem `similarity.py --threshold 0.25`: najwyższe pary z partią – 0204/0443 = 0,259 i 0321/0447 = 0,259 (inne elementy przepisu).
6. Kandydaci 0436 – #890 pominął **0078** (1.4.3.1.1 (b) – mokry karton, nie ładować), a dołączył 0135 (rozładowca – inny temat).
7. Słusznie w #890: 0436 – duplikat; klucze 0437–0450 poprawne co do istoty; 0446 – przepis wymaga „wyprodukowane **i dopuszczone**” przed 1.01.2003; cytaty dosłowne (1.4.3.1.1 (b) s. 57, 7.5.1.2 s. 1304, 1.1.4.5.1–1.1.4.5.2 s. 30, 1.1.4.3 s. 30, 1.1.4.5.3 i 1.1.4.7 s. 31); licznik 345 → 330; test od razu z dwiema stałymi FIRST_PASS_BANK_SHA / EXPECTED_BANK_SHA.

## Duplikaty – sprawdzenie w całym banku (780) i między sobą

Przeszukano cały bank po temacie (1.1.4.x, 5.4.1.1.7, 5.4.1.1.24, IMDG, ICAO, RID, ADN, SOLAS, prom, kolej, DOT, CFR, 4.1.6.12–13, uszkodzone opakowania, 7.5.1.x, wystające części, CSC) oraz skryptami `check_near_duplicates.py` (0,60), `check_cross_module_duplicates.py` (0,80), `similarity.py` (0,45; dodatkowo 0,25) na kopii po poprawkach – brak par powyżej 0,26 z udziałem 0436–0450.
- **0436** nowe (7.5.1.2 akapit 2 – wystająca śruba/blacha we wnętrzu kontenera) vs 0554 (pozostałości na podłodze), 0138/0560 (niezgodność wyposażenia), 0202 (od przyjazdu), 0239 (dokumenty), 0555/0584/0020/0517/0078 (uszkodzona przesyłka) – inny element.
- **0437** (wagon – przepisy kolejowe/RID) vs 0205 (przeładunek kolej → ciężarówka, 1.2.3), 0141 (gałęzie), 0320 (ADN). **0438** nowe (kto może uzgodnić ADR na promie – państwa) vs 0439 (warunek umowy), 0440 (wymagania dodatkowe), 0441 (zgłoszenie). **0442** (1.1.4.5.3 – cała konstrukcja). **0443** nowe (1.1.4.2.3 – dokument IMDG + dodatkowe informacje ADR) vs 0030 (ogólnie „sprawdzić dokumenty i wymagania ADR”), 0601/0708/0714/0779 (wpis z 5.4.1.1.7) – inny element.
- **0444** (1.1.4.3 – data + badania IMDG) vs **0445** (1.1.4.3 zdanie 2 – kolumny (10)/(11) i dział 4.2). **0446** nowe (4.1.6.12 (c) – nieczytelne znaki, nie napełniać) vs 0386 (4.1.6.13 (a) – nieszczelna), 0451 (termin badania), 0452 (przewóz do badania). **0447** (1.1.4.7.1 – do odbiorcy finalnego) vs 0321 (brak odcinka morskiego). **0448** (eksport poza ADR), **0449** (napełnianie wg CFR), **0450** (oznakowanie wg 5.2) vs 0453/0454 (wpis 5.4.1.1.24).

## Ustalenia dla poszczególnych pytań (cytaty, strony Dz.U., klucze)

### ADR-B-0436 – POPRAW (09-K08, A) – NOWY TEMAT (duplikat 0020/0517/0555/0584/0078)
- 7.5.1.2 (s. 1304): „Jednostka transportowa cargo powinna być sprawdzona w celu zapewnienia, że … jej podłoga, ściany wewnętrzne i sufit, o ile występuje, nie mają wystających części i uszkodzeń mogących oddziaływać na przewożony towar…”; zdanie 1: „…załadunek nie powinien się odbyć, jeżeli … oględziny … wskazują, że … kontener … nie spełniają wymagań…”. Klucz A „Nie, wystające części mogące uszkodzić towar trzeba najpierw usunąć” ✔.

### ADR-B-0437 – POPRAW (10-K04, C) – przeredagowane
- 1.1.4.5.1 (s. 30): „…na tej części trasy stosuje się tylko te przepisy krajowe lub międzynarodowe, które dotyczą przewozu towarów niebezpiecznych tym rodzajem transportu, którym przewożony jest ten pojazd.” Klucz C „Przepisy o przewozie towarów niebezpiecznych koleją, takie jak RID” ✔.

### ADR-B-0438 – POPRAW (10-K04, C) – NOWY ELEMENT (≈ 0437)
- 1.1.4.5.2 (s. 30): „…zainteresowane Umawiające się Strony ADR mogą uzgodnić stosowanie przepisów ADR do tej części trasy, na której pojazd przewożony jest inaczej niż po drogach kołowych…”. Klucz C „Zainteresowane państwa, które są Umawiającymi się Stronami ADR” ✔.

### ADR-B-0439 – POPRAW (10-K04, C) – przeredagowane
- 1.1.4.5.2 (s. 30): „…jeżeli takie umowy … nie są sprzeczne z postanowieniami umów międzynarodowych regulujących przewóz towarów niebezpiecznych rodzajem transportu użytym do przewozu pojazdu drogowego … np. … (SOLAS)…”. Klucz C ✔.

### ADR-B-0440 – POPRAW (10-K04, A) – przeredagowane
- 1.1.4.5.2 (s. 30): „…uzupełnionych, jeżeli uznają to za potrzebne, o wymagania dodatkowe…”. Klucz A „Tak, strony mogą uzupełnić ją o wymagania dodatkowe, jeśli to potrzebne” ✔.

### ADR-B-0441 – POPRAW (10-K04, C) – przeredagowane (strona: s. 30, nie 31)
- 1.1.4.5.2 akapit 2 (s. 30): „Umowy, o których mowa, powinny być zgłaszane przez Umawiającą się Stronę będącą inicjatorem umowy do Sekretariatu Europejskiej Komisji Gospodarczej Organizacji Narodów Zjednoczonych, który następnie podaje je do wiadomości Umawiających się Stron.” Klucz C ✔.

### ADR-B-0442 – POPRAW (10-K04, C) – przeredagowane (cała konstrukcja 1.1.4.5.3)
- 1.1.4.5.3 (s. 30–31): „…przepisy tej umowy międzynarodowej stosuje się na danym odcinku przewozu łącznie z przepisami ADR, które nie są z nimi sprzeczne; na tym odcinku przewozu nie stosuje się innych przepisów ADR.” (zdanie na s. 31). Klucz C „Razem z tą umową, ale bez przepisów ADR, które są z nią sprzeczne” ✔.

### ADR-B-0443 – POPRAW (10-K04, C) – NOWY ELEMENT (duplikat 0442)
- 1.1.4.2.3 (s. 30): „W przypadku przewozu w łańcuchu transportowym zawierającym przewóz morski lub powietrzny, informacje wymagane na podstawie przepisów 5.4.1, 5.4.2 … mogą być zastąpione przez dokument przewozowy i informacje wymagane odpowiednio na podstawie Kodeksu IMDG lub Instrukcji Technicznych ICAO, pod warunkiem, że będzie również podana każda dodatkowa informacja, wymagana na podstawie ADR.” Klucz C ✔.

### ADR-B-0444 – POPRAW (10-K05, B) – przeredagowane (istniejący temat cysternowy)
- 1.1.4.3 (s. 30): „…które zostały wyprodukowane i dopuszczone przed 1 stycznia 2003 r., zgodnie z przepisami Kodeksu IMDG (zmiany 29-98), mogą być używane nadal pod warunkiem, że spełniają wymagania odpowiednich przepisów dotyczących badań okresowych i prób, zawartych w Kodeksie IMDG.” Klucz B ✔.

### ADR-B-0445 – POPRAW (10-K05, C) – przeredagowane (istniejący temat cysternowy)
- 1.1.4.3 (s. 30): „Ponadto powinny one spełniać wymagania odpowiednich instrukcji podanych w kolumnach (10) i (11) w tabeli A w dziale 3.2 oraz przepisów działu 4.2 ADR.” Klucz C ✔.

### ADR-B-0446 – POPRAW (10-K05, C) – NOWY TEMAT, NIECYSTERNOWY (duplikat 0444)
- 1.1.4.7.2 (c) (s. 31): „Do naczyń ciśnieniowych mają zastosowanie przepisy 4.1.6.12 i 4.1.6.13.” 4.1.6.12 (s. 855): „Naczynia ciśnieniowe nie powinny być przeznaczone do napełniania: … (c) jeśli nieczytelne są znaki dotyczące certyfikacji, badań i napełniania.” Klucz C ✔.

### ADR-B-0447 – POPRAW (10-K05, A) – przeredagowane
- 1.1.4.7.1 (s. 31): „…nadane do przewozu w łańcuchu transportowym zgodnie z 1.1.4.2, mogą być przewożone od miejsca tymczasowego składowania do odbiorcy finalnego na końcu łańcucha przewozowego.” Klucz A ✔.

### ADR-B-0448 – POPRAW (10-K05, C) – przeredagowane
- 1.1.4.7.2 (s. 31): „…mogą być napełniane i przewożone wyłącznie w celu eksportu do krajów niebędących Umawiającymi się Stronami ADR…”. Klucz C ✔ (słowo „wyłącznie” tylko w wyjaśnieniu/cytacie, nie w opcjach).

### ADR-B-0449 – POPRAW (10-K05, C) – przeredagowane
- 1.1.4.7.2 (a) (s. 31): „Napełnianie naczynia ciśnieniowego jest zgodne z odpowiednimi wymaganiami Kodeksu Przepisów Federalnych Stanów Zjednoczonych Ameryki”. Klucz C ✔.

### ADR-B-0450 – POPRAW (10-K05, C) – przeredagowane
- 1.1.4.7.2 (b) (s. 31): „naczynia ciśnieniowe powinny być oznakowane i opatrzone nalepkami ostrzegawczymi zgodnie z działem 5.2”. Klucz C ✔.

## Wskaźniki

- „Poprawna = jedyna najdłuższa”: **32/780 = 4,10% bez zmian**, maksimum działu **7,87%** bez zmian – tych linii w `docs/POKRYCIE-KURSU.md`, `podstawowy/README.md`, `PAKIET-ZAMKNIECIE-0780.md` **nie zmieniać** (tylko SHA tam, gdzie występuje).
- „Poprawna = jedyna najkrótsza”: **180 → 173/780**; ADR-B-10 21,1% → **10,5%** (6/57), ADR-B-09 25,8% → **24,2%** (15/62); maksimum działu 31,5% (bez zmian); wszystkie działy ≤ 38%.
- Wszystkie 15 wyjaśnień: 5 zdań, 419–527 znaków, maks. 30 słów w zdaniu, na końcu „Podstawa: ADR …”; opcje 41–74 znaki; bez słów absolutnych i średników w opcjach.

## Egzaminy, kolejki, snapshoty (pułapki CI)

- Egzaminy próbne – z partii **tylko 0448 w `questions` wariant-005 / klucz-005**; na listach `excluded_question_ids` żadnego ID z partii. Pozostałe 8 plików egzaminów – tylko SHA.
- `review/specialist/KOLEJKA-PRIORYTETOWA-4X44.json` zawiera **0448** („question” + „legal_basis”); 4X40 – tylko SHA.
- Snapshoty: `review/sequential/` i `review/legal-clauses/` – pliki **417-436.json** (0436), **437-446.json** (0437–0446), **447-454.json** (0447–0450); clause, answer_review A/B/C, notes_on_conditions ≥ 25 zn.
- Ledger `review/legal-polish/stage4w4-literal-verification-ledger-0001-0609.json`: `source_references` z nowych sources dla 15 ID (zmienia się 10: 0436, 0438, 0439, 0440, 0441, 0443, 0445, 0446, 0449, 0450).
- Rejestry `REJESTR-AKTUALNY-0001-0765.md` i `-0001-0780.md`: po 15 wierszy.
- SHA banku fa4e3835… występuje w **33 plikach** poza historycznymi raportami `review/literal-pl/`: **32 zamieniane wprost** (docs/POKRYCIE-KURSU.md, docs/STAN-KONCOWY-…, podstawowy/README.md, review/README.md, podstawowy/raporty/etap-4x135-wykluczenia-proby.json, 8 plików review/specialist, 10 plików egzaminów, tests/test_literal_review_0301_0315 … 0391_0405 (7), **0406_0420** (EXPECTED_BANK_SHA; FIRST_PASS 5e369822… zostaje) i **0421_0435** (EXPECTED_BANK_SHA **oraz** literał w `test_second_pass_artifacts_and_bank_sha`; FIRST_PASS 02506637… zostaje)) + `tests/test_literal_review_0436_0450.py` – TYLKO EXPECTED_BANK_SHA (FIRST_PASS_BANK_SHA = fa4e3835… zostaje).
- Oczekiwany SHA banku: **fa4e38350731bd52c1a64a8cab934bdf18988438 → 094473164719bc6a651a6e303dc117cfa6503ffb**.

## Test na kopii repo

`test_p30.sh` (kopia /tmp/b30 z main **29d9dc65a** = po scaleniu #890, bez commitów i pushu): `apply_poprawki.py` → „Changed (15): ADR-B-0436 … ADR-B-0450”, blob **094473164719bc6a651a6e303dc117cfa6503ffb**; po synchronizacji (`sync_p30_test.py`, 42 zmienione pliki + nowy POPRAWKI) wszystkie 14 skryptów CI = 0 i `python3 -m unittest discover -s tests` – **193 testy OK**.

## Licznik

Po wdrożeniu partii 30 (obie kontrole 0436–0450): **330 pytań bez porównania dosłownego po obu kontrolach** (0451–0780); kontrola pierwsza partii 31 (0451–0465): 330 → 315.

## Do zapamiętania na kolejne partie
- 0451–0454 (1.1.4.7.2 (c), 5.4.1.1.24; 10-K05 = 19) – porównać z 0386, nową 0446 (4.1.6.12 (c)), 0447–0450 i między sobą (0451/0452 – ten sam akapit (c); 0453/0454 – ten sam punkt 5.4.1.1.24); 0455–0460 (1.10.3.1.2 – towary dużego ryzyka, 12-K05 = 17) – między sobą i z 0122, 0211–0213, 0249, 0304, 0305, 0399, 0402, 0403, 0405–0408, 0416, 0582; 0456 (próg 3000 l w cysternie) – jeśli duplikat, zamiennik NIECYSTERNOWY; 0461–0465 (5.2.1.8, 5.4.1.1.18 – zagrożenie dla środowiska, 03-K01 = 13) – z 0007, 0045, 0276, 0327, 0466–0470, 0734.
- 0071/0072 (0,909) i 0632 (≈ stara 0297) – przy właściwych partiach (bez zmian).
