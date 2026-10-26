# Etap 4x56 — próbka 60 explanation: fałszywe alarmy

- Data: 26.10.2026.
- Świeży `main` przed pracą: `6229c0bc58e47af5ca08ffb3a92db447057ac741` (po PR #505).
- Seed: `2026102656`; LCG `state = (1664525 × state + 1013904223) mod 2^32`, Fisher–Yates.
- Wykluczono ID wymienione w raportach 4x45, 4x46, 4x48, 4x49, 4x50, 4x51 i 4x52: 440 unikalnych ID w tych dokumentach; pozostała pula 169 pytań; próbka 60 ID.

## Wynik ręcznego przeglądu

**60/60 wyjaśnień pozostawiono bez zmian — fałszywe alarmy heurystyki.** Każde ma 3–5 zdań, co najmniej 300 znaków, nie zaczyna się samym numerem przepisu, wyjaśnia sens poprawnej odpowiedzi, odnosi się do najważniejszego błędnego wariantu i kończy podstawą ADR. Nie znaleziono potwierdzonej potrzeby redakcyjnej; nie zmieniono tekstu tylko po to, by wymusić diff.

1. `ADR-B-0587` — fałszywy alarm: explanation spełnia strukturę, objaśnia sens poprawnej odpowiedzi, najważniejszy błąd i podstawę ADR.
2. `ADR-B-0037` — fałszywy alarm: explanation spełnia strukturę, objaśnia sens poprawnej odpowiedzi, najważniejszy błąd i podstawę ADR.
3. `ADR-B-0513` — fałszywy alarm: explanation spełnia strukturę, objaśnia sens poprawnej odpowiedzi, najważniejszy błąd i podstawę ADR.
4. `ADR-B-0388` — fałszywy alarm: explanation spełnia strukturę, objaśnia sens poprawnej odpowiedzi, najważniejszy błąd i podstawę ADR.
5. `ADR-B-0295` — fałszywy alarm: explanation spełnia strukturę, objaśnia sens poprawnej odpowiedzi, najważniejszy błąd i podstawę ADR.
6. `ADR-B-0492` — fałszywy alarm: explanation spełnia strukturę, objaśnia sens poprawnej odpowiedzi, najważniejszy błąd i podstawę ADR.
7. `ADR-B-0429` — fałszywy alarm: explanation spełnia strukturę, objaśnia sens poprawnej odpowiedzi, najważniejszy błąd i podstawę ADR.
8. `ADR-B-0417` — fałszywy alarm: explanation spełnia strukturę, objaśnia sens poprawnej odpowiedzi, najważniejszy błąd i podstawę ADR.
9. `ADR-B-0119` — fałszywy alarm: explanation spełnia strukturę, objaśnia sens poprawnej odpowiedzi, najważniejszy błąd i podstawę ADR.
10. `ADR-B-0050` — fałszywy alarm: explanation spełnia strukturę, objaśnia sens poprawnej odpowiedzi, najważniejszy błąd i podstawę ADR.
11. `ADR-B-0148` — fałszywy alarm: explanation spełnia strukturę, objaśnia sens poprawnej odpowiedzi, najważniejszy błąd i podstawę ADR.
12. `ADR-B-0015` — fałszywy alarm: explanation spełnia strukturę, objaśnia sens poprawnej odpowiedzi, najważniejszy błąd i podstawę ADR.
13. `ADR-B-0101` — fałszywy alarm: explanation spełnia strukturę, objaśnia sens poprawnej odpowiedzi, najważniejszy błąd i podstawę ADR.
14. `ADR-B-0242` — fałszywy alarm: explanation spełnia strukturę, objaśnia sens poprawnej odpowiedzi, najważniejszy błąd i podstawę ADR.
15. `ADR-B-0195` — fałszywy alarm: explanation spełnia strukturę, objaśnia sens poprawnej odpowiedzi, najważniejszy błąd i podstawę ADR.
16. `ADR-B-0287` — fałszywy alarm: explanation spełnia strukturę, objaśnia sens poprawnej odpowiedzi, najważniejszy błąd i podstawę ADR.
17. `ADR-B-0454` — fałszywy alarm: explanation spełnia strukturę, objaśnia sens poprawnej odpowiedzi, najważniejszy błąd i podstawę ADR.
18. `ADR-B-0539` — fałszywy alarm: explanation spełnia strukturę, objaśnia sens poprawnej odpowiedzi, najważniejszy błąd i podstawę ADR.
19. `ADR-B-0245` — fałszywy alarm: explanation spełnia strukturę, objaśnia sens poprawnej odpowiedzi, najważniejszy błąd i podstawę ADR.
20. `ADR-B-0339` — fałszywy alarm: explanation spełnia strukturę, objaśnia sens poprawnej odpowiedzi, najważniejszy błąd i podstawę ADR.
21. `ADR-B-0282` — fałszywy alarm: explanation spełnia strukturę, objaśnia sens poprawnej odpowiedzi, najważniejszy błąd i podstawę ADR.
22. `ADR-B-0262` — fałszywy alarm: explanation spełnia strukturę, objaśnia sens poprawnej odpowiedzi, najważniejszy błąd i podstawę ADR.
23. `ADR-B-0239` — fałszywy alarm: explanation spełnia strukturę, objaśnia sens poprawnej odpowiedzi, najważniejszy błąd i podstawę ADR.
24. `ADR-B-0051` — fałszywy alarm: explanation spełnia strukturę, objaśnia sens poprawnej odpowiedzi, najważniejszy błąd i podstawę ADR.
25. `ADR-B-0415` — fałszywy alarm: explanation spełnia strukturę, objaśnia sens poprawnej odpowiedzi, najważniejszy błąd i podstawę ADR.
26. `ADR-B-0369` — fałszywy alarm: explanation spełnia strukturę, objaśnia sens poprawnej odpowiedzi, najważniejszy błąd i podstawę ADR.
27. `ADR-B-0574` — fałszywy alarm: explanation spełnia strukturę, objaśnia sens poprawnej odpowiedzi, najważniejszy błąd i podstawę ADR.
28. `ADR-B-0170` — fałszywy alarm: explanation spełnia strukturę, objaśnia sens poprawnej odpowiedzi, najważniejszy błąd i podstawę ADR.
29. `ADR-B-0515` — fałszywy alarm: explanation spełnia strukturę, objaśnia sens poprawnej odpowiedzi, najważniejszy błąd i podstawę ADR.
30. `ADR-B-0065` — fałszywy alarm: explanation spełnia strukturę, objaśnia sens poprawnej odpowiedzi, najważniejszy błąd i podstawę ADR.
31. `ADR-B-0214` — fałszywy alarm: explanation spełnia strukturę, objaśnia sens poprawnej odpowiedzi, najważniejszy błąd i podstawę ADR.
32. `ADR-B-0198` — fałszywy alarm: explanation spełnia strukturę, objaśnia sens poprawnej odpowiedzi, najważniejszy błąd i podstawę ADR.
33. `ADR-B-0185` — fałszywy alarm: explanation spełnia strukturę, objaśnia sens poprawnej odpowiedzi, najważniejszy błąd i podstawę ADR.
34. `ADR-B-0140` — fałszywy alarm: explanation spełnia strukturę, objaśnia sens poprawnej odpowiedzi, najważniejszy błąd i podstawę ADR.
35. `ADR-B-0020` — fałszywy alarm: explanation spełnia strukturę, objaśnia sens poprawnej odpowiedzi, najważniejszy błąd i podstawę ADR.
36. `ADR-B-0183` — fałszywy alarm: explanation spełnia strukturę, objaśnia sens poprawnej odpowiedzi, najważniejszy błąd i podstawę ADR.
37. `ADR-B-0288` — fałszywy alarm: explanation spełnia strukturę, objaśnia sens poprawnej odpowiedzi, najważniejszy błąd i podstawę ADR.
38. `ADR-B-0023` — fałszywy alarm: explanation spełnia strukturę, objaśnia sens poprawnej odpowiedzi, najważniejszy błąd i podstawę ADR.
39. `ADR-B-0443` — fałszywy alarm: explanation spełnia strukturę, objaśnia sens poprawnej odpowiedzi, najważniejszy błąd i podstawę ADR.
40. `ADR-B-0562` — fałszywy alarm: explanation spełnia strukturę, objaśnia sens poprawnej odpowiedzi, najważniejszy błąd i podstawę ADR.
41. `ADR-B-0357` — fałszywy alarm: explanation spełnia strukturę, objaśnia sens poprawnej odpowiedzi, najważniejszy błąd i podstawę ADR.
42. `ADR-B-0013` — fałszywy alarm: explanation spełnia strukturę, objaśnia sens poprawnej odpowiedzi, najważniejszy błąd i podstawę ADR.
43. `ADR-B-0467` — fałszywy alarm: explanation spełnia strukturę, objaśnia sens poprawnej odpowiedzi, najważniejszy błąd i podstawę ADR.
44. `ADR-B-0107` — fałszywy alarm: explanation spełnia strukturę, objaśnia sens poprawnej odpowiedzi, najważniejszy błąd i podstawę ADR.
45. `ADR-B-0517` — fałszywy alarm: explanation spełnia strukturę, objaśnia sens poprawnej odpowiedzi, najważniejszy błąd i podstawę ADR.
46. `ADR-B-0584` — fałszywy alarm: explanation spełnia strukturę, objaśnia sens poprawnej odpowiedzi, najważniejszy błąd i podstawę ADR.
47. `ADR-B-0392` — fałszywy alarm: explanation spełnia strukturę, objaśnia sens poprawnej odpowiedzi, najważniejszy błąd i podstawę ADR.
48. `ADR-B-0075` — fałszywy alarm: explanation spełnia strukturę, objaśnia sens poprawnej odpowiedzi, najważniejszy błąd i podstawę ADR.
49. `ADR-B-0458` — fałszywy alarm: explanation spełnia strukturę, objaśnia sens poprawnej odpowiedzi, najważniejszy błąd i podstawę ADR.
50. `ADR-B-0302` — fałszywy alarm: explanation spełnia strukturę, objaśnia sens poprawnej odpowiedzi, najważniejszy błąd i podstawę ADR.
51. `ADR-B-0096` — fałszywy alarm: explanation spełnia strukturę, objaśnia sens poprawnej odpowiedzi, najważniejszy błąd i podstawę ADR.
52. `ADR-B-0014` — fałszywy alarm: explanation spełnia strukturę, objaśnia sens poprawnej odpowiedzi, najważniejszy błąd i podstawę ADR.
53. `ADR-B-0145` — fałszywy alarm: explanation spełnia strukturę, objaśnia sens poprawnej odpowiedzi, najważniejszy błąd i podstawę ADR.
54. `ADR-B-0478` — fałszywy alarm: explanation spełnia strukturę, objaśnia sens poprawnej odpowiedzi, najważniejszy błąd i podstawę ADR.
55. `ADR-B-0577` — fałszywy alarm: explanation spełnia strukturę, objaśnia sens poprawnej odpowiedzi, najważniejszy błąd i podstawę ADR.
56. `ADR-B-0419` — fałszywy alarm: explanation spełnia strukturę, objaśnia sens poprawnej odpowiedzi, najważniejszy błąd i podstawę ADR.
57. `ADR-B-0487` — fałszywy alarm: explanation spełnia strukturę, objaśnia sens poprawnej odpowiedzi, najważniejszy błąd i podstawę ADR.
58. `ADR-B-0442` — fałszywy alarm: explanation spełnia strukturę, objaśnia sens poprawnej odpowiedzi, najważniejszy błąd i podstawę ADR.
59. `ADR-B-0533` — fałszywy alarm: explanation spełnia strukturę, objaśnia sens poprawnej odpowiedzi, najważniejszy błąd i podstawę ADR.
60. `ADR-B-0117` — fałszywy alarm: explanation spełnia strukturę, objaśnia sens poprawnej odpowiedzi, najważniejszy błąd i podstawę ADR.

## Ponowny przegląd scenariuszy

Sprawdzono 39 scenariuszy pod kątem kroków kierowcy, pytań i modułu, podstawy ADR, podsumowania dla kursanta oraz typowych błędów.

- Scenariusze: 39; mniej niż 3 kroki: 0.
- Brakujące question IDs: 0.
- Question IDs z innego modułu: 0.
- Brak learner takeaway, podstawy lub common mistakes: 0.
- Potwierdzone braki wymagające zmiany: 0.

## Metryki banku

- Pytania: 609; duplikaty ID: 0.
- Statusy: 609 `needs_review`, 0 `verified`.
- Explanation poniżej 200 znaków: 0; minimum 300 znaków.
- „Poprawna = jedyna najdłuższa”: 72/609 = 11.82%; maksimum działu 14.29%.

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

## Zmiany

Bank, klucze egzaminów 001–005, scenariusze i statusy prawne bez zmian. Nie dodano nowych pytań, bo w tej próbce nie wykryto potwierdzonej luki programu. Nie oznaczono żadnego pytania jako `verified`.

## Testy

Brak lokalnego checkoutu i niedostępny DNS dla `git clone` uniemożliwiają zadeklarowanie lokalnych testów. Raport i odsyłacz przechodzą przez PR; wymagany PASS Quality Gate CI przed scaleniem.
