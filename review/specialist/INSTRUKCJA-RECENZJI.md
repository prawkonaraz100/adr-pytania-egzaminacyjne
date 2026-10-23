# Instrukcja niezależnej recenzji banku ADR podstawowego — wersja 1 (23.10.2026)

**Cel:** weryfikacja każdego z 506 pytań osobno — treści, klucza, odpowiedzi A/B/C, wyjaśnienia i wszystkich wyjątków — przez rzeczywistego specjalistę ADR. Żadne pytanie nie zostało zatwierdzone. **Nie publikować banku ani egzaminu próbnego opartego na potrzebujących recenzji pytaniach.**

## Materiały wejściowe

1. Pełny indeks [aktualny wykaz pytań 0001–0542](REJESTR-AKTUALNY-0001-0542.md), oryginalne rekordy w `podstawowy/questions.jsonl`.
2. Urzędowe polskie ADR 2025 — [Dz.U. 2025 poz. 642](https://dziennikustaw.gov.pl/DU/2025/642) oraz [sprostowanie poz. 1575](https://eli.gov.pl/eli/DU/2025/1575/ogl); program kursu [Dz.U. 2021 poz. 2150](https://eli.gov.pl/eli/DU/2021/2150/ogl).
3. Audyty redakcyjne `review/sequential/`, analizy wariantów `review/legal-clauses/`, raporty `review/batches/`, matryca `podstawowy/kompetencje.json`, materiały 13 lekcji i `podstawowy/praktyka/SCENARIUSZE.md`.
4. Procedura zatwierdzania: `review/README.md` i skrypt `scripts/release_gate.py`.

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
