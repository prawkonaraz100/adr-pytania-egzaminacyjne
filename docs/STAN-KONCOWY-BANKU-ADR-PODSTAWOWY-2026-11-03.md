# Bank pytań ADR — kurs podstawowy: raport zamknięcia do recenzji specjalisty

**Stan na 3 listopada 2026 r. — etap zamknięcia 4x355.** Zgodnie z REGUŁĄ KOŃCA z 2.11 **zakończono dopisywanie pytań**, ponieważ wszystkie kompetencje teoretyczne mają co najmniej sześć powiązanych pytań. Nie obejmuje kursu cystern, Kod 95 ani innych kursów.

## Stan banku

| Wskaźnik | Wartość |
|---|---:|
| Pytania w banku | **780** |
| Zakres ID | ADR-B-0001 – ADR-B-0780 |
| Status `needs_review` | **780** |
| Status `verified` | **0** |
| Moduły/lekcje | **13** |
| Kompetencje teoretyczne | **104** |
| Teoretyczne z mniej niż 6 pytaniami | **0** |
| Kompetencje praktyczne (osobno, nie wliczane do progu sześciu) | **3** |
| Rozkład poprawnych A/B/C | **258 / 291 / 231** |
| Poprawna odpowiedź jedyną najdłuższą | **85/780 = 10,90%** |
| Najwyższy wskaźnik w pojedynczym dziale | **15,22%** |
| Git blob SHA `podstawowy/questions.jsonl` | `d71ad1c3595b2c54f240178e30d0b2613fff9b41` |

### Rozkład pytań według modułów

| Moduł | Pytania | Moduł | Pytania |
|---|---:|---|---:|
| ADR-B-01 | 54 | ADR-B-08 | 53 |
| ADR-B-02 | 89 | ADR-B-09 | 62 |
| ADR-B-03 | 60 | ADR-B-10 | 57 |
| ADR-B-04 | 50 | ADR-B-11 | 46 |
| ADR-B-05 | 87 | ADR-B-12 | 48 |
| ADR-B-06 | 66 | ADR-B-13 | 54 |
| ADR-B-07 | 54 | **Razem** | **780** |

## Ostatnie pięć kompetencji zakończonych zgodnie z regułą

| Partia | Pytanie | Kompetencja | Wynik po partii: teoretyczne z mniej niż 6 |
|---|---|---|---:|
| 4x350 | ADR-B-0776 | ADR-B-12-K04 | 4 |
| 4x351 | ADR-B-0777 | ADR-B-13-K03 | 3 |
| 4x352 | ADR-B-0778 | ADR-B-13-K05 | 2 |
| 4x353 | ADR-B-0779 | ADR-B-13-K06 | 1 |
| 4x354 | ADR-B-0780 | ADR-B-13-K07 | **0** |

**STOP**: po ADR-B-0780 nie dopisywać kolejnych pytań na potrzeby domknięcia pokrycia. Zmiany merytoryczne wyłącznie po wykryciu i udokumentowaniu potwierdzonego błędu, zgodnie z oddzielnym procesem recenzji.

## Artefakty przekazania

- **Bank zamrożony do recenzji:** `podstawowy/questions.jsonl`; SHA podano wyżej.
- **Mapa kompetencji:** `podstawowy/kompetencje.json`; wszystkie 104 kompetencje teoretyczne mają minimum 6 powiązanych pytań; 3 praktyczne zachowują odrębny status.
- **Pięć wariantów egzaminu próbnego i pięć kluczy:** `podstawowy/egzamin-probny/wariant-001.json`–`005.json` oraz `klucz-001.json`–`005.json`; wszystkie dziesięć plików wskazuje ten sam blob SHA `d71ad1c3595b2c54f240178e30d0b2613fff9b41`. Każdy wariant obejmuje 30 pytań.
- **Snapshoty recenzji:** `review/sequential/780-780.json` i `review/legal-clauses/780-780.json` dla ostatniego pytania; istniejące wcześniejsze snapshoty pozostają w repo. Sprawdzenie spójności całego banku jest wymagane w Quality Gate.
- **Pakiet specjalisty:** `review/specialist/PAKIET-0780-MANIFEST.json`, aktualny rejestr `review/specialist/REJESTR-AKTUALNY-0001-0780.md` (780 unikalnych wierszy), rejestr partii `review/specialist/REJESTR-0780-0780.md`, instrukcje w `review/specialist/INSTRUKCJA-RECENZJI.md`.
- **Źródła i status dowodów:** `review/legal-polish/stage4w4-literal-verification-ledger-0001-0609.json` i `review/legal-polish/stage4w4-literal-verification-ledger-0610-0678.json`; pola `sources[].reference` odpowiadają zapisom ledgera.
- **Historyczny przebieg i Quality Gate:** raporty w `podstawowy/raporty/`, dziennik Issue #10 oraz PR #822–#826.

## Granice gotowości

Bank jest **zamknięty redakcyjnie i gotowy do rozpoczęcia niezależnego przeglądu specjalisty** — nie jest jeszcze zweryfikowany prawnie ani dopuszczony do publikacji jako certyfikowany zbiór. Wszystkie 780 pozycji pozostają `needs_review`; `verified=0`, formalnych zatwierdzeń: 0. W pakiecie jest 723 pozycje bez pobranego dosłownego polskiego fragmentu przepisu oraz 27 pozycji z kontrolą źródła, ale bez zakończonego pełnego porównania literalnego. Przed zatwierdzeniem specjalista musi ocenić podstawę ADR 2025, poprawność A/B/C, dostępność dokumentu źródłowego i zapisać wyniki zgodnie z procedurą repo. Samo przejście CI nie oznacza weryfikacji prawnej.

**Końcowy status projektu: „bank zamknięty, gotowy do przeglądu specjalisty” (nie „zweryfikowany”).**
