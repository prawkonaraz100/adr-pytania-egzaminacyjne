# Etap 4x274 — mocowanie elastycznego kontenera do przewozu luzem

Data: 01.11.2026  
Zakres: wyłącznie kurs podstawowy ADR  
Baza: main `b804d3685da9d3a9402575d84088f1f1a5ae338d`  
Gałąź: `stage4x274-flexible-bulk-container-restraints`  
Nowe ID: `ADR-B-0700`  
Kompetencja: `ADR-B-09-K06` — unikanie nadmiernego naprężenia pasów

## Wybór luki

Cztery dotychczasowe pytania kompetencji dotyczyły głównie ogólnego mocowania sztuk przesyłek i zwykłych opakowań. Brakowało sytuacji dotyczącej szczególnego przepisu dla elastycznych kontenerów do przewozu luzem (7.5.7.6.2), w których nadmierne napięcie wiązań lub pasów może zdeformować sam kontener.

## Dodane pytanie

- `ADR-B-0700`: pasy mocujące elastyczny kontener są napięte tak mocno, że widocznie zmieniają jego kształt.
- Klucz: **B** — poprawić unieruchomienie, aby kontener nie przesuwał się i nie był uszkadzany ani deformowany.
- Explanation: **303 znaki**; praktyczny sens wymogu, wyjaśnienie mylących odpowiedzi i podstawa ADR.
- Długości A/B/C: **105/114/109** znaków; poprawna B jest najdłuższa.
- Audyt A/B/C: A — błędnie dopuszcza deformację; B — spełnia oba warunki: brak przemieszczenia i brak uszkodzenia; C — proponuje czynność wprost sprzeczną z zakazem nadmiernego napinania.
- Status: `needs_review`; nic nie oznaczono jako `verified`.

## Podstawa prawna

- ADR 2025, 7.5.7.6.2: elastyczne kontenery do przewozu luzem należy unieruchomić tak, aby nie przemieszczały się ani nie ulegały uszkodzeniu; wiązania i pasy nie mogą być zbyt mocno zapięte, aby nie powodować uszkodzenia lub deformacji.
- Oficjalny polski tekst ADR 2025, tom II, s. 604: https://www.gov.pl/attachment/b4638c72-30e3-4bff-afd1-1b9ba4100e70
- Dz.U. 2025 poz. 642: https://dziennikustaw.gov.pl/DU/2025/642
- UNECE ADR 2025: https://unece.org/adr-2025-files

Punkt 7.5.7.6.2 sprawdzono bezpośrednio w oficjalnym polskim tekście ADR 2025. Pełne porównanie wszystkich elementów pytania i niezależna recenzja specjalisty pozostają pending.

## Synchronizacja #646 — w toku

- Bank: 700 pytań ADR-B-0001–0700; wszystkie `needs_review`, 0 `verified`.
- Blob SHA banku: `35284ef525c41ebc5ee08fa0423ebf22e262db8c`.
- Warianty i klucze egzaminów próbnych 001–005 wskazują nowy SHA.
- Snapshoty sequential/legal 700-700, rejestr źródeł, manifesty, indeksy, metryki, raport i materiały kursu muszą zostać zsynchronizowane przed PR.
