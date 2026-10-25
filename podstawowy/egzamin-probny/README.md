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

## Wynik kontroli etapu 4x18

- Warianty 001–005 mają po 30 unikalnych pytań; żadne ID nie powtarza się między wariantami.
- Każdy wariant obejmuje wszystkie 13 działów; każdy dział ma 2 lub 3 pytania, zgodnie z proporcjonalnym rozkładem w arkuszu 30-pytaniowym.
- Arkusze i klucze mają wspólny `source_bank_head`, odpowiadający aktualnemu blobowi `questions.jsonl`; Quality Gate liczy SHA Git blob i porównuje go z każdym arkuszem oraz kluczem.
- Rozkład poprawnych liter po zmianie kolejności opcji: każdy wariant A/B/C = 10/10/10.
- Najdłuższa seria tej samej poprawnej litery: 001=3, 002=3, 003=3, 004=3, 005=2.
- Walidator: `scripts/check_mock_exam_variants.py`; testy: `tests/test_mock_exam_variants.py`.
- Raport audytu języka: [Etap 4x10](../raporty/etap-4x10-egzaminy-jezyk-kursanta-2026-10-25.md).


## Kontrola etapu 4x18

- Migawka banku: `ec1bb5391aa9875e2a1aa7bdb138fb79b3bf72dd` (609 rekordów; 0 duplikatów ID).
- Wszystkie 5 arkuszy i 5 kluczy wskazują tę samą migawkę; test sprawdza zgodność ID, treści, działu, opcji, poprawnej odpowiedzi i explanation z bankiem.
- Każdy wariant ma 30 pytań bez powtórzeń, wszystkie 13 działów (po 2–3 pytania), A/B/C = 10/10/10 i serię tej samej litery nie dłuższą niż 3.
- Walidator oblicza Git blob SHA-1 z aktualnego pliku banku i blokuje rozjazd metadanych źródła. Testy: `tests/test_mock_exam_variants.py`.
