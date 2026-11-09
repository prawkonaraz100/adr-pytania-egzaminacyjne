# Kontrola druga – partia ADR-B-0421–0435 (porównanie dosłowne z polskim tekstem ADR 2025)

Data: 2026-11-09, ok. 19:25 (czas polski, CET).
Przedmiot: pierwsza kontrola ChatGPT (PR #888, gałąź `literal-first-0421-0435`, head **a3207b6df**; `review/literal-pl/PARTIA-0421-0435.md` + `.json` + `tests/test_literal_review_0421_0435.py`, wynik 1 OK / 14 POPRAW / 0 BLOKUJ) oraz rekordy 0421–0435 na main **379c599f5** (bank blob **02506637…**, 780 pytań; #888 banku nie zmienia).
Źródło: Dz.U. 2025 poz. 642 (skany PDF), OCR tesseract `-l pol`; strony wg nagłówka „Dziennik Ustaw — NNN —”. Tabela 7.5.2.1 z odsyłaczami (a)–(d) odczytana z **obrazu strony PDF** (część 27, strona 5 = **Dz.U. s. 1305**, render 150 dpi); 7.5.2.2 i 7.5.2.3 – s. 1306, 7.5.2.4 – s. 1307. Sprostowanie poz. 1575 nie dotyczy punktów tej partii (1.1.3.6.2, 1.9.5, 5.4.3.4, 7.5.2, 8.1.4, 8.6.3).
Status: kontrola robocza. **Żadne pytanie nie jest oznaczone jako zweryfikowane**; wszystkie pozostają `needs_review`.

## Podsumowanie

- Werdykty kontroli drugiej: **OK 0, POPRAW 15, BLOKUJ 0** (#888: 1 OK / 14 POPRAW – 0427 nie jest OK, niżej).
- **12 pytań to duplikaty lub bliskie powtórzenia** → **nowy temat z tej samej kompetencji, niecysternowy**: 0421 = 0073, 0422 = 0074/0232, 0423 = 0015/0169/0704/0717/0749, 0426 ≈ 0324, 0428 = 0491, 0429 = 0492, 0430 = 0031, 0431 ≈ 0065/0603 (i merytorycznie mylące), 0432 = 0064/0086/0574/0771, 0433 ≈ 0207/0489/0602, 0434 = 0063/0575, 0435 = 0107/0143/0166/0210.
- **3 pytania** (0424, 0425, 0427) mają właściwy podtemat, ale wady formy/treści → przeredagowane w tym samym podtemacie (konkretny odczyt tabeli 7.5.2.1 / odsyłaczy (a) i (d)).
- Wszędzie ta sama litera klucza, ten sam `module_id`, `image` = null; przypisania w `kompetencje.json` bez zmian (08-K02 = 6, 08-K03 = 6, 09-K01 = 12, 11-K01 = 7, 11-K03 = 6, 11-K04 = 6, 11-K05 = 6, 11-K07 = 6; każda kompetencja teoretyczna ≥ 6).
- **Błąd merytoryczny w banku**: 0431 – wyjaśnienie: „Jeżeli znak zakazuje wjazdu, kierowca musi go respektować niezależnie od wpisu w tabeli A” przy towarze „(-)”. Znak z tabliczką (1.9.5.3.5) dotyczy pojazdów z towarami **objętymi** ograniczeniem danej kategorii, a 1.9.5.3.6 i 8.6.3.1 wyłączają towar „(-)”. Nowa wersja uczy tego poprawnie.
- **Tematy cysternowe**: żaden zamiennik nie jest cysternowy (stary dystraktor 0434 B o kolumnie (12) i cysternach usunięty).
- **Wady formy starych wersji**: opcje > 80 zn. – 0421 B (84), 0423 A (90), 0424 A (94), 0425 A/B (88/92), 0431 A (109), 0432 B (95), 0433 B/C (102/90), 0434 A/B (91/93), 0435 B (81); klucz jedyną najkrótszą – 0424, 0425, 0430, 0431, 0433, 0434, 0435; średniki – 0422 B, 0424 A/C, 0426 A/B, 0429 B; słowa absolutne – 0424 B „tylko”, 0425 A „każdej”, 0427 B „wszystkie”, C (klucz) „tylko”, 0429 A „każda”, C „wszystkie”, 0431 A „wszystkie”/„niezależnie”, B „wyłącznie”, 0433 B „każdy”; opcje-polecenia przy pytaniu „co/jakie znaczenie” – 0422 A, 0424 A/B, 0425 A/B; treść podpowiada – 0424 („wyłącznie po tym, że obie są ADR”), 0427 („dowolnego materiału utleniającego”).

## Błędy / różnice względem raportu ChatGPT (#888)

1. **0427 nie jest OK**: klucz C „Uwaga (d) obejmuje **tylko** wskazane materiały…” (słowo absolutne w kluczu), treść podpowiada („dowolnego materiału utleniającego”), A absurdalne („bez sprawdzania tabeli”), a wyjaśnienie nie mówi, czego dotyczy odsyłacz (d) (materiały wybuchowe kruszące poza UN 0083 + azotan amonu UN 1942/2067, UN 3375, azotany metali alkalicznych i ziem alkalicznych; ładunek traktowany łącznie jako materiał wybuchowy kruszący klasy 1). Odsyłacz (d) zaczyna się na **s. 1305** (kończy na 1306) – #888 podaje tylko 1306.
2. **0424 – propozycja zastępcza z BŁĘDEM MERYTORYCZNYM** (7.5.2.3): klucz „Nie; zakazy obejmują także towary w kontenerze i pozostałe towary pojazdu” jako zasada ogólna jest fałszywy. 7.5.2.3 zdanie 1: przy zakazach ładowania razem do pojazdu **nie bierze się pod uwagę** materiałów w zamkniętych kontenerach o pełnych ścianach; wyjątek (zdanie 2) dotyczy tylko nalepek 1, 1.4, 1.5, 1.6 i grup zgodności klasy 1. Opcja A („Tak, gdy kontener jest szczelnie zamknięty i ma pełne ściany”) opisuje właśnie regułę ogólną – pytanie miałoby dwie bronione odpowiedzi. Temat 7.5.2.3 wykorzystałem poprawnie w 0428 (przypadek z nalepką 1).
3. **0431 – przeoczony błąd merytoryczny** w kluczu/wyjaśnieniu (patrz wyżej), a propozycja zastępcza (1.9.5.3.4 – miejsce ustawienia znaków) **wychodzi poza kompetencję 11-K05** („znaczenie kodu „(-)””). Strona: 1.9.5.3.5–1.9.5.3.6 stoją na **Dz.U. s. 109**, nie 1338.
4. **0435 – propozycja zastępcza to duplikat**: „mały pożar opony – użyć gaśnicy” = 0108, 0184, 0493, 0640, 0695, 0702 (moduł 05), do tego bez związku z tunelem (kompetencja 11-K07 – pożar w tunelu); opcja B „żadnym”.
5. **Inne propozycje #888 z wadami formy**: 0422 – średnik w kluczu B, scenariusz niespójny („etykieta z terminem, ale bez kontroli okresowej”); 0423 – średniki w A i C, temat bliski 0759 (oznaczenie daty/okresu); 0426 (7.5.2.4) – C „wyłącznie”; 0429 (B+D) – A powtarza pułapkę 0492 („oddzielne dokumenty”), temat specjalistyczny (grupy zgodności klasy 1); 0430 (1.9.5.1) – B „wyłącznie”; 0433 (1.9.5.3.7) – B i C „wyłącznie”. Pomysły 7.5.2.4 (wyjątek 1.4) i 1.9.5.1 wykorzystałem w poprawionej formie (0429, 0433).
6. **Brak propozycji dla 0421, 0432, 0434** („brak bezpiecznego tematu”) – są: 0421 – 1.1.3.6.2 zostawia 8.1.4.2–8.1.4.5 (terminy kontroli gaśnicy 2 kg obowiązują), 0432 – „(-)” + kod E (masa nie decyduje, „(-)” nie łagodzi), 0434 – pomyłka kodu klasyfikacyjnego (3b) z kodem tunelowym.
7. **Cytaty niedosłowne**: 0425 („W tabeli 7.5.2.1 przy pozycji 1.4 występuje odsyłacz „a””) i 0426 („występuje zapis „4.1 + 1””) to opisy, nie cytaty. Dosłownie: odsyłacz (a) „Dozwolone jest ładowanie razem z materiałami i przedmiotami 1.4S.”, (b) „Dozwolone jest ładowanie razem towarów klasy 1 i urządzeń ratowniczych klasy 9 (UN 2990, 3072 i 3268).”
8. **Tabela tylko z OCR**: #888 nie miał obrazu tabeli 7.5.2.1 – obraz s. 1305 potwierdza: wiersz 3 / kolumna 1 – puste (zakaz); 1.4 z innymi klasami – „a”; 5.1 / 1 – „d”; 9 / 1 – „b”; 9 / 1.4 – „a, b, c”; 4.1+1 – X tylko z 4.1+1; 5.2+1 – X z 5.2 i 5.2+1.
9. **Brak automatycznego wyszukiwania podobieństw** (manifest #888: „no automated similarity script run”) – przy duplikatach po temacie trzeba przeszukać cały bank, nie tylko listę kandydatów z polecenia (np. 0435 vs 0108/0184/0695).
10. Słusznie w #888: duplikaty 0421 = 0073, 0422 = 0074/0232, 0423 = 0015/0169/0704/0717/0749, 0424 ≈ 0025, 0426 ≈ 0324, 0428 = 0491, 0429 = 0492, 0430 = 0031, 0432 = 0064/0086/0574/0771, 0433 (kategoria E/znak), 0434 = 0063/0575, 0435 – zakaz gaszenia ładowni; strony 1325 (8.1.4.2–8.1.4.5), 1305–1307 (7.5.2), 107 (1.9.5.2.2), 109 (1.9.5.3.5), 1338 (8.6.3), 975 (instrukcje pisemne); licznik 360 → 345; test od razu z dwiema stałymi FIRST_PASS_BANK_SHA / EXPECTED_BANK_SHA; klucze propozycji z tą samą literą.

## Duplikaty – sprawdzenie w całym banku (780) i między sobą

Przeszukano cały bank po temacie (gaśnic, plomb, 8.1.4.3, norm krajow, 1.1.3.6.2, 7.5.2.x, 1.4S, UN 2990/3072/3268, azotan, pełnych ścian, 7.5.2.4, kategorie tuneli, właściwa władza, 1.9.5.3.6, „(-)”, (3b), opon/hamulc/przedział silnika, stojące znaki) oraz skryptami `check_near_duplicates.py` (0,60), `check_cross_module_duplicates.py` (0,80), `similarity.py` (0,45) na kopii po poprawkach – żadnej pary z udziałem 0421–0435. `similarity.py --threshold 0.30`: jedyna para 0291/0429 = 0,304 (0291: LQ + 1.1 → zakaz; 0429: wyjątek dla 1.4 – inny element przepisu).
- **0421** nowe (1.1.3.6.2 + 8.1.4.4) vs 0073/0197/0282/0711/0760 (pojemność, środek równoważny, grupy pożarów, jednostka) i 0074/0232 (miniony termin bez 1.1.3.6) oraz 0761/0762 (inne wyjątki 1.1.3.6.2) – inny element.
- **0422** nowe (ADR odsyła do norm krajowych – nie podaje okresu) – w banku brak; 0176 (plomba ≠ kontrola) tylko jako dystraktor.
- **0423** nowe (8.1.4.3 – gazy toksyczne) – w banku brak pytania o 8.1.4.3.
- **0424** (nalepki 1 i 3 – kratka pusta) vs 0199 (3 i 8 – dozwolone), 0025 (ogólnie „sprawdź tabelę”). **0425** (1.4S + 8 – odsyłacz a) – jedyne o (a). **0426** nowe (odsyłacz b – urządzenia ratownicze klasy 9) – w banku brak. **0427** (odsyłacz d – treść warunku) – jedyne. **0428** nowe (7.5.2.3) – w banku brak. **0429** nowe (7.5.2.4 – wyjątek 1.4) vs 0291 (1.1).
- **0430** nowe (C a D – duży pożar) vs 0031 (A), 0207 (B). **0431** (1.9.5.3.6 – tablice pomarańczowe, ale „(-)” wyłączony; tabliczka E) vs 0065/0174/0603 (znaczenie „(-)”), 0264 (UN 2919), 0540 (LQ 3.4.13). **0432** („(-)” + E) vs 0064/0086/0574/0771/0263/0539/0772. **0433** nowe (1.9.5.1 – kto i jak kategoryzuje) vs 0262 (kategoria zależna od pory). **0434** ((3b) ≠ kod tunelowy) vs 0248 (cyfra kategorii transportowej), 0063/0575/0208/0174. **0435** (w tunelu nie rozstawiać znaków kosztem ucieczki) vs 0143/0210/0308/0592/0773 i 0231/0739 (moduł 05 – „możliwe i bezpieczne” na drodze).
- Uwagi poza partią: para **0071 / 0072** (`similarity.py` 0,909) – do przejrzenia (informacyjnie); **0632** dubluje starą wersję 0297 – do partii z 0632, teraz nic.

## Ustalenia dla poszczególnych pytań (cytaty, strony Dz.U., klucze)

### ADR-B-0421 – POPRAW (08-K02, C) – NOWY TEMAT (duplikat 0073)
- 1.1.3.6.2 (s. 26): „…bez stosowania następujących przepisów: … części 8, z wyjątkiem: 8.1.2.1 (a), 8.1.4.2 do 8.1.4.5, …”. 8.1.4.4 (s. 1325): „…powinny one podlegać kontrolom okresowym…”; 8.1.4.5: „Podczas przewozu nie powinny być przekroczone terminy określone w 8.1.4.4.” Nowy klucz C „Nie, gaśnica wymagana przy 1.1.3.6 też musi mieć ważny termin kontroli” ✔.

### ADR-B-0422 – POPRAW (08-K03, B) – NOWY TEMAT (duplikat 0074/0232)
- 8.1.4.4 akapit 2 (s. 1325): „W celu zapewnienia bezpiecznego działania gaśnic, powinny one podlegać kontrolom okresowym, zgodnie z przyjętymi normami krajowymi.” Klucz B „ADR odsyła do kontroli okresowych według przyjętych norm krajowych” ✔; A (12 miesięcy) – ADR takiego okresu nie podaje.

### ADR-B-0423 – POPRAW (08-K03, C) – NOWY TEMAT (duplikat 0015/0169/0704/0717/0749)
- 8.1.4.3 (s. 1325): „Środki gaśnicze nie powinny powodować uwalniania gazów toksycznych do wnętrza kabiny kierowcy lub pod wpływem ciepła wydzielanego podczas pożaru.” Klucz C ✔.

### ADR-B-0424 – POPRAW (09-K01, C) – przeredagowane (tabela 7.5.2.1)
- 7.5.2.1 (s. 1305): „…mogą zostać załadowane do tego samego pojazdu lub kontenera, tylko wtedy, gdy jest to dozwolone na podstawie poniższej tabeli…”. Obraz: wiersz 3 / kolumna 1 – brak X i odsyłacza. Klucz C „Nie, tabela nie dopuszcza ładowania razem przesyłek z nalepkami 1 i 3” ✔.

### ADR-B-0425 – POPRAW (09-K01, C) – przeredagowane (odsyłacz a)
- Odsyłacz (a) (s. 1305): „Dozwolone jest ładowanie razem z materiałami i przedmiotami 1.4S.” Obraz: wiersz 8 / kolumna 1.4 – „a”. Klucz C ✔ (naboje 1.4S + nalepka 8).

### ADR-B-0426 – POPRAW (09-K01, B) – NOWY TEMAT (≈ 0324)
- Odsyłacz (b) (s. 1305): „Dozwolone jest ładowanie razem towarów klasy 1 i urządzeń ratowniczych klasy 9 (UN 2990, 3072 i 3268).” Obraz: wiersz 9 / kolumna 1 – „b”. Klucz B ✔.

### ADR-B-0427 – POPRAW (09-K01, C) – przeredagowane (odsyłacz d; #888: OK)
- Odsyłacz (d) (s. 1305–1306): „Dozwolone jest ładowanie razem materiałów wybuchowych kruszących (z wyjątkiem UN 0083 …) z azotanem amonu (UN 1942 i 2067), … pod warunkiem, że w zakresie oznakowania pojazdu lub kontenera, segregacji, rozmieszczenia i ograniczeń ilościowych, ładunek taki traktowany jest łącznie jako materiał wybuchowy kruszący klasy 1.” Obraz: wiersz 5.1 / kolumna 1 – „d”. Klucz C ✔.

### ADR-B-0428 – POPRAW (09-K01, C) – NOWY TEMAT (duplikat 0491)
- 7.5.2.3 (s. 1306): „…nie bierze się pod uwagę materiałów znajdujących się w kontenerach zamkniętych, o pełnych ścianach. Jednakże zakazy ładowania razem podane w 7.5.2.1 dotyczące ładowania sztuk przesyłek zaopatrzonych w nalepki ostrzegawcze zgodne ze wzorami nr 1, 1.4, 1.5 lub 1.6 z innymi sztukami przesyłek … mają również zastosowanie do towarów niebezpiecznych znajdujących się w kontenerze i innych towarów niebezpiecznych załadowanych do tego samego pojazdu…”. Klucz C ✔.

### ADR-B-0429 – POPRAW (09-K01, B) – NOWY TEMAT (duplikat 0492)
- 7.5.2.4 (s. 1307): „Ładowanie razem towarów niebezpiecznych zapakowanych w ilościach ograniczonych z jakimkolwiek rodzajem materiałów wybuchowych i przedmiotów z materiałami wybuchowymi, z wyłączeniem podklasy 1.4 oraz UN 0161 i UN 0499, jest zabronione.” Klucz B ✔.

### ADR-B-0430 – POPRAW (11-K01, C) – NOWY TEMAT (duplikat 0031)
- 1.9.5.2.2 (s. 107–108): C – „…wybuchem o bardzo dużym zasięgu, wybuchem o dużym zasięgu lub działaniem trującym o dużym zasięgu”; D (s. 108) – „…działaniem trującym o dużym zasięgu lub dużym pożarem”, „towary niebezpieczne objęte ograniczeniem określonym dla tunelu kategorii C; oraz …”. Klucz C ✔.

### ADR-B-0431 – POPRAW (11-K05, C) – przepisane (merytorycznie mylące; ≈ 0065/0603)
- 1.9.5.3.6 (s. 109): „Ograniczenia przewozu przez tunele mają zastosowanie do jednostek transportowych, dla których, zgodnie z przepisami 5.3.2, wymagane jest oznakowanie tablicami barwy pomarańczowej, z wyjątkiem przewozu towarów niebezpiecznych, które oznaczono „(-)” w kolumnie (15) tabeli A…”; 8.6.3.1 (s. 1338): „Znak „(—)” … oznacza, że towar niebezpieczny nie podlega żadnym ograniczeniom przewozu przez tunele.” Klucz C ✔.

### ADR-B-0432 – POPRAW (11-K04, C) – NOWY WARIANT (duplikat 0064/0086/0574/0771)
- 8.6.3.2 (s. 1338): „…do całego ładunku stosuje się ten ze wskazanych kodów, który odpowiada największym ograniczeniom.” + 8.6.3.1 („(-)” – brak ograniczeń dla tego towaru). Klucz C „Kod E…” ✔.

### ADR-B-0433 – POPRAW (11-K01, A) – NOWY TEMAT (≈ 0207/0489/0602)
- 1.9.5.1 (s. 106): „…właściwa władza powinna zaliczyć ten tunel do jednej z kategorii tuneli określonych w 1.9.5.2.2, biorąc pod uwagę charakterystykę tunelu, ocenę ryzyka z uwzględnieniem dostępności i odpowiedniości alternatywnych tras przewozu i użycia innych rodzajów transportu oraz warunków zarządzania ruchem drogowym.” Klucz A ✔.

### ADR-B-0434 – POPRAW (11-K03, C) – NOWY WARIANT (duplikat 0063/0575)
- 8.6.3.1 (s. 1338): „Kod ograniczeń przewozu przez tunele podany jest w nawiasie w dolnej części komórki.” (kolumna (15) tabeli A); kolumna (3b) – kod klasyfikacyjny (3.2.1). Klucz C ✔.

### ADR-B-0435 – POPRAW (11-K07, A) – NOWY TEMAT (duplikat 0107/0143/0166/0210)
- Instrukcje pisemne 5.4.3.4 (s. 975): „…członkowie załogi pojazdu powinni wykonać następujące czynności, jeżeli jest to możliwe i bezpieczne: … Założyć kamizelkę ostrzegawczą i odpowiednio umieścić stojące znaki ostrzegawcze; … Członkowie załogi pojazdu nie powinni gasić pożaru obejmującego przedział ładunkowy; … Oddalić się od miejsca wypadku lub zagrożenia, poinformować inne osoby o konieczności oddalenia się…”. Klucz A ✔.

## Wskaźniki

- „Poprawna = jedyna najdłuższa”: **32/780 = 4,10% bez zmian**, maksimum działu **7,87%** bez zmian – linii w `docs/POKRYCIE-KURSU.md`, `podstawowy/README.md`, `PAKIET-ZAMKNIECIE-0780.md` **nie zmieniać** (tylko SHA tam, gdzie występuje).
- „Poprawna = jedyna najkrótsza”: **187 → 180/780**; ADR-B-09 29,0% → **25,8%** (16/62), ADR-B-11 23,9% → **13,0%** (6/46), ADR-B-08 30,2% bez zmian; maksimum działu 31,5%; wszystkie działy ≤ 38%.
- Wszystkie 15 wyjaśnień: 5 zdań, 363–472 znaki, maks. 34 słowa w zdaniu, na końcu „Podstawa: ADR …”; opcje 59–78 znaków; bez słów absolutnych i średników w opcjach.

## Egzaminy, kolejki, snapshoty (pułapki CI)

- Egzaminy próbne – pytania z partii **w `questions`**: wariant/klucz-001: **0421, 0427**; 002: **0433**; 004: **0430**; 005: **0422, 0424, 0431**. Na listach `excluded_question_ids` (NIE zmieniać): 002 – 0421, 0427; 003 – 0421, 0427, 0433; 004 – 0421, 0427, 0433; 005 – 0421, 0427, 0430, 0433. Wariant/klucz-003 – tylko SHA.
- `review/specialist/KOLEJKA-PRIORYTETOWA-4X44.json` zawiera **0427 i 0428** („question” + „legal_basis”); 4X40 – tylko SHA.
- Snapshoty: `review/sequential/417-436.json` i `review/legal-clauses/417-436.json` (wszystkie 15 ID; clause, answer_review A/B/C, notes_on_conditions ≥ 25 zn.).
- Ledger `review/legal-polish/stage4w4-literal-verification-ledger-0001-0609.json`: nowe `source_references` dla wszystkich 15 ID (wszystkie się zmieniają).
- Rejestry `REJESTR-AKTUALNY-0001-0765.md` i `-0001-0780.md`: po 15 wierszy.
- SHA banku 02506637… występuje w **32 plikach**: **31 zamienianych wprost** (docs/POKRYCIE-KURSU.md, docs/STAN-KONCOWY-…, podstawowy/README.md, review/README.md, podstawowy/raporty/etap-4x135-wykluczenia-proby.json, 9 plików review/specialist, 10 plików egzaminów, tests/test_literal_review_0301_0315 … 0391_0405 (7) oraz **0406_0420** – w nim EXPECTED_BANK_SHA, FIRST_PASS = 5e369822… zostaje) + `tests/test_literal_review_0421_0435.py` – TYLKO EXPECTED_BANK_SHA (FIRST_PASS_BANK_SHA = 02506637… zostaje). Historycznych raportów `review/literal-pl/` nie zmieniać.
- Oczekiwany SHA banku: **025066373056366cfff08ee01a6a5394c7c90218 → fa4e38350731bd52c1a64a8cab934bdf18988438**.

## Test na kopii repo

`test_p29.sh` (kopia /tmp/b29 z head #888 **a3207b6df** = main 379c599f5 + raport #888, bez commitów i pushu): `apply_poprawki.py` → „Changed (15): ADR-B-0421 … ADR-B-0435”, blob **fa4e38350731bd52c1a64a8cab934bdf18988438**; po synchronizacji (`sync_p29_test.py`) wszystkie 14 skryptów CI = 0 i `python3 -m unittest discover -s tests` – **190 testów OK**.

## Licznik

Po wdrożeniu partii 29 (obie kontrole 0421–0435): **345 pytań bez porównania dosłownego po obu kontrolach** (0436–0780); kontrola pierwsza partii 30 (0436–0450): 345 → 330.

## Do zapamiętania na kolejne partie
- 0436 (7.5.1.2 – uszkodzona przesyłka przed załadunkiem, 09-K08 = 7) – porównać z 0138, 0202, 0239, 0554, 0555, 0560 i 0078, 0238; 0437–0443 (1.1.4.5 – przewóz innym środkiem transportu, 10-K04 = 11) – 7 pytań o ten sam punkt, sprawdzić duplikaty między sobą i z 0141, 0205, 0320, 0387; 0444–0450 (1.1.4.3 cysterny przenośne IMO, 1.1.4.7 naczynia ciśnieniowe DOT, 10-K05 = 19) – między sobą i z 0321, 0386, 0451–0454; zamienniki niecysternowe.
- 0071/0072 (0,909) i 0632 (≈ stara 0297) – przy właściwych partiach.
