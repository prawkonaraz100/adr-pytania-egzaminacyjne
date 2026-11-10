# Kontrola druga – partia ADR-B-0601–0615 (porównanie dosłowne z polskim tekstem ADR 2025)

Data: 2026-11-10 (czas polski, CET).
Przedmiot: pierwsza kontrola ChatGPT (PR #913, scalony; main **757412d62**; `review/literal-pl/PARTIA-0601-0615.md` + `.json` + `tests/test_literal_review_0601_0615.py`, podsumowanie 2 OK / 13 POPRAW / 0 BLOKUJ, licznik 180 → 165) oraz rekordy 0601–0615 na main (bank blob **6147aeb4…**, 780 pytań; #913 banku nie zmienia).
Źródła: Dz.U. 2025 poz. 642 (OCR `-l pol`, przy tabelach obraz strony PDF – s. 353–354, 485, 688, 1339; strony wg nagłówka „Dziennik Ustaw — NNN —”): s. 26–28 (1.1.3.6.3 i objaśnienie pod tabelą), s. 29–30 (1.1.4.2.1), s. 56 (1.4.2.2.1 (a)), s. 107 (1.9.5.2.2), s. 109 (1.9.5.3.5–1.9.5.3.6), s. 119 (2.1.2.4), s. 159 (2.2.2.2.2), s. 171 (2.2.41.1.3), s. 308 (3.2.1 – objaśnienia kolumn (3b), (4), (5)), s. 354 (UN 1006), s. 485 (UN 2455 – „PRZEWÓZ ZABRONIONY”), s. 686 (3.4.2–3.4.3), s. 687 (3.4.7.1), s. 688 (3.4.13), s. 689 (3.4.14), s. 956 (5.3.2.3.1 – litera „X”), s. 962 (5.4.1.1.1 (k)), s. 965 (5.4.1.1.7), s. 975 (wzór instrukcji pisemnych – pierwsza strona), s. 1325 (8.1.5.3), s. 1326 (8.2.1.6), s. 1338 (8.6.3.1), s. 1339 (8.6.4, UWAGA 2).
Status: kontrola robocza. **Żadne pytanie nie jest oznaczone jako zweryfikowane**; wszystkie pozostają `needs_review`; `review/approvals.jsonl` pusty.

## Podsumowanie

- Werdykty kontroli drugiej: **OK 0, POPRAW 15, BLOKUJ 0**.
- **Żaden z 2 werdyktów OK w #913 nie jest OK** (0610, 0611 – szczegóły niżej). ChatGPT nadal zawyża OK.
- **#913 – liczniki spójne** (2/13 w .md, .json i rekordach; licznik 180 → 165 poprawny). **Strony Dz.U. w #913 – poprawne.** Cytaty `exact_quote` zgodne z OCR. #913 znów przyznaje, że obrazów stron PDF nie oglądał.
- **#913 – test znów ma tylko jedną stałą SHA** (`EXPECTED_BANK_SHA` = 6147aeb4…), choć polecenie wymagało dwóch. Przy wdrożeniu: `FIRST_PASS_BANK_SHA = 6147aeb4…` (asercja manifestu), `EXPECTED_BANK_SHA` → nowy SHA. Przeliczenie werdyktów z rekordów #913 już ma.
- **#913 – zamienniki**: 10 z 13 POPRAW ma `proposed_replacement`, ale żaden nie nadaje się do wdrożenia (duplikaty albo wady formy – tabela niżej); 0613, 0614, 0615 mają tylko `reason_no_safe_candidate` – rekord niekompletny (test #913 sprawdza jedynie, że pole nie jest puste, więc to przepuszcza).
- **Duplikaty pominięte w #913**: 0601 także = 0029/0030/0119/0708; 0606 ≈ 0002 (ogólnik 1.1.3.6); 0608 ≈ 0373; 0610 ≈ 0189/0655; 0611 ≈ 0094/0095/0153/0621/0724; 0612 ≈ 0100/0163/0735/0743; 0614 także ≈ 0143/0210/0702.
- **11 pytań → nowy element tej samej kompetencji, niecysternowy**: 0601 (łańcuch lotniczy – pakowanie razem według ICAO, 1.1.4.2.1 (b)), 0602 („Brak znaku oznacza brak ograniczeń”, 1.9.5.3.5), 0603 (wzmianka „(-)” w dokumencie, 5.4.1.1.1 (k)), 0604 (UWAGA 2 pod 8.6.4 – LQ w kontenerze ze znakami IMDG do 8 t), 0606 (gaz sprężony – liczy się pojemność wodna butli), 0607 (8.2.1.6 – uznawanie zaświadczenia w innych państwach), 0611 (2.2.41.1.3 – proszki metali a gaszenie wodą lub CO2), 0612 (osłonić kratkę i zebrać granulat wyposażeniem z 8.1.5.3), 0613 (pył – unikać wdychania, strona nawietrzna), 0614 (pożar zwykłych kartonów w ładowni – też nie gasić), 0615 (X423 – gaśnica proszkowa przy małym pożarze silnika dozwolona).
- **4 pytania przeredagowane (ten sam element)**: 0605 (3.4.2 – 30 kg brutto sztuki przesyłki LQ), 0608 (UN 2455 – „PRZEWÓZ ZABRONIONY” w tabeli A), 0609 (3.4.7.1 – znak LQ na kartonach, wpis w liście go nie zastępuje), 0610 (kolumna (5) tabeli A).
- Litery kluczy, moduły i kompetencje bez zmian; nowych ID brak; bez tematów cysternowych (dawne 0604 – cysterna D/E – zastąpione). Kompetencje zachowują ≥ 6 pytań (przypisania bez zmian).

## Błędy / różnice względem raportu ChatGPT (#913)

| ID | #913 | Kontrola 2 | Różnica |
|---|---|---|---|
| 0601 | POPRAW | POPRAW – nowy element | zgoda (= 0089/0215/0287/0714/0779), także = 0029/0030/0119/0708; zamiennik #913 (ICAO, oznakowanie) = 0277/0397, A ≈ 85 zn. z kropką |
| 0602 | POPRAW | POPRAW – nowy element | zgoda (= 0032/0083); zamiennik #913 (znaczenie tabliczki E) ≈ 0207/0431/0540, „;” w kluczu, „zawsze” w B |
| 0603 | POPRAW | POPRAW – nowy element | zgoda (= 0065/0174); zamiennik #913 („(-)” + E → E) = 0432, 8.6.3.2 wyczerpany |
| 0604 | POPRAW | POPRAW – nowy element | zgoda (cysterna); zamiennik #913 (C/E) ≈ 0084, „każdym”/„Każdy”; wariant B/D ≈ 0539 – odrzucony |
| 0605 | POPRAW | POPRAW – przeredagowane | zgoda; zamiennik #913 z kropkami i „Nie. …” – przeredagowane |
| 0606 | POPRAW | POPRAW – nowy element | zamiennik #913 zostaje przy ogólniku „masa całego ładunku” ≈ 0002 |
| 0607 | POPRAW | POPRAW – nowy element | zgoda (= 0003/0719); zamiennik #913 (klasa 1 – kurs specjalistyczny) ≈ 0160, „wszystkie” w A |
| 0608 | POPRAW | POPRAW – przeredagowane | zamiennik #913 (samoreaktywny typu A) bez konkretnego wiersza tabeli A; ≈ 0373 – teraz konkretne UN 2455 |
| 0609 | POPRAW | POPRAW – przeredagowane | zamiennik #913: klucz jedyną najdłuższą |
| 0610 | OK | POPRAW – przeredagowane | kropki na końcu opcji, „kolumna 5” bez nawiasów, B błędnie opisuje kolumnę (4); ≈ 0189/0655 |
| 0611 | OK | POPRAW – nowy element | „;” w kluczu, kropki, w wyjaśnieniu „Odpowiedź A … a B”; ≈ 0094/0095/0153/0621/0724 |
| 0612 | POPRAW | POPRAW – nowy element | zgoda (A 82 zn.); ≈ 0100/0163/0735/0743; zamiennik #913: klucz jedyną najdłuższą |
| 0613 | POPRAW | POPRAW – nowy element | zgoda (= 0101/0178/0735); brak zamiennika w #913 |
| 0614 | POPRAW | POPRAW – nowy element | zgoda (= 0107/0166/0222/0641/0742), także ≈ 0143/0210/0702; brak zamiennika w #913 |
| 0615 | POPRAW | POPRAW – nowy element | zgoda (= 0017/0170/0256/0698/0752); brak zamiennika w #913 |

## Duplikaty – sprawdzenie w całym banku (780) i między sobą

- Stare rekordy: 0601 = 0029, 0030, 0089, 0119, 0215, 0287, 0708, 0714, 0779; 0602 = 0032, 0083; 0603 = 0065, 0174; 0606 ≈ 0002; 0607 = 0003, 0719; 0608 ≈ 0373; 0610 ≈ 0189, 0655; 0611 ≈ 0094, 0095, 0153, 0621, 0724; 0612 ≈ 0100, 0163, 0735, 0743; 0613 = 0101, 0178, 0735; 0614 = 0107, 0143, 0166, 0210, 0222, 0641, 0702, 0742; 0615 = 0017, 0170, 0256, 0698, 0752.
- Nowe rekordy – sprawdzone ręcznie z najbliższymi tematami: 0601 vs 0287 (ten sam punkt 1.1.4.2.1 (b), 0287 – łańcuch morski/IMDG, 0601 – łańcuch lotniczy/ICAO; kompetencja 13-K06 jest nasycona – **do decyzji specjalisty**); 0601 vs 0277/0397 (ICAO – oznakowanie, nie pakowanie razem); 0602 vs 0431 (1.9.5.3.6 – towar „(-)”), 0207/0574 (kategoria B, doładunek); 0603 vs 0525 (wpis kodu D/E) i 0248/0063 (gdzie stoi kod); 0604 vs 0209/0540 (LQ a tunel E bez znaków IMDG – 0604 dotyczy UWAGI 2: znaki według IMDG) i 0539 (B/D); 0605 vs 0609 (masa vs znak LQ); 0606 vs 0570–0572/0272/0323 (inne kategorie i ciecze); 0607 vs 0148/0301 (ważność zaświadczenia); 0608 vs 0373 (rola załadowcy, bez odczytu tabeli A) i 0329 (odpad); 0610 vs 0125/0128/0314 (inne kolumny); 0611 vs 0153 (różnica 4.1/4.3); 0612 vs 0613 (zebranie granulatu vs pył i strona nawietrzna); 0614 vs 0641/0222 (ogień ładowni ogólnie; 0614 – palą się zwykłe kartony obok towaru ADR); 0615 vs 0592 (mały pożar silnika w tunelu, bez litery X) i 0017/0170 (znaczenie X).
- `similarity.py`: cały bank – main **8 par ≥ 0,45 / 167 par ≥ 0,25**; po poprawkach **8 / 165**. Pary z udziałem partii: main **0 ≥ 0,45 / 6 ≥ 0,25** (zgodnie z #913); po poprawkach **0 / 4**: 0287/0601 = 0,417 (wyżej – nasycona kompetencja), 0209/0604 = 0,281, 0574/0602 = 0,267, 0207/0602 = 0,259 – odrębne (wyżej).
- `check_near_duplicates.py --threshold 0.60`: 0 nieprzejrzanych par; `check_cross_module_duplicates.py --threshold 0.80`: PASS.
- Uwagi na później (poza tą partią): **0708 (moduł 10) = 0714** (brak wpisu 5.4.1.1.7 w łańcuchu morskim – ten sam scenariusz).

## Szczegóły – cytaty (dosłownie z Dz.U.) i rozstrzygnięcia

### ADR-B-0601 – POPRAW (13-K06, B) – NOWY ELEMENT (= 0089/0215/0287/0714/0779, 0029/0030/0119/0708)
1.1.4.2.1 (s. 29): „Sztuki przesyłek, kontenery, cysterny przenośne, kontenery-cysterny i MEGC, które nie spełniają wymagań ADR dotyczących pakowania, pakowania razem, oznakowania i stosowania nalepek ostrzegawczych, ale są zgodne z wymaganiami Kodeksu IMDG lub Instrukcji Technicznych ICAO, powinny być dopuszczone do przewozu w łańcuchu transportowym zawierającym przewóz morski lub lotniczy pod następującymi warunkami: (…) (b) w odniesieniu do pakowania razem w do jednej sztuki przesyłki, powinny być stosowane wymagania Kodeksu IMDG lub Instrukcji Technicznych ICAO”. 5.4.1.1.7 (s. 965): „W przypadku przewozu zgodnie z 1.1.4.2.1, w dokumencie przewozowym powinien być zamieszczony dodatkowo następujący zapis: „PRZEWÓZ ZGODNY Z 1.1.4.2.1”.” Nowe pytanie: paczki do samolotu, znaki ADR, pakowanie razem według ICAO → zapis potrzebny. Opcje 79/68/51 zn.

### ADR-B-0602 – POPRAW (11-K01, B) – NOWY ELEMENT (= 0032/0083)
1.9.5.3.5 (s. 109): „W przypadku wprowadzenia zakazu wjazdu do tunelu lub wskazania drogi alternatywnej, zastosowane znaki drogowe powinny być zaopatrzone w dodatkową tabliczkę (…) Brak znaku oznacza brak ograniczeń”; 1.9.5.2.2 (s. 107) – kategoria A bez ograniczeń. Nowe pytanie: beczki D/E, przed tunelem brak znaku i tabliczki → może wjechać. Opcje 75/73/67 zn.

### ADR-B-0603 – POPRAW (11-K05, A) – NOWY ELEMENT (= 0065/0174)
5.4.1.1.1 (k) (s. 962): „dla przewozu obejmującego przewóz przez tunele z ograniczeniami przewozu - kod ograniczeń przewozu przez tunele podany w nawiasach wielkimi literami w kolumnie (15) tabeli A w dziale 3.2 lub wzmiankę „(-)” lub jak wskazano w zatwierdzeniu specjalnym zgodnie z 1.7.4.2.” Nowe pytanie: towar „(-)”, trasa przez tunel z ograniczeniami → w dokumencie wzmianka „(-)”. Opcje 75/78/72 zn.

### ADR-B-0604 – POPRAW (11-K02, C) – NOWY ELEMENT, niecysternowy (dawniej cysterna D/E)
8.6.4, UWAGA 2 pod tabelą (s. 1339, obraz strony): „Towary niebezpieczne zapakowane w ilościach ograniczonych, przewożone w kontenerach lub jednostkach transportowych oznakowanych zgodnie z Kodeksem IMDG nie podlegają ograniczeniom przewozu przez tunele kategorii E, jeżeli masa całkowita brutto sztuk przesyłek zawierających towary niebezpieczne zapakowane w ilościach ograniczonych nie przekracza 8 ton na jednostkę transportową.” 1.9.5.3.6 (s. 109) – ograniczenia tunelu E dla jednostek i kontenerów oznakowanych według 3.4.13. Nowe pytanie: kontener do portu, 5 t LQ, znaki LQ według IMDG, tunel E → może przejechać. Opcje 73/76/74 zn. Odrzucony wariant B/D dla butli (≈ 0539).

### ADR-B-0605 – POPRAW (01-K05, A) – przeredagowane
3.4.2 (s. 686): „Towary niebezpieczne powinny być zapakowane wyłącznie w opakowania wewnętrzne umieszczone w odpowiednich opakowaniach zewnętrznych. (…) Całkowita masa brutto sztuki przesyłki nie powinna przekraczać 30 kg.” 3.4.3 (s. 686) – tace z folią: 20 kg. Nowe ujęcie: karton LQ 32 kg brutto → nie. Opcje 73/64/74 zn.

### ADR-B-0606 – POPRAW (01-K06, B) – NOWY ELEMENT (≈ 0002)
Objaśnienie pod tabelą 1.1.3.6.3 (s. 28): „Odnośnie do gazów sprężonych, gazów zaadsorbowanych i chemikaliów pod ciśnieniem, pojemność wodną naczynia w litrach.”; tabela A UN 1006 ARGON SPRĘŻONY – kategoria 3 (s. 354, obraz strony). Nowe pytanie: 20 butli × 50 l → 1000 l porównuje się z limitem 1000. Opcje 55/59/65 zn.

### ADR-B-0607 – POPRAW (01-K03, C) – NOWY ELEMENT (= 0003/0719)
8.2.1.6 (s. 1326): „Wszystkie zaświadczenia, zgodne z wymaganiami określonymi w tym rozdziale, wydane zgodnie z 8.2.2.8 przez właściwą władzę Umawiającej się Strony, powinny być uznawane w okresie ich ważności przez właściwe władze innych Umawiających się Stron.” Nowe pytanie: polskie zaświadczenie w Niemczech – uznawane. Opcje 65/71/67 zn.

### ADR-B-0608 – POPRAW (01-K07, A) – przeredagowane (konkretny wiersz tabeli A)
Tabela A (s. 485, obraz strony): „2455 AZOTYN METYLU — PRZEWÓZ ZABRONIONY”; 2.2.2.2.2 (s. 159) – „UN 2455 AZOTYN METYLU” na liście gazów niedopuszczonych; 2.1.2.4 (s. 119): „Towary niebezpieczne, które są wymienione lub zdefiniowane w podrozdziale 2.2.x.2 każdej klasy, nie są dopuszczone do przewozu.”; 1.4.2.2.1 (a) (s. 56): przewoźnik „upewnić się, że towary niebezpieczne przeznaczone do przewozu są dopuszczone do przewozu zgodnie z ADR”. Opcje 62/60/62 zn.

### ADR-B-0609 – POPRAW (01-K05, B) – przeredagowane
3.4.7.1 (s. 687): „Z wyjątkiem transportu lotniczego, sztuki przesyłek zawierające towary niebezpieczne w ilościach ograniczonych powinny posiadać znak wskazany na rys. 3.4.7.1”; 3.4.13 (a) (s. 688) – jednostki > 12 t; 3.4.14 (s. 689) – znaki z 3.4.13 niewymagane do 8 t. Nowe ujęcie: brak znaku LQ na kartonach, wpis w liście go nie zastępuje; dystraktor C myli próg 8 t dla pojazdu ze znakiem na kartonie. Opcje 72/70/68 zn.

### ADR-B-0610 – POPRAW (02-K14, A) – przeredagowane (#913: OK)
3.2.1, objaśnienia do tabeli A (s. 308): kolumna (5) „Nalepki” – numery wzorów nalepek; kolumna (4) – grupa pakowania; kolumna (3b) – kod klasyfikacyjny. Opcje 50/51/48 zn.; bez kropek, „kolumna (N)” z nawiasami.

### ADR-B-0611 – POPRAW (02-K04, C) – NOWY ELEMENT (#913: OK)
2.2.41.1.3 (s. 171): „Szczególnie niebezpieczne są proszki metali, ponieważ gaszenie ich normalnymi środkami gaśniczymi, takimi jak ditlenek węgla lub woda, może zwiększać zagrożenie.” Opcje 66/74/67 zn.

### ADR-B-0612 – POPRAW (03-K04, B) – NOWY ELEMENT (≈ 0100/0163/0735/0743)
Wzór 5.4.3.4 (s. 975): „Jeżeli jest to właściwe i bezpieczne, zapobiec przedostaniu się uwolnionych materiałów do środowiska wodnego lub kanalizacji oraz zebrać uwolnione materiały, używając wyposażenia przewożonego w jednostce transportowej”; 8.1.5.3 (s. 1325): łopata, osłona otworów kanalizacyjnych, pojemnik do zbierania pozostałości (niewymagane tylko dla nalepek 1, 1.4, 1.5, 1.6, 2.1, 2.2, 2.3). **Do oceny specjalisty**: zbieranie przez załogę a oczekiwanie na służby. Opcje 73/68/67 zn.

### ADR-B-0613 – POPRAW (03-K05, C) – NOWY ELEMENT (= 0101/0178/0735)
Wzór (s. 975): „Nie wchodzić na uwolnione materiały, nie dotykać ich, unikać wdychania oparów, dymu, pyłu i pary poprzez pozostawanie po stronie nawietrznej”. Nowe pytanie: chmura pyłu z worka, kierowca chce stanąć z wiatrem → nie. Opcje 62/63/63 zn.

### ADR-B-0614 – POPRAW (05-K05, A) – NOWY ELEMENT (= 0107/0143/0166/0210/0222/0641/0702/0742)
Wzór (s. 975): „Członkowie załogi pojazdu nie powinni gasić pożaru obejmującego przedział ładunkowy”. Nowe pytanie: palą się zwykłe kartony w ładowni obok beczek ADR → też nie gasić (liczy się miejsce pożaru). **Do oceny specjalisty**: wykładnia „pożaru obejmującego przedział ładunkowy”. Opcje 69/60/70 zn.

### ADR-B-0615 – POPRAW (06-K04, B) – NOWY ELEMENT (= 0017/0170/0256/0698/0752)
5.3.2.3.1 (s. 956): „Numer rozpoznawczy zagrożenia poprzedzony literą „X” oznacza, że materiał reaguje niebezpiecznie z wodą. W odniesieniu do takich materiałów woda może być stosowana jedynie za zgodą specjalistów.”; wzór (s. 975): „Jeżeli jest to właściwe i bezpieczne, użyć gaśnic w celu ugaszenia małego lub będącego w fazie początkowej pożaru, obejmującego opony, hamulce lub przedział silnika”. Opcje 64/68/71 zn.

## Wskaźniki

- Wszystkie 15 rekordów: wyjaśnienie ≥ 300 zn., 2–5 zdań, maks. 35 słów w zdaniu, koniec „Podstawa: ADR …”; opcje ≤ 80 zn.; bez słów absolutnych, średników, kropek na końcu opcji, „np.”, „min.”, „kol.”, „odpowiedź A/B/C”.
- Klucz nie jest jedyną najdłuższą ani jedyną najkrótszą w żadnym z 15 rekordów.
- „Poprawna = jedyna najdłuższa”: **26/780 = 3,33% → 24/780 = 3,08%**; maksimum działu **6,74%** bez zmian. **Aktualizacja w 3 plikach**: `docs/POKRYCIE-KURSU.md`, `docs/STAN-KONCOWY-BANKU-ADR-PODSTAWOWY-2026-11-03.md`, `podstawowy/README.md`.
- „Poprawna = jedyna najkrótsza”: 113 → 109/780; maks. działu 26,4% bez zmian – poniżej 38%. Działy: 01: 20,4% → 16,7%; 06: 21,2% → 19,7%; 11: 6,5% → 4,3%.
- Rozkład liter kluczy bez zmian.

## Egzaminy, kolejki, snapshoty (pułapki CI)

- Egzaminy próbne: 0605 w wariancie 001 – `wariant-001.json` (stem, options) i `klucz-001.json` (explanation, legal_basis; litera bez zmian). `excluded_question_ids` (0605 w 002–005) bez zmian.
- Kolejki `KOLEJKA-PRIORYTETOWA-4X40.json` / `4X44.json`: żadnego ID z partii – zmienia się tylko `source_bank_blob_sha`.
- Snapshoty `review/sequential/` i `review/legal-clauses/`: **598-609.json** (0601–0609) i **610-620.json** (0610–0615).
- Ledgery `review/legal-polish/stage4w4-literal-verification-ledger-0001-0609.json` (0601–0609) i `…-0610-0678.json` (0610–0615): `source_references` – 15 ID.
- Rejestry `REJESTR-AKTUALNY-0001-0765.md` i `-0001-0780.md`: po 15 wierszy.
- SHA banku 6147aeb4… w **44 plikach** poza historycznymi raportami `review/literal-pl/` i poza `tests/test_literal_review_0601_0615.py` (FIRST_PASS) – w tym 20 testów `test_literal_review_0301_0315 … 0586_0600` (tylko EXPECTED_BANK_SHA).
- Lekcje, instruktor i scenariusze odwołują się do ID tylko w listach – tematy zgodne (SC-ADR-B-01, SC-ADR-B-01-03, SC-ADR-B-11-02, SC-ADR-B-11-03, SC-ADR-B-13), bez zmian.
- Oczekiwany SHA banku: **6147aeb45bf0efd1631ae17ce5e1d82357bffb0b → 7c6b46d4134301f616cfc39d2b3e33e4318da428**.

## Test na kopii repo

`test_p41.sh` – git worktree `/tmp/b41` z main 757412d62 (bez commitów i pushu): `tools/apply_poprawki.py` z dopisanym `POPRAWKI-KONTROLA2-0601-0615.jsonl` → „Changed (15)”, blob **7c6b46d4134301f616cfc39d2b3e33e4318da428**; synchronizacja (`sync_p41_test.py`); wszystkie **14 skryptów CI** – kod 0; `python3 -m unittest discover -s tests` – **Ran 235 tests – OK**.