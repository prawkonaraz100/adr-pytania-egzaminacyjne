# Etap 4x63 — egzamin próbny i nowa próbka 60 wyjaśnień

**Data:** 2026-10-26. **Źródłowy main:** `216f7c46d4cb6c244ca4b1991a2be5522a378d5d`. Wyłącznie kurs podstawowy ADR; wszystkie pytania mają `needs_review`.

## 1. Wynik Quality Gate i stan banku

- Główny workflow `#40405030765` dla wskazanego main: **PASS**.
- Bank: **609 pytań**, ADR-B-0001…ADR-B-0609; **609 needs_review, 0 verified**.
- Poprawna odpowiedź jest jedyną najdłuższą: **72/609 = 11,82%**, poniżej progu 18%. Explanation: wszystkie co najmniej 300 znaków.
- Nie stwierdzono potwierdzonej luki wymagającej dodania ADR-B-0610; nie zmieniono banku ani odpowiedzi.

## 2. Egzamin próbny — rzeczywisty odczyt pięciu wariantów i kluczy

| Wariant | Liczba pytań | Działy | Rozkład A/B/C | Maksymalna seria tej samej poprawnej litery | Próg treningowy | Podobne pary (Jaccard tokenów ≥0,40) |
|---|---:|---:|---|---:|---|---:|
| 001 | 30 | 13 | 10/10/10 | 3 | 20/30 w 60 minut | 0 |
| 002 | 30 | 13 | 10/10/10 | 3 | 20/30 w 60 minut | 0 |
| 003 | 30 | 13 | 10/10/10 | 3 | 20/30 w 60 minut | 0 |
| 004 | 30 | 13 | 10/10/10 | 3 | 20/30 w 60 minut | 0 |
| 005 | 30 | 13 | 10/10/10 | 3 | 20/30 w 60 minut | 0 |

Każdy wariant ma **po 2–3 pytania z każdego z 13 działów**, zgodnie z aktualnym testem i względnie równym udziałem modułów. Zweryfikowano numery ID, zgodność liter w kluczach z tekstem poprawnej opcji, wymagane wyjaśnienia oraz `publication_authorized=false`. Próg 20/30 jest **progiem treningowym, nie oficjalnym potwierdzeniem kwalifikacji**; opis jest już w `podstawowy/egzamin-probny/README.md`.

Nie stwierdzono powtórzonych ID ani par nawet o podobieństwie ≥0,40 w tym samym arkuszu. **Nie regenerowano arkuszy bez potwierdzonego problemu**, aby zachować istniejące poprawne warianty i źródłowy hash banku.

Dla przyszłych regeneracji dodano blokującą regresję `near_duplicate_pairs` w `scripts/check_mock_exam_variants.py`: Jaccard tokenów ≥0,70 przy co najmniej pięciu wspólnych wyrazach. To sygnał potencjalnego powtórzenia, nie samodzielny dowód prawnej równoważności; każde trafienie wymaga sprawdzenia. Dodano test pozytywny i negatywny w `tests/test_mock_exam_variants.py`. Weryfikacja końcowa: pełny CI PR.

## 3. Losowa próba 60 explanation, bez powtórzeń z wcześniejszych raportów

- Seed: `2026102663`; deterministyczny generator LCG (`state = (1664525 × state + 1013904223) mod 2^32`), Fisher–Yates po rosnących ID.
- Wykluczono **410 unikalnych ID** wymienionych w raportach próbek i przeglądów 4x51–4x61 (lista plików poniżej); do losowania pozostało 199+ pytań (dokładnie 200).
- Każde wybrane explanation: **3–5 zdań, 302–424 znaki**, nie zaczyna się od numeru przepisu, nie ma zdania powyżej 35 słów i zawiera objaśnienie przyczyny odrzucenia błędnej opcji; podaje podstawę ADR.
- Po przeglądzie nie stwierdzono potwierdzonej potrzeby redakcji w wylosowanych 60. **0 pytań zmienionych**, aby nie wprowadzać zmian kosmetycznych bez uzasadnienia. Heurystyki wspierają odbiór, ale nie zastępują niezależnej recenzji specjalisty.

| Pytanie | Dział | Zdania | Znaki explanation | Decyzja |
|---|---|---:|---:|---|
| ADR-B-0260 | ADR-B-01 | 4 | 335 | Pozostawiono: objaśnia poprawną odpowiedź, typową pomyłkę i wskazuje ADR |
| ADR-B-0421 | ADR-B-08 | 4 | 344 | Pozostawiono: objaśnia poprawną odpowiedź, typową pomyłkę i wskazuje ADR |
| ADR-B-0196 | ADR-B-07 | 4 | 373 | Pozostawiono: objaśnia poprawną odpowiedź, typową pomyłkę i wskazuje ADR |
| ADR-B-0511 | ADR-B-10 | 4 | 407 | Pozostawiono: objaśnia poprawną odpowiedź, typową pomyłkę i wskazuje ADR |
| ADR-B-0029 | ADR-B-10 | 5 | 379 | Pozostawiono: objaśnia poprawną odpowiedź, typową pomyłkę i wskazuje ADR |
| ADR-B-0007 | ADR-B-03 | 4 | 327 | Pozostawiono: objaśnia poprawną odpowiedź, typową pomyłkę i wskazuje ADR |
| ADR-B-0189 | ADR-B-06 | 4 | 390 | Pozostawiono: objaśnia poprawną odpowiedź, typową pomyłkę i wskazuje ADR |
| ADR-B-0181 | ADR-B-04 | 4 | 342 | Pozostawiono: objaśnia poprawną odpowiedź, typową pomyłkę i wskazuje ADR |
| ADR-B-0452 | ADR-B-10 | 4 | 316 | Pozostawiono: objaśnia poprawną odpowiedź, typową pomyłkę i wskazuje ADR |
| ADR-B-0281 | ADR-B-06 | 4 | 360 | Pozostawiono: objaśnia poprawną odpowiedź, typową pomyłkę i wskazuje ADR |
| ADR-B-0545 | ADR-B-06 | 4 | 382 | Pozostawiono: objaśnia poprawną odpowiedź, typową pomyłkę i wskazuje ADR |
| ADR-B-0341 | ADR-B-03 | 4 | 379 | Pozostawiono: objaśnia poprawną odpowiedź, typową pomyłkę i wskazuje ADR |
| ADR-B-0543 | ADR-B-06 | 4 | 321 | Pozostawiono: objaśnia poprawną odpowiedź, typową pomyłkę i wskazuje ADR |
| ADR-B-0246 | ADR-B-07 | 4 | 312 | Pozostawiono: objaśnia poprawną odpowiedź, typową pomyłkę i wskazuje ADR |
| ADR-B-0596 | ADR-B-08 | 4 | 335 | Pozostawiono: objaśnia poprawną odpowiedź, typową pomyłkę i wskazuje ADR |
| ADR-B-0338 | ADR-B-03 | 4 | 328 | Pozostawiono: objaśnia poprawną odpowiedź, typową pomyłkę i wskazuje ADR |
| ADR-B-0199 | ADR-B-09 | 4 | 302 | Pozostawiono: objaśnia poprawną odpowiedź, typową pomyłkę i wskazuje ADR |
| ADR-B-0057 | ADR-B-08 | 4 | 330 | Pozostawiono: objaśnia poprawną odpowiedź, typową pomyłkę i wskazuje ADR |
| ADR-B-0479 | ADR-B-07 | 4 | 373 | Pozostawiono: objaśnia poprawną odpowiedź, typową pomyłkę i wskazuje ADR |
| ADR-B-0136 | ADR-B-07 | 4 | 326 | Pozostawiono: objaśnia poprawną odpowiedź, typową pomyłkę i wskazuje ADR |
| ADR-B-0568 | ADR-B-07 | 3 | 335 | Pozostawiono: objaśnia poprawną odpowiedź, typową pomyłkę i wskazuje ADR |
| ADR-B-0191 | ADR-B-06 | 4 | 345 | Pozostawiono: objaśnia poprawną odpowiedź, typową pomyłkę i wskazuje ADR |
| ADR-B-0480 | ADR-B-07 | 4 | 318 | Pozostawiono: objaśnia poprawną odpowiedź, typową pomyłkę i wskazuje ADR |
| ADR-B-0404 | ADR-B-12 | 4 | 316 | Pozostawiono: objaśnia poprawną odpowiedź, typową pomyłkę i wskazuje ADR |
| ADR-B-0423 | ADR-B-08 | 4 | 322 | Pozostawiono: objaśnia poprawną odpowiedź, typową pomyłkę i wskazuje ADR |
| ADR-B-0350 | ADR-B-04 | 4 | 365 | Pozostawiono: objaśnia poprawną odpowiedź, typową pomyłkę i wskazuje ADR |
| ADR-B-0127 | ADR-B-02 | 4 | 322 | Pozostawiono: objaśnia poprawną odpowiedź, typową pomyłkę i wskazuje ADR |
| ADR-B-0491 | ADR-B-09 | 4 | 322 | Pozostawiono: objaśnia poprawną odpowiedź, typową pomyłkę i wskazuje ADR |
| ADR-B-0379 | ADR-B-07 | 4 | 351 | Pozostawiono: objaśnia poprawną odpowiedź, typową pomyłkę i wskazuje ADR |
| ADR-B-0236 | ADR-B-09 | 4 | 338 | Pozostawiono: objaśnia poprawną odpowiedź, typową pomyłkę i wskazuje ADR |
| ADR-B-0566 | ADR-B-08 | 4 | 344 | Pozostawiono: objaśnia poprawną odpowiedź, typową pomyłkę i wskazuje ADR |
| ADR-B-0541 | ADR-B-02 | 4 | 319 | Pozostawiono: objaśnia poprawną odpowiedź, typową pomyłkę i wskazuje ADR |
| ADR-B-0231 | ADR-B-05 | 4 | 331 | Pozostawiono: objaśnia poprawną odpowiedź, typową pomyłkę i wskazuje ADR |
| ADR-B-0171 | ADR-B-08 | 4 | 351 | Pozostawiono: objaśnia poprawną odpowiedź, typową pomyłkę i wskazuje ADR |
| ADR-B-0347 | ADR-B-04 | 4 | 424 | Pozostawiono: objaśnia poprawną odpowiedź, typową pomyłkę i wskazuje ADR |
| ADR-B-0509 | ADR-B-08 | 4 | 330 | Pozostawiono: objaśnia poprawną odpowiedź, typową pomyłkę i wskazuje ADR |
| ADR-B-0128 | ADR-B-02 | 4 | 314 | Pozostawiono: objaśnia poprawną odpowiedź, typową pomyłkę i wskazuje ADR |
| ADR-B-0310 | ADR-B-04 | 4 | 333 | Pozostawiono: objaśnia poprawną odpowiedź, typową pomyłkę i wskazuje ADR |
| ADR-B-0342 | ADR-B-03 | 4 | 326 | Pozostawiono: objaśnia poprawną odpowiedź, typową pomyłkę i wskazuje ADR |
| ADR-B-0456 | ADR-B-12 | 4 | 397 | Pozostawiono: objaśnia poprawną odpowiedź, typową pomyłkę i wskazuje ADR |
| ADR-B-0398 | ADR-B-10 | 4 | 382 | Pozostawiono: objaśnia poprawną odpowiedź, typową pomyłkę i wskazuje ADR |
| ADR-B-0581 | ADR-B-04 | 4 | 309 | Pozostawiono: objaśnia poprawną odpowiedź, typową pomyłkę i wskazuje ADR |
| ADR-B-0049 | ADR-B-05 | 4 | 307 | Pozostawiono: objaśnia poprawną odpowiedź, typową pomyłkę i wskazuje ADR |
| ADR-B-0469 | ADR-B-03 | 4 | 342 | Pozostawiono: objaśnia poprawną odpowiedź, typową pomyłkę i wskazuje ADR |
| ADR-B-0225 | ADR-B-05 | 4 | 325 | Pozostawiono: objaśnia poprawną odpowiedź, typową pomyłkę i wskazuje ADR |
| ADR-B-0241 | ADR-B-03 | 4 | 364 | Pozostawiono: objaśnia poprawną odpowiedź, typową pomyłkę i wskazuje ADR |
| ADR-B-0525 | ADR-B-13 | 4 | 347 | Pozostawiono: objaśnia poprawną odpowiedź, typową pomyłkę i wskazuje ADR |
| ADR-B-0047 | ADR-B-04 | 4 | 343 | Pozostawiono: objaśnia poprawną odpowiedź, typową pomyłkę i wskazuje ADR |
| ADR-B-0595 | ADR-B-01 | 4 | 335 | Pozostawiono: objaśnia poprawną odpowiedź, typową pomyłkę i wskazuje ADR |
| ADR-B-0154 | ADR-B-02 | 4 | 353 | Pozostawiono: objaśnia poprawną odpowiedź, typową pomyłkę i wskazuje ADR |
| ADR-B-0054 | ADR-B-07 | 4 | 361 | Pozostawiono: objaśnia poprawną odpowiedź, typową pomyłkę i wskazuje ADR |
| ADR-B-0528 | ADR-B-01 | 3 | 353 | Pozostawiono: objaśnia poprawną odpowiedź, typową pomyłkę i wskazuje ADR |
| ADR-B-0573 | ADR-B-01 | 4 | 316 | Pozostawiono: objaśnia poprawną odpowiedź, typową pomyłkę i wskazuje ADR |
| ADR-B-0336 | ADR-B-03 | 4 | 337 | Pozostawiono: objaśnia poprawną odpowiedź, typową pomyłkę i wskazuje ADR |
| ADR-B-0537 | ADR-B-13 | 4 | 367 | Pozostawiono: objaśnia poprawną odpowiedź, typową pomyłkę i wskazuje ADR |
| ADR-B-0291 | ADR-B-09 | 4 | 325 | Pozostawiono: objaśnia poprawną odpowiedź, typową pomyłkę i wskazuje ADR |
| ADR-B-0580 | ADR-B-04 | 4 | 322 | Pozostawiono: objaśnia poprawną odpowiedź, typową pomyłkę i wskazuje ADR |
| ADR-B-0232 | ADR-B-05 | 4 | 405 | Pozostawiono: objaśnia poprawną odpowiedź, typową pomyłkę i wskazuje ADR |
| ADR-B-0090 | ADR-B-13 | 4 | 308 | Pozostawiono: objaśnia poprawną odpowiedź, typową pomyłkę i wskazuje ADR |
| ADR-B-0202 | ADR-B-09 | 4 | 326 | Pozostawiono: objaśnia poprawną odpowiedź, typową pomyłkę i wskazuje ADR |

**Źródła wykluczeń:** `podstawowy/raporty/etap-4x51-proba60-scenariusze-2026-10-26.md`, `podstawowy/raporty/etap-4x52-proba60-czytelnosc-2026-10-26.md`, `podstawowy/raporty/etap-4x56-proba60-false-alarms-2026-10-26.md`, `podstawowy/raporty/etap-4x57-proba60-lekcje-2026-10-26.md`, `podstawowy/raporty/etap-4x58-pozostale49-explanation-2026-10-26.md`, `podstawowy/raporty/etap-4x59-proba60-explanation-2026-10-26.md`, `podstawowy/raporty/etap-4x61-proba60-i-lekcje-01-04-2026-10-26.md`.

## 4. Pakiet recenzyjny i dalsza kontrola

Aktualny manifest `review/specialist/PAKIET-0609-MANIFEST.json` zawiera 609 pytań, 39 scenariuszy, 13 lekcji, 13 materiałów instruktorskich i 5 wariantów/kluczy. Żadne pytanie nie uzyskało statusu `verified`. Niniejszy raport przekazuje wynik nowej próby i kontroli arkuszy; nie stanowi formalnego zatwierdzenia treści prawnej ani egzaminu. W następnym kroku zaleca się przegląd redakcyjnej użyteczności rzeczywistych przykładów w podręczniku, bez rozpoczynania innej specjalizacji.
