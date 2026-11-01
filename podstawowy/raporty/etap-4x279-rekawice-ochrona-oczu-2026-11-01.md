# Etap 4x279 — indywidualne rękawice i ochrona oczu dla załogi

Data: 01.11.2026  
Zakres: wyłącznie kurs podstawowy ADR  
Baza: main `83ddff2b5f27aad31a7ed057cf3d5b1bb06b6f2f`  
Gałąź: `stage4x279-personal-protective-equipment`  
Nowe ID: `ADR-B-0705`  
Kompetencja: `ADR-B-08-K06` — rękawice i ochrona oczu

## Wybór luki

W kompetencji były pytania o rękawice, ochronę oczu i komplet wyposażenia, ale brakowało sytuacji sprawdzającej słowa „dla każdego członka załogi”. Nowe pytanie weryfikuje, czy kursant rozumie, że wymagane elementy muszą być dostępne indywidualnie dla każdej osoby, a nie jako jeden wspólny komplet.

## Dodane pytanie

- `ADR-B-0705`: w kabinie są dwie osoby, ale środki ochrony ma tylko kierowca.
- Klucz: **B** — każdemu członkowi załogi zapewnić własne rękawice ochronne i ochronę oczu.
- Explanation: **327 znaków**, 4 zdania; najpierw praktyczny sens, następnie wyjaśnienie błędnych odpowiedzi, na końcu podstawa ADR.
- Długości A/B/C: **107/102/102** znaków; poprawna B nie jest najdłuższa.
- Audyt A/B/C: A — błędnie zakłada możliwość współdzielenia zestawu; B — odzwierciedla wymóg „dla każdego członka załogi”; C — pomija ochronę oczu drugiej osoby, choć kierowca nie jest jedynym członkiem załogi.
- Status: `needs_review`; nic nie oznaczono jako `verified`.

## Podstawa prawna

- ADR 2025, 8.1.5.2: w jednostce transportowej ma być para rękawic ochronnych i ochrona oczu (np. okulary ochronne) **dla każdego członka załogi pojazdu**.
- Oficjalny polski tekst ADR 2025, tom II: https://www.gov.pl/attachment/b4638c72-30e3-4bff-afd1-1b9ba4100e70
- Dz.U. 2025 poz. 642: https://dziennikustaw.gov.pl/DU/2025/642
- UNECE ADR 2025: https://unece.org/adr-2025-files

Punkt 8.1.5.2 sprawdzono w oficjalnym polskim tekście ADR 2025. Pełne literalne porównanie pytania i niezależna recenzja specjalisty pozostają pending.

## Synchronizacja #646

- Bank: 705 pytań ADR-B-0001–0705; wszystkie `needs_review`, 0 `verified`.
- Blob SHA banku: `c1e4a8bb7c44771246bedf691b528f5f43b07630`.
- Warianty i klucze egzaminów próbnych 001–005 wskazują ten SHA.
- Snapshoty sequential/legal 705-705, ledger źródeł, manifest i indeks recenzyjny zostały odświeżone. Wykryty pusty plik głównego rejestru (609 rekordów) odtworzono wyłącznie ze statusem `not_retrieved_not_literally_compared`; nie przypisano mu dawnych porównań ani zatwierdzeń.
- Rozkład prawidłowych opcji A/B/C: 238/248/219.
- „Poprawna = jedyna najdłuższa”: 75/705 = 10,64%; maksimum modułu: 13,95%.
