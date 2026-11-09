# Kontrola druga – partia ADR-B-0346–0360 (porównanie dosłowne z polskim tekstem ADR 2025)

Data: 2026-11-09, ok. 14:45 (czas polski, CET).
Przedmiot: pierwsza kontrola ChatGPT (PR #876, scalony na main **ae5c8eeab**; `review/literal-pl/PARTIA-0346-0360.md` + `.json` + `tests/test_literal_review_0346_0360.py`, wynik 1 OK / 14 POPRAW / 0 BLOKUJ) oraz rekordy 0346–0360 na main ae5c8eeab (bank blob **d44c9548…**, 780 pytań).
Źródło: Dz.U. 2025 poz. 642 (skany PDF), OCR tesseract `-l pol`; strony wg nagłówka „Dziennik Ustaw — NNNN —”. Obrazem strony PDF sprawdzone: s. 976, 977 i 978 (tabela wskazówek dodatkowych we wzorze instrukcji pisemnych: nalepka 2.2 „Mogą powodować odmrożenia”, nalepka 5.1 „Nie dopuszczać do zmieszania z materiałami zapalnymi lub palnymi (np. trocinami)”, materiały o podwyższonej temperaturze „Unikać kontaktu z gorącymi częściami jednostki transportowej i z uwolnionym materiałem”; `kontrola2/p24-20-26-26.png`, `p24-20-27-27.png`, `p24-20-28-28.png`). Sprostowanie poz. 1575 nie dotyczy punktów tej partii.
Status: kontrola robocza. **Żadne pytanie nie jest oznaczone jako zweryfikowane**; wszystkie pozostają `needs_review`.

## Podsumowanie

- Werdykty kontroli drugiej: **OK 0, POPRAW 15, BLOKUJ 0**.
- **11 pytań to duplikaty** (0347, 0348, 0349, 0350, 0353, 0354, 0355, 0356, 0357, 0359, 0360) → **nowy temat z tej samej kompetencji**. **4 pytania** (0346, 0351, 0352, 0358) mają właściwy, niepowtórzony podtemat, ale wady formy → przeredagowane w tym samym podtemacie. Wszędzie ta sama litera klucza, ten sam `module_id` (ADR-B-04), `image` = null; liczebność kompetencji bez zmian (04-K01 = 6, 04-K02 = 6, 04-K03 = 6, 04-K04 = 6, 04-K05 = 11, 04-K06 = 15; każda kompetencja teoretyczna ≥ 6).
- **Wady formy starych wersji** (sprawdzone automatycznie): opcje > 80 zn. – 0349 A (89), 0353 A (93) i C (90), 0354 B (83) i C (104), 0355 B (83) i C (94), 0358 C (91); klucz jedyną najkrótszą – 0346 (44), 0351 (27), 0352 (34), 0353 (54), 0354 (80), 0355 (47), 0357 (38); słowa absolutne – 0350 B „tylko”, C „wszystkich”, 0351 A „tylko”, 0352 B „każdym”, C „tylko”, 0353 A „tylko”, 0360 A „wyłącznie”; średnik w 0354 **A** (nie w C, jak podaje #876); absurdalne dystraktory – 0346 („cena przewozu”, „własna cysterna”), 0358 A („dla zasilania kabiny”), 0359 C („Otworzyć sztuki przesyłek”, 25 zn.).
- **Błędy / różnice względem raportu ChatGPT (#876):**
  - **zawyżone OK – 0356**: skażona odzież to dokładnie ten sam temat co **0110, 0167, 0687, 0707, 0745** (i bliskie 0643) – duplikat, zastąpiony;
  - **0353** – #876 pisze „podtemat odrębny od 0738”, ale lampa z 8.3.4 (iskra krzesana) jest już w **0663 i 0762** – duplikat, zastąpiony (S2(1));
  - **0355** – dubluje nie tylko 0130/0354, lecz całą rodzinę „strona nawietrzna”: **0178, 0183, 0221, 0230, 0692, 0741**; **0354** – „nie wchodzić w rozlew”: 0130, **0113, 0642, 0735**;
  - **0350** – „tylko” jest w opcji **B**, a w C jest „wszystkich” (#876 podaje „A zawiera tylko”); 0354 – średnik w A, nie w C;
  - **0358** – #876: „uzupełnia 0244”; to prawda (lustrzany przypadek obu warunków 8.3.6), więc temat zostaje, ale z nowymi opcjami (C 91 zn., A bez sensu);
  - **0351/0352** – #876 łączy 0352 z rodziną klinów 8.1.5.2 (0023, 0056, 0509, 0699, 0761); tamte pytania dotyczą **wyposażenia** (posiadanie i rozmiar klina), a 8.3.7 – **unieruchomienia przyczepy bez układu hamulcowego** na postoju → nie duplikat, przeredagowane; 0351 (hamulec postojowy) nie ma odpowiednika w banku (0104/0182/0690 to „zahamować pojazd” po wypadku z 5.4.3.4);
  - strony w #876 **poprawne** (8.3.x – s. 1332; 8.4.1 – s. 1333; wzór instrukcji – s. 975), licznik 435 → 420 poprawny; test `tests/test_literal_review_0346_0360.py` tym razem jest (dobrze) – przy wdrożeniu trzeba w nim zmienić oczekiwany SHA.
- Egzaminy próbne: w wariantach są **0348 (001), 0355 i 0357 (003), 0359 (005)** – trzeba odświeżyć stem/options w wariant-00N i explanation/legal_basis w klucz-00N (litery kluczy bez zmian). Warianty/klucze 002 i 004 – tylko SHA.
- `review/specialist/KOLEJKA-PRIORYTETOWA-4X40.json` i `-4X44.json` **nie zawierają** ID 0346–0360 (tylko SHA do podmiany).
- Ledger `review/legal-polish/stage4w4-literal-verification-ledger-0001-0609.json`: nowe `source_references` dla 11 ID – 0346, 0347, 0348, 0349, 0350, 0353, 0354, 0355, 0356, 0357, 0360 (0351, 0352, 0358, 0359 mają niezmienione referencje).
- Wskaźnik „poprawna = jedyna najdłuższa”: **35/780 = 4,49% bez zmian**, maks. działu **7,87%** bez zmian. „Poprawna = jedyna najkrótsza”: ADR-B-04 24,0% → **10,0%**, maks. działu 37,0% (ADR-B-07, bez zmian); wszystkie działy ≤ 38%.
- Oczekiwany SHA banku po wdrożeniu: **d44c95488d28507ffc3fa901d14b7d20cdd9fb38 → 129d09039ee7fbee90198049cb3d733368070c77**.
- Plik poprawek: `kontrola2/POPRAWKI-KONTROLA2-0346-0360.jsonl` – **15 pełnych linii**. Generator: `kontrola2/build_p24.py` + `common_k2.py`.

## Test na kopii repo

Skrypt `kontrola2/test_p24.sh`: kopia `/tmp/b24` z main ae5c8eeab → plik poprawek do `review/literal-pl/` → wpis w `tools/apply_poprawki.py` (SOURCES, po 0331-0345) → `apply_poprawki.py` („Changed (15): ADR-B-0346 … ADR-B-0360”) → synchronizacja pomocnicza `kontrola2/sync_p24_test.py` (snapshoty sequential/legal-clauses 345-362.json, ledger, egzaminy 001/003/005, SHA w 27 plikach, rejestry 0765/0780 po 15 wierszy) → 14 skryptów CI: **wszystkie 0** (validate, coverage, check_mock_exam_variants, answer_leakage_metrics, answer_length_bias --threshold 0.16 --strict, check_explanation_quality --minimum 300, check_near_duplicates --threshold 0.60, check_cross_module_duplicates --threshold 0.80, similarity --threshold 0.45, check_explanation_heuristics, release_gate --report, check_sequential_audit, check_legal_clause_review, course_consistency); **unittest 178/178 OK**. Wcześniejsza wersja 0350 (próg S14 „20 kg”) padła na check_near_duplicates (0,750 z 0345) – dlatego 0350 dostało inny temat (dział 8.4 w limicie 1.1.3.6).

## Zmiany (jedna linia na pytanie; klucz / kompetencja / punkt / s. Dz.U.)

- 0346 (04-K06, B) – przeredagowane: personel parkingu z 8.4.1 (a) musi znać właściwości ładunku i miejsce pobytu kierowcy (8.4.1 (a) / 1333);
- 0347 (04-K06, B) – NOWE: S15 – nadzór z 8.4 przy jakiejkolwiek ilości, ale nie przy przedziale ładunkowym zamkniętym przed osobami nieuprawnionymi (S15 / 1336);
- 0348 (04-K06, A) – NOWE: S9 – dłuższy postój przy miejscach zamieszkałych tylko za zgodą właściwych władz (S9 / 1336);
- 0349 (04-K06, B) – NOWE: S10 – kwiecień–październik, ochrona przed słońcem, opończa ≥ 20 cm nad ładunkiem (S10 / 1336);
- 0350 (04-K06, A) – NOWE: dział 8.4 obowiązuje także w limicie 1.1.3.6 (1.1.3.6.2 / 26; 8.4.1 / 1333; S14–S24 / 1336–1337);
- 0351 (04-K06, B) – przeredagowane: bieg na płaskim terenie nie zastępuje hamulca postojowego (8.3.7 / 1332);
- 0352 (04-K06, A) – przeredagowane: przyczepa bez układu hamulcowego – co najmniej jeden klin pod koło (8.3.7 / 1332; 8.1.5.2);
- 0353 (04-K04, B) – NOWE: S2(1) – do zamkniętego przedziału z cieczą zapalną (tz ≤ 60 °C) tylko oświetlenie niezdolne zapalić par i gazów (S2(1) / 1335);
- 0354 (04-K05, A) – NOWE: nalepka 5.1 – nie dopuszczać do zmieszania z trocinami i innymi materiałami palnymi (5.4.3.4 / 977);
- 0355 (04-K05, A) – NOWE: nalepka 2.2 – zagrożenie odmrożeniem, nie dotykać oszronionego zaworu ani gazu (5.4.3.4 / 975–976);
- 0356 (04-K05, B) – NOWE: materiały o podwyższonej temperaturze – unikać kontaktu z gorącymi częściami jednostki i uwolnionym materiałem (5.4.3.4 / 978; 5.3.3 / 959);
- 0357 (04-K02, A) – NOWE: zakaz otwierania z 8.3.3 obowiązuje także w limicie 1.1.3.6 (1.1.3.6.2 / 26; 8.3.3 / 1332);
- 0358 (04-K03, B) – przeredagowane: żuraw napędzany od silnika + zgoda przepisów państwa pobytu → silnik może pracować (8.3.6 / 1332);
- 0359 (04-K03, B) – NOWE: decydują przepisy państwa, na którego terytorium jest pojazd, a nie kraj rejestracji (8.3.6 / 1332);
- 0360 (04-K01, B) – NOWE: S1(3) – przy klasie 1 zakaz palenia obejmuje pojazd i jego pobliże także poza czynnościami ładunkowymi, również e-papierosy (S1(3) / 1334; 8.3.5 / 1332).

## Cytaty i uzasadnienia

### ADR-B-0346 – przeredagowane (8.4.1 (a))
- 8.4.1 (s. 1333): „(a) na parkingu samochodowym nadzorowanym przez personel, który został poinformowany o właściwościach ładunku i miejscu pobytu kierowcy;”. Temat sprawdzany tylko tu (0181 wymienia ten parking w treści, ale pyta o (b) przed (c); 0144 – pierwsza kolejność). Klucz B ✔.

### ADR-B-0347 – nowy temat (S15)
- Stara wersja ((a) przed (b)) = **0144** i **0181** (cała kolejność 8.4.1).
- S15 (s. 1336): „Przepisy działu 8.4 dotyczące nadzorowania pojazdów mają zastosowanie do pojazdów przewożących jakąkolwiek ilość tych materiałów. Jednakże, przepisy działu 8.4 nie muszą być stosowane w przypadku, gdy przedział ładunkowy jest zamknięty w sposób uniemożliwiający dostęp osobom nieuprawnionym lub przewożone sztuki przesyłek są zabezpieczone w inny sposób przed nieuprawnionym rozładunkiem.” Klucz B ✔. Nie powtarza progu 500 kg z 0345 (S16) – próg jest tu dystraktorem C.

### ADR-B-0348 – nowy temat (S9)
- Stara wersja (miejsce z lit. (c)) = **0181**, 0349.
- S9 (s. 1336): „Podczas przewozu tych materiałów postoje na potrzeby służbowe, w miarę możliwości, nie powinny odbywać się w pobliżu miejsc zamieszkałych lub uczęszczanych przez ludzi. Dłuższy postój w pobliżu takich miejsc jest dozwolony wyłącznie za zgodą właściwych władz.” Klucz A ✔. W banku brak pytań o S8/S9.

### ADR-B-0349 – nowy temat (S10)
- Stara wersja (lit. (c)) = **0181**, 0348.
- S10 (s. 1336): „Jeżeli wymagają tego przepisy krajowe, to w okresie od kwietnia do października, w czasie postoju pojazdu, sztuki przesyłek powinny być skutecznie chronione przed działaniem słońca, np. za pomocą opończy umieszczonej co najmniej 20 cm ponad ładunkiem.” Klucz B ✔ (treść zakłada, że przepisy krajowe wymagają S10). W banku brak pytań o S10.

### ADR-B-0350 – nowy temat (1.1.3.6.2 + dział 8.4)
- Stara wersja („jak sprawdzić, czy przewóz podlega nadzorowi”) = **0131** (i 0580).
- 1.1.3.6.2 (s. 26): „… bez stosowania następujących przepisów: … części 8, z wyjątkiem: 8.1.2.1 (a), 8.1.4.2 do 8.1.4.5, 8.2.3, 8.3.3, 8.3.4, 8.3.5, działu 8.4, S1(3) i (6), S2(1), S4, S5, S14 do S21 oraz S24 z działu 8.5; …”; 8.4.1 (s. 1333). Klucz A ✔. Dział 5.3 (tablice) jest wyłączony – stąd dystraktor B. Rodzina 1.1.3.6 w banku: 0279 (8.3.5), 0761 (8.1.5.2), 0762 (8.3.4) – dział 8.4 dotąd nieobjęty. Pierwsza wersja z S14 („20 kg”) padła na check_near_duplicates (0,750 z 0345) i została odrzucona.

### ADR-B-0351 – przeredagowane (8.3.7, hamulec postojowy)
- 8.3.7 (s. 1332): „Pojazdy z towarami niebezpiecznymi nie mogą być pozostawione na postoju, jeżeli nie zostały zabezpieczone hamulcami postojowymi.” Klucz B ✔.

### ADR-B-0352 – przeredagowane (8.3.7, przyczepa bez hamulców)
- 8.3.7 (s. 1332): „Przyczepy bez układu hamulcowego powinny być unieruchomione przy użyciu co najmniej jednego klina do podkładania pod koła, zgodnie z 8.1.5.2.” Klucz A ✔. Różni się od 0023/0056/0509/0699/0761 (wyposażenie z 8.1.5.2).

### ADR-B-0353 – nowy temat (S2(1))
- Stara wersja (8.3.4, iskra krzesana) = **0663**, **0762**.
- S2(1) (s. 1335): „Zabrania się wchodzenia do przedziału ładunkowego pojazdów zamkniętych, przewożących materiały ciekłe o temperaturze zapłonu nie wyższej niż 60 °C, albo materiały lub przedmioty z materiałami palnymi klasy 2, z przenośnymi urządzeniami oświetleniowymi, innymi niż zaprojektowane i wykonane w sposób uniemożliwiający zapalenie się palnych par i gazów, które mogą rozprzestrzeniać się wewnątrz pojazdu.” Klucz B ✔.

### ADR-B-0354 – nowy temat (nalepka 5.1, trociny)
- Stara wersja („nie wchodzić w rozlew”) = **0130**, 0113, 0642, 0735.
- Wzór instrukcji pisemnych, wskazówki dodatkowe (s. 977, obraz strony): nalepka 5.1 – „Zagrożenie gwałtowną reakcją, pożarem i wybuchem w przypadku kontaktu z materiałami palnymi.” / „Nie dopuszczać do zmieszania z materiałami zapalnymi lub palnymi (np. trocinami).” Klucz A ✔. W banku brak pytań o tę wskazówkę (0666 – inny scenariusz: 5.1 nasila pożar kartonu).

### ADR-B-0355 – nowy temat (nalepka 2.2, odmrożenia)
- Stara wersja (strona nawietrzna) = **0178, 0183, 0221, 0230, 0692, 0741**, 0354.
- s. 975: „Nie wchodzić na uwolnione materiały, nie dotykać ich …”; s. 976 (obraz strony), nalepka 2.2: „Zagrożenie działaniem duszącym. Mogą znajdować się pod ciśnieniem. Mogą powodować odmrożenia. Zagrożenie wybuchem w przypadku ogrzania.” / „Schronić się. Unikać zagłębień terenu.” Klucz A ✔. W banku brak pytań o odmrożenia (0284 – działanie duszące 2.2).

### ADR-B-0356 – nowy temat (materiały o podwyższonej temperaturze)
- Stara wersja (skażona odzież; OK w #876) = **0110, 0167, 0687, 0707, 0745**.
- s. 978 (obraz strony): „Materiały o podwyższonej temperaturze” – „Zagrożenie poparzeniem” / „Unikać kontaktu z gorącymi częściami jednostki transportowej i z uwolnionym materiałem.”; znak – 5.3.3 (s. 959). Klucz B ✔. Temat nie dotyczy cystern (treść mówi o jednostce transportowej).

### ADR-B-0357 – nowy temat (8.3.3 w limicie 1.1.3.6)
- Stara wersja (zakaz otwierania) = **0011, 0048, 0243, 0678, 0737**.
- 1.1.3.6.2 (s. 26) – cytat jak przy 0350 (wśród wyjątków „8.3.3”); 8.3.3 (s. 1332): „Zabrania się kierowcy i jego pomocnikowi otwierania sztuk przesyłek zawierających towary niebezpieczne.” Klucz A ✔. Treść celowo inna niż 0279 (similarity: brak pary powyżej progu).

### ADR-B-0358 – przeredagowane (8.3.6, wyjątek spełniony)
- 8.3.6 (s. 1332): „Silnik pojazdu nie powinien pracować podczas załadunku i rozładunku, z wyjątkiem przypadków, gdy uruchomienie silnika jest niezbędne dla pracy pomp lub innych urządzeń zapewniających załadunek lub rozładunek pojazdu oraz gdy zezwalają na to przepisy państwa, na którego terytorium znajduje się pojazd.” Klucz B ✔ (oba warunki spełnione; lustrzany przypadek 0244, gdzie brak zgody państwa).

### ADR-B-0359 – nowy temat (8.3.6, które państwo)
- Stara wersja (silnik dla klimatyzacji → wyłączyć) = **0012, 0047, 0515** (ogrzewanie kabiny).
- 8.3.6 (s. 1332) – cytat jak przy 0358: „… przepisy państwa, na którego terytorium znajduje się pojazd.” Klucz B ✔.

### ADR-B-0360 – nowy temat (S1(3), klasa 1)
- Stara wersja (palenie przy pojeździe podczas przeładunku) = **0736**, 0010, 0103, 0279, 0280.
- S1(3) (s. 1334): „Zabrania się palenia, używania ognia lub nieosłoniętego płomienia w pojazdach przewożących materiały lub przedmioty klasy 1, w ich pobliżu, a także podczas załadunku i rozładunku tych materiałów lub przedmiotów. Niniejszy zakaz palenia ma również zastosowanie do używania papierosów elektronicznych i podobnych urządzeń.”; 8.3.5 (s. 1332): „W czasie manipulowania ładunkiem zabronione jest palenie …”. Klucz B ✔.

## Do zapamiętania na kolejne partie
- 0361 (5.4.3.4, „nie włączać urządzeń elektrycznych”) ≈ 0102, 0738 oraz (po tej partii) brak kolizji z 0353; 0362 – opcja A „Tylko prywatne wiadomości” (słowo absolutne, dystraktor absurdalny), temat dokumentów dla ratowników ≈ 0630, 0735; 0372 → 1.4.3.7.1 (e)/(f) – sprawdzić literę; 0632 dubluje starą wersję 0297 (partia 43).