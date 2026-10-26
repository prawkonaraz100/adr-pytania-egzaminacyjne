# Etap 4x25 — raport końcowy: czytelność explanation i synchronizacja egzaminów

- Data: 2026-10-26.
- Punkt wyjścia: main przed końcową kontrolą ca38dc43ec0700b2d6ee3c83a019300ef90def4c; końcowa gałąź opiera się na świeżym main, a Quality Gate weryfikuje wszystkie zmiany.
- Zakres: bank ADR-B-0001–0609, wszystkie odpowiedzi A/B/C, explanation, pytania z przeczeniem, podobieństwo stemów i warianty egzaminu próbnego 001–005.

## Wynik redakcyjny

| Kontrola | Wynik |
|---|---:|
| Pytania w banku przejrzane w partiach | 609 |
| Explanation przepisane w partiach | 0 |
| Dodatkowa korekta po skanie całego banku | 1 — ADR-B-0197 |
| Explanation poniżej 200 znaków | 0 |
| Najkrótsze explanation | 300 znaków |
| Zdania dłuższe niż 35 słów (heurystyka) | 0 |
| Potwierdzone duplikaty semantyczne | 0 |
| Pytania ze stemem zawierającym przeczenie/zakaz sprawdzone | 106 |
| Kandydaci heurystyki 4x11 przeczytani w partiach | 86 |
| Kandydaci skrótów/pojęć z globalnego skanu sprawdzeni | 36; nie znaleziono dodatkowego potwierdzonego braku objaśnienia |
| Rekordy oznaczone verified | 0 |

### Korekta końcowa ADR-B-0197

Wyjaśnienie rozpoczynało się od numeru przepisu. Przepisano pierwsze zdanie tak, aby najpierw wyjaśniało sens wyłączenia ilościowego, a dopiero potem podawało podstawę ADR. Zachowano poprawną literę A, treść pytania, dystraktory i status needs_review.

### Pary podobne, ale niepotwierdzone jako duplikaty

- **ADR-B-0071 i ADR-B-0072:** podobny szablon pytania o gaśnice, ale różne DMC (3,5 t i 6 t) i różne wymagane progi; sprawdzają inne zastosowanie tabeli.
- **ADR-B-0042 i ADR-B-0096:** oba pytają o klasę ADR, ale dotyczą różnych materiałów (gazy i nadtlenki organiczne); nie są tym samym pytaniem.

Skan podobieństwa całego banku (tokenowe Jaccard ≥0,60 oraz identyczny zestaw odpowiedzi) nie znalazł innych par. Heurystyka braku jawnego słowa kontrastu dawała wiele fałszywych alarmów, ponieważ nie rozpoznaje porównań opisanych przez klasy, warunki i przykłady zamiast stałych fraz. Nie zmieniano treści tylko po to, aby dopasować je do regexu.

## Wskaźnik „poprawna = jedyna najdłuższa”

- Cały bank: **73/609 = 11.99%**.
- Explanation krótsze niż 200 znaków: **0**.
- Duplikaty ID: **0**.
- Status: 609 needs_review, 0 verified.

| Dział | Liczba pytań | Poprawna jedyną najdłuższą |
|---|---:|---:|
| ADR-B-01 | 45 | 6/45 = 13.33% |
| ADR-B-02 | 56 | 8/56 = 14.29% |
| ADR-B-03 | 49 | 7/49 = 14.29% |
| ADR-B-04 | 46 | 6/46 = 13.04% |
| ADR-B-05 | 43 | 6/43 = 13.95% |
| ADR-B-06 | 45 | 5/45 = 11.11% |
| ADR-B-07 | 48 | 6/48 = 12.50% |
| ADR-B-08 | 42 | 5/42 = 11.90% |
| ADR-B-09 | 46 | 4/46 = 8.70% |
| ADR-B-10 | 55 | 4/55 = 7.27% |
| ADR-B-11 | 43 | 6/43 = 13.95% |
| ADR-B-12 | 44 | 6/44 = 13.64% |
| ADR-B-13 | 47 | 4/47 = 8.51% |

Wszystkie działy są poniżej limitu 18%; najwyższy wynik wynosi 14.29%.

## Partie i PR-y

| Zakres | PR | Status |
|---|---:|---|
| ADR-B-0001–0050 | [#443](https://github.com/prawkonaraz100/adr-pytania-egzaminacyjne/pull/443) | PASS, scalony |
| ADR-B-0051–0100 | [#444](https://github.com/prawkonaraz100/adr-pytania-egzaminacyjne/pull/444) | PASS, scalony |
| ADR-B-0101–0150 | [#445](https://github.com/prawkonaraz100/adr-pytania-egzaminacyjne/pull/445) | PASS, scalony |
| ADR-B-0151–0200 | [#446](https://github.com/prawkonaraz100/adr-pytania-egzaminacyjne/pull/446) | PASS, scalony; follow-up ADR-B-0197 poniżej |
| ADR-B-0201–0250 | [#447](https://github.com/prawkonaraz100/adr-pytania-egzaminacyjne/pull/447) | PASS, scalony |
| ADR-B-0251–0300 | [#448](https://github.com/prawkonaraz100/adr-pytania-egzaminacyjne/pull/448) | PASS, scalony |
| ADR-B-0301–0350 | [#449](https://github.com/prawkonaraz100/adr-pytania-egzaminacyjne/pull/449) | PASS, scalony |
| ADR-B-0351–0400 | [#450](https://github.com/prawkonaraz100/adr-pytania-egzaminacyjne/pull/450) | PASS, scalony |
| ADR-B-0401–0450 | [#451](https://github.com/prawkonaraz100/adr-pytania-egzaminacyjne/pull/451) | PASS, scalony |
| ADR-B-0451–0500 | [#452](https://github.com/prawkonaraz100/adr-pytania-egzaminacyjne/pull/452) | PASS, scalony |
| ADR-B-0501–0550 | [#453](https://github.com/prawkonaraz100/adr-pytania-egzaminacyjne/pull/453) | PASS, scalony |
| ADR-B-0551–0600 | [#454](https://github.com/prawkonaraz100/adr-pytania-egzaminacyjne/pull/454) | PASS, scalony |
| ADR-B-0601–0609 | [#455](https://github.com/prawkonaraz100/adr-pytania-egzaminacyjne/pull/455) | PASS, scalony |

## Egzaminy próbne 001–005 — kontrola końcowa

Po korekcie explanation ADR-B-0197 odświeżono pole source_bank_head we wszystkich pięciu arkuszach i pięciu kluczach. Żaden wariant nie zawiera ADR-B-0197, więc nie było potrzeby zmieniać pytań, odpowiedzi ani regenerować układu arkuszy.

| Wariant | Pytań / klucz | Rozkład A/B/C | Najdłuższa seria | Błędy synchronizacji |
|---|---|---|---:|---:|
| 001 | 30 / 30 | 10/10/10 | 3 | 0 |
| 002 | 30 / 30 | 10/10/10 | 3 | 0 |
| 003 | 30 / 30 | 10/10/10 | 3 | 0 |
| 004 | 30 / 30 | 10/10/10 | 3 | 0 |
| 005 | 30 / 30 | 10/10/10 | 3 | 0 |

Dodatkowo potwierdzono: wszystkie pięć arkuszy i kluczy wskazuje aktualny blob banku; wszystkie ID istnieją, nie powtarzają się w arkuszu ani między wariantami, treść i opcje zgadzają się z bankiem, klucze wskazują poprawny tekst odpowiedzi, a explanation odpowiadają bankowi po uwzględnieniu przestawienia liter A/B/C.

## Przekazanie do specjalisty

Wynik 4x24 i rejestr zbiorczy znajdują się w [rejestrze 4x24](../../review/specialist/ETAP-4X24-POZYCJE-BEZ-CYTATU-MI.md). Świeży indeks wykazuje **121** rekordów bez potwierdzonego dosłownego fragmentu MI, choć wcześniejsza prośba wskazywała 120. Zachowano wszystkie ID; nie ponawiano wyszukiwania ani pobierania PDF/MI. Te rekordy pozostają do niezależnego porównania z oficjalnym tekstem Dz.U.

## Status końcowy

Bank zawiera 609 pytań; wszystkie pozostają needs_review. Nie zmieniono żadnej poprawnej odpowiedzi ani statusu weryfikacji. Quality Gate CI jest wymaganym testem końcowym; ten raport nie stanowi prawnej recenzji ADR.
