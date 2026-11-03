# Etap 4x331 — odbiorca: kontrola wymagań ADR po rozładunku

Data: 03.11.2026. Gałąź: `stage4x331-recipient-post-unloading-check`. Bazowy main: `41a88c5403f0dfef2cb4a74d908c88f3f366b16c`.

- Dodano ADR-B-0757 do kompetencji `ADR-B-07-K04` — odbiorca: przyjęcie i dalsze obowiązki; K04: 5→6.
- Podstawa: ADR 2025, 1.4.2.3.1.
- Bank: **757** pytań (ADR-B-0001–0757), 757 `needs_review`, 0 `verified`; SHA `6fa58d5fc5cdf2063883ff77747d5624cb6406e8`.
- Moduł ADR-B-07: **53** pytania.
- Rozkład kluczy A/B/C: **255/273/229**.
- „Poprawna odpowiedź jest jedyną najdłuższą”: **81/757 = 10,70%**; maksimum działu **14,61%**.
- Długości opcji A/B/C: **92/95/93**; poprawna A nie jest najdłuższa.
- Explanation: **349 znaków, 4 zdania**.
- Kompetencje teorii z mniej niż 6 pytaniami: **23** (3 praktyczne pominięte).

## Pytanie ADR-B-0757

Po rozładunku przesyłki ADR odbiorca chce zakończyć odbiór bez sprawdzenia, czy wykonano odnoszące się do niego wymagania ADR. Co powinien zrobić?

A. Po rozładunku sprawdzić, czy spełniono wymagania ADR, które dotyczą odbiorcy w tej operacji.

B. Ograniczyć się do sprawdzenia ilości towaru; kontrola wymagań ADR należy wyłącznie do kierowcy.

C. Uznać, że podpis dokumentu przewozowego potwierdza zgodność i zwalnia z dalszego sprawdzenia.

Odbiorca ma obowiązek sprawdzić po rozładunku, czy wykonano wymagania ADR, które dotyczą go jako uczestnika przewozu. Samo odebranie towaru, policzenie sztuk albo podpisanie dokumentu nie zastępuje tej kontroli. Nie może też przerzucić całej odpowiedzialności na kierowcę, bo ADR nakłada obowiązki również na odbiorcę. Podstawa: ADR 2025, 1.4.2.3.1.

## Audyt A/B/C i źródła

- A — poprawna: 1.4.2.3.1 nakłada na odbiorcę obowiązek sprawdzenia po rozładunku wymagań ADR odnoszących się do niego.
- B — błędna: sama kontrola ilości nie wystarcza, a obowiązki odbiorcy nie należą wyłącznie do kierowcy.
- C — błędna: podpisanie dokumentu nie zastępuje kontroli wymaganej po rozładunku.
- Źródło: Dz.U. 2025 poz. 642, ADR 2025, 1.4.2.3.1 — https://eli.gov.pl/api/acts/DU/2025/642/text.pdf. W oficjalnym tekście przepis mówi o sprawdzeniu po rozładunku, czy spełniono wymagania ADR odnoszące się do odbiorcy.
- Status pozostaje `needs_review`; nie oznaczono żadnego pytania jako `verified`.

## Synchronizacja artefaktów

Klucze i warianty egzaminów próbnych 001–005 wskazują SHA bieżącego banku. Snapshoty `review/sequential/757-757.json` i `review/legal-clauses/757-757.json` zawierają ADR-B-0757. Zaktualizowano ledger prawny, manifesty pakietu specjalisty, kolejki, rejestr bieżący i rejestr partii, coverage, README, lekcję B-07 oraz testy liczebności. Pełne literalne porównanie tekstu polskiego i niezależna recenzja specjalisty pozostają otwarte.
