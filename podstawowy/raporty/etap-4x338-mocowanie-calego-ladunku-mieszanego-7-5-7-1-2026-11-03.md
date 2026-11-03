# Etap 4x338 — mocowanie całego ładunku mieszanego (ADR 7.5.7.1)

Data: 03.11.2026. Gałąź: `stage4x338-load-securing-packages-7-5-7-1`. Bazowy main: `b692061d17bf3ba6ae19c8f5edc43b48bd5c54a8`.

## Zakres i wynik

- Dokończono ADR-B-0764 w kompetencji teoretycznej `ADR-B-09-K02` — „Mocowanie sztuk przesyłek”; liczba pytań: 5→6.
- Scenariusz sprawdza ładunek mieszany: gdy towary niebezpieczne jadą razem z innymi towarami, nie wystarczy zabezpieczyć samych opakowań ADR. Zwykłe palety także trzeba umocować lub zaklinować, by zapobiec uwolnieniu towarów niebezpiecznych.
- Podstawa: ADR 2025, 7.5.7.1 (Dz.U. 2025 poz. 642).
- Explanation: 377 znaków, 4 zdania; status `needs_review`.
- Podczas korekty doprecyzowano terminologię przepisu: „zamocować lub zaklinować” (nie „zapakować”).

## Audyt odpowiedzi A/B/C

- A — błędna: obowiązek nie ogranicza się do samych sztuk przesyłek ADR; przy przewozie mieszanym obejmuje wszystkie towary.
- B — poprawna: wszystkie towary trzeba zamocować lub zaklinować tak, aby zapobiec uwolnieniu towarów niebezpiecznych.
- C — błędna: przepis nie uzależnia obowiązku zabezpieczenia zwykłych towarów od ich masy ani od tego, czy wydają się zdolne przesunąć opakowania ADR.

## Metryki banku po partii

- Bank: **764** pytań, 764 `needs_review`, 0 `verified`; blob SHA `dfc59132c0d5282742c7ff456c414ebba9acc81c`.
- Kompetencje teorii z mniej niż 6 pytaniami: **16** (3 praktyczne pominięte).
- Moduł ADR-B-09: **57** pytań.
- Rozkład prawidłowych opcji: A/B/C = **257/278/229**.
- Poprawna odpowiedź jest jedyną najdłuższą: **83/764 = 10,86%**; maksimum działu: **14,61%**.
- Długości opcji A/B/C: **116/134/112**; klucz: **B**.

## Synchronizacja artefaktów

- Klucze i warianty egzaminów próbnych 001–005 wskazują aktualny blob banku.
- Snapshoty: `review/sequential/764-764.json`, `review/legal-clauses/764-764.json`.
- Ledger prawny, kolejki i manifesty pakietu specjalisty zsynchronizowane.
- Rejestr specjalisty: `review/specialist/REJESTR-AKTUALNY-0001-0764.md` (764 unikalne ID).
- Coverage, README, lekcja B-09, instrukcja specjalisty i testy liczebności zaktualizowane.
- Pełne literalne porównanie polskiego tekstu i niezależna recenzja specjalisty pozostają otwarte; pytania nie oznaczono `verified`.

## Źródło

ADR 2025, Dz.U. 2025 poz. 642, 7.5.7.1: https://eli.gov.pl/api/acts/DU/2025/642
