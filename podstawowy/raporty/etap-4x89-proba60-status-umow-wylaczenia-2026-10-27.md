# Etap 4x89 — próbka explanation, scenariusze i aktualność wyłączeń ADR

- Data: 27.10.2026.
- Punkt wejścia: świeży `main`, `871de19dae83e478b60712804c6227114546316e`.
- Gałąź: `stage4x89-proba60-m364-113-20261027`.
- Zakres: wyłącznie kurs podstawowy ADR.
- Bank: blob `4a1a5d7f1ca8a5124eb096cd228aa92952fac6da`, 609 pytań; wszystkie `needs_review`, bez `verified`.

## 1. Quality Gate na świeżym main

Ostatni workflow Quality Gate dla HEAD `871de19` zakończył się **PASS**: [run #40525965199](https://github.com/prawkonaraz100/adr-pytania-egzaminacyjne/actions/runs/40525965199). Niezależny preflight na pobranych plikach potwierdził:

| Kontrola | Wynik |
|---|---:|
| Rekordy / unikalne ID | 609 / 609 |
| `needs_review` / `verified` | 609 / 0 |
| Najkrótsze explanation | 300 znaków |
| Explanation poniżej 200 znaków | 0 |
| Poprawna odpowiedź jest jedyną najdłuższą | 73/609 = 11.99% |
| Scenariusze | 39, po 3 w każdym dziale |
| Rozbieżności kluczy egzaminów w porównaniu treści poprawnej opcji | 0 |

### Wskaźnik „poprawna = jedyna najdłuższa” per dział

| Dział | Liczba pytań | Poprawna jedyna najdłuższa | Wskaźnik |
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

Wszystkie działy pozostają poniżej 18%; żaden rekord banku nie został zmieniony w tej partii, więc nie było potrzeby ponownej synchronizacji wariantów.

## 2. Losowa próbka 60 explanation

- Seed: `2026102789`; generator: LCG (`state = 1664525 × state + 1013904223 mod 2^32`) i Fisher–Yates.
- Pula: 489 ID po odjęciu 120 ID jawnie wymienionych w raportach 4x84, 4x85 i 4x87 oraz jawnych korekt z raportu 4x86.
- **Ograniczenie ważne dla audytu:** raport 4x86 nie podaje pełnej listy swoich 60 wylosowanych ID — zawiera tylko jawnie opisane korekty. Dlatego nie mogę potwierdzić braku przecięcia z nieujawnioną częścią tamtej próbki. Zapisuję to wprost, zamiast przedstawiać próbkę jako udowodnione 60 nowych ID.
- Sprawdzono 60 rekordów w kontekście treści pytania, trzech opcji, poprawnej litery i podstawy prawnej. Wszystkie wybrane rekordy miały explanation co najmniej 300 znaków i 3–5 zdań; nie znaleziono jednozdaniowego ani rozpoczynającego się od samego numeru przepisu.
- **Potwierdzone poprawki banku: 0.** Nie zmieniono treści, poprawnych liter ani statusów, ponieważ w tej próbce nie stwierdzono potwierdzonej niejednoznaczności lub błędu wymagającego korekty.

### Lista ID sprawdzonych

1. `ADR-B-0003` — ADR-B-01
2. `ADR-B-0477` — ADR-B-07
3. `ADR-B-0450` — ADR-B-10
4. `ADR-B-0030` — ADR-B-10
5. `ADR-B-0022` — ADR-B-08
6. `ADR-B-0341` — ADR-B-03
7. `ADR-B-0568` — ADR-B-07
8. `ADR-B-0461` — ADR-B-03
9. `ADR-B-0112` — ADR-B-05
10. `ADR-B-0557` — ADR-B-09
11. `ADR-B-0393` — ADR-B-10
12. `ADR-B-0413` — ADR-B-12
13. `ADR-B-0147` — ADR-B-01
14. `ADR-B-0150` — ADR-B-02
15. `ADR-B-0372` — ADR-B-07
16. `ADR-B-0278` — ADR-B-10
17. `ADR-B-0149` — ADR-B-01
18. `ADR-B-0293` — ADR-B-07
19. `ADR-B-0326` — ADR-B-03
20. `ADR-B-0282` — ADR-B-08
21. `ADR-B-0269` — ADR-B-02
22. `ADR-B-0555` — ADR-B-09
23. `ADR-B-0417` — ADR-B-08
24. `ADR-B-0343` — ADR-B-03
25. `ADR-B-0452` — ADR-B-10
26. `ADR-B-0381` — ADR-B-10
27. `ADR-B-0355` — ADR-B-04
28. `ADR-B-0177` — ADR-B-03
29. `ADR-B-0496` — ADR-B-02
30. `ADR-B-0007` — ADR-B-03
31. `ADR-B-0267` — ADR-B-02
32. `ADR-B-0257` — ADR-B-06
33. `ADR-B-0518` — ADR-B-09
34. `ADR-B-0501` — ADR-B-02
35. `ADR-B-0212` — ADR-B-12
36. `ADR-B-0394` — ADR-B-10
37. `ADR-B-0214` — ADR-B-13
38. `ADR-B-0585` — ADR-B-05
39. `ADR-B-0074` — ADR-B-08
40. `ADR-B-0124` — ADR-B-01
41. `ADR-B-0401` — ADR-B-12
42. `ADR-B-0161` — ADR-B-02
43. `ADR-B-0078` — ADR-B-09
44. `ADR-B-0259` — ADR-B-01
45. `ADR-B-0380` — ADR-B-07
46. `ADR-B-0188` — ADR-B-06
47. `ADR-B-0320` — ADR-B-10
48. `ADR-B-0351` — ADR-B-04
49. `ADR-B-0414` — ADR-B-12
50. `ADR-B-0118` — ADR-B-07
51. `ADR-B-0295` — ADR-B-03
52. `ADR-B-0244` — ADR-B-04
53. `ADR-B-0169` — ADR-B-05
54. `ADR-B-0365` — ADR-B-07
55. `ADR-B-0018` — ADR-B-06
56. `ADR-B-0382` — ADR-B-10
57. `ADR-B-0005` — ADR-B-02
58. `ADR-B-0408` — ADR-B-12
59. `ADR-B-0239` — ADR-B-09
60. `ADR-B-0369` — ADR-B-07

### Wynik czytelności próbki

- `ADR-B-0003` (ADR-B-01): 352 znaków; 6 zdań; sens poprawnej odpowiedzi i rozróżnienie błędnych opcji obecne; podstawa ADR wskazana.
- `ADR-B-0477` (ADR-B-07): 311 znaków; 12 zdań; sens poprawnej odpowiedzi i rozróżnienie błędnych opcji obecne; podstawa ADR wskazana.
- `ADR-B-0450` (ADR-B-10): 374 znaków; 9 zdań; sens poprawnej odpowiedzi i rozróżnienie błędnych opcji obecne; podstawa ADR wskazana.
- `ADR-B-0030` (ADR-B-10): 353 znaków; 7 zdań; sens poprawnej odpowiedzi i rozróżnienie błędnych opcji obecne; podstawa ADR wskazana.
- `ADR-B-0022` (ADR-B-08): 384 znaków; 7 zdań; sens poprawnej odpowiedzi i rozróżnienie błędnych opcji obecne; podstawa ADR wskazana.
- `ADR-B-0341` (ADR-B-03): 412 znaków; 8 zdań; sens poprawnej odpowiedzi i rozróżnienie błędnych opcji obecne; podstawa ADR wskazana.
- `ADR-B-0568` (ADR-B-07): 335 znaków; 8 zdań; sens poprawnej odpowiedzi i rozróżnienie błędnych opcji obecne; podstawa ADR wskazana.
- `ADR-B-0461` (ADR-B-03): 305 znaków; 7 zdań; sens poprawnej odpowiedzi i rozróżnienie błędnych opcji obecne; podstawa ADR wskazana.
- `ADR-B-0112` (ADR-B-05): 341 znaków; 7 zdań; sens poprawnej odpowiedzi i rozróżnienie błędnych opcji obecne; podstawa ADR wskazana.
- `ADR-B-0557` (ADR-B-09): 337 znaków; 7 zdań; sens poprawnej odpowiedzi i rozróżnienie błędnych opcji obecne; podstawa ADR wskazana.
- `ADR-B-0393` (ADR-B-10): 318 znaków; 6 zdań; sens poprawnej odpowiedzi i rozróżnienie błędnych opcji obecne; podstawa ADR wskazana.
- `ADR-B-0413` (ADR-B-12): 369 znaków; 7 zdań; sens poprawnej odpowiedzi i rozróżnienie błędnych opcji obecne; podstawa ADR wskazana.
- `ADR-B-0147` (ADR-B-01): 334 znaków; 6 zdań; sens poprawnej odpowiedzi i rozróżnienie błędnych opcji obecne; podstawa ADR wskazana.
- `ADR-B-0150` (ADR-B-02): 374 znaków; 11 zdań; sens poprawnej odpowiedzi i rozróżnienie błędnych opcji obecne; podstawa ADR wskazana.
- `ADR-B-0372` (ADR-B-07): 343 znaków; 8 zdań; sens poprawnej odpowiedzi i rozróżnienie błędnych opcji obecne; podstawa ADR wskazana.
- `ADR-B-0278` (ADR-B-10): 442 znaków; 9 zdań; sens poprawnej odpowiedzi i rozróżnienie błędnych opcji obecne; podstawa ADR wskazana.
- `ADR-B-0149` (ADR-B-01): 364 znaków; 8 zdań; sens poprawnej odpowiedzi i rozróżnienie błędnych opcji obecne; podstawa ADR wskazana.
- `ADR-B-0293` (ADR-B-07): 351 znaków; 6 zdań; sens poprawnej odpowiedzi i rozróżnienie błędnych opcji obecne; podstawa ADR wskazana.
- `ADR-B-0326` (ADR-B-03): 302 znaków; 9 zdań; sens poprawnej odpowiedzi i rozróżnienie błędnych opcji obecne; podstawa ADR wskazana.
- `ADR-B-0282` (ADR-B-08): 345 znaków; 10 zdań; sens poprawnej odpowiedzi i rozróżnienie błędnych opcji obecne; podstawa ADR wskazana.
- `ADR-B-0269` (ADR-B-02): 316 znaków; 10 zdań; sens poprawnej odpowiedzi i rozróżnienie błędnych opcji obecne; podstawa ADR wskazana.
- `ADR-B-0555` (ADR-B-09): 314 znaków; 7 zdań; sens poprawnej odpowiedzi i rozróżnienie błędnych opcji obecne; podstawa ADR wskazana.
- `ADR-B-0417` (ADR-B-08): 358 znaków; 8 zdań; sens poprawnej odpowiedzi i rozróżnienie błędnych opcji obecne; podstawa ADR wskazana.
- `ADR-B-0343` (ADR-B-03): 417 znaków; 9 zdań; sens poprawnej odpowiedzi i rozróżnienie błędnych opcji obecne; podstawa ADR wskazana.
- `ADR-B-0452` (ADR-B-10): 316 znaków; 8 zdań; sens poprawnej odpowiedzi i rozróżnienie błędnych opcji obecne; podstawa ADR wskazana.
- `ADR-B-0381` (ADR-B-10): 393 znaków; 7 zdań; sens poprawnej odpowiedzi i rozróżnienie błędnych opcji obecne; podstawa ADR wskazana.
- `ADR-B-0355` (ADR-B-04): 336 znaków; 7 zdań; sens poprawnej odpowiedzi i rozróżnienie błędnych opcji obecne; podstawa ADR wskazana.
- `ADR-B-0177` (ADR-B-03): 370 znaków; 7 zdań; sens poprawnej odpowiedzi i rozróżnienie błędnych opcji obecne; podstawa ADR wskazana.
- `ADR-B-0496` (ADR-B-02): 300 znaków; 9 zdań; sens poprawnej odpowiedzi i rozróżnienie błędnych opcji obecne; podstawa ADR wskazana.
- `ADR-B-0007` (ADR-B-03): 327 znaków; 7 zdań; sens poprawnej odpowiedzi i rozróżnienie błędnych opcji obecne; podstawa ADR wskazana.
- `ADR-B-0267` (ADR-B-02): 303 znaków; 8 zdań; sens poprawnej odpowiedzi i rozróżnienie błędnych opcji obecne; podstawa ADR wskazana.
- `ADR-B-0257` (ADR-B-06): 342 znaków; 8 zdań; sens poprawnej odpowiedzi i rozróżnienie błędnych opcji obecne; podstawa ADR wskazana.
- `ADR-B-0518` (ADR-B-09): 305 znaków; 7 zdań; sens poprawnej odpowiedzi i rozróżnienie błędnych opcji obecne; podstawa ADR wskazana.
- `ADR-B-0501` (ADR-B-02): 318 znaków; 8 zdań; sens poprawnej odpowiedzi i rozróżnienie błędnych opcji obecne; podstawa ADR wskazana.
- `ADR-B-0212` (ADR-B-12): 368 znaków; 10 zdań; sens poprawnej odpowiedzi i rozróżnienie błędnych opcji obecne; podstawa ADR wskazana.
- `ADR-B-0394` (ADR-B-10): 349 znaków; 8 zdań; sens poprawnej odpowiedzi i rozróżnienie błędnych opcji obecne; podstawa ADR wskazana.
- `ADR-B-0214` (ADR-B-13): 395 znaków; 8 zdań; sens poprawnej odpowiedzi i rozróżnienie błędnych opcji obecne; podstawa ADR wskazana.
- `ADR-B-0585` (ADR-B-05): 326 znaków; 7 zdań; sens poprawnej odpowiedzi i rozróżnienie błędnych opcji obecne; podstawa ADR wskazana.
- `ADR-B-0074` (ADR-B-08): 350 znaków; 10 zdań; sens poprawnej odpowiedzi i rozróżnienie błędnych opcji obecne; podstawa ADR wskazana.
- `ADR-B-0124` (ADR-B-01): 331 znaków; 7 zdań; sens poprawnej odpowiedzi i rozróżnienie błędnych opcji obecne; podstawa ADR wskazana.
- `ADR-B-0401` (ADR-B-12): 327 znaków; 8 zdań; sens poprawnej odpowiedzi i rozróżnienie błędnych opcji obecne; podstawa ADR wskazana.
- `ADR-B-0161` (ADR-B-02): 343 znaków; 8 zdań; sens poprawnej odpowiedzi i rozróżnienie błędnych opcji obecne; podstawa ADR wskazana.
- `ADR-B-0078` (ADR-B-09): 359 znaków; 10 zdań; sens poprawnej odpowiedzi i rozróżnienie błędnych opcji obecne; podstawa ADR wskazana.
- `ADR-B-0259` (ADR-B-01): 304 znaków; 11 zdań; sens poprawnej odpowiedzi i rozróżnienie błędnych opcji obecne; podstawa ADR wskazana.
- `ADR-B-0380` (ADR-B-07): 349 znaków; 8 zdań; sens poprawnej odpowiedzi i rozróżnienie błędnych opcji obecne; podstawa ADR wskazana.
- `ADR-B-0188` (ADR-B-06): 344 znaków; 8 zdań; sens poprawnej odpowiedzi i rozróżnienie błędnych opcji obecne; podstawa ADR wskazana.
- `ADR-B-0320` (ADR-B-10): 403 znaków; 8 zdań; sens poprawnej odpowiedzi i rozróżnienie błędnych opcji obecne; podstawa ADR wskazana.
- `ADR-B-0351` (ADR-B-04): 358 znaków; 7 zdań; sens poprawnej odpowiedzi i rozróżnienie błędnych opcji obecne; podstawa ADR wskazana.
- `ADR-B-0414` (ADR-B-12): 305 znaków; 7 zdań; sens poprawnej odpowiedzi i rozróżnienie błędnych opcji obecne; podstawa ADR wskazana.
- `ADR-B-0118` (ADR-B-07): 327 znaków; 8 zdań; sens poprawnej odpowiedzi i rozróżnienie błędnych opcji obecne; podstawa ADR wskazana.
- `ADR-B-0295` (ADR-B-03): 318 znaków; 7 zdań; sens poprawnej odpowiedzi i rozróżnienie błędnych opcji obecne; podstawa ADR wskazana.
- `ADR-B-0244` (ADR-B-04): 319 znaków; 6 zdań; sens poprawnej odpowiedzi i rozróżnienie błędnych opcji obecne; podstawa ADR wskazana.
- `ADR-B-0169` (ADR-B-05): 358 znaków; 7 zdań; sens poprawnej odpowiedzi i rozróżnienie błędnych opcji obecne; podstawa ADR wskazana.
- `ADR-B-0365` (ADR-B-07): 350 znaków; 8 zdań; sens poprawnej odpowiedzi i rozróżnienie błędnych opcji obecne; podstawa ADR wskazana.
- `ADR-B-0018` (ADR-B-06): 346 znaków; 8 zdań; sens poprawnej odpowiedzi i rozróżnienie błędnych opcji obecne; podstawa ADR wskazana.
- `ADR-B-0382` (ADR-B-10): 419 znaków; 8 zdań; sens poprawnej odpowiedzi i rozróżnienie błędnych opcji obecne; podstawa ADR wskazana.
- `ADR-B-0005` (ADR-B-02): 316 znaków; 8 zdań; sens poprawnej odpowiedzi i rozróżnienie błędnych opcji obecne; podstawa ADR wskazana.
- `ADR-B-0408` (ADR-B-12): 329 znaków; 7 zdań; sens poprawnej odpowiedzi i rozróżnienie błędnych opcji obecne; podstawa ADR wskazana.
- `ADR-B-0239` (ADR-B-09): 382 znaków; 7 zdań; sens poprawnej odpowiedzi i rozróżnienie błędnych opcji obecne; podstawa ADR wskazana.
- `ADR-B-0369` (ADR-B-07): 311 znaków; 8 zdań; sens poprawnej odpowiedzi i rozróżnienie błędnych opcji obecne; podstawa ADR wskazana.

## 3. Umowy wielostronne, wyłączenia 1.1.3 i przepisy szczególne

### Umowy wielostronne

W banku występują odwołania do umowy M364 w dwóch pytaniach: **ADR-B-0145** i **ADR-B-0198**. Oba pytania dotyczą samochodu silnikowego typu FL, a nie naczepy. Treść nie przenosi wyjątku dla przyczepy na pojazd silnikowy; nie znaleziono podstaw do zmiany odpowiedzi.

Sprawdzono aktualny wpis [UNECE — ADR Multilateral Agreements](https://unece.org/transport/road-transport/adr-multilateral-agreements): M364 jest wymieniona jako ważna do **31.12.2026**, Polska widnieje jako sygnatariusz z datą 11.09.2025, bez wskazanej daty wypowiedzenia w aktualnym wpisie. Tekst M364 dotyczy warunkowego sposobu przechowywania świadectwa dopuszczenia **przyczepy**. Nie stanowi podstawy do zmiany odpowiedzi w pytaniach o pojazd silnikowy.

Inne oznaczenia Mxxx nie występują w rekordach banku w sposób, który tworzyłby kolejne pytania zależne od statusu umowy. Przed wykorzystaniem materiału po 31.12.2026 trzeba ponownie sprawdzić oficjalny wpis i ewentualne przedłużenie lub zastępczą umowę. W raporcie nie zakładamy z góry ani wygaśnięcia wcześniejszego, ani przedłużenia.

### Wyłączenia ADR 1.1.3

Skrypt znalazł 26 rekordów z odwołaniami do punktów 1.1.3:
`ADR-B-0002`, `ADR-B-0008`, `ADR-B-0046`, `ADR-B-0061`, `ADR-B-0073`, `ADR-B-0085`, `ADR-B-0089`, `ADR-B-0091`, `ADR-B-0093`, `ADR-B-0127`, `ADR-B-0147`, `ADR-B-0179`, `ADR-B-0197`, `ADR-B-0259`, `ADR-B-0271`, `ADR-B-0272`, `ADR-B-0282`, `ADR-B-0294`, `ADR-B-0313`, `ADR-B-0323`, `ADR-B-0421`, `ADR-B-0530`, `ADR-B-0570`, `ADR-B-0571`, `ADR-B-0595`, `ADR-B-0606`.

W próbkowym i ukierunkowanym przeglądzie zwrócono szczególną uwagę na:
- odróżnienie LQ (ilości ograniczonych, ADR 3.4) od wyłączenia ilościowego 1.1.3.6;
- limity kategorii transportowych i obliczenia mieszane z mnożnikiem dla kategorii 2;
- warunki wyłączenia dla osób prywatnych;
- wpływ wyłączeń na ustalanie kodu tunelowego;
- fakt, że wyłączenie nie usuwa automatycznie wszystkich obowiązków, np. wymagań gaśniczych.

W sprawdzonych rekordach nie znaleziono potwierdzonej sprzeczności z przywołanym punktem ADR. Wartości liczbowe nie zostały zmienione na podstawie domysłu.

### Przepisy szczególne

Wystąpienia oznaczeń `SP`, `CV` lub `S` wykryto w 3 rekordach: `ADR-B-0027`, `ADR-B-0082`, `ADR-B-0160`. Są to odwołania do wymagań zależnych od konkretnej pozycji lub sytuacji; nie należy ich uogólniać na wszystkie towary. W tej kontroli nie wykryto potwierdzonej rozbieżności wymagającej korekty klucza.

**Granica kontroli:** jest to przegląd ukierunkowany oraz kontrola referencji, nie formalna opinia prawna dla każdego z 609 rekordów. Niepewne lub zależne od aktualnego wpisu przypadki pozostają do niezależnego odbioru specjalisty.

## 4. Scenariusze praktyczne

Skryptowa kontrola 39 scenariuszy wykazała:
- 13 działów, po 3 scenariusze w każdym;
- 4 kroki postępowania kierowcy w każdym scenariuszu;
- brak nieistniejących lub przypisanych do złego działu `question_ids`;
- każdy scenariusz ma typowe błędy, podstawę ADR, kryteria oceny i podsumowanie dla kursanta.

Liczba scenariuszy z problemem strukturalnym lub błędnymi ID: **0**. Poprzedni pełny przegląd treści 39 scenariuszy w raporcie 4x85 nie wykazał potwierdzonej sprzeczności prawnej; w tej partii nie zmieniono ich bez konkretnego, potwierdzonego błędu.

## 5. Egzaminy próbne i pakiet recenzyjny

Warianty 001–005 oraz klucze wskazują aktualny blob banku `4a1a5d7f1ca8a5124eb096cd228aa92952fac6da`. Każdy arkusz zawiera 30 unikalnych pytań i obejmuje wszystkie 13 działów. Porównanie klucza z treścią poprawnej opcji po uwzględnieniu przestawienia liter A/B/C wykazało **0 rozbieżności**. Nie zmieniono banku, dlatego nie regenerowano egzaminów ani migawek audytu.

Lista kontrolna dla specjalisty:
1. ponownie sprawdzić M364 przed 31.12.2026 i przed publikacją materiałów po tej dacie;
2. przeprowadzić pełną recenzję prawną pytań o wyłączenia 1.1.3, w szczególności obliczeń i warunków LQ;
3. potwierdzić stosowanie przepisów szczególnych w kontekście konkretnego numeru UN;
4. pozostawić wszystkie rekordy w statusie `needs_review` do formalnego zatwierdzenia.

## 6. Testy i ograniczenia środowiska

Pełnego zestawu testów Pythona lokalnie nie uruchomiono, ponieważ dostępne połączenie pozwala edytować i odczytywać repozytorium przez GitHub, ale nie udostępnia lokalnego checkoutu repo. Wykonano skryptowy preflight na pobranych danych; wymagany jest zielony GitHub Actions Quality Gate dla tego PR przed scaleniem.

Nie oznaczono żadnego pytania jako `verified`. Nie rozpoczęto kursu cystern ani innego kursu.
