# ETAP 4t — przegląd pokrycia programu ADR podstawowego

- Data audytu: 2026-10-25.
- Bazowy `main`: `7d58e74aa41c311df0334819c93e62b76a85ee57` (odczyt z GitHuba).
- Zakres: wyłącznie kurs początkowy podstawowy ADR; bez kursu cystern.
- Źródła: [polski program kursu, załącznik nr 1 do Dz.U. 2021 poz. 2150](https://eli.gov.pl/api/acts/DU/2021/2150/text.html) oraz [ADR 2025, punkt 8.2.2.3.2](https://unece.org/adr-2025-files).
- Przed zmianą: 566 pytań; 103/103 celów teoretycznych miało co najmniej 3 pytania, brak nieistniejących ID w mapie; wszystkie pytania `needs_review`, zero `verified`.

## 1. Polski program — 13 punktów

Przyjęta ocena ilościowa: **wystarczające** = co najmniej 3 pytania w module. To próg redakcyjny, nie wymóg prawny ani dowód pełnego pokrycia jakościowego.

| Punkt programu (zał. 1) | Dział | Liczba pytań | Ocena ilościowa | Uwaga jakościowa |
|---|---|---:|---|---|
| a. Wymagania ogólne, definicje, szkolenie, wyłączenia | ADR-B-01 | 35 | Wystarczające | Rozdzielać podstawy od szczególnych warunków zwolnień |
| b. Główne rodzaje zagrożeń i rozpoznawanie oznaczeń | ADR-B-02 | 56 | Wystarczające | Łączyć definicje, nalepki i sytuacje |
| c. Ochrona środowiska i odpady | ADR-B-03 | 49 | Wystarczające | Kompetencja o kanalizacji zawiera podobne scenariusze; warto rozszerzyć formy ćwiczeń |
| d. Zapobieganie zdarzeniom i środki bezpieczeństwa | ADR-B-04 | 44 | Wystarczające | Łączyć zakazy z czynnościami kierowcy |
| e. Postępowanie po wypadku, pierwsza pomoc i sprzęt ochronny | ADR-B-05 | 40 | Wystarczające dla teorii | Test nie zastępuje rzeczywistych ćwiczeń P1–P3 |
| f. Oznakowanie, nalepki i tablice pomarańczowe | ADR-B-06 | 45 | Wystarczające | Utrzymać przykłady wizualne i wyjątki |
| g. Odpowiedzialność kierowcy i innych uczestników | ADR-B-07 | 43 → 46 | Wystarczające po uzupełnieniu | Dodano cel odpowiedzialności cywilnej z ADR 8.2.2.3.2(k) |
| h. Wyposażenie techniczne i ochronne pojazdu | ADR-B-08 | 40 | Wystarczające | Rozdzielać wymagania zależne od pojazdu i przewozu |
| i. Manipulowanie, układanie, załadunek/rozładunek, ładunki mieszane i mocowanie | ADR-B-09 | 46 | Wystarczające | Szeroki temat; różne operacje, nie tylko zakazy wspólnego załadunku |
| j. Przewóz kombinowany | ADR-B-10 | 55 | Wystarczające | Każdy wyjątek zachowuje warunki odcinka drogowego |
| k. Tunele i zachowanie w zagrożeniu | ADR-B-11 | 35 | Wystarczające | Ograniczenia trasy i scenariusz awaryjny |
| l. Ochrona towarów niebezpiecznych | ADR-B-12 | 43 | Wystarczające | Rozróżniać ochronę przed kradzieżą od zwykłego bezpieczeństwa |
| m. Dokumentacja przewozowa | ADR-B-13 | 35 | Wystarczające | Nadal potrzebna kontrola dokumentów warunkowych |

## 2. Crosswalk do ADR 2025, 8.2.2.3.2

| Temat ADR | Mapa kursu | Liczba pytań | Ocena |
|---|---|---:|---|
| (a) Wymagania ogólne | B-01 | 35 | Wystarczające ilościowo |
| (b) Główne rodzaje zagrożeń | B-02 | 56 | Wystarczające ilościowo |
| (c) Ochrona środowiska i odpady | B-03 | 49 | Wystarczające ilościowo |
| (d) Zapobieganie i środki bezpieczeństwa | B-04 | 44 | Wystarczające ilościowo |
| (e) Postępowanie po wypadku, pierwsza pomoc i sprzęt ochronny | B-05 | 40 | Wystarczające dla teorii; praktyka osobno |
| (f) Oznakowanie, nalepki i tablice | B-06 | 45 | Wystarczające ilościowo |
| (g) Co kierowca powinien i czego nie powinien robić | B-07 | 46 po zmianie | Wystarczające ilościowo |
| (h) Cel i działanie wyposażenia technicznego | B-08 | 40 | Wystarczające ilościowo |
| (i) Zakazy wspólnego załadunku | B-09 | 46 | Wystarczające ilościowo |
| (j) Środki ostrożności przy załadunku/rozładunku | B-09 | 46 | Wystarczające ilościowo |
| (k) Ogólne informacje o odpowiedzialności cywilnej | B-07-K07 | 3 nowe pytania | Uzupełniono wyodrębniony cel |
| (l) Transport multimodalny | B-10 | 55 | Wystarczające ilościowo |
| (m) Przemieszczanie i układanie sztuk przesyłek | B-09 | 46 | Wystarczające ilościowo |
| (n) Ograniczenia tunelowe i zachowanie w sytuacji awaryjnej | B-11 | 35 | Wystarczające ilościowo |

## 3. Potwierdzona luka i działanie

Mapa nie miała osobnego celu dotyczącego odpowiedzialności cywilnej, mimo że temat wskazuje ADR 8.2.2.3.2(k). Pytania o obowiązki nadawcy, przewoźnika i kierowcy nie dowodzą, że kursant odróżnia odpowiedzialność za szkodę wyrządzoną z winy od odpowiedzialności za niewykonanie zobowiązania.

Dodano cel `ADR-B-07-K07` i pytania `ADR-B-0567–0569`: odpowiedzialność za szkodę (Kodeks cywilny, art. 415), niewykonanie zobowiązania (art. 471) i brak automatyzmu w przypisywaniu osobistej odpowiedzialności. Podstawy: ADR 8.2.2.3.2(k), [Kodeks cywilny — tekst jednolity Dz.U. 2026 poz. 795](https://eli.gov.pl/eli/DU/2026/795/ogl). To ogólne ujęcie; konkretna odpowiedzialność może zależeć od umowy, rodzaju przewozu i ustalonych okoliczności.

Wszystkie nowe wyjaśnienia mają 300–500 znaków, a poprawna odpowiedź nie jest jedyną najdłuższą opcją. Pytania pozostają `needs_review`; wymagają niezależnej recenzji specjalisty i kontroli źródeł.

## 4. Ograniczenia

- Bank nie ma formalnego pola określającego typ pytania. Dlatego nie przedstawiam automatycznej heurystyki jako potwierdzonej oceny różnorodności definicji, scenariuszy, obliczeń i pytań obrazkowych.
- Przegląd wykrył konkretne pominięcie tematu cywilnej odpowiedzialności; nie oznacza to, że wszystkie wyjątki prawne zostały niezależnie sprawdzone.
- Próg „minimum 3 pytania” jest wewnętrzną regułą redakcyjną. Umiejętności praktyczne nadal wymagają realnych zajęć z instruktorem.

## 5. Stan po zmianie

- Bank: 569 pytań, wszystkie `needs_review`, 0 `verified`.
- Cele teoretyczne: 104; każdy ma pytania robocze.
- Dział B-07: 46 pytań.
- Wskaźnik „poprawna = najdłuższa” nie rośnie przez nowe rekordy; wymagany PASS CI przed scaleniem.
