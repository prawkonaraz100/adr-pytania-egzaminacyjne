# Etap 4x253 — klasyfikacja towaru i kompletność danych przed przewozem

Data: 31.10.2026  
Zakres: wyłącznie kurs podstawowy ADR  
Baza: świeży `main`, bank 678 pytań, ostatni ID `ADR-B-0678`  
Kompetencja: `ADR-B-01-K07` — towary zabronione i dopuszczone do przewozu  
Nowe pytanie: `ADR-B-0679`

## Dlaczego wybrano tę lukę

Mapa kompetencji wskazywała, że ADR-B-01-K07 miała cztery pytania. Istniejące rekordy sprawdzały ogólną potrzebę klasyfikacji, położenie numeru UN i nazwy przewozowej w tabeli A oraz reakcję na jawny zakaz przewozu. Brakowało pytania, które wprost rozdziela odpowiedzialność nadawcy za klasyfikację od obowiązku przewoźnika sprawdzenia dopuszczenia towaru i kompletności informacji przed rozpoczęciem przewozu.

## Dodane pytanie

- **ADR-B-0679** — kierowca otrzymuje jedynie nazwę handlową nowego materiału, bez klasyfikacji i wymaganych danych ADR. Pytanie sprawdza, czy kursant wie, że nie wolno samodzielnie zgadywać numeru UN ani rozpoczynać przewozu z brakami; należy uzyskać od nadawcy prawidłową klasyfikację i komplet informacji.
- Klucz: **B**.
- Explanation: **375 znaków, 3 zdania**. Najpierw wyjaśnia rolę nadawcy i przewoźnika w praktyce, potem odrzuca zgadywanie i odkładanie braków na później, na końcu podaje podstawę ADR.
- Długości A/B/C: **119/108/117** znaków. Poprawna odpowiedź nie jest najdłuższa.
- Status: `needs_review`; nie zmieniono żadnego statusu na `verified`.

## Podstawa prawna

- ADR 2025, **1.4.2.1.1(a)** — nadawca zapewnia, że towary niebezpieczne są sklasyfikowane i dopuszczone do przewozu zgodnie z ADR.
- ADR 2025, **1.4.2.2.1(a)–(b)** — przewoźnik sprawdza dopuszczenie towaru oraz to, czy nadawca dostarczył wymagane informacje i dokumenty przed przewozem.
- ADR 2025, **1.4.2.2.3** — jeżeli przewoźnik stwierdzi naruszenie wymagań, nie powinien rozpoczynać przewozu do czasu usunięcia nieprawidłowości.
- ADR 2025, **5.4.1.1.1** — zakres informacji wymaganych w dokumencie przewozowym.
- Źródło urzędowe: ADR 2025, Dz.U. 2025 poz. 642, udostępnienie tomu I PL przez Ministerstwo Infrastruktury: https://www.gov.pl/attachment/8856b22a-bfd8-4567-8386-b9709bba8da7 . Strona MI wskazuje, że źródłem prawa jest Umowa ADR ogłoszona w Dzienniku Ustaw: https://www.gov.pl/web/infrastruktura/towary-niebezpieczne .

Pytanie nie przenosi obowiązku klasyfikacji na kierowcę. Nie sugeruje też, że przewoźnik musi samodzielnie przeprowadzać klasyfikację chemiczną; sprawdza podział obowiązków i reakcję na brak danych. Pełne porównanie treści pytania z każdym elementem polskiego tekstu oraz niezależna recenzja specjalisty pozostają otwarte.

## Synchronizacja #646

- Bank: 679 pytań, ID `ADR-B-0001–0679`; SHA: `5df8cb5200a2c357cdcc04959893969d8ca448a0`.
- Kompetencja K07 ma 5 przypisanych pytań; moduł ADR-B-01 ma 50 pytań.
- Zaktualizowano warianty i klucze egzaminów próbnych 001–005 do bieżącego SHA banku. Nowe pytanie nie zostało sztucznie dopisane do zamrożonych zestawów egzaminacyjnych; zachowano ich zestawy pytań i zgodność kluczy.
- Dodano snapshot sekwencyjny `review/sequential/679-679.json` i snapshot prawny `review/legal-clauses/679-679.json`.
- Dopisano rekord do ledgeru źródeł prawnych i osobny wpis w rejestrze specjalisty `review/specialist/REJESTR-0679-0679.md`.
- Oba manifesty pakietów specjalisty wskazują 679 rekordów, 679 `needs_review`, 0 `verified`, nowy SHA oraz snapshoty 679.

## Metryki po dodaniu pytania

- Bank: **679** pytań; wszystkie `needs_review`, **0 verified**.
- Rozkład poprawnych odpowiedzi: **A=232, B=231, C=216**.
- Poprawna odpowiedź jest jedyną najdłuższą w **72/679 = 10,60%** rekordów (limit projektu: 18%).
- Liczebność modułu ADR-B-01: **50** pytań.

## Testy i status

Zmiana jest ograniczona do kursu podstawowego. Zaktualizowano testy regresyjne liczby pytań i macierzy pokrycia; wymagany jest pełny PASS Quality Gate na PR przed scaleniem. Statusy prawne pozostają robocze i nie stanowią zatwierdzenia przez specjalistę.
