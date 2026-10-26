# Egzamin próbny ADR podstawowy — materiały treningowe

Warianty są przeznaczone wyłącznie do nauki. Każdy arkusz ma 30 pytań, 60 minut i próg treningowy 20/30. Odpowiedzi A/B/C są wyrównane, a najdłuższa seria tej samej poprawnej litery nie przekracza trzech.

## Jak interpretować wynik

- **20–30 poprawnych odpowiedzi:** osiągasz próg treningowy tego arkusza, ale nie jest to oficjalne potwierdzenie kwalifikacji ani dowód, że wszystkie zagadnienia opanowano.
- **0–19 poprawnych odpowiedzi:** wróć do nauki przed kolejną próbą. Zapisz ID pytań, na które odpowiedziałeś błędnie, i sprawdź ich `module_id` w banku.
- **Po każdym błędzie:** przeczytaj explanation do końca: najpierw sens poprawnej odpowiedzi, potem przyczynę błędu pozostałych opcji, a na końcu wskazany punkt ADR. Nie ucz się samej litery, bo warianty mogą mieć inne kolejności A/B/C.
- **Powtórka:** otwórz lekcję właściwego działu, przećwicz trzy scenariusze tego działu i dopiero wtedy rozwiąż inny wariant.
- **Status materiału:** wszystkie pytania pozostają `needs_review`; wynik jest wyłącznie informacją do samodzielnej nauki.

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


## Aktualizacja synchronizacji — etap 4x31

- Migawka banku i kluczy: `99c06e736c0e5812e97d4ff02567dbf741629434`.
- Po redakcji wyjaśnienia ADR-B-0540 zsynchronizowano `source_bank_head` we wszystkich wariantach i kluczach 001–005.
- Wszystkie warianty pozostają materiałami treningowymi; pytania nadal mają status `needs_review`.


## Etap 4x34 — kontrola powtórzeń i podpowiedzi (2026-10-26)

- Migawka aktualnego banku: `7c7573215da82caeabe9543eb47dfc9703ecf622`.
- Zmieniono pytania ADR-B-0048, ADR-B-0078, ADR-B-0127 i ADR-B-0238; warianty i klucze 001–005 wskazują aktualny blob banku.
- Wariant 002 i jego klucz zaktualizowano dla ADR-B-0078; pozostałe warianty zachowały zestaw pytań.
- Status prawny pozostaje bez zmian: 609 pytań `needs_review`, 0 `verified`, brak formalnej zgody na publikację.
