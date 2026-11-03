# Etap 4x330 — numer zagrożenia 86: materiał żrący lub słabo żrący i toksyczny

Data: 03.11.2026. Gałąź: `stage4x330-hazard-number-8-corrosivity`. Bazowy main: `57f412e26af45301561730bbc337eee0d877151b`.

- Dodano ADR-B-0756 do kompetencji `ADR-B-06-K08` — znaczenie cyfry 8 w numerze zagrożenia; K08: 5→6.
- Podstawa: ADR 2025, 5.3.2.3.1–5.3.2.3.2.
- Bank: **756** pytań (ADR-B-0001–0756), 756 `needs_review`, 0 `verified`; SHA `28a535b640a1e6fc8ff23e2bfc9b746bd1f58908`.
- Moduł ADR-B-06: **66** pytań.
- Rozkład kluczy A/B/C: **254/273/229**.
- „Poprawna odpowiedź jest jedyną najdłuższą”: **81/756 = 10,71%**; maksimum działu **14,61%**.
- Długości opcji A/B/C: **107/112/100**; poprawna A nie jest najdłuższa.
- Explanation: **347 znaków, 4 zdania**.
- Kompetencje teorii z mniej niż 6 pytaniami: **24** (3 praktyczne pominięte).

## Pytanie ADR-B-0756

Na górnym polu tablicy ADR odczytujesz numer zagrożenia 86. Jak powinieneś przekazać znaczenie tego kodu ratownikom?

A. Jako substancję żrącą lub słabo żrącą, która jest jednocześnie toksyczna; oba zagrożenia trzeba uwzględnić.

B. Jako substancję silnie żrącą i toksyczną, ponieważ każda kombinacja z cyfrą 8 oznacza najwyższy poziom żrącości.

C. Jako substancję utleniającą i toksyczną; cyfra 8 opisuje tu nasilenie palności, nie działanie żrące.

Numer 86 oznacza substancję żrącą lub słabo żrącą, która jest jednocześnie toksyczna. Cyfra 8 wskazuje na działanie żrące, a 6 na toksyczność, więc ratownicy muszą znać oba zagrożenia. Odpowiedź B myli kod 86 z 88, który oznacza substancję silnie żrącą; C błędnie przypisuje cyfrze 8 znaczenie utleniające. Podstawa: ADR 2025, 5.3.2.3.1–5.3.2.3.2.

## Audyt A/B/C i źródła

- A — poprawna: numer 86 oznacza substancję żrącą lub słabo żrącą, która jest toksyczna.
- B — błędna: kod 88 oznacza substancję silnie żrącą; nie wolno przenosić tego znaczenia na 86.
- C — błędna: cyfra 8 opisuje zagrożenie żrące, a nie utleniające ani palność; 6 oznacza toksyczność.
- Źródło: Dz.U. 2025 poz. 642, ADR 2025, 5.3.2.3.1–5.3.2.3.2 — https://eli.gov.pl/api/acts/DU/2025/642/text.pdf.
- Status pozostaje `needs_review`; nie oznaczono żadnego pytania jako `verified`.

## Synchronizacja artefaktów

Klucze i warianty egzaminów próbnych 001–005 wskazują SHA bieżącego banku. Snapshoty `review/sequential/756-756.json` i `review/legal-clauses/756-756.json` zawierają ADR-B-0756. Zaktualizowano ledger prawny, manifesty pakietu specjalisty, kolejki, rejestr bieżący i rejestr partii, coverage, README, lekcję B-06 oraz testy liczebności. Pełne literalne porównanie tekstu polskiego i niezależna recenzja specjalisty pozostają otwarte.
