# Etap 4x276 — granica użycia gaśnicy przy pożarze obejmującym ładownię

Data: 01.11.2026  
Zakres: wyłącznie kurs podstawowy ADR  
Baza: main `52d16f0d47acdb63a93edf63efc277b75089670d`  
Gałąź: `stage4x276-parking-supervision-adr-84`  
Nowe ID: `ADR-B-0702`  
Kompetencja: `ADR-B-05-K06` — mały pożar opon, hamulców lub silnika

## Wybór luki

Kompetencja miała cztery pytania o małe pożary opon i hamulców. Brakowało sytuacji, w której początkowy pożar opony zaczyna obejmować przestrzeń ładunkową — czyli moment, w którym kierowca musi przerwać próbę gaszenia i przejść do ewakuacji oraz instrukcji awaryjnych.

## Dodane pytanie

- `ADR-B-0702`: mały pożar opony zaczyna obejmować elementy przestrzeni ładunkowej.
- Klucz: **B** — przerwać gaszenie, oddalić się w bezpieczne miejsce i postępować zgodnie z instrukcjami awaryjnymi.
- Explanation: **356 znaków**, 4 zdania.
- Długości A/B/C: **100/105/91** znaków; odpowiedzi zbliżone długością, poprawna nie jest znacząco dłuższa.
- Audyt A/B/C: A — błędnie uznaje, że początkowe miejsce pożaru nadal uzasadnia gaszenie; B — rozpoznaje przekroczenie granicy małego pożaru i nakazuje bezpieczne wycofanie; C — proponuje otwarcie ładowni i zbliżenie się do ognia.
- Status: `needs_review`; nic nie oznaczono jako `verified`.

## Podstawa prawna

- ADR 2025, 5.4.3.4, instrukcje pisemne: gaśnice mogą służyć do gaszenia małych/początkowych pożarów opon, hamulców lub komory silnika, jeżeli jest to bezpieczne i właściwe; nie należy podejmować prób gaszenia pożaru w przedziale ładunkowym.
- Oficjalny polski tekst ADR 2025, tom II: https://www.gov.pl/attachment/b4638c72-30e3-4bff-afd1-1b9ba4100e70
- Dz.U. 2025 poz. 642: https://dziennikustaw.gov.pl/DU/2025/642
- UNECE ADR 2025: https://unece.org/adr-2025-files

Właściwy punkt 5.4.3.4 sprawdzono w oficjalnym polskim tekście ADR 2025. Pełne literalne porównanie całego pytania i niezależna recenzja specjalisty pozostają pending.

## Synchronizacja #646

- Bank: 702 pytania ADR-B-0001–0702; wszystkie `needs_review`, 0 `verified`.
- Blob SHA banku: `2363e2cd93b2b4921d77aca7ab3730c3221c44b9`.
- Warianty i klucze egzaminów próbnych 001–005 wskazują aktualny SHA.
- Snapshoty sequential/legal 702-702; rejestr źródeł, manifesty, indeksy, metryki i materiały kursu aktualizowane.
- Rozkład odpowiedzi A/B/C: 237/246/219.
- Wskaźnik „poprawna = jedyna najdłuższa”: 75/702 = 10,68%; maksimum modułu 13,95%.
