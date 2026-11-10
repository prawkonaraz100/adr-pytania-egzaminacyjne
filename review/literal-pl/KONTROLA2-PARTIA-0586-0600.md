# Kontrola druga – partia ADR-B-0586–0600 (porównanie dosłowne z polskim tekstem ADR 2025)

Data: 2026-11-10 (czas polski, CET).
Przedmiot: pierwsza kontrola ChatGPT (PR #911, scalony; main **bc4dfadc6**; `review/literal-pl/PARTIA-0586-0600.md` + `.json` + `tests/test_literal_review_0586_0600.py`, podsumowanie 5 OK / 10 POPRAW / 0 BLOKUJ, licznik 195 → 180) oraz rekordy 0586–0600 na main (bank blob **bcac6f69…**, 780 pytań; #911 banku nie zmienia).
Źródła: Dz.U. 2025 poz. 642 (OCR `-l pol`, przy wątpliwościach obraz strony PDF; strony wg nagłówka „Dziennik Ustaw — NNN —”): s. 23 (1.1.3.1 (a)(i)–(ii)), s. 25 (1.1.3.4.3), s. 33 (1.2.1 – „członek załogi pojazdu”), s. 304 (3.1.2.2 (a) – przykład UN 1057), s. 379–380 (UN 1263), s. 519–520 (UN 2810), s. 690 (3.5.1.1), s. 961 (5.4.1.1.1 (a)–(b)), s. 962 (5.4.1.1.1 (e)–(g)), s. 974 (5.4.3.1–5.4.3.4), s. 975 (wzór – pierwsza strona: czynności w razie wypadku lub awarii), s. 976–977 (tabela nalepek, kolumny (1)–(3), nalepka 8, UWAGA 2), s. 1324 (8.1.2.1–8.1.2.3), s. 1325 (8.1.5.2), s. 1327 (8.2.2.3.2 (n)), s. 1332 (8.3.7), s. 1338 (8.6.3.1–8.6.3.3).
Status: kontrola robocza. **Żadne pytanie nie jest oznaczone jako zweryfikowane**; wszystkie pozostają `needs_review`; `review/approvals.jsonl` pusty.

## Podsumowanie

- Werdykty kontroli drugiej: **OK 0, POPRAW 15, BLOKUJ 0**.
- **Żaden z 5 werdyktów OK w #911 nie jest OK** (0588, 0591, 0595, 0596, 0600 – szczegóły niżej). ChatGPT znów zawyża OK.
- **#911 – liczniki spójne** (5/10 w .md, .json i rekordach). **Strony Dz.U. w #911 – poprawne.** Cytaty `exact_quote` zgodne z OCR. #911 przyznaje, że obrazów stron PDF nie oglądał.
- **#911 – test ma tylko jedną stałą SHA** (`EXPECTED_BANK_SHA` = bcac6f69…), mimo polecenia, by były dwie (FIRST_PASS_BANK_SHA i EXPECTED_BANK_SHA), i nie przelicza werdyktów z rekordów. Przy wdrożeniu: dodać `FIRST_PASS_BANK_SHA = bcac6f69…` (asercja manifestu), `EXPECTED_BANK_SHA` → nowy SHA, przeliczenie `counts` z rekordów.
- **#911 – brak propozycji zamienników** (`proposed_replacement`) dla 10 POPRAW – sam werdykt bez treści.
- **#910 nie wykonał poprawek partii 39** (mimo polecenia): `PARTIA-0571-0585.json` nadal `counts` 6/9 (rekordy 8/7), 0577 nadal `gazette_pages` [962] (powinno być 961), podsumowanie .md nadal „6 OK / 9 POPRAW”, brak sekcji „Kontrola druga”, w teście `EXPECTED_COUNTS` 6/9 i 0577 [962]. Do zrobienia przy tym wdrożeniu.
- **Duplikaty pominięte w #911**: 0589 = 0716 (oprócz 0050/0620); 0593 = 0104, 0182; 0596 = 0075, 0057 (#911: OK); 0597 = 0705, 0763 (oprócz 0024); 0595 ≈ 0002, 0091 (#911: OK); 0600 – klucz ogólnikowy, „wyjątek” wymyślony w treści (#911: OK).
- **14 pytań → nowy element tej samej kompetencji, niecysternowy**: 0586 (UWAGA 2 – kolumnę (3) wolno modyfikować), 0587 (kolumna (2) „Charakterystyka zagrożeń”, nalepka 8), 0588 (8.1.2.1 „Poza dokumentami wymaganymi na podstawie innych przepisów”), 0589 (pierwsza strona wzoru dotyczy każdej klasy), 0590 (jeden komplet instrukcji dla całej załogi rozumiejącej język), 0591 (EQ pomijane przy kodzie tunelowym całego ładunku), 0592 (mały początkowy pożar komory silnika – wolno użyć gaśnicy), 0593 („Zahamować pojazd” – hamulec postojowy na spadku), 0594 (informacja o wszystkich towarach w pojeździe, nie tylko o wyciekającym), 0595 (1.1.3.1 (a)(ii) – odpady z gospodarstwa domowego poza oryginalnymi opakowaniami), 0596 (praktykant = członek załogi → własna kamizelka i latarka), 0597 (przyłbica spełnia „ochrona oczu (np. okulary ochronne)”), 0598 (3.1.2.2 (a) – „ZAPALNICZKI lub POJEMNIKI…” → najbardziej odpowiednia nazwa), 0599 (ilość osobno dla każdej grupy pakowania).
- **1 pytanie przeredagowane (ten sam element)**: 0600 (5.4.1.1.1 (g) – NIP bez adresu nie wystarcza).
- Litery kluczy, moduły i kompetencje bez zmian; nowych ID brak; bez tematów cysternowych. Kompetencje zachowują ≥ 6 pytań (przypisania bez zmian).

## Błędy / różnice względem raportu ChatGPT (#911)

| ID | #911 | Kontrola 2 | Różnica |
|---|---|---|---|
| 0586 | POPRAW | POPRAW – nowy element | zgoda (= 0088); C 85 zn. – niezgłoszone |
| 0587 | POPRAW | POPRAW – nowy element | zgoda (= 0516); B 82, C 108 zn., „wyłącznie” w C; 5.4.3.3 wyczerpany – nowy element z 5.4.3.4 |
| 0588 | OK | POPRAW – nowy element | klucz ogólnikowy („zgodnie z wykazem”); A 87, C 84 zn.; kropki na końcu opcji |
| 0589 | POPRAW | POPRAW – nowy element | zgoda (= 0050/0620), dodatkowo = 0716; opcje 96–111 zn. |
| 0590 | POPRAW | POPRAW – nowy element | zgoda (= 0090), dodatkowo = 0780 |
| 0591 | OK | POPRAW – nowy element | ogólna procedura = 0487/0602 (kod + znak); opcje 89/91/92 zn.; kropki |
| 0592 | POPRAW | POPRAW – nowy element | zgoda; opcje 96–99 zn.; nowy element – gaśnica przy pożarze komory silnika |
| 0593 | POPRAW | POPRAW – nowy element | zgoda (= 0690), dodatkowo = 0104/0182 |
| 0594 | POPRAW | POPRAW – nowy element | zgoda (= 0105/0165); A 87 zn. |
| 0595 | OK | POPRAW – nowy element | „;” w kluczu, „każdy”, „zawsze”, „automatycznie”; ≈ 0002/0091 |
| 0596 | OK | POPRAW – nowy element | = 0075/0057 (kamizelka dla każdego członka załogi); opcje 80/97/93 zn. |
| 0597 | POPRAW | POPRAW – nowy element | zgoda (= 0024), dodatkowo = 0705/0763; „;” w kluczu; 93/95/81 zn. |
| 0598 | POPRAW | POPRAW – nowy element | zgoda (= 0038); „;” w kluczu; 86/103 zn. |
| 0599 | POPRAW | POPRAW – nowy element | zgoda (= 0070); 90/89/102 zn. |
| 0600 | OK | POPRAW – przeredagowane | klucz ogólnikowy; „Nie wskazano żadnego wyjątku” – wyjątku w (g) nie ma; A 89 zn. |

## Duplikaty – sprawdzenie w całym banku (780) i między sobą

- Stare rekordy: 0586 = 0088; 0587 = 0516; 0589 = 0050, 0620, 0716; 0590 = 0090, 0780; 0591 ≈ 0487, 0602; 0592 ≈ 0210; 0593 = 0690, 0104, 0182; 0594 = 0105, 0165; 0595 ≈ 0002, 0091; 0596 = 0075, 0057; 0597 = 0024, 0705, 0763; 0598 = 0038; 0599 = 0070.
- Nowe rekordy – sprawdzone ręcznie z najbliższymi tematami: 0587 vs 0234 (0234: wykaz wyposażenia na 4. stronie; 0587: opis zagrożeń w kolumnie (2) – inny element); 0589 vs 0587 (struktura wzoru – inne pytanie: zakres pierwszej strony); 0591 vs 0085/0322/0576/0772 (8.6.3.3 – inne przypadki: LQ, 1.1.3.6; 0591 – EQ); 0592 vs 0184/0640/0695 (gaśnice – poza tunelem i bez rozróżnienia komory silnika / ładowni); 0593 vs 0351 (8.3.7 w module 04 – postój; 0593 – instrukcje pisemne po kolizji, moduł 05); 0596 vs 0300/0196 (definicja członka załogi – bez wyposażenia); 0598 vs 0038 (nazwa handlowa vs wybór z nazwy alternatywnej); 0599 vs 0070/0578 (ilość ogólnie / UWAGA 1 – kategorie transportowe; 0599 – rozdział wg grup pakowania); 0600 vs 0068/0579 (dane odbiorcy).
- `similarity.py`: cały bank – main **8 par ≥ 0,45 / 169 par ≥ 0,25**; po poprawkach **8 / 167**. Pary z udziałem partii: main **0 ≥ 0,45 / 3 ≥ 0,25** (zgodnie z #911: 0219/0593 = 0,292, 0593/0739 = 0,280, 0593/0690 = 0,261); po poprawkach **0 / 1**: 0234/0587 = 0,269 – odrębne (wyżej).
- `check_near_duplicates.py --threshold 0.60`: 0 nieprzejrzanych par; `check_cross_module_duplicates.py --threshold 0.80`: PASS.
- Uwagi na później (poza tą partią): **0777** – „Delivery Sale” zamiast „Sprzedaż obwoźna”; **0772** – wątpliwe prawnie wobec 8.6.3.3/8.6.4.

## Szczegóły – cytaty (dosłownie z Dz.U.) i rozstrzygnięcia

### ADR-B-0586 – POPRAW (13-K04, A) – NOWY ELEMENT (= 0088)
Tabela nalepek we wzorze 5.4.3.4, UWAGA 2 (s. 977): „Dodatkowe wskazówki określone w kolumnie (3) tej tabeli, mogą być modyfikowane w celu ich [dostosowania do klas towarów niebezpiecznych przeznaczonych do przewozu oraz do środków transportu]”. Nowe pytanie: przewoźnik wożący farby (nalepka 3) chce dostosować kolumnę (3) – może. Dystraktory: „bez jakichkolwiek zmian” i „po zatwierdzeniu przez nadawcę” (takiego warunku nie ma). Opcje 75/74/76 zn.

### ADR-B-0587 – POPRAW (13-K04, B) – NOWY ELEMENT (= 0516; 5.4.3.3 wyczerpany)
Tabela nalepek (s. 976–977), nagłówek: „Nalepki ostrzegawcze | Charakterystyka zagrożeń | Wskazówki dodatkowe”; nalepka 8: „Zagrożenie poparzeniem chemicznym. …”. Nowe pytanie: gdzie we wzorze jest opis zagrożeń ładunku z nalepką 8 – w kolumnie (2) tabeli nalepek. Opcje 65/76/78 zn.

### ADR-B-0588 – POPRAW (13-K05, C) – NOWY ELEMENT (#911: OK; ogólnik)
8.1.2.1 (s. 1324): „Poza dokumentami wymaganymi na podstawie innych przepisów, w kabinie kierowcy jednostki transportowej powinny znajdować się następujące dokumenty…”; 8.1.2.2 (b) – zaświadczenie ADR. Nowe pytanie: dyspozytor twierdzi, że dokumenty z innych przepisów mogą zostać w bazie – nie ma racji. Celowo bez przykładów dowodu rejestracyjnego/prawa jazdy (różne przepisy krajowe).

### ADR-B-0589 – POPRAW (13-K04, A) – NOWY ELEMENT (= 0050/0620/0716)
Wzór (s. 975): pierwsza strona „Czynności w razie wypadku lub awarii” – bez ograniczenia do klasy; tabela nalepek (s. 976–977) – „wskazówki dodatkowe” dla poszczególnych nalepek. Nowe pytanie: kierowca z kartonami z nalepką 9 czyta jedynie wiersz nalepki 9 – czynności z pierwszej strony też go dotyczą.

### ADR-B-0590 – POPRAW (13-K07, A) – NOWY ELEMENT (= 0090/0780)
5.4.3.1 (s. 974): instrukcje „w kabinie załogi pojazdu w miejscu łatwo dostępnym”; 5.4.3.2 (s. 974): „w języku(-ach), które każdy członek załogi pojazdu może przeczytać i zrozumieć”; 8.1.2.3 (s. 1324). Nowe pytanie: kierowca i pomocnik rozumieją po polsku, jeden komplet w kieszeni drzwi – drugi komplet niepotrzebny.

### ADR-B-0591 – POPRAW (11-K06, B) – NOWY ELEMENT (#911: OK; ogólnik = 0487/0602)
8.6.3.3 (s. 1338): przy ustalaniu kodu dla całego ładunku nie bierze się pod uwagę towarów wyłączonych zgodnie z 1.1.3.4.3 (s. 25 – ilości wyłączone wg 3.5.1.1, s. 690); UN 2810 III grupa – „2 (E)” (s. 519–520); UN 1263 II grupa – „2 (D/E)”, E2 (s. 379–380). Nowe pytanie: beczki UN 2810 III (E) + kartony UN 1263 w EQ → kod całego ładunku E.

### ADR-B-0592 – POPRAW (11-K07, C) – NOWY ELEMENT (≈ 0210; ogólnik)
Wzór (s. 975): „Użyć gaśnic do gaszenia małych/początkowych pożarów opon, hamulców lub komory silnika, jeżeli jest to możliwe i bezpieczne”; „Pożary w przedziałach ładunkowych nie powinny być gaszone przez członków załogi pojazdu”; 8.2.2.3.2 (n) (s. 1327) – szkolenie o przejazdach przez tunele i postępowaniu przy zdarzeniu. Nowe pytanie: mały początkowy pożar komory silnika w tunelu, ładunek się nie pali – wolno użyć gaśnicy.

### ADR-B-0593 – POPRAW (05-K02, A) – NOWY ELEMENT (= 0690/0104/0182)
Wzór (s. 975): „Zahamować pojazd, wyłączyć silnik i odłączyć akumulator…”; 8.3.7 (s. 1332) – hamulec postojowy przy postoju. Nowe pytanie: po kolizji na lekkim spadku, silnik wyłączony – najpierw hamulec postojowy (jeśli możliwe i bezpieczne), potem odejście. Opcje 64/64/64 zn.

### ADR-B-0594 – POPRAW (05-K03, B) – NOWY ELEMENT (= 0105/0165)
Wzór (s. 975): powiadomić służby, „przekazując możliwie wszystkie informacje dotyczące wypadku lub awarii i towarów niebezpiecznych”; nalepka 5.1 – możliwość gwałtownej reakcji i zapalenia (s. 977). Nowe pytanie: wycieka tylko ciecz zapalna, ale w pojeździe są też materiały żrące i utleniające – przekazać dane o wszystkich.

### ADR-B-0595 – POPRAW (01-K04, A) – NOWY ELEMENT (#911: OK; „;”, „każdy”, „zawsze”, „automatycznie”; ≈ 0002/0091)
1.1.3.1 (a)(ii) (s. 23): przewóz przez osoby prywatne w ilościach z (a)(i), towarów pierwotnie do użytku osobistego/domowego, „przewożone jako odpady, w tym w przypadkach, gdy te towary niebezpieczne nie są już zapakowane w oryginalnych opakowaniach do sprzedaży detalicznej, pod warunkiem, że przedsięwzięto środki zapobiegające uwolnieniu zawartości…”. Nowe pytanie: resztki farb w szczelnych słoikach do punktu zbiórki – ADR nie ma zastosowania.

### ADR-B-0596 – POPRAW (08-K05, A) – NOWY ELEMENT (#911: OK; = 0075/0057)
1.2.1 (s. 33): „Członek załogi pojazdu oznacza kierowcę lub osobę towarzyszącą kierowcy z przyczyn związanych [z bezpieczeństwem, ochroną, szkoleniem lub obsługą]”; 8.1.5.2 (s. 1325): kamizelka ostrzegawcza i przenośne urządzenie oświetleniowe dla każdego członka załogi. Nowe pytanie: praktykant uczący się przy przewozie = członek załogi → własna kamizelka i latarka.

### ADR-B-0597 – POPRAW (08-K06, C) – NOWY ELEMENT (= 0024/0705/0763)
8.1.5.2 (s. 1325): „ochrona oczu (np. okulary ochronne)”. Nowe pytanie: przyłbica zasłaniająca oczy i twarz – spełnia wymóg (okulary to przykład). **Wątpliwość do recenzji specjalisty** (praktyka kontroli).

### ADR-B-0598 – POPRAW (13-K01, B) – NOWY ELEMENT (= 0038)
3.1.2.2 (a) (s. 304): przy nazwie z „lub” wybiera się najbardziej odpowiednią – przykład „UN 1057 ZAPALNICZKI lub POJEMNIKI DO NAPEŁNIANIA ZAPALNICZEK – należy wybrać najbardziej odpowiednią z następujących możliwych kombinacji: ZAPALNICZKI, POJEMNIKI DO NAPEŁNIANIA ZAPALNICZEK”; 5.4.1.1.1 (a)–(b) (s. 961). Nowe pytanie: nadawca wysyła zapalniczki → „ZAPALNICZKI”.

### ADR-B-0599 – POPRAW (13-K02, A) – NOWY ELEMENT (= 0070)
5.4.1.1.1 (f) (s. 962): „całkowita ilość każdego towaru niebezpiecznego o różnym numerze UN, prawidłowej nazwie przewozowej lub grupie pakowania”; (e) – liczba i opis sztuk przesyłek. Nowe pytanie: 200 l UN 1263 II + 300 l UN 1263 III – ilość osobno dla każdej grupy.

### ADR-B-0600 – POPRAW (13-K03, C) – przeredagowane (#911: OK; ogólnik, wymyślony „wyjątek”)
5.4.1.1.1 (g) (s. 962): „nazwa i adres nadawcy”. Nowe ujęcie: wpisano nazwę firmy i NIP bez adresu – trzeba dopisać adres. Opcje 66/58/63 zn.

## Wskaźniki

- Wszystkie 15 rekordów: wyjaśnienie ≥ 300 zn., 2–5 zdań, maks. 35 słów w zdaniu, koniec „Podstawa: ADR …”; opcje ≤ 80 zn.; bez słów absolutnych, średników, „np.”, „min.”, „kol.”, „odpowiedź A/B/C”.
- Klucz nie jest jedyną najdłuższą ani jedyną najkrótszą w żadnym z 15 rekordów.
- „Poprawna = jedyna najdłuższa”: **27/780 = 3,46% → 26/780 = 3,33%**; maksimum działu **6,74%** bez zmian. **Aktualizacja w 3 plikach**: `docs/POKRYCIE-KURSU.md`, `docs/STAN-KONCOWY-BANKU-ADR-PODSTAWOWY-2026-11-03.md`, `podstawowy/README.md`.
- „Poprawna = jedyna najkrótsza”: 118 → 113; maks. działu 26,4% bez zmian – poniżej 38%. Działy: 08: 20,8% → 17,0%; 11: 8,7% → 6,5%; 13: 11,1% → 7,4%.
- Rozkład liter kluczy bez zmian.

## Egzaminy, kolejki, snapshoty (pułapki CI)

- Egzaminy próbne: 0586 i 0590 w wariancie 001; 0594 w 005 – `wariant-00N.json` (stem, options) i `klucz-00N.json` (explanation, legal_basis; litera bez zmian). Wykluczenia (`excluded_question_ids`: 0586, 0590 w 002–005) bez zmian.
- `KOLEJKA-PRIORYTETOWA-4X40.json`: 0591, 0595, 0599; `KOLEJKA-PRIORYTETOWA-4X44.json`: 0600.
- Snapshoty `review/sequential/` i `review/legal-clauses/`: **586-597.json** (0586–0597) i **598-609.json** (0598–0600).
- Ledger `review/legal-polish/stage4w4-literal-verification-ledger-0001-0609.json`: `source_references` – 15 ID.
- Rejestry `REJESTR-AKTUALNY-0001-0765.md` i `-0001-0780.md`: po 15 wierszy.
- SHA banku bcac6f69… w **43 plikach** poza historycznymi raportami `review/literal-pl/` i poza `tests/test_literal_review_0586_0600.py` (FIRST_PASS) – w tym 19 testów `test_literal_review_0301_0315 … 0571_0585` (tylko EXPECTED_BANK_SHA) i `PAKIET-0585-MANIFEST.json`.
- Scenariusze i lekcje odwołują się do ID tylko w listach – tematy zgodne, bez zmian.
- Oczekiwany SHA banku: **bcac6f69bcec5dd257832774e54922c7c2c47d97 → 6147aeb45bf0efd1631ae17ce5e1d82357bffb0b**.

## Test na kopii repo

`test_p40.sh` – git worktree `/tmp/b40` z main bc4dfadc6 (bez commitów i pushu): `tools/apply_poprawki.py` z dopisanym `POPRAWKI-KONTROLA2-0586-0600.jsonl` → „Changed (15)”, blob **6147aeb45bf0efd1631ae17ce5e1d82357bffb0b**; synchronizacja (`sync_p40_test.py`); wszystkie **14 skryptów CI** – kod 0; `python3 -m unittest discover -s tests` – **Ran 232 tests – OK**.
