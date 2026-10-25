# ETAP 4x8 — raport końcowy: jakość dystraktorów i wyjaśnień

- Data: 25.10.2026.
- Punkt wyjścia dla raportu: `main` `874dc79d6973b382036ff0081a30caead35e968f`.
- Zakres: wyłącznie kurs podstawowy, wszystkie 609 pytań i wszystkie 13 lekcji.

## Partie i PR-y

| Zakres | PR | Wynik |
|---|---|---|
| B-01–04 | [#331](../pull/331) | PASS CI, scalony |
| B-05–08 | [#332](../pull/332) | PASS CI, scalony |
| B-09–13 | [#333](../pull/333) | PASS CI, scalony |

Raporty szczegółowe:
- [B-01–04 — dystraktory i wyjaśnienia](etap-4x8-dystraktory-wyjasnienia-01-04-2026-10-25.md)
- [B-05–08 — dystraktory i wyjaśnienia](etap-4x8-dystraktory-wyjasnienia-05-08-2026-10-25.md)
- [B-09–13 — dystraktory i wyjaśnienia](etap-4x8-dystraktory-wyjasnienia-09-13-2026-10-25.md)

## Podsumowanie zmian

- Sprawdzono 609 pytań: 196 w B-01–04, 178 w B-05–08 i 235 w B-09–13.
- Poprawiono **9 dystraktorów w 7 pytaniach**: ADR-B-0350, ADR-B-0220, ADR-B-0291, ADR-B-0324, ADR-B-0388, ADR-B-0413 i ADR-B-0586. Usunięto przykłady zbyt łatwe do odrzucenia (m.in. kolor kabiny/opakowania lub logo) i zastąpiono je typowymi błędami w interpretacji wymagań, dokumentów, oznakowania albo upoważnień.
- Przeredagowano **7 wyjaśnień** tak, aby w prostym języku tłumaczyły poprawną odpowiedź i powód błędności pozostałych opcji. Każde ma 2–5 zdań merytorycznych, z krótką podstawą ADR.
- Dodano sekcję „Najczęstsze błędy kursantów” do wszystkich **13 lekcji**, z linkiem do słowniczka i odniesieniami do przepisów.
- Zsynchronizowano migawki zmienionych rekordów w audycie sekwencyjnym i rejestrze przeglądu klauzul.
- Zsynchronizowano arkusze/klucze egzaminów próbnych 001–005 z aktualnym bankiem. Warianty 001 i 002 zawierały zmienione pytania; ich opcje i wyjaśnienia w kluczach zostały odświeżone. W pozostałych wariantach odświeżono `source_bank_head`; CI potwierdziło zgodność wszystkich pięciu wariantów i kluczy.
- Nie zmieniono ID ani poprawnych liter. Żadnego pytania nie oznaczono jako `verified`.

## Metryki po zmianach

| Kontrola | Wynik |
|---|---:|
| Pytania w banku | 609 |
| Duplikaty ID | 0 |
| Poprawna odpowiedź jest jedyną najdłuższą | 81/609 = 13,30% |
| Minimalna długość explanation | 300 znaków |
| Explanation poniżej 200 znaków | 0 |
| `needs_review` | 609 |
| `verified` | 0 |

### Wskaźnik „poprawna = jedyna najdłuższa” per moduł

| Dział | Wynik | Limit |
|---|---:|---:|
| B-10 | 4/55 = 7.27% | ≤18% |
| B-11 | 7/43 = 16.28% | ≤18% |
| B-12 | 7/44 = 15.91% | ≤18% |
| B-13 | 4/47 = 8.51% | ≤18% |
| B-01 | 8/45 = 17.78% | ≤18% |
| B-02 | 9/56 = 16.07% | ≤18% |
| B-03 | 7/49 = 14.29% | ≤18% |
| B-04 | 8/46 = 17.39% | ≤18% |
| B-05 | 6/43 = 13.95% | ≤18% |
| B-06 | 5/45 = 11.11% | ≤18% |
| B-07 | 6/48 = 12.50% | ≤18% |
| B-08 | 6/42 = 14.29% | ≤18% |
| B-09 | 4/46 = 8.70% | ≤18% |

Wszystkie działy są poniżej 18%; B-01 i B-04 mają najmniejszy zapas, więc dalsze redakcje wymagają ponownego sprawdzenia wskaźnika modułowego.

## Quality Gate

Końcowy Quality Gate dla partii B-09–13 zakończył się PASS: [run #40206467745](../actions/runs/40206467745). Wszystkie trzy PR-y zostały scalone po PASS CI; testy sprawdzają też aktualność snapshotów audytowych i synchronizację wariantów egzaminu z bankiem.

## Zastrzeżenia

- Wskaźniki długości i testy automatyczne nie potwierdzają poprawności prawnej odpowiedzi.
- Zmiany są redakcyjne/dydaktyczne i oparte na wskazanych podstawach ADR; pełne porównanie każdego pytania z polskim tekstem urzędowym, sprostowaniem i niezależna akceptacja specjalisty nadal pozostają wymagane.
- Wszystkie pytania pozostają `needs_review`; nie rozpoczęto kursu cystern ani innej specjalizacji.
