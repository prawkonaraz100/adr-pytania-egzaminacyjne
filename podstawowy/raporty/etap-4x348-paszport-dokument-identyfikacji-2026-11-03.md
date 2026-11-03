# Etap 4x348 — ADR-B-0774: paszport jako dokument tożsamości ze zdjęciem

Data: 03.11.2026  
Gałąź: `stage4x348-photo-id-passport-acceptance`  
Baza: `31f70e47b201481fc94a01ff11ccbf0e9b893b91`

## Zakres i podstawa

Dokończono ADR-B-0774 dla kompetencji teoretycznej `ADR-B-12-K01` — „Dokument tożsamości ze zdjęciem” (5→6). ADR 1.10.1.4 wymaga, aby każdy członek załogi pojazdu przewożącego towary niebezpieczne miał przy sobie środek identyfikacji zawierający fotografię tej osoby. Przepis nie wskazuje wyłącznie polskiego dowodu osobistego; ważny paszport ze zdjęciem spełnia wymóg identyfikacji.

Podstawa: ADR 2025, 1.10.1.4 (Dz.U. 2025 poz. 642).

## Audyt odpowiedzi A/B/C

- A — poprawna: przepis wymaga fotografii w środku identyfikacji, a nie konkretnego rodzaju polskiego dokumentu. Paszport ze zdjęciem spełnia ten warunek.
- B — błędna: ADR nie ogranicza dokumentu do polskiego dowodu osobistego.
- C — błędna: ADR nie wymaga dodatkowego identyfikatora przewoźnika ze zdjęciem, jeśli członek załogi ma już ważny dokument identyfikacyjny ze zdjęciem.

## Explanation i jakość odpowiedzi

- Explanation: 336 znaków, 4 zdania; prosty język kierowcy.
- Długości A/B/C: 153/155/145 znaków; poprawna A nie jest najdłuższa.
- Klucz: A; status `needs_review`; nic nie oznaczono jako `verified`.

## Metryki banku po partii

- Bank: **774** pytań, 774 `needs_review`, 0 `verified`; blob SHA `dddfd4d70c9e5e0e4050be60ccf1cc52163e82d9`.
- Kompetencje teorii z mniej niż 6 pytaniami: **6** (3 praktyczne pominięte).
- ADR-B-12: **46** pytań; ADR-B-12-K01: 5→6.
- Rozkład kluczy A/B/C: **258/286/230**.
- Poprawna odpowiedź jest jedyną najdłuższą: **84/774 = 10,85%**; maksimum działu: **15,22%**.

## Artefakty

- Klucze i warianty egzaminów próbnych 001–005 wskazują blob banku `dddfd4d70c9e5e0e4050be60ccf1cc52163e82d9`.
- Dodano snapshoty `review/sequential/774-774.json` i `review/legal-clauses/774-774.json`.
- Uzupełniono ledger prawny, rejestr partii, rejestr aktualny i pakiet specjalisty.
- Zaktualizowano `docs/POKRYCIE-KURSU.md`, README i lekcję ADR-B-12.

Pełne porównanie tekstu polskiego ADR 2025 i niezależna recenzja specjalisty pozostają otwarte.

## Źródło

ADR 2025, Dz.U. 2025 poz. 642, 1.10.1.4: https://dziennikustaw.gov.pl/DU/2025/642
