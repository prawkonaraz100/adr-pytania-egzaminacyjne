# Raport końcowy — ETAP 4x12: słowniczek kursanta i żargon w lekcjach

- Data: 25.10.2026.
- Zakres: wyłącznie kurs podstawowy ADR.
- Bank: 609 pytań, 609 `needs_review`, 0 `verified`.
- Słowniczek: `podstawowy/SLOWNICZEK.md` — **90 haseł** z prostymi objaśnieniami i punktami ADR.
- Ścieżka kursanta: każda z 13 lekcji ma odsyłacz do słowniczka bezpośrednio pod tytułem, przed pierwszym rozdziałem.
- Test CI: dodano blokujący `tests/test_learner_glossary.py`; uruchamia się w istniejącym kroku `python -m unittest discover -s tests -v`. Sprawdza ustaloną listę 27 fachowych terminów i to, że wszystkie 13 lekcji odsyłają do słowniczka. Test ocenia obecność definicji/odsyłaczy, a nie samodzielnie poprawność prawną haseł.

## Ręczny przegląd kandydatów heurystyki

Raport 4x11 opisywał 11 kandydatów pozostałych po rozszerzeniu słów-sygnałów. Ponowne odtworzenie funkcji z aktualnego `scripts/check_explanation_heuristics.py` na aktualnym banku wskazało **13 ID**. Rozbieżność jest odnotowana, zamiast bez sprawdzenia powtarzać starszą liczbę.

Przejrzano ręcznie 13/13 kandydatów. **0 explanation przepisano**, ponieważ wszystkie ocenione wyjaśnienia miały sens dydaktyczny: uzasadniały odpowiedź poprawną, wskazywały konkretną pomyłkę i zawierały podstawę ADR. To oznacza 13 fałszywych alarmów heurystyki, a nie 13 formalnie zweryfikowanych treści prawnych.

| Partia | Kandydaci przeczytani | Przepisane | Fałszywe alarmy |
|---|---:|---:|---:|
| B-01–04 | 5 | 0 | 5 |
| B-05–08 | 2 | 0 | 2 |
| B-09–13 | 6 | 0 | 6 |
| **Łącznie** | **13** | **0** | **13** |

Lista ID: ADR-B-0147, ADR-B-0529, ADR-B-0534, ADR-B-0349, ADR-B-0357, ADR-B-0136, ADR-B-0186, ADR-B-0086, ADR-B-0248, ADR-B-0067, ADR-B-0120, ADR-B-0402 i ADR-B-0403. Każdy przypadek ma jednozdaniowe uzasadnienie w raporcie swojej partii.

## Zmiany objaśnień w lekcjach

Nie dodano definicji inline do treści lekcji — zamiast powielać te same informacje w 13 plikach, umieszczono widoczny odsyłacz do wspólnego słowniczka. Dodano **po jednym odsyłaczu w każdej lekcji**:

| Lekcja | Nowe definicje inline | Odsyłacz do słowniczka |
|---|---:|---:|
| B-01 | 0 | 1 |
| B-02 | 0 | 1 |
| B-03 | 0 | 1 |
| B-04 | 0 | 1 |
| B-05 | 0 | 1 |
| B-06 | 0 | 1 |
| B-07 | 0 | 1 |
| B-08 | 0 | 1 |
| B-09 | 0 | 1 |
| B-10 | 0 | 1 |
| B-11 | 0 | 1 |
| B-12 | 0 | 1 |
| B-13 | 0 | 1 |

Wspólny słowniczek ma 90 haseł; każda definicja wskazuje punkt ADR lub miejsce do sprawdzenia. Przy pierwszym spotkaniu z fachowym terminem lekcja zachęca do użycia słowniczka. To centralne objaśnienie zamiast dublowania definicji w każdej lekcji.

## Wskaźnik „poprawna = jedyna najdłuższa”

Bank i opcje nie były zmieniane, dlatego wskaźniki pozostają bez zmian:

| Dział | Wynik |
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

Każdy dział pozostaje ≤16%. Najkrótsze explanation: 300 znaków; poniżej 200 znaków: 0. Nie zmieniono banku, liter odpowiedzi ani statusów.

## Quality Gate i ograniczenia

- CI dla partii B-01–04: PASS, run [#40214046409](../actions/runs/40214046409).
- CI dla partii B-05–08: PASS, run [#40214125950](../actions/runs/40214125950).
- CI dla partii B-09–13: PASS, run [#40214214283](../actions/runs/40214214283).
- Test słowniczka jest blokujący; jego zakres jest jawnie ograniczony do ustalonej listy terminów.
- Nie stwierdzono potwierdzonej sprzeczności prawnej, więc nie zmieniano merytoryki banku.
- Hasła i materiały pozostają do niezależnej recenzji specjalisty; niczego nie oznaczono jako `verified`.
- Nie rozpoczęto kursu cystern ani innej specjalizacji.
