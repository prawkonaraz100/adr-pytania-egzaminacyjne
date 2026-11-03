# Etap 4x328 — szczególne znaczenie numeru zagrożenia 22

Data: 03.11.2026. Gałąź: `stage4x328-special-hazard-number-22`. Bazowy main: `bf17f37a40fe3f161b3502ffd5727cceef1115e5`.

## Zakres i wynik

Dodano ADR-B-0754 do kompetencji `ADR-B-06-K06` — powtórzone cyfry i szczególne kombinacje numerów zagrożenia. Pytanie dotyczy szczególnego znaczenia kodu 22, które ma pierwszeństwo przed odczytaniem go wyłącznie według ogólnej reguły o powtórzeniu cyfry. Podstawa: ADR 2025, 5.3.2.3.1–5.3.2.3.2.

- Bank: **754** pytania (ADR-B-0001–0754), 754 `needs_review`, 0 `verified`.
- SHA `a8e7354f8f27c9f69d0e2b61742f2ac9dea9244a`.
- Moduł ADR-B-06: **64** pytania; K06: 5→6.
- Kompetencje teorii z mniej niż 6 pytaniami: **26** (3 praktyczne pominięte).
- Rozkład kluczy A/B/C: **253/272/229**.
- „Poprawna odpowiedź jest jedyną najdłuższą”: **81/754 = 10,74%**; maksimum działu **14,61%**.
- Długości opcji A/B/C: **115/110/103**; poprawna B nie jest najdłuższa.
- Explanation: **323 znaki, 4 zdania**.

## Pytanie ADR-B-0754

W górnym polu tablicy pomarańczowej odczytujesz numer 22. Znasz zasadę, że powtórzona cyfra zwykle wzmacnia zagrożenie. Co musisz sprawdzić przed zastosowaniem tej zasady?

A. Odczytać go tylko jako podwójne nasilenie zagrożenia emisją gazu, bez dodatkowego znaczenia przypisanego kodowi 22.

B. Rozpoznać szczególny kod: gaz skroplony schłodzony o działaniu duszącym, zgodnie z tabelą znaczeń numerów ADR.

C. Uznać, że każda z dwóch cyfr opisuje osobne zagrożenie gazowe i sprawdzić je jako dwa niezależne wpisy.

Nie każdy numer z powtórzoną cyfrą odczytuje się wyłącznie według ogólnej zasady nasilenia. Kod 22 ma w ADR szczególne znaczenie: oznacza gaz skroplony schłodzony, działający dusząco. Odpowiedź A pomija wyjątek wpisany w tabeli, a C błędnie rozdziela cyfry na dwa osobne zagrożenia. Podstawa: ADR 2025, 5.3.2.3.1–5.3.2.3.2.

## Audyt A/B/C i źródła

- A — błędna: stosuje tylko regułę ogólną i pomija szczególne znaczenie numeru 22.
- B — poprawna: ADR 5.3.2.3.2 określa 22 jako gaz skroplony schłodzony, działający dusząco.
- C — błędna: dwie cyfry tworzą jeden numer rozpoznawczy, a nie dwa osobne wpisy zagrożeń.
- Podstawa prawna: Dz.U. 2025 poz. 642, ADR 2025, 5.3.2.3.1–5.3.2.3.2 — https://eli.gov.pl/api/acts/DU/2025/642/text.pdf.
- Dodatkowe porównanie treści ADR 2025, tom II, s. 257 — https://www.mindop.sk/fileadmin/documents/doprava/nebezpecnetovary/cesta/ADR_2025_Vol._II._EN.pdf.
- Pytanie pozostaje `needs_review`; pełne literalne porównanie polskiego tekstu i niezależna recenzja specjalisty są nadal wymagane. Nie oznaczono żadnego pytania jako `verified`.

## Synchronizacja artefaktów

Klucze i warianty egzaminów próbnych 001–005 wskazują SHA bieżącego banku. Snapshoty `review/sequential/754-754.json` i `review/legal-clauses/754-754.json` zawierają ADR-B-0754. Ledger prawny, manifesty pakietu i kolejki specjalisty mają zaktualizowane SHA oraz stan 754 pytań. Zaktualizowano coverage, README kursanta i specjalisty, lekcję B-06, rejestr specjalisty oraz testy liczebności.
