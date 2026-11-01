# Etap 4x280 — bezpieczny przejazd do miejsca czyszczenia po wycieku

Data: 01.11.2026  
Zakres: wyłącznie kurs podstawowy ADR  
Baza: main `50b30082656191d29a1a1e9e91b3fcab84274103`  
Gałąź: `stage4x280-residual-contamination-before-loading`  
Nowe ID: `ADR-B-0706`  
Kompetencja: `ADR-B-09-K07` — czyszczenie pojazdu po rozładunku

## Wybór luki

Kompetencja miała pytania o niezwłoczne czyszczenie po wycieku oraz wyjątek przy ponownym załadunku tego samego towaru luzem. Brakowało drugiego kroku z ADR 7.5.8.1: gdy nie można oczyścić pojazdu w miejscu rozładunku, należy przemieścić go z odpowiednimi środkami ostrożności do najbliższego miejsca, gdzie czyszczenie jest możliwe, tak aby nie doszło do niekontrolowanego wycieku.

## Dodane pytanie

- `ADR-B-0706`: po rozładunku sztuk przesyłek pozostały resztki uwolnionej zawartości, a na placu nie można bezpiecznie oczyścić pojazdu.
- Klucz: **B** — przemieścić pojazd do najbliższego miejsca czyszczenia z zabezpieczeniami zapobiegającymi niekontrolowanemu wyciekowi.
- Explanation: **430 znaków**, 4 zdania; praktyczny sens, wyjaśnienie błędnych odpowiedzi i podstawa ADR.
- Długości A/B/C: **103/99/98** znaków; poprawna B nie jest najdłuższa.
- Audyt A/B/C: A — pozostawia zanieczyszczenie bez bezpiecznego rozwiązania; B — odpowiada drugiemu akapitowi 7.5.8.1; C — błędnie zakłada, że można jechać zwykłą trasą do dowolnej bazy bez zabezpieczeń.
- Status: `needs_review`; nic nie oznaczono jako `verified`.

## Podstawa prawna

- ADR 2025, 7.5.8.1: pojazd lub kontener, w którym po przewozie w sztukach przesyłek stwierdzono uwolnienie części zawartości, należy oczyścić niezwłocznie. Jeżeli nie można tego zrobić w miejscu rozładunku, pojazd powinien być przewieziony — z odpowiednimi środkami ostrożności zapobiegającymi niekontrolowanemu wyciekowi — do najbliższego miejsca, gdzie można przeprowadzić czyszczenie.
- Oficjalny polski tekst ADR 2025, tom II: https://www.gov.pl/attachment/b4638c72-30e3-4bff-afd1-1b9ba4100e70
- Dz.U. 2025 poz. 642: https://dziennikustaw.gov.pl/DU/2025/642
- UNECE ADR 2025: https://unece.org/adr-2025-files

Punkt 7.5.8.1 sprawdzono w oficjalnym polskim tekście ADR 2025. Pełne literalne porównanie całego pytania i niezależna recenzja specjalisty pozostają pending.

## Synchronizacja #646

- Bank: 706 pytań ADR-B-0001–0706; wszystkie `needs_review`, 0 `verified`.
- Blob SHA banku: `8d84e1a448cb25c1b597ba0bf82d4eb1125cb0fb`.
- Warianty i klucze egzaminów próbnych 001–005 wskazują ten SHA.
- Snapshoty sequential/legal 706-706, ledger źródeł, manifesty i indeks recenzyjny zostały odświeżone.
- Rozkład prawidłowych opcji A/B/C: 238/249/219.
- „Poprawna = jedyna najdłuższa”: 75/706 = 10,62%; maksimum modułu: 13,95%.
