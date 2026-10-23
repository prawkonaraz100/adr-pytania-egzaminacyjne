# ADR podstawowy — aktualne pokrycie kursu

**Stan roboczy: 22.10.2026.** Ramowy polski program to **13 tematów**, 18 godzin lekcyjnych teorii oraz wymagane ćwiczenia praktyczne (Dz.U. 2021 poz. 2150, załącznik nr 1). Nasza mapa 106 kompetencji to **wewnętrzny podział redakcyjny**, a nie urzędowy dokument z listą 106 wymagań.

## Co naprawdę zostało ukończone?

- **216 autorskich pytań** z A/B/C, własnym wyjaśnieniem i referencją do przepisu; **216 needs_review / 0 verified**.
- **103/103 kompetencji teoretycznych** ma co najmniej jedno pytanie w wersji roboczej. **0/103** ma pytanie zatwierdzone przez niezależnego eksperta.
- **3/3 cele praktyczne** mają scenariusz w `podstawowy/praktyka/SCENARIUSZE.md`. To program ćwiczeń, **nie dowód odbycia zajęć**.
- **13/13 lekcji ma szkic dydaktyczny** w `podstawowy/lekcje/`. Żadna nie ma jeszcze potwierdzonego odbioru eksperta.
- Rozkład prawidłowych opcji: A=72, B=74, C=70.
- Wciąż **brakuje gotowych ilustracji** wszystkich wymaganych nalepek i tablic, przykładowych poprawnie wypełnionych dokumentów oraz raportu kontroli tekstu prawnego i wszystkich błędnych wariantów odpowiedzi.

**Ważne:** 100% pokrycia *tematycznego pytaniami roboczymi* **nie oznacza gotowego kursu ani certyfikatu ADR**. Dla wybranych kompetencji jedno pytanie nie wystarczy do skutecznej nauki; kolejnym zadaniem jest zwiększenie głębokości pokrycia i niezależna kontrola.

## Matryca gotowości

| Dział | Zakres | Pytaniami roboczymi / teoria | Cele praktyczne | Liczba pytań | Zweryfikowane | Materiał do nauki |
|---|---|---:|---:|---:|---:|---|
| ADR-B-01 | Podstawy i wyłączenia | 7/7 | 0 | 14 | 0 | Szkic lekcji |
| ADR-B-02 | Klasyfikacja i zagrożenia | 14/14 | 0 | 28 | 0 | Szkic lekcji |
| ADR-B-03 | Środowisko i odpady | 6/6 | 0 | 12 | 0 | Szkic lekcji |
| ADR-B-04 | Zapobieganie zagrożeniom | 6/6 | 0 | 12 | 0 | Szkic lekcji |
| ADR-B-05 | Awaria, pierwsza pomoc | 12/12 | 3 | 26 | 0 | Szkic lekcji |
| ADR-B-06 | Oznakowanie | 9/9 | 0 | 18 | 0 | Szkic lekcji |
| ADR-B-07 | Obowiązki uczestników | 6/6 | 0 | 13 | 0 | Szkic lekcji |
| ADR-B-08 | Wyposażenie | 8/8 | 0 | 17 | 0 | Szkic lekcji |
| ADR-B-09 | Załadunek i mocowanie | 9/9 | 0 | 19 | 0 | Szkic lekcji |
| ADR-B-10 | Przewóz kombinowany | 5/5 | 0 | 13 | 0 | Szkic lekcji |
| ADR-B-11 | Tunele | 7/7 | 0 | 16 | 0 | Szkic lekcji |
| ADR-B-12 | Ochrona (security) | 6/6 | 0 | 12 | 0 | Szkic lekcji |
| ADR-B-13 | Dokumentacja | 8/8 | 0 | 16 | 0 | Szkic lekcji |
| **Razem** | | **103/103** | **3** | **216** | **0** | **13 szkiców** |

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

- Zapisano **360 uzasadnień A/B/C dla pierwszych 120 pytań**, osobno dla każdej możliwości: [raport 001–060](../review/legal-clauses/RAPORT-001-060.md) i [raport 061–090](../review/legal-clauses/RAPORT-061-090.md).
- Skorygowano sześć pytań (0009, 0019, 0027, 0031, 0033, 0043). Test CI blokuje nieaktualne uzasadnienie po edycji pytania.
- To redakcyjne sprawdzenie podanych podstaw ADR 2025, a **nie pełne dosłowne porównanie każdej odpowiedzi z polskim aktem i nie niezależna recenzja specjalisty**. Pozostałe 96 pytań czeka na analogiczny przegląd A/B/C. Nadal **0 `verified`**.

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
