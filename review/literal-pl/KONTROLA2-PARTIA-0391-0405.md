# Kontrola druga – partia ADR-B-0391–0405 (porównanie dosłowne z polskim tekstem ADR 2025)

Data: 2026-11-09, ok. 17:15 (czas polski, CET).
Przedmiot: pierwsza kontrola ChatGPT (PR #883, scalony na main **287fe23de**; `review/literal-pl/PARTIA-0391-0405.md` + `.json` + `tests/test_literal_review_0391_0405.py`, wynik 0 OK / 15 POPRAW / 0 BLOKUJ) oraz rekordy 0391–0405 na main 287fe23de (bank blob **9475e2d4…**, 780 pytań).
Źródło: Dz.U. 2025 poz. 642 (skany PDF), OCR tesseract `-l pol`; strony wg nagłówka „Dziennik Ustaw — NNN —”. Sprostowanie poz. 1575 nie dotyczy punktów tej partii.
Status: kontrola robocza. **Żadne pytanie nie jest oznaczone jako zweryfikowane**; wszystkie pozostają `needs_review`.

## Podsumowanie

- Werdykty kontroli drugiej: **OK 0, POPRAW 15, BLOKUJ 0** (zgodnie z #883 co do liczby, ale z innymi ustaleniami – niżej).
- **3 pytania to duplikaty** (0395, 0396, 0398) → **nowy temat z tej samej kompetencji, niecysternowy**. **12 pytań** (0391–0394, 0397, 0399–0405) ma właściwy podtemat, ale wady formy/treści → przeredagowane w tym samym podtemacie. Wszędzie ta sama litera klucza, ten sam `module_id`, `image` = null; przypisania w `kompetencje.json` bez zmian (10-K01 = 11, 10-K02 = 6, 10-K03 = 10, 10-K05 = 19, 12-K05 = 17; każda kompetencja teoretyczna ≥ 6).
- **Tematy cysternowe**: żaden zamiennik nie jest cysternowy. 0394 (UWAGA: certyfikat pakowania nie jest wymagany dla cystern przenośnych) zostaje jako pytanie, tylko poprawiona forma – wątku nie rozszerzam.
- **Wady formy starych wersji**: opcje > 80 zn. – 0392 A/B/C (83/81/82), 0393 A (82), 0394 B (81), 0395 A/B/C (83/87/99), 0397 A (83) i C (86), 0398 A/B/C (92/105/108), 0399 B (96), 0400 B (85) i C (100), 0401 B (87), 0402 B (102) i C (89), 0403 C (87), 0404 C (94), 0405 B (101) i C (84); klucz jedyną najkrótszą – 0391, 0392, 0395, 0396; klucz jedyną najdłuższą – 0403; średniki – 0392 A/C, 0394 A/B/C, 0396 A/B/C; słowa absolutne w opcjach – 0392 A „zawsze”, 0394 B „każdej”, C „tylko”, 0396 A „zawsze”, C „automatycznie”, 0397 B „Każdy … całkowicie”, 0400 C „wszystkie”, 0404 C „niezależnie”, 0405 B (brak kontroli – poprawione); opcje-polecenia przy pytaniu „co/jakie” – 0395, 0398 A/C, 0399 A/C, 0400 A/B, 0401–0405; terminologia – 0391–0394 mówią „świadectwo pakowania”, a ADR używa „certyfikat pakowania kontenera/pojazdu”; wyjaśnienie 0393 zawiera „odpowiedź B”.

## Błędy / różnice względem raportu ChatGPT (#883)

1. **0393 – przeoczony błąd merytoryczny klucza.** Klucz B „Może być dołączone do dokumentu przewozowego, jeśli spełniono wymagania ADR”, a wyjaśnienie wprost: „odpowiedź B opisuje możliwość, a nie obowiązek”. 5.4.2 akapit trzeci (s. 973): „to do dokumentu przewozowego **powinien być również dołączony** certyfikat pakowania kontenera/pojazdu” – to obowiązek. #883 ocenił klucz jako prawidłowy i wskazał tylko długość opcji A.
2. **Strony Dz.U. dla 1.10.3.2.2 (0399–0405) błędne**: #883 podaje s. 96 i 97 – to numery stron wewnętrznych ADR w stopce („96”, „97”), a nie Dz.U. Cały 1.10.3.2.2 (a)–(h) stoi na **Dz.U. s. 113** (nagłówek „Dziennik Ustaw — 113 — Poz. 642”). Dz.U. s. 96–97 to 1.8.7. Także 1.1.4.2.3 (0398) jest na **s. 30**, nie 29.
3. **0405 – klucz opisywał lit. (h), nie (g)**: „ochrony informacji transportowych przed dostępem osób nieuprawnionych” to treść (h) (= temat 0406). #883 sam zauważył różnicę (g)/(h), ale nie zauważył, że klucz 0405 jej nie zachowuje. Przeredagowane: (g) = ochrona fizyczna informacji z planu.
4. **Propozycja zastępcza dla 0398 wadliwa**: (a) **litera klucza A**, a 0398 ma klucz **B** – litery nie wolno zmieniać; (b) źródło „ADR 2025, 5.4.2.3” – takiego punktu ADR nie ma (to IMDG 5.4.2.3 przytoczony w przypisie 6 do 5.4.2); (c) temat (EDI, nazwiska wielkimi literami) bardzo bliski **0278** (IMDG 5.4.2.4 – EDI, „Oryginał otrzymano drogą elektroniczną” i nazwisko wielkimi literami); (d) opcja B „Wyłącznie…” (słowo absolutne). Użyłem innego tematu: IMDG 5.4.2.1 pkt .9.
5. **Brak propozycji zastępczych dla 0395 i 0396** – #883 napisał, że „nie wskazuje pozornego zamiennika”/„brak bezpiecznego zamiennika”. Zamienniki istnieją (niżej) – 10-K02: zapis z 5.4.1.1.7 przy kontenerze z dużymi nalepkami IMDG (1.1.4.2.1 (c)); 10-K05: kontener do przewozu luzem w 1.1.4.2.1 (c).
6. **Test `tests/test_literal_review_0391_0405.py` znowu ma jedną stałą** `EXPECTED_BANK_SHA` (polecenie wymagało od razu FIRST_PASS_BANK_SHA + EXPECTED_BANK_SHA) – przy wdrożeniu trzeba go rozdzielić, inaczej pada `test_report_scope_and_verdicts`.
7. Słusznie w #883: duplikaty 0395 = 0061 (i rodzina), 0396 = 0028/0029/0389, 0398 = 0030; 0391–0394 nie są duplikatami 0140/0204/0278/0388/0390 (różne aspekty 5.4.2 – zgadzam się; uwaga: wyjaśnienia 0140 i 0204 wspominają, kto dostarcza certyfikat, a 0140 – że można połączyć dokumenty, ale żadne z tych pytań tego nie sprawdza); 0399–0405 to różne litery (a)–(g); strony 973 (5.4.2), 965 (5.4.1.1.7), 29 (1.1.4.2.1) – poprawne; licznik 390 → 375 poprawny.

## Duplikaty – sprawdzenie w całym banku (780) i między sobą

- **0395** (stara: jaki zapis przy 1.1.4.2.1) = **0061** (ten sam klucz „PRZEWÓZ ZGODNY Z 1.1.4.2.1”), też 0089, 0277, 0708. Nowy temat: zapis potrzebny także, gdy sztuki przesyłek mają oznakowanie ADR, a odstępstwo dotyczy jedynie dużych nalepek IMDG na kontenerze (lit. (c)). Sprawdzone z 0203 (pełne ADR, brak odstępstwa → brak zapisu), 0287 (pakowanie razem, lit. (b) → zapis), 0215, 0714, 0770, 0779 – inny wyzwalacz, nie duplikat. Wpis „MARINE POLLUTANT” (5.4.1.1.18) odrzucony jako zamiennik – to już 0467.
- **0396** (stara: przejazd do portu nie zwalnia z ADR) = **0028/0029/0389**. Nowy temat: lit. (c) obejmuje kontenery do przewozu luzem (towar stały) – niecysternowy; sprawdzone z 0062, 0142, 0206, 0384, 0385 (inne aspekty lit. (c)). Rodzina 1.1.4.3 (0444–0446), 1.1.4.5 (0437–0443) i DOT (0321, 0386, 0447–0454) jest zajęta – nie dokładam tam pytań.
- **0398** (stara: 1.1.4.2.3 – dokument IMDG zamiast ADR) = **0030**. Nowy temat: IMDG 5.4.2.1 pkt .9 (przypis 6 do 5.4.2) – przed podpisaniem certyfikatu musi być dokument przewozowy na każdą przesyłkę. Różny od 0388 (pkt .1 – czysty, suchy kontener), 0390 (pkt .4 – bębny pionowo), 0278 (5.4.2.4 – EDI) i 0391–0394.
- **0391–0394 między sobą i z 0140/0204/0278/0388/0390**: kto dostarcza (0391), jeden dokument (0392), pojazd – obowiązek dołączenia (0393), cysterny przenośne – wyjątek (0394), kiedy wymagany (0140), brak wymogu po rejsie (0204), EDI (0278), treść certyfikatu (0388, 0390, nowe 0398) – bez duplikatów.
- **0397** (ICAO, oznakowanie sztuk przesyłek, 1.1.4.2.1 (a)) – najbliżej 0119/0511 (to samo dla IMDG) oraz 0277/0383 (ICAO po wylądowaniu: zapis w dokumencie / definicja). Przeredagowane na przewóz drogowy **na lotnisko przed lotem** – jedyne pytanie o uznanie oznakowania ICAO; nie duplikat, ale blisko rodziny – do oceny specjalisty.
- **0399–0405** – litery (a)–(g) 1.10.3.2.2; sprawdzone z 0122 (czy plan jest potrzebny), 0212 (nadawca też ma plan), 0406 (lit. (h)), 0410 (szkolenie), 0582 (środki podczas postoju). 0401 przeredagowane tak, by objąć przechowywanie przed/podczas/po przewozie (nie tylko postoje – odróżnienie od 0582); 0402 – elementy lit. (d) (szkolenie, procedury, działania praktyczne, wyposażenie); 0405 – lit. (g), nie (h).
- Nowe teksty przeszły `check_near_duplicates.py --threshold 0.60`, `check_cross_module_duplicates.py --threshold 0.80` i `similarity.py --threshold 0.45` na kopii repo.

## Pytania – cytaty i ustalenia

### ADR-B-0391 – przeredagowane (5.4.2 akapit 1 – kto dostarcza certyfikat), klucz B
- 5.4.2 (s. 973): „Jeżeli przewóz towarów niebezpiecznych znajdujących się w kontenerze dokonywany jest bezpośrednio przed przewozem morskim, certyfikat pakowania kontenera/pojazdu zgodny z przepisami rozdziału 5.4.2 Kodeksu IMDG, powinien być dostarczony przewoźnikowi morskiemu przez odpowiedzialnych za pakowanie kontenera.” Klucz B ✔. Poprawione: „świadectwo” → „certyfikat”, klucz nie jest już jedyną najkrótszą, usunięte „automatycznie”/„tylko” z wyjaśnienia.

### ADR-B-0392 – przeredagowane (5.4.2 akapit 2 – jeden dokument), klucz B
- 5.4.2 (s. 973): „Funkcje dokumentu przewozowego wymaganego w 5.4.1 i certyfikatu pakowania kontenera / pojazdu, o którym mowa powyżej, może pełnić jeden dokument (patrz przykład w 5.4.5). Jeżeli wymienione funkcje pełni jeden dokument, to uważa się za wystarczające zamieszczenie w nim stwierdzenia, że załadunek kontenera odbył się zgodnie z odpowiednimi przepisami, właściwymi dla danego rodzaju transportu, oraz danych umożliwiających identyfikację osoby odpowiedzialnej za sporządzenie certyfikatu pakowania kontenera/pojazdu.” Klucz B ✔.

### ADR-B-0393 – przeredagowane, **poprawiony sens klucza** (5.4.2 akapit 3 – pojazd), klucz B
- 5.4.2 (s. 973): „Jeżeli przewóz drogowy towarów niebezpiecznych znajdujących się w pojeździe dokonywany jest bezpośrednio przed przewozem morskim, to do dokumentu przewozowego powinien być również dołączony certyfikat pakowania kontenera/pojazdu zgodny z przepisami rozdziału 5.4.2 Kodeksu IMDG.” Nowy klucz B „Trzeba go dołączyć do dokumentu przewozowego” ✔ (stary „Może być dołączone…” + wyjaśnienie „możliwość, a nie obowiązek” – sprzeczne z „powinien być”).

### ADR-B-0394 – przeredagowane (UWAGA w przypisie 6 do 5.4.2), klucz A
- 5.4.2 (s. 973), przypis 6 (IMDG 5.4.2.1): „UWAGA: Certyfikat pakowania kontenera/pojazdu nie jest wymagany dla cystern przenośnych.” Klucz A ✔. Usunięte średniki i słowa absolutne; wątek cysternowy nierozszerzany.

### ADR-B-0395 – nowy temat (zapis z 5.4.1.1.7 przy lit. (c)), klucz A
- 5.4.1.1.7 (s. 965): „W przypadku przewozu zgodnie z 1.1.4.2.1, w dokumencie przewozowym powinien być zamieszczony dodatkowo następujący zapis: „PRZEWÓZ ZGODNY Z 1.1.4.2.1”.” 1.1.4.2.1 (s. 29): „Sztuki przesyłek, kontenery, cysterny przenośne, kontenery-cysterny i MEGC, które nie spełniają wymagań ADR dotyczących … stosowania nalepek ostrzegawczych, ale są zgodne z wymaganiami Kodeksu IMDG …”; (c) (s. 29–30): „jeżeli kontenery … nie są oznakowane i zaopatrzone w duże nalepki ostrzegawcze zgodnie z działem 5.3 niniejszego załącznika, to powinny być one oznakowane i zaopatrzone w duże nalepki ostrzegawcze zgodnie z działem 5.3 Kodeksu IMDG.” Klucz A ✔ (wniosek: kontener korzysta z 1.1.4.2.1 → zapis wymagany – do oceny specjalisty).

### ADR-B-0396 – nowy temat (lit. (c) – kontener do przewozu luzem), klucz B
- 1.1.4.2.1 (c) (s. 29): „w przypadku przewozu w łańcuchu transportowym zawierającym przewóz morski, jeżeli kontenery, kontenery do przewozu luzem, cysterny przenośne lub kontenery-cysterny i MEGC nie są oznakowane …” – dalej s. 30: „W takim przypadku, w odniesieniu do oznakowania pojazdu, mają zastosowanie jedynie przepisy podane w 5.3.2.1.1”. Klucz B ✔.

### ADR-B-0397 – przeredagowane (1.1.4.2.1 (a), ICAO przed lotem), klucz A
- 1.1.4.2.1 (a) (s. 29): „jeżeli sztuki przesyłek nie są oznakowane znakami i nalepkami ostrzegawczymi zgodnie z ADR, to powinny być oznakowane znakami i nalepkami ostrzegawczymi zgodnie z wymaganiami Kodeksu IMDG lub Instrukcji Technicznych ICAO;” + zdanie wprowadzające „w łańcuchu transportowym zawierającym przewóz morski lub lotniczy”; 5.4.1.1.7 (s. 965). Klucz A ✔.

### ADR-B-0398 – nowy temat (IMDG 5.4.2.1 pkt .9 – dokument na każdą przesyłkę), klucz B
- 5.4.2 (s. 973), przypis 6: „.9 Na każdą przesyłkę z towarami niebezpiecznymi załadowaną do kontenera/pojazdu otrzymano dokument przewozowy towarów niebezpiecznych, zgodnie z rozdziałem 5.4.1 (Kodeksu IMDG).” Klucz B ✔. Stara wersja (1.1.4.2.3, s. 30) = 0030.

### ADR-B-0399 … 0405 – przeredagowane (1.10.3.2.2 (a)–(g), **Dz.U. s. 113**)
- (a) „szczegółowy podział obowiązków w zakresie ochrony wraz ze wskazaniem kompetentnych i wykwalifikowanych osób, które posiadają odpowiednie uprawnienia do ich wykonywania;” – 0399 klucz C ✔.
- (b) „wykaz towarów niebezpiecznych podlegających ochronie lub wykaz rodzajów towarów niebezpiecznych podlegających ochronie;” – 0400 klucz B ✔.
- (c) „opis wykonywanych czynności i ocenę związanych z nimi zagrożeń, z uwzględnieniem postojów niezbędnych do wykonania operacji transportowych, przechowywania towarów niebezpiecznych — przed, podczas i po przewozie — w pojeździe, w cysternie lub w kontenerze, a także czasowego przechowywania towarów niebezpiecznych związanego ze zmianą rodzaju transportu lub środka transportu;” – 0401 klucz C ✔.
- (d) „szczegółowy wykaz przedsięwzięć … obejmujący: szkolenie; procedury postępowania (np. reagowanie w stanach podwyższonego zagrożenia, kontrola pracowników nowoprzyjętych i zmieniających stanowiska); działania praktyczne (np. wybór i korzystanie ze znanych tras przewozu …); wyposażenie i inne środki …” – 0402 klucz C ✔.
- (e) „skuteczne i aktualne procedury powiadamiania i postępowania w przypadkach zagrożeń, nieprzestrzegania zasad bezpieczeństwa i związanych z nimi zdarzeń;” – 0403 klucz C ✔ (nie jest już jedyną najdłuższą).
- (f) „procedury oceny i testowania planów ochrony oraz procedury przeglądów okresowych i aktualizacji tych planów;” – 0404 klucz B ✔.
- (g) „działania zapewniające ochronę fizyczną informacji o transporcie zawartych w planie ochrony;” – 0405 klucz C ✔ ((h) – ograniczenie dostępu do osób upoważnionych – to 0406).

## Metryki po poprawkach (na kopii repo)

- „Poprawna = jedyna najdłuższa”: **34/780 = 4,36% → 33/780 = 4,23%** (0403 przestało być jedyną najdłuższą), maksimum działu **7,87%** bez zmian – linie w `docs/POKRYCIE-KURSU.md`, `podstawowy/README.md` i `review/specialist/PAKIET-ZAMKNIECIE-0780.md` **trzeba zmienić** na 33/780 = 4,23%.
- „Poprawna = jedyna najkrótsza”: **197 → 193/780**; ADR-B-10 28,1% → **21,1%**, ADR-B-12 **35,4%** bez zmian (17/48, maks. działu); wszystkie działy ≤ 38%.
- Wszystkie 15 wyjaśnień: 5 zdań, 336–453 znaki, maks. 24 słowa w zdaniu, na końcu „Podstawa: ADR …”; opcje ≤ 80 znaków; bez słów absolutnych i średników w opcjach.

## Egzaminy, kolejki, snapshoty (pułapki CI)

- Egzaminy próbne – pytania z partii **w `questions`**: wariant-002/klucz-002: **0402**; wariant-003/klucz-003: **0393, 0398**; wariant-005/klucz-005: **0395**. Na listach `excluded_question_ids` (NIE zmieniać): 003 – 0402; 004 – 0393, 0398, 0402; 005 – 0393, 0398, 0402. Wariant/klucz 001 i 004 – tylko SHA.
- `review/specialist/KOLEJKA-PRIORYTETOWA-4X40.json` **zawiera 0402** (question + legal_basis); 4X44 – tylko SHA.
- Snapshoty: `review/sequential/381-398.json` (0391–0398) i `399-416.json` (0399–0405) oraz `review/legal-clauses/381-398.json` i `399-416.json`.
- Ledger `review/legal-polish/stage4w4-literal-verification-ledger-0001-0609.json`: nowe `source_references` dla wszystkich 15 ID.
- Rejestry `REJESTR-AKTUALNY-0001-0765.md` i `-0001-0780.md`: po 15 wierszy.
- SHA banku w **30 plikach** (29 jak w partii 26 + `tests/test_literal_review_0391_0405.py`).
- Oczekiwany SHA banku: **9475e2d4f7107dc676486710ce03d626dc7473d8 → 5e369822335dd871b6499fae080d6e689dc6377c**.

## Test na kopii repo

`test_p27.sh` (kopia /tmp/b27 z main 287fe23de, bez commitów i pushu): `apply_poprawki.py` → „Changed (15): ADR-B-0391 … ADR-B-0405”, blob **5e369822…**; po synchronizacji (`sync_p27_test.py`) wszystkie 14 skryptów CI = 0 i `python3 -m unittest discover -s tests` – **Ran 185 tests, OK**.

## Do zapamiętania na kolejne partie
- 0406–0420: 0406 (1.10.3.2.2 (h)) – sprawdzić z nowym 0405 (g) i 0410; 0407–0408 (postój/kradzież) – z 0144, 0213, 0305, 0582; 0409–0412 (szkolenie z ochrony 1.10.2) – z 0036, 0121, 0275; 0413–0416 (1.10.1.2 / 1.10.1.3 / 1.10.1.4) – z 0034, 0035, 0066, 0067, 0120, 0211, 0249, 0274, 0300, 0519, 0701, 0774–0776; 0417–0420 (8.1.4.1 – liczba i pojemność gaśnic wg DMC) – porównać z pozostałymi pytaniami o gaśnice (8.1.4, moduł ADR-B-08) i sprawdzić tabelę 8.1.4.1 na obrazie strony PDF. Strony Dz.U. dla działu 1.10: 110–114 (nie numery stopki ADR).