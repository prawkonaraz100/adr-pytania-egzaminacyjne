# Etap 4x251 — praktyczne decyzje przy małym pożarze

Data: 31.10.2026  
Zakres: wyłącznie kurs podstawowy ADR  
Baza: świeży `main` po PR #720, commit `ef8ec937567b7720932702e1e7f27f318cc25acc`  
Kompetencja: `ADR-B-05-K06`  
Nowy scenariusz: `SC-ADR-B-05-04`

## Uzasadnienie luki

Audyt mapy kompetencji wykazał, że ADR-B-05-K06 („Mały pożar opon, hamulców lub silnika”) ma cztery pytania (ADR-B-0108, 0184, 0223, 0493), ale żaden scenariusz praktyczny nie odwoływał się do tych pytań. W module istniał już scenariusz pożaru przy przestrzeni ładunkowej, lecz sprawdzał inną decyzję — nie rozstrzygał, kiedy załoga może rozważyć użycie gaśnicy przy małym pożarze poza ładunkiem.

## Zmiana

Dodano `SC-ADR-B-05-04`, który prowadzi kursanta przez ocenę małego, początkowego pożaru opon, hamulców lub silnika. Scenariusz wymaga sprawdzenia, czy ogień nie obejmuje ładunku, czy droga odwrotu pozostaje bezpieczna i czy użycie gaśnicy jest właściwe. Jeśli warunki nie są bezpieczne, kursant ma przerwać próbę, oddalić się, ostrzec innych i wezwać służby. Scenariusz nie zachęca do gaszenia pożaru ładunku ani do narażania życia.

- Pytania powiązane: ADR-B-0108, ADR-B-0184, ADR-B-0223, ADR-B-0493.
- Zaktualizowano mapę kompetencji K06, lekcję ADR-B-05 i materiał instruktora.
- Moduł ADR-B-05 ma teraz 4 scenariusze; cały kurs ma 41 scenariuszy (minimum 3 na każdy z 13 działów).
- Nie dodano ani nie zmieniono pytań; bank pozostaje 677 rekordów, wszystkie `needs_review`, zero `verified`.

## Podstawa i ograniczenia

ADR 2025, 5.4.3.4 — instrukcje pisemne opisują działania załogi przy zdarzeniu, w tym granice użycia gaśnicy. Ćwiczenie jest planszowe lub prowadzone na sucho z użyciem szkoleniowej gaśnicy pod nadzorem instruktora; bez prawdziwego ognia i bez rzeczywistych towarów niebezpiecznych. Scenariusz nie zastępuje praktycznego szkolenia z obsługi gaśnicy.

## Stan po partii

- Bank: 677 pytań ADR-B-0001–0677, 677 `needs_review`, 0 `verified`.
- SHA banku bez zmian: `9dbbf511b3b057e3771ee382dda1a768226a916a`.
- Scenariusze: 41, w tym 4 dla ADR-B-05.
- Warianty i klucze egzaminów 001–005 pozostają zgodne z niezmienionym SHA banku.
- Pełny Quality Gate i CI wymagane przed scaleniem PR.
