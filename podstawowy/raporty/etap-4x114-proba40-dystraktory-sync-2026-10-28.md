# Etap 4x114 — próbka 40, dystraktory i synchronizacja egzaminów

- Data: 2026-10-28.
- Punkt wyjścia: `main` `912c176ee4755af25cce3abf70614ae8ee9a630c`, Quality Gate ostatniego przebiegu PASS.
- Zakres: wyłącznie kurs podstawowy ADR.
- Bank przed poprawkami: 609 pytań, blob `2675c0636a421bf3b4347ad0117087d6ec633321`.
- Bank po poprawkach: 609 pytań, blob `04d7246d074d6f12fc46e91b4b47fc0e2364f0f0`; ID i poprawne litery niezmienione.

## 1. Próba i powtarzalność

Seed: `41142026`; algorytm LCG + Fisher–Yates. Z puli 146 pytań pozostałych po wykluczeniu ID zapisanych w manifestach etapów 4x107–4x113 wylosowano 40 unikalnych ID. Próbka nie nakłada się na zarejestrowane próbki poprzednich etapów.

ID próbki: `ADR-B-0473`, `ADR-B-0222`, `ADR-B-0190`, `ADR-B-0063`, `ADR-B-0219`, `ADR-B-0102`, `ADR-B-0490`, `ADR-B-0171`, `ADR-B-0336`, `ADR-B-0182`, `ADR-B-0412`, `ADR-B-0132`, `ADR-B-0213`, `ADR-B-0121`, `ADR-B-0277`, `ADR-B-0378`, `ADR-B-0355`, `ADR-B-0588`, `ADR-B-0546`, `ADR-B-0572`, `ADR-B-0145`, `ADR-B-0508`, `ADR-B-0433`, `ADR-B-0460`, `ADR-B-0350`, `ADR-B-0330`, `ADR-B-0255`, `ADR-B-0608`, `ADR-B-0075`, `ADR-B-0338`, `ADR-B-0103`, `ADR-B-0311`, `ADR-B-0386`, `ADR-B-0452`, `ADR-B-0395`, `ADR-B-0421`, `ADR-B-0316`, `ADR-B-0438`, `ADR-B-0556`, `ADR-B-0486`.

Manifest wraz z pełnym zestawem wykluczeń znajduje się w [etap-4x114-wykluczenia-proby.json](etap-4x114-wykluczenia-proby.json).

## 2. Wynik przeglądu

Ręcznie sprawdzono wszystkie 40 pytań pod kątem zrozumiałości explanation, wiarygodności dystraktorów, jednoznaczności i zgodności klucza z treścią.

- **34 pytania** pozostawiono bez zmian: explanation już wyjaśniały sens odpowiedzi, typową pomyłkę i podstawę ADR w prostym języku.
- **6 pytań** miało potwierdzoną słabość redakcyjną dystraktorów; poprawiono łącznie **9 błędnych opcji** oraz dopasowano do nich explanation.
- Nie zmieniono ID, poprawnych liter, kluczy merytorycznych ani podstaw prawnych.
- Po zmianach explanation w sześciu poprawionych pytaniach mają 318–389 znaków i wyjaśniają, dlaczego nowe dystraktory są błędne.

| ID | Problem | Poprawka |
|---|---|---|
| ADR-B-0190 | Dystraktor A miał nienaturalną frazę i nieczytelnie opisywał górne pole tablicy. | Zmieniono A tak, by opisywał prawdziwą funkcję numeru UN, ale błędnie przypisywał ją do górnego pola. |
| ADR-B-0433 | Opcje B i C były zbyt skrajne i słabo odróżniały błąd w interpretacji znaku tunelowego. | Wprowadzono realistyczne pomyłki: automatyczny zakaz dla wszystkich przewozów ADR i poleganie wyłącznie na nalepce klasy. |
| ADR-B-0378 | Opcje B i C odwoływały się do przypadkowych lub oczywiście nieuprawnionych osób. | Zastąpiono je pomyłką polegającą na odłożeniu oznakowania do dostawy oraz próbą zastąpienia nalepek wpisem w dokumencie. |
| ADR-B-0355 | „Rozpoznać substancję po zapachu” było zbyt oczywistym dystraktorem. | Zmieniono na niebezpieczną, lecz bardziej realistyczną próbę podejścia od strony, w którą wiatr niesie opary. |
| ADR-B-0330 | Opcja C („dopiero po rozładunku”) była mało wiarygodna. | Zastąpiono ją błędnym przekonaniem, że zgoda załadowcy może uchylić wyłączenie z procedury. |
| ADR-B-0316 | Odpowiedzi B i C odwoływały się do odległych klas zagrożeń. | Zastąpiono je bardziej diagnostycznym rozróżnieniem wybuchu ograniczonego i masowego. |

Podstawy prawne dla zmienionych pozycji pozostają zgodne z istniejącymi źródłami: ADR 5.3.2.2.2, 1.9.5.3.5 i 8.6.3, 1.4.3.1.1(c) i 5.3, 5.4.3.4, 2.1.3.5.3 i 2.1.3.5.5 oraz 2.2.1.1.5. Zmiany są redakcyjne; nie wprowadzają nowych twierdzeń prawnych.

## 3. Spójność lekcji, scenariuszy i egzaminów

- Wszystkie 13 lekcji: od 42 do 56 odwołań do ID pytań; **0 nieistniejących ID i 0 odwołań do pytań z innego działu**.
- Scenariusze: 39/39; każdy ma 4 kroki, typowe błędy i kryteria oceny; **0 brakujących ID i 0 ID z niewłaściwego działu**.
- Warianty egzaminu 001–005: 30 pytań każdy; wszystkie ID istnieją i moduły się zgadzają. Zmienione treści zsynchronizowano w wariantach 002 i 003, w których występują ADR-B-0433 i ADR-B-0378. We wszystkich wariantach zaktualizowano `source_bank_head`.
- Klucze 001–005: po 30 odpowiedzi; poprawna odpowiedź odpowiada tekstowi opcji w wariancie dla wszystkich 150 pozycji. Explanation dla zmienionych pytań zsynchronizowano w kluczach 002 i 003. Wszystkie klucze wskazują nowy blob banku.

## 4. Quality Gate — preflight

- Liczba pytań: 609; zduplikowane ID: 0.
- Poprawna odpowiedź jest jedyną najdłuższą: 73/609 = 11.99% (limit 18%).
- Najwyższy wskaźnik działu: 14.29%.
- Najkrótsze explanation: 300 znaków; poniżej 200 znaków: 0.
- Status: 609 `needs_review`, 0 `verified`.

| Dział | Liczba pytań | Klucz A/B/C | Poprawna jedyną najdłuższą | Min. explanation |
|---|---:|---:|---:|---:|
| ADR-B-01 | 45 | 17/17/11 | 6/45 (13.33%) | 300 |
| ADR-B-02 | 56 | 21/19/16 | 8/56 (14.29%) | 300 |
| ADR-B-03 | 49 | 16/21/12 | 5/49 (10.20%) | 300 |
| ADR-B-04 | 46 | 15/18/13 | 6/46 (13.04%) | 301 |
| ADR-B-05 | 43 | 18/14/11 | 5/43 (11.63%) | 300 |
| ADR-B-06 | 45 | 16/14/15 | 6/45 (13.33%) | 301 |
| ADR-B-07 | 48 | 18/18/12 | 6/48 (12.50%) | 304 |
| ADR-B-08 | 42 | 12/12/18 | 5/42 (11.90%) | 303 |
| ADR-B-09 | 46 | 13/15/18 | 5/46 (10.87%) | 301 |
| ADR-B-10 | 55 | 19/18/18 | 4/55 (7.27%) | 308 |
| ADR-B-11 | 43 | 12/13/18 | 6/43 (13.95%) | 300 |
| ADR-B-12 | 44 | 14/13/17 | 6/44 (13.64%) | 303 |
| ADR-B-13 | 47 | 15/15/17 | 5/47 (10.64%) | 308 |

Wykonano preflight na danych pobranych z GitHub. Nie uruchamiano testów w lokalnym checkout repozytorium; wynik końcowy zależy od pełnego CI na PR. Nie oznaczono żadnego pytania jako `verified`.
