# Etap 4x204 — drugi przegląd explanation (partia 45)

Data: 2026-10-30. Świeży main po PR #672: `49a748a6dc6efd651e0e2695eb06fcd7813da4db`. Bank kursu podstawowego 651 pytań.

## Wybrane ID

ADR-B-0044, ADR-B-0060, ADR-B-0065, ADR-B-0073, ADR-B-0080, ADR-B-0082, ADR-B-0085, ADR-B-0093, ADR-B-0097 i ADR-B-0098.

## Zmiany

Zmiany wyłącznie w polu `explanation` tych 10 pytań. Każde wyjaśnienie ma 4–5 zdań i 340–408 znaków: praktyczny sens poprawnej odpowiedzi, dlaczego błędne opcje są błędne, krótka podstawa ADR. Zachowano wszystkie pytania, warianty A/B/C, klucze, źródła i statusy. Brak potwierdzonego błędu merytorycznego wymagającego zmiany odpowiedzi.

## Synchronizacja

- Snapshoty `review/sequential` i `review/legal-clauses` — zakresy 031–060, 061–090, 091–120, razem 10 ID.
- Warianty i klucze egzaminów próbnych 001–005: blob `864fca93ec15436701a2facb580ac86a61b031e7`. W kluczu 001 odświeżono explanation ADR-B-0044; w kluczu 004 — ADR-B-0065, ADR-B-0080 i ADR-B-0073.
- Manifest próbkowy oraz referencje SHA pakietu recenzenta uaktualnione.

## Granice weryfikacji

651 pytań pozostaje `needs_review`, zero `verified`. Redakcja nie oznacza prawnego zatwierdzenia odpowiedzi przez eksperta. Zakres wyłącznie podstawowy ADR; nie obejmuje kursu cystern.

## Kontrola regresji

Pierwszy przebieg Quality Gate wykazał test wymagający zwrotu „nie jest wymaganym minimum” w ADR-B-0073. Przywrócono tę formułę bez zmiany znaczenia odpowiedzi; odświeżono klucz 004, snapshoty i wszystkie referencje SHA.
