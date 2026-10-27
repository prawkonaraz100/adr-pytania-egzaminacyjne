# Etap 4x92 — odbiór B-06–B-13, próbka 60 explanation i kontrola wartości

- Data: 27.10.2026.
- Punkt wejścia: świeży `main`, `64a9d00df096a7eb551eed6fb472daa5ec53c66f`.
- Zakres: wyłącznie kurs podstawowy ADR.
- Bank: 609 pytań, blob `4a1a5d7f1ca8a5124eb096cd228aa92952fac6da`.

## 1. Próbka 60 explanation

- Seed: `2026102792`; LCG + Fisher–Yates.
- Pula po wykluczeniu ID widocznych w raportach 4x84–4x91: 234 pytania, z których wybrano 60.
- Zastrzeżenie: raport 4x86 nie zawiera kompletnej listy wszystkich 60 ID. Z tego powodu brak przecięcia z nieujawnioną częścią tej próbki pozostaje nieudowodniony. Pula wykluczyła wszystkie ID jawnie widoczne w raportach, a niepewność pozostaje w raporcie.
- Ręcznie sprawdzono pytanie, odpowiedzi A/B/C, poprawną literę, explanation i podaną podstawę. Explanation miały 300–454 znaków; 57 miało 4 zdania, 2 miały 3 zdania, 1 miało 5 zdań. Nie wykryto zdania dłuższego niż 35 słów ani wyjaśnienia zaczynającego się od samego numeru przepisu.
- **Potwierdzone poprawki: 0.** W tej próbce nie znaleziono wyjaśnienia wymagającego przeredagowania ani potwierdzonej niejednoznaczności opcji.

### Lista sprawdzonych ID

```
ADR-B-0043, ADR-B-0165, ADR-B-0348, ADR-B-0554, ADR-B-0273,
ADR-B-0550, ADR-B-0015, ADR-B-0488, ADR-B-0435, ADR-B-0070,
ADR-B-0340, ADR-B-0166, ADR-B-0289, ADR-B-0396, ADR-B-0119,
ADR-B-0105, ADR-B-0474, ADR-B-0529, ADR-B-0400, ADR-B-0375,
ADR-B-0072, ADR-B-0473, ADR-B-0416, ADR-B-0297, ADR-B-0420,
ADR-B-0200, ADR-B-0331, ADR-B-0256, ADR-B-0453, ADR-B-0410,
ADR-B-0444, ADR-B-0106, ADR-B-0121, ADR-B-0238, ADR-B-0449,
ADR-B-0480, ADR-B-0583, ADR-B-0505, ADR-B-0346, ADR-B-0292,
ADR-B-0344, ADR-B-0481, ADR-B-0349, ADR-B-0395, ADR-B-0164,
ADR-B-0329, ADR-B-0144, ADR-B-0075, ADR-B-0227, ADR-B-0492,
ADR-B-0507, ADR-B-0194, ADR-B-0088, ADR-B-0345, ADR-B-0601,
ADR-B-0591, ADR-B-0419, ADR-B-0242, ADR-B-0303, ADR-B-0324
```

## 2. Odbiór lekcji B-06–B-13

| Lekcja | Pytań w module | ID w lekcji | Brakujące ID | Wprowadzenie, cele, błędy, scenariusze, podsumowanie i podstawa |
|---|---:|---:|---:|---|
| B-06 | 45 | 45 | 0 | Wszystkie obecne |
| B-07 | 48 | 48 | 0 | Wszystkie obecne |
| B-08 | 42 | 42 | 0 | Wszystkie obecne |
| B-09 | 46 | 46 | 0 | Wszystkie obecne |
| B-10 | 55 | 55 | 0 | Wszystkie obecne |
| B-11 | 43 | 43 | 0 | Wszystkie obecne |
| B-12 | 44 | 44 | 0 | Wszystkie obecne |
| B-13 | 47 | 47 | 0 | Wszystkie obecne |
| **Razem** | **370** | **370** | **0** | **Referencje PASS** |

Każda z ośmiu lekcji zawiera cele, rozdziały merytoryczne, typowe błędy kursantów, scenariusze praktyczne, podsumowanie, pytania kontrolne, odwołania do pytań i podstawę prawną. Wszystkie ID pytań z tych modułów istnieją i należą do właściwego działu. Nie znaleziono potwierdzonej sprzeczności wymagającej zmiany treści.

## 3. Kontrola wartości i terminów wrażliwych

Wykonano skryptowy spis wartości liczbowych i punktów ADR w pytaniach B-06–B-13 oraz porównano je z lekcjami. Ręcznie sprawdzono reprezentatywne reguły z rejestru 4x90 i przypadki, w których ta sama liczba może oznaczać wartość prawną albo jedynie błędną odpowiedź.

| Reguła / wartość | Porównane źródła | Wynik |
|---|---|---|
| Tablica pomarańczowa: standard 400×300 mm i warunkowy format 300×120 mm; obrzeże odpowiednio 15 mm / 10 mm | B-06, ADR-B-0018, 0191, 0258 | Zgodne w sprawdzonych pytaniach i lekcji |
| Oznakowanie dużego formatu i położenie nalepek | B-06, pytania o tablice i kontenery | Zgodne; nie znaleziono potwierdzonej sprzeczności |
| Obowiązki uczestników: nadawca, przewoźnik, pakujący, załadowca i odbiorca | B-07, pytania o role i uszkodzone opakowania | Zgodne w sprawdzonych przypadkach; polecenie handlowe nie usuwa obowiązku ADR |
| Gaśnice: minimum 4 / 8 / 12 kg w zależności od DMC; odrębna reguła 8.1.4.2 dla 1.1.3.6 | B-08, ADR-B-0022, 0071–0074, 0420 | Zgodne; 3,5 t i 7,5 t są rozgraniczone zgodnie z opisem przedziałów |
| Wspólny załadunek, piętrzenie, mocowanie i czyszczenie po wycieku | B-09, pytania o 0,8 m, 7.5.2, 7.5.7 i 7.5.8 | Zgodne w sprawdzonych przypadkach |
| ADR/RID/IMDG, odcinek morsko-drogowy i dokumenty dla butli DOT | B-10, pytania z 1.1.4.2 i 1.1.4.7 | Nie wykryto potwierdzonej rozbieżności; sam port ani dokument morski nie stanowią automatycznego zwolnienia |
| Kody D/E, zapis `(-)` oraz kod B1000C i próg 1000 kg netto | B-11, ADR-B-0033, 0264, 0488, 0490, 0576, 0603, 0604 | Zgodne w sprawdzonych pytaniach i lekcji |
| Ochrona przewozu, plan ochrony, dostęp do informacji i nadzór postoju | B-12, pytania z ADR 1.10 i 8.4 | Nie wykryto potwierdzonej rozbieżności w sprawdzonym zakresie |
| Dokument przewozowy, instrukcje pisemne, identyfikacja załogi i szczególne zapisy | B-13, pytania z ADR 5.4, 8.1.2 i 1.10 | Zgodne w sprawdzonych przypadkach |
| M364 i świadectwo dopuszczenia przyczepy | B-08/B-13, ADR-B-0145, rejestr 4x88–4x90 | Bez zmiany. Przed użyciem materiału po 31.12.2026 trzeba ponownie sprawdzić aktualny wpis UNECE i polską publikację |

W tej kontroli nie znaleziono potwierdzonego błędu prawnego. Nie zmieniano żadnej wartości na podstawie domysłu. To kontrola skryptowa oraz ukierunkowany przegląd reprezentatywnych przypadków, a nie formalna recenzja wszystkich 609 rekordów przez specjalistę.

## 4. Scenariusze praktyczne

- Liczba scenariuszy: 39; dokładnie 3 w każdym z 13 działów.
- Dla B-06–B-13 sprawdzono 24 scenariusze: wszystkie mają cztery kroki, podstawę ADR, typowe błędy, kryteria oceny i powiązane pytania.
- Nieistniejące lub przypisane do złego działu `question_ids`: 0.
- Braki wymaganych pól: 0.

Nie stwierdzono potrzeby zmiany scenariuszy.

## 5. Egzaminy próbne 001–005

Ponownie sprawdzono warianty i klucze względem bieżącego banku; nie wprowadzano zmian w pytaniach.

| Wariant | Pytania / unikalne ID | Działy | Rozkład A/B/C | Najdłuższa seria | Zgodność klucza |
|---|---|---:|---|---:|---|
| 001 | 30 / 30 | 13 | 10/10/10 | 3 | PASS |
| 002 | 30 / 30 | 13 | 10/10/10 | 3 | PASS |
| 003 | 30 / 30 | 13 | 10/10/10 | 3 | PASS |
| 004 | 30 / 30 | 13 | 10/10/10 | 3 | PASS |
| 005 | 30 / 30 | 13 | 10/10/10 | 3 | PASS |

Każdy wariant i klucz wskazuje aktualny blob banku `4a1a5d7f1ca8a5124eb096cd228aa92952fac6da`. Nie było potrzeby regeneracji egzaminów ani odświeżania snapshotów.

## 6. Quality Gate — stan po 4x91

- Bank: 609 pytań, 609 unikalnych ID, 0 duplikatów.
- Status: 609 `needs_review`, 0 `verified`.
- Explanation: minimum 300 znaków; 0 poniżej 200.
- Poprawna odpowiedź jest jedyną najdłuższą: 73/609 = 11,99%; maksimum działu 14,29%.
- Ostatni PASS na `main` przed tą partią: [run #40543750084](https://github.com/prawkonaraz100/adr-pytania-egzaminacyjne/actions/runs/40543750084).

Pełnego lokalnego checkoutu repozytorium nie udostępnia połączenie GitHub, więc nie deklaruję lokalnego uruchomienia testów Pythona. Kontrole skryptowe wykonano na pobranych plikach; przed scaleniem wymagany jest PASS GitHub Actions.

Nie zmieniono pytań, kluczy, podstaw prawnych ani statusów. Nie rozpoczęto kursu cystern ani innego kursu.
