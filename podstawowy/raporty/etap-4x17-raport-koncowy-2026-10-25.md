# Etap 4x17 — raport końcowy: lekcje i scenariusze praktyczne

- Data: 25.10.2026.
- Zakres: kurs podstawowy ADR, wszystkie 13 lekcji i 39 scenariuszy.
- Bank: 609 pytań; statusy: 609 needs_review, 0 verified.

## Partie scalone

| PR | Zakres | Quality Gate |
|---|---|---|
| [#372](../../pull/372) | B-01–03 | PASS; poprawiono brak linku do słowniczka w B-06? Nie — ten błąd wystąpił w partii #373. |
| [#373](../../pull/373) | B-04–06 | PASS po poprawce: pierwsze użycie „Tabela A” w B-06 otrzymało link do kotwicy słowniczka. |
| [#374](../../pull/374) | B-07–09 | PASS |
| [#375](../../pull/375) | B-10–12 | PASS |
| [#376](../../pull/376) | B-13 | PASS |

## Co wykonano

- W 13 lekcjach połączono powtórzone sekcje „Najczęstsze błędy kursantów” z główną sekcją „Typowe błędy kursantów”, zachowując punkty merytoryczne. Każda lekcja ma jedną główną sekcję błędów, a duplikaty nagłówka zostały usunięte.
- Naprawiono uszkodzony termin w B-01 i nagłówek w B-02. W B-06 CI wykryło brak objaśnienia/linku przy pierwszym użyciu „Tabela A”; poprawiono to na tej samej gałęzi i ponowny CI przeszedł.
- W 39 scenariuszach (po 3 na dział) dodano po 3 typowe błędy kursanta z prostym wyjaśnieniem, listę podstaw ADR i krótkie „co zapamiętać”.
- Uzupełniono przewodnik podstawowy/praktyka/SCENARIUSZE.md o ścieżki omawiania scenariuszy dla wszystkich 13 działów.
- Nie zmieniano pytań, odpowiedzi, kluczy ani statusów w banku.

## Kontrola powiązań

| Dział | Pytań | Referencje w lekcji | Błędne/brakujące ID | Scenariusze | Błędne question_ids w scenariuszach |
|---|---:|---:|---:|---:|---:|
| B-01 | 45 | OK | 0 | 3 | 0 |
| B-02 | 56 | OK | 0 | 3 | 0 |
| B-03 | 49 | OK | 0 | 3 | 0 |
| B-04 | 46 | OK | 0 | 3 | 0 |
| B-05 | 43 | OK | 0 | 3 | 0 |
| B-06 | 45 | OK | 0 | 3 | 0 |
| B-07 | 48 | OK | 0 | 3 | 0 |
| B-08 | 42 | OK | 0 | 3 | 0 |
| B-09 | 46 | OK | 0 | 3 | 0 |
| B-10 | 55 | OK | 0 | 3 | 0 |
| B-11 | 43 | OK | 0 | 3 | 0 |
| B-12 | 44 | OK | 0 | 3 | 0 |
| B-13 | 47 | OK | 0 | 3 | 0 |

Preflight potwierdził, że wszystkie ID użyte w lekcjach istnieją w banku i należą do właściwego modułu; wszystkie 39 scenariuszy mają istniejące pytania z właściwego modułu.

## Wskaźniki banku

| Dział | Pytań | „Poprawna = jedyna najdłuższa” | Najkrótsze explanation | Poniżej 200 znaków | verified |
|---|---:|---:|---:|---:|---:|
| B-01 | 45 | 7/45 = 15.56% | 300 znaków | 0 | 0 |
| B-02 | 56 | 8/56 = 14.29% | 300 znaków | 0 | 0 |
| B-03 | 49 | 7/49 = 14.29% | 300 znaków | 0 | 0 |
| B-04 | 46 | 7/46 = 15.22% | 301 znaków | 0 | 0 |
| B-05 | 43 | 6/43 = 13.95% | 300 znaków | 0 | 0 |
| B-06 | 45 | 5/45 = 11.11% | 301 znaków | 0 | 0 |
| B-07 | 48 | 6/48 = 12.5% | 304 znaków | 0 | 0 |
| B-08 | 42 | 7/42 = 16.67% | 303 znaków | 0 | 0 |
| B-09 | 46 | 4/46 = 8.7% | 301 znaków | 0 | 0 |
| B-10 | 55 | 4/55 = 7.27% | 308 znaków | 0 | 0 |
| B-11 | 43 | 6/43 = 13.95% | 300 znaków | 0 | 0 |
| B-12 | 44 | 7/44 = 15.91% | 303 znaków | 0 | 0 |
| B-13 | 47 | 4/47 = 8.51% | 307 znaków | 0 | 0 |

Każdy dział mieści się w progu CI 18%, a wszystkie explanation mają co najmniej 300 znaków. B-08 ma 16,67% według ścisłego kryterium „poprawna = jedyna najdłuższa”; nie zmieniano banku w etapie redakcji lekcji/scenariuszy.

## Ograniczenia i dalszy odbiór

To odbiór dydaktyczny, redakcyjny i śledzenie referencji, nie formalna opinia prawna. Pytania nadal wymagają niezależnej recenzji specjalisty ADR; żadne nie zostało oznaczone jako verified. Scenariusze pozostają symulacjami i nie dowodzą przeprowadzenia zajęć praktycznych.