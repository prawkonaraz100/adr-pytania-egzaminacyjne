# Etap 4x105 — próbka 40 explanation, przegląd scenariuszy i egzaminów

- Data: 2026-10-27.
- Punkt wejścia: świeży `main`, commit `e74541fbad7a307514cee92986b1ea133f43bbfc`.
- Zakres: wyłącznie kurs podstawowy ADR.
- Bank: 609 pytań, ID `ADR-B-0001`–`ADR-B-0609`; wszystkie `needs_review`, 0 `verified`.
- Bieżący Quality Gate na `main`: PASS, GitHub Actions run [#40591135392](https://github.com/prawkonaraz100/adr-pytania-egzaminacyjne/actions/runs/40591135392).

## 1. Próbka 40 explanation

Próbkę wylosowano deterministycznie algorytmem LCG/Fisher–Yates, seed `41052026`. Wyłączono 75 unikalnych ID z jawnych list próbek etapów 4x103 i 4x104. Próbka została przeczytana w kontekście pytania, trzech odpowiedzi, poprawnej litery i podstawy ADR.

**Wylosowane ID:**
```
ADR-B-0079, ADR-B-0284, ADR-B-0427, ADR-B-0392, ADR-B-0206, ADR-B-0223, ADR-B-0044, ADR-B-0026, ADR-B-0335, ADR-B-0025, ADR-B-0080, ADR-B-0231, ADR-B-0580, ADR-B-0162, ADR-B-0385, ADR-B-0327, ADR-B-0472, ADR-B-0031, ADR-B-0352, ADR-B-0332, ADR-B-0524, ADR-B-0348, ADR-B-0024, ADR-B-0136, ADR-B-0300, ADR-B-0420, ADR-B-0562, ADR-B-0259, ADR-B-0175, ADR-B-0130, ADR-B-0459, ADR-B-0539, ADR-B-0383, ADR-B-0326, ADR-B-0605, ADR-B-0558, ADR-B-0184, ADR-B-0188, ADR-B-0265, ADR-B-0247
```

### Wynik przeglądu

- Przeczytano: **40/40** explanation.
- Explanation przepisane: **0**.
- Pozostawione bez zmian po ręcznej ocenie: **40**.
- Długość: **302–457 znaków**.
- Liczba zdań: **3–5** dla każdej pozycji.
- Najdłuższe zdanie: **28 słów**; zdania ponad 35 słów: **0**.
- Explanation poniżej 200 znaków w całym banku: **0**; minimum w banku: **300 znaków**.

Nie znaleziono w tej próbce wyjaśnienia, które zaczynałoby się od suchego cytatu przepisu, nie tłumaczyło sensu poprawnej odpowiedzi albo pozostawiało główną błędną odpowiedź bez wyjaśnienia. Przykładowo ADR-B-0079 wyjaśnia, czemu pas nie może deformować opakowania; ADR-B-0392 opisuje warunki połączenia dwóch funkcji dokumentu; ADR-B-0539 rozróżnia kod tunelowy i postać przewozu. Nie dopisywano zmian wyłącznie po to, by zwiększyć liczbę edycji.

## 2. Scenariusze praktyczne

Sprawdzono wszystkie **39 scenariuszy** z `podstawowy/praktyka/scenariusze-13-dzialow.json`:

| Kontrola | Wynik |
|---|---:|
| Scenariusze łącznie | 39 |
| Scenariusze z kompletem kroków kierowcy (minimum 3) | 39/39 |
| Scenariusze z typowymi błędami kursanta | 39/39 |
| Scenariusze z podstawą ADR | 39/39 |
| Scenariusze z kryteriami oceny | 39/39 |
| Scenariusze z podsumowaniem dla kursanta | 39/39 |
| Nieistniejące lub przypisane do innego działu `question_ids` | 0 |
| Braki wymagające potwierdzonej poprawki | 0 |

Każdy scenariusz ma kroki działania, błędy z objaśnieniem, podstawę prawną, kryteria oceny, wniosek dla kursanta i odwołania do pytań właściwego działu. W tej kontroli nie wykryto potwierdzonej luki ani sprzeczności, więc scenariuszy nie zmieniano.

## 3. Egzaminy próbne 001–005

Wszystkie warianty i klucze sprawdzono względem aktualnego banku, z uwzględnieniem mapowania liter A/B/C po zmianie kolejności opcji.

| Wariant | Pytania | Unikalne ID | Zgodność klucza i explanation | A/B/C | Najdłuższa seria |
|---|---:|---:|---:|---:|---:|
| 001 | 30 | 30 | PASS | 10/10/10 | 3 |
| 002 | 30 | 30 | PASS | 10/10/10 | 3 |
| 003 | 30 | 30 | PASS | 10/10/10 | 3 |
| 004 | 30 | 30 | PASS | 10/10/10 | 3 |
| 005 | 30 | 30 | PASS | 10/10/10 | 3 |

- Każdy arkusz obejmuje 13 działów i ma 2–3 pytania z działu.
- W każdym wariancie brak powtórzonych ID; łącznie jest 150 unikalnych ID między pięcioma wariantami.
- Każdy wariant i klucz wskazuje aktualny blob banku: `d9b60f583d5176d0f34ace407933d4d883c9b911`.
- Porównanie poprawnego tekstu odpowiedzi oraz explanation w kluczu z bankiem: **0 rozbieżności**. Pozorna różnica przy ADR-B-0489 wynika z poprawnego przemapowania odniesienia do litery odpowiedzi po przestawieniu opcji; nie jest błędem klucza.
- Nie zmieniono pytań, explanation ani kolejności odpowiedzi, więc nie było potrzeby regeneracji arkuszy lub snapshotów audytu.

## 4. Quality Gate — metryki banku

| Dział | Pytania | Poprawna = jedyna najdłuższa | Wskaźnik |
|---|---:|---:|---:|
| B-01 | 45 | 6 | 13,33% |
| B-02 | 56 | 8 | 14,29% |
| B-03 | 49 | 7 | 14,29% |
| B-04 | 46 | 6 | 13,04% |
| B-05 | 43 | 5 | 11,63% |
| B-06 | 45 | 5 | 11,11% |
| B-07 | 48 | 6 | 12,50% |
| B-08 | 42 | 5 | 11,90% |
| B-09 | 46 | 4 | 8,70% |
| B-10 | 55 | 4 | 7,27% |
| B-11 | 43 | 6 | 13,95% |
| B-12 | 44 | 6 | 13,64% |
| B-13 | 47 | 5 | 10,64% |
| **Razem** | **609** | **73** | **11,99%** |

- Unikalne ID: 609/609.
- Explanation poniżej 200 znaków: 0; minimum: 300 znaków.
- Statusy: 609 `needs_review`, 0 `verified`.

## 5. Testy i ograniczenia

Dane zostały sprawdzone skryptowo na plikach pobranych przez GitHub, a wyniki ręcznej oceny próbki zapisano powyżej. Dostępne połączenie nie udostępnia lokalnego checkoutu repozytorium, więc **nie deklaruję uruchomienia testów lokalnych**. PR wymaga zielonego Quality Gate w GitHub Actions przed scaleniem.

Brak zmian w banku oznacza, że nie zmieniono statusów prawnych, poprawnych liter, kluczy, snapshotów audytu ani pakietu recenzyjnego. Żadne pytanie nie zostało oznaczone jako `verified`. Nie rozpoczęto kursu cystern ani innego kursu.
