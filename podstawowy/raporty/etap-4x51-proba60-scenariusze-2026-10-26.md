# Etap 4x51 — próbka 60 explanation i kontrola scenariuszy

- Data: 26.10.2026.
- Świeży punkt bazowy `main`: `215c3692af2ad0786aa16ed224cafa024b1ae2b0` (PR #500).
- Gałąź: `stage4x51-proba60-scenariusze`.
- Zakres: kurs podstawowy ADR בלבד; brak zmian statusów prawnych.

## Stan po 4x50

- Bank: 609 pytań, 609 `needs_review`, 0 `verified`, duplikaty ID: 0.
- Quality Gate na main: PASS, run [#40363578704](https://github.com/prawkonaraz100/adr-pytania-egzaminacyjne/actions/runs/40363578704).
- „Poprawna = jedyna najdłuższa”: 72/609 = 11.82%; najwyższy dział 14.29%.
- Explanation minimum 300 znaków; poniżej 200: 0.
- Raport i wpis 4x50 znalezione w repo/Issue #10; nie wymagały uzupełnienia.

## Próbka 60 — metoda i wynik

Seed: `2026102651`; LCG `state = (1664525 × state + 1013904223) mod 2^32`, Fisher–Yates. Aby nie powtarzać ID, wykluczono wszystkie ID wymienione w raportach 4x45, 4x46, 4x48, 4x49 i 4x50 (łącznie 320 różnych ID w tych dokumentach; pula po wykluczeniu 289 rekordów). Wybrano 60 ID:

1. `ADR-B-0164` — bez zmiany: explanation czytelne, podaje sens poprawnej odpowiedzi, odnosi się do istotnych błędnych opcji i kończy podstawą ADR
2. `ADR-B-0548` — **przepisano explanation**
3. `ADR-B-0058` — bez zmiany: explanation czytelne, podaje sens poprawnej odpowiedzi, odnosi się do istotnych błędnych opcji i kończy podstawą ADR
4. `ADR-B-0168` — bez zmiany: explanation czytelne, podaje sens poprawnej odpowiedzi, odnosi się do istotnych błędnych opcji i kończy podstawą ADR
5. `ADR-B-0468` — bez zmiany: explanation czytelne, podaje sens poprawnej odpowiedzi, odnosi się do istotnych błędnych opcji i kończy podstawą ADR
6. `ADR-B-0555` — bez zmiany: explanation czytelne, podaje sens poprawnej odpowiedzi, odnosi się do istotnych błędnych opcji i kończy podstawą ADR
7. `ADR-B-0499` — bez zmiany: explanation czytelne, podaje sens poprawnej odpowiedzi, odnosi się do istotnych błędnych opcji i kończy podstawą ADR
8. `ADR-B-0099` — bez zmiany: explanation czytelne, podaje sens poprawnej odpowiedzi, odnosi się do istotnych błędnych opcji i kończy podstawą ADR
9. `ADR-B-0507` — **przepisano explanation**
10. `ADR-B-0174` — bez zmiany: explanation czytelne, podaje sens poprawnej odpowiedzi, odnosi się do istotnych błędnych opcji i kończy podstawą ADR
11. `ADR-B-0475` — bez zmiany: explanation czytelne, podaje sens poprawnej odpowiedzi, odnosi się do istotnych błędnych opcji i kończy podstawą ADR
12. `ADR-B-0405` — **przepisano explanation**
13. `ADR-B-0254` — bez zmiany: explanation czytelne, podaje sens poprawnej odpowiedzi, odnosi się do istotnych błędnych opcji i kończy podstawą ADR
14. `ADR-B-0187` — bez zmiany: explanation czytelne, podaje sens poprawnej odpowiedzi, odnosi się do istotnych błędnych opcji i kończy podstawą ADR
15. `ADR-B-0248` — bez zmiany: explanation czytelne, podaje sens poprawnej odpowiedzi, odnosi się do istotnych błędnych opcji i kończy podstawą ADR
16. `ADR-B-0122` — bez zmiany: explanation czytelne, podaje sens poprawnej odpowiedzi, odnosi się do istotnych błędnych opcji i kończy podstawą ADR
17. `ADR-B-0097` — bez zmiany: explanation czytelne, podaje sens poprawnej odpowiedzi, odnosi się do istotnych błędnych opcji i kończy podstawą ADR
18. `ADR-B-0149` — bez zmiany: explanation czytelne, podaje sens poprawnej odpowiedzi, odnosi się do istotnych błędnych opcji i kończy podstawą ADR
19. `ADR-B-0217` — **przepisano explanation**
20. `ADR-B-0269` — bez zmiany: explanation czytelne, podaje sens poprawnej odpowiedzi, odnosi się do istotnych błędnych opcji i kończy podstawą ADR
21. `ADR-B-0549` — bez zmiany: explanation czytelne, podaje sens poprawnej odpowiedzi, odnosi się do istotnych błędnych opcji i kończy podstawą ADR
22. `ADR-B-0247` — bez zmiany: explanation czytelne, podaje sens poprawnej odpowiedzi, odnosi się do istotnych błędnych opcji i kończy podstawą ADR
23. `ADR-B-0144` — bez zmiany: explanation czytelne, podaje sens poprawnej odpowiedzi, odnosi się do istotnych błędnych opcji i kończy podstawą ADR
24. `ADR-B-0026` — bez zmiany: explanation czytelne, podaje sens poprawnej odpowiedzi, odnosi się do istotnych błędnych opcji i kończy podstawą ADR
25. `ADR-B-0367` — bez zmiany: explanation czytelne, podaje sens poprawnej odpowiedzi, odnosi się do istotnych błędnych opcji i kończy podstawą ADR
26. `ADR-B-0550` — bez zmiany: explanation czytelne, podaje sens poprawnej odpowiedzi, odnosi się do istotnych błędnych opcji i kończy podstawą ADR
27. `ADR-B-0328` — bez zmiany: explanation czytelne, podaje sens poprawnej odpowiedzi, odnosi się do istotnych błędnych opcji i kończy podstawą ADR
28. `ADR-B-0345` — bez zmiany: explanation czytelne, podaje sens poprawnej odpowiedzi, odnosi się do istotnych błędnych opcji i kończy podstawą ADR
29. `ADR-B-0380` — bez zmiany: explanation czytelne, podaje sens poprawnej odpowiedzi, odnosi się do istotnych błędnych opcji i kończy podstawą ADR
30. `ADR-B-0046` — bez zmiany: explanation czytelne, podaje sens poprawnej odpowiedzi, odnosi się do istotnych błędnych opcji i kończy podstawą ADR
31. `ADR-B-0016` — bez zmiany: explanation czytelne, podaje sens poprawnej odpowiedzi, odnosi się do istotnych błędnych opcji i kończy podstawą ADR
32. `ADR-B-0094` — bez zmiany: explanation czytelne, podaje sens poprawnej odpowiedzi, odnosi się do istotnych błędnych opcji i kończy podstawą ADR
33. `ADR-B-0235` — bez zmiany: explanation czytelne, podaje sens poprawnej odpowiedzi, odnosi się do istotnych błędnych opcji i kończy podstawą ADR
34. `ADR-B-0093` — bez zmiany: explanation czytelne, podaje sens poprawnej odpowiedzi, odnosi się do istotnych błędnych opcji i kończy podstawą ADR
35. `ADR-B-0312` — bez zmiany: explanation czytelne, podaje sens poprawnej odpowiedzi, odnosi się do istotnych błędnych opcji i kończy podstawą ADR
36. `ADR-B-0484` — bez zmiany: explanation czytelne, podaje sens poprawnej odpowiedzi, odnosi się do istotnych błędnych opcji i kończy podstawą ADR
37. `ADR-B-0021` — bez zmiany: explanation czytelne, podaje sens poprawnej odpowiedzi, odnosi się do istotnych błędnych opcji i kończy podstawą ADR
38. `ADR-B-0352` — bez zmiany: explanation czytelne, podaje sens poprawnej odpowiedzi, odnosi się do istotnych błędnych opcji i kończy podstawą ADR
39. `ADR-B-0477` — bez zmiany: explanation czytelne, podaje sens poprawnej odpowiedzi, odnosi się do istotnych błędnych opcji i kończy podstawą ADR
40. `ADR-B-0377` — bez zmiany: explanation czytelne, podaje sens poprawnej odpowiedzi, odnosi się do istotnych błędnych opcji i kończy podstawą ADR
41. `ADR-B-0253` — bez zmiany: explanation czytelne, podaje sens poprawnej odpowiedzi, odnosi się do istotnych błędnych opcji i kończy podstawą ADR
42. `ADR-B-0375` — bez zmiany: explanation czytelne, podaje sens poprawnej odpowiedzi, odnosi się do istotnych błędnych opcji i kończy podstawą ADR
43. `ADR-B-0160` — bez zmiany: explanation czytelne, podaje sens poprawnej odpowiedzi, odnosi się do istotnych błędnych opcji i kończy podstawą ADR
44. `ADR-B-0292` — bez zmiany: explanation czytelne, podaje sens poprawnej odpowiedzi, odnosi się do istotnych błędnych opcji i kończy podstawą ADR
45. `ADR-B-0297` — bez zmiany: explanation czytelne, podaje sens poprawnej odpowiedzi, odnosi się do istotnych błędnych opcji i kończy podstawą ADR
46. `ADR-B-0208` — bez zmiany: explanation czytelne, podaje sens poprawnej odpowiedzi, odnosi się do istotnych błędnych opcji i kończy podstawą ADR
47. `ADR-B-0213` — bez zmiany: explanation czytelne, podaje sens poprawnej odpowiedzi, odnosi się do istotnych błędnych opcji i kończy podstawą ADR
48. `ADR-B-0412` — bez zmiany: explanation czytelne, podaje sens poprawnej odpowiedzi, odnosi się do istotnych błędnych opcji i kończy podstawą ADR
49. `ADR-B-0040` — bez zmiany: explanation czytelne, podaje sens poprawnej odpowiedzi, odnosi się do istotnych błędnych opcji i kończy podstawą ADR
50. `ADR-B-0303` — bez zmiany: explanation czytelne, podaje sens poprawnej odpowiedzi, odnosi się do istotnych błędnych opcji i kończy podstawą ADR
51. `ADR-B-0118` — bez zmiany: explanation czytelne, podaje sens poprawnej odpowiedzi, odnosi się do istotnych błędnych opcji i kończy podstawą ADR
52. `ADR-B-0279` — bez zmiany: explanation czytelne, podaje sens poprawnej odpowiedzi, odnosi się do istotnych błędnych opcji i kończy podstawą ADR
53. `ADR-B-0355` — bez zmiany: explanation czytelne, podaje sens poprawnej odpowiedzi, odnosi się do istotnych błędnych opcji i kończy podstawą ADR
54. `ADR-B-0360` — **przepisano explanation**
55. `ADR-B-0215` — bez zmiany: explanation czytelne, podaje sens poprawnej odpowiedzi, odnosi się do istotnych błędnych opcji i kończy podstawą ADR
56. `ADR-B-0197` — bez zmiany: explanation czytelne, podaje sens poprawnej odpowiedzi, odnosi się do istotnych błędnych opcji i kończy podstawą ADR
57. `ADR-B-0293` — bez zmiany: explanation czytelne, podaje sens poprawnej odpowiedzi, odnosi się do istotnych błędnych opcji i kończy podstawą ADR
58. `ADR-B-0022` — bez zmiany: explanation czytelne, podaje sens poprawnej odpowiedzi, odnosi się do istotnych błędnych opcji i kończy podstawą ADR
59. `ADR-B-0407` — bez zmiany: explanation czytelne, podaje sens poprawnej odpowiedzi, odnosi się do istotnych błędnych opcji i kończy podstawą ADR
60. `ADR-B-0212` — bez zmiany: explanation czytelne, podaje sens poprawnej odpowiedzi, odnosi się do istotnych błędnych opcji i kończy podstawą ADR

### Poprawione wyjaśnienia

| ID | Problem | Korekta |
|---|---|---|
| ADR-B-0548 | Powtórzenie tej samej myśli o częściowym rozładunku i podpisie protokołu. | Rozdzielono utrzymujące się zagrożenie od formalnego potwierdzenia czynności; podano warunek zdjęcia nalepek. ADR 5.3.1.1.5. |
| ADR-B-0507 | Powtórzenie informacji o poziomej linii i niepotrzebne rozbicie wyjaśnienia. | Jasna reguła: numer zagrożenia u góry, numer UN na dole; wskazano, dlaczego zamiana linii nie naprawia tablicy. ADR 5.3.2.2.2. |
| ADR-B-0405 | Dwa zdania przekazywały tę samą informację o pieczątce i publikowaniu tras. | Wyjaśniono cel planu ochrony i zasadę ograniczonego dostępu do informacji. ADR 1.10.3.2.2(g). |
| ADR-B-0217 | Powtórzenie „druga ósemka nie jest numerem paczki” oraz niespójne nazwanie numeru. | Uproszczono znaczenie powtórzonej cyfry i wyjaśniono, że numer należy czytać jako całość. ADR 5.3.2.3.1. |
| ADR-B-0360 | Nieprofesjonalne określenie „absurdalny nakaz palenia”. | Zastąpiono neutralnym wyjaśnieniem, że obecność kierowcy ani światła awaryjne nie uchylają zakazu. ADR 8.3.5. |

Każde nowe explanation ma 4 zdania i 306–438 znaków. Zachowano poprawne litery, treść opcji, ID, źródła i status `needs_review`.

## Scenariusze praktyczne

Skontrolowano strukturę wszystkich 39 scenariuszy z `podstawowy/praktyka/scenariusze-13-dzialow.json`: liczbę kroków, powiązania `question_ids`, zgodność modułu, podsumowanie dla kursanta, podstawę ADR i listę typowych błędów. Wynik:

| Dział | Scenariusze | Min. kroków | Min. pytań/scenariusz | Brakujące ID | ID z innego działu | Braki strukturalne |
|---|---:|---:|---:|---:|---:|---:|
| ADR-B-01 | 3 | 4 | 3 | 0 | 0 | 0 |
| ADR-B-02 | 3 | 4 | 2 | 0 | 0 | 0 |
| ADR-B-03 | 3 | 4 | 2 | 0 | 0 | 0 |
| ADR-B-04 | 3 | 4 | 3 | 0 | 0 | 0 |
| ADR-B-05 | 3 | 4 | 3 | 0 | 0 | 0 |
| ADR-B-06 | 3 | 4 | 3 | 0 | 0 | 0 |
| ADR-B-07 | 3 | 4 | 1 | 0 | 0 | 0 |
| ADR-B-08 | 3 | 4 | 3 | 0 | 0 | 0 |
| ADR-B-09 | 3 | 4 | 3 | 0 | 0 | 0 |
| ADR-B-10 | 3 | 4 | 2 | 0 | 0 | 0 |
| ADR-B-11 | 3 | 4 | 3 | 0 | 0 | 0 |
| ADR-B-12 | 3 | 4 | 2 | 0 | 0 | 0 |
| ADR-B-13 | 3 | 4 | 3 | 0 | 0 | 0 |
| **Łącznie** | **39** | — | — | **0** | **0** | **0** |

Każdy scenariusz ma co najmniej 3 kroki i powiązane pytania z właściwego modułu. Nie znaleziono potwierdzonej luki programu, której nie obejmowałoby żadne pytanie; nie dodano pytań ani nie zmieniano egzaminów próbnych 001–005.

## Kontrola jakości po zmianach

| Dział | Pytania | Poprawna jedyna najdłuższa | Wskaźnik |
|---|---:|---:|---:|
| ADR-B-01 | 45 | 6 | 13.33% |
| ADR-B-02 | 56 | 7 | 12.50% |
| ADR-B-03 | 49 | 7 | 14.29% |
| ADR-B-04 | 46 | 6 | 13.04% |
| ADR-B-05 | 43 | 5 | 11.63% |
| ADR-B-06 | 45 | 5 | 11.11% |
| ADR-B-07 | 48 | 6 | 12.50% |
| ADR-B-08 | 42 | 5 | 11.90% |
| ADR-B-09 | 46 | 4 | 8.70% |
| ADR-B-10 | 55 | 4 | 7.27% |
| ADR-B-11 | 43 | 6 | 13.95% |
| ADR-B-12 | 44 | 6 | 13.64% |
| ADR-B-13 | 47 | 5 | 10.64% |
| **Łącznie** | **609** | **72** | **11.82%** |

- Duplikaty ID: 0.
- Explanation poniżej 200 znaków: 0; minimum po zmianach: 300 znaków.
- Wszystkie statusy prawne pozostają `needs_review`; nie oznaczono żadnego pytania jako `verified`.
- Klucze egzaminów 001–005 bez zmian, ponieważ poprawne litery i opcje nie uległy zmianie.

## Testy

Nie ma lokalnego checkoutu repozytorium w tym środowisku, a próba `git clone` nie powiodła się z powodu braku rozwiązywania DNS dla GitHub. Nie deklaruję zatem wykonania lokalnych testów. Pełny Quality Gate CI na PR jest warunkiem scalenia; raport metryk powyżej został policzony z pobranej zawartości banku i scenariuszy.
