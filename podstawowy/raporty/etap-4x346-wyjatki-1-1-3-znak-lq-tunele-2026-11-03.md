# Etap 4x346 — ADR-B-0772: wyjątek 1.1.3 przy oznakowaniu LQ

Data: 03.11.2026  
Gałąź: `stage4x346-lq-marking-exception-tunnel-code`  
Baza: `f4b8aef00b531d68709b4c7f9732cd786193bc63`

## Zakres i podstawa

Dodano ADR-B-0772 do kompetencji teoretycznej `ADR-B-11-K06` — „Wyłączenia 1.1.3 i przypadek 3.4.13” (5→6). Scenariusz sprawdza wyjątek z ADR 8.6.3.3: towary przewożone zgodnie z 1.1.3 są co do zasady pomijane przy ustalaniu kodu tunelowego całego ładunku, ale nie wtedy, gdy jednostka wymaga oznakowania zgodnie z 3.4.13 z uwzględnieniem 3.4.14. Wówczas kod towaru objętego 1.1.3 należy uwzględnić, a zgodnie z 8.6.3.2 wybrać najbardziej restrykcyjny kod dla całego ładunku. Oznakowana jednostka podlega też ograniczeniu tuneli kategorii E zgodnie z 8.6.4.

Podstawa: ADR 2025, 8.6.3.2, 8.6.3.3 i 8.6.4 (Dz.U. 2025 poz. 642).

## Audyt odpowiedzi A/B/C

- A — błędna: pomija wyjątek z 8.6.3.3 i bezwarunkowo wyłącza towary 1.1.3 z ustalania kodu.
- B — poprawna: wymagane oznakowanie 3.4.13/3.4.14 uruchamia wyjątek; kod B należy uwzględnić i wybrać jako bardziej restrykcyjny niż D.
- C — błędna: oznakowanie LQ nie zwalnia jednostki z ograniczeń tunelowych; 8.6.4 przewiduje ograniczenie kategorii E.

## Explanation i jakość odpowiedzi

- Explanation: 463 znaki, 5 zdań; prosty język kierowcy.
- Długości A/B/C: 182/188/192 znaki; poprawna B nie jest najdłuższa.
- Klucz: B; status `needs_review`; nic nie oznaczono jako `verified`.

## Metryki banku po partii

- Bank: **772** pytań, 772 `needs_review`, 0 `verified`; blob SHA `577557ae08e7354fe5d5f329d2672266e62c2d98`.
- Kompetencje teorii z mniej niż 6 pytaniami: **8** (3 praktyczne pominięte).
- ADR-B-11: **45** pytań; ADR-B-11-K06: 5→6.
- Rozkład kluczy A/B/C: **257/286/229**.
- Poprawna odpowiedź jest jedyną najdłuższą: **83/772 = 10,75%**; maksimum działu: **14,61%**.

## Artefakty

- Klucze i warianty egzaminów próbnych 001–005 wskazują blob banku `577557ae08e7354fe5d5f329d2672266e62c2d98`.
- Dodano snapshoty `review/sequential/772-772.json` i `review/legal-clauses/772-772.json`.
- Uzupełniono ledger prawny, rejestr partii, rejestr aktualny i pakiet specjalisty.
- Zaktualizowano `docs/POKRYCIE-KURSU.md`, README i lekcję ADR-B-11.

Pełne porównanie tekstu polskiego ADR 2025 i niezależna recenzja specjalisty pozostają otwarte.

## Źródło

ADR 2025, Dz.U. 2025 poz. 642, 8.6.3.2–8.6.3.3 i 8.6.4: https://dziennikustaw.gov.pl/DU/2025/642
