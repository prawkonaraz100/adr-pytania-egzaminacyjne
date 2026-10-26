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


## Etap 4x25 — końcowa kontrola synchronizacji (2026-10-26)

- Bank: 609 pytań, wszystkie `needs_review`, 0 `verified`.
- Warianty 001–005: każdy ma 30 pytań i 30 odpowiedzi w kluczu; brak duplikatów w arkuszach i między wariantami.
- Każdy arkusz i klucz wskazuje aktualny blob `questions.jsonl`; treść, moduł, zestaw odpowiedzi, poprawna litera i explanation zostały porównane z bankiem z uwzględnieniem przestawiania liter A/B/C.
- Rozkład poprawnych odpowiedzi dla każdego wariantu: A/B/C = 10/10/10; najdłuższa seria tej samej litery = 3; 13 działów reprezentowanych w każdym arkuszu.
- Korekta explanation ADR-B-0197 nie wymagała zmiany pytań w arkuszach, ponieważ ten ID nie występuje w wariantach 001–005. Zaktualizowano wyłącznie metadane źródła w arkuszach i kluczach.
- Raport pełny: [Etap 4x25 — raport końcowy](../raporty/etap-4x25-raport-koncowy-2026-10-26.md).


## Etap 4x26 — ponowna synchronizacja po redakcji podręcznika (2026-10-26)

- Lekcje i materiały instruktora zostały zredagowane; bank nie zmienił się od wygenerowania wariantów.
- Warianty 001–005 i klucze ponownie zsynchronizowano z aktualnym `questions.jsonl`, zachowując wybór ID i proporcje działów oraz odświeżając kolejność błędnych odpowiedzi. `source_bank_head` pozostaje blob SHA banku: `ed0dee6e93f21cbb758c3d088a4d02e0aaed9fc4`.
- Każdy wariant ma 30 pytań, 13 działów, brak powtórzeń w arkuszu i między wariantami, rozkład A/B/C 10/10/10 oraz najdłuższą serię tej samej poprawnej litery nie większą niż 3.
- Klucze są zsynchronizowane z poprawnymi opcjami i explanation banku; explanation mają co najmniej 200 znaków.
- Pełny raport: [Etap 4x26 — raport końcowy](../raporty/etap-4x26-raport-koncowy-2026-10-26.md).
