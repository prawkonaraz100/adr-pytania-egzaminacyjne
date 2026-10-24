# ADR podstawowy — aktualne pokrycie kursu

**Stan aktualny po etapie 4p: 24.10.2026.** Ramowy polski program to **13 tematów**, 18 godzin lekcyjnych teorii oraz wymagane ćwiczenia praktyczne (Dz.U. 2021 poz. 2150, załącznik nr 1). Nasza mapa 106 kompetencji to **wewnętrzny podział redakcyjny**, a nie urzędowy dokument z listą 106 wymagań.

## Co naprawdę zostało ukończone?

- **566 autorskich pytań** z A/B/C, wyjaśnieniem i wskazaniem podstawy; **566 needs_review / 0 verified**.
- **103/103 kompetencji teoretycznych** ma co najmniej jedno pytanie w wersji roboczej. **0/103** ma pytanie zatwierdzone przez niezależnego eksperta.
- **3/3 cele praktyczne** mają scenariusz w `podstawowy/praktyka/SCENARIUSZE.md`. To program ćwiczeń, **nie dowód odbycia zajęć**.
- **13/13 lekcji** ma szkic dydaktyczny, mapę konkretnych ID pytań i przykład praktyczny; wszystkie wymagają niezależnego odbioru.
- Rozkład prawidłowych opcji: A=189, B=191, C=186.
- Globalny wskaźnik „poprawna odpowiedź jest jedyną najdłuższą”: **71/566 = 12,54%**; wszystkie 13 działów są poniżej 18%.
- Wciąż **brakuje gotowych ilustracji** wszystkich wymaganych nalepek i tablic, przykładowych poprawnie wypełnionych dokumentów oraz raportu kontroli tekstu prawnego i wszystkich błędnych wariantów odpowiedzi.

**Ważne:** 100% pokrycia *tematycznego pytaniami roboczymi* **nie oznacza gotowego kursu ani certyfikatu ADR**. Dla wybranych kompetencji jedno pytanie nie wystarczy do skutecznej nauki; kolejnym zadaniem jest zwiększenie głębokości pokrycia i niezależna kontrola.

## Matryca gotowości

| Dział | Zakres | Pytaniami roboczymi / teoria | Cele praktyczne | Liczba pytań | Zweryfikowane | Materiał do nauki |
|---|---|---:|---:|---:|---:|---|
| ADR-B-01 | Podstawy i wyłączenia | 7/7 | 0 | 35 | 0 | Lekcja + mapa pytań |
| ADR-B-02 | Klasyfikacja i zagrożenia | 14/14 | 0 | 56 | 0 | Lekcja + mapa pytań |
| ADR-B-03 | Środowisko i odpady | 6/6 | 0 | 49 | 0 | Lekcja + mapa pytań |
| ADR-B-04 | Zapobieganie zagrożeniom | 6/6 | 0 | 44 | 0 | Lekcja + mapa pytań |
| ADR-B-05 | Awaria, pierwsza pomoc | 12/12 | 3 | 40 | 0 | Lekcja + mapa pytań |
| ADR-B-06 | Oznakowanie | 9/9 | 0 | 45 | 0 | Lekcja + mapa pytań |
| ADR-B-07 | Obowiązki uczestników | 6/6 | 0 | 43 | 0 | Lekcja + mapa pytań |
| ADR-B-08 | Wyposażenie | 8/8 | 0 | 40 | 0 | Lekcja + mapa pytań |
| ADR-B-09 | Załadunek i mocowanie | 9/9 | 0 | 46 | 0 | Lekcja + mapa pytań |
| ADR-B-10 | Przewóz kombinowany | 5/5 | 0 | 55 | 0 | Lekcja + mapa pytań |
| ADR-B-11 | Tunele | 7/7 | 0 | 35 | 0 | Lekcja + mapa pytań |
| ADR-B-12 | Ochrona (security) | 6/6 | 0 | 43 | 0 | Lekcja + mapa pytań |
| ADR-B-13 | Dokumentacja | 8/8 | 0 | 35 | 0 | Lekcja + mapa pytań |
| **Razem** | | **103/103** | **3** | **566** | **0** | **13 szkiców z mapą pytań** |

## Pogłębienie zagadnień po partii 007B

- Po partii 007A **20 z 103** celów teoretycznych miało tylko jeden szkic pytania. Partia 007B dodała do tych celów kolejne 20 pytań; **0/103** celów ma teraz mniej niż dwa.
- **103/103 celów teorii ma co najmniej dwa autorskie szkice**, przy czym wciąż **0/103** celów ma odpowiedź zatwierdzoną przez niezależnego eksperta ADR.
- Wszystkie **216 pytań są `needs_review`**, bez automatycznej zmiany statusu. Obecność dwóch zbliżonych pytań nie oznacza przetestowania całej kompetencji.
- [Audyt partii 007B](AUDYT-PARTIA-007B.md) obejmuje 20 nowych rekordów, korekty 4 wcześniejszych pytań oraz **4 pary podobieństwa językowego** do oceny przez redaktora.
- `scripts/similarity.py` służy tylko do informacyjnego rankingu podobieństw; nie rozpoznaje wszystkich parafraz, nie weryfikuje prawa i nie usuwa pytań.

## Dodatkowa kontrola aktualności prawa i gotowości publikacji (23.10.2026)

- Potwierdzono znaczenie umów wielostronnych ADR 1.5.1 w 2026 r. — patrz [rejestr wybranych odstępstw](ODSTEPSTWA-ADR-2026.md). Z tego powodu doprecyzowano pytania `ADR-B-0145` i `ADR-B-0198` o świadectwie dopuszczenia samochodu FL, które nie mogą bezwarunkowo dotyczyć naczepy przy stosowaniu M364.
- Zmieniono błędne warianty pięciu pytań, zgodnie z [audytem wydawniczym](AUDYT-WYDAWNICZY-2026.md).
- Dodano mechanizm eksportu tylko pytań z udokumentowaną recenzją, [review/README.md](../review/README.md). **0 zatwierdzeń**, więc egzamin próbny pozostaje niedostępny na tym zbiorze.
- 103/103 teoretycznych celów z dwoma pytaniami to wyłącznie robocze pokrycie, nie prawnomerytoryczny odbiór.

## Pierwsza partia audytu zgodności treści (23.10.2026)

- Wybrano 30 pytań o największym ryzyku błędów interpretacyjnych i sprawdzono warianty, źródła i wyjaśnienia: [raport](../review/batches/risk-001.md).
- **8 pytań poprawiono**, w szczególności nr 0073 (dwa możliwe poprawne warianty), 0139 (odrębny sposób dopuszczenia przewozu luzem przez szczególny punkt) i 0140 (wyjątek przy kontenerach-cysternach).
- 19 pytań nie wykazało sprzeczności w zakresie wstępnej kontroli, a 3 wymagają szczególnego sprawdzenia polskiego brzmienia/wyjątku. **0/30 uzyskało niezależne zatwierdzenie specjalisty; statusy pozostają needs_review.**
- Zestaw 103/103 kompetencji z minimum dwoma pytaniami **nie mówi nic o tym**, czy dane dwa pytania są poprawne lub niezależne znaczeniowo.

## Sekwencyjna kontrola całej bazy (23.10.2026)

- Przeprowadzono **pierwsze czytanie redakcyjne wszystkich 216 pytań po kolei**: A/B/C, klucz, wyjaśnienie, podane odniesienie do ADR. Rejestr i [raport](../review/sequential/RAPORT.md) obejmują 8 kolejnych bloków ID.
- **34 wpisy** z konkretną uwagą priorytetową, **25** z dodatkową kontrolą wybranego tematu/punktu z zewnętrznym źródłem.
- Poprawiono `0048` (niespójne odpowiedzi), `0099` i `0162` (nalepka 9A obejmuje odpowiednie baterie sodowo-jonowe w ADR 2025) oraz `0173` (wyraźne odesłania do szczególnego ustępu obok BK/VC).
- **Nie wykonano 216 indywidualnych porównań pełnego polskiego tekstu prawa ani niezależnej recenzji**. Liczba `verified` pozostaje 0, a publikacja zablokowana. Wynik pierwszego czytania nie stanowi certyfikacji prawnej.

## Indywidualna kontrola odpowiedzi pytań 0001–0060

- Zapisano **648 uzasadnień A/B/C dla wszystkich 216 pytań**, osobno dla każdej możliwości: [raport 001–060](../review/legal-clauses/RAPORT-001-060.md) i [raport 061–090](../review/legal-clauses/RAPORT-061-090.md).
- Skorygowano sześć pytań (0009, 0019, 0027, 0031, 0033, 0043). Test CI blokuje nieaktualne uzasadnienie po edycji pytania.
- To redakcyjne sprawdzenie podanych podstaw ADR 2025, a **nie pełne dosłowne porównanie każdej odpowiedzi z polskim aktem i nie niezależna recenzja specjalisty**. Cała baza przeszła etap analizy A/B/C; **pełna kontrola wiążącego polskiego tekstu i niezależne zatwierdzenia pozostają otwarte**. Nadal **0 `verified`**.

## Co musi być zrobione przed publikacją

1. **Kontrola jakości prawa:** dla wszystkich rekordów sprawdzić dokładne brzmienie aktu ADR 2025 w Dz.U. poz. 642 ze sprostowaniem poz. 1575, szczegółowe wyjątki oraz każdą prawidłową i błędną odpowiedź. Potwierdzenie przez rzeczywistego specjalistę ADR, z datą i identyfikatorem recenzenta.
2. **Dopracowanie materiału:** poprawić nadmiernie podobne pytania, dopisać scenariusze trudniejszych sytuacji, sprawdzić czy każda kompetencja ma **wystarczającą** liczbę pytań, a nie tylko jedno.
3. **Grafiki i dokumenty:** własne lub legalnie pozyskane wzory nalepek i tablic; materiały do rozpoznawania klas, opakowań, kodów i ograniczeń; wzorcowe opisy UN i dokumenty przewozowe.
4. **Praktyka:** zatwierdzenie 3 scenariuszy przez instruktora, rzeczywista realizacja ćwiczeń i odrębne potwierdzenie obecności i umiejętności. Quiz nie zalicza praktyki.
5. **Tryb egzaminu:** generator 30 pytań / 60 minut / próg 20 prawidłowych — wyłącznie ze zweryfikowanych rekordów, po sprawdzeniu jakości losowania, dostępności i powtórek.
6. **Odbiór końcowy:** ponowna weryfikacja każdej z 13 lekcji z aktualnymi źródłami i korektami legislacyjnymi oraz potwierdzony PASS wymaganego CI.

## Narzędzia kontroli

- `python scripts/validate.py` — format rekordów JSONL, unikalne ID, odpowiedzi A/B/C, metadane, rozkład kluczy.
- `python scripts/coverage.py` — powiązanie pytań z kompetencjami, 13 działów i obecność 13 plików lekcji, z rozdzieleniem `draft` i `verified`.
- `python -m unittest discover -s tests -v` — testy automatyczne.
- `docs/AUDYT-PARTIA-007B.md` — przegląd nowych pytań, ryzyk źródłowych i podobieństw; wcześniejsze audyty pozostają w repozytorium.
- `python scripts/similarity.py --threshold 0.45 --limit 15` — informacyjny ranking par do ręcznego przeglądu.

## Status szkolenia praktycznego

Scenariusze: [SCENARIUSZE.md](../podstawowy/praktyka/SCENARIUSZE.md). Trzy wymagane obszary: gaśnica, pierwsza pomoc i działania po awarii/wypadku. Przygotowany materiał jest wyłącznie pomocą dla instruktora. Nie wystawia zaświadczenia ani nie zastępuje zorganizowanych zajęć.

## Dokumenty nadrzędne

- [Program kursu (Dz.U. 2021 poz. 2150)](https://eli.gov.pl/api/acts/DU/2021/2150/text.pdf)
- [Egzaminy ADR (Dz.U. 2024 poz. 964)](https://eli.gov.pl/api/acts/DU/2024/964/text.html)
- [ADR 2025 ogłoszone w Dz.U. poz. 642](https://dziennikustaw.gov.pl/DU/2025/642)
- [Sprostowanie Dz.U. 2025 poz. 1575](https://eli.gov.pl/eli/DU/2025/1575/ogl/pol/pdf)

## Etap 2 — analiza rzeczywistej głębokości (23.10.2026, po kartach 0001–0216)

**Analiza na podstawie rzeczywistych plików** `podstawowy/questions.jsonl`, `podstawowy/kompetencje.json` oraz roboczych celów redakcyjnych z `PROGRAM-PODSTAWOWY.md`. Dotychczasowe 216 kart w `review/legal-detail/` to **wstępne przeglądy oparte na wcześniejszych analizach, a nie pełna weryfikacja polskich przepisów**.

**Wynik:** 216 pytań, wszystkie `needs_review`; **103/103** celów teorii ma minimum dwa robocze szkice, ale **96/103 ma dokładnie dwa**, tylko **7/103 trzy lub więcej**. Brak pytania w sensie liczbowym dla któregoś z tych 103 celów: **0**. Praktyka: trzy cele wymagające wykonania ćwiczeń, nie quizu. Pola `image` z niepustą wartością: **0/216**. Kwoty do 400 pozostają wyłącznie planem redakcyjnym, nie nakazem prawa.

| Dział | Pytania teraz | Cele teorii | Cele z dokładnie 2 pytaniami | Orientacyjny cel projektu | Różnica do celu* |
|---|---:|---:|---:|---:|---:|
| ADR-B-01 | 14 | 7 | 6 | 30 | 16 |
| ADR-B-02 | 28 | 14 | 14 | 40 | 12 |
| ADR-B-03 | 12 | 6 | 6 | 20 | 8 |
| ADR-B-04 | 12 | 6 | 6 | 25 | 13 |
| ADR-B-05 | 26 | 12 | 11 | 35 | 9 |
| ADR-B-06 | 18 | 9 | 9 | 45 | 27 |
| ADR-B-07 | 13 | 6 | 5 | 35 | 22 |
| ADR-B-08 | 17 | 8 | 7 | 40 | 23 |
| ADR-B-09 | 19 | 9 | 8 | 45 | 26 |
| ADR-B-10 | 13 | 5 | 4 | 15 | 2 |
| ADR-B-11 | 16 | 7 | 6 | 25 | 9 |
| ADR-B-12 | 12 | 6 | 6 | 20 | 8 |
| ADR-B-13 | 16 | 8 | 8 | 25 | 9 |
| **Razem** | **216** | **103** | **96** | **400** | **184** |

*Różnica do planistycznego celu 400 nie jest liczbą brakujących urzędowych zagadnień ani poleceniem mechanicznego dopisania 184 rekordów. Należy rozszerzać bank dopiero po wyborze konkretnych braków umiejętności: wykorzystanie prawa w scenariuszu, dokumenty i oznakowanie, decyzja kierowcy w warunkach wyjątków, rozróżnianie podobnych pojęć; ograniczać parafrazy pytań istniejących.*

### Priorytet redakcyjny po kontroli 13 działów

1. **ADR-B-06 i ADR-B-02:** brak grafik; przygotować własne schematy nalepek, tablic i sytuacyjne rozpoznawanie oznakowania. Zanim dodamy pytania obrazkowe, zweryfikować autentyczność znaku i prawa do grafiki.
2. **ADR-B-08, ADR-B-09, ADR-B-11 i ADR-B-13:** ćwiczenia rozpoznawania wyposażenia, kontroli przed załadunkiem, kodów tuneli i interpretacji dokumentu z granicznymi warunkami.
3. **ADR-B-01, ADR-B-03, ADR-B-10, ADR-B-12:** wyjątki, odpady, przewóz kombinowany i ochrona przed nadużyciem; kontrolować warunki stosowania 1.1.3, 1.10 oraz właściwych punktów, zanim ustali się klucz.
4. **ADR-B-05:** przejść od pytań pamięciowych do bezpiecznych scenariuszy wypadkowych, zachowując niezastępowalność rzeczywistych trzech ćwiczeń.
5. **ADR-B-04 i ADR-B-07:** scenariusze decyzji kierowcy i odróżniania obowiązków uczestników.

**Zależność przed dopisywaniem**: każde nowe pytanie wymaga własnego źródła, wariantów A/B/C, jednoznaczności, odrębnego sprawdzenia wyjątku i odniesienia do kompetencji; istniejący skrypt `check_legal_clause_review.py` ma aktualnie zakres 216 i przy rozbudowie należy go rozszerzyć razem z audytem oraz testami, a nie wyłączać. Nie podnosić `verified` i nie eksportować banku przed podpisaną fachową recenzją. Żadnych pytań z kursu cystern.

## Aktualizacja po etapach 4o i uzupełnieniu pokrycia (24.10.2026)

- Bank podstawowy: **566 pytań**, wszystkie `needs_review`, **0 verified**. Etap 4o rozbudował wszystkie 90 wyjaśnień krótszych niż 300 znaków; aktualna kontrola wykazała 0 takich wyjaśnień.
- Wewnętrzna mapa obejmuje 106 kompetencji (103 teoria, 3 praktyczne); wszystkie 103 cele teoretyczne mają przypisane pytania robocze, a każde pytanie ma mapowanie. To nie oznacza niezależnego zatwierdzenia ani pełnej głębokości wszystkich wyjątków.
- Raport pogłębienia luk: [RAPORT-LUK-POKRYCIA-ADR-PODSTAWOWY-2026-10-24.md](RAPORT-LUK-POKRYCIA-ADR-PODSTAWOWY-2026-10-24.md). Dział B-06 osiągnął 45 pytań, B-08 40, a B-09 ma 46. Kwoty są wewnętrznym planem, nie wymogiem prawa.
- Wszystkie 13 lekcji otrzymało kartę powtórkową dla kursanta z typowymi błędami i powiązanymi pytaniami. To redakcyjne dopracowanie, nie odbiór eksperta.
- `podstawowy/praktyka/SCENARIUSZE.md` zawiera dopracowany protokół instruktora, kryteria obserwacji i formularz P1–P3. Formularz wolno uzupełnić tylko podczas rzeczywistych zajęć; quiz nie potwierdza wykonania praktyki.
- Otwarta pozostaje niezależna recenzja ADR, dosłowne porównanie polskiego tekstu urzędowego ze sprostowaniem oraz odbiór lekcji i ćwiczeń przez instruktora. Nie nadano statusu `verified`.


## Aktualny stan po etapie 4p (24.10.2026)

- HEAD po scaleniu generatora i testu powtarzalności: `4ebdf594bbd7bb8e8cf93eb227745b91faa1b0b9`.
- Egzamin próbny: [wariant 001](../podstawowy/egzamin-probny/wariant-001.json), [oddzielny klucz](../podstawowy/egzamin-probny/klucz-001.json), [instrukcja generatora](../podstawowy/egzamin-probny/README.md). To trening wewnętrzny, nie oficjalny arkusz; źródłowe pytania są niezatwierdzone.
- Generator `scripts/draft_mock_exam.py` dobiera 30 pytań proporcjonalnie do liczebności 13 działów, 60 minut, próg 20/30. Quality Gate sprawdza ID i zgodność klucza oraz odtwarzanie wariantu seedem.
- Dodatkowy test potwierdza, że wszystkie ID jawnie zapisane w mapach 13 lekcji istnieją w banku.
- Długość odpowiedzi: 71/566 (12,54%) globalnie; B-01 17,1%, B-02 12,5%, B-03 12,2%, B-04 11,4%, B-05 15,0%, B-06 8,9%, B-07 7,0%, B-08 17,5%, B-09 10,9%, B-10 7,3%, B-11 17,1%, B-12 14,0%, B-13 17,1%.
- Nadal **0 verified**. Weryfikacja pełnego polskiego tekstu ADR 2025 wraz ze sprostowaniem i niezależna recenzja A/B/C pozostają otwarte. Nie traktować egzaminu próbnego jako prawnie zatwierdzonego.

## Aktualizacja etapu 4t — odpowiedzialność cywilna (25.10.2026)

Audyt szczegółowy: [`podstawowy/raporty/etap-4t-pokrycie-programu-2026-10-25.md`](../podstawowy/raporty/etap-4t-pokrycie-programu-2026-10-25.md). Dodano kompetencję ADR-B-07-K07 i pytania ADR-B-0567–0569, aby wyodrębnić temat ogólnej odpowiedzialności cywilnej wskazany w ADR 8.2.2.3.2(k). Bank ma 569 pytań; wszystkie pozostają `needs_review`, zero `verified`. Próg co najmniej 3 pytań na kompetencję jest roboczy, a nie prawny. Audyt nie poświadcza pełnej różnorodności typów pytań ani prawnej poprawności; wymagane pozostają niezależna recenzja i kontrola polskiego tekstu urzędowego.

## Etap 4t — przegląd lekcji 01–04 (25.10.2026)

W [raporcie lekcji 01–04](../podstawowy/raporty/etap-4t-lekcje-01-04-2026-10-25.md) opisano potwierdzone braki wprowadzenia dla początkującego, objaśnienia skrótów i podsumowania końcowego. Dodano wprowadzenia „Po co to jest?” z przykładem kierowcy oraz sekcje „Co musisz zapamiętać” do ADR-B-01–04. Zmiany są redakcyjne; nie zmieniono pytań ani statusów prawnych. Kolejne lekcje pozostają do przeglądu.

## Etap 4t — przegląd lekcji 05–08 (25.10.2026)

W [raporcie lekcji 05–08](../podstawowy/raporty/etap-4t-lekcje-05-08-2026-10-25.md) udokumentowano brak prostego wprowadzenia i podsumowania końcowego w czterech lekcjach oraz brak objaśnienia skrótu DMC na początku ADR-B-08. Dodano wprowadzenia, przykłady kierowcy i końcowe podsumowania. ADR-B-07 uzupełniono o ogólną odpowiedzialność cywilną, z odsyłaczem do pytań 0567–0569; to materiał roboczy, nie zatwierdzenie prawne. Wszystkie pytania pozostają `needs_review`.

## Etap 4t — przegląd lekcji 09–13 (25.10.2026)

W [raporcie lekcji 09–13](../podstawowy/raporty/etap-4t-lekcje-09-13-2026-10-25.md) odnotowano brak prostego wprowadzenia i podsumowania końcowego w lekcjach 09–13 oraz skróty RID, IMDG, ICAO, LQ i UN wymagające rozwinięcia przy pierwszym objaśnieniu. Dodano krótkie wprowadzenia z przykładami kierowcy, objaśnienia skrótów i listy „Co musisz zapamiętać”. Nie zmieniono banku pytań ani statusów prawnych.
