# Etap 4x18 — egzamin próbny, pakiet recenzyjny i wyrównanie B-08/B-12

- Zakres: wyłącznie kurs podstawowy ADR.
- Punkt wyjścia: świeży `main` `9de920c4df74b393ab0a7e28b50266458eef3e4a`.
- Bank po zmianach: 609 rekordów, 0 zduplikowanych ID, wszystkie `needs_review`, 0 `verified`.
- Aktualny Git blob SHA banku: `ec1bb5391aa9875e2a1aa7bdb138fb79b3bf72dd`.

## 1. Egzaminy próbne 001–005

Sprawdzono każdy arkusz i klucz względem aktualnego `questions.jsonl`: ID, numerację, moduł, treść pytania, zestaw opcji, mapowanie poprawnej odpowiedzi po ewentualnym przestawieniu opcji oraz explanation po remapowaniu. Wszystkie arkusze mają 30 unikalnych pytań i zawierają wszystkie 13 działów. Rozkład działów jest proporcjonalny do wielkości banku w 30-pytaniowym arkuszu: każdy dział ma 2 lub 3 pytania. Żadne ID nie powtarza się pomiędzy pięcioma wariantami.

| Wariant | Liczba | Unikalne ID | Działy | Rozkład | Klucz A/B/C |
|---|---:|---:|---:|---|---|
| 001 | 30 | 30 | 13 | 9×2, 4×3 | 10/10/10 |
| 002 | 30 | 30 | 13 | 9×2, 4×3 | 10/10/10 |
| 003 | 30 | 30 | 13 | 9×2, 4×3 | 10/10/10 |
| 004 | 30 | 30 | 13 | 9×2, 4×3 | 10/10/10 |
| 005 | 30 | 30 | 13 | 9×2, 4×3 | 10/10/10 |

Wszystkie 5 arkuszy i 5 kluczy wskazują tę samą migawkę banku `ec1bb5391aa9875e2a1aa7bdb138fb79b3bf72dd`. Zaostrzono `scripts/check_mock_exam_variants.py`: test oblicza Git blob SHA-1 z pliku banku i blokuje nieaktualne `source_bank_head` w dowolnym wariancie lub kluczu. Walidator blokuje też rozkład inny niż 30 pytań / 13 działów / 2–3 pytania na dział. Testy są w `tests/test_mock_exam_variants.py`.

## 2. Wyrównanie wskaźnika długości odpowiedzi

Poprawiono wyłącznie długość dwóch błędnych dystraktorów w B-08 i jednego w B-12; nie zmieniono ID, poprawnej litery, sensu poprawnej odpowiedzi ani explanation:
- **ADR-B-0074 (B-08):** wydłużono realistyczny, błędny wariant o uznaniu gaśnicy za prawidłową tylko dlatego, że plomba jest nienaruszona.
- **ADR-B-0422 (B-08):** doprecyzowano błędny wariant polegający na ocenianiu wyglądu obudowy zamiast terminu kontroli.
- **ADR-B-0144 (B-12):** doprecyzowano błędny wariant wyboru parkingu z monitoringiem bez sprawdzenia zgodności z wymaganiami ADR.

Warianty i klucze 001–005 zaktualizowano do nowej migawki banku. Pytania występujące w arkuszach mają zaktualizowany tekst opcji, a poprawna litera i explanation pozostają zsynchronizowane. Nie zmieniono żadnego statusu weryfikacji.

## 3. Metryki po zmianach

| Dział | Pytań | Poprawna = jedyna najdłuższa | Rozkład poprawnych liter A/B/C |
|---|---:|---:|---:|
| ADR-B-01 | 45 | 7/45 (15.56%) | 17/17/11 |
| ADR-B-02 | 56 | 8/56 (14.29%) | 21/19/16 |
| ADR-B-03 | 49 | 7/49 (14.29%) | 16/21/12 |
| ADR-B-04 | 46 | 7/46 (15.22%) | 15/18/13 |
| ADR-B-05 | 43 | 6/43 (13.95%) | 18/14/11 |
| ADR-B-06 | 45 | 5/45 (11.11%) | 16/14/15 |
| ADR-B-07 | 48 | 6/48 (12.50%) | 18/18/12 |
| ADR-B-08 | 42 | 5/42 (11.90%) | 12/12/18 |
| ADR-B-09 | 46 | 4/46 (8.70%) | 13/15/18 |
| ADR-B-10 | 55 | 4/55 (7.27%) | 19/18/18 |
| ADR-B-11 | 43 | 6/43 (13.95%) | 12/13/18 |
| ADR-B-12 | 44 | 6/44 (13.64%) | 14/13/17 |
| ADR-B-13 | 47 | 4/47 (8.51%) | 15/15/17 |

- Globalnie: **75/609 = 12.32%**, poniżej limitu 16%.
- B-08: **5/42 = 11.90%**, poniżej 14%.
- B-12: **6/44 = 13.64%**, poniżej 14%.
- Najkrótsze explanation: 300 znaków; poniżej 200 znaków: 0.
- Statusy: 609 `needs_review`, 0 `verified`.

CI wymusza teraz globalny i modułowy limit **≤16%** oraz osobny test, że B-08 i B-12 pozostają poniżej 14%.

## 4. Pakiet recenzyjny specjalisty

Zaktualizowano:
- `review/README.md` — aktualny stan, priorytety i ograniczenia automatycznych kontroli;
- `review/specialist/INSTRUKCJA-RECENZJI.md` — priorytetowe rekordy i zasada zatwierdzania;
- `review/specialist/PAKIET-0609-MANIFEST.json` — migawka banku, warianty/klucze, lista priorytetowych ID i statusy.

Lista priorytetowa obejmuje ADR-B-0073, 0074, 0253, 0283, 0420, 0422, 0484 oraz ADR-B-0144, 0249, 0274, 0275, 0300, 0304, 0305. To nie jest lista wyczerpująca: wszystkie 609 pytań wymagają indywidualnej recenzji. Do kontroli wartości zależnych od przyszłej edycji ADR nadal służą trzy rejestry z etapu 4x9. `verified` może nadać wyłącznie rzeczywisty specjalista po kontroli polskiego tekstu urzędowego, sprostowania i każdej odpowiedzi A/B/C.

## 5. Ograniczenia

Nie oznaczono żadnego pytania jako `verified`; nie twierdzimy, że automatyczne testy stanowią potwierdzenie prawne. Arkusze pozostają materiałem treningowym, `publication_authorized: false`. Kontrole danych i metryk wykonano na treści pobranej z GitHuba; ostateczny status testów jednostkowych i Quality Gate potwierdzi CI w PR.
