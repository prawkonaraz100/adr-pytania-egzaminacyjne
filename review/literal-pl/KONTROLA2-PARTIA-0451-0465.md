# Kontrola druga – partia ADR-B-0451–0465 (porównanie dosłowne z polskim tekstem ADR 2025)

Data: 2026-11-09, ok. 22:15 (czas polski, CET).
Przedmiot: pierwsza kontrola ChatGPT (PR #892, scalony; main **ab49a858a**; `review/literal-pl/PARTIA-0451-0465.md` + `.json` + `tests/test_literal_review_0451_0465.py`, wynik 1 OK / 14 POPRAW / 0 BLOKUJ) oraz rekordy 0451–0465 na main (bank blob **09447316…**, 780 pytań; #892 banku nie zmienia).
Źródło: Dz.U. 2025 poz. 642 (skany PDF), OCR tesseract `-l pol`; strony wg nagłówka „Dziennik Ustaw — NNN —”. Na **obrazach stron PDF** sprawdzone: s. 111 (tabela 1.10.3.1.2 z przypisami a–d), s. 937 (5.2.1.8.1–5.2.1.8.3), s. 966 (5.4.1.1.18), s. 967 (5.4.1.1.24). Sprostowanie poz. 1575 nie dotyczy punktów tej partii (1.1.3.6.2, 1.1.4.7, 1.10.3.1.2, 4.1.6.12, 5.2.1.8, 5.4.1.1.18, 5.4.1.1.24).
Status: kontrola robocza. **Żadne pytanie nie jest oznaczone jako zweryfikowane**; wszystkie pozostają `needs_review`.

## Podsumowanie

- Werdykty kontroli drugiej: **OK 0, POPRAW 15, BLOKUJ 0** (#892: 1 OK – 0459 nie jest OK, niżej).
- **3 pytania to duplikaty lub bliskie powtórzenia** → **nowy element z tej samej kompetencji, niecysternowy**: 0454 ≈ 0453 (ten sam zapis 5.4.1.1.24, różni się tylko cyfrą .1/.2), 0456 ≈ 0460/0457 (wartość z kolumny cysterny nie przenosi się na sztuki przesyłek – „czytaj kolumnę dla sposobu przewozu”; dodatkowo temat cysternowy), 0464 = 0045 (miejsce znaku środowiskowego obok oznakowań przesyłki, 5.2.1.8.2).
- **12 pytań** (0451, 0452, 0453, 0455, 0457, 0458, 0459, 0460, 0461, 0462, 0463, 0465) ma właściwy podtemat, ale wady formy/treści → przeredagowane w tym samym podtemacie. **0465 miało błędny klucz co do brzmienia** (polski ADR: „ZAGRAŻAJĄCY ŚRODOWISKU”, nie „ENVIRONMENTALLY HAZARDOUS”) – litera B zostaje, treść poprawiona.
- **Żaden zamiennik nie jest cysternowy**: 0454 → butla DOT, 4.1.6.12 (b); 0456 → naboje UN 0012 w sztukach przesyłek (wiersz 1.4 tabeli); 0464 → kanister UN 3082 (znak środowiskowy obok nalepki 9).
- Wszędzie ta sama litera klucza, ten sam `module_id`, `image` = null; przypisania w `kompetencje.json` bez zmian (10-K05 = 19, 12-K05 = 17, 03-K01 = 13; każda kompetencja teoretyczna ≥ 6).
- **Wady formy starych wersji**: opcje > 80 zn. – 0451 C (81), 0455 B (87), 0457 A (84), 0460 A (81), 0461 A/B (85/99), 0465 A/B (90/87); średniki – 0451 B, 0452 A/B/C, 0456 A/B/C, 0460 A/B/C, 0462 A/B; słowa absolutne – 0452 A „żadnym”, B „tylko”, 0454 A „zawsze”, 0455 B „Wyłącznie”, 0456 A „każdego”, 0457 A „niezależnie”, B „każda”, 0458 C „niezależnie”, 0459 A „dowolną”, 0460 A „każda … zawsze … niezależnie”, B „żadnych”, 0461 B „wszystkie … niezależnie”, C „tylko”, 0462 A „tylko”, 0463 A „zawsze”, 0464 A „wyłącznie”, B „tylko”, 0465 A „żadnego”; klucz jedyną najkrótszą – 0455, 0457, 0460, 0463, 0464; kropki na końcu opcji – 0458 B/C; klucz-polecenie zamiast treści – 0453 („Dodać wzmiankę…”), 0454 („W dokumencie umieścić…”); klucz odsyła sam do siebie – 0461 („gdy spełniono warunki 5.2.1.8.1”); treść podpowiada klucz – 0459 („dodatniej ilości” w treści i w kluczu); zmyślone liczby w dystraktorach – 0458 C „próg 100 kg”, 0462 B „30 l”; w wyjaśnieniach: 0460 „Odpowiedzi A i B”, polecenia „Sprawdź…/Odczytaj…” zamiast wyjaśnienia (0453, 0455, 0456, 0457, 0464, 0465), „automatycznie” (0457, 0458).

## Błędy / różnice względem raportu ChatGPT (#892)

1. **Błędne strony Dz.U. (o jedną za mało)**: 5.2.1.8.1–5.2.1.8.2 stoją na **s. 937** (nie 936); 5.4.1.1.18 na **s. 966** (nie 965); 5.4.1.1.24 na **s. 967** (nie 966); opis znaku z 5.2.1.8.3 (romb, 100 × 100 mm) na **s. 938** (propozycja 0464 podaje 936). Sprawdzone na obrazach stron PDF (część 19 s. 37–38, część 20 s. 16–17). Strony 1.1.4.7.2 (s. 31) i 1.10.3.1.2 (s. 111) – poprawne.
2. **0459 nie jest OK**: treść podpowiada klucz („przy przewozie dodatniej ilości” → klucz „przekroczony dla dodatniej ilości”), pytanie abstrakcyjne („dla danego towaru”), A „dowolną”, wyjaśnienie ogólnikowe („Próg 3000 kg dotyczy innego wpisu”) i **bez zastrzeżenia z 1.1.3.6.2**: przy przewozie w sztukach przesyłek ze zwolnieniem z 1.1.3.6 dział 1.10 nie ma zastosowania (poza towarami dużego ryzyka klasy 1 i klasą 7) – więc „próg 0 kg = każda ilość jest towarem dużego ryzyka” bez tego zastrzeżenia jest nieprawdą dla 6.1. Przeredagowane: 30 kg 6.1 I gr. na pełnych zasadach ADR.
3. **Przeoczone bliskie powtórzenia**: 0453/0454 (#892: „dwa różne, dosłownie wskazane wpisy”) – to jeden przepis i jeden zapis „PRZEWÓZ ZGODNY Z 1.1.4.7.x”, różni się tylko cyfrą; po przeredagowaniu 0453 wariant .2 jest jej dystraktorem. 0456 – „czytaj kolumnę dla sposobu przewozu” to ten sam element co klucz 0460 („trzeba uwzględnić … sposób przewozu i próg tabeli”) i bliski 0457; do tego temat cysternowy – zastąpione tematem niecysternowym.
4. **Propozycja zastępcza 0464 z wadami**: opcja A „Prostokąt 100 × 100 mm…” nie jest jednoznacznie błędna – kwadrat 100 × 100 mm to ta sama figura co romb (kwadrat obrócony o 45°), więc pytanie miałoby dwie bronione odpowiedzi; wszystkie trzy opcje powtarzają „z czarnym symbolem na białym lub kontrastowym tle”, czyli element już sprawdzany w 0276 (a 0007 = symbol z tego samego rysunku 5.2.1.8.3); strona 936 błędna (opis znaku – s. 938). Zastąpiłem innym elementem: znak środowiskowy umieszcza się oprócz nalepki wzoru 9 (5.2.1.8.1–5.2.1.8.2).
5. **Przeoczone wady formy**: 0458 C – zmyślony „próg 100 kg”, kropki w B/C; 0462 B – zmyślony limit „30 l”; 0461 – klucz odsyła sam do siebie; 0460 – w wyjaśnieniu „Odpowiedzi A i B”; 0452 A „żadnym”, B „tylko”; 0457 A „niezależnie”, B „każda”; 0451 – wyjaśnienie bez treści przepisu („w zwykłym trybie”). 0461 – #892 widzi tylko długości.
6. **Znowu bez repozytoryjnego similarity.py** („wykonano według algorytmu…” – własna implementacja). Na kopii po poprawkach `similarity.py --threshold 0.25`: pary z partią – 0461/0463 = 0,318, 0462/0463 = 0,280, 0459/0460 = 0,267, 0407/0456 = 0,250 (inne elementy przepisu; ręcznie sprawdzone niżej). `check_near_duplicates.py --threshold 0.40` – brak par z partią.
7. **Słusznie w #892**: 0464 = 0045; **0465 – błędne brzmienie klucza** (dobre wychwycenie: „ZAGRAŻAJĄCY ŚRODOWISKU” lub „MARINE POLLUTANT / ENVIRONMENTALLY HAZARDOUS”) i „zwykle”; 0453/0454 – klucze-polecenia zamiast treści zapisu; 0451 – „nie powinny być napełniane”; odczyt tabeli 1.10.3.1.2 (wiersz 6.1 = 0 kg, klasa 3 = 3 000 / a / b); cytaty dosłowne; licznik 330 → 315; test od razu z dwiema stałymi FIRST_PASS_BANK_SHA / EXPECTED_BANK_SHA.

## Duplikaty – sprawdzenie w całym banku (780) i między sobą

Przeszukano cały bank po temacie (1.1.4.2, 1.1.4.7, DOT, butle, 4.1.6.12–13, termin badania, 5.4.1.1.7, 5.4.1.1.24, dużego ryzyka, 1.10.3, tabela, próg, 0 kg, UN 0012, naboje, 1.4, środowisko, ryba i drzewo, 5.2.1.8, 5 l / 5 kg, nalepka 9, 5.4.1.1.18, ZAGRAŻAJĄCY ŚRODOWISKU, MARINE POLLUTANT) oraz skryptami `check_near_duplicates.py` (0,60 i 0,40), `check_cross_module_duplicates.py` (0,80), `similarity.py` (0,45; dodatkowo 0,25) na kopii po poprawkach.
- **0451** (nie napełniać po terminie badania) vs **0452** (przewóz po terminie w celu badania, z przewozami pośrednimi) – dwie różne normy tego samego zdania (zakaz napełniania / zezwolenie na przewóz) – zostają oba. vs 0446 (4.1.6.12 (c) – nieczytelne znaki), 0386 (4.1.6.13 (a) – nieszczelna), **nowa 0454** (4.1.6.12 (b) – sprawdzenie stanu przed napełnieniem) – inne przesłanki.
- **0453** (zapis „PRZEWÓZ ZGODNY Z 1.1.4.7.1”) vs 0061/0089/0708/0714/0779 (zapis z 5.4.1.1.7 dla 1.1.4.2.1), 0215 – inny zapis i inny przepis.
- **0454 nowa** – pierwotny pomysł (1.1.4.2.1 akapit ostatni: towar niebezpieczny według ADR, a nie według IMDG) **odrzucony**, bo to już **0247 i 0770** (uwaga na później: 0247 i 0770 dublują się wzajemnie – partia 52). Wybrany element 4.1.6.12 (b) – w banku brak.
- **0455** (o zaliczeniu decyduje wpis w tabeli i ilość większa niż podana) vs 0304 (sens pojęcia – zamach), 0407 (środki z 1.10.3.3), 0122/0212 (plan ochrony). **0456 nowa** (wiersz 1.4 – tylko wymienione numery UN; UN 0012 poza wykazem) vs 0249 (klasa 1 dużego ryzyka w limicie 1.1.3.6), 0425/0429 (naboje 1.4S – ładowanie razem) – inny element. **0457** (przypis b – gazy palne w butlach), **0458** (przypis a – klasa 3 luzem), **0459** (0 kg – 6.1 I gr., 30 kg), **0460** (klasa 3 III gr. – brak w tabeli) – cztery różne komórki i różne reguły odczytu.
- **0461** (opakowanie pojedyncze, 4 l cieczy – zwolnione), **0462** (opakowania wewnętrzne po 6 l – limit na każde opakowanie wewnętrzne), **0463** (dokładnie 5 kg netto, masa netto zamiast brutto, „nie więcej niż”) – różne przypadki graniczne. **0464 nowa** (znak środowiskowy oprócz nalepki 9) vs 0045 (miejsce znaku), 0007/0276 (symbol, tło), 0734 (wyposażenie przy UN 3082), 0099 (klasa 9) – inny element. **0465** (brzmienie zapisu) vs 0466 (wyłączenie UN 3077/3082), 0467 (MARINE POLLUTANT w łańcuchu morskim).

## Ustalenia dla poszczególnych pytań (cytaty, strony Dz.U., klucze)

### ADR-B-0451 – POPRAW (10-K05, B) – przeredagowane
- 1.1.4.7.2 (c) (s. 31): „Naczynia ciśnieniowe nie powinny być napełniane po upływie ich terminu badania okresowego…”. Klucz B „Nie, po upływie terminu badania okresowego nie powinna być napełniana” ✔.

### ADR-B-0452 – POPRAW (10-K05, C) – przeredagowane
- 1.1.4.7.2 (c) (s. 31): „…ale mogą być przewożone po upływie tego terminu, w celu przeprowadzenia badań, łącznie z przewozami pośrednimi.” Klucz C „Tak, w celu badania, także z przewozami pośrednimi po drodze” ✔.

### ADR-B-0453 – POPRAW (10-K05, C) – przeredagowane (klucz = dosłowny zapis)
- 5.4.1.1.24 (s. 967): „W przypadku przewozu zgodnego z 1.1.4.7 w dokumencie przewozowym należy, odpowiednio, umieścić następujące zapisy: „PRZEWÓZ ZGODNY Z 1.1.4.7.1” lub „PRZEWÓZ ZGODNY Z 1.1.4.7.2””. 1.1.4.7.1 (s. 31) – przywóz do odbiorcy finalnego. Klucz C „„PRZEWÓZ ZGODNY Z 1.1.4.7.1”” ✔.

### ADR-B-0454 – POPRAW (10-K05, C) – NOWY ELEMENT, NIECYSTERNOWY (≈ 0453)
- 1.1.4.7.2 (c) (s. 31): „Do naczyń ciśnieniowych mają zastosowanie przepisy 4.1.6.12 i 4.1.6.13.” 4.1.6.12 (s. 855): „Naczynia ciśnieniowe nie powinny być przeznaczone do napełniania: … (b) dopóki podczas badania nie stwierdzi się dobrego stanu technicznego naczynia i jego wyposażenia obsługowego”. Klucz C „Nie, butlę napełnia się dopiero po stwierdzeniu dobrego stanu jej i zaworu” ✔.

### ADR-B-0455 – POPRAW (12-K05, A) – przeredagowane
- 1.10.3.1.2 (s. 111): „Towarami niebezpiecznymi dużego ryzyka klas innych niż klasa 7 są towary wskazane w tabeli 1.10.3.1.2 poniżej, przewożone w ilościach większych niż wskazane w tej tabeli.” Klucz A ✔.

### ADR-B-0456 – POPRAW (12-K05, B) – NOWY ELEMENT, NIECYSTERNOWY (≈ 0460/0457, temat cysternowy)
- Tabela 1.10.3.1.2 (s. 111, obraz strony): wiersz 1.4 – „Materiały wybuchowe i przedmioty z materiałami wybuchowymi: UN: 0104, 0237, 0255, 0267, 0289, 0361, 0365, 0366, 0440, 0441, 0455, 0456, 0500, 0512 i 0513” – UN 0012 poza wykazem; wiersze 1.1, 1.2, 1.3 (gr. zgodności C), 1.5, 1.6 – ogólnie. Klucz B „Nie, UN 0012 nie jest wśród numerów UN wymienionych w wierszu podklasy 1.4” ✔. Ogólne zasady 1.10.1 – w wyjaśnieniu.

### ADR-B-0457 – POPRAW (12-K05, C) – przeredagowane (konkretny wiersz)
- Tabela 1.10.3.1.2 (s. 111): klasa 2 „Gazy palne nietrujące (kody klasyfikacyjne zawierające wyłącznie litery F lub FC)” – cysterna 3 000 / luzem a / sztuki przesyłek **b**; przypis b: „Niezależnie od ilości towarów, przepisy rozdziału 1.10.3 nie mają zastosowania.” Klucz C ✔.

### ADR-B-0458 – POPRAW (12-K05, A) – przeredagowane (konkretny wiersz)
- Tabela 1.10.3.1.2 (s. 111): klasa 3 „Materiały zapalne ciekłe I i II grupy pakowania” – 3 000 / **a** / b; przypis a: „Nie dotyczy.” Klucz A „Że kolumna przewozu luzem nie dotyczy tej pozycji tabeli” ✔.

### ADR-B-0459 – POPRAW (12-K05, B) – przeredagowane (#892: OK)
- Tabela 1.10.3.1.2 (s. 111): 6.1 „Materiały trujące I grupy pakowania” – 0 / a / **0**; zdanie wprowadzające: „…w ilościach większych niż wskazane w tej tabeli”. 1.1.3.6.2 (s. 26): przy zwolnieniu ilościowym bez stosowania „działu 1.10, z wyjątkiem towarów dużego ryzyka klasy 1 … oraz … materiałów klasy 7…” – dlatego w treści „na pełnych zasadach ADR, bez zwolnienia z 1.1.3.6” (30 kg > 20 kg dla kat. 1). Klucz B ✔.

### ADR-B-0460 – POPRAW (12-K05, C) – przeredagowane (konkretny przypadek)
- Tabela 1.10.3.1.2 (s. 111): w klasie 3 tylko „Materiały zapalne ciekłe I i II grupy pakowania” i „Materiały wybuchowe odczulone ciekłe” – brak III grupy pakowania (UN 1202 olej napędowy, III gr.). Klucz C ✔.

### ADR-B-0461 – POPRAW (03-K01, A) – przeredagowane
- 5.2.1.8.1 (s. 937): „…z wyłączeniem opakowań pojedynczych oraz opakowań wewnętrznych w opakowaniach kombinowanych, jeżeli … zawierają: nie więcej niż 5 l materiałów ciekłych, lub nie więcej niż 5 kg netto materiałów stałych.” Klucz A ✔.

### ADR-B-0462 – POPRAW (03-K01, C) – przeredagowane
- 5.2.1.8.1 (s. 937) – jw.; limit dotyczy każdego opakowania wewnętrznego; 6 l > 5 l. Klucz C ✔.

### ADR-B-0463 – POPRAW (03-K01, C) – przeredagowane
- 5.2.1.8.1 (s. 937): „nie więcej niż 5 kg netto materiałów stałych” – 5 kg netto (brutto 5,3 kg) mieści się w limicie. Klucz C ✔.

### ADR-B-0464 – POPRAW (03-K01, C) – NOWY ELEMENT (duplikat 0045)
- 5.2.1.8.1 (s. 937): „Sztuki przesyłek zawierające materiały zagrażające środowisku spełniające kryteria podane w 2.2.9.1.10, powinny być trwale oznakowane znakiem dla materiału zagrażającego środowisku, podanym w 5.2.1.8.3…”; 5.2.1.8.2 (s. 937): „…w pobliżu znaków wymaganych w 5.2.1.1.” Kanister 20 l > 5 l. Klucz C „Tak, znak środowiskowy umieszcza się na kanistrze oprócz nalepki wzoru 9” ✔.

### ADR-B-0465 – POPRAW (03-K01, B) – przeredagowane (błędne brzmienie klucza)
- 5.4.1.1.18 (s. 966): „Jeżeli materiał należący do klasy od 1 do 9 spełnia kryteria klasyfikacyjne podane w 2.2.9.1.10, to dokument przewozowy powinien zawierać dodatkowy zapis „ZAGRAŻAJĄCY ŚRODOWISKU” lub „MARINE POLLUTANT / ENVIRONMENTALLY HAZARDOUS”. Tego dodatkowego zapisu nie stosuje się do UN 3077 i UN 3082 oraz w przypadku wyłączeń podanych w 5.2.1.8.1.” Klucz B (nowe brzmienie) ✔.

## Wskaźniki

- „Poprawna = jedyna najdłuższa”: **32/780 = 4,10% bez zmian**, maksimum działu **7,87%** bez zmian – tych linii w `docs/POKRYCIE-KURSU.md`, `podstawowy/README.md`, `PAKIET-ZAMKNIECIE-0780.md` **nie zmieniać** (tylko SHA tam, gdzie występuje).
- „Poprawna = jedyna najkrótsza”: **173 → 168/780**; ADR-B-03 21,7% → **18,3%** (11/60), ADR-B-12 22,9% → **16,7%** (8/48), ADR-B-10 10,5% bez zmian; maksimum działu 31,5% (bez zmian); wszystkie działy ≤ 38%.
- Wszystkie 15 wyjaśnień: 5 zdań, 372–515 znaków, maks. 29 słów w zdaniu, na końcu „Podstawa: ADR …”; opcje 28–79 znaków; bez słów absolutnych i średników w opcjach.

## Egzaminy, kolejki, snapshoty (pułapki CI)

- Egzaminy próbne – w `questions`: **0465 – wariant-001/klucz-001, 0451 – wariant-002/klucz-002, 0464 – wariant-004/klucz-004, 0462 – wariant-005/klucz-005**. Na listach `excluded_question_ids` są ID z partii (002: 0465; 003: 0451, 0465; 004: 0451, 0465; 005: 0451, 0464, 0465) – tych list **nie zmieniać**. Pozostałe pliki egzaminów – tylko SHA.
- `review/specialist/KOLEJKA-PRIORYTETOWA-4X40.json` zawiera **0451 i 0452**, `KOLEJKA-PRIORYTETOWA-4X44.json` zawiera **0453** („question” + „legal_basis”).
- Snapshoty: `review/sequential/` i `review/legal-clauses/` – pliki **447-454.json** (0451–0454), **455-460.json** (0455–0460), **461-470.json** (0461–0465); clause, answer_review A/B/C, notes_on_conditions ≥ 25 zn.
- Ledger `review/legal-polish/stage4w4-literal-verification-ledger-0001-0609.json`: `source_references` z nowych sources dla 15 ID (zmienia się 10: 0451, 0452, 0453, 0454, 0456, 0457, 0458, 0459, 0460, 0464).
- Rejestry `REJESTR-AKTUALNY-0001-0765.md` i `-0001-0780.md`: po 15 wierszy.
- SHA banku 09447316… występuje w **34 plikach** poza historycznymi raportami `review/literal-pl/`: **33 zamieniane wprost** (docs/POKRYCIE-KURSU.md, docs/STAN-KONCOWY-…, podstawowy/README.md, review/README.md, podstawowy/raporty/etap-4x135-wykluczenia-proby.json, 8 plików review/specialist, 10 plików egzaminów, tests/test_literal_review_0301_0315 … 0421_0435 (9) i **0436_0450** (EXPECTED_BANK_SHA **oraz** literał w `test_second_pass_artifacts_and_bank_sha`; FIRST_PASS fa4e3835… zostaje)) + `tests/test_literal_review_0451_0465.py` – TYLKO EXPECTED_BANK_SHA (FIRST_PASS_BANK_SHA = 09447316… zostaje).
- Oczekiwany SHA banku: **094473164719bc6a651a6e303dc117cfa6503ffb → e560a3892b2b76217bf4ff9a977a1a4c2771eff8**.

## Test na kopii repo

`test_p31.sh` (kopia /tmp/b31 z main **ab49a858a** = po scaleniu #892, bez commitów i pushu): `apply_poprawki.py` → „Changed (15): ADR-B-0451 … ADR-B-0465”, blob **e560a3892b2b76217bf4ff9a977a1a4c2771eff8**; po synchronizacji (`sync_p31_test.py`, 43 zmienione pliki + nowy POPRAWKI) wszystkie 14 skryptów CI = 0 i `python3 -m unittest discover -s tests` – **197 testów OK**.

## Licznik

Po wdrożeniu partii 31 (obie kontrole 0451–0465): **315 pytań bez porównania dosłownego po obu kontrolach** (0466–0780); kontrola pierwsza partii 32 (0466–0480): 315 → 300.

## Do zapamiętania na kolejne partie
- 0466 – treść mówi o „dodatkowym wpisie ENVIRONMENTALLY HAZARDOUS”; polski 5.4.1.1.18 ma „ZAGRAŻAJĄCY ŚRODOWISKU” lub „MARINE POLLUTANT / ENVIRONMENTALLY HAZARDOUS” – poprawić brzmienie (strona 5.4.1.1.18 = s. 966). 0466–0470 porównać z nowymi 0461–0465 (zwłaszcza 0464 – UN 3082 i znak) oraz z 0007, 0045, 0276; 0469/0470 (5.3.6.2) – 0470 to kontener-cysterna: przy duplikacie zamiennik NIECYSTERNOWY.
- 0247 i 0770 dublują się wzajemnie (1.1.4.2.1 akapit ostatni) – przy partii 52 (0766–0780).
- 0071/0072 (0,909) i 0632 (≈ stara 0297) – przy właściwych partiach (bez zmian).