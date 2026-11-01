# Etap 4x275 — plac czasowego składowania towarów niebezpiecznych

Data: 01.11.2026  
Zakres: wyłącznie kurs podstawowy ADR  
Baza: main `7841f3b0b69e24c1f37b8370e7cd2586ca27b5fc`  
Gałąź: `stage4x275-tunnel-fire-evacuation-procedure`  
Nowe ID: `ADR-B-0701`  
Kompetencja: `ADR-B-12-K02` — zabezpieczenie placów i składowania

## Wybór luki

Kompetencja miała cztery pytania o ogólne zabezpieczenie terminali i placów. Brakowało scenariusza, w którym kursant ocenia konkretne miejsce czasowego składowania, uwzględniając łącznie zabezpieczenie terenu, oświetlenie oraz ograniczenie dostępu publicznego — z zachowaniem zastrzeżenia „gdzie to możliwe i właściwe”.

## Dodane pytanie

- `ADR-B-0701`: plac terminalu jest ciemny, a brama od strony ulicy pozostaje otwarta.
- Klucz: **B** — plac musi być zabezpieczony i oświetlony, a gdy jest to możliwe i właściwe — niedostępny dla osób postronnych.
- Explanation: **344 znaki**, 4 zdania; najpierw praktyczny sens poprawnej odpowiedzi, następnie wyjaśnienie pułapek A/C, na końcu podstawa ADR.
- Długości A/B/C: **110/110/107** znaków; dystraktory wyrównane.
- Audyt A/B/C: A — pomija zabezpieczenie dostępu; B — obejmuje trzy elementy przepisu i zachowuje jego kwalifikator; C — pomija oświetlenie i błędnie traktuje zamknięty pojazd jako zamiennik wymagań wobec placu.
- Status: `needs_review`; nic nie oznaczono jako `verified`.

## Podstawa prawna

- ADR 2025, 1.10.1.3: obszary w terminalach, bazach i na placach wykorzystywane do czasowego składowania towarów niebezpiecznych podczas przewozu powinny być właściwie zabezpieczone, dobrze oświetlone i, gdzie to możliwe oraz właściwe, niedostępne dla ogółu.
- Oficjalny polski tekst ADR 2025, tom II: https://www.gov.pl/attachment/b4638c72-30e3-4bff-afd1-1b9ba4100e70
- Dz.U. 2025 poz. 642: https://dziennikustaw.gov.pl/DU/2025/642
- UNECE ADR 2025: https://unece.org/adr-2025-files

Właściwy punkt 1.10.1.3 sprawdzono w oficjalnym polskim tekście ADR 2025. Pełne literalne porównanie całego pytania i niezależna recenzja specjalisty pozostają pending.

## Synchronizacja #646

- Bank: 701 pytań ADR-B-0001–0701; wszystkie `needs_review`, 0 `verified`.
- Blob SHA banku: `64544daffd52784e1a9a85c8c14cd22d2e293950`.
- Warianty i klucze egzaminów próbnych 001–005 wskazują aktualny SHA.
- Snapshoty sequential/legal 701-701; rejestr źródeł, manifesty, indeksy, metryki i materiały kursu zaktualizowane.
- Rozkład odpowiedzi A/B/C: 237/245/219.
- Wskaźnik „poprawna = jedyna najdłuższa”: 74/701 = 10,56%; maksimum modułu 13,95%.
