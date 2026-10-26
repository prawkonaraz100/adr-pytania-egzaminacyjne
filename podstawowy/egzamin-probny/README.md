# Egzamin próbny ADR podstawowy — materiały treningowe

Warianty są przeznaczone wyłącznie do nauki. Każdy arkusz ma 30 pytań, 60 minut i próg treningowy 20/30. Odpowiedzi A/B/C są wyrównane, a najdłuższa seria tej samej poprawnej litery nie przekracza trzech.

## Arkusze — rozwiąż przed otwarciem klucza

- [Wariant 001 — arkusz pytań](wariant-001.json)
- [Wariant 002 — arkusz pytań](wariant-002.json)
- [Wariant 003 — arkusz pytań](wariant-003.json)
- [Wariant 004 — arkusz pytań](wariant-004.json)
- [Wariant 005 — arkusz pytań](wariant-005.json)

## Klucze i wyjaśnienia — dopiero po rozwiązaniu

- [Wariant 001 — klucz i wyjaśnienia](klucz-001.json)
- [Wariant 002 — klucz i wyjaśnienia](klucz-002.json)
- [Wariant 003 — klucz i wyjaśnienia](klucz-003.json)
- [Wariant 004 — klucz i wyjaśnienia](klucz-004.json)
- [Wariant 005 — klucz i wyjaśnienia](klucz-005.json)

**Uwaga o dostępie:** klucze są rozdzielone od arkuszy w nawigacji, ale repozytorium jest publiczne, więc nie ma technicznego ograniczenia dostępu. Przed zakończeniem próby nie otwieraj plików kluczy.

## Status prawny

Bank zawiera 609 pytań `needs_review` i 0 `verified`. Arkusze mają `publication_authorized: false` i nie są oficjalnymi arkuszami ani materiałem do formalnej oceny. Klucze i explanation są synchronizowane z bankiem przez Quality Gate.

## Etap 4x20 — regeneracja wariantów 001–005 (2026-10-26)

- Migawka banku: `46e7d1a0c28d21dce01b054be8513ef7db1f6210` (609 pytań; ADR-B-0001–ADR-B-0609).
- Warianty 001–005 i odpowiadające im klucze zostały wygenerowane ponownie z aktualnego banku. Każdy wariant ma 30 pytań, obejmuje wszystkie 13 działów (po 2–3 pytania na dział), a ID nie powtarzają się ani w wariancie, ani między wariantami.
- Wskaźnik „poprawna odpowiedź jest jedyną najdłuższą”: 001=0/30 (0%), 002=0/30 (0%), 003=0/30 (0%), 004=0/30 (0%), 005=0/30 (0%); próg kontrolny wynosi 18%.
- Rozkład poprawnych liter A/B/C: każdy wariant 10/10/10. Najdłuższa seria tej samej litery: każdy wariant ≤3.
- Warianty i klucze wskazują ten sam blob banku. Wyjaśnienia w kluczach są mapowane do kolejności odpowiedzi na arkuszu.
- Quality Gate: `scripts/check_mock_exam_variants.py` blokuje również przekroczenie 18% w dowolnym wariancie; test regresyjny w `tests/test_mock_exam_variants.py`.
- Raport: [Etap 4x20 — regeneracja egzaminów 001–005](../raporty/etap-4x20-egzaminy-001-005-2026-10-26.md).

**Status prawny:** 609 pytań `needs_review`, 0 `verified`; arkusze są wyłącznie materiałem treningowym, `publication_authorized: false`.
