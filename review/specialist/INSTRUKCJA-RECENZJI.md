# Instrukcja niezależnej recenzji banku ADR podstawowego — stan aktualny 26.10.2026

**Cel:** weryfikacja każdego z 609 pytań osobno — treści, klucza, odpowiedzi A/B/C, wyjaśnienia i wszystkich wyjątków — przez rzeczywistego specjalistę ADR. Stan: 609 `needs_review`, 0 `verified`, 0 formalnych zatwierdzeń. **Nie publikować banku ani egzaminu próbnego opartego na potrzebujących recenzji pytaniach.**

## Materiały wejściowe

Bieżący snapshot po etapie 4x29: 609 pytań `needs_review`, 0 `verified`, 0 formalnych zatwierdzeń; bank blob SHA `99c06e736c0e5812e97d4ff02567dbf741629434`. Najnowszy raport próbki i synchronizacji: [Etap 4x29](../../podstawowy/raporty/etap-4x29-proba-wyjasnien-i-egzaminy-2026-10-26.md). Egzaminy 001–005 są wyłącznie materiałami treningowymi, a klucze porównano z bankiem z uwzględnieniem zmiany liter przy przestawieniu opcji.

1. Pełny indeks [aktualny wykaz pytań 0001–0609](REJESTR-AKTUALNY-0001-0609.md), manifest [PAKIET-0609-MANIFEST.json](PAKIET-0609-MANIFEST.json), oryginalne rekordy w `podstawowy/questions.jsonl`.
2. Urzędowe polskie ADR 2025 — [Dz.U. 2025 poz. 642](https://dziennikustaw.gov.pl/DU/2025/642) oraz [sprostowanie poz. 1575](https://eli.gov.pl/eli/DU/2025/1575/ogl); program kursu [Dz.U. 2021 poz. 2150](https://eli.gov.pl/eli/DU/2021/2150/ogl).
3. Audyty redakcyjne `review/sequential/`, analizy wariantów `review/legal-clauses/`, raporty `review/batches/`, matryca `podstawowy/kompetencje.json`, materiały 13 lekcji i `podstawowy/praktyka/SCENARIUSZE.md`.
4. Procedura zatwierdzania: `review/README.md` i skrypt `scripts/release_gate.py`.
5. Egzaminy próbne: `podstawowy/egzamin-probny/wariant-001.json`–`wariant-005.json` i odpowiadające im `klucz-001.json`–`klucz-005.json`; kontrola synchronizacji i biasu: `scripts/check_mock_exam_variants.py`.
6. Lista wrażliwości na przyszłą edycję: `review/specialist/ETAP-4X9-ADR-2027-LISTA-KONTROLNA.md`.

## Kolejność pracy recenzenta

- Potwierdź **rzeczywistą tożsamość i kompetencję recenzenta** (nie twórz fikcyjnych nazwisk ani dat).
- Zapisz SHA aktualnej wersji `questions.jsonl` i SHA HEAD repo. Pracuj na tej konkretnej migawce. Nie traktuj poprzednich audytów jako wiążącego potwierdzenia.
- Dla każdego ID sprawdź **obowiązujące brzmienie urzędowego polskiego ADR 2025**, korektę i ewentualne właściwe odstępstwa wielostronne. Oceń zakres, jednostki miary, rodzaj przewozu, wyłączenia oraz wyjątki dla roku i kraju.
- Osobno dla A, B i C podaj, dlaczego wariant jest prawdziwy albo fałszywy w opisanych warunkach. Sprawdź, czy **dokładnie jedna** odpowiedź jest bezspornie poprawna, czy pytanie nie sugeruje zbyt szerokiego zwolnienia.
- Oceń jasność języka dla kierowcy, brak dwuznaczności, poprawność opisu klas, zagrożeń i nalepkowania, odpowiedniość do kursu podstawowego (bez specjalistycznej obsługi cystern).
- Zapisz wynik: `zaakceptuj / wymaga korekty / blokuj / nie rozstrzygnięto`; wskaż dokładny punkt, fragment wymagający korekty i uzasadnienie. Dokumentację zgromadź w formularzu, nie w polu `verified` na podstawie automatycznego przeglądu.
- Po rzeczywistej pozytywnej akceptacji zastosuj **oddzielną** kontrolowaną procedurę `review/README.md` i bramkę wersjonującą SHA-256; żaden krok w tej partii nie wpisuje `approvals.jsonl` ani `verified`.

## Zakres audytów i ryzyka

- `review/batches/coverage-001-502.md`: **106 wewnętrznych kompetencji**, w tym 103 teoretyczne i 3 praktyczne (te ostatnie nie są egzaminem internetowym). Rozkład modułów i kompletność powiązań należy sprawdzać ponownie na aktualnym HEAD.
- `review/batches/semantic-001-502.md`: wstępny screening *leksykalny*, nie pełny model semantyczny. Przeredagowane potwierdzone zbieżności: `review/batches/semantic-fixes-0241-0278-0324.md`. Sprawdź na nowo wątpliwe parafrazy i treść raportów historycznych.
- Przy lekcjach 01–13 oceń poprawność materiałów oraz dopasowanie do urzędowego zakresu i czasu trwania. Nie uznawaj scenariusza ćwiczeń za dowód odbycia rzeczywistych zajęć.
- Każdy nierozstrzygnięty przypadek oznacz **niezaakceptowany**, nie `verified`; unikaj automatycznych decyzji bez bezpośredniego odczytu obowiązującego polskiego aktu.

## Wynik recenzji

Recenzent przekazuje formularz z polami: ID, data kontroli, recenzent, źródło z jednostką redakcyjną, ocena A/B/C, wyjątki, wynik, szczegółowe uwagi, proponowane zmiany i podpis / wiarygodne potwierdzenie. Formularz [wzór uwag](FORMULARZ-UWAG.md). Redaktor nanosi tylko potwierdzone poprawki, aktualizuje wszystkie migawki audytu w `review/sequential/` i `review/legal-clauses/`, uruchamia Quality Gate i przeprowadza ponowną recenzję zmienionych pytań. Brak wpisów akceptacji nadal blokuje publikację.


## Aktualizacja 4l po 4h–4k

- Zamrożony zakres tej partii: **ADR-B-0001–0542**. Dokumenty 0520–0542: `review/sequential/520-525.json`, `526-533.json`, `534-538.json`, `539-540.json`, `541-542.json` i odpowiadające pliki `review/legal-clauses/`. Przy recenzji sprawdź warianty każdej litery *obecnego* stanu, nie poprzednich migawek.
- **P1:** 23 nowe pozycje ADR-B-0520–0542. Wszystkie zawierają robocze przepisy, żadne nie ma potwierdzonego dosłownego porównania z urzędowym polskim PDF i sprostowaniem. Prioritet: 0520–0538 dokumentacja, szkolenie i LQ/EQ; 0539–0540 tunele; 0541–0542 nalepki i autorskie SVG.
- **P2:** 519 starszych pozycji nadal z otwartymi zagadnieniami prawnej weryfikacji. Każdą korektę przenoś do jej migawki oraz do nowego bieżącego indeksu.
- **Grafiki:** dla każdego niepustego `image` porównaj dokładny rysunek i semantykę pytania z konkretnym wzorem ADR 2025; zweryfikuj autora/licencję, tekst alternatywny i dostępność. Samo `image` nie jest dowodem wykonanej recenzji.
- **Literalny rejestr:** `review/legal-polish/stage4k-literal-verification-ledger-0001-0542.json` zawiera faktycznie nieporównane pozycje; angielska publikacja UNECE ani pomocniczy tekst MI nie są dowodem odczytu urzędowej strony PDF. Zapisz stronę/tom, jednostkę redakcyjną, wynik sprostowania, wyjątki oraz osobną ocenę A/B/C.
- **Egzamin próbny:** `scripts/mock_exam.py` musi pozostać fail-closed. Rekord `needs_review` (nawet z grafiką) jest niedopuszczony do losowania i publicznej publikacji. Testy syntetyczne wyłącznie w katalogach tymczasowych.
- Raport przekazania i gotowości: `review/batches/stage4l-readiness-0542.md`. Żadnego `verified` bez indywidualnego prawdziwego protokołu.


## Aktualny zakres odbioru dydaktycznego — 4x6

- **Bank:** 609 rekordów, wszystkie `needs_review`, 0 `verified`.
- **Lekcje:** `podstawowy/lekcje/ADR-B-01.md` … `ADR-B-13.md`.
- **Materiały instruktora:** `podstawowy/instruktor/ADR-B-01.md` … `ADR-B-13.md`.
- **Scenariusze:** 39 wpisów, po trzy na dział, w `podstawowy/praktyka/scenariusze-13-dzialow.json` i przewodniku `podstawowy/praktyka/SCENARIUSZE.md`.
- **Egzaminy próbne:** `podstawowy/egzamin-probny/wariant-001.json` … `wariant-005.json` oraz odpowiadające im `klucz-001.json` … `klucz-005.json`. Wszystkie są treningowe i mają pozostać niezatwierdzone.
- **Kontrola spójności:** Quality Gate sprawdza, czy każda lekcja i instrukcja zawiera odwołania do wszystkich trzech scenariuszy swojego działu, a wszystkie identyfikatory pytań istnieją w banku i należą do właściwego modułu. To kontrola strukturalna, nie potwierdzenie poprawności prawnej.

Przed recenzją specjalista ma zapisać commit SHA i pracować na jednej migawce. Dla każdego pytania sprawdzić treść, trzy odpowiedzi, explanation dla początkującego kierowcy, podstawę prawną i zakres kursu. Osobno sprawdzić, czy trzy scenariusze działu są spójne z lekcją i pytaniami oraz czy wszystkie warianty egzaminu i klucze są zgodne z tą samą migawką banku. Nie ustawiać `verified` na podstawie samego przejścia testów automatycznych.


## Uzupełnienie procedury — etap 4x18

- Migawka banku po redakcji dystraktorów: 609 rekordów, SHA blob `ec1bb5391aa9875e2a1aa7bdb138fb79b3bf72dd`; arkusze 001–005 i klucze mają wskazywać dokładnie tę migawkę.
- Priorytetowe rekordy do ponownego odczytu: ADR-B-0073, 0074, 0253, 0283, 0420, 0422, 0484 (wyposażenie i kontrole) oraz ADR-B-0144, 0249, 0274, 0275, 0300, 0304, 0305 (postój, identyfikacja, ochrona i szkolenia). Sprawdź szczególnie zakres stosowania wymogu, warunki i wyjątki — nie tylko numer punktu.
- Rejestry pytań wrażliwych na edycję ADR 2027 są w `podstawowy/raporty/etap-4x9-wrazliwosc-01-04.json`, `...-05-08.json`, `...-09-13.json`. Są to flagi do kontroli, nie stwierdzenie, że przepisy się zmieniły.
- Status `verified` nadaje wyłącznie specjalista po rzeczywistej recenzji. Wymagane są źródło urzędowe i sprostowanie, analiza A/B/C, warunki i wyjątki, data oraz prawdziwa tożsamość recenzenta zgodnie z procedurą repo. Nie przenoś statusu z poprzedniej migawki na nowy rekord bez ponownego sprawdzenia.


## Aktualizacja pakietu po etapach 4x25–4x29

- **4x25:** przejrzano bank redakcyjnie; dodatkowa korekta językowa dotyczyła ADR-B-0197. Bez zmian statusów prawnych.
- **4x26:** zsynchronizowano 13 lekcji, 13 materiałów instruktora, 39 scenariuszy i pięć wariantów egzaminu.
- **4x27:** usunięto powtarzające się odsyłacze redakcyjne; bank i odpowiedzi bez zmian.
- **4x28:** potwierdzono pokrycie ID lekcji/banku, powiązania 39 scenariuszy oraz unikalność 90 kotwic słowniczka; w próbce 60 explanation nie znaleziono potwierdzonego przypadku do przepisania.
- **4x29:** druga próbka 60 nowych explanation (ziarno `4292026`) nie wykazała potwierdzonego przypadku wymagającego przepisania. Warianty i klucze 001–005 zgodne z aktualnym bankiem po uwzględnieniu przestawiania liter.
- **Dowody do recenzji:** [121 pozycji bez zapisanego dosłownego fragmentu MI](ETAP-4X24-POZYCJE-BEZ-CYTATU-MI.md); odrębnie 376 porównań z pełnym polskim tekstem urzędowym pozostaje nierozstrzygniętych, a 10 rekordów wymaga dokończenia porównania. Te kategorie nie są zamienne.

Kontrola redakcyjna, spójność plików ani PASS CI nie stanowią potwierdzenia poprawności prawnej. Wszystkie 609 pytań pozostają `needs_review`.


## Aktualizacja bieżącej migawki — etap 4x31

Bank ma nowy blob SHA `99c06e736c0e5812e97d4ff02567dbf741629434` po pojedynczej korekcie redakcyjnej explanation ADR-B-0540. Warianty i klucze 001–005 wskazują ten SHA. Nie zmieniono stemu, opcji, poprawnej litery ani statusu `needs_review`. Test CI sprawdza 2–5 zdań oraz maksymalnie 35 słów na zdanie, z ochroną typowych skrótów (np. „m.in.”) przed fałszywym podziałem.


## Aktualizacja przeglądu redakcyjnego — etapy 4x30–4x39 (26.10.2026)

- Etapy 4x30–4x38: przegląd zmian w dystraktorach, duplikatach, podpowiedziach leksykalnych i wyjaśnieniach; lista zmian znajduje się w raportach etapów 4x32 i 4x34–4x38 w `podstawowy/raporty/`.
- Etap 4x39: ręczny przegląd 50 explanation (zmienione pytania z 4x30–4x38 i ADR-B-0586–0609). Nie znaleziono potwierdzonego problemu językowego wymagającego zmiany; ADR-B-0479 to fałszywy alarm prostej heurystyki.
- Warianty/klucze 001–005 wskazują bieżący bank SHA `8a16afb47c5d5a9e460092b7e474b4a3e8a5a8d9`; statusy 609 `needs_review`, 0 `verified`.
- Raport: `podstawowy/raporty/etap-4x39-przeglad-explanation-i-synchronizacja-2026-10-26.md`.

Kontrola nie jest formalną weryfikacją prawną i nie upoważnia do publikacji egzaminu.


## Priorytety otwartej recenzji — etap 4x40

Najpierw można przejrzeć 20 rekordów z `review/specialist/KOLEJKA-PRIORYTETOWA-4X40.json`. Kolejka została uszeregowana na podstawie sygnałów z treści (liczby/progi, wyjątki, sprzęt/dokumenty, klasy ryzyka, tunele), a nie na podstawie ustalenia błędu prawnego. Dla każdego rekordu trzeba niezależnie porównać treść z oficjalnym polskim tekstem Dz.U. 2025 poz. 642 i sprostowaniem poz. 1575, zapisać cytat oraz stronę i ocenić A/B/C. Nie kontynuować prób wydobywania cytatów z MI/PDF. Nie zmieniać statusu `needs_review` bez formalnego protokołu.



## Integralność kolejki 4x40 — kontrola CI

Quality Gate sprawdza, czy 20 pozycji kolejki istnieje w banku i na liście rekordów bez cytatu MI, czy ich dział/pytanie/podstawa odpowiadają aktualnemu bankowi, czy snapshot SHA jest aktualny i czy wszystkie statusy pozostają `needs_review`. Kolejka nadal jest tylko priorytetyzacją, nie oceną poprawności prawnej.
