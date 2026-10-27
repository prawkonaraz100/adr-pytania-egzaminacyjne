# Etap 4x69 — raport końcowy: scenariusze, lekcje i próbka explanation

Data: 27.10.2026. Zakres wyłącznie kurs podstawowy ADR. Punkt bazowy: `main` `de4c2a640ae791bb1bbb2367588e44df60b7563e`.

## 1. Rezultat partii

| PR | Zakres | Wynik |
|---|---|---|
| [#524](https://github.com/prawkonaraz100/adr-pytania-egzaminacyjne/pull/524) | B-01–04 | PASS CI; 196 pytań i 12 scenariuszy sprawdzonych; usunięto powtórzenie redakcyjne w B-02 |
| [#525](https://github.com/prawkonaraz100/adr-pytania-egzaminacyjne/pull/525) | B-05–08 | PASS CI; poprawiono powtórzony zestaw pytań scenariuszy B-07; dodano blokujący test regresyjny |
| B-09–13 | Kontrola mapowania i czytelności | Wszystkie ID scenariuszy i pytań istnieją oraz należą do właściwych modułów; poprawiono jedno explanation w B-11 |

## 2. Kontrola 13 lekcji i 39 scenariuszy

- Bank zawiera **609 pytań**; każda lekcja odwołuje się do pytań swojego modułu, bez brakujących ID i bez pytań z obcych modułów.
- **39 scenariuszy** — po 3 dla każdego z 13 działów.
- Wszystkie scenariusze mają co najmniej 3 kroki, granicę bezpieczeństwa i powiązane ID z właściwego modułu.
- Po korekcie B-07 nie ma identycznych zestawów pytań w dwóch scenariuszach tego samego działu.
- `SC-ADR-B-07-03` pozostaje z jednym pytaniem (`ADR-B-0019`), bo sprawdza wąski obowiązek zapewnienia instrukcji pisemnych; nie dodawano sztucznie niepowiązanych pytań.
- Lekcje B-01–04 sprawdzono oczami początkującego. Nie znaleziono potwierdzonego błędu prawnego; w B-02 usunięto tylko powtórzoną definicję, zachowując informacje o kolumnach tabeli A.

## 3. Deterministyczna próba wyjaśnień — wszystkie pozostałe ID

W raportach prób 4x51–4x68 znaleziono łącznie **589 różnych ID** użytych w poprzednich próbach redakcyjnych. Z banku 609 pytań pozostało tylko **20 niepowtarzanych ID**. Z tego powodu uczciwa próba **60 nowych, niepowtarzanych pytań jest niemożliwa** bez ponownego wykorzystania wcześniejszych ID. Zamiast pozorować próbę 60, ręcznie przejrzano wszystkie 20 pozostałych kandydatów (seed referencyjny `2026102769`; pula po wykluczeniach wynosiła 20).

| ID | Dział | Wynik |
|---|---|---|
| `ADR-B-0001` | ADR-B-01 | Fałszywy alarm / bez zmiany — sens poprawnej odpowiedzi, najważniejsza błędna alternatywa i podstawa ADR wyjaśnione w 3–5 zdaniach. |
| `ADR-B-0008` | ADR-B-03 | Fałszywy alarm / bez zmiany — sens poprawnej odpowiedzi, najważniejsza błędna alternatywa i podstawa ADR wyjaśnione w 3–5 zdaniach. |
| `ADR-B-0031` | ADR-B-11 | **Przepisano** — usunięto powtórzenie; doprecyzowano sens kategorii tunelu A i dlaczego A/C są błędne. |
| `ADR-B-0032` | ADR-B-11 | Fałszywy alarm / bez zmiany — sens poprawnej odpowiedzi, najważniejsza błędna alternatywa i podstawa ADR wyjaśnione w 3–5 zdaniach. |
| `ADR-B-0035` | ADR-B-12 | Fałszywy alarm / bez zmiany — sens poprawnej odpowiedzi, najważniejsza błędna alternatywa i podstawa ADR wyjaśnione w 3–5 zdaniach. |
| `ADR-B-0036` | ADR-B-12 | Fałszywy alarm / bez zmiany — sens poprawnej odpowiedzi, najważniejsza błędna alternatywa i podstawa ADR wyjaśnione w 3–5 zdaniach. |
| `ADR-B-0042` | ADR-B-02 | Fałszywy alarm / bez zmiany — sens poprawnej odpowiedzi, najważniejsza błędna alternatywa i podstawa ADR wyjaśnione w 3–5 zdaniach. |
| `ADR-B-0044` | ADR-B-02 | Fałszywy alarm / bez zmiany — sens poprawnej odpowiedzi, najważniejsza błędna alternatywa i podstawa ADR wyjaśnione w 3–5 zdaniach. |
| `ADR-B-0052` | ADR-B-06 | Fałszywy alarm / bez zmiany — sens poprawnej odpowiedzi, najważniejsza błędna alternatywa i podstawa ADR wyjaśnione w 3–5 zdaniach. |
| `ADR-B-0053` | ADR-B-06 | Fałszywy alarm / bez zmiany — sens poprawnej odpowiedzi, najważniejsza błędna alternatywa i podstawa ADR wyjaśnione w 3–5 zdaniach. |
| `ADR-B-0056` | ADR-B-08 | Fałszywy alarm / bez zmiany — sens poprawnej odpowiedzi, najważniejsza błędna alternatywa i podstawa ADR wyjaśnione w 3–5 zdaniach. |
| `ADR-B-0060` | ADR-B-09 | Fałszywy alarm / bez zmiany — sens poprawnej odpowiedzi, najważniejsza błędna alternatywa i podstawa ADR wyjaśnione w 3–5 zdaniach. |
| `ADR-B-0063` | ADR-B-11 | Fałszywy alarm / bez zmiany — sens poprawnej odpowiedzi, najważniejsza błędna alternatywa i podstawa ADR wyjaśnione w 3–5 zdaniach. |
| `ADR-B-0116` | ADR-B-07 | Fałszywy alarm / bez zmiany — sens poprawnej odpowiedzi, najważniejsza błędna alternatywa i podstawa ADR wyjaśnione w 3–5 zdaniach. |
| `ADR-B-0120` | ADR-B-12 | Fałszywy alarm / bez zmiany — sens poprawnej odpowiedzi, najważniejsza błędna alternatywa i podstawa ADR wyjaśnione w 3–5 zdaniach. |
| `ADR-B-0211` | ADR-B-12 | Fałszywy alarm / bez zmiany — sens poprawnej odpowiedzi, najważniejsza błędna alternatywa i podstawa ADR wyjaśnione w 3–5 zdaniach. |
| `ADR-B-0259` | ADR-B-01 | Fałszywy alarm / bez zmiany — sens poprawnej odpowiedzi, najważniejsza błędna alternatywa i podstawa ADR wyjaśnione w 3–5 zdaniach. |
| `ADR-B-0518` | ADR-B-09 | Fałszywy alarm / bez zmiany — sens poprawnej odpowiedzi, najważniejsza błędna alternatywa i podstawa ADR wyjaśnione w 3–5 zdaniach. |
| `ADR-B-0519` | ADR-B-12 | Fałszywy alarm / bez zmiany — sens poprawnej odpowiedzi, najważniejsza błędna alternatywa i podstawa ADR wyjaśnione w 3–5 zdaniach. |
| `ADR-B-0558` | ADR-B-09 | Fałszywy alarm / bez zmiany — sens poprawnej odpowiedzi, najważniejsza błędna alternatywa i podstawa ADR wyjaśnione w 3–5 zdaniach. |

**Wynik próbki:** 1 explanation przepisano; 19 pozostawiono bez zmian po sprawdzeniu. Zakres długości po korekcie: 304–430 znaków (w tym `ADR-B-0031`: 374 znaki). Wszystkie 20 pozostają `needs_review`; przegląd językowy nie potwierdza prawnej poprawności odpowiedzi.

## 4. Wskaźniki po zmianach

| Dział | Poprawna jedyną najdłuższą | Odsetek |
|---|---:|---:|
| ADR-B-01 | 6/45 | 13.33% |
| ADR-B-02 | 7/56 | 12.50% |
| ADR-B-03 | 7/49 | 14.29% |
| ADR-B-04 | 6/46 | 13.04% |
| ADR-B-05 | 5/43 | 11.63% |
| ADR-B-06 | 5/45 | 11.11% |
| ADR-B-07 | 6/48 | 12.50% |
| ADR-B-08 | 5/42 | 11.90% |
| ADR-B-09 | 4/46 | 8.70% |
| ADR-B-10 | 4/55 | 7.27% |
| ADR-B-11 | 6/43 | 13.95% |
| ADR-B-12 | 6/44 | 13.64% |
| ADR-B-13 | 5/47 | 10.64% |
| **Całość** | **72/609** | **11,82%** |

- Explanation minimum: 300 znaków; poniżej 200: 0.
- Duplikaty ID banku: 0.
- Statusy: 609 `needs_review`, 0 `verified`.
- Poprawne litery, ID i `module_id` nie zmieniły się; zmieniono wyłącznie explanation `ADR-B-0031` oraz mapowanie pytań w `SC-ADR-B-07-02`.

## 5. Egzaminy próbne i pakiet specjalisty

- Warianty i klucze 001–005 nie wymagały regeneracji: nie zmieniono ID ani poprawnych liter, a CI sprawdza synchronizację arkuszy i kluczy z bankiem.
- Zaktualizowano migawkę pakietu recenzyjnego do nowego blob SHA banku, zachowując liczbę pytań, 13 działów, 39 scenariuszy i 0 formalnych zatwierdzeń.
- Lista kontrolna dla specjalisty i liczba nierozstrzygniętych porównań literalnych pozostają otwarte; nie oznaczono żadnego pytania jako `verified`.

## 6. Quality Gate i ograniczenia

- Preflight przez API: 609 unikalnych ID, brak wyjaśnień poniżej 300 znaków, 39 scenariuszy z istniejącymi i zgodnymi modułowo ID, brak identycznych zestawów scenariuszy w module.
- Testy automatyczne uruchomiono w CI na PR; nie deklarujemy uruchomienia lokalnego test runnera w tym środowisku.
- Pełna, niezależna literalna recenzja prawna ADR 2025 nadal należy do specjalisty.
