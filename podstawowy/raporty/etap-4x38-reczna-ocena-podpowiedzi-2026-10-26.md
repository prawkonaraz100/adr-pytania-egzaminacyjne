# Etap 4x38 — końcowa ręczna ocena kandydatów podpowiedzi leksykalnych

- Data: 26.10.2026.
- Punkt wyjścia: świeży `main` po PR #480, commit `9026369acd2b29749185cf691018f35f815a96d6`.
- Zakres: kurs podstawowy, bank 609 pytań.

## Ręczna ocena kandydatów

Po poprawkach 4x36–4x37 ponowne skanowanie wykrywa **37** kandydatów, w których fraza z treści pytania pojawia się również w poprawnej odpowiedzi, ale nie w dystraktorach. Po ręcznym przeglądzie uznano, że pozostałe powtórzenia wynikają z koniecznej terminologii, warunku sytuacyjnego albo treści reguły. Nie przeredagowywano ich automatycznie, ponieważ usunięcie terminu mogłoby uczynić pytanie nieprecyzyjnym lub zmienić badany wymóg.

Przykładowe fałszywe alarmy:
- **ADR-B-0009 — „przed ponownym załadunkiem”:** to warunek czasowy wymagania czyszczenia po wycieku; nie ujawnia samoistnie, co trzeba zrobić.
- **ADR-B-0034 / 0300 / 0416 / 0519 — „dokument tożsamości” / „członek załogi”:** nazwy są kluczowymi pojęciami wymogu identyfikacji; odpowiedzi rozróżniają, kto ma mieć dokument i jaki dokument jest potrzebny.
- **ADR-B-0065 / 0264 — „ograniczenie tunelowe”:** termin jest przedmiotem pytania, a odpowiedzi różnią się interpretacją znaku `(-)`.
- **ADR-B-0184 — „początkowa faza”:** to warunek bezpieczeństwa określający, kiedy można w ogóle rozważyć użycie gaśnicy; pozostałe opcje proponują działania niebezpieczne.
- **ADR-B-0450 / 0467 — „oznakowanie i nalepki” / „MARINE POLLUTANT”:** są to nazwy regulacyjne, które trzeba rozpoznać, a nie niezamierzone podpowiedzi.
- **ADR-B-0571 — „wynik przekracza”:** poprawność wymaga wykonania obliczenia, nie tylko dopasowania słów.

## Dwa potwierdzone przypadki poprawione w tej partii

1. **ADR-B-0431 — kod tunelowy `(-)`:** po wcześniejszej zmianie scenariusza poprawna odpowiedź nadal powtarzała frazę „znak drogowy” ze stemu. Zmieniono ją na „Nie traktować kodu (-) jako zwolnienia z pozostałych ograniczeń na trasie”. Zachowano literę C, ID i dział. Explanation: 318 znaków. Podstawa: ADR 8.6.3.1.
2. **ADR-B-0334 — pozycja i.n.o.:** poprawna odpowiedź powtarzała zwrot „najbardziej szczegółowa właściwa pozycja” z treści. Zmieniono odpowiedź na „Użyć wpisu najlepiej dopasowanego do rzeczywistych właściwości odpadu” i skrócono stem do sytuacji z dwoma możliwymi wpisami. Zachowano literę B, ID i dział. Explanation: 392 znaki. Podstawa: ADR 2.1.3.6.

## Synchronizacja i metryki

- Zaktualizowano snapshoty sekwencyjne i klauzulowe dla ADR-B-0334 i ADR-B-0431.
- Wariant 005 i jego klucz zostały zsynchronizowane dla obu pytań; warianty i klucze 001–005 wskazują bieżący blob banku `8a16afb47c5d5a9e460092b7e474b4a3e8a5a8d9`.
- Bank: 609 pytań, 0 duplikatów ID; 609 `needs_review`, 0 `verified`.
- Explanation poniżej 300 znaków: 0.
- „Poprawna odpowiedź jest jedyną najdłuższą”: 72/609 = 11,82% globalnie; wszystkie działy pozostają poniżej 18%.

## Ograniczenia

Skan leksykalny jest heurystyką. Pozostałe 37 przypadków nie zostało uznane za potwierdzone podpowiedzi po ręcznej ocenie; mogą wymagać ponownego przeglądu przy zmianie brzmienia pytań. Nie jest to formalna recenzja prawna. Nie rozpoczęto kursu cystern ani innej specjalizacji.
