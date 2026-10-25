# Etap 4x10 — egzaminy próbne i język kursanta

Data: 25.10.2026. Zakres: wyłącznie kurs podstawowy. Punkt wyjścia: świeży `main` `50a35bb927602094cd892a2b4fa5e2eaae851d1c`. Wpis podsumowujący 4x9 istnieje już w Issue #10; nie dodano duplikatu.

## 1. Egzaminy próbne 001–005

Wszystkie arkusze mają po 30 pytań, zachowano dobór pytań i dotychczasowy rozkład działów. Zmieniono wyłącznie kolejność trzech odpowiedzi w arkuszach, bez zmiany treści odpowiedzi ani poprawności merytorycznej. Klucze i wyjaśnienia zsynchronizowano z nowymi literami.

| Wariant | Przed A/B/C | Seria przed | Po A/B/C | Seria po |
|---|---:|---:|---:|---:|
| 001 | 16/5/9 | 4 | 10/10/10 | 3 |
| 002 | 10/11/9 | 4 | 10/10/10 | 3 |
| 003 | 8/14/8 | 3 | 10/10/10 | 3 |
| 004 | 9/10/11 | 3 | 10/10/10 | 3 |
| 005 | 10/10/10 | 4 | 10/10/10 | 2 |

Wszystkie warianty nadal mają 30 unikalnych pytań; nie ma wspólnych ID między wariantami. Zachowano rozkład 13 działów. Każdy arkusz pozostaje `publication_authorized: false`.

Dodano `scripts/check_mock_exam_variants.py` oraz `tests/test_mock_exam_variants.py`; Quality Gate sprawdza: zgodność treści i zestawu opcji z bankiem, poprawność wskazanej litery po przestawieniu, synchronizację explanation, kolejność ID w kluczu, 30 pytań, brak powtórzeń, rozkład działów, minimum 8 wystąpień każdej litery, serię najwyżej 3 i brak klucza osadzonego w arkuszu.

## 2. Audyt języka kursanta — próba 104 pytań

- Seed: `20261025`.
- Metoda: dla każdego działu B-01–B-13 osobno tasowanie Fishera–Yatesa z deterministycznym generatorem pseudolosowym; wybrano pierwsze 8 rekordów z przetasowanej listy, łącznie 104.
- W próbie wszystkie explanation miały co najmniej 200 znaków; nie wykryto wyjaśnień rozpoczynających się od numeru przepisu ani zdań przekraczających 35 słów w tej próbie.
- Sześć wyjaśnień miało niewyjaśniony skrót lub termin specjalistyczny, który utrudniał zrozumienie osobie początkującej: **ADR-B-0041, ADR-B-0499, ADR-B-0315, ADR-B-0318, ADR-B-0082, ADR-B-0036**. To 6/104 = **5,77%**, czyli poniżej progu 10%; nie rozszerzano próby na całe działy.
- Przepisano te 6 explanation: wyjaśniono potrzebę aktualizacji szkolenia, znaczenie numeru UN, klasyfikację baterii sodowo-jonowych, klasyfikację nieznanego odpadu, przepis CV28 oraz różnicę między ochroną przewozu a mocowaniem ładunku. Każde wyjaśnienie ma 2–5 zdań, ponad 200 znaków i kończy się podstawą ADR.
- Pełna lista 104 ID z próby: `podstawowy/raporty/etap-4x10-proba-jezykowa-seed-20261025.json`.

## 3. Heurystyka ostrzegawcza explanation

Walidator ostrzega o explanation, które zaczyna się numerem przepisu, odwołuje się do ponad trzech działów albo nie zawiera żadnego z prostych sygnałów wyjaśniających z listy heurystycznej. W aktualnym banku pozostało **86 ostrzeżeń heurystycznych** — wszystkie dotyczą braku jednego z tych słów/zwrotów; nie ma trafień rozpoczynających się od numeru przepisu ani z ponad trzema odwołaniami do działów. To ostrzeżenia do przeglądu, nie automatyczne stwierdzenie błędu prawnego. Przypadki potwierdzone podczas próby (6 wyżej) poprawiono.

ID ostrzeżeń (86): ADR-B-0001, ADR-B-0022, ADR-B-0023, ADR-B-0024, ADR-B-0036, ADR-B-0037, ADR-B-0039, ADR-B-0046, ADR-B-0057, ADR-B-0067, ADR-B-0068, ADR-B-0075, ADR-B-0081, ADR-B-0085, ADR-B-0086, ADR-B-0094, ADR-B-0120, ADR-B-0122, ADR-B-0124, ADR-B-0128, ADR-B-0132, ADR-B-0136, ADR-B-0137, ADR-B-0147, ADR-B-0173, ADR-B-0176, ADR-B-0178, ADR-B-0186, ADR-B-0198, ADR-B-0211, ADR-B-0228, ADR-B-0240, ADR-B-0248, ADR-B-0250, ADR-B-0254, ADR-B-0255, ADR-B-0257, ADR-B-0271, ADR-B-0280, ADR-B-0281, ADR-B-0285, ADR-B-0291, ADR-B-0297, ADR-B-0300, ADR-B-0304, ADR-B-0306, ADR-B-0309, ADR-B-0312, ADR-B-0319, ADR-B-0325, ADR-B-0327, ADR-B-0346, ADR-B-0349, ADR-B-0357, ADR-B-0362, ADR-B-0365, ADR-B-0368, ADR-B-0374, ADR-B-0378, ADR-B-0391, ADR-B-0395, ADR-B-0402, ADR-B-0403, ADR-B-0404, ADR-B-0415, ADR-B-0417, ADR-B-0438, ADR-B-0441, ADR-B-0448, ADR-B-0453, ADR-B-0471, ADR-B-0486, ADR-B-0490, ADR-B-0499, ADR-B-0527, ADR-B-0529, ADR-B-0534, ADR-B-0535, ADR-B-0561, ADR-B-0563, ADR-B-0571, ADR-B-0573, ADR-B-0576, ADR-B-0580, ADR-B-0582, ADR-B-0595.

## 4. Wskaźnik „poprawna = jedyna najdłuższa”

| Dział | Wskaźnik |
|---|---:|
| B-01 | 7/45 = 15,56% |
| B-02 | 8/56 = 14,29% |
| B-03 | 7/49 = 14,29% |
| B-04 | 7/46 = 15,22% |
| B-05 | 6/43 = 13,95% |
| B-06 | 5/45 = 11,11% |
| B-07 | 6/48 = 12,50% |
| B-08 | 6/42 = 14,29% |
| B-09 | 4/46 = 8,70% |
| B-10 | 4/55 = 7,27% |
| B-11 | 6/43 = 13,95% |
| B-12 | 7/44 = 15,91% |
| B-13 | 4/47 = 8,51% |
| **Globalnie** | **77/609 = 12,64%** |

Każdy dział spełnia limit 16%; minimum explanation w banku wynosi 300 znaków, 0 poniżej 200. Wszystkie 609 pytań pozostają `needs_review`, 0 `verified`.

## Pliki zmienione

- Bank: `podstawowy/questions.jsonl` — tylko 6 explanation.
- Arkusze i klucze: `podstawowy/egzamin-probny/wariant-001.json` … `wariant-005.json`, `klucz-001.json` … `klucz-005.json`.
- Kontrola: `scripts/check_mock_exam_variants.py`, `tests/test_mock_exam_variants.py`, `.github/workflows/quality.yml`.
- Nawigacja: `podstawowy/README.md`, `podstawowy/egzamin-probny/README.md`.
- Próba: `podstawowy/raporty/etap-4x10-proba-jezykowa-seed-20261025.json`.

Nie zmieniono poprawnych liter w banku, statusów weryfikacji ani doboru pytań do wariantów. Nie rozpoczęto kursu cystern ani innego kursu.
