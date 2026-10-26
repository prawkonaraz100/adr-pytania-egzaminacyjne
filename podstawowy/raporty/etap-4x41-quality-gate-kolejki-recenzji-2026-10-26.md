# Etap 4x41 — Quality Gate dla kolejki recenzji prawnej

- Data: 2026-10-26.
- Świeży `main`: `da7842cc08dbcad1d6bf889bae579128238b16f2`.
- Zakres: wyłącznie kurs podstawowy ADR; bez zmian banku i odpowiedzi.

## Problem

Po dodaniu kolejki priorytetowej 4x40 nie było jeszcze testu regresyjnego pilnującego, by jej ID, pytania, podstawy i snapshot banku pozostały zgodne po późniejszych edycjach. Plik kolejki mógłby się zestarzeć bez wykrycia przez dotychczasowe testy.

## Zmiana

Dodano `test_priority_legal_review_queue_stays_synchronized` do `tests/test_review_packet_integrity.py`. Test sprawdza:
- kolejka ma 20 unikalnych rekordów;
- każdy ID istnieje w banku i na liście ID bez dosłownego cytatu MI;
- dział, treść pytania i lista podstaw prawnych są zgodne z aktualnym rekordem banku;
- bank SHA zgadza się z manifestem i kolejką;
- wszystkie wpisy pozostają `needs_review`, a porównanie z Dz.U. pozostaje `pending`;
- nie ma numerów stron ani twierdzeń o formalnej weryfikacji w rekordach kolejki.

Dodano odwołanie do testu w manifeście i instrukcji recenzji.

## Preflight danych

- Bank: 609 pytań; bank blob SHA `8a16afb47c5d5a9e460092b7e474b4a3e8a5a8d9`.
- Lista bez cytatu MI: 121 ID.
- Kolejka: 20 rekordów, 20 unikalnych ID.
- ID z kolejki nieobecne w banku: 0.
- Statusy kolejki: wszystkie needs_review / pending.
- Bank: 609 `needs_review`, 0 `verified`; „poprawna = jedyna najdłuższa” 11,82% globalnie.

## Testy

Próba lokalnego klonowania nie powiodła się z powodu błędu DNS dla `github.com`; lokalnego PASS nie deklaruję. Wymagany pełny PASS Quality Gate CI na PR.

## Ograniczenia

Test pilnuje integralności i aktualności danych, ale nie potwierdza poprawności prawa ani priorytetu merytorycznego. Rozstrzygnięcie wymaga specjalisty oraz oficjalnego polskiego tekstu Dz.U. 2025 poz. 642 i sprostowania poz. 1575. Wszystkie pytania pozostają `needs_review`.
