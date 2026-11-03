# Etap 4x345 — ADR-B-0771: najbardziej restrykcyjny kod tunelowy

Data: 03.11.2026  
Gałąź: `stage4x345-mixed-tunnel-code-route-planning`  
Baza: `9a009402dce1e423148618cc0077feb732a1f723`

## Zakres i podstawa

Dodano ADR-B-0771 do teoretycznej kompetencji `ADR-B-11-K04` — „Najbardziej restrykcyjny kod w jednostce” (5→6 pytań). Scenariusz obejmuje jedną jednostkę transportową przewożącą towary z kodami B i D oraz planowaną trasę przez tunel kategorii C. Kierowca stosuje kod powodujący największe ograniczenia dla całego ładunku, czyli B, i wybiera trasę omijającą tunel C.

Podstawa: ADR 2025, 8.6.3.2 i 8.6.4 (Dz.U. 2025 poz. 642).

## Audyt odpowiedzi A/B/C

- A — błędna: nie można wybrać łagodniejszego kodu D dla całej jednostki, gdy drugi towar ma bardziej restrykcyjny kod B.
- B — poprawna: kod B wyklucza tunele kategorii B, C, D i E; trzeba ominąć tunel C.
- C — błędna: kod D samodzielnie nie wyklucza kategorii C, ale nie jest właściwym kodem dla całego ładunku przy obecności kodu B.

## Explanation i jakość odpowiedzi

- Explanation: 353 znaków, 4 zdania; proste wyjaśnienie praktycznej decyzji kierowcy.
- Długości A/B/C: 86/79/78 znaków; poprawna B nie jest najdłuższa.
- Klucz: B; status `needs_review`; nic nie oznaczono jako `verified`.

## Metryki banku po partii

- Bank: **771** pytań, 771 `needs_review`, 0 `verified`; blob SHA `0467701668f4ff28139fb72ab341100b67df4268`.
- Kompetencje teorii z mniej niż 6 pytaniami: **9** (3 praktyczne pominięte).
- ADR-B-11: **58** pytań.
- Rozkład kluczy A/B/C: **257/285/229**.
- Poprawna odpowiedź jest jedyną najdłuższą: **83/771 = 10.77%**; ADR-B-11: 6/44 = 13.64%.

## Artefakty

- Klucze i warianty egzaminów próbnych 001–005 wskazują blob banku `0467701668f4ff28139fb72ab341100b67df4268` (zaktualizowane na gałęzi).
- Dodano snapshoty `review/sequential/771-771.json` i `review/legal-clauses/771-771.json`.
- Dodano rejestr partii i uzupełniono rejestr aktualny specjalisty bez duplikowania ID.
- Uzupełniono pakiet specjalisty o 4x345, SHA banku i licznik kompetencji.
- Zaktualizowano `docs/POKRYCIE-KURSU.md`: ADR-B-11 = 58, łącznie = 771.

Pełne porównanie tekstu polskiego ADR 2025 i niezależna recenzja specjalisty pozostają otwarte.

## Źródło

ADR 2025, Dz.U. 2025 poz. 642, 8.6.3.2 i 8.6.4: https://eli.gov.pl/api/acts/DU/2025/642
