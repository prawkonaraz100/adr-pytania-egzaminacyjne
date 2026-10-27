# Etap 4x90 — nowa próbka 60 i rejestr wartości zależnych od aktualizacji ADR

- Data: 27.10.2026.
- Punkt wejścia: świeży `main`, `91f853f1f15d0bab47b695ea210f9cc73a683241`.
- Gałąź: `stage4x90-sampling-register-legal-values-20261027`.
- Zakres: wyłącznie kurs podstawowy ADR.

## 1. Stan Quality Gate

Main miał PASS: [Quality Gate run #40535084568](https://github.com/prawkonaraz100/adr-pytania-egzaminacyjne/actions/runs/40535084568). Preflight danych po pobraniu banku:

| Kontrola | Wynik |
|---|---:|
| Pytania / unikalne ID | 609 / 609 |
| Status `needs_review` / `verified` | 609 / 0 |
| Minimum explanation | 300 znaków |
| Explanation poniżej 200 znaków | 0 |
| Poprawna odpowiedź jako jedyna najdłuższa | 73/609 = 11.99% |

| Dział | Pytania | Poprawna jedyna najdłuższa | Wskaźnik |
|---|---:|---:|---:|
| ADR-B-01 | 45 | 6 | 13.33% |
| ADR-B-02 | 56 | 8 | 14.29% |
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
| **Razem** | **609** | **73** | **11.99%** |

## 2. Próbka 60 explanation

- Seed: `2026102790`; generator LCG i Fisher–Yates.
- Pula po wykluczeniu jawnie wymienionych ID z raportów 4x84, 4x85, 4x86, 4x87 i 4x89: 410 rekordów; 60 wybranych.
- Zastrzeżenie: raport 4x86 nie zawiera kompletnej listy wszystkich 60 ID, więc wykluczenie wszystkich wcześniejszych próbek nie jest możliwe do dowiedzenia. Zostały wykluczone wszystkie jawnie zapisane ID z tego raportu; ograniczenie pozostaje w rejestrze.
- Ręczny przegląd: sprawdzono sens poprawnej opcji, wiarygodność błędnych odpowiedzi, jasność explanation oraz zgodność wskazanego punktu ADR z omawianą regułą. W tej próbce nie znaleziono potwierdzonego błędu wymagającego zmiany.
- Potwierdzone korekty: **0**; poprawne litery, ID, moduły i statusy bez zmian.

### Lista sprawdzonych pytań

1. `ADR-B-0268` — ADR-B-02, 338 znaków, 11 zdań.
2. `ADR-B-0190` — ADR-B-06, 369 znaków, 8 zdań.
3. `ADR-B-0064` — ADR-B-11, 323 znaków, 10 zdań.
4. `ADR-B-0063` — ADR-B-11, 307 znaków, 7 zdań.
5. `ADR-B-0513` — ADR-B-01, 347 znaków, 6 zdań.
6. `ADR-B-0574` — ADR-B-11, 322 znaków, 7 zdań.
7. `ADR-B-0472` — ADR-B-04, 326 znaków, 9 zdań.
8. `ADR-B-0468` — ADR-B-03, 357 znaków, 13 zdań.
9. `ADR-B-0454` — ADR-B-10, 398 znaków, 16 zdań.
10. `ADR-B-0307` — ADR-B-02, 351 znaków, 12 zdań.
11. `ADR-B-0388` — ADR-B-10, 427 znaków, 7 zdań.
12. `ADR-B-0371` — ADR-B-07, 339 znaków, 8 zdań.
13. `ADR-B-0153` — ADR-B-02, 307 znaków, 11 zdań.
14. `ADR-B-0041` — ADR-B-01, 345 znaków, 7 zdań.
15. `ADR-B-0168` — ADR-B-05, 337 znaków, 10 zdań.
16. `ADR-B-0208` — ADR-B-11, 376 znaków, 10 zdań.
17. `ADR-B-0457` — ADR-B-12, 360 znaków, 12 zdań.
18. `ADR-B-0352` — ADR-B-04, 321 znaków, 8 zdań.
19. `ADR-B-0120` — ADR-B-12, 379 znaków, 7 zdań.
20. `ADR-B-0157` — ADR-B-02, 342 znaków, 10 zdań.
21. `ADR-B-0299` — ADR-B-06, 319 znaków, 7 zdań.
22. `ADR-B-0478` — ADR-B-07, 305 znaków, 7 zdań.
23. `ADR-B-0466` — ADR-B-03, 407 znaków, 12 zdań.
24. `ADR-B-0284` — ADR-B-02, 303 znaków, 10 zdań.
25. `ADR-B-0511` — ADR-B-10, 407 znaków, 8 zdań.
26. `ADR-B-0547` — ADR-B-06, 458 znaków, 11 zdań.
27. `ADR-B-0044` — ADR-B-02, 430 znaków, 10 zdań.
28. `ADR-B-0549` — ADR-B-06, 315 znaków, 7 zdań.
29. `ADR-B-0301` — ADR-B-01, 352 znaków, 7 zdań.
30. `ADR-B-0493` — ADR-B-05, 344 znaków, 7 zdań.
31. `ADR-B-0247` — ADR-B-10, 318 znaków, 8 zdań.
32. `ADR-B-0433` — ADR-B-11, 318 znaków, 8 zdań.
33. `ADR-B-0500` — ADR-B-02, 373 znaków, 10 zdań.
34. `ADR-B-0535` — ADR-B-01, 393 znaków, 7 zdań.
35. `ADR-B-0483` — ADR-B-08, 361 znaków, 12 zdań.
36. `ADR-B-0275` — ADR-B-12, 323 znaków, 7 zdań.
37. `ADR-B-0335` — ADR-B-03, 358 znaków, 8 zdań.
38. `ADR-B-0098` — ADR-B-02, 395 znaków, 8 zdań.
39. `ADR-B-0378` — ADR-B-07, 321 znaków, 8 zdań.
40. `ADR-B-0113` — ADR-B-05, 311 znaków, 7 zdań.
41. `ADR-B-0350` — ADR-B-04, 365 znaków, 6 zdań.
42. `ADR-B-0551` — ADR-B-08, 352 znaków, 10 zdań.
43. `ADR-B-0305` — ADR-B-12, 309 znaków, 7 zdań.
44. `ADR-B-0218` — ADR-B-02, 315 znaków, 8 zdań.
45. `ADR-B-0311` — ADR-B-02, 349 znaków, 9 zdań.
46. `ADR-B-0279` — ADR-B-04, 325 znaków, 6 zdań.
47. `ADR-B-0240` — ADR-B-09, 347 znaków, 7 zdań.
48. `ADR-B-0383` — ADR-B-10, 363 znaków, 8 zdań.
49. `ADR-B-0140` — ADR-B-10, 385 znaków, 7 zdań.
50. `ADR-B-0028` — ADR-B-10, 382 znaków, 8 zdań.
51. `ADR-B-0411` — ADR-B-12, 315 znaków, 7 zdań.
52. `ADR-B-0596` — ADR-B-08, 335 znaków, 7 zdań.
53. `ADR-B-0548` — ADR-B-06, 398 znaków, 8 zdań.
54. `ADR-B-0122` — ADR-B-12, 321 znaków, 7 zdań.
55. `ADR-B-0146` — ADR-B-13, 334 znaków, 9 zdań.
56. `ADR-B-0109` — ADR-B-05, 322 znaków, 7 zdań.
57. `ADR-B-0522` — ADR-B-01, 364 znaków, 7 zdań.
58. `ADR-B-0217` — ADR-B-06, 348 znaków, 8 zdań.
59. `ADR-B-0579` — ADR-B-13, 374 znaków, 8 zdań.
60. `ADR-B-0538` — ADR-B-13, 374 znaków, 8 zdań.

## 3. Rejestr wrażliwych odniesień prawnych

### Umowy wielostronne M…

W bieżącym banku występują dwa pytania z odniesieniem do M364: **ADR-B-0145** i **ADR-B-0198**. Oba jednoznacznie pytają o samochód silnikowy FL, nie o przyczepę. Wyjątek z M364 nie został rozszerzony na pojazd silnikowy. Oficjalna lista [UNECE — ADR Multilateral Agreements](https://unece.org/transport/road-transport/adr-multilateral-agreements) wskazuje M364 jako ważną do **31.12.2026**, z Polską jako sygnatariuszem i bez daty wypowiedzenia widocznej przy polskim wpisie. W tej kontroli nie znaleziono potwierdzonego powodu do zmiany pytań.

**Działanie kontrolne:** przed użyciem materiału po 31.12.2026 ponownie sprawdzić status umowy w UNECE i polską publikację; nie zakładać przedłużenia bez źródła urzędowego.

### Wyłączenia ADR 1.1.3

W 26 rekordach wykryto odwołanie do 1.1.3. Najważniejsze reguły w kontrolowanym zakresie:
- 1.1.3.1(a): wyłączenie dla osoby prywatnej zależy od przeznaczenia i spełnienia warunków, a nie tylko od niewielkiej ilości;
- 1.1.3.6: limit zależy od kategorii transportowej i właściwego sposobu obliczenia; dla ładunku mieszanego stosuje się współczynniki z 1.1.3.6.4;
- 3.4 LQ (ilości ograniczone) nie jest tym samym co wyłączenie 1.1.3.6;
- wyłączenie nie oznacza automatycznie, że znikają wszystkie pozostałe obowiązki.

Kontrolowane obliczenia 100×3+600=900 oraz 200×3+500=1100 są wewnętrznie spójne z podanymi współczynnikami i progiem 1000. Nie znaleziono potwierdzonej sprzeczności w badanych rekordach.

### Przepisy szczególne

Wyszukiwanie po oznaczeniach SP/CV/S wskazało **ADR-B-0027, ADR-B-0082 i ADR-B-0160**. W każdym przypadku explanation wskazuje konkretny warunek (CV28, przypis/warunek 8.5 S12) zamiast przedstawiać go jako regułę dla wszystkich towarów. Nie znaleziono potwierdzonego błędu wymagającego zmiany.

## 4. Scenariusze i egzaminy — kontrola regresji

- Scenariusze: 39, po 3 na dział; ostatni test struktury wykazał 4 kroki na każdy scenariusz i brak nieistniejących/obcych `question_ids`.
- Egzaminy próbne 001–005: bank się nie zmienił, więc nie regenerowano wariantów. W poprzednim preflight wszystkie klucze zgadzały się z treścią poprawnej opcji.
- Pakiet recenzyjny: 609 pytań, wszystkie `needs_review`; niezależna recenzja specjalisty pozostaje obowiązkowa.

## 5. Ograniczenia

Pełnych testów Python lokalnie nie uruchomiono, ponieważ połączenie udostępnia repozytorium przez GitHub, ale nie lokalny checkout. Kontrole skryptowe wykonano na pobranych danych; wymagany jest PASS GitHub Actions na PR. Brak potwierdzonego błędu nie oznacza formalnego zatwierdzenia prawnego. Nie zmieniono pytań i nie nadano statusu `verified`.
