# Kontrola druga — ADR-B-0331–0345

**Wynik: 0 OK / 15 POPRAW / 0 BLOKUJ.**

## Rozstrzygnięcia

- **Osiem duplikatów zastąpiono nowymi tematami w tej samej kompetencji:** 0334 — UN 3509 i PS 663; 0336 — próbka do badań i tymczasowa klasyfikacja; 0337 — mieszanina węglowodorów z PCB, UN 2315; 0338 — roztwór acetonu o innej grupie pakowania niż UN 1090; 0339 — limit 2,5 kg dla próbki; 0341 — opakowanie wewnętrzne a pojęcie przedmiotu; 0343 — niedopuszczenie roztworów utleniających o właściwościach wybuchowych; 0345 — próg S16 wynoszący 500 kg.
- **Siedem pytań przeredagowano w dotychczasowym podtemacie:** 0331 — klasyfikacja według składnika o największym zagrożeniu przy nadmiernym koszcie badań; 0332 — pierwszeństwo klasy 2 (c) przed klasą 6.1 (h); 0333 — amina klasy 3, II GP i klasy 8, I GP według tabeli 2.1.3.10; 0335 — wiedza nadawcy z uwzględnieniem danych technicznych i bezpieczeństwa; 0340 — zastrzeżenie w 2.1.3.5.3(h); 0342 — pierwszeństwo klasy 7 przed klasą 6.2; 0344 — wybór szczegółowej pozycji UN 1987 przed ogólną UN 1993.
- **Klucze:** zachowano wszystkie litery: 0331 B, 0332 A, 0333 A, 0334 B, 0335 A, 0336 B, 0337 A, 0338 B, 0339 B, 0340 B, 0341 C, 0342 A, 0343 B, 0344 C, 0345 A.
- **Kompetencje:** bez zmian; 0331–0344 pozostają w ADR-B-03-K06, a 0345 w ADR-B-04-K06. Obrazki pozostają null. Wszystkie rekordy mają `needs_review`, `checked_at=null`, `reviewer=null`.

## Uwagi korygujące do kontroli pierwszej

Raport pierwszej kontroli zawyżył liczbę pytań OK: 0332, 0333, 0340 i 0342 nie spełniały kontroli jakości odpowiedzi. W szczególności wykryto odpowiedzi z samymi numerami przepisów, klucz będący jedyną najkrótszą odpowiedzią, opcje przekraczające 80 znaków oraz treść pytania podpowiadającą klucz. Pytanie 0345 było duplikatem wcześniejszych pytań o kolejność i miejsca postoju według 8.4.1; samo dopisanie zakresu przepisów nie usuwałoby duplikatu.

## Synchronizacja i stan

- Bank po wdrożeniu: 780 pytań; blob SHA `d44c95488d28507ffc3fa901d14b7d20cdd9fb38`.
- Wskaźnik „poprawna = jedyna najdłuższa”: **35/780 = 4,49%**; maksimum działu: **7,87%**.
- Licznik pytań bez porównania dosłownego: **435**.
- Odświeżono warianty i klucze egzaminów próbnych 001, 002, 003 i 005; SHA źródłowego banku zaktualizowano we wszystkich 10 plikach 001–005.
- Snapshoty sequential/legal, ledger, rejestry specjalistyczne, manifesty, sumy SHA i testy regresyjne zsynchronizowano.
- To wdrożenie i zielone CI nie są formalnym zatwierdzeniem eksperckim ani prawnym. Status `verified` pozostaje niedopuszczony.
