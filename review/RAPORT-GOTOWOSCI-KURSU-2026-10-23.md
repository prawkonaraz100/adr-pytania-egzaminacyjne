# Etap 3 — końcowa kontrola spójności i gotowości do recenzji

Data 23.10.2026. Zakres: 324 rekordy `podstawowy/questions.jsonl`, 106 kompetencji w `podstawowy/kompetencje.json`, 13 lekcji `podstawowy/lekcje/ADR-B-01.md`…`ADR-B-13.md`, `podstawowy/praktyka/SCENARIUSZE.md`, rejestr `review/REJESTR-RECENZJI-ETAP3.md`.

## Potwierdzone kontrole strukturalne

| Kontrola | Wynik | Granica wyniku |
|---|---|---|
| Bank | 324 kolejnych rekordów do ADR-B-0324 | Nie są zatwierdzone prawnie |
| Rejestr | 324/324 ID z banku | Wpis nie oznacza recenzji fachowca |
| Matryca kompetencji | 0 nieistniejących ID, 0 przypisań do innego działu, 0 pytań bez przypisania | Nie weryfikuje poprawności merytorycznej przypisania |
| Lekcje | 13/13 istnieje; każdy rekord ma lekcję zgodną z `module_id` | Nie wykazano dosłownego omówienia każdej odpowiedzi i każdego punktu przepisu w lekcji |
| Praktyka | 3 cele praktyczne powiązane z P1–P3 w scenariuszach | Nie ma realnych protokołów zaliczenia |
| Duplikaty pytań | 0 identycznych pytań po normalizacji interpunkcji/wielkości liter | Nie wyklucza parafraz semantycznych |
| Niemal-duplikaty | 1 para z podobieństwem Jaccarda tokenów > 0,68 w tym samym dziale: 0071/0072 | Celowo różne DMC: 3,5 t i 6 t. Nie usuwać bez recenzji, zachować do kontroli normy 8.1.4.1 |
| Literalna wzmianka „ADR 2023” w treści rekordów i lekcji | 0 | Wersja archiwalna w bibliografii nie stanowi sama w sobie błędu |
| Nietypowe źródła | ADR-B-0145, ADR-B-0198 — uwzględniają M364 | Nie przerabiać wyjątków bez kontroli państw sygnatariuszy i terminu obowiązywania |

## Kontrola prawa i terminologii — nierozstrzygnięte

Wyszukiwanie literalnych numerów ADR w lekcjach wykazało występowanie cytowanych rodzin przepisów w odpowiednich działach, ale **nie stanowi dowodu, że każdy konkretny podpunkt 324 pytań jest omówiony lub zgodny z treścią lekcji**. Wskazane źródła pytań i materiałów należy porównać per ustęp z urzędowym [Dz.U. 2025 poz. 642](https://www.dziennikustaw.gov.pl/DU/rok/2025/pozycja/642) oraz [sprostowaniem 1575](https://eli.gov.pl/api/acts/DU/2025/1575/text.pdf). Polskie brzmienie i wyjątki pozostają **PENDING**. Słownik do ujednolicenia przez redaktora/specjalistę: `jednostka transportowa`, `sztuka przesyłki`, `nalepka ostrzegawcza`, `duża nalepka ostrzegawcza`, `tablica barwy pomarańczowej`, `grupa pakowania`, `kategoria transportowa`, `świadectwo dopuszczenia pojazdu`, `zaświadczenie ADR kierowcy`.

**M364:** dotyczy lokalizacji świadectwa dopuszczenia przyczepy/naczepy w warunkach porozumienia, nie automatycznie pojazdu silnikowego. Polska publikacja porozumienia wskazuje termin do 31.12.2026, przy zachowaniu warunku sygnatariuszy; ocena indywidualnych pytań 0145/0198 nadal wymagania recenzji.

## Jakościowa ocena głębokości: priorytety i decyzje

Wstępny raport głębokości `docs/AUDYT-GLEBOKOSCI-ETAP2-0323-0324.md` wykorzystuje wskaźniki leksykalne, które **nie oceniają indywidualnie zdolności do zastosowania przepisu**. Nie można na ich podstawie zakwalifikować jako potwierdzonych luk ani ogłosić 103/103 kompetencji jako jakościowo domkniętych. Dla każdej kompetencji należy wykonać ręczny test: rozpoznanie sytuacji, decyzja, ograniczenia/wyjątki, referencja ADR, spójność z lekcją. Priorytet: 1.1.3.6, dokumenty, oznakowanie, wyposażenie, wypadek, tunele i zakazy ładowania razem. W tej partii **nie dopisano ADR-B-0325**: automatycznie wykryte ryzyka nie stanowią potwierdzonej luki wymagającej nowego pytania; dodawanie bez pełnego porównania prawnego przeczyłoby zasadom projektu.

## Lista otwartych punktów dla specjalisty

1. Zbadać 324 pytania i 972 warianty A/B/C z pełnym oficjalnym polskim tekstem, sprostowaniem i stosowalnymi odstępstwami; ocenić warunki i wyjątki.
2. Każde pytanie sparować z konkretną treścią lekcji — zaznaczyć zakres odpowiedzi, nie tylko zgodność numeru działu. Rozstrzygnąć brakujące ustępy i dopiero wtedy dopisać brakujące ćwiczenia lub pytania.
3. Ręcznie odczytać parę 0071/0072 pod kątem odpowiedzi, wymagań 8.1.4.1 oraz dydaktycznej sensowności; wykonać niezależną kontrolę podobieństwa semantycznego całego banku.
4. Sprawdzić zakres M364 dla 0145 i 0198 oraz pozostałych aktualnych umów wielostronnych, w tym jurysdykcje i daty.
5. Ujednolicić język polski i terminologię prawno-techniczną w całym banku i wszystkich lekcjach, z zachowaniem kontroli zmian snapshotów A/B/C.
6. Ocenić i zatwierdzić przez instruktora scenariusze P1–P3; faktyczną praktykę zalicza się tylko po rzeczywistym wykonaniu.
7. Wdrożyć i przetestować generator próbnego egzaminu tylko na podpisanym `verified` eksporcie; obecna specyfikacja nie jest działającym generatorem.
8. Uruchomić release gate na konkretnym zatwierdzonym HEAD; przed akceptacją eksperta pozostaje BLOCKED.

## Decyzja

**GOTOWY DO PRZEKAZANIA DO NIEZALEŻNEJ RECENZJI — NIEGOTOWY DO PUBLICZNEGO EGZAMINU ANI WYDANIA.** 324 `needs_review`, 0 `verified`; bez fikcyjnych protokołów i bez zmian w kursach specjalistycznych. Same kontrole strukturalne nie poświadczają prawnej zgodności każdej odpowiedzi ani terminologii.

## Aktualizacja: 14 powiązań z lekcjami (23.10.2026)

Dla 14 pytań z niewystarczającym automatycznym dopasowaniem dodano odrębne podsekcje w istniejących lekcjach; zaktualizowano `review/MACIERZ-PYTANIE-LEKCJA-ETAP3.md`. Tekst powstał z dotychczasowych niezatwierdzonych objaśnień. Nie poświadcza legalności ani jakości dydaktycznej; każda ze 106 kompetencji nadal wymaga osobnego odczytu i rozstrzygnięcia przypadków, decyzji, wyjątków i prawa. Nie poprawiano żadnych niepotwierdzonych błędów terminologicznych. 324 needs_review, 0 verified, eksport BLOCKED.

## Status po czterech partiach przeglądu kompetencji — 23.10.2026

Dokonano pierwszego porównania zakresu i zróżnicowania zestawów pytań ze wskazanymi kompetencjami i odpowiadającymi lekcjami. Zakres ewidencyjny obejmuje 106/106 kompetencji, ale **nie jest to pozytywne zakończenie wymaganego ręcznego przeglądu prawnego każdego wariantu A/B/C ani wszystkich wyjątków**.

| Działy | Kompetencje | Raport | PR | Stan |
|---|---:|---|---|---|
| 01–03 | 27 | [JAKOSC-KOMPETENCJI-01-03-2026-10-23.md](JAKOSC-KOMPETENCJI-01-03-2026-10-23.md) | #78 | Scalony, Quality Gate PASS |
| 04–06 | 30, w tym praktyczne P1–P3 | [JAKOSC-KOMPETENCJI-04-06-2026-10-23.md](JAKOSC-KOMPETENCJI-04-06-2026-10-23.md) | #79 | Scalony, Quality Gate PASS |
| 07–09 | 23 | [JAKOSC-KOMPETENCJI-07-09-2026-10-23.md](JAKOSC-KOMPETENCJI-07-09-2026-10-23.md) | #80 | Scalony, Quality Gate PASS |
| 10–13 | 26 | [JAKOSC-KOMPETENCJI-10-13-2026-10-23.md](JAKOSC-KOMPETENCJI-10-13-2026-10-23.md) | #81 | Scalony, Quality Gate PASS |

**Uwaga do etykiety „wystarczająca”:** w tych raportach oznacza wstępne zróżnicowanie dydaktyczne zestawu; nie oznacza prawnej poprawności, satysfakcjonującej trudności egzaminacyjnej, kompletności wyjątków ani akceptacji niezależnego specjalisty.

W raporcie 01–03 szczególnie wymagają dopracowania 01-K07, 02-K01/K02/K09/K12 oraz 03-K01/K04/K06. W 04–06 wielokrotnie powtarzają się scenariusze dotyczące zachowania załogi i oznakowania; P1–P3 wymagają realnej oceny instruktora. W 07–09 szczególnym priorytetem jest praktyczna tabela zakazów wspólnego ładowania i warunkowe wyposażenie. W 10–13 — zastosowanie wyjątków multimodalnych, kodów tuneli i warunków dokumentacji. Szczegółowe przypadki podano w czterech raportach.

**Nadal otwarte:** indywidualne literalne porównanie 324 pytań (972 wariantów A/B/C) z ogłoszonym tekstem polskim [Dz.U. 2025 poz. 642](https://dziennikustaw.gov.pl/DU/2025/642) i sprostowaniem 1575, analiza M364 tam, gdzie jest stosowne, ekspercka kontrola wyjątków i terminologii oraz uzupełnienie rzeczywiście potwierdzonych braków praktycznych nowymi pytaniami z pełnym audytem. Z samego wykrycia powtarzalności nie wynika poprawna treść nowego pytania. Nie dopisywano 0325, nie zmieniano kluczy ani snapshotów.

**Decyzja bez zmian:** 324 pytania `needs_review`, 0 `verified`, eksport BLOCKED, żadnego szkolenia specjalistycznego.
