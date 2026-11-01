# Etap 4x273 — dobór rozmiaru klina pod koło

Data: 01.11.2026  
Zakres: wyłącznie kurs podstawowy ADR  
Baza: main `a344125b923412081e7cfdab35912169de8e7dfc`  
Gałąź: `stage4x273-wheel-chock-sizing`  
Nowe ID: `ADR-B-0699`  
Kompetencja: `ADR-B-08-K04` — klin pod koło

## Wybór luki

Kompetencja miała cztery pytania dotyczące obecności klina, liczby klinów i zestawu z przyczepą. Dodano sytuację, która sprawdza osobny wymóg doboru rozmiaru klina do dopuszczalnej masy całkowitej pojazdu oraz średnicy jego kół.

## Dodane pytanie

- `ADR-B-0699`: klin pasuje fizycznie pod koło, ale jest przeznaczony do znacznie lżejszego pojazdu.
- Klucz: **B** — wymienić go na klin o rozmiarze odpowiednim do DMC i średnicy kół tego pojazdu.
- Explanation: **331 znaków**; praktyczne uzasadnienie, wyjaśnienie pułapek odpowiedzi i podstawa ADR.
- Długości A/B/C: **108/105/103** znaków; poprawna B nie jest najdłuższa.
- Audyt A/B/C: A — myli samo posiadanie z wymaganym doborem rozmiaru; B — zgodna z wymogiem dopasowania do DMC i średnicy koła; C — błędnie zakłada, że liczba małych klinów zastępuje odpowiedni rozmiar.
- Status: `needs_review`; nic nie oznaczono jako `verified`.

## Podstawa prawna

- ADR 2025, 8.1.5.2: klin pod koło dla każdego pojazdu, o rozmiarze odpowiednim do dopuszczalnej masy całkowitej pojazdu i średnicy jego kół.
- Oficjalny polski tekst ADR 2025, tom II: https://www.gov.pl/attachment/b4638c72-30e3-4bff-afd1-1b9ba4100e70
- Dz.U. 2025 poz. 642: https://dziennikustaw.gov.pl/DU/2025/642
- UNECE ADR 2025: https://unece.org/adr-2025-files

Właściwy fragment 8.1.5.2 został sprawdzony w oficjalnym polskim tekście ADR 2025. Pełne porównanie wszystkich elementów pytania i niezależna recenzja specjalisty pozostają pending.

## Synchronizacja #646 — w toku

- Bank: 699 pytań ADR-B-0001–0699; wszystkie `needs_review`, 0 `verified`.
- Blob SHA banku: `9359365b4381b3b644b70d9b80bd35d171256bd7`.
- Warianty 001–005 i klucze 001–005 muszą wskazywać nowy SHA.
- Snapshoty sequential/legal 699-699, manifesty, rejestry, indeksy, raporty jakości i testy regresyjne muszą zostać odświeżone przed PR.
