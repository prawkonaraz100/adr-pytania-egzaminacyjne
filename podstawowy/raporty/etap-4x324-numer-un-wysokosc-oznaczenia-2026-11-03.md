# Etap 4x324 — numer UN: wysokość oznaczenia na opakowaniu

2026-11-03. Bazowy main `a72aa19b4f798088e054d7abb072f1cc3dc1ae02`; gałąź `stage4x324-un-number-package-marking`.

- Dodano ADR-B-0750 do `ADR-B-06-K01`: wysokość oznaczenia numeru UN na opakowaniu.
- Kompetencja wzrosła z 5 do 6 pytań; kompetencje teorii z mniej niż 6 pytaniami: **30** (3 praktyczne pominięte).
- Bank: 750 pytań (ADR-B-0001–0750), 750 `needs_review`, 0 `verified`; SHA `7ee34699938fde20813e3149e188e37b46c69697`.
- Moduł ADR-B-06: 60 pytań.
- Rozkład kluczy A/B/C: 252/269/229.
- „Poprawna odpowiedź jest jedyną najdłuższą”: **81/750 = 10,80%**; maksimum działu **14,61%**. Długości opcji ADR-B-0750: A=85, B=95, C=92; poprawna C nie jest najdłuższa.
- Explanation: 327 znaków, 4 zdania. Dla opakowania 20 l wymagana wysokość liter „UN” i numeru to co najmniej 6 mm. Odpowiedź A myli wymiar ogólny z wyjątkiem, a B pomija dolny próg.
- Podstawa: ADR 2025, 5.2.1.1. Status `needs_review`; pełne literalne porównanie i niezależna recenzja pozostają otwarte.
- Odświeżono klucze i warianty egzaminów próbnych 001–005, snapshoty sequential/legal 750, ledger, manifest, kolejki prawne, rejestr specjalisty, coverage, lekcję B-06, README i testy liczebności.

## Pytanie ADR-B-0750

Kierowca odbiera kanister o pojemności 20 litrów, na którym ADR wymaga oznaczenia numerem UN. Jakiej minimalnej wysokości powinny być cyfry numeru UN wraz z literami „UN”?

A. Co najmniej 12 mm, ponieważ ten wymiar obowiązuje bez wyjątku dla każdego opakowania.

B. Co najmniej 4 mm, ponieważ przy opakowaniach do 30 litrów ADR nie określa minimalnej wysokości.

C. Co najmniej 6 mm, ponieważ kanister o pojemności do 30 litrów korzysta z obniżonego wymiaru.

Dla kanistra o pojemności 20 litrów obowiązuje mniejszy wymiar oznaczenia: cyfry numeru UN i poprzedzające je litery powinny mieć co najmniej 6 mm wysokości. Zwykłe 12 mm dotyczy większych opakowań, więc nie jest jedyną dopuszczalną wartością. ADR nie pozwala też dowolnie zmniejszyć znaku do 4 mm. Podstawa: ADR 2025, 5.2.1.1.

## Audyt A/B/C i źródła

- A — błędna: 12 mm to wymiar ogólny, ale ADR przewiduje 6 mm dla opakowań o pojemności do 30 l lub maksymalnej masie netto do 30 kg.
- B — błędna: wyjątek obniża wymaganą wysokość do 6 mm, a nie znosi minimalnego wymiaru.
- C — poprawna: kanister 20 l mieści się w progu do 30 l, dlatego litery „UN” i numer powinny mieć co najmniej 6 mm.
- Źródło: Dz.U. 2025 poz. 642, ADR 2025, 5.2.1.1 — https://dziennikustaw.gov.pl/DU/2025/642. Pomocniczy tekst ADR 2025 potwierdza ten sam próg: https://www.euraca.eu/media/frmeo2lm/adr-2025-vol-ii.pdf.
- Nie oznaczono żadnego pytania jako `verified`.
