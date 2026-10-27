# Etap 4x87 — próbka 60, spójność kursu i egzaminów

- Data: 27.10.2026.
- Punkt wejściowy: świeży `main`, commit `4488b29ce3d1b94438deaa0b5fa6828ff0df07a0`.
- Gałąź robocza: `stage4x87-sample60-course-consistency-20261027`.
- Migawka banku po zmianach: `4a1a5d7f1ca8a5124eb096cd228aa92952fac6da`.
- Zakres: wyłącznie kurs podstawowy ADR.

## 1. Próbka 60 explanation

- Seed: `2026102787`.
- Generator: LCG (`state = 1664525 × state + 1013904223 mod 2^32`) oraz Fisher–Yates.
- Z puli wykluczono wszystkie ID znalezione w raportach 4x84 i 4x85 oraz jawnie wymienione zmiany z 4x86.
- **Ograniczenie identyfikacji próbek:** raport 4x86 nie zawiera pełnej listy 60 wylosowanych ID. Dlatego nie da się potwierdzić, że żadne ID tej próbki nie wystąpiło w nieopublikowanej części 4x86. Ograniczenie jest jawnie zapisane, zamiast deklarować niepotwierdzony brak przecięcia.
- Wynik: 60 explanation przeczytanych w kontekście pytania, trzech odpowiedzi, poprawnej litery i podstawy ADR; 6 pytań poprawionych, 54 bez zmian.
- Długość explanation w próbce: 300–498 znaków; 0 poniżej 200 lub 300 znaków; 0 jednozdaniowych; 0 zaczynających się od samego numeru przepisu; 0 zdań powyżej 35 słów w kontroli technicznej. W próbce: 2 wyjaśnienia z 3 zdaniami, 56 z 4, 2 z 5.

### ID sprawdzone w próbce

1. `ADR-B-0241`
2. `ADR-B-0025`
3. `ADR-B-0186`
4. `ADR-B-0099`
5. `ADR-B-0224`
6. `ADR-B-0323`
7. `ADR-B-0184`
8. `ADR-B-0167`
9. `ADR-B-0353`
10. `ADR-B-0067`
11. `ADR-B-0597`
12. `ADR-B-0484`
13. `ADR-B-0258`
14. `ADR-B-0234`
15. `ADR-B-0178`
16. `ADR-B-0262`
17. `ADR-B-0462`
18. `ADR-B-0020`
19. `ADR-B-0520`
20. `ADR-B-0094`
21. `ADR-B-0201`
22. `ADR-B-0288`
23. `ADR-B-0446`
24. `ADR-B-0523`
25. `ADR-B-0049`
26. `ADR-B-0508`
27. `ADR-B-0475`
28. `ADR-B-0565`
29. `ADR-B-0356`
30. `ADR-B-0516`
31. `ADR-B-0593`
32. `ADR-B-0031`
33. `ADR-B-0602`
34. `ADR-B-0604`
35. `ADR-B-0136`
36. `ADR-B-0358`
37. `ADR-B-0101`
38. `ADR-B-0359`
39. `ADR-B-0280`
40. `ADR-B-0089`
41. `ADR-B-0206`
42. `ADR-B-0236`
43. `ADR-B-0445`
44. `ADR-B-0085`
45. `ADR-B-0221`
46. `ADR-B-0391`
47. `ADR-B-0220`
48. `ADR-B-0250`
49. `ADR-B-0470`
50. `ADR-B-0050`
51. `ADR-B-0103`
52. `ADR-B-0438`
53. `ADR-B-0376`
54. `ADR-B-0023`
55. `ADR-B-0008`
56. `ADR-B-0425`
57. `ADR-B-0459`
58. `ADR-B-0053`
59. `ADR-B-0317`
60. `ADR-B-0456`

### Potwierdzone poprawki dydaktyczne

| ID | Problem przed zmianą | Zmiana |
|---|---|---|
| ADR-B-0101 | „Przejść przez rozlew, by sprawdzić głębokość” i zbieranie szmatką bez oceny zagrożenia były zbyt skrajne | Zbliżanie się po etykietę oraz poleganie na zwykłych rękawicach i zbieranie bez ustalenia zagrożenia |
| ADR-B-0186 | Zapraszanie obserwatorów do kabiny, aby obejrzeli dokumenty, było mało wiarygodne | Podejście do pojazdu w celu samodzielnego odczytania oznaczeń |
| ADR-B-0258 | Wymiary 10 cm i 80 cm były skrajnie nieprawdopodobne | Wiarygodniejsze błędne wysokości 20 cm i 40 cm przy zachowaniu poprawnych 30 cm |
| ADR-B-0356 | „Przenieść skażenie na siedzenie” brzmiało żartobliwie | Uznanie odzieży za bezpieczną, jeśli nie widać zabrudzenia, oraz zwykłe pranie bez ostrzeżenia o skażeniu |
| ADR-B-0470 | Zastąpienie znaku reklamą firmy było oczywiście absurdalne | Zmniejszenie znaku bez sprawdzenia pojemności i warunków przepisu |
| ADR-B-0484 | Wariant o gazach klasy 2.2 nie pasował do pytania o ciecz żrącą | Błędne uogólnienie, że wymóg dotyczy każdej cieczy żrącej bez względu na warunki |

Nie zmieniono poprawnych liter, ID, modułów ani podstaw prawnych. Wszystkie pytania zachowują `needs_review`. Zaktualizowano migawki sekwencyjne i A/B/C dla zmienionych ID. Migawka korekt: [4x87-distractor-snapshot](../../review/batches/4x87-distractor-snapshot-2026-10-27.json).

## 2. Odbiór kursanta lekcji B-10–B-13

| Lekcja | Pytania w banku | ID w lekcji | Brakujące / obce ID | Wynik |
|---|---:|---:|---:|---|
| B-10 | 55 | 55 | 0 / 0 | Zgodność referencji PASS |
| B-11 | 43 | 43 | 0 / 0 | Zgodność referencji PASS |
| B-12 | 44 | 44 | 0 / 0 | Zgodność referencji PASS |
| B-13 | 47 | 47 | 0 / 0 | Zgodność referencji PASS |
| **Razem** | **189** | **189** | **0 / 0** | **PASS** |

Przy odbiorze sprawdzono prosty sens przed odwołaniem do przepisu, przykłady z pracy kierowcy, podsumowanie, powiązane pytania i scenariusze. Nie wykryto potwierdzonej sprzeczności wymagającej zmiany tekstu tych lekcji. W tej partii ich nie przepisywano, aby nie zmieniać poprawnej treści bez konkretnego powodu.

## 3. Scenariusze praktyczne

- 39 scenariuszy, po 3 w każdym z 13 działów.
- Brak brakujących lub nieistniejących `question_ids`.
- Brak ID przypisanych do innego modułu.
- Wszystkie scenariusze mają sytuację, kroki kierowcy, typowe błędy, podstawę ADR, kryteria oceny i wniosek dla kursanta.
- Nie znaleziono potwierdzonego błędu wymagającego zmiany scenariusza.

## 4. Egzaminy próbne 001–005

Sprawdzono warianty i klucze względem aktualnego banku, uwzględniając, że kolejność A/B/C w arkuszu może różnić się od banku.

| Kontrola | Wynik |
|---|---:|
| Warianty / klucze | 5 / 5 |
| Pytań w każdym wariancie | 30 |
| Działy w każdym wariancie | 13 |
| Duplikaty w wariancie | 0 |
| Powtórzenia ID między wariantami | 0 |
| Rozkład klucza A/B/C w każdym wariancie | 10 / 10 / 10 |
| Najdłuższa seria tej samej litery | 3 |
| Rzeczywiste niezgodności opcji, poprawnej litery lub wyjaśnienia po remapowaniu | 0 |

Surowy tekst explanation w kluczu może mieć inne litery niż explanation banku, gdy wariant przestawia odpowiedzi. Dla ADR-B-0489 w wariancie 001 odwołanie do błędnej opcji C jest prawidłowe po remapowaniu opcji; nie uznano tego za rozbieżność. Wszystkie warianty i klucze otrzymały bieżące `source_bank_head`: `4a1a5d7f1ca8a5124eb096cd228aa92952fac6da`.

## 5. Pokrycie programu i sprawa dla specjalisty

Nie dopisano nowych pytań. Kontrola ścieżki lekcja–bank w 4x83 oraz aktualny Quality Gate nie wskazują potwierdzonej luki w pokryciu programu, która uzasadniałaby nowe ID bez dodatkowej podstawy. Nie zmieniono wartości prawnych ani progów na podstawie domysłu.

**Do niezależnej kontroli specjalisty:** ADR-B-0145 / M364, ponieważ zapisany termin 31.12.2026 zbliża się i trzeba potwierdzić urzędowy status porozumienia oraz ewentualne przedłużenie. Do czasu sprawdzenia oficjalnego źródła nie zmieniano odpowiedzi.

## 6. Quality Gate — preflight na gałęzi

- Pytania: 609; unikalne ID: 609; duplikaty: 0.
- Statusy: 609 `needs_review`, 0 `verified`.
- Explanation minimum: 300 znaków; poniżej 200: 0; poniżej 300: 0.
- Poprawna odpowiedź jest jedyną najdłuższą: 73/609 = **11,99%**.
- Wszystkie 13 działów poniżej 16%; najwyższy wskaźnik: B-02 i B-03, po 14,29%.
- Warianty i klucze zsynchronizowane z bankiem; snapshoty audytu odświeżone dla sześciu zmienionych ID.

Testów lokalnych nie deklaruję: dostępna integracja umożliwia edycję repozytorium przez GitHub, ale nie udostępnia lokalnego checkoutu do uruchomienia Pythona. Warunkiem scalenia jest zielony CI Quality Gate na PR; jego wynik zostanie odnotowany po zakończeniu workflow.

## Status

To przegląd dydaktyczny, spójności i integralności artefaktów — nie niezależna recenzja prawna. Wszystkie pytania pozostają `needs_review`; niczego nie oznaczono jako `verified`. Zakres pracy obejmuje wyłącznie kurs podstawowy ADR.
