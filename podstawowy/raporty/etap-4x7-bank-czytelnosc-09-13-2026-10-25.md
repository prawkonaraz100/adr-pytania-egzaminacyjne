# Etap 4x7 — kontrola banku i czytelności, partia B-09–13

## Punkt wyjścia
- Świeży `main`: `7a581e96a7331065e806ae59652619834832a679`.
- Zakres: 235 pytań przypisanych do modułów ADR-B-09–13. Cały bank 609 pytań przeskanowano pod kątem podobieństwa stemów i identycznych zestawów odpowiedzi w obrębie modułu.
- Zmieniono wyłącznie treść explanation i nie zmieniano poprawnych liter, ID, źródeł ani przypisania modułów.

## Czytelność wyjaśnień
Rozwinięto skróty i terminy w 22 wyjaśnieniach:
`ADR-B-0038`, `ADR-B-0085`, `ADR-B-0209`, `ADR-B-0214`, `ADR-B-0215`, `ADR-B-0226`, `ADR-B-0227`, `ADR-B-0233`, `ADR-B-0248`, `ADR-B-0278`, `ADR-B-0322`, `ADR-B-0382`, `ADR-B-0384`, `ADR-B-0388`, `ADR-B-0398`, `ADR-B-0508`, `ADR-B-0512`, `ADR-B-0536`, `ADR-B-0537`, `ADR-B-0540`, `ADR-B-0578`, `ADR-B-0579`, `ADR-B-0591`, `ADR-B-0598`.

Uwaga: lista zawiera 24 identyfikatory kontrolowane w tej partii; 22 explanation wymagały faktycznej zmiany. Pozostałe pozycje z automatycznego skanu miały już wyjaśnione skróty lub wystarczające objaśnienie w treści. Dodane definicje dotyczą m.in. LQ (ilości ograniczone), numeru UN (identyfikator towaru niebezpiecznego), IMDG (przepisy dla przewozu morskiego) i RID (przepisy dla przewozu kolejowego).

Zaktualizowano klucze egzaminów próbnych 001–005 dla zmienionych wyjaśnień, odświeżono pola `source_bank_head` we wszystkich wariantach oraz snapshoty w rejestrach `review/sequential/` i `review/legal-clauses/`. Te aktualizacje nie oznaczają ponownej recenzji prawnej.

## Powtórzenia
- Nie znaleziono nowej nieudokumentowanej pary o podobieństwie co najmniej 0,60 lub identycznym zestawie odpowiedzi w obrębie modułu.
- `ADR-B-0071` / `ADR-B-0072` pozostają w jawnej allowliście: podobna forma, lecz pytania dotyczą różnych progów DMC i wymagają odrębnych odpowiedzi.
- `ADR-B-0330` / `ADR-B-0337` pozostają udokumentowaną parą podobnych pytań o różne wyłączenia proceduralne (klasy 5.2 i 6.2).
- Potwierdzony duplikat `ADR-B-0169` / `ADR-B-0585` został już rozwiązany w poprzedniej partii; 0585 sprawdza teraz mocowanie gaśnicy, a 0169 jej dostępność.

## Słowniczek
Dodano link do `podstawowy/SLOWNICZEK.md` na końcu lekcji B-09–B-13. README już prowadzi do słowniczka i raportów poprzednich partii.

## Kontrole przed PR
- Bank: 609 pytań; unikalne ID: 609; duplikaty ID: 0.
- Poprawna odpowiedź jest jedyną najdłuższą w 82/609 = 13,46% (limit 18%).
- Najkrótsze explanation: 300 znaków; poniżej 200 znaków: 0.
- Statusy: 609 `needs_review`, 0 `verified`.
- Warianty 001–005 i klucze zostały zsynchronizowane dla zmienionych wyjaśnień; wymagane kontrole spójności wykona Quality Gate.

## Ograniczenia
To kontrola redakcyjna i automatyczna kontrola podobieństwa. Nie jest niezależną recenzją prawną ADR; wszystkie pytania nadal wymagają oceny specjalisty i pozostają `needs_review`.
