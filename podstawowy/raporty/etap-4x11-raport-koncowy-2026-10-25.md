# Raport końcowy — ETAP 4x11: ręczny przegląd 86 ostrzeżeń explanation

- Data: 25.10.2026.
- Zakres: wyłącznie bank ADR — kurs podstawowy.
- Punkt końcowy po scaleniu PR #340–#342: `93efb73d7fa29700e918d635488e59e9c6108c2a`.
- Bank: 609 pytań, wszystkie `needs_review`, 0 `verified`.

## Podsumowanie wyników

| Partia | Ostrzeżenia przeczytane | Explanation przepisane | Fałszywe alarmy |
|---|---:|---:|---:|
| B-01–04 (PR #340) | 28 | 0 | 28 |
| B-05–08 (PR #341) | 25 | 5 | 20 |
| B-09–13 (PR #342) | 33 | 3 | 30 |
| **Łącznie** | **86** | **8** | **78** |

„Fałszywy alarm” oznacza tu, że ręczne czytanie nie potwierdziło wady dydaktycznej: wyjaśnienie mówi, dlaczego poprawna odpowiedź jest właściwa, wskazuje konkretny błąd w kuszących odpowiedziach i kończy się podstawą ADR. Nie oznacza to niezależnej akceptacji prawnej.

## Lista przepisanych explanation

1. **ADR-B-0085** — poprawiono gramatykę i jaśniej opisano warunek wyłączenia przy kodzie tunelowym; podstawa ADR 8.6.3.3.
2. **ADR-B-0198** — usunięto powtórzenie o miejscu przechowywania świadectwa; ADR 8.1.2.2(a).
3. **ADR-B-0281** — usunięto powtórzenie o danych zastępczych dla numeru UN; ADR 5.2.1.1.
4. **ADR-B-0319** — usunięto powtórzenie o typach pojazdów FL/AT i EX; ADR 9.1.1.2.
5. **ADR-B-0402** — usunięto powtórzenie w wyjaśnieniu elementów planu ochrony; ADR 1.10.3.2.2(d).
6. **ADR-B-0403** — usunięto powtórzenie w wyjaśnieniu procedur zgłaszania i reagowania; ADR 1.10.3.2.2(e).
7. **ADR-B-0417** — usunięto powtórzenie o liczbie i pojemności gaśnic; ADR 8.1.4.1.
8. **ADR-B-0563** — usunięto powtórzenie dotyczące usuwania nalepek po rozładunku; ADR 5.3.1.1.5.

Dla tych ośmiu rekordów nie zmieniano ID, treści pytania, opcji, poprawnej litery ani źródeł. Zmieniono tylko wyjaśnienia, a snapshoty w `review/sequential/` i `review/legal-clauses/` zsynchronizowano. Wszystkie zmienione explanation mają co najmniej 300 znaków.

## Fałszywe alarmy — zestawienie

- **B-01–04:** 28/28 — lista ID znajduje się w [raporcie partii 01–04](etap-4x11-przeglad-explanation-01-04-2026-10-25.md).
- **B-05–08:** 20/25 — lista wszystkich 25 i poprawionych 5 ID znajduje się w [raporcie partii 05–08](etap-4x11-przeglad-explanation-05-08-2026-10-25.md).
- **B-09–13:** 30/33 — lista wszystkich 33 i poprawionych 3 ID znajduje się w [raporcie partii 09–13](etap-4x11-przeglad-explanation-09-13-2026-10-25.md).

W tych przypadkach brak jednego słowa-sygnału nie był traktowany jako wada. Zachowano treść, która już jasno objaśniała rozumowanie i błędne dystraktory.

## Heurystyka — przed i po

- Ostrzeżenia w raporcie 4x10: **86**.
- Po rozszerzeniu słownictwa o „więc”, „czyli”, „oznacza to”, „z tego powodu”, „w rezultacie”, „dzięki temu”, „nie zastępuje”, „nie wystarczy” i inne sygnały kontrastu: **11** kandydatów nadal bez żadnego sygnału.
- Redukcja: **75 ostrzeżeń** (86 → 11).
- Walidator `scripts/check_explanation_heuristics.py` jest doradczy. Wynik 11 nie oznacza 11 błędnych wyjaśnień; każdy taki przypadek wymaga czytania przez człowieka, a brak sygnału nie blokuje dobrej treści.

## Wskaźnik „poprawna = jedyna najdłuższa” po zmianach

Zmiany dotyczyły tylko explanation, więc rozkład długości opcji nie uległ zmianie.

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

Wszystkie działy pozostają ≤16%. Minimalna długość explanation w banku po poprawkach wynosi 300 znaków; żadna nie jest krótsza niż 200.

## Kontrole i granice wniosków

- Quality Gate CI dla partii #340, #341 i #342: PASS.
- Testy integralności snapshotów sekwencyjnego i klauzulowego audytu: PASS po synchronizacji.
- Egzaminy próbne 001–005 nie wymagały zmian, bo nie zmieniano pytań, opcji ani poprawnych liter.
- 609 pytań zachowuje status `needs_review`; nikt nie został oznaczony jako `verified`.
- Przegląd dotyczył języka i jakości dydaktycznej, nie stanowi formalnej weryfikacji prawnej ani potwierdzenia zmian ADR 2027.
- Nie rozpoczęto kursu cystern ani żadnego innego kursu.
