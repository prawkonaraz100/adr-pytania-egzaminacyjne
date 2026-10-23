# Instrukcja niezależnej recenzji banku ADR podstawowego — wersja 1 (23.10.2026)

**Cel:** weryfikacja każdego z 506 pytań osobno — treści, klucza, odpowiedzi A/B/C, wyjaśnienia i wszystkich wyjątków — przez rzeczywistego specjalistę ADR. Żadne pytanie nie zostało zatwierdzone. **Nie publikować banku ani egzaminu próbnego opartego na potrzebujących recenzji pytaniach.**

## Materiały wejściowe

1. Pełny indeks [pytania 0001–0506](REJESTR-0001-0506.md), oryginalne rekordy w `podstawowy/questions.jsonl`.
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
