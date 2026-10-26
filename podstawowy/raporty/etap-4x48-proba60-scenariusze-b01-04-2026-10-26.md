# Etap 4x48 — próbka 60 explanation i scenariusze B-01–04

- Data: 2026-10-26.
- Punkt bazowy świeżego `main`: `b7ae7e9c2a96450089248c9edf58424801238301`.
- Seed próbki: `2026102648`; PRNG LCG `state = (1664525 * state + 1013904223) mod 2^32`, Fisher–Yates.
- Wykluczono próbkę 40 pytań z 4x45, próbkę 60 z 4x46 i 13 sygnałów redakcyjnych z 4x47. Próbka 4x48 obejmuje 60 unikalnych ID.
- Zakres: wyłącznie kurs podstawowy ADR.

## 1. Odbiór 60 wyjaśnień „oczami kursanta”

Każde explanation przeczytano razem z pytaniem, trzema odpowiedziami i podstawą ADR. Oceniono, czy początek wyjaśnia sens poprawnej odpowiedzi, czy błędne alternatywy są obalone, czy skróty są objaśnione i czy podano podstawę.

**Wynik: 60/60 pozostawiono bez zmian; 0 przepisano.** Nie znaleziono potwierdzonego problemu dydaktycznego uzasadniającego zmianę. Wszystkie 60 mają co najmniej 300 znaków, 3–5 zdań i podstawę ADR. To ocena redakcyjna, nie formalne zatwierdzenie prawne.

### Lista ID i decyzja

| ID | Wynik | Uzasadnienie redakcyjne |
|---|---|---|
| ADR-B-0444 | Bez zmiany | Wyjaśnia sens poprawnej odpowiedzi, odnosi się do kuszących błędnych opcji i podaje podstawę ADR; brak potwierdzonej niejasności. |
| ADR-B-0472 | Bez zmiany | Wyjaśnia sens poprawnej odpowiedzi, odnosi się do kuszących błędnych opcji i podaje podstawę ADR; brak potwierdzonej niejasności. |
| ADR-B-0011 | Bez zmiany | Wyjaśnia sens poprawnej odpowiedzi, odnosi się do kuszących błędnych opcji i podaje podstawę ADR; brak potwierdzonej niejasności. |
| ADR-B-0457 | Bez zmiany | Wyjaśnia sens poprawnej odpowiedzi, odnosi się do kuszących błędnych opcji i podaje podstawę ADR; brak potwierdzonej niejasności. |
| ADR-B-0399 | Bez zmiany | Wyjaśnia sens poprawnej odpowiedzi, odnosi się do kuszących błędnych opcji i podaje podstawę ADR; brak potwierdzonej niejasności. |
| ADR-B-0216 | Bez zmiany | Wyjaśnia sens poprawnej odpowiedzi, odnosi się do kuszących błędnych opcji i podaje podstawę ADR; brak potwierdzonej niejasności. |
| ADR-B-0005 | Bez zmiany | Wyjaśnia sens poprawnej odpowiedzi, odnosi się do kuszących błędnych opcji i podaje podstawę ADR; brak potwierdzonej niejasności. |
| ADR-B-0569 | Bez zmiany | Wyjaśnia sens poprawnej odpowiedzi, odnosi się do kuszących błędnych opcji i podaje podstawę ADR; brak potwierdzonej niejasności. |
| ADR-B-0165 | Bez zmiany | Wyjaśnia sens poprawnej odpowiedzi, odnosi się do kuszących błędnych opcji i podaje podstawę ADR; brak potwierdzonej niejasności. |
| ADR-B-0296 | Bez zmiany | Wyjaśnia sens poprawnej odpowiedzi, odnosi się do kuszących błędnych opcji i podaje podstawę ADR; brak potwierdzonej niejasności. |
| ADR-B-0387 | Bez zmiany | Wyjaśnia sens poprawnej odpowiedzi, odnosi się do kuszących błędnych opcji i podaje podstawę ADR; brak potwierdzonej niejasności. |
| ADR-B-0127 | Bez zmiany | Wyjaśnia sens poprawnej odpowiedzi, odnosi się do kuszących błędnych opcji i podaje podstawę ADR; brak potwierdzonej niejasności. |
| ADR-B-0265 | Bez zmiany | Wyjaśnia sens poprawnej odpowiedzi, odnosi się do kuszących błędnych opcji i podaje podstawę ADR; brak potwierdzonej niejasności. |
| ADR-B-0546 | Bez zmiany | Wyjaśnia sens poprawnej odpowiedzi, odnosi się do kuszących błędnych opcji i podaje podstawę ADR; brak potwierdzonej niejasności. |
| ADR-B-0035 | Bez zmiany | Wyjaśnia sens poprawnej odpowiedzi, odnosi się do kuszących błędnych opcji i podaje podstawę ADR; brak potwierdzonej niejasności. |
| ADR-B-0044 | Bez zmiany | Wyjaśnia sens poprawnej odpowiedzi, odnosi się do kuszących błędnych opcji i podaje podstawę ADR; brak potwierdzonej niejasności. |
| ADR-B-0001 | Bez zmiany | Wyjaśnia sens poprawnej odpowiedzi, odnosi się do kuszących błędnych opcji i podaje podstawę ADR; brak potwierdzonej niejasności. |
| ADR-B-0512 | Bez zmiany | Wyjaśnia sens poprawnej odpowiedzi, odnosi się do kuszących błędnych opcji i podaje podstawę ADR; brak potwierdzonej niejasności. |
| ADR-B-0329 | Bez zmiany | Wyjaśnia sens poprawnej odpowiedzi, odnosi się do kuszących błędnych opcji i podaje podstawę ADR; brak potwierdzonej niejasności. |
| ADR-B-0133 | Bez zmiany | Wyjaśnia sens poprawnej odpowiedzi, odnosi się do kuszących błędnych opcji i podaje podstawę ADR; brak potwierdzonej niejasności. |
| ADR-B-0028 | Bez zmiany | Wyjaśnia sens poprawnej odpowiedzi, odnosi się do kuszących błędnych opcji i podaje podstawę ADR; brak potwierdzonej niejasności. |
| ADR-B-0438 | Bez zmiany | Wyjaśnia sens poprawnej odpowiedzi, odnosi się do kuszących błędnych opcji i podaje podstawę ADR; brak potwierdzonej niejasności. |
| ADR-B-0393 | Bez zmiany | Wyjaśnia sens poprawnej odpowiedzi, odnosi się do kuszących błędnych opcji i podaje podstawę ADR; brak potwierdzonej niejasności. |
| ADR-B-0603 | Bez zmiany | Wyjaśnia sens poprawnej odpowiedzi, odnosi się do kuszących błędnych opcji i podaje podstawę ADR; brak potwierdzonej niejasności. |
| ADR-B-0209 | Bez zmiany | Wyjaśnia sens poprawnej odpowiedzi, odnosi się do kuszących błędnych opcji i podaje podstawę ADR; brak potwierdzonej niejasności. |
| ADR-B-0536 | Bez zmiany | Wyjaśnia sens poprawnej odpowiedzi, odnosi się do kuszących błędnych opcji i podaje podstawę ADR; brak potwierdzonej niejasności. |
| ADR-B-0286 | Bez zmiany | Wyjaśnia sens poprawnej odpowiedzi, odnosi się do kuszących błędnych opcji i podaje podstawę ADR; brak potwierdzonej niejasności. |
| ADR-B-0111 | Bez zmiany | Wyjaśnia sens poprawnej odpowiedzi, odnosi się do kuszących błędnych opcji i podaje podstawę ADR; brak potwierdzonej niejasności. |
| ADR-B-0305 | Bez zmiany | Wyjaśnia sens poprawnej odpowiedzi, odnosi się do kuszących błędnych opcji i podaje podstawę ADR; brak potwierdzonej niejasności. |
| ADR-B-0071 | Bez zmiany | Wyjaśnia sens poprawnej odpowiedzi, odnosi się do kuszących błędnych opcji i podaje podstawę ADR; brak potwierdzonej niejasności. |
| ADR-B-0176 | Bez zmiany | Wyjaśnia sens poprawnej odpowiedzi, odnosi się do kuszących błędnych opcji i podaje podstawę ADR; brak potwierdzonej niejasności. |
| ADR-B-0453 | Bez zmiany | Wyjaśnia sens poprawnej odpowiedzi, odnosi się do kuszących błędnych opcji i podaje podstawę ADR; brak potwierdzonej niejasności. |
| ADR-B-0425 | Bez zmiany | Wyjaśnia sens poprawnej odpowiedzi, odnosi się do kuszących błędnych opcji i podaje podstawę ADR; brak potwierdzonej niejasności. |
| ADR-B-0498 | Bez zmiany | Wyjaśnia sens poprawnej odpowiedzi, odnosi się do kuszących błędnych opcji i podaje podstawę ADR; brak potwierdzonej niejasności. |
| ADR-B-0301 | Bez zmiany | Wyjaśnia sens poprawnej odpowiedzi, odnosi się do kuszących błędnych opcji i podaje podstawę ADR; brak potwierdzonej niejasności. |
| ADR-B-0496 | Bez zmiany | Wyjaśnia sens poprawnej odpowiedzi, odnosi się do kuszących błędnych opcji i podaje podstawę ADR; brak potwierdzonej niejasności. |
| ADR-B-0072 | Bez zmiany | Wyjaśnia sens poprawnej odpowiedzi, odnosi się do kuszących błędnych opcji i podaje podstawę ADR; brak potwierdzonej niejasności. |
| ADR-B-0411 | Bez zmiany | Wyjaśnia sens poprawnej odpowiedzi, odnosi się do kuszących błędnych opcji i podaje podstawę ADR; brak potwierdzonej niejasności. |
| ADR-B-0049 | Bez zmiany | Wyjaśnia sens poprawnej odpowiedzi, odnosi się do kuszących błędnych opcji i podaje podstawę ADR; brak potwierdzonej niejasności. |
| ADR-B-0260 | Bez zmiany | Wyjaśnia sens poprawnej odpowiedzi, odnosi się do kuszących błędnych opcji i podaje podstawę ADR; brak potwierdzonej niejasności. |
| ADR-B-0042 | Bez zmiany | Wyjaśnia sens poprawnej odpowiedzi, odnosi się do kuszących błędnych opcji i podaje podstawę ADR; brak potwierdzonej niejasności. |
| ADR-B-0116 | Bez zmiany | Wyjaśnia sens poprawnej odpowiedzi, odnosi się do kuszących błędnych opcji i podaje podstawę ADR; brak potwierdzonej niejasności. |
| ADR-B-0031 | Bez zmiany | Wyjaśnia sens poprawnej odpowiedzi, odnosi się do kuszących błędnych opcji i podaje podstawę ADR; brak potwierdzonej niejasności. |
| ADR-B-0066 | Bez zmiany | Wyjaśnia sens poprawnej odpowiedzi, odnosi się do kuszących błędnych opcji i podaje podstawę ADR; brak potwierdzonej niejasności. |
| ADR-B-0323 | Bez zmiany | Wyjaśnia sens poprawnej odpowiedzi, odnosi się do kuszących błędnych opcji i podaje podstawę ADR; brak potwierdzonej niejasności. |
| ADR-B-0522 | Bez zmiany | Wyjaśnia sens poprawnej odpowiedzi, odnosi się do kuszących błędnych opcji i podaje podstawę ADR; brak potwierdzonej niejasności. |
| ADR-B-0191 | Bez zmiany | Wyjaśnia sens poprawnej odpowiedzi, odnosi się do kuszących błędnych opcji i podaje podstawę ADR; brak potwierdzonej niejasności. |
| ADR-B-0427 | Bez zmiany | Wyjaśnia sens poprawnej odpowiedzi, odnosi się do kuszących błędnych opcji i podaje podstawę ADR; brak potwierdzonej niejasności. |
| ADR-B-0556 | Bez zmiany | Wyjaśnia sens poprawnej odpowiedzi, odnosi się do kuszących błędnych opcji i podaje podstawę ADR; brak potwierdzonej niejasności. |
| ADR-B-0189 | Bez zmiany | Wyjaśnia sens poprawnej odpowiedzi, odnosi się do kuszących błędnych opcji i podaje podstawę ADR; brak potwierdzonej niejasności. |
| ADR-B-0560 | Bez zmiany | Wyjaśnia sens poprawnej odpowiedzi, odnosi się do kuszących błędnych opcji i podaje podstawę ADR; brak potwierdzonej niejasności. |
| ADR-B-0098 | Bez zmiany | Wyjaśnia sens poprawnej odpowiedzi, odnosi się do kuszących błędnych opcji i podaje podstawę ADR; brak potwierdzonej niejasności. |
| ADR-B-0599 | Bez zmiany | Wyjaśnia sens poprawnej odpowiedzi, odnosi się do kuszących błędnych opcji i podaje podstawę ADR; brak potwierdzonej niejasności. |
| ADR-B-0338 | Bez zmiany | Wyjaśnia sens poprawnej odpowiedzi, odnosi się do kuszących błędnych opcji i podaje podstawę ADR; brak potwierdzonej niejasności. |
| ADR-B-0110 | Bez zmiany | Wyjaśnia sens poprawnej odpowiedzi, odnosi się do kuszących błędnych opcji i podaje podstawę ADR; brak potwierdzonej niejasności. |
| ADR-B-0264 | Bez zmiany | Wyjaśnia sens poprawnej odpowiedzi, odnosi się do kuszących błędnych opcji i podaje podstawę ADR; brak potwierdzonej niejasności. |
| ADR-B-0518 | Bez zmiany | Wyjaśnia sens poprawnej odpowiedzi, odnosi się do kuszących błędnych opcji i podaje podstawę ADR; brak potwierdzonej niejasności. |
| ADR-B-0558 | Bez zmiany | Wyjaśnia sens poprawnej odpowiedzi, odnosi się do kuszących błędnych opcji i podaje podstawę ADR; brak potwierdzonej niejasności. |
| ADR-B-0436 | Bez zmiany | Wyjaśnia sens poprawnej odpowiedzi, odnosi się do kuszących błędnych opcji i podaje podstawę ADR; brak potwierdzonej niejasności. |
| ADR-B-0311 | Bez zmiany | Wyjaśnia sens poprawnej odpowiedzi, odnosi się do kuszących błędnych opcji i podaje podstawę ADR; brak potwierdzonej niejasności. |

## 2. Scenariusze praktyczne — B-01–04

Każdy z czterech działów ma trzy scenariusze. Główna luka strukturalna: listy `question_ids` były zbyt długie (np. 13 pytań w SC-ADR-B-01), przez co ćwiczenie traciło konkretny cel. Każdy z 12 scenariuszy B-01–04 ma teraz 1–3 pytania dopasowane do sytuacji. Nie zmieniano pytań, odpowiedzi ani kluczy.

| Scenariusz | Pytania po zmianie |
|---|---|
| SC-ADR-B-01 | ADR-B-0605, ADR-B-0606, ADR-B-0608 |
| SC-ADR-B-02 | ADR-B-0006, ADR-B-0510 |
| SC-ADR-B-03 | ADR-B-0009, ADR-B-0514 |
| SC-ADR-B-04 | ADR-B-0010, ADR-B-0581, ADR-B-0310 |
| SC-ADR-B-01-02 | ADR-B-0002, ADR-B-0259, ADR-B-0570 |
| SC-ADR-B-01-03 | ADR-B-0002, ADR-B-0573, ADR-B-0608 |
| SC-ADR-B-02-02 | ADR-B-0005, ADR-B-0006, ADR-B-0510 |
| SC-ADR-B-02-03 | ADR-B-0004, ADR-B-0005, ADR-B-0006 |
| SC-ADR-B-03-02 | ADR-B-0009, ADR-B-0514 |
| SC-ADR-B-03-03 | ADR-B-0009, ADR-B-0514 |
| SC-ADR-B-04-02 | ADR-B-0010, ADR-B-0012, ADR-B-0580 |
| SC-ADR-B-04-03 | ADR-B-0310, ADR-B-0347, ADR-B-0581 |

Walidacja referencji: 12/12 scenariuszy; brakujące ID: 0; ID z innego modułu: 0.

## 3. Preflight

- Bank: 609 pytań; unikalne ID: 609; duplikaty ID: 0.
- Statusy prawne bez zmian: wszystkie `needs_review`, 0 `verified`.
- Explanation banku, odpowiedzi i poprawne litery bez zmian w tej partii.
- Testy repozytorium wymagają wykonania w CI PR; nie deklaruję lokalnego PASS.

## Ograniczenia i dalszy krok

Przegląd explanation jest redakcyjny i nie zastępuje niezależnej recenzji ADR 2025 oraz polskiego tekstu urzędowego. Następna partia obejmie scenariusze B-05–08, potem B-09–13. Nie rozpoczęto kursu cystern ani innego kursu.
