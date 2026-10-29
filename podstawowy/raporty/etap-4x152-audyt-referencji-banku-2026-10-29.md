# Etap 4x152 — audyt referencji banku, egzaminów i mapy kompetencji

Data: 29.10.2026. Bazowy main: `170ac459623a530d3747475472dc8b1ae60420b9`.

## Wersja źródłowa

- `podstawowy/questions.jsonl`: 638 rekordów, ostatnie ID `ADR-B-0638`.
- Aktualny identyfikator Git blob: `3f5cf70d024f9f18f93a708961e948a8b249fa91`.
- Statusy: 638 `needs_review`, 0 `verified`.

## Egzaminy próbne 001–005

Sprawdzono wszystkie pięć plików `wariant-001.json`–`wariant-005.json` i wszystkie pięć `klucz-001.json`–`klucz-005.json`. **10/10 plików wskazuje aktualny blob `3f5cf70d024f9f18f93a708961e948a8b249fa91`.** Nie zmieniano ich, ponieważ referencje były już zgodne; nie było podstaw do tworzenia zbędnego diffu. Warianty pozostają nieautoryzowane do publikacji, a kontrola referencji nie jest zatwierdzeniem prawnym pytań.

## Mapa 107 kompetencji

- `podstawowy/kompetencje.json` zawiera 107 kompetencji: 104 teoretyczne i 3 praktyczne.
- Sprawdzono wszystkie wpisane `question_ids` względem aktualnego banku: **0 nieistniejących ID**.
- Najmniejsza liczba pytań wśród kompetencji teoretycznych wynosi 3. Dwa najniżej pokryte cele to `ADR-B-01-K01` (ramy prawne i definicje ADR) oraz `ADR-B-07-K07` (rozróżnienie odpowiedzialności deliktowej i kontraktowej). Wśród pozostałych kompetencji teoretycznych występują cele z 4 pytaniami.
- Trzy kompetencje praktyczne w dziale 05 mają 0 `question_ids`; są opisane jako instruktaż/scenariusz praktyczny i nie traktuje się tego automatycznie jako błędu banku. Powinny być pokrywane ćwiczeniami praktycznymi, a niekoniecznie pytaniami testowymi.

Zaktualizowano metadane `last_editorial_audit`, zapisując aktualny blob banku i wyniki tej kontroli.

## Pakiet specjalisty

- `review/specialist/KOLEJKA-PRIORYTETOWA-4X40.json` i `KOLEJKA-PRIORYTETOWA-4X44.json` już wskazywały aktualny blob.
- `PAKIET-0628-MANIFEST.json` już wskazywał aktualny blob.
- Wykryto i poprawiono niezgodność w `PAKIET-0638-MANIFEST.json`: `current_bank_blob_sha` wskazywał poprzedni blob `f06adebc34d982d8eb09b5e7569785cb1e7cf743`; teraz wskazuje `3f5cf70d024f9f18f93a708961e948a8b249fa91`.

## Wynik i ograniczenia

W zakresie referencji: egzaminy 10/10 zgodne, mapa 107 kompetencji ma 0 nieistniejących odwołań, kolejki specjalisty zgodne, nieaktualny blob w najnowszym manifeście naprawiony. Test ten potwierdza spójność metadanych, a nie zgodność merytoryczną pytań z ADR 2025. Wszystkie pytania pozostają `needs_review`; niczego nie oznaczono `verified`.
