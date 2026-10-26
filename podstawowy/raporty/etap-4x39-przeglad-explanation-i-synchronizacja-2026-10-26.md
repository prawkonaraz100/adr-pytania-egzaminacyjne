# Etap 4x39 — przegląd explanation po etapach 4x30–4x38 i synchronizacja materiałów

- Data: 2026-10-26.
- Świeży `main` na starcie: `cb91b0e1c63bf31c148db6bf7c75da6cdde0ef10` (PR #481 scalony).
- Zakres: wyłącznie kurs podstawowy ADR; bank nie był zmieniany w tej partii.

## 1. Przegląd wyjaśnień dla kursanta

Ręcznie przeczytano **50 explanation**: 26 pytań zmienionych w etapach 4x30–4x38 oraz 24 rekordy ADR-B-0586–0609.

- Długość: 304–490 znaków.
- Explanation poniżej 200 znaków: 0.
- Explanation powyżej 500 znaków: 0.
- Poza zakresem 2–5 zdań: 0.
- Zdania dłuższe niż 35 słów: 0.
- Potwierdzone wyjaśnienia wymagające przepisania: **0**. Nie zmieniano treści merytorycznej bez potwierdzonego błędu.
- Jeden alarm heurystyki — **ADR-B-0479** — uznano za fałszywy: wyjaśnienie zaczyna się od zdania „ADR pozwala…”, czyli od nazwy przepisów jako podmiotu zdania, a nie od numeru przepisu ani suchego cytatu. Dalej prostym językiem wyjaśnia zakres obowiązku załadowcy i dlaczego komplet dokumentów nie uchyla zakazu wspólnego załadunku. Bez zmian.

### Lista sprawdzonych ID

- ADR-B-0048
- ADR-B-0078
- ADR-B-0079
- ADR-B-0127
- ADR-B-0148
- ADR-B-0184
- ADR-B-0213
- ADR-B-0223
- ADR-B-0226
- ADR-B-0228
- ADR-B-0238
- ADR-B-0248
- ADR-B-0266
- ADR-B-0313
- ADR-B-0317
- ADR-B-0318
- ADR-B-0334
- ADR-B-0353
- ADR-B-0379
- ADR-B-0398
- ADR-B-0431
- ADR-B-0479
- ADR-B-0531
- ADR-B-0540
- ADR-B-0552
- ADR-B-0565
- ADR-B-0586
- ADR-B-0587
- ADR-B-0588
- ADR-B-0589
- ADR-B-0590
- ADR-B-0591
- ADR-B-0592
- ADR-B-0593
- ADR-B-0594
- ADR-B-0595
- ADR-B-0596
- ADR-B-0597
- ADR-B-0598
- ADR-B-0599
- ADR-B-0600
- ADR-B-0601
- ADR-B-0602
- ADR-B-0603
- ADR-B-0604
- ADR-B-0605
- ADR-B-0606
- ADR-B-0607
- ADR-B-0608
- ADR-B-0609

## 2. Spójność lekcji z bankiem i egzaminami

- Sprawdzono odwołania do wszystkich 26 pytań zmienionych w etapach 4x30–4x38: każde ID występuje w lekcji właściwego działu.
- Wszystkie rekordy ADR-B-0586–0609 są ujęte w wykazach pytań lekcji właściwych działów: B-13 0586–0590 i 0598–0601; B-11 0591–0592 i 0602–0604; B-05 0593–0594; B-01 0595 i 0605–0609; B-08 0596–0597.
- Warianty i klucze 001–005 wskazują bieżący bank blob SHA `8a16afb47c5d5a9e460092b7e474b4a3e8a5a8d9`.
- Porównanie wyjaśnień w kluczach dla zmienionych ID obecnych w arkuszach: **0 rozbieżności**. Przestawienia liter A/B/C w arkuszach są celowe; nie zmieniano kluczy, ponieważ ich wyjaśnienia są już zgodne z bankiem.
- Warianty 001–005: po 30 pytań; każdy klucz zawiera 30 odpowiedzi.

## 3. Aktualizacja pakietu recenzyjnego

Pakiet specjalisty uzupełniono o aktualny stan po 4x39, listę zakresu sprawdzonego redakcyjnie i wyraźne rozdzielenie kontroli języka, integralności plików, porównań tekstu prawnego i formalnej akceptacji przez specjalistę.

Nierozstrzygnięte porównania tekstu urzędowego pozostają otwarte. Wszystkie pytania nadal mają status `needs_review`; nie nadano `verified` ani zgody na publikację.

## 4. Quality Gate — preflight

- Bank: 609 pytań, duplikaty ID: 0.
- Najkrótsze explanation w całym banku: 300 znaków; poniżej 200: 0.
- „Poprawna odpowiedź jest jedyną najdłuższą”: 72/609 = 11.82% globalnie.
- Rozkład per dział:
  - ADR-B-01: 6/45 = 13.33%
  - ADR-B-02: 7/56 = 12.50%
  - ADR-B-03: 7/49 = 14.29%
  - ADR-B-04: 6/46 = 13.04%
  - ADR-B-05: 5/43 = 11.63%
  - ADR-B-06: 5/45 = 11.11%
  - ADR-B-07: 6/48 = 12.50%
  - ADR-B-08: 5/42 = 11.90%
  - ADR-B-09: 4/46 = 8.70%
  - ADR-B-10: 4/55 = 7.27%
  - ADR-B-11: 6/43 = 13.95%
  - ADR-B-12: 6/44 = 13.64%
  - ADR-B-13: 5/47 = 10.64%
- Statusy: 609 `needs_review`, 0 `verified`.

## 5. Ograniczenia testów

Próba lokalnego `git clone` nie powiodła się, ponieważ środowisko nie mogło rozwiązać `github.com` (DNS). Nie przedstawiam tego jako lokalnego PASS. Dane i metryki sprawdzono przez GitHub API; PR wymaga pełnego PASS Quality Gate CI przed scaleniem.

## Wniosek

W badanej próbce nie znaleziono potwierdzonego wyjaśnienia wymagającego zmiany. Bank, klucze egzaminów i referencje do lekcji są spójne w sprawdzonym zakresie. Nie rozpoczęto kursu cystern ani innego kursu.
