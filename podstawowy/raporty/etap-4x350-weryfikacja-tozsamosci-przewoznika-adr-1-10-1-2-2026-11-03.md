# Etap 4x350 — ADR-B-0776: identyfikacja przewoźnika

Data: 03.11.2026  
Gałąź: `stage4x350-carrier-identity-verification`  
Baza: `7cd755d874a358203876ee717edae903ecfcec3c`

## Zakres i podstawa

Dodano ADR-B-0776 do kompetencji teoretycznej `ADR-B-12-K04` — „Weryfikacja tożsamości przewoźnika” (5→6). Sytuacja sprawdza rozbieżność między przewoźnikiem wskazanym w zleceniu a firmą faktycznie zgłaszającą odbiór. Przed wydaniem należy zidentyfikować przewoźnika przyjmującego towary niebezpieczne; sama znajomość numeru zlecenia, tablica pojazdu lub dokument kierowcy nie zastępują tej identyfikacji.

Podstawa: ADR 2025, 1.10.1.2 (Dz.U. 2025 poz. 642).

## Audyt odpowiedzi A/B/C

- A — błędna: numer zlecenia i numer rejestracyjny nie dowodzą, że ładunek przyjmuje właściwie zidentyfikowany przewoźnik.
- B — błędna: dokument kierowcy potwierdza tożsamość osoby, ale nie identyfikuje przewoźnika, któremu wydawany jest towar.
- C — poprawna: wydanie należy wstrzymać do czasu potwierdzenia tożsamości przewoźnika faktycznie przyjmującego ładunek.

## Explanation i jakość odpowiedzi

- Explanation: 344 znaki, 4 zdania; prosty język kierowcy.
- Długości A/B/C: 115/116/113 znaków; poprawna C nie jest najdłuższa.
- Klucz: C; status `needs_review`; nic nie oznaczono jako `verified`.

## Metryki banku po partii

- Bank: **776** pytań, 776 `needs_review`, 0 `verified`; blob SHA `dfafbcae0d594e25553ddc30190156aae1b9dd76`.
- Kompetencje teorii z mniej niż 6 pytaniami: **4** (3 praktyczne pominięte).
- ADR-B-12: **48** pytań; ADR-B-12-K04: 5→6.
- Rozkład kluczy A/B/C: **258/287/231**.
- Poprawna odpowiedź jest jedyną najdłuższą: **84/776 = 10,82%**; maksimum działu: **15,22%**.

## Artefakty

- Klucze i warianty egzaminów próbnych 001–005 wskazują blob banku `dfafbcae0d594e25553ddc30190156aae1b9dd76`.
- Dodano snapshoty `review/sequential/776-776.json` i `review/legal-clauses/776-776.json`.
- Uzupełniono ledger źródeł, rejestr partii, rejestr aktualny i pakiet specjalisty.
- Zaktualizowano `docs/POKRYCIE-KURSU.md`, README i lekcję ADR-B-12.

Pełne porównanie tekstu polskiego ADR 2025 i niezależna recenzja specjalisty pozostają otwarte.

## Źródło

ADR 2025, Dz.U. 2025 poz. 642, 1.10.1.2: https://dziennikustaw.gov.pl/DU/2025/642
