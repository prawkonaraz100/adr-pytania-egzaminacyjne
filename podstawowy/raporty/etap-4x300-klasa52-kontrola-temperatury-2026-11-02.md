# Etap 4x300 — klasa 5.2: kontrola temperatury nadtlenków organicznych

2026-11-02. Bazowy main `87b2e384`; gałąź `stage4x300-class52-organic-peroxides`.

- ADR-B-0726 do ADR-B-02-K08, 5→6 pytań.
- Kompetencje teorii <6 pytań: **54** (wcześniej 55; trzy praktyczne wyłączone).
- Bank 726 pytań, 726 `needs_review`, 0 `verified`. SHA `4dcc4a8f86db5d6bfd8917679a4e29b4f0575c4b`.
- Rozkład A/B/C: 242/260/224; poprawna jedyna najdłuższa 80/726 = 11,02% (limit 18%).
- Klucz C; długości A/B/C 99/89/107; explanation 357 znaków.
- Źródło ADR 2025, 2.2.52.1.15 i 7.1.7. Niezależna recenzja specjalisty i pełne porównanie polskiego tekstu nadal wymagane.
- Zależności: klucze i warianty 001–005, snapshoty 726-726, ledger i SHA, kolejki, manifest 0726, rejestr specjalisty, testy regresji i coverage.

## Pytanie

Przed wyjazdem z nadtlenkiem organicznym klasy 5.2 wymagającym kontroli temperatury kierowca zauważa, że urządzenie chłodzące przestało działać. Co powinien zrobić?

A. Jechać dalej, ponieważ ograniczenie temperatury obowiązuje tylko przed załadunkiem i po rozładunku.

B. Poczekać, aż ładunek sam się schłodzi, bez informowania osób odpowiedzialnych za przewóz.

C. Nie kontynuować przewozu bez przywrócenia wymaganej kontroli temperatury i powiadomić odpowiedzialne osoby.

Niektóre nadtlenki organiczne klasy 5.2 mogą rozkładać się szybciej przy wzroście temperatury, dlatego podczas przewozu muszą mieć zapewnione odpowiednie warunki. Awaria chłodzenia wymaga reakcji, a nie dalszej jazdy ani biernego czekania. Błędne odpowiedzi pomijają obowiązek kontroli temperatury w czasie przewozu. Podstawa: ADR 2025, 2.2.52.1.15 i 7.1.7.
