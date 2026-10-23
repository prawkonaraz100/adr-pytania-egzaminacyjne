# Etap 4m — bieżący raport gotowości (545 pytań)

Stan obliczony ze świeżej gałęzi main po PR #159–#161, data 23.10.2026. **Raport zastępuje liczbami stan 4l, nie nadpisuje jego historii.**

| Kontrola | Faktyczny stan | Werdykt |
|---|---|---|
| Bank pytań | 545 (ADR-B-0001–0545) | Spójny strukturalnie |
| Statusy | 545 `needs_review`, 0 `verified` | Do recenzji |
| Dział ADR-B-06 | 35 pytań, +3 scenariusze rozpoznawania cyfr 2/4/7 | Wypełniony cel liczbowy |
| Indeks recenzenta | `REJESTR-AKTUALNY-0001-0545.md`, 545 wpisów | Zaktualizowany |
| Manifest / ledger | `PAKIET-0545-MANIFEST.json`, `stage4m-literal-verification-ledger-0001-0545.json` | 545 otwartych porównań |
| Załączniki SVG | 10 istniejących odnośników, wymagają kontroli wzoru | Szkice szkoleniowe |
| Klucz odpowiedzi A/B/C | Wskaźnik długości kontrolowany w Quality Gate | Próg 40% **NIEOSIĄGNIĘTY** |
| Egzamin próbny | Zablokowany przez `release_gate`, 0 zatwierdzonych pytań | Niepublikowalny |

## Wskaźnik długości A/B/C w 13 działach

Definicja: poprawny wariant jest **ściśle** dłuższy niż oba pozostałe, po usunięciu białych znaków na końcach. Remisy nie są zaliczane. Suma: **365/545 (67.0%)**. Cel ≤40% globalnie **i w każdym dziale**.

| Moduł | Pytania | Poprawna najdłuższa | Udział | Cel ≤40% |
|---|---:|---:|---:|---|
| ADR-B-01 | 35 | 18 | 51.4% | OTWARTY |
| ADR-B-02 | 56 | 34 | 60.7% | OTWARTY |
| ADR-B-03 | 49 | 35 | 71.4% | OTWARTY |
| ADR-B-04 | 44 | 32 | 72.7% | OTWARTY |
| ADR-B-05 | 40 | 30 | 75.0% | OTWARTY |
| ADR-B-06 | 35 | 14 | 40.0% | spełniony |
| ADR-B-07 | 43 | 30 | 69.8% | OTWARTY |
| ADR-B-08 | 36 | 20 | 55.6% | OTWARTY |
| ADR-B-09 | 39 | 32 | 82.1% | OTWARTY |
| ADR-B-10 | 55 | 45 | 81.8% | OTWARTY |
| ADR-B-11 | 35 | 22 | 62.9% | OTWARTY |
| ADR-B-12 | 43 | 35 | 81.4% | OTWARTY |
| ADR-B-13 | 35 | 18 | 51.4% | OTWARTY |

## Przebieg etapu 4m

- PR #159: `scripts/answer_length_bias.py`, testy regresyjne, raport ostrzegawczy globalny/per-moduł w Quality Gate; 12 ostrożnych korekt treści wariantów, pełny CI PASS i wpis do Issue #10.
- PR #160: nowe pytania ADR-B-0543–0545, audyt A/B/C, aktualizacja mapy kompetencji, manifestu i indeksu 545, pełny CI PASS, wpis do Issue #10. Porównanie z polskim urzędowym PDF **niepotwierdzone**, więc wszystkie pozostają needs_review.
- PR #161: 13 kolejnych redakcyjnych korekt odpowiedzi w działach 03, 04 i 07; wszystkie migawki sequential/legal-clauses zaktualizowane, PASS i wpis w Issue #10.
- Bieżący PR aktualizuje instrukcję przekazania recenzentowi, status egzaminu próbnego i ten raport; **nie przerabia historycznych raportów**.

## Otwarte warunki publikacji

1. **Doprowadzić udział najdłuższych poprawnych odpowiedzi poniżej 40%** zarówno globalnie, jak i dla każdego modułu; uruchomić `python scripts/answer_length_bias.py --strict` i potwierdzić PASS, nie obniżać progu sztucznie.
2. Rzetelnie sprawdzić semantykę dystraktorów — statystyczne skracanie wariantu nie może zmieniać właściwej odpowiedzi. Priorytet dla modułów z największą dysproporcją; weryfikacja prawna i migawki przy każdym ID.
3. Dosłowne porównanie polskiego ADR 2025 w Dz.U. poz. 642 ze sprostowaniem poz. 1575 dla wszystkich 545 rekordów (otwarta kolejka). Pomocnicze materiały MI/UNECE nie zastępują urzędowego źródła.
4. Rzeczywisty niezależny specjalista ADR zatwierdza osobno A/B/C, wyjaśnienie, wyjątki, a także grafiki rozpoznawcze. Nie zapisywać fikcyjnych akceptacji.
5. Egzamin próbny i wydanie publiczne są zablokowane do przejścia istniejącej `release_gate`; karta praktyki P1–P3 nie oznacza rzeczywistego odbycia ćwiczeń.

**Wniosek:** gotowość strukturalna do dalszej redakcji i recenzji, **nie do publikacji**. 545 `needs_review`, zero `verified`, brak kursu cystern i innych kursów.


## Aktualizacja 4m, partia 4 — ADR-B-06

Po pięciu zmianach w pytaniach 0503, 0504, 0507, 0543, 0544 wskaźnik dla ADR-B-06 wynosi **14/35 = 40,0%**, czyli osiąga lokalny próg. Globalnie **365/545 = 67,0%**, dlatego pozostała redakcja innych działów jest konieczna. Migawki i oceny A/B/C zaktualizowano w tych samych PR-ach. Raport: `review/batches/stage4m-length-bias-batch4-b06.md`. Nie zmieniono statusów `needs_review`.
