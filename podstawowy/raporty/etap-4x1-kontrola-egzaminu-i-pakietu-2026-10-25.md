# Etap 4x1 — końcowa kontrola egzaminu próbnego i pakietu recenzyjnego

- Data: 25.10.2026.
- Świeży `main` przed kontrolą: `a4b629756ae85943957248f08d43004d3a5a4b21`.
- Zakres: kurs podstawowy ADR; kontrola spójności, nie zatwierdzenie prawne.

## 1. Egzamin próbny — warianty 001–003

Wszystkie trzy arkusze i klucze porównano rekord po rekordzie z bankiem.

| Kontrola | Wynik |
|---|---|
| Liczba pytań w każdym wariancie | 30 |
| Duplikaty ID w wariancie | 0 |
| Brakujące ID w banku | 0 |
| Zgodność treści pytania, działu i opcji A/B/C z bankiem | 0 rozbieżności |
| Zgodność kolejności arkusza i klucza | 3/3 warianty |
| Zgodność klucza i wyjaśnienia z bankiem | 0 rozbieżności |
| Pokrycie działów | Każdy wariant obejmuje wszystkie 13 działów |
| Nakładanie ID między wariantami | 0 dla każdej pary |
| Publikacja/formalny egzamin | Zablokowane; `publication_authorized: false` |

Warianty wskazują źródłowy commit `e1eb80d9db9bb5f475bb655fc08b47b7a866bb64`. Sprawdzono, że zawartość `podstawowy/questions.jsonl` na tym commicie jest identyczna z bankiem na `main` (blob SHA `2e6e9665e25c361ee584ff8ad43f8c4b37154f8f`). Warianty są deterministycznymi zestawami treningowymi, nie oficjalnymi arkuszami.

## 2. Pakiet recenzyjny

- Bank: 609 pytań i 609 unikalnych ID, od ADR-B-0001 do ADR-B-0609.
- Bieżący indeks specjalisty: 609 wierszy, bez brakujących ID.
- Ledger kontroli prawnej: 609 wpisów, 609 unikalnych ID, 0 wpisów spoza banku.
- Snapshoty audytu sekwencyjnego dla ADR-B-0598–0609: 12/12 zgodnych z aktualnym bankiem.
- Snapshoty audytu A/B/C dla ADR-B-0598–0609: 12/12 zgodnych z aktualnym bankiem.
- Manifest pakietu: 609 pytań, 609 `needs_review`, 0 `verified`, 0 formalnych akceptacji.
- Pole manifestu `unresolved_literal_comparisons = 599` liczy rekordy, dla których pełny polski fragment nie został pobrany i porównany literalnie. Dodatkowe 10 rekordów ma sprawdzone źródło pomocnicze, ale ich pełne literalne porównanie również pozostaje otwarte. **Łącznie wszystkie 609 rekordów nadal oczekują pełnego literalnego porównania i niezależnej akceptacji.** Licznik manifestu zachowuje definicję sprawdzaną przez Quality Gate.

## 3. Quality Gate i metryki banku

- 609 pytań, bez duplikatów ID.
- Poprawna odpowiedź jest jedyną najdłuższą w **86/609 = 14,12%**; limit 18%.
- Najkrótsze explanation: **300 znaków**; wyjaśnienia poniżej 200 znaków: **0**.
- Wszystkie 13 działów pozostają poniżej limitu 18%.
- Wszystkie pytania nadal `needs_review`; nie nadano żadnego statusu `verified`.

## 4. Status odbioru 13 lekcji

Etap 4x1 obejmował wszystkie lekcje B-01–B-13 w trzech scalonych partiach: [PR #301](https://github.com/prawkonaraz100/adr-pytania-egzaminacyjne/pull/301), [PR #302](https://github.com/prawkonaraz100/adr-pytania-egzaminacyjne/pull/302) i [PR #303](https://github.com/prawkonaraz100/adr-pytania-egzaminacyjne/pull/303). Raporty dydaktyczne dla zakresów 01–04, 05–08 i 09–13 są w katalogu `podstawowy/raporty`.

## 5. Ograniczenia i następny krok

Ta kontrola potwierdza spójność danych arkuszy/kluczy, ID, rozkładu działów, metryk i struktury pakietu. Nie potwierdza poprawności prawnej każdego pytania ani nie zastępuje niezależnej recenzji specjalisty. Pełne literalne porównanie polskiego ADR 2025 i sprostowania pozostaje otwarte dla wszystkich 609 rekordów; formalny release jest niedozwolony. Nie przechodzono do kursu cystern ani innych kursów.
