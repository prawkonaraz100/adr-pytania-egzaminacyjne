# Etap 4x347 — ADR-B-0773: informacje dla ratowników po pożarze w tunelu

Data: 03.11.2026  
Gałąź: `stage4x347-tunnel-fire-emergency-information`  
Baza: `7b5dc5b9a111caed84574c01e8b458b0b92b9ff2`

## Zakres i podstawa

Dodano ADR-B-0773 do kompetencji teoretycznej `ADR-B-11-K07` — „Zachowanie podczas pożaru w tunelu” (5→6). Pytanie dotyczy przekazania ratownikom informacji o przewożonych towarach niebezpiecznych po bezpiecznej ewakuacji kierowcy. Instrukcje pisemne ADR wymagają powiadomienia odpowiednich służb, przekazania im wszystkich dostępnych informacji o zdarzeniu i towarach niebezpiecznych oraz zapewnienia dostępności dokumentów przewozowych. Nie oznacza to jednak, że kierowca ma wracać do strefy zagrożenia po dokument.

Podstawa: ADR 2025, 5.4.3.4 (Dz.U. 2025 poz. 642).

## Audyt odpowiedzi A/B/C

- A — błędna: sam numer rejestracyjny i miejsce zdarzenia nie informują ratowników o rodzaju przewożonych towarów niebezpiecznych.
- B — błędna: opóźnianie informacji do czasu rozpoznania przez ratowników może utrudnić i spowolnić dobór działań.
- C — poprawna: należy przekazać dostępne informacje o zdarzeniu i ładunku oraz udostępnić dokument przewozowy, jeśli jest bezpiecznie dostępny; nie wracać po niego do strefy zagrożenia.

## Explanation i jakość odpowiedzi

- Explanation: 376 znaków, 4 zdania; prosty język kierowcy.
- Długości A/B/C: 168/172/185 znaków.
- Klucz: C; status `needs_review`; nic nie oznaczono jako `verified`.

## Metryki banku po partii

- Bank: **773** pytań, 773 `needs_review`, 0 `verified`; blob SHA `996c04867b69106382e88188c10d6253e36479e2`.
- Kompetencje teorii z mniej niż 6 pytaniami: **7** (3 praktyczne pominięte).
- ADR-B-11: **46** pytań; ADR-B-11-K07: 5→6.
- Rozkład kluczy A/B/C: **257/286/230**.
- Poprawna odpowiedź jest jedyną najdłuższą: **84/773 = 10,87%**; maksimum działu: **15,22%** (ADR-B-11: 7/46).

## Artefakty

- Klucze i warianty egzaminów próbnych 001–005 wskazują blob banku `996c04867b69106382e88188c10d6253e36479e2`.
- Dodano snapshoty `review/sequential/773-773.json` i `review/legal-clauses/773-773.json`.
- Uzupełniono ledger prawny, rejestr partii, rejestr aktualny i pakiet specjalisty.
- Zaktualizowano `docs/POKRYCIE-KURSU.md`, README i lekcję ADR-B-11.

Pełne porównanie tekstu polskiego ADR 2025 i niezależna recenzja specjalisty pozostają otwarte.

## Źródło

ADR 2025, Dz.U. 2025 poz. 642, 5.4.3.4: https://dziennikustaw.gov.pl/DU/2025/642
UNECE — Polish instructions in writing: https://unece.org/transport/road-transport/linguistic-versions-adr-instructions-writing
