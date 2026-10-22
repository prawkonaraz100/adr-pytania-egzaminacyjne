# Status i dziennik decyzji

## 2026-10-22 — start projektu

- Repozytorium: prawkonaraz100/adr-pytania-egzaminacyjne (publiczne, decyzja właściciela).
- Zakres aktywny: polski kurs ADR **początkowy podstawowy**, pytania autorskie i objaśnienia.
- Kolejny zakres: ADR **specjalistyczny — cysterny**; nie zaczynamy, zanim podstawa nie przejdzie przeglądu jakości.
- Oficjalny program: 13 pozycji a–m, 18 godzin lekcyjnych teorii, oddzielne ćwiczenia praktyczne.
- Egzamin państwowy: pisemny, 30 pytań / 3 odpowiedzi / 60 minut / próg 20 poprawnych.
- Stan banku pytań po inicjalizacji: **0 zweryfikowanych**, 0 gotowych do publikacji.
- Kwota 400 pytań: **robocza propozycja planistyczna**, nie obowiązek prawny.
- Pełna urzędowa baza pytań: **brak potwierdzenia publicznego udostępnienia**.
- Polityka treści: osobno wymagana walidacja strukturalna, prawna i redakcyjna.
- Przepisy główne: ADR 2025 + prawo polskie. Dla szczegółowych pytań stosować konkretne źródła i datę sprawdzenia.

## Jak aktualizować ten plik

Każdy ukończony etap wpisywać z datą, identyfikatorem commita, dokładnymi wynikami walidacji i CI. Nie oznaczać prac jako DONE bez potwierdzonego wyniku. Zapis zmian decyzji zachowywać, nie nadpisywać historii.

## 2026-10-22 — etap 1 / partia 001

- **Zapisano mapę przepisów** 13 tematów w `docs/MAPA-PUNKTOW-ADR-2025.md` (commit `7e0249849de848125128284328f35f61e4a4f9b8`).
- **Zapisano 39 autorskich pytań**, po 3 na każdy temat, w `podstawowy/questions.jsonl` (commit `96e7c9b98e9a5a141d207a4891031b6929b6e2ec`).
- Wszystkie 39 rekordów: `needs_review`. W szczególności **0 verified**, 0 zwolnionych do publikacji.
- Przeprowadzono kontrolę spójności JSONL przez odczyt pliku z GitHub i walidację struktury w kodzie pomocniczym: 39 rekordów, 13 modułów, po 3 pytania, unikalne identyfikatory, 3 odpowiedzi, poprawny klucz, metadane źródeł: 0 usterek w tym przeglądzie.
- **Niepotwierdzony CI PASS** i brak eksperckiej recenzji prawnomerytorycznej. GitHub Actions ma konfigurację, ale wynik jej uruchomienia nie został w tym kroku odczytany.
- Pytania uwzględniają punkty referencyjne ADR 2025; każdy podpunkt i wyjątek wymagają końcowej lektury pełnego tekstu Dz.U. 2025 poz. 642, a także sprawdzenia sprostowań.
- Podstawa prawna ADR 2025 ogłoszona w **Dz.U. 2025 poz. 642** została dodana do mapy — to ważniejsze źródło niż pomocnicze pliki na stronie MI.
- Bieżące zadania: #1 dokończenie mapy i weryfikacja pełnych ustępów, #2 audyt partii 001.
- Kurs cysterny: nadal **NIE ROZPOCZĘTO**.

**Następny wymagany krok:** pełna kontrola 39 pytań z dokładnym brzmieniem ADR 2025, rozstrzygnięcie wyjątków i niezależna recenzja fachowa; następnie walidator Python i potwierdzony wynik CI.

## 2026-10-22 — kontrola techniczna partii 001 (PR #3)

- Raport QA: `docs/QA-PARTIA-001.md`, PR #3 **merged** jako `125133b21437c1dd913232b7bd6149cabe974772`.
- GitHub Actions: [Quality Gate run #14](https://github.com/prawkonaraz100/adr-pytania-egzaminacyjne/actions/runs/39828372547), wynik **success** dla commita PR `e90bab7b4b79f549f509231a4b373055cd509628`.
- Kroki tego uruchomienia: wczytanie repo, konfiguracja Python, składnia JSON schema, testy jednostkowe, walidacja bazy — **success** według danych zadania `structure-and-tests`.
- Bramka techniczna potwierdza tylko strukturę, a nie poprawność przepisów.
- Końcowy HEAD po aktualizacji tego pliku może mieć osobny przebieg CI; nie przenosić automatycznie statusu PASS na nowszy commit.
- Nadal: **39 needs_review, 0 verified** — prawny audyt merytoryczny otwarty w #2.

## 2026-10-22 — przegląd treści partii 001 (PR oczekuje na CI)

- Wpisy poddane analizie: **39/39**, wyniki per ID w `docs/AUDYT-MERYTORYCZNY-PARTIA-001.md`.
- Bezpośrednio skonfrontowano 24 tezy z tekstem ADR 2025 i źródłami aktualnymi; 15 nadal wymaga pełnego sprawdzenia i wyjątków.
- Poprawiono pytania 0007, 0008, 0009, 0018, 0022, 0029, 0030, 0033, 0035; w #0009 także odpowiedź B.
- Ujęto sprostowanie ADR 2025: **Dz.U. 2025 poz. 1575**, w tym uwagę o pkt 8.2.2.7.2.3. Nie jest to podstawa do niezweryfikowanego dopisywania odpowiedzi.
- Linki prawne do 39 pytań kierują teraz do stabilnej strony oficjalnego ogłoszenia (Dz.U. 2025 poz. 642), a wskazanie punktu pozostaje w `reference`.
- Statusy pozostają: **39 needs_review / 0 verified**; brak niezależnego eksperta ADR i pełnego audytu każdego pkt PL.
- Bramka merytoryczna nadal **OPEN**; techniczną sprawdzić na PR i HEAD po scaleniu.

## 2026-10-22 — partia 002 i zamknięcie redakcyjnej luki 15/15

- Dodano **31 nowych autorskich pytań** ADR-B-0040…ADR-B-0070 (każde 3 odpowiedzi, klucz, proste wyjaśnienie, punkt ADR 2025).
- Bank po tej zmianie: **70 pytań**; moduły: 01=5, 02=6, 03=5, 04=5, 05=5, 06=6, 07=5, 08=5, 09=6, 10=5, 11=6, 12=5, 13=6.
- **70 needs_review, 0 verified** — żadnego wpisu nie zatwierdził niezależny recenzent ADR.
- Uzupełniono `docs/AUDYT-MERYTORYCZNY-PARTIA-001.md` o konkretne adresy źródłowe dla wcześniejszych 15 nierozstrzygniętych pozycji. Jest to **kontrola redakcyjna**, nie poświadczenie przez eksperta.
- Skorygowano #0001 i #0002, aby nie mylić wymagań dla pracowników nadawcy z odrębnym szkoleniem kierowcy i nie sugerować ogólnego zwolnienia z całego ADR; uściślono #0017, #0025 i #0032.
- Niezależny od walidatora Python odczyt JSONL z gałęzi: **70 rekordów, 13 tematów, brak powielonych ID/identycznych pytań, poprawna struktura A/B/C, 0 błędów**.
- Wynik formalnego Quality Gate w GitHub Actions: **do odczytu na PR** przed scaleniem.
- Do ukończenia: udokumentowana niezależna kontrola ekspert ADR dla 70 pytań oraz potwierdzenie pełnego, ostatecznego jakościowego statusu po ewentualnym merge; nie udostępniać w produkcji.

**Następny krok:** audyt merytoryczny partii 002 per ID, usuwanie pytań niemiarodajnych, pokrywanie brakujących scenariuszy i profesjonalna recenzja. Cysterny pozostają poza aktywnym zakresem.

## 2026-10-22 — wynik techniczny partii 002 po scaleniu PR #5

- PR: [#5](https://github.com/prawkonaraz100/adr-pytania-egzaminacyjne/pull/5), **merged** jako commit `b97da9a461333e3d6f98e59ee93983401c424a74`.
- Uruchomienie CI: [Quality Gate run #32](https://github.com/prawkonaraz100/adr-pytania-egzaminacyjne/actions/runs/39832204845) na commicie PR `66ca60be32b1e0068bf78083da6967943646629c`: **success**.
- Zadanie `structure-and-tests`: **success**. Kroki `Check JSON schema syntax`, `Unit tests` i `Validate question bank`: **success**.
- Ponownie odczytano dane z `main`: **70 rekordów**, 13/13 modułów, **70 needs_review, 0 verified**; poprawki i audyt partii 002 są widoczne.
- Nie przypisujemy sukcesu z PR do najnowszego HEAD `main`, gdyż dla końcowego commita po aktualizacjach dokumentacji wynik osobnego CI nie został potwierdzony.
- Bramka merytoryczna **OPEN**: niezależna recenzja eksperta, ocena wyjątków i dopuszczenie do produkcji nadal niewykonane.

## 2026-10-22 — partia 003 / jakość egzaminu

- W gałęzi `authoring/batch-003-realistic-tests` dodano 20 autorskich pytań scenariuszowych `ADR-B-0071...0090` (gaśnice, środki ochrony, załadunek, tunele, dokumentacja).
- Zmieniono 22 zestawy błędnych odpowiedzi, aby były merytorycznie wiarygodne i miały wartość dydaktyczną. To **nie** zastępuje eksperckiej weryfikacji.
- W całej bazie 90 pytań poprawna odpowiedź miała początkowo rozkład A=57/B=24/C=9; po zmianach układu wariantów rozkład A=30/B=30/C=30. Zachowano znaczenie poprawnych odpowiedzi.
- Dodano kontrolę odrzucającą rozkład klucza >55% jednej litery w bankach liczących co najmniej 30 pytań, wraz z testami.
- Skorygowano pytanie `ADR-B-0085`, żeby uwzględniało wyjątek 8.6.3.3 związany z 3.4.13 i 3.4.14.
- Stworzono `docs/AUDYT-PARTIA-003.md` z tabelą ID→przepis→ryzyko i źródłami.
- Stan banku w tej gałęzi: **90 needs_review, 0 verified**. Ekspercka recenzja nadal wymagana.
- Formalna kontrola CI dla tej gałęzi/PR: **oczekuje na odczyt**.

## 2026-10-22 — partia 004 i mapa kompletności programu

- Zidentyfikowano pełny oficjalny program: Dz.U. 2021 poz. 2150, załącznik nr 1: 13 tematów teoretycznych (18 h lekcyjnych) oraz osobne ćwiczenia praktyczne z gaśnicy, pierwszej pomocy i wypadku/awarii. Porównano załącznik z treścią oficjalnego aktu.
- Dopisano **32 autorskie pytania** ADR-B-0091...0122 — brakujące klasy ADR, zwolnienia, wypadki, środowisko, rozpoznawanie odpowiedzialności i ochrona.
- Aktualny bank w gałęzi roboczej: **122 potrzeby recenzji / 0 verified**; klucze A=40/B=41/C=41.
- Dodano **106 kompetencji redakcyjnych**: 103 teorii, 3 praktyczne. Wszystkie 122 pytania przypisane do kompetencji.
- Pokrycie redakcyjne: 84/103 celów teoretycznych mają ≥1 szkic pytania; **19 teoretycznych bez pytań** i **3 praktyczne wymagające ćwiczeń**. Brak zatwierdzonych `verified`.
- Stworzono materiały wstępne: `podstawowy/lekcje/ADR-B-01.md`, `ADR-B-05.md`, `ADR-B-12.md`. Pozostałe 10 lekcji do opracowania.
- Nowy walidator `scripts/coverage.py` oraz testy `tests/test_coverage.py` kontrolują 13 modułów, przypisanie wszystkich pytań, brak linków do nieistniejących ID i rozdzielenie teorii od ćwiczeń. Dodano do workflow.
- Nadrzędny dokument pokrycia: `docs/POKRYCIE-KURSU.md`, szczegóły kontroli partii 004: `docs/AUDYT-PARTIA-004.md`.
- **Jest to wersja robocza.** Formalna weryfikacja prawna każdej odpowiedzi, odbiór instruktora, pełny zestaw wizualizacji i materiały do prowadzenia zajęć praktycznych nie zostały wykonane.
- Dalsze czynności: sprawdzić CI na PR, następnie przygotować brakujące 19 kompetencji i lekcje; cysterny pozostają kolejnym etapem.


## 2026-10-22 — potwierdzony wynik CI i merge etapu kompetencji (PR #9)

- [PR #9](https://github.com/prawkonaraz100/adr-pytania-egzaminacyjne/pull/9) scalony do `main`, commit `8d8f9ac923129cfaa7be80b65ffa570e61b0ae2d`.
- **Pierwszy run #67** wykrył błąd opisu celu `ADR-B-11-K05` („Kod (-)” za krótki). Nie oznaczono kroku jako PASS; poprawiono tytuł kompetencji i odporność walidatora na błędne typy.
- [Quality Gate #71](https://github.com/prawkonaraz100/adr-pytania-egzaminacyjne/actions/runs/39843032931) na PR #9: `completed/success`; wszystkie kroki (schemat JSON, testy jednostkowe, walidacja banku i walidacja mapy kompetencji) `success`.
- Po scaleniu odczytano rzeczywiste dane na `main`: **122 pytania**, **122 needs_review**, **0 verified**, A/B/C = 40/41/41, **106 kompetencji**, **19 brakujących celów teorii**, **3 cele praktyczne**.
- Statusy merytoryczne pozostają otwarte; kompletny bank zatwierdzonych pytań ani formalny kurs nie został ukończony.
- [Issue #10](https://github.com/prawkonaraz100/adr-pytania-egzaminacyjne/issues/10) zawiera listę 19 luk, 10 brakujących lekcji i plan ćwiczeń.
- **Uwaga:** sukces PR nie jest automatycznie potwierdzeniem niezależnego przebiegu Actions dla każdego nowszego commita gałęzi `main`. Szczegółowo zarejestrowano dokładny SHA oraz numer uruchomienia.


## 2026-10-22 — partia 005: zakończone szkice 13 działów i 19 luk tematycznych

- Do banku dopisano `ADR-B-0123...0146`: **24 pytania** z wyjaśnieniami i wskazaniem punktów ADR 2025.
- Bank w gałęzi: **146 needs_review / 0 verified**, A=48, B=49, C=49.
- Powiązano 24 pytania z **19 wcześniej pustymi kompetencjami**. Matryca: 106 wewnętrznych kompetencji (103 teoria, 3 praktyczne), **103/103 celów teorii mają co najmniej 1 szkic pytania**, 0/103 ma zatwierdzony rekord.
- Dopisano **10 lekcji**, co daje komplet **13 szkiców** (`podstawowy/lekcje/ADR-B-01.md` do `ADR-B-13.md`). Wciąż **0 lekcji po potwierdzonej recenzji eksperckiej**.
- Utworzono `podstawowy/praktyka/SCENARIUSZE.md` z instrukcją, ćwiczeniami P1–P3 i pustym protokołem: **nie wykonano żadnych zajęć**, nie zaliczono praktyki.
- `scripts/coverage.py` sprawdza obecność i minimalną strukturę 13 lekcji i raportuje cele bez co najmniej dwóch pytań. To weryfikacja techniczna, nie jakości merytorycznej.
- Mapa gotowości `docs/POKRYCIE-KURSU.md` zaktualizowana bez utożsamiania 100% pokrycia redakcyjnego z ukończonym kursem. Szczegóły 24 pytań w `docs/AUDYT-PARTIA-005.md`.
- **Otwarte:** niezależny specjalista ADR dla pytań i lekcji, weryfikacja wyjątków każdej odpowiedzi, pełne ilustracje, przykładowe dokumenty, odbiór scenariuszy i faktyczna realizacja praktyki; symulator egzaminów na zweryfikowanych pytaniach nieuruchomiony.
- Formalny Quality Gate PR: **oczekuje na sprawdzenie**. Nie oznaczać partii jako zakończonej bez sukcesu wszystkich kroków CI.


## 2026-10-22 — kontrola i poprawki PR #12 (partia 005)

- [PR #12](https://github.com/prawkonaraz100/adr-pytania-egzaminacyjne/pull/12) łączy **24 pytania**, powiązanie 19 dawnych luk, 10 nowych szkiców lekcji (razem 13) i 3 scenariusze praktyczne.
- Pierwszy [Quality Gate #101](https://github.com/prawkonaraz100/adr-pytania-egzaminacyjne/actions/runs/39849471425): **FAIL** w `Check coverage map`; pozostale wymagane kroki były success. Przyczyna: walidator tytułów nie uwzględniał trzech starszych lekcji z nagłówkiem „Lekcja ADR-B-…” oraz nagłówka „Podstawa”.
- Poprawiono `scripts/coverage.py` bez wyłączania bramki; akceptuje różne, poprawne style nagłówka i nadal wymaga ID działu, minimalnej długości oraz źródeł. Dodano test regresyjny.
- [Quality Gate #105](https://github.com/prawkonaraz100/adr-pytania-egzaminacyjne/actions/runs/39849663003) dla commita `f2ae2251d12d451f831d3f00b13465367d3f2ddb`: **completed/success** — każdy krok schematu JSON, unit tests, walidacji pytań i matrycy ma success.
- Wynik dotyczy wskazanego commita PR; dla nowego commita dokumentacyjnego i HEAD po merge wymagane jest osobne potwierdzenie. Nie uznajemy testów merytorycznych za wykonane.
- Bank nadal ma **146 needs_review, 0 verified**. Nie rozpoczęto formalnych ćwiczeń praktycznych, nie ma niezależnego podpisu specjalisty, nie wydano materiałów produkcyjnych.


## 2026-10-22 — partia 006 / pogłębianie kompetencji

- Na gałęzi `authoring/batch-006-depth-and-safety` dodano **30 pytań** `ADR-B-0147…0176` (scenariusze klas towarów niebezpiecznych, awarii, wyposażenia i załadunku).
- Aktualny bank roboczy: **176 needs_review / 0 verified**, rozkład poprawnych A/B/C: **58/60/58**.
- Przypisano pytania do 30 wcześniej jedno-pytaniowych kompetencji; ich liczba spadła z **70 do 40**. Wszystkie 103 cele teorii mają ≥1 pytanie, ale 0 ma potwierdzoną recenzję specjalisty.
- Każdy z 30 nowych rekordów ma klucz odpowiedzi i prosty komentarz, źródło `ADR 2025` z ustępem do pełnego sprawdzenia; ryzyka zapisano w `docs/AUDYT-PARTIA-006.md`.
- Dodano test jednostkowy licznika `theory_with_less_than_two_questions`, aby nie mylić liczby rekordów z głębokością pytań.
- Część praktyczna nadal jest wyłącznie przygotowanym szkicem scenariuszy bez potwierdzenia obecności lub wykonania.
- **Otwarta bramka:** niezależna weryfikacja 176 pytań z aktualnym prawem i sprostowaniem 2025, audyt dystraktorów, legalne grafiki i dokumenty.
- Status formalnego CI: **oczekuje na kontrolę PR**; dopóki nie ma potwierdzonego success wszystkich kontroli, etap techniczny pozostaje otwarty.

