# Etap 4x303 — klasa 7: rozpoznawanie materiałów promieniotwórczych

2026-11-02. Bazowy main `d18e82f1`; gałąź `stage4x303-class7-radioactive-recognition`.

- ADR-B-0729 do ADR-B-02-K11, kompetencja uzupełniona z 5 do 6 pytań.
- **Kompetencje teorii <6 pytań: 51** (poprzednio 52; trzy praktyczne pomijane).
- Bank 729, 729 `needs_review`, 0 `verified`; SHA `29dd69585e261ce1b8f6f9e5b1282cf4ec2d4be3`.
- Rozkład A/B/C: 242/262/225; poprawna jedyna najdłuższa **82/729 = 11,25%**, maksimum działu 16,09% (limit 18%).
- Klucz B; długości A/B/C 84/88/84; explanation 324 znaków.
- Podstawa ADR 2025, 2.2.7.1.1.1 i 5.2.2.1.11. Pełne literalne porównanie tekstu polskiego i recenzja specjalisty pozostają wymagane.
- Odświeżono egzaminy 001–005, snapshoty 729, ledger, kolejki, manifest PAKIET-0729, rejestr specjalisty, coverage i testy.

## Pytanie

Podczas kontroli dokumentów kierowca widzi, że sztuka przesyłki ma etykietę z czarnym symbolem koniczyny promieniotwórczej i cyfrą 7. Do jakiej klasy ADR należy ten ładunek?

A. Do klasy 6.2 — materiały zakaźne, które mogą przenosić drobnoustroje chorobotwórcze.

B. Do klasy 7 — materiały promieniotwórcze, wymagające rozpoznania zagrożenia radiacyjnego.

C. Do klasy 5.1 — materiały utleniające, które mogą nasilać spalanie innych substancji.

Symbol koniczyny i numer 7 wskazują na materiały promieniotwórcze klasy 7. Kierowca powinien rozpoznać tę klasę, ponieważ przewóz wiąże się z zagrożeniem promieniowaniem jonizującym, a nie z zakażeniem czy nasilaniem pożaru. Nie należy mylić numeru klasy z klasą 6.2 ani 5.1. Podstawa: ADR 2025, 2.2.7.1.1.1 oraz 5.2.2.1.11.
