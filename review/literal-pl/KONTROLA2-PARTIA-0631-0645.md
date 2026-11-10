# Kontrola druga – partia ADR-B-0631–0645 (porównanie dosłowne z polskim tekstem ADR 2025)

Data: 2026-11-10 (czas polski, CET).
Przedmiot: pierwsza kontrola ChatGPT (PR #917, scalony; main **a158c1dc4**; `review/literal-pl/PARTIA-0631-0645.md` + `.json` + `tests/test_literal_review_0631_0645.py`, podsumowanie 2 OK / 13 POPRAW / 0 BLOKUJ, licznik 150 → 135) oraz rekordy 0631–0645 na main (bank blob **8596a7a6…**, 780 pytań; #917 banku nie zmienia).
Źródła: Dz.U. 2025 poz. 642 (OCR `-l pol`, przy tabelach obraz strony PDF – s. 976, 977; strony wg nagłówka „Dziennik Ustaw — NNN —”): s. 38, 42, 44 (1.2.1 – definicje), s. 182 (2.2.42.1.1), s. 953 (5.3.2.1.1), s. 955 (5.3.2.2.1), s. 956 (5.3.2.3.1), s. 957 i 959 (5.3.2.3.2 – 33, 323, 333, 83, X83, 85), s. 975 (wzór instrukcji pisemnych), s. 976–977 (dodatkowe wskazówki – nalepki 2.2, 3, 9, 9A), s. 978 (wykaz wyposażenia), s. 1307 (7.5.4), s. 1324–1325 (8.1.4.1, 8.1.4.4, 8.1.5.2, 8.1.5.3), s. 1327 (8.2.2.3.2 (e)), s. 1328 (8.2.2.3.8). Dodatkowo: Wytyczne ERC 2025 (BLS dorosłych) dla 0642 i 0643.
Status: kontrola robocza. **Żadne pytanie nie jest oznaczone jako zweryfikowane**; wszystkie pozostają `needs_review`; `review/approvals.jsonl` pusty.

## Podsumowanie

- Werdykty kontroli drugiej: **OK 0, POPRAW 15, BLOKUJ 0**.
- **Żaden z 2 werdyktów OK w #917 nie jest OK** (0632, 0633 – szczegóły niżej). ChatGPT nadal zawyża OK.
- **#917 – wreszcie każdy POPRAW ma `proposed_replacement`** (13/13) – dobrze. ALE **wszystkie 13 zamienników dublują pytania z banku**: 0631 = 0110/0167/0707; 0634 = 0018; 0635 = 0017/0170/0698/0752; 0636 = 0052; 0637 = 0507; 0638 = 0081; 0639 = 0659; 0640 ≈ 0176; 0641 = 0585/0647/0717; 0642 = 0165; 0643 = 0745; 0644 = 0104/0182/0690; 0645 = 0102/0164/0738. Żadnego nie dało się przejąć.
- **#917 – test ma znów JEDNĄ stałą SHA** (EXPECTED_BANK_SHA dla manifestu i banku) – wbrew poleceniu (dwie stałe). Przy wdrożeniu rozdzielam ją na FIRST_PASS_BANK_SHA (manifest) i EXPECTED_BANK_SHA (bank). Test sprawdza `counts` względem stałej, nie przelicza ich z rekordów (wbrew poleceniu); liczby 2/13 są jednak zgodne z rekordami.
- **#917 – licznik 150 → 135 poprawny; strony Dz.U. dla pierwotnych treści poprawne** (0631 [975], 0632 [975], 0633 [975, 1325], 0634 [955], 0635 [956], 0636 [955], 0637 [956], 0638 [1307], 0639 [22], 0640–0645 [975]).
- **Wspólne wady pierwotnych 0631–0645**: treści ogólnikowe („Co powinien zrobić?”), opcje > 80 zn. w całej partii, kropki na końcu opcji (0639–0645), średniki (0640 B, 0641 B, 0642 C, 0644 B), słowa absolutne (0633, 0635, 0637–0640, 0642, 0644), klucz jedyną najkrótszą (0631–0638, 0640, 0645) lub najdłuższą (0641, 0644), a przede wszystkim duplikaty tematyczne – każde z 15 pytań dubluje temat już obecny w banku.
- **15 pytań → nowy element tej samej kompetencji, niecysternowy**: 0631 (rękawice i ochrona oczu przed osłonięciem kratki), 0632 (gapie palący papierosy przy oparach benzyny), 0633 (kamizelka także w dzień), 0634 (tablica zostaje z tyłu odłączonej przyczepy), 0635 (333 – materiał piroforyczny ciekły), 0636 (pozioma linia na tablicy bez numerów – dozwolona, niewymagana), 0637 (83 – żrący i zapalny), 0638 (CV28 – także rampa i karma dla zwierząt), 0639 (definicja ładunku całkowitego), 0640 (gaśnica z zerwaną plombą po użyciu), 0641 (podejście do pożaru hamulca od strony nawietrznej), 0642 (RKO – 5–6 cm, 100–120/min), 0643 (AED – nikt nie dotyka, potem od razu RKO), 0644 (butle 2.2 przy pożarze – wybuch przy ogrzaniu, schronić się), 0645 (dymiący karton baterii z nalepką 9A).
- Litery kluczy, moduły i kompetencje bez zmian; nowych ID brak; bez tematów cysternowych. Liczebność kompetencji bez zmian: 05-K08, 05-K09, 05-K10, 06-K05, 06-K06, 06-K07, 06-K08, 09-K03, 01-K01 – po 6; **05-K13, 05-K14, 05-K15 – nadal po 5** (nie uszczuplone; uzupełnienie do 6 wymaga decyzji poza tą partią).

## Błędy / różnice względem raportu ChatGPT (#917)

| ID | #917 | Kontrola 2 | Różnica |
|---|---|---|---|
| 0631 | POPRAW | POPRAW – nowy element | zgoda co do werdyktu; zamiennik = 0110/0167/0707 (zdjąć zanieczyszczoną odzież); A/B/C > 80, klucz jedyną najkrótszą; = 0643 w tej samej partii |
| 0632 | OK | POPRAW – nowy element | B/C > 80 zn., klucz jedyną najkrótszą, treść ogólnikowa; = 0111/0186/0697 (ostrzeganie osób postronnych) |
| 0633 | OK | POPRAW – nowy element | B/C > 80 zn., „tylko” w B, klucz jedyną najkrótszą; = 0112/0168/0693 (kamizelka i znaki) |
| 0634 | POPRAW | POPRAW – nowy element | zgoda; zamiennik = 0018 (wymiary 40 × 30 cm); stare = 0753 |
| 0635 | POPRAW | POPRAW – nowy element | zgoda; zamiennik = 0017/0170/0698/0752; stare = 0051/0754, „zawsze” w A |
| 0636 | POPRAW | POPRAW – nowy element | zgoda; zamiennik = 0052 (barwa tablicy); stare = 0193 |
| 0637 | POPRAW | POPRAW – nowy element | zgoda; zamiennik = 0507 (zero w numerze 80); stare = 0053/0005, „wyłącznie” w B |
| 0638 | POPRAW | POPRAW – nowy element | zgoda; zamiennik = 0081 (0,8 m); stare ≈ 0027/0082, w treści brak CV28 – pytanie niejednoznaczne |
| 0639 | POPRAW | POPRAW – nowy element | zgoda; zamiennik = 0659 (struktura ADR); stare = 0659, kropki, „wszystkie”/„wyłącznie” |
| 0640 | POPRAW | POPRAW – nowy element | zgoda; zamiennik ≈ 0176 (plomba); stare = 0592/0695/0108, „;” w B, „Zawsze”/„Tylko” |
| 0641 | POPRAW | POPRAW – nowy element | zgoda; zamiennik = 0585/0647/0717; stare = 0107/0166/0614/0702/0742, klucz jedyną najdłuższą |
| 0642 | POPRAW | POPRAW – nowy element | zgoda; zamiennik = 0165; stare = 0113/0187/0648, „;” w C, „zawsze” w A |
| 0643 | POPRAW | POPRAW – nowy element | zgoda; zamiennik = 0745 (rękawice); stare = 0110/0167/0707 i 0631 |
| 0644 | POPRAW | POPRAW – nowy element | zgoda; zamiennik = 0104/0182/0690; stare = 0100/0163/0612, „;” w B, klucz jedyną najdłuższą |
| 0645 | POPRAW | POPRAW – nowy element | zgoda; zamiennik = 0102/0164/0738; stare = 0104/0116/0735, kropki, klucz jedyną najkrótszą |

## Duplikaty – sprawdzenie w całym banku (780) i między sobą

- Stare rekordy: 0631 = 0110/0167/0707 (i = 0643); 0632 = 0111/0186/0697; 0633 = 0112/0168/0693; 0634 = 0753; 0635 = 0051/0754; 0636 = 0193; 0637 = 0053/0005; 0638 ≈ 0027/0082; 0639 = 0659; 0640 = 0592/0695/0108; 0641 = 0107/0166/0614/0702/0742; 0642 = 0113/0187/0648; 0643 = 0110/0167/0707; 0644 = 0100/0163/0612; 0645 = 0104/0116/0735.
- Nowe rekordy – sprawdzone ręcznie z najbliższymi tematami: 0631 vs 0110/0167/0707/0745 (skażona odzież, rękawice) i 0163/0612 (osłona kratki); 0632 vs 0111/0186/0697/0746 i 0152/0736/0010 (palenie przy przeładunku); 0633 vs 0112/0168/0693/0231/0747/0252; 0634 vs 0018/0191/0258/0753/0694; 0635 vs 0051/0754/0192/0505/0217; 0636 vs 0190/0052/0193/0257/0685/0755; 0637 vs 0053/0194/0653/0756/0298/0256/0507; 0638 vs 0027/0081/0082/0684/0765; 0639 vs 0123/0147/0312/0659/0709; 0640 vs 0176/0015/0592/0695; 0641 vs 0184/0108/0695/0493/0702/0742/0743; 0642 i 0643 vs 0715 (kolejność 112–RKO–AED), 0748 (pozycja boczna); 0644 vs 0221 (2.1), 0284/0355 (2.2); 0645 vs 0099/0162/0546/0673.
- Odrzucone kandydatury (temat zajęty): okna przy klasie 1 (0222), pozycja boczna (0748), sekwencja RKO (0715), płukanie oczu (0225), maska ucieczkowa (0230), 4.3 sucho (0155), 4.2 (0361), 5.1 trociny (0354), czas narażenia klasy 7 (0295), litera X, cyfra zero (0507), barwa i wymiary tablic, zagłębienia terenu 2.1 (0221), palenie przy czynnościach ładunkowych (0152/0736/0010).
- `similarity.py`: cały bank – main **7 par ≥ 0,45 / 154 par ≥ 0,25**; po poprawkach **7 / 156**. Pary z udziałem partii: main **0 ≥ 0,45 / 7 ≥ 0,25**; po poprawkach **0 / 9** (najwyższe: 0184/0641 = 0,357 – 0184 „czy wolno gasić”, 0641 „skąd podejść”; 0635/0653 = 0,353 i pozostałe – rodzina pytań o różne numery rozpoznawcze zagrożenia: 44, 83, 88, 99, 333, 336, 886 – każdy numer inny).
- `check_near_duplicates.py --threshold 0.60`: 0 nieprzejrzanych par; `check_cross_module_duplicates.py --threshold 0.80`: PASS.
- Uwagi na później (poza tą partią): 0708 (moduł 10) = 0714; w partii 44: 0646 i 0651 (zaliczenie tematu samym testem) dublują się wzajemnie; 0647 ≈ 0015 (dostępność gaśnicy, 8.1.4.5).

## Szczegóły – cytaty (dosłownie z Dz.U.) i rozstrzygnięcia

### ADR-B-0631 – POPRAW (05-K08, C) – NOWY ELEMENT (= 0110/0167/0707)
Wzór instrukcji pisemnych 5.4.3.4 (s. 975): „Jeżeli jest to właściwe i bezpieczne, zapobiec przedostaniu się uwolnionych materiałów do środowiska wodnego lub kanalizacji oraz zebrać uwolnione materiały, używając wyposażenia przewożonego w jednostce transportowej;”. 8.1.5.2 (s. 1325): „oraz dla każdego członka załogi pojazdu (…) para rękawic ochronnych; oraz ochrona oczu (np. okulary ochronne).” 8.1.5.3 (s. 1325): maska ucieczkowa – dla nalepek 2.3 lub 6.1. Nowe pytanie: przed osłonięciem kratki przy wycieku z nalepką 3 kierowca zakłada rękawice i ochronę oczu. Do oceny specjalisty (czy użycie środków ochrony jest obowiązkiem, czy dobrą praktyką). Opcje 67/72/72 zn.

### ADR-B-0632 – POPRAW (05-K09, A) – NOWY ELEMENT (= 0111/0186/0697)
Wzór instrukcji pisemnych 5.4.3.4 (s. 975): „Unikać źródeł zapłonu, w szczególności nie palić, nie używać papierosów elektronicznych lub podobnych urządzeń oraz nie włączać żadnych urządzeń elektrycznych;” oraz „Oddalić się od miejsca wypadku lub zagrożenia, poinformować inne osoby o konieczności oddalenia się od tego miejsca oraz stosować się do zaleceń służb ratowniczych;”. Nalepka 3 (s. 976, obraz strony): „Zagrożenie pożarem. Zagrożenie wybuchem.”. Nowe pytanie: gapie palą papierosy po zawietrznej stronie wycieku benzyny → ostrzec, by zgasili papierosy i odeszli. Opcje 70/69/71 zn.

### ADR-B-0633 – POPRAW (05-K10, A) – NOWY ELEMENT (= 0112/0168/0693)
Wzór instrukcji pisemnych 5.4.3.4 (s. 975): „Założyć kamizelkę ostrzegawczą i odpowiednio umieścić stojące znaki ostrzegawcze;”. 8.1.5.2 (s. 1325): „dla każdego członka załogi pojazdu – kamizelka ostrzegawcza (np. określona w normie EN ISO 20471)”. Nowe pytanie: awaria w dzień na drodze lokalnej → kamizelkę zakłada się także w dzień. Do oceny specjalisty. Opcje 63/72/58 zn.

### ADR-B-0634 – POPRAW (06-K05, A) – NOWY ELEMENT (= 0753, ≈ 0018/0191)
5.3.2.1.1 akapit drugi (s. 953): „Jeżeli przyczepa zawierająca towary niebezpieczne została odłączona od pojazdu samochodowego w trakcie przewozu towarów niebezpiecznych, to tablica barwy pomarańczowej powinna pozostać z tyłu przyczepy.” Nowe pytanie: przyczepa odłączona na parkingu → tablica zostaje z tyłu przyczepy. Opcje 74/73/74 zn.

### ADR-B-0635 – POPRAW (06-K06, C) – NOWY ELEMENT (= 0051/0754)
5.3.2.3.2 (s. 957): „333 materiał piroforyczny ciekły”; „33 materiał łatwo zapalny ciekły (temperatura zapłonu niższa niż 23 °C)”; „323 materiał zapalny ciekły, który reaguje z wodą wydzielając gazy palne”. 2.2.42.1.1 (s. 182): „Materiały piroforyczne, które (…) w zetknięciu z powietrzem, nawet w małych ilościach, zapalają się w ciągu 5 minut.” 5.3.2.3.1 (s. 956) – zasada potrajania cyfry. Nowe pytanie: 333 ≠ 33 – materiał piroforyczny ciekły. Opcje 59/76/70 zn.

### ADR-B-0636 – POPRAW (06-K07, B) – NOWY ELEMENT (= 0193)
5.3.2.2.1 (s. 955): „Przez środek tablicy może przebiegać czarna pozioma linia o szerokości 15 mm.” Nowe pytanie: na jednej tablicy bez numerów linia jest, na drugiej nie ma – obie zgodne, linia dozwolona, ale niewymagana. Do oceny specjalisty (tablice z linią i bez linii na jednej jednostce). Opcje 64/62/61 zn.

### ADR-B-0637 – POPRAW (06-K08, A) – NOWY ELEMENT (= 0053/0005)
5.3.2.3.2 (s. 959): „83 materiał żrący lub słabo żrący, zapalny (temperatura zapłonu od 23 °C do 60 °C włącznie)”; „X83 materiał żrący lub słabo żrący, zapalny (…), który reaguje niebezpiecznie z wodą”; „85 materiał żrący lub słabo żrący, utleniający (wzmagający palenie)”. Nowe pytanie: numer 83 → materiał żrący i zapalny (23–60 °C). Opcje 68/69/66 zn.

### ADR-B-0638 – POPRAW (09-K03, A) – NOWY ELEMENT (≈ 0027/0082; treść bez CV28)
7.5.4 (s. 1307): „Jeżeli w kolumnie (18) tabeli A w dziale 3.2 wskazany jest dla danego materiału lub przedmiotu przepis szczególny CV28, to należy przedsięwziąć podane poniżej środki ostrożności wobec żywności, artykułów spożywczych i karmy dla zwierząt.” oraz akapit drugi: sztuki przesyłek z nalepkami 6.1, 6.2 lub 9 (wskazane UN) „nie powinny być spiętrzane lub ładowane w bezpośredniej bliskości sztuk przesyłek, o których wiadomo, że zawierają żywność, artykuły spożywcze lub karmę dla zwierząt. Dotyczy to pojazdów, kontenerów oraz miejsc załadunku, rozładunku i przeładunku.” Nowe pytanie: CV28 podany w treści; ograniczenia obejmują też rampę (miejsce przeładunku) i karmę dla zwierząt. Opcje 74/74/72 zn.

### ADR-B-0639 – POPRAW (01-K01, A) – NOWY ELEMENT (= 0659)
1.2.1 (s. 38): „Ładunek całkowity oznacza ładunek pochodzący od jednego nadawcy, mającego wyłączne prawo do używania pojazdu lub kontenera wielkiego, a wszystkie czynności załadunkowe i rozładunkowe wykonywane są zgodnie z instrukcjami nadawcy lub odbiorcy.” (s. 44): „Przewóz luzem oznacza przewóz nieopakowanych materiałów stałych lub przedmiotów (…)”. (s. 42): „Opakowanie zbiorcze oznacza opakowanie użyte (…) w celu umieszczenia w nim jednej lub większej liczby sztuk przesyłek (…)”. Nowe pytanie: rozpoznanie definicji ładunku całkowitego. Opcje 59/61/59 zn.

### ADR-B-0640 – POPRAW (05-K13, C) – NOWY ELEMENT (= 0592/0695/0108)
8.1.4.4 (s. 1325): „Gaśnice przenośne, zgodne z przepisami podanymi w 8.1.4.1 lub 8.1.4.2, powinny być zaopatrzone w plombę potwierdzającą, że nie były one używane.”; 8.1.4.1 (s. 1324) – minimalne wymagania. Nowe pytanie: po ugaszeniu pożaru opony gaśnica ma zerwaną plombę → nie spełnia już wymagań 8.1.4.4. Pokrewne 0176 (co potwierdza plomba). Do oceny specjalisty (czy przed dalszą jazdą trzeba ją wymienić). Opcje 70/72/72 zn.

### ADR-B-0641 – POPRAW (05-K13, B) – NOWY ELEMENT (= 0107/0166/0614/0702/0742)
Wzór instrukcji pisemnych 5.4.3.4 (s. 975): „Nie wchodzić na uwolnione materiały, nie dotykać ich, unikać wdychania oparów, dymu, pyłu i pary poprzez pozostawanie po stronie nawietrznej;” oraz „Jeżeli jest to właściwe i bezpieczne, użyć gaśnic w celu ugaszenia małego lub będącego w fazie początkowej pożaru, obejmującego opony, hamulce lub przedział silnika;”. Nowe pytanie: mały pożar hamulca, wiatr od przodu → podejść od strony nawietrznej (od przodu). Odrębne od 0184 (czy wolno gasić) – similarity 0,357. Opcje 61/60/58 zn.

### ADR-B-0642 – POPRAW (05-K14, C) – NOWY ELEMENT (= 0113/0187/0648)
8.2.2.3.2 (e) (s. 1327): „czynności, które należy podjąć po zaistnieniu wypadku (pierwsza pomoc, bezpieczeństwo ruchu drogowego, podstawowa wiedza na temat używania sprzętu ochronnego, itp.)”; 8.2.2.3.8 (s. 1328): „(…) indywidualne ćwiczenia praktyczne, obejmujące co najmniej sposoby udzielania pierwszej pomocy, gaszenie pożaru oraz postępowanie w razie zaistnienia wypadku lub awarii.” Treść merytoryczna: Wytyczne ERC 2025 (BLS dorosłych) – uciśnięcia na głębokość 5–6 cm, tempo 100–120/min (sprawdzone w źródle internetowym). ADR nie podaje parametrów RKO – do oceny specjalisty (instruktor pierwszej pomocy). Opcje 73/65/68 zn.

### ADR-B-0643 – POPRAW (05-K14, C) – NOWY ELEMENT (= 0110/0167/0707 i 0631)
8.2.2.3.2 (e) (s. 1327) i 8.2.2.3.8 (s. 1328) – jak 0642. Treść merytoryczna: Wytyczne ERC 2025 (BLS dorosłych, AED) – podczas analizy i wyładowania nikt nie dotyka poszkodowanego; po wyładowaniu natychmiast wznowić uciśnięcia. Pokrewne 0715 (kolejność: 112, RKO, AED) – tu odrębny etap. Do oceny specjalisty (instruktor pierwszej pomocy). Opcje 77/70/73 zn.

### ADR-B-0644 – POPRAW (05-K15, B) – NOWY ELEMENT (= 0100/0163/0612)
Wzór 5.4.3.4, dodatkowe wskazówki (s. 976, obraz strony), nalepka 2.2 „Gazy niepalne i nietrujące”: „Zagrożenie działaniem duszącym. Mogą znajdować się pod ciśnieniem. Mogą powodować odmrożenia. Zagrożenie wybuchem w przypadku ogrzania.” – kolumna (3): „Schronić się. Unikać zagłębień terenu.” Nowe pytanie: butle 2.2 obok płonącego pojazdu → zagrożenie wybuchem przy ogrzaniu, oddalić się i schronić. Opcje 65/67/69 zn.

### ADR-B-0645 – POPRAW (05-K15, C) – NOWY ELEMENT (= 0104/0116/0735)
Wzór 5.4.3.4, dodatkowe wskazówki (s. 977, obraz strony), nalepki 9 i 9A „Różne materiały i przedmioty niebezpieczne”: „Zagrożenie poparzeniem. Zagrożenie pożarem. Zagrożenie wybuchem. Zagrożenie w przypadku przedostania się do środowiska wodnego lub kanalizacji.” Nowe pytanie: dymiący karton baterii litowych z nalepką 9A → ryzyko pożaru, wybuchu i poparzenia, odsunąć się. Odrębne od 0099/0162/0546/0673 (rozpoznanie klasy 9). Opcje 60/61/60 zn.

## Wskaźniki

- Wszystkie 15 rekordów: wyjaśnienie ≥ 300 zn., 2–5 zdań, maks. 35 słów w zdaniu, koniec „Podstawa: ADR …”; opcje ≤ 80 zn.; bez słów absolutnych, średników, kropek na końcu opcji, „np.”, „min.”, „kol.”, „odpowiedź A/B/C”.
- Klucz nie jest jedyną najdłuższą ani jedyną najkrótszą w żadnym z 15 rekordów.
- „Poprawna = jedyna najdłuższa”: **23/780 = 2,95% → 21/780 = 2,69%**; maksimum działu **5,66% bez zmian**. **Aktualizacja w 3 miejscach / 3 plikach**: `docs/POKRYCIE-KURSU.md`, `docs/STAN-KONCOWY-BANKU-ADR-PODSTAWOWY-2026-11-03.md` (wiersz globalny; wiersz „Najwyższy wskaźnik w pojedynczym dziale” 5,66% bez zmian), `podstawowy/README.md`.
- „Poprawna = jedyna najkrótsza”: 104 → 94/780; ADR-B-05 24,1% → 18,4%; ADR-B-06 18,2% → 12,1%; ADR-B-09 11,3% → 9,7%; ADR-B-01 16,7% bez zmian; każdy dział ≤ 38%.
- Rozkład liter kluczy bez zmian.

## Egzaminy, kolejki, snapshoty (pułapki CI)

- Egzaminy próbne: wariant 002 – 0631, 0634; wariant 003 – 0632, 0635; wariant 004 – 0633, 0636; wariant 005 – 0637, 0638 (`wariant-00N.json`: stem, options; `klucz-00N.json`: explanation, legal_basis; litery bez zmian). `excluded_question_ids` w 003–005 zawierają ID z partii – bez zmian.
- Kolejki `KOLEJKA-PRIORYTETOWA-4X40.json` / `4X44.json`: żadnego ID z partii – zmienia się tylko `source_bank_blob_sha`.
- Snapshoty `review/sequential/` i `review/legal-clauses/`: **629-654.json** (0631–0645; rekordy 0629–0630 i 0646–0654 bez zmian).
- Ledger `review/legal-polish/stage4w4-literal-verification-ledger-0610-0678.json` (0631–0645): `source_references` – 15 ID.
- Rejestry `REJESTR-AKTUALNY-0001-0765.md` i `-0001-0780.md`: po 15 wierszy.
- SHA banku 8596a7a6… w **46 plikach** poza historycznymi raportami `review/literal-pl/` i poza `tests/test_literal_review_0631_0645.py` – w tym 22 testy `test_literal_review_0301_0315 … 0616_0630` (w 0571_0585, 0586_0600, 0601_0615, 0616_0630 tylko EXPECTED_BANK_SHA; ich FIRST_PASS zostają).
- Lekcje: `podstawowy/lekcje/ADR-B-06.md` (scenariusz „tablice pomarańczowe — ADR-B-0634–0637”) – „sprawdzaj go z ADR 5.3.2.2.1, 5.3.2.2.2 i 5.3.2.3.1.” → „sprawdzaj go z ADR 5.3.2.1.1, 5.3.2.2.1, 5.3.2.2.2, 5.3.2.3.1 i 5.3.2.3.2.”; `podstawowy/instruktor/ADR-B-06.md` – „Podstawy do sprawdzenia: ADR 5.3.2.2.1, 5.3.2.2.2 i 5.3.2.3.1.” → „Podstawy do sprawdzenia: ADR 5.3.2.1.1, 5.3.2.2.1, 5.3.2.2.2, 5.3.2.3.1 i 5.3.2.3.2.” (nowe 0634 – 5.3.2.1.1; 0635, 0637 – 5.3.2.3.2). Pozostałe odwołania (lekcje 01, 05, 09; instruktor 05, 09; `praktyka/scenariusze-13-dzialow.json`) są tylko na listach pytań – tematy zgodne, bez zmian.
- Oczekiwany SHA banku: **8596a7a61cdc27c4f558af7197cdca9072090c4e → 6dc2b850f70d300ef3c214708b3283933934301c**.

## Test na kopii repo

`test_p43.sh` – git worktree `/tmp/b43` z main a158c1dc4 (bez commitów i pushu): `tools/apply_poprawki.py` z dopisanym `POPRAWKI-KONTROLA2-0631-0645.jsonl` → „Changed (15)”, blob **6dc2b850f70d300ef3c214708b3283933934301c**; synchronizacja (`sync_p43_test.py`); wszystkie **14 skryptów CI** – kod 0; `python3 -m unittest discover -s tests` – **Ran 241 tests – OK**.

## Specjaliści – pozycje do pakietu

- 0631 – czy użycie rękawic i ochrony oczu przed osłonięciem kratki to obowiązek, czy dobra praktyka.
- 0633 – kamizelka także w dzień (wzór nie rozróżnia pory dnia).
- 0636 – tablica z linią i bez linii na tej samej jednostce.
- 0640 – czy gaśnicę po użyciu (zerwana plomba) trzeba wymienić przed dalszą jazdą.
- 0642, 0643 – parametry RKO i AED według ERC 2025, nie według tekstu ADR (instruktor pierwszej pomocy).

## Licznik

Pozostało **135** pytań bez porównania dosłownego po obu kontrolach (0646–0780).