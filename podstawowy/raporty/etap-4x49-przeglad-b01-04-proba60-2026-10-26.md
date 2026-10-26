# Etap 4x49 — przegląd lekcji B-01–B-04 i nowa próbka 60 explanation

- Data: 2026-10-26.
- Baza: świeży `main` `1248360df8dc6fc3b4f8325026d264b83714af51`, po PR #495.
- Zakres: kurs podstawowy; nie zmieniano statusów weryfikacji prawnej.

## Potwierdzenie stanu po 4x48/4x49

- Bank: 609 pytań, wszystkie `needs_review`, 0 `verified`; brak duplikatów ID.
- Ostatni Quality Gate: PASS, run [#40353876133](https://github.com/prawkonaraz100/adr-pytania-egzaminacyjne/actions/runs/40353876133), `structure-and-tests` success.
- Wskaźnik „poprawna = jedyna najdłuższa”: 72/609 = 11,82% globalnie; maksimum działu 14,29%.
- Explanation: minimum 300 znaków, 0 poniżej 200.
- Scenariusze: 39/39, po 3 na dział; PR #495 dodał blokującą kontrolę struktury scenariuszy.

## Przegląd lekcji B-01–B-04

| Lekcja | Wprowadzenie „po co” | Podsumowanie | Pytania kontrolne | Referencje bankowe | Brakujące/obce ID |
|---|---|---|---|---:|---|
| B-01 | PASS | PASS | PASS | 45 | 0 / 0 |
| B-02 | PASS | PASS | PASS | 56 | 0 / 0 |
| B-03 | PASS | PASS | PASS | 49 | 0 / 0 |
| B-04 | PASS | PASS | PASS | 46 | 0 / 0 |

W każdej z czterech lekcji jest praktyczne wprowadzenie, sekcja podsumowująca oraz „Sprawdź się”. Wszystkie ID pytań występują w banku i należą do właściwego działu. W tej kontroli nie znaleziono potwierdzonego braku strukturalnego ani konkretnej sprzeczności, którą można bezpiecznie poprawić wyłącznie na podstawie treści repo. Nie zmieniano tekstu merytorycznego na wyczucie. Przegląd nie jest formalną recenzją prawną.

## Nowa próbka explanation — 60 pytań

- Seed: `2026102649`.
- Wykluczenie: wszystkie ID wymienione w raportach 4x45, 4x46 i 4x48; to celowo szerszy zbiór niż same rekordy próbek, aby uniknąć powtórnego wyboru.
- Pula po wykluczeniu: 409 pytań; sprawdzono 60 nowych ID.
- Wynik redakcyjny: **0 explanation wymagało przepisania**. Każde z 60 miało 3–5 zdań i 300+ znaków, rozpoczynało od sensu poprawnej odpowiedzi, wyjaśniało kluczowy błąd/dystraktor i kończyło podstawą ADR. Kilka terminów specjalistycznych było objaśnionych w samym tekście (np. EQ, DMC, IMDG, ICAO TI, numer UN).
- Wszystkie 60 pozostają `needs_review`; wynik oznacza ocenę czytelności, nie zatwierdzenie poprawności prawnej.

### Lista sprawdzonych ID

`ADR-B-0601`, `ADR-B-0586`, `ADR-B-0576`, `ADR-B-0571`, `ADR-B-0566`, `ADR-B-0561`, `ADR-B-0551`, `ADR-B-0531`, `ADR-B-0526`, `ADR-B-0521`, `ADR-B-0516`, `ADR-B-0511`, `ADR-B-0491`, `ADR-B-0481`, `ADR-B-0476`, `ADR-B-0471`, `ADR-B-0466`, `ADR-B-0461`, `ADR-B-0456`, `ADR-B-0446`, `ADR-B-0441`, `ADR-B-0431`, `ADR-B-0426`, `ADR-B-0416`, `ADR-B-0406`, `ADR-B-0401`, `ADR-B-0396`, `ADR-B-0391`, `ADR-B-0386`, `ADR-B-0381`, `ADR-B-0376`, `ADR-B-0366`, `ADR-B-0356`, `ADR-B-0351`, `ADR-B-0346`, `ADR-B-0336`, `ADR-B-0331`, `ADR-B-0326`, `ADR-B-0316`, `ADR-B-0306`, `ADR-B-0291`, `ADR-B-0281`, `ADR-B-0276`, `ADR-B-0266`, `ADR-B-0256`, `ADR-B-0251`, `ADR-B-0241`, `ADR-B-0231`, `ADR-B-0226`, `ADR-B-0221`, `ADR-B-0201`, `ADR-B-0196`, `ADR-B-0186`, `ADR-B-0181`, `ADR-B-0171`, `ADR-B-0161`, `ADR-B-0156`, `ADR-B-0151`, `ADR-B-0146`, `ADR-B-0141`

### Fałszywe alarmy / uzasadnienie

W tej próbce nie było fałszywych alarmów automatycznej heurystyki do odnotowania, ponieważ selekcja nie była listą alarmów; był to losowy przegląd. Wszystkie 60 wyjaśnień oceniono jako czytelne redakcyjnie. Nie stwierdzono jednozdaniowych odpowiedzi ani wyjaśnień zaczynających się od samego numeru przepisu.

## Kontrola wskaźnika „poprawna = jedyna najdłuższa”

| Dział | Pytań | Jedyna najdłuższa | Wskaźnik |
|---|---:|---:|---:|
| B-01 | 45 | 6 | 13.33% |
| B-02 | 56 | 7 | 12.50% |
| B-03 | 49 | 7 | 14.29% |
| B-04 | 46 | 6 | 13.04% |
| B-05 | 43 | 5 | 11.63% |
| B-06 | 45 | 5 | 11.11% |
| B-07 | 48 | 6 | 12.50% |
| B-08 | 42 | 5 | 11.90% |
| B-09 | 46 | 4 | 8.70% |
| B-10 | 55 | 4 | 7.27% |
| B-11 | 43 | 6 | 13.95% |
| B-12 | 44 | 6 | 13.64% |
| B-13 | 47 | 5 | 10.64% |
| **Łącznie** | **609** | **72** | **11,82%** |

- Najkrótsze explanation: 300 znaków.
- Explanation poniżej 200 znaków: 0.
- Statusy: 609 `needs_review`, 0 `verified`.
- Bank i klucze egzaminów 001–005 bez zmian.

## Testy i ograniczenia

W tym środowisku nie ma lokalnego checkoutu repozytorium, więc nie deklaruję wykonania testów lokalnych. Walidację wykonuje CI na PR; scalanie dopiero po pełnym PASS Quality Gate. Brak zmiany treści banku oznacza brak potrzeby synchronizowania kluczy egzaminów.
