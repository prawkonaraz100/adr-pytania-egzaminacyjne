# Etap 4x351 — ADR-B-0777: wyjątek „Delivery Sale”

Data: 03.11.2026  
Gałąź: `stage4x351-delivery-sale-consignee-exception`  
Baza: `86e529e68ecd73476ed96501aea76046c81c26c3`

## Zakres i podstawa

Dodano ADR-B-0777 do kompetencji teoretycznej `ADR-B-13-K03` — „Dane odbiorcy i nadawcy” (5→6). Pytanie sprawdza wąski wyjątek dotyczący dostawy do kilku odbiorców, których nie można zidentyfikować na początku przewozu. Zwrot „Delivery Sale” nie jest ogólnym zamiennikiem danych odbiorcy: wymaga zgody właściwych władz państw, których dotyczy przewóz.

Podstawa: ADR 2025, 5.4.1.1.1(h) (Dz.U. 2025 poz. 642).

## Audyt odpowiedzi A/B/C

- A — błędna: nieznajomość odbiorców na początku trasy sama w sobie nie daje prawa do użycia zwrotu „Delivery Sale”.
- B — poprawna: wyjątek jest dopuszczalny tylko przy dostawie do wielu odbiorców nieznanych na początku przewozu i po uzyskaniu zgody właściwych władz państw objętych przewozem.
- C — błędna: nazwa przewoźnika nie zastępuje danych odbiorcy i nie jest zwrotem przewidzianym w tym wyjątku.

## Explanation i jakość odpowiedzi

- Explanation: 354 znaki, 4 zdania; prosty język kierowcy.
- Długości A/B/C: 112/106/105 znaków; poprawna B nie jest najdłuższa.
- Klucz: B; status `needs_review`; nic nie oznaczono jako `verified`.

## Metryki banku po partii

- Bank: **777** pytań, 777 `needs_review`, 0 `verified`; blob SHA `a21eae83c0b5ee259e8fad7618e4cb4270ca64b2`.
- Kompetencje teorii z mniej niż 6 pytaniami: **3** (3 praktyczne pominięte).
- ADR-B-13: **51** pytań; ADR-B-13-K03: 5→6.
- Rozkład kluczy A/B/C: **258/288/231**.
- Poprawna odpowiedź jest jedyną najdłuższą: **84/777 = 10,81%**; maksimum działu: **15,22%**.

## Artefakty

- Klucze i warianty egzaminów próbnych 001–005 wskazują blob banku `a21eae83c0b5ee259e8fad7618e4cb4270ca64b2`.
- Dodano snapshoty `review/sequential/777-777.json` i `review/legal-clauses/777-777.json`.
- Uzupełniono ledger źródeł, rejestr partii, rejestr aktualny i pakiet specjalisty.
- Zaktualizowano `docs/POKRYCIE-KURSU.md`, README i lekcję ADR-B-13.

Pełne porównanie tekstu polskiego ADR 2025 i niezależna recenzja specjalisty pozostają otwarte.

## Źródło

ADR 2025, Dz.U. 2025 poz. 642, 5.4.1.1.1(h): https://dziennikustaw.gov.pl/DU/2025/642
