# Kontrola druga – partia ADR-B-0406–0420 (porównanie dosłowne z polskim tekstem ADR 2025)

Data: 2026-11-09, ok. 17:55 (czas polski, CET).
Przedmiot: pierwsza kontrola ChatGPT (PR #885, scalony na main **396b22d41**; `review/literal-pl/PARTIA-0406-0420.md` + `.json` + `tests/test_literal_review_0406_0420.py`, wynik 0 OK / 15 POPRAW / 0 BLOKUJ) oraz rekordy 0406–0420 na main 396b22d41 (bank blob **5e369822…**, 780 pytań).
Źródło: Dz.U. 2025 poz. 642 (skany PDF), OCR tesseract `-l pol`; strony wg nagłówka „Dziennik Ustaw — NNN —”. Tabela 8.1.4.1 odczytana z **obrazu strony PDF** (część 27, strona 24 = **Dz.U. s. 1324**, render 300 dpi). Sprostowanie poz. 1575 nie dotyczy punktów tej partii (1.10, 1.2.1, 8.1.4).
Status: kontrola robocza. **Żadne pytanie nie jest oznaczone jako zweryfikowane**; wszystkie pozostają `needs_review`.

## Podsumowanie

- Werdykty kontroli drugiej: **OK 0, POPRAW 15, BLOKUJ 0** (liczbowo jak #885, ale z innymi ustaleniami – niżej).
- **7 pytań to duplikaty lub bliskie powtórzenia** (0409 = 0036, 0413 ≈ 0776, 0414 = 0120, 0415 ≈ 0701/0035/0775, 0416 = 0067/0175/0519/0672, 0417 ≈ 0071, 0420 ≈ 0022) → **nowy temat z tej samej kompetencji, niecysternowy**. **8 pytań** (0406, 0407, 0408, 0410, 0411, 0412, 0418, 0419) ma właściwy podtemat, ale wady formy/treści → przeredagowane w tym samym podtemacie (0419 bliskie 0072 – zostaje granica 7,5 t, ale jako ocena zestawu 2 kg + 6 kg). Wszędzie ta sama litera klucza, ten sam `module_id`, `image` = null; przypisania w `kompetencje.json` bez zmian (08-K01 = 7, 12-K01 = 6, 12-K02 = 6, 12-K03 = 7, 12-K04 = 6, 12-K05 = 17, 12-K06 = 6; każda kompetencja teoretyczna ≥ 6).
- **Zmiany kluczy (litery bez zmian, sens/treść klucza poprawiony)**: 0406 (z „potrzebują do zadań” na „osoby upoważnione z zachowaniem innych wymagań ADR” – lit. (h)), 0411 („przed powierzeniem zadań” → „przeprowadzone lub **weryfikowane** przy zatrudnianiu + okresowo uzupełniane”), 0412 (dodane udostępnianie **pracownikowi** i okres ustalany przez właściwą władzę), 0413 (usunięty nieistniejący w 1.10.1.2 warunek „upoważnienia kierowcy”), 0417 (stara opcja B fałszywie twierdziła, że dla > 7,5 t wymagane są **trzy** gaśnice – tabela: 2 w każdym wierszu).
- **Tematy cysternowe**: żaden zamiennik nie jest cysternowy.
- **Wady formy starych wersji**: opcje > 80 zn. – 0407 A/C (84/89), 0408 A (83), 0410 A/B/C (81/83/82), 0411 C (85), 0412 A/B/C (94/86/82), 0413 A/B (86/93), 0415 A/B/C (86/89/82), 0416 C (89), 0417 B (102), 0418 C (90); klucz jedyną najkrótszą – 0407, 0408, 0411, 0412, 0414, 0416; klucz jedyną najdłuższą – 0420; średniki – 0418 A/B, 0420 A/B/C; słowa absolutne w opcjach – 0406 A „Każdy”, B „Wyłącznie”, 0407 C „tylko”, 0410 A „wszystkie … bez wyjątków”, B „Każdemu”, 0412 A „wyłącznie”, 0413 C „każdemu”, 0415 C „wyłącznie”, 0416 A „Każdy”; opcje-polecenia przy pytaniu „kto/co” – 0406 C, 0412, 0413 A–C, 0414, 0415; opcje 0419 – jeden szablon różniący się tylko liczbą; wyjaśnienie 0418 mówi o „obecności drugiej osoby”, której nie ma w opcjach; 0417/0419 mówią „DMC pojazdu”, a tabela dotyczy **dopuszczalnej masy całkowitej jednostki transportowej**.

## Błędy / różnice względem raportu ChatGPT (#885)

1. **BŁĘDNA STRONA tabeli 8.1.4.1 (0417–0420)**: #885 podaje Dz.U. s. **1325** – tabela 8.1.4.1 stoi na **Dz.U. s. 1324** (nagłówek „Dziennik Ustaw — 1324 — Poz. 642”, stopka ADR 619). Na s. 1325 są 8.1.4.2–8.1.5.3.
2. **0420 – fałszywy zarzut i fałszywa treść tabeli**: #885 pisze „dla > 7,5 t tabela wymaga **trzech** gaśnic”, „wyjaśnienie błędnie podaje co najmniej dwie”. Obraz tabeli (s. 1324): kolumna (2) „Minimalna liczba gaśnic” = **2** we wszystkich trzech wierszach (≤ 3,5 t / > 3,5 t ≤ 7,5 t / > 7,5 t); dla > 7,5 t: 12 kg, gaśnica silnik/kabina ≥ 2 kg, co najmniej jedna dodatkowa ≥ 6 kg. Wyjaśnienie 0420 było w tym punkcie **poprawne**.
3. **0417 – przeoczony fałsz w dystraktorze**: stara opcja B „trzy gaśnice … jak dla jednostek o DMC powyżej 7,5 t” uczy nieprawdy (#885 wskazał tylko długość 102 zn.). Ponadto 0417 (3,5 t → 2 gaśnice / 4 kg) dubluje **0071** (3,5 t → 4 kg) – #885 tego nie wykrył.
4. **Znaki graniczne** (#885: „nie przesądzam”): obraz potwierdza „≤ 3,5 tony”, „> 3,5 tony ≤ 7,5 tony”, „> 7,5 tony” – 3,5 t należy do pierwszego wiersza, 7,5 t do drugiego. Klucze 0417 (C) i 0419 (B) w starych wersjach były poprawne.
5. **Nieuznane duplikaty**: 0413 bliskie 0776 (kierowca u bramy, upoważnienie), 0416 = 0067/0175/0519/0672 (drugi członek załogi z identyfikatorem bez zdjęcia – #885 widział podobieństwo, ale proponował ten sam motyw „dokument zostawiony w biurze”, bliski 0778), 0420 bliskie 0022 (> 7,5 t → 12 kg), 0419 bliskie 0072 (6 t → 8 kg).
6. **Propozycje zastępcze #885 wadliwe**: 0409 („metody wykrywania i usuwania zagrożeń”) – bliskie 0036/0121, opcje „Wyłącznie…”/„Tylko…” (słowa absolutne); 0414 („kogo zidentyfikować – przewoźnika”) – ogólnik równoważny 0120; 0415 (wykaz miejsc) – opcje 86/87 zn., „Wyłącznie”/„Tylko”, klucz A jedyną najdłuższą… (pomysł tematu słuszny – wykorzystany w innej formie); 0416 („dokument w biurze”) – bliskie 0778 (dokumenty poza kabiną) i 0067.
7. Słusznie w #885: strony 110 (1.10.1–1.10.2) i 113 (1.10.3.2.2 (h), 1.10.3.3) poprawne; 0406 – kryterium „osoby upoważnione”; 0409 bliskie 0036; 0412 – brak pracownika i okresu przechowywania; 0413 – brak w 1.10.1.2 wymogu „upoważnienia kierowcy”; 0414 – duplikat 0120/0776; 0415 bliskie 0035/0066/0701/0775; licznik 375 → 360 poprawny; test #885 od razu z dwiema stałymi FIRST_PASS_BANK_SHA / EXPECTED_BANK_SHA (dobrze).

## Duplikaty – sprawdzenie w całym banku (780) i między sobą

Przeszukano cały bank po temacie (słowa kluczowe: gaśnic, 8.1.4, 1.10.1.x, 1.10.2.x, 1.10.3.3, upoważnion, ratownicz, rozrząd, przeładunk, 8.1.2.1 (d)) oraz skryptami `check_near_duplicates.py` (0,60), `check_cross_module_duplicates.py` (0,80), `similarity.py` (0,45) na kopii po poprawkach – żadnej pary z udziałem 0406–0420.
- **0406** (h) vs 0405 (g – ochrona fizyczna), 0410 (szkolenie – informacje o planie), 0213 (telematyka; (h) w źródle) – inny aspekt (kto ma dostęp + nie wolno blokować informacji wymaganych innymi przepisami).
- **0407** (jakie środki: urządzenia, układy lub działania; pojazd i ładunek; ubezpieczenie ≠ zapobieganie) vs 0305 (naczepa też), 0213 (telematyka nie zastępuje), 0144 (8.4.1 parking), 0582 (plan – postój) – różne.
- **0408** (środki nie mogą utrudniać akcji ratowniczo-gaśniczej) – w banku jedyne pytanie o 1.10.3.3 zdanie 2 (25 trafień „ratownicz” to 5.4.3.4).
- **0409** stara = **0036** (zakres szkolenia 1.10.2.2). Nowa: 1.10.2.1 zdanie 1 (szkolenie z działu 1.3 obejmuje ochronę; magazynierzy) – 0275 dotyczy zdania 2 (doskonalące nie tylko o zmianach przepisów).
- **0410** (informacje o planie wg funkcji) – unikalne. **0411** (weryfikacja szkolenia z ochrony przy zatrudnieniu) – 0275 (okresowość), 0521 (1.3.3, moduł 01 – inny przepis). **0412** (udostępnienie pracownikowi) – unikalne (jedyne 1.10.2.4).
- **0413** stara ≈ **0776**. Nowa: dowód ze zdjęciem kierowcy (1.10.1.4) ≠ identyfikacja przewoźnika (1.10.1.2). **0414** stara = **0120** (+ dystraktory 0249/0776 o numerze zlecenia). Nowa: terminal przeładunkowy wydaje przesyłki kolejnemu przewoźnikowi (1.10.1.2 z 1.10.1.1). Sprawdzone z 0211 (towar nie dużego ryzyka), 0249 (1.1.3.6 + kl. 1).
- **0415** stara ≈ **0701** (otwarta brama od ulicy), 0035, 0775. Nowa: plac przeładunkowy/stacja rozrządowa przy przeładunku na kolej – 0274 dotyczy bazy transportowej przewoźnika.
- **0416** stara = **0067/0175/0519/0672**. Nowa: 1.10.1.4 to przepis ogólny 1.10.1 – dotyczy także przewozu towaru, który nie jest towarem dużego ryzyka. Sprawdzone z 0034, 0087, 0300 (praktykant), 0774 (paszport), 0778 (miejsce dokumentów).
- **0417** stara ≈ **0071**. Nowa: wiersz tabeli wg dopuszczalnej masy całkowitej **całej jednostki transportowej** (samochód 7 t + przyczepa, zespół 12 t) – w banku brak takiego pytania dla 8.1.4.1 (0711/0760 dotyczą jednostki przy 8.1.4.2).
- **0418** (jedna gaśnica 8 kg przy 6 t – liczba gaśnic) – różni się od 0072 (suma 8 kg). **0419** (dokładnie 7,5 t, zestaw 2 + 6 kg spełnia) – granica i kolumna (5), różne od 0072. **0420** stara ≈ **0022**. Nowa: kolumna (5) – zestaw 2/2/4/4 kg = 12 kg bez gaśnicy 6 kg nie spełnia tabeli.
- Uwaga poza partią: para **0071 / 0072** (podobieństwo treści 0,909 w `similarity.py`) – do przejrzenia przy kontroli tych pytań (już po obu kontrolach – tylko informacyjnie).

## Ustalenia dla poszczególnych pytań (cytaty, strony Dz.U., klucze)

### ADR-B-0406 – POPRAW (12-K05, C) – przeredagowane, lit. (h)
- 1.10.3.2.2 (h) (s. 113): „działania zapewniające ograniczenie dostępu do informacji o operacjach transportowych zawartych w planie ochrony wyłącznie do osób upoważnionych. Działania te nie powinny pozostawać w sprzeczności z wymaganiami dotyczącymi podawania informacji zawartymi w innych przepisach ADR.” Nowy klucz C „Dostęp mają osoby upoważnione, z zachowaniem innych wymagań ADR” ✔. Stary: kryterium „potrzebują do zadań”, opcja-polecenie przy „Kto…”, „Każdy”/„Wyłącznie”.

### ADR-B-0407 – POPRAW (12-K06, B) – przeredagowane, 1.10.3.3 zdanie 1
- 1.10.3.3 (s. 113): „powinny być zastosowane urządzenia, układy lub działania skutecznie zapobiegające kradzieży tych pojazdów i ich ładunku.” Stare pytanie „kiedy” – przepis nie mówi o czasie; dopowiadało „przez cały przewóz”. Nowy klucz B ✔; dystraktory: alarm bez ochrony ładunku, ubezpieczenie zamiast zabezpieczeń.

### ADR-B-0408 – POPRAW (12-K06, B) – przeredagowane (forma), 1.10.3.3 zdanie 2
- 1.10.3.3 (s. 113): „Zastosowanie wymienionych środków nie powinno utrudniać prowadzenia akcji ratowniczo-gaśniczej.” Klucz B ✔ (stary też merytorycznie poprawny; A 83 zn., klucz jedyną najkrótszą). Pytanie jest w **egzaminie 003** (questions) i na listach excluded 004/005.

### ADR-B-0409 – POPRAW (12-K03, C) – NOWY TEMAT (duplikat 0036)
- 1.10.2.1 (s. 110): „Szkolenie oraz szkolenie doskonalące, określone w dziale 1.3, powinny obejmować również wiedzę na temat ochrony.” Nowy klucz C ✔. Dystraktory: tylko przy towarach dużego ryzyka (1.10.2 to przepis ogólny, nie 1.10.3), tylko kierowcy (1.3 – wszystkie osoby uczestniczące w przewozie).

### ADR-B-0410 – POPRAW (12-K03, C) – przeredagowane (forma), 1.10.2.2 zdanie 2
- 1.10.2.2 (s. 110): „Jeżeli wymagane jest sporządzenie planu ochrony, to szkolenie powinno zawierać informacje o tym planie odpowiednio do zakresu obowiązków i odpowiedzialności osób szkolonych oraz do ich funkcji związanych z wykonaniem planu.” Klucz C ✔.

### ADR-B-0411 – POPRAW (12-K03, B) – przeredagowane, 1.10.2.3
- 1.10.2.3 (s. 110): „Szkolenie powinno być przeprowadzone lub weryfikowane przy zatrudnianiu na stanowiska związane z przewozem towarów niebezpiecznych oraz powinno być okresowo uzupełniane szkoleniem doskonalącym.” Nowy klucz B „Zweryfikować je przy zatrudnieniu, a potem okresowo je uzupełniać” ✔ (stary: „przed powierzeniem zadań” – niedokładne).

### ADR-B-0412 – POPRAW (12-K03, C) – przeredagowane, 1.10.2.4
- 1.10.2.4 (s. 110): „Dokumenty potwierdzające przeprowadzenie wszystkich szkoleń w zakresie ochrony powinny być przechowywane przez pracodawcę i udostępniane pracownikowi lub właściwej władzy, na ich wniosek. Dokumenty powinny być przechowywane przez pracodawcę przez okres ustalony przez właściwą władzę.” Nowy klucz C ✔.

### ADR-B-0413 – POPRAW (12-K04, A) – NOWY TEMAT (bliskie 0776; stary klucz dodawał warunek spoza przepisu)
- 1.10.1.2 (s. 110): „Towary niebezpieczne mogą być wydane do przewozu wyłącznie przewoźnikowi odpowiednio zidentyfikowanemu.”; 1.10.1.4 (s. 110): „Każdy członek załogi … powinien posiadać przy sobie dokument z fotografią potwierdzający jego tożsamość.” Nowy klucz A ✔ (dowód kierowcy ≠ identyfikacja przewoźnika). Do oceny specjalisty.

### ADR-B-0414 – POPRAW (12-K04, B) – NOWY TEMAT (duplikat 0120)
- 1.10.1.2 (s. 110) jw.; 1.10.1.1 (s. 110): „Wszystkie osoby uczestniczące w przewozie towarów niebezpiecznych powinny stosować się, odpowiednio do zakresu swoich obowiązków, do wymagań niniejszego działu dotyczących ochrony tych towarów.” Nowy klucz B (terminal identyfikuje kolejnego przewoźnika) ✔. Do oceny specjalisty (zastosowanie 1.10.1.2 do wydania w terminalu przeładunkowym – wykładnia).

### ADR-B-0415 – POPRAW (12-K02, A) – NOWY TEMAT (bliski duplikat 0701/0035/0775)
- 1.10.1.3 (s. 110): „Miejsca używane do czasowego przechowywania towarów niebezpiecznych podczas ich przewozu, znajdujące się w obrębie terminali, placów przeładunkowych, baz transportowych, placów postojowych i stacji rozrządowych powinny być odpowiednio chronione, dobrze oświetlone, a także — o ile jest to możliwe i wskazane — niedostępne dla osób postronnych.” Nowy klucz A ✔.

### ADR-B-0416 – POPRAW (12-K01, A) – NOWY TEMAT (duplikat 0067/0175/0519/0672)
- 1.10.1.4 (s. 110) jw. – przepis ogólny (1.10.1), niezależny od 1.10.3 (towary dużego ryzyka). Nowy klucz A ✔. Pytanie jest w **egzaminie 005** (questions).

### ADR-B-0417 – POPRAW (08-K01, C) – NOWY TEMAT (bliski duplikat 0071; fałszywa opcja B)
- 8.1.4.1 (s. **1324**, obraz): „Poniższa tabela określa minimalne wymagania dotyczące gaśnic przenośnych dla grup pożarów A, B i C. Wymagania te mają zastosowanie do jednostek transportowych, z wyjątkiem jednostek transportowych wymienionych w 8.1.4.2”; kolumna (1) „Dopuszczalna masa całkowita jednostki transportowej”; wiersz „> 7,5 tony”: 2 / 12 kg / 2 kg / 6 kg. 1.2.1 (s. 36): „Jednostka transportowa oznacza pojazd samochodowy bez przyczepy lub zespół pojazdów składający się z pojazdu samochodowego i dołączonej do niego przyczepy.” Nowy klucz C ✔.

### ADR-B-0418 – POPRAW (08-K01, A) – przeredagowane (forma)
- 8.1.4.1 (s. 1324, obraz), wiersz „> 3,5 tony ≤ 7,5 tony”: minimalna liczba gaśnic 2, łącznie 8 kg, silnik/kabina co najmniej jedna 2 kg, dodatkowa – co najmniej jedna 6 kg. Klucz A ✔.

### ADR-B-0419 – POPRAW (08-K01, B) – przeredagowane (granica 7,5 t jako ocena zestawu)
- 8.1.4.1 (s. 1324, obraz): „> 3,5 tony / ≤ 7,5 tony” – 7,5 t w środkowym wierszu ✔. Zestaw 2 kg + 6 kg: 2 gaśnice, 8 kg, 2 kg silnik/kabina, 6 kg dodatkowa – spełnia. Klucz B ✔.

### ADR-B-0420 – POPRAW (08-K01, C) – NOWY TEMAT (bliskie 0022; klucz jedyną najdłuższą)
- 8.1.4.1 (s. 1324, obraz), kolumna (5) „Wymaganie dotyczące dodatkowej gaśnicy (gaśnic). Co najmniej jedna gaśnica powinna mieć minimalną pojemność:” – „6 kg” dla > 7,5 t. Zestaw 2/2/4/4 kg = 12 kg bez gaśnicy 6 kg – nie spełnia. Klucz C ✔.

## Metryki po poprawkach (na kopii repo)

- „Poprawna = jedyna najdłuższa”: **33/780 = 4,23% → 32/780 = 4,10%** (0420 przestało być jedyną najdłuższą), maksimum działu **7,87%** bez zmian – linie w `docs/POKRYCIE-KURSU.md`, `podstawowy/README.md` i `review/specialist/PAKIET-ZAMKNIECIE-0780.md` **trzeba zmienić** na 32/780 = 4,10%.
- „Poprawna = jedyna najkrótsza”: **193 → 187/780**; ADR-B-12 35,4% → **22,9%** (11/48), ADR-B-08 30,2% bez zmian; maksimum działu 31,5%; wszystkie działy ≤ 38%.
- Wszystkie 15 wyjaśnień: 5 zdań, 379–471 znaków, maks. 26 słów w zdaniu, na końcu „Podstawa: ADR …”; opcje 57–74 znaki; bez słów absolutnych i średników w opcjach.

## Egzaminy, kolejki, snapshoty (pułapki CI)

- Egzaminy próbne – pytania z partii **w `questions`**: wariant-003/klucz-003: **0408**; wariant-005/klucz-005: **0416**. Na listach `excluded_question_ids` (NIE zmieniać): 004 – 0408; 005 – 0408. Warianty/klucze 001, 002, 004 – tylko SHA.
- `review/specialist/KOLEJKA-PRIORYTETOWA-4X40.json` i `4X44.json` **nie zawierają** ID z partii – tylko SHA.
- Snapshoty: `review/sequential/399-416.json` (0406–0416) i `417-436.json` (0417–0420) oraz `review/legal-clauses/399-416.json` i `417-436.json` (clause, answer_review A/B/C, notes_on_conditions ≥ 25 zn.).
- Ledger `review/legal-polish/stage4w4-literal-verification-ledger-0001-0609.json`: nowe `source_references` (zmieniają się dla 0406, 0407, 0408, 0409, 0410, 0413, 0414, 0417).
- Rejestry `REJESTR-AKTUALNY-0001-0765.md` i `-0001-0780.md`: po 15 wierszy.
- SHA banku 5e369822… występuje w **31 plikach**: **30 zamienianych wprost** (te same co w partii 27: docs/POKRYCIE-KURSU.md, docs/STAN-KONCOWY-…, podstawowy/README.md, review/README.md, podstawowy/raporty/etap-4x135-wykluczenia-proby.json, 9 plików review/specialist, 10 plików egzaminów, tests/test_literal_review_0301_0315 … 0391_0405 – w 0391_0405 to EXPECTED_BANK_SHA, FIRST_PASS 9475e2d4… zostaje) oraz **`tests/test_literal_review_0406_0420.py` osobno**: tam obie stałe mają dziś 5e369822…, więc ślepa zamiana „stary → nowy SHA” zepsułaby FIRST_PASS_BANK_SHA (manifest #885) – zmienić **tylko EXPECTED_BANK_SHA**, test `test_bank_blob_and_question_records_unchanged` przemianować na `test_bank_has_expected_sha_after_second_pass`.
- Oczekiwany SHA banku: **5e369822335dd871b6499fae080d6e689dc6377c → 025066373056366cfff08ee01a6a5394c7c90218**.
- `check_near_duplicates.py --threshold 0.60`: pierwsza wersja moich treści 0418/0420 miała podobne pytania (0,714) – przeredagowane; obecna wersja przechodzi.

## Test na kopii repo

`test_p28.sh` (kopia /tmp/b28 z main 396b22d41, bez commitów i pushu): `apply_poprawki.py` → „Changed (15): ADR-B-0406 … ADR-B-0420”, blob **025066373056366cfff08ee01a6a5394c7c90218**; po synchronizacji (`sync_p28_test.py`) wszystkie 14 skryptów CI = 0 i `python3 -m unittest discover -s tests` – **Ran 187 tests, OK** (linie „FAIL: --strict …” w logu to wyjście testów negatywnych – występują też na main).

## Licznik

Po wdrożeniu partii 28 (obie kontrole 0406–0420): **360 pytań bez porównania dosłownego po obu kontrolach** (0421–0780); kontrola pierwsza partii 29 (0421–0435): 360 → 345.

## Do zapamiętania na kolejne partie
- 0421–0435: 0421 (8.1.4.2 – gaśnica 2 kg przy 1.1.3.6) – porównać z 0073, 0197, 0282, 0711, 0760; 0422–0423 (8.1.4.4–8.1.4.5) – z 0015, 0074, 0169, 0176, 0232, 0283, 0585, 0704, 0717, 0749, 0759; 0424–0429 (7.5.2 – zakaz ładowania razem, tabela 7.5.2.1 i uwagi) – z 0025, 0199, 0291, 0324, 0491, 0492 (tabelę 7.5.2.1 czytać z obrazu PDF – s. 1305); 0430–0434 (tunele 8.6, 1.9.5) – z 0031–0033, 0063–0065, 0083–0086, 0174, 0207–0209, 0248, 0262–0264, 0322, 0487–0490, 0512, 0539, 0540, 0574–0576, 0591, 0602–0604, 0771, 0772; 0435 (5.4.3.4 – pożar ładowni w tunelu) – z 0107, 0143, 0166, 0210, 0614, 0641, 0742. Strony: 8.1.4.2–8.1.4.5 Dz.U. s. 1325, tabela 8.1.4.1 s. 1324, 7.5.2.1 s. 1305, 7.5.2.2 s. 1306, 8.6.3 s. 1338 (8.6.4 – sprawdzić nagłówek strony), 1.9.5.3.5 s. 109.
