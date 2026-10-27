# Etap 4x80 — lekcje B-05–09, spójność scenariuszy i próba wyjaśnień

- Data: 27.10.2026.
- Punkt wejściowy: `main` `c6285c98c420cd70ff4b61af402e1d8b851ff783`.
- Zakres: wyłącznie kurs podstawowy ADR.

## 1. Stan banku i Quality Gate

- 609 pytań i 609 unikalnych ID; wszystkie `needs_review`, 0 `verified`.
- „Poprawna = jedyna najdłuższa”: 73/609 = **11,99%**.
- Najkrótsze explanation: 300 znaków; 0 poniżej 200.
- Po tej partii nie zmieniano ID, opcji ani klucza. Zmieniono wyłącznie cztery wyjaśnienia, żeby objaśnić skrót UN przy pierwszym użyciu.
- Testy lokalne nie mogły zostać uruchomione z poziomu dostępnej integracji GitHub (brak lokalnej powłoki/checkoutu). Przed scaleniem wymagany pełny CI Quality Gate; poniższe kontrole strukturalne wykonano programowo na zawartości z GitHub.

## 2. Lekcje B-05–09 — odbiór oczami kursanta

W każdej z pięciu lekcji treść merytoryczna pozostaje bez zmian. Występowały dwa sąsiadujące nagłówki: „Scenariusze praktyczne” obejmował 4–5 krótkich przykładów do omówienia, a „Trzy scenariusze praktyczne do przejścia po pytaniach” prowadził do trzech pełnych rekordów z mapy scenariuszy. Mogło to sugerować, że wszystkie przykłady mają ten sam format.

Zmiany w każdej lekcji:
- B-05: nagłówek zmieniono na „Krótkie przykłady sytuacyjne”.
- B-06: nagłówek zmieniono na „Krótkie przykłady sytuacyjne”.
- B-07: nagłówek zmieniono na „Krótkie przykłady sytuacyjne”.
- B-08: nagłówek zmieniono na „Krótkie przykłady sytuacyjne”.
- B-09: nagłówek zmieniono na „Krótkie przykłady sytuacyjne”.

Pod tym nagłówkiem dodano jedno zdanie wyjaśniające, że przykłady są pomocnicze, a trzy pełne scenariusze znajdują się w mapie praktycznej i mają własne kroki, typowe błędy, podstawę ADR, kryteria oraz `question_ids`. Żadnego przykładu nie usunięto. W `podstawowy/praktyka/SCENARIUSZE.md` dodano tę samą informację, aby instruktor i kursant rozróżniali oba rodzaje materiału.

## 3. Kontrola wszystkich 39 scenariuszy

Sprawdzono automatycznie wszystkie 39 rekordów z `praktyka/scenariusze-13-dzialow.json`:
- 3 scenariusze dla każdego z 13 działów;
- każdy ma sytuację, co najmniej 3 kroki, typowe błędy, podstawę ADR, kryteria oceny i wniosek do zapamiętania;
- wszystkie `question_ids` istnieją w banku i należą do modułu scenariusza;
- brak brakujących ID, powiązań z innym działem i scenariuszy z mniej niż 3 krokami.

**Wynik kontroli strukturalnej: 0 usterek.** Przegląd nie dostarczył potwierdzonego powodu do zmiany treści prawnej scenariuszy; nie dopisywano wymogów na wyczucie.

## 4. Rotacyjna próba 60 wyjaśnień

### Ograniczenie doboru

Raporty 4x51–4x79 łącznie obejmują już 598 z 609 ID w próbach lub rejestrach prób. Pozostało **11 ID bez wcześniejszego wystąpienia w tych próbach**. Nie da się więc przygotować 60 całkowicie nowych ID. Zastosowano jawny podział:
- **11 nowych względem poprzednich prób:** ADR-B-0008, ADR-B-0031, ADR-B-0036, ADR-B-0042, ADR-B-0052, ADR-B-0053, ADR-B-0063, ADR-B-0120, ADR-B-0211, ADR-B-0519, ADR-B-0558.
- **49 pozycji kontrolnych w rotacji** (wcześniej próbkowane; nie są przedstawiane jako nowe): ADR-B-0327, ADR-B-0050, ADR-B-0164, ADR-B-0287, ADR-B-0140, ADR-B-0051, ADR-B-0412, ADR-B-0083, ADR-B-0043, ADR-B-0555, ADR-B-0290, ADR-B-0107, ADR-B-0307, ADR-B-0547, ADR-B-0215, ADR-B-0523, ADR-B-0210, ADR-B-0239, ADR-B-0038, ADR-B-0550, ADR-B-0468, ADR-B-0095, ADR-B-0214, ADR-B-0339, ADR-B-0174, ADR-B-0419, ADR-B-0458, ADR-B-0085, ADR-B-0424, ADR-B-0255, ADR-B-0288, ADR-B-0303, ADR-B-0017, ADR-B-0358, ADR-B-0355, ADR-B-0443, ADR-B-0112, ADR-B-0297, ADR-B-0048, ADR-B-0429, ADR-B-0168, ADR-B-0124, ADR-B-0142, ADR-B-0172, ADR-B-0285, ADR-B-0403, ADR-B-0467, ADR-B-0562, ADR-B-0149.
- Dla odtwarzalności losowania rotacyjnego użyto ziarna `2026102781`.

### Wynik ręcznego przeglądu

Przejrzano pytanie, A/B/C, klucz i explanation dla całej próby. Wszystkie wyjaśnienia mają co najmniej 300 znaków i zachowują prosty tok: sens poprawnej odpowiedzi, powód błędności pozostałych opcji oraz podstawę ADR.

Heurystyka skrótów wskazała 7 kandydatów:
- **Potwierdzone poprawki — 4:** ADR-B-0008, ADR-B-0037, ADR-B-0327 i ADR-B-0547. W pierwszym użyciu skrótu UN dodano objaśnienie „czterocyfrowy identyfikator towaru niebezpiecznego”. Nie zmieniono poprawnej litery ani opcji.
- **Fałszywe alarmy — 3:**
  - ADR-B-0142 — skrót IMDG jest wyjaśniony w pierwszym zdaniu jako kodeks morski.
  - ADR-B-0215 — numer UN jest objaśniony jako czterocyfrowy identyfikator towaru.
  - ADR-B-0467 — IMDG jest rozwinięty wprost w explanation.
  
Pozostałe 53 pozycje nie wykazały potwierdzonej potrzeby redakcji w ramach tego przeglądu. Brak flagi heurystycznej nie jest certyfikatem poprawności prawnej.

## 5. Metryki „poprawna = jedyna najdłuższa”

| Dział | Pytania | Poprawna jedyną najdłuższą | Odsetek |
|---|---:|---:|---:|
| B-01 | 45 | 6 | 13.33% |
| B-02 | 56 | 8 | 14.29% |
| B-03 | 49 | 7 | 14.29% |
| B-04 | 46 | 6 | 13.04% |
| B-05 | 43 | 5 | 11.63% |
| B-06 | 45 | 5 | 11.11% |
| B-07 | 48 | 6 | 12.50% |
| B-08 | 42 | 5 | 11.90% |
| B-09 | 46 | 4 | 8.70% |
| B-10 | 55 | 4 | 7.27% |
| B-11 | 43 | 6 | 13.95% |
| B-12 | 44 | 6 | 13.64% |
| B-13 | 47 | 5 | 10.64% |
| **Cały bank** | **609** | **73** | **11,99%** |

Wszystkie działy pozostają poniżej progu 18%. Minimum explanation po poprawkach: 300 znaków.

## 6. Pliki i zakres zmian

- `podstawowy/lekcje/ADR-B-05.md`–`ADR-B-09.md` — rozróżnienie przykładów sytuacyjnych od trzech pełnych scenariuszy.
- `podstawowy/praktyka/SCENARIUSZE.md` — doprecyzowanie ścieżki pracy z mapą scenariuszy.
- `podstawowy/questions.jsonl` — wyjaśnienia ADR-B-0008, ADR-B-0037, ADR-B-0327 i ADR-B-0547; bez zmian ID, opcji, kluczy i statusów.
- Scenariusze JSON nie wymagały zmian.
- Nie znaleziono potwierdzonej luki programu uzasadniającej nowe pytanie w tej partii.

## 7. Zastrzeżenie

To przegląd dydaktyczny i strukturalny, nie formalna recenzja prawna. Wszystkie pytania nadal wymagają niezależnego odbioru specjalisty ADR i zachowują `needs_review`.


## Naprawa Quality Gate — migawki po aktualizacji pytań

Po redakcji explanation cztery migawki techniczne pozostały nieaktualne, choć treść pytań była już poprawiona. Odświeżono wyłącznie snapshoty zgodnie z bieżącym `questions.jsonl`:
- `ADR-B-0008`: `review/sequential/001-030.json` i `review/legal-clauses/001-030.json`;
- `ADR-B-0037`: `review/sequential/031-060.json` i `review/legal-clauses/031-060.json`;
- `ADR-B-0327`: `review/sequential/325-344.json` i `review/legal-clauses/325-344.json`;
- `ADR-B-0547`: `review/sequential/546-560.json` i `review/legal-clauses/546-560.json`.

Migawki odzwierciedlają aktualne stem/options/klucz/explanation/źródła oraz status `needs_review`. Nie zmieniano poprawnych liter ani statusów weryfikacji, nie dopisano potwierdzenia zgodności prawnej. CI dla migawki końcowej `6a79da829043618b04444e3195c4b331a3d6382c` zakończyło się PASS (Quality Gate run `40475992925`); weryfikacja tekstu urzędowego i recenzja specjalisty pozostają otwarte.
