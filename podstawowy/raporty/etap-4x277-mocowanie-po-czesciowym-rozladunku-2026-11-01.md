# Etap 4x277 — ponowne mocowanie ładunku po częściowym rozładunku

Data: 01.11.2026  
Zakres: wyłącznie kurs podstawowy ADR  
Baza: main `ffe1e7d229a9e5743898e15ebef228c1d3d2ccc1`  
Gałąź: `stage4x277-load-resecuring-after-partial-unload`  
Nowe ID: `ADR-B-0703`  
Kompetencja: `ADR-B-09-K02` — mocowanie sztuk przesyłek

## Wybór luki

Kompetencja miała cztery pytania o ogólne mocowanie, odkształcanie opakowań i luźne skrzynie. Brakowało praktycznej sytuacji z wielopunktowej dostawy, w której częściowy rozładunek zmienia układ pozostałych przesyłek i może pozostawić wolną przestrzeń.

## Dodane pytanie

- `ADR-B-0703`: po zdjęciu części skrzyń pozostały ładunek może przesunąć się podczas hamowania.
- Klucz: **A** — ponownie ułożyć i zabezpieczyć pozostałe skrzynie przed dalszą jazdą.
- Explanation: **352 znaki**, 4 zdania.
- Długości A/B/C: **100/122/103** znaków; poprawna A nie jest najdłuższa.
- Audyt A/B/C: A — prawidłowo nakazuje ponowną ocenę i zabezpieczenie reszty ładunku; B — błędnie zakłada, że mocowanie sprzed częściowego rozładunku nadal wystarcza; C — pojedyncza taśma bez sprawdzenia wolnej przestrzeni nie zapewnia zabezpieczenia.
- Status: `needs_review`; nic nie oznaczono jako `verified`.

## Podstawa prawna

- ADR 2025, 7.5.7.1: sztuki przesyłki załadowane na pojazd lub do kontenera należy zabezpieczyć odpowiednimi środkami, aby zapobiec ich przemieszczaniu się podczas przewozu.
- Oficjalny polski tekst ADR 2025, tom II: https://www.gov.pl/attachment/b4638c72-30e3-4bff-afd1-1b9ba4100e70
- Dz.U. 2025 poz. 642: https://dziennikustaw.gov.pl/DU/2025/642
- UNECE ADR 2025: https://unece.org/adr-2025-files

Właściwy punkt 7.5.7.1 sprawdzono w oficjalnym polskim tekście ADR 2025. Pełne literalne porównanie całego pytania i niezależna recenzja specjalisty pozostają pending.

## Synchronizacja #646

- Bank: 703 pytania ADR-B-0001–0703; wszystkie `needs_review`, 0 `verified`.
- Blob SHA banku: `c260f5acf3c035db2a9d1268c73d00a3b76328c3`.
- Warianty i klucze egzaminów próbnych 001–005 wskazują aktualny SHA.
- Snapshoty sequential/legal 703-703; rejestr źródeł, manifesty, indeksy, metryki i materiały kursu aktualizowane.
- Rozkład odpowiedzi A/B/C: 238/246/219.
- Wskaźnik „poprawna = jedyna najdłuższa”: 75/703 = 10,67%; maksimum modułu 13,95%.
