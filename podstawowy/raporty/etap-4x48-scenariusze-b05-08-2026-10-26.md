# Etap 4x48 — scenariusze praktyczne B-05–08

- Data: 2026-10-26.
- Punkt bazowy: świeży `main` `a2a1a1db342aab73bd03a30c3e0925495f30cb14` (po scaleniu PR #491).
- Zakres: tylko kurs podstawowy ADR.

## Co sprawdzono i poprawiono

Przejrzano trzy scenariusze w każdym z działów B-05–08. Sytuacje, decyzje kierowcy, kroki, typowe błędy, kryteria oceny, podstawy ADR i wnioski dla kursanta już zawierały opis działania i uzasadnienie. Potwierdzona wada dotyczyła zbyt szerokich list `question_ids`: zamiast kilku pytań bezpośrednio związanych z ćwiczeniem część scenariuszy linkowała cały blok pytań działu. Zawężono je do 1–3 pytań, bez zmian banku i kluczy.

| Scenariusz | Powiązane pytania po zmianie | Cel do omówienia |
|---|---|---|
| SC-ADR-B-05 | ADR-B-0169, ADR-B-0585, ADR-B-0594 | dostępność gaśnicy i zgłoszenie zdarzenia |
| SC-ADR-B-06 | ADR-B-0507, ADR-B-0546, ADR-B-0562 | tablica i nalepki czytelne przed wyjazdem |
| SC-ADR-B-07 | ADR-B-0020, ADR-B-0517, ADR-B-0584 | niezgodne lub uszkodzone opakowanie |
| SC-ADR-B-08 | ADR-B-0596, ADR-B-0597, ADR-B-0423 | wyposażenie osobiste i dostępność sprzętu |
| SC-ADR-B-05-02 | ADR-B-0106, ADR-B-0220, ADR-B-0594 | bezpieczne miejsce, opary i informacje dla służb |
| SC-ADR-B-05-03 | ADR-B-0107, ADR-B-0222, ADR-B-0223 | pożar ładowni a niewielki pożar poza ładunkiem |
| SC-ADR-B-06-02 | ADR-B-0016, ADR-B-0507, ADR-B-0170 | porównanie numerów tablicy z dokumentem |
| SC-ADR-B-06-03 | ADR-B-0133, ADR-B-0546, ADR-B-0550 | widoczność oznakowania z zewnątrz |
| SC-ADR-B-07-02 | ADR-B-0020, ADR-B-0517, ADR-B-0584 | obowiązki załadowcy i reakcja na pęknięcie |
| SC-ADR-B-07-03 | ADR-B-0019 | kto zapewnia instrukcje pisemne |
| SC-ADR-B-08-02 | ADR-B-0074, ADR-B-0423, ADR-B-0596 | gaśnica po przeglądzie i dostęp do sprzętu |
| SC-ADR-B-08-03 | ADR-B-0596, ADR-B-0597, ADR-B-0076 | oddzielne elementy ochrony dla członków załogi |

## Kontrola referencji

- Scenariusze zmienione: 12/12.
- Pytania na scenariusz: minimum 1, maksimum 3.
- Nieistniejące ID: 0.
- Pytania z niewłaściwego modułu: 0.
- Bank: 609 pytań, bez zmian; wszystkie statusy pozostają `needs_review`, żadnego `verified`.

## Uwaga dydaktyczna

SC-ADR-B-07-03 dotyczy przekazania instrukcji nowemu członkowi załogi. W dziale B-07 najbliższe tematyczne pytanie dotyczy osoby odpowiedzialnej za przekazanie instrukcji (ADR-B-0019); osobne pytanie o język instrukcji znajduje się w innym dziale. Nie przeniesiono ID między działami ani nie zmieniono przypisania pytań bez potwierdzonej potrzeby.

Lokalne testy repozytorium nie są dostępne przez GitHub Contents API; wymagany jest pełny Quality Gate CI przed scaleniem. Nie zmieniono explanation, poprawnych liter, statusów prawnych ani wskaźnika długości odpowiedzi.
