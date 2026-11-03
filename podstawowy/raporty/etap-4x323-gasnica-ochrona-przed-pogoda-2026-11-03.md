# Etap 4x323 — gaśnica: ochrona przed pogodą i łatwy dostęp

2026-11-03. Bazowy main `66c2b474d146ebf433b1c3532fd9231292f2abcb`; gałąź `stage4x323-extinguisher-mounting-accessibility`.

- Dodano ADR-B-0749 do `ADR-B-05-K12`: gaśnica musi być łatwo dostępna dla załogi i chroniona przed działaniem warunków atmosferycznych.
- Kompetencja wzrosła z 5 do 6 pytań; kompetencje teorii z mniej niż 6 pytaniami: **31** (3 praktyczne pominięte).
- Bank: 749 pytań (ADR-B-0001–0749), 749 `needs_review`, 0 `verified`; SHA `a35f9ad50c4c76d404877cc1fa8eb515a7f1d749`.
- Moduł ADR-B-05: 87 pytań.
- Rozkład kluczy A/B/C: 252/269/228.
- „Poprawna odpowiedź jest jedyną najdłuższą”: **81/749 = 10,81%**; maksimum działu **14,61%**. Długości opcji ADR-B-0749: A=77, B=72, C=88; poprawna B nie jest najdłuższa.
- Explanation: 354 znaki, 4 zdania. Wyjaśnia dwa równoczesne warunki: łatwy dostęp i ochrona przed pogodą. A pomija ochronę, C ukrywa gaśnicę pod ładunkiem i utrudnia dostęp.
- Podstawa: ADR 2025, 8.1.4.5. Status `needs_review`; pełne literalne porównanie i niezależna recenzja pozostają otwarte.
- Odświeżono klucze i warianty 001–005, snapshoty sequential/legal 749, ledger, manifesty, kolejki, rejestr specjalisty (749 unikalnych ID), coverage, lekcję B-05, README i testy regresji.

## Pytanie ADR-B-0749

Gaśnica ADR jest zamocowana na zewnątrz pojazdu i łatwo dostępna, ale podczas jazdy bezpośrednio narażona na deszcz i sól drogową. Co należy poprawić?

A. Pozostawić ją bez osłony, bo liczy się wyłącznie możliwość szybkiego wyjęcia.

B. Zabezpieczyć ją przed pogodą, nie utrudniając załodze szybkiego dostępu.

C. Zamknąć ją w szczelnej skrzyni pod ładunkiem, aby deszcz i sól nie docierały do sprzętu.

Gaśnica ma być łatwo dostępna dla załogi, ale trzeba ją też chronić przed działaniem warunków atmosferycznych. Sam łatwy dostęp nie wystarczy, jeśli deszcz i sól drogowa mogą przyspieszyć korozję lub uszkodzić sprzęt. Nie chowaj jej jednak w miejscu, do którego trudno się dostać; osłona nie może utrudniać szybkiego wyjęcia. Podstawa: ADR 2025, 8.1.4.5.

## Audyt A/B/C i źródła

- A — błędna: pomija obowiązek ochrony gaśnicy przed warunkami atmosferycznymi.
- B — poprawna: łączy ochronę przed pogodą z zachowaniem łatwego dostępu załodze.
- C — błędna: osłona nie może powodować, że gaśnica jest schowana pod ładunkiem i trudno ją wyjąć.
- Źródło: Dz.U. 2025 poz. 642, ADR 2025, 8.1.4.5 — https://eli.gov.pl/api/acts/DU/2025/642/text.pdf. Materiał pomocniczy MI: https://www.gov.pl/attachment/b4638c72-30e3-4bff-afd1-1b9ba4100e70.
- Nie oznaczono żadnego pytania jako `verified`.
