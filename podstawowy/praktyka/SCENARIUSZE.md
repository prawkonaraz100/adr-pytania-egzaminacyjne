# ADR podstawowy — scenariusze praktyczne dla instruktora

**Status: materiał szkoleniowy do odbioru instruktorskiego, nie zaliczenie szkolenia.** Program odwołuje się do ćwiczeń praktycznych wymaganych w załączniku nr 1 do rozporządzenia o kursach ADR (Dz.U. 2021 poz. 2150) i do instrukcji pisemnych ADR 2025, 5.4.3.4. Szczegóły należy zatwierdzić z osobą uprawnioną do prowadzenia zajęć.

**Ćwiczenie łączące cztery działy:** [karta kontroli przed wyjazdem](KARTA-KONTROLI-PRZED-WYJAZDEM.md) — B-01, B-06, B-08 i B-13, krok po kroku na fikcyjnej dokumentacji.

**Instruktor:** do każdego scenariusza korzystaj z [karty oceny i omówienia](KARTA-OCENY-SCENARIUSZY.md) — zawiera kolejność przeprowadzenia ćwiczenia, typowe błędy i sposób przekazania informacji zwrotnej, bez udawania formalnego zaliczenia zajęć.

## Scenariusze dla kursanta — działy B-01–B-03

Scenariusze w pliku `scenariusze-13-dzialow.json` są ćwiczeniami na fikcyjnych dokumentach i sytuacjach. **Kolejność pracy kursanta:** najpierw przeczytaj `situation`, odpowiedz własnymi słowami na `learner_question`, a dopiero potem porównaj swoją decyzję z listą `steps`, typowymi błędami `common_mistakes`, wytłumaczeniem `learner_takeaway` i odpowiednimi `question_ids`. Dzięki temu poznajesz powód decyzji, a nie tylko gotowe kroki. W każdym przypadku kursant powinien powiedzieć **co robi**, **czego nie robi** i **dlaczego**. Instruktor może użyć pól `common_mistakes`, `legal_basis` i `learner_takeaway` jako krótkiej karty omówienia. Nie należy traktować samej odpowiedzi w quizie jako zaliczenia praktyki.

### B-01 — wyłączenia i dopuszczalność przewozu
- `SC-ADR-B-01`: sprawdź numer UN, kategorię, ilość, LQ/EQ, dopuszczalność przewozu i wymagane zaświadczenie.
- `SC-ADR-B-01-02`: wyjaśnij, dlaczego mała paczka nie oznacza automatycznego zwolnienia.
- `SC-ADR-B-01-03`: nie ruszaj z brakującymi danymi; polecenie dyspozytora nie uchyla ADR.

### B-02 — klasy i rozpoznawanie zagrożeń
- `SC-ADR-B-02`: przy klasie 4.3 nie zmywaj zabrudzenia wodą.
- `SC-ADR-B-02-02`: nie dotykaj nieznanej plamy i nie neutralizuj jej domowymi środkami.
- `SC-ADR-B-02-03`: porównaj numer UN, nazwę, klasę i nalepki; rozbieżność wyjaśnij przed przyjęciem.

### B-03 — wycieki, środowisko i odpady
- `SC-ADR-B-03`: nie wąchaj, nie dotykaj i nie spłukuj cieczy do kanalizacji.
- `SC-ADR-B-03-02`: zachowaj dystans i przekaż służbom tylko sprawdzone obserwacje.
- `SC-ADR-B-03-03`: przed kolejnym załadunkiem sprawdź pozostałości i wymagania czyszczenia.

Powiązane question IDs, kryteria oceny i podstawy ADR znajdują się w rekordach scenariuszy. Wszystkie 39 scenariuszy sprawdzono pod kątem istnienia pytań i zgodności ich `module_id` z działem scenariusza.

## Scenariusze dla kursanta — działy B-04–B-06

W każdej symulacji kursant powinien wyjaśnić, co robi, czego nie robi i dlaczego. Pola `common_mistakes`, `legal_basis` i `learner_takeaway` w pliku scenariuszy pomagają instruktorowi omówić błąd bez żargonu. Scenariusze są ćwiczeniami na fikcyjnych danych i nie dowodzą wykonania zajęć praktycznych.

### B-04 — załadunek, silnik i nadzór postoju
- `SC-ADR-B-04`: oddziel zakaz palenia od zasady dotyczącej silnika i sprawdź, czy postój podlega nadzorowi.
- `SC-ADR-B-04-02`: e-papieros i silnik pracujący tylko dla wygody nie są automatycznymi wyjątkami; pytania odnoszą się wyłącznie do palenia i pracy silnika.
- `SC-ADR-B-04-03`: wybierz miejsce postoju według warunków ADR, nie wyłącznie według odległości.

### B-05 — awaria, gaśnice i pierwsza pomoc
- `SC-ADR-B-05`: nieznana przyczyna awarii nie zwalnia z wezwania pomocy i sprawdzenia dostępności sprzętu.
- `SC-ADR-B-05-02`: nie wąchaj substancji i nie zgaduj jej składu.
- `SC-ADR-B-05-03`: nie gaś pożaru obejmującego przedział ładunkowy z towarami niebezpiecznymi.

### B-06 — tablice pomarańczowe i nalepki
- `SC-ADR-B-06`: porównaj oznakowanie z dokumentami i wpisem ADR.
- `SC-ADR-B-06-02`: odróżnij numer UN od numeru rozpoznawczego zagrożenia.
- `SC-ADR-B-06-03`: nie odjeżdżaj z nalepką zasłoniętą lub nieczytelną.

## Scenariusze dla kursanta — działy B-07–B-09

Każda symulacja ma pomóc kursantowi wyjaśnić decyzję własnymi słowami: co robi, czego nie robi i dlaczego. W rekordach scenariuszy pola common_mistakes, legal_basis i learner_takeaway służą do krótkiego omówienia po ćwiczeniu. Nie zastępują prawdziwych zajęć praktycznych.

### B-07 — role uczestników i opakowanie
- SC-ADR-B-07: rozpoznaj niezgodne opakowanie i nie przekazuj go do przewozu.
- SC-ADR-B-07-02: nie przerzucaj całej odpowiedzialności na nadawcę; zatrzymaj załadunek uszkodzonej sztuki.
- SC-ADR-B-07-03: sprawdź, czy instrukcje pisemne są dostępne i zrozumiałe dla każdego członka załogi.

### B-08 — wyposażenie
- SC-ADR-B-08: sprawdź wyposażenie pojazdu i każdej osoby osobno.
- SC-ADR-B-08-02: sprawdź nie tylko obecność gaśnicy, ale też stan, mocowanie i dostępność.
- SC-ADR-B-08-03: środki ochrony osobistej nie zastępują się wzajemnie.

### B-09 — kontrola załadunku i mocowanie
- SC-ADR-B-09: oceń pozostałości, opakowania i mocowanie przed wyjazdem.
- SC-ADR-B-09-02: nieznane pozostałości wyjaśnij przed kolejnym załadunkiem.
- SC-ADR-B-09-03: zabezpiecz cały ładunek, w tym ciężkie elementy obok palet, i nie napinaj pasów tak mocno, by uszkadzały opakowania.
## Scenariusze dla kursanta — działy B-10–B-12

Przy każdym ćwiczeniu kursant powinien wyjaśnić własnymi słowami: co sprawdza, dlaczego nie wybiera skrótu i kiedy zatrzymuje czynność. Pola common_mistakes, legal_basis i learner_takeaway w rekordach scenariuszy pomagają przeprowadzić omówienie po ćwiczeniu. To symulacje, nie dowód wykonania zajęć praktycznych.

### B-10 — transport kombinowany
- SC-ADR-B-10: dokument morski nie oznacza automatycznego zwolnienia z wymagań drogowych.
- SC-ADR-B-10-02: sprawdź warunki ADR 1.1.4.2 i nie zgaduj brakujących danych.
- SC-ADR-B-10-03: porównaj identyfikator kontenera z certyfikatem i dokumentem przewozowym.

### B-11 — tunele i planowanie trasy
- SC-ADR-B-11: ustal kod dla całej jednostki i porównaj go ze znakiem tunelu.
- SC-ADR-B-11-02: nawigacja nie uchyla zakazu przejazdu.
- SC-ADR-B-11-03: nie wybieraj najłagodniejszego kodu; zastosuj regułę ADR dla całego ładunku.

### B-12 — ochrona przewozu
- SC-ADR-B-12: sprawdź plan ochrony i zweryfikuj odbiorcę.
- SC-ADR-B-12-02: zmianę postoju uzgodnij zgodnie z procedurą ochrony.
- SC-ADR-B-12-03: numer zlecenia nie zastępuje potwierdzenia tożsamości przewoźnika; scenariusz i pytania dopasowano do ADR 1.10.1.2.
## Scenariusze dla kursanta — dział B-13

Przy każdym ćwiczeniu kursant powinien powiedzieć, co sprawdza, dlaczego nie zgaduje brakujących danych i co musi być dostępne przed wyjazdem. Pola common_mistakes, legal_basis i learner_takeaway w rekordach scenariuszy pomagają omówić odpowiedź prostym językiem. Scenariusze są symulacjami, nie dowodem realizacji zajęć praktycznych.

- SC-ADR-B-13: porównaj dokument przewozowy, instrukcje pisemne i wymagania dla odcinka drogowego.
- SC-ADR-B-13-02: nie zgaduj brakujących danych i nie odkładaj ich do uzupełnienia po wyjeździe.
- SC-ADR-B-13-03: instrukcje pisemne muszą być zrozumiałe dla każdego członka załogi.
## Zakres i zasada bezpieczeństwa

Ćwiczenia muszą być prowadzone w warunkach odpowiednich do nadzorowanych zajęć. Nie wykorzystuje się prawdziwej niebezpiecznej substancji ani nie naraża kursantów na działanie ognia, oparów lub innych zagrożeń. Ćwiczenia ogniowe odbywają się wyłącznie na przygotowanym stanowisku szkoleniowym z zabezpieczeniem i instruktorem.

**Testy online sprawdzają wiedzę. Nie dowodzą, że kursant praktycznie użył gaśnicy, udzielił pomocy lub ćwiczył zachowanie w wypadku.**

## Ćwiczenie P1 — zastosowanie sprzętu gaśniczego

**Cel:** rozpoznanie, kiedy kierowca może rozważyć użycie gaśnicy, a kiedy powinien przerwać działanie i ewakuować się.

**Przebieg:** instruktor pokazuje typy gaśnic i wymagane warunki ich użycia, następnie demonstruje prawidłowe użycie na stanowisku szkoleniowym; kursant ćwiczy pod nadzorem, bez działań improwizowanych.

**Ocena:** kursant rozpoznaje, że nie podejmuje gaszenia pożaru obejmującego przedział ładunkowy; potrafi określić ograniczenia własnego bezpieczeństwa i potrafi użyć sprzętu zgodnie z instrukcją instruktora.

**Podstawa:** ADR 5.4.3.4 i 8.1.4; program części praktycznej zał. 1.

## Ćwiczenie P2 — pierwsza pomoc po zdarzeniu ADR

**Cel:** prawidłowo ocenia własne bezpieczeństwo, rozpoznaje potencjalną strefę skażenia, wzywa pomoc i dobiera czynności pierwszej pomocy adekwatne do sytuacji oraz posiadanych umiejętności.

**Przebieg:** instruktor przedstawia scenariusz urazu z ryzykiem skażenia, uczy bezpiecznego postępowania, wzywania służb, komunikacji i właściwych czynności pierwszej pomocy na manekinie lub stanowisku dydaktycznym. Nie wykonuje się ćwiczeń na prawdziwym niebezpiecznym materiale.

**Ocena:** kursant nie naraża siebie ani innych, potrafi przekazać dyspozytorowi informacje o miejscu, towarze i zdarzeniu oraz działać zgodnie z instrukcją instruktora.

**Podstawa:** program zajęć praktycznych zał. 1, ADR 5.4.3.4.

## Ćwiczenie P3 — awaria pojazdu / zdarzenie drogowe

**Cel:** rozpoznaje zagrożenie i poprawną kolejność działań oraz rolę dokumentów i wyposażenia.

**Przebieg:** na przygotowanym stanowisku kursant otrzymuje kartę sytuacji, dokument przewozowy i czterostronicowe instrukcje pisemne. Ma wskazać bezpieczne działania: zabezpieczenie pojazdu i miejsca, uniknięcie źródeł zapłonu, powiadomienie służb, ostrzeżenie osób postronnych, przekazanie informacji ratownikom. Wszystkie czynności są symulowane.

**Ocena:** kursant zachowuje bezpieczny dystans, potrafi wskazać konieczne wyposażenie, właściwie komunikuje zdarzenie i nie podejmuje samowolnej akcji na nieznanej substancji.

**Podstawa:** ADR 5.4.3.4, 8.1.5, 8.3; program praktyczny zał. 1.

## Protokół odbioru ćwiczeń — pola wymagające rzeczywistego uzupełnienia

| Pole | Wartość |
|---|---|
| Ośrodek prowadzący kurs | **do uzupełnienia przez rzeczywisty OSK** |
| Data i miejsce ćwiczenia | **do uzupełnienia** |
| Imię i kwalifikacja instruktora | **do uzupełnienia** |
| Lista obecnych kursantów / potwierdzenie tożsamości | **do uzupełnienia** |
| Rodzaj ćwiczenia P1 / P2 / P3 | **do uzupełnienia** |
| Ocena działania i uwagi instruktora | **do uzupełnienia** |
| Dokumentacja wymagana obowiązującym prawem | **do uzupełnienia** |
| Podpis/potwierdzenie przez prowadzącego | **do uzupełnienia** |

Nie wolno tworzyć fikcyjnego potwierdzenia ani automatycznie zamieniać wyniku quizu na zaliczenie zajęć.

## Pytania do wiedzy przed zajęciami

- Dlaczego nie wolno gasić przez załogę pożaru ładowni?
- Kiedy kierowca może próbować zapobiec przedostaniu się materiału do kanalizacji?
- Jak bezpiecznie przekazać ratownikom dokument przewozowy?
- Jakie elementy wyposażenia są na członka załogi, a jakie na pojazd?
- Dlaczego trzeba pozostawać po stronie nawietrznej?

Powiązane kompetencje: `ADR-B-05-K13`, `ADR-B-05-K14`, `ADR-B-05-K15`.

## Źródła

- [Program kursu ADR (Dz.U. 2021 poz. 2150), załącznik nr 1](https://eli.gov.pl/api/acts/DU/2021/2150/text.pdf)
- [ADR 2025 — Dz.U. 2025 poz. 642](https://dziennikustaw.gov.pl/DU/2025/642)
- [Sprostowanie — Dz.U. 2025 poz. 1575](https://eli.gov.pl/eli/DU/2025/1575/ogl/pol/pdf)

## Uzupełnienie przygotowania do P1–P3 (23.10.2026; bez zaliczeń)

**P1 — sprzęt gaśniczy:** instruktor pokazuje różnicę między pożarem przedziału ładunkowego (załoga nie gasi) a małym pożarem elementów pojazdu, przy którym sprzęt wolno rozważyć wyłącznie w bezpiecznych warunkach. Pytania przygotowawcze 0222–0223.

**P2 — pierwsza pomoc:** symulacja poszkodowanego przy niezidentyfikowanym wycieku. Kursant najpierw ocenia zagrożenia dla siebie i innych, wzywa pomoc, działa tylko na bezpiecznym stanowisku. Pytania 0220, 0221, 0225.

**P3 — wypadek/awaria:** suchy scenariusz bez substancji: bezpieczne zatrzymanie, środki ostrożności, wezwanie służb, ostrzeganie postronnych. Pytania 0219–0224.

**Ocena praktyczna:** nauczyciel/instruktor wypełnia realny protokół dopiero po wykonanych ćwiczeniach. Test internetowy ani powyższe scenariusze nie są dowodem uczestnictwa czy zaliczenia. Źródło ADR 5.4.3.4, program praktyki Dz.U. 2021 poz. 2150; wymaga prawnej i dydaktycznej recenzji.

## Rozszerzenie P3 — oględziny przed załadunkiem (szkic, 23.10.2026)

Przygotować bezpieczny model pojazdu i atrapy sztuk przesyłek. Kursant rozpoznaje źle zamocowane opakowania, zbyt mocno zaciśnięty pas, niedozwolone piętrzenie i pozostałości po symulowanym wycieku. Powiązane pytania 0235–0240; ADR 7.5.1, 7.5.7, 7.5.8. Scenariusz dydaktyczny nie jest dowodem przeprowadzenia ani zaliczenia ćwiczeń z ramowego programu; kontrola instruktora wymagana.

## Matryca dydaktyczna P1–P3 — doprecyzowanie etapu 2 (23.10.2026)

| Scenariusz | Przygotowanie i stanowisko | Zadania instruktora | Kryteria obserwacji (nie zaliczenie zdalne) |
|---|---|---|---|
| P1 — sprzęt gaśniczy | Bezpieczne, przygotowane stanowisko szkoleniowe, odpowiedni sprzęt i ochrona, bez prawdziwego ładunku ADR | Pokaz, nadzorowanie użycia sprzętu, zatrzymanie ćwiczenia w razie ryzyka | Kursant odróżnia pożar przedziału ładunkowego od małego pożaru pojazdu, zna granice bezpieczeństwa, posługuje się gaśnicą zgodnie z instruktażem |
| P2 — pierwsza pomoc | Manekin lub stanowisko symulacyjne, brak skażenia i rzeczywistego uwolnienia materiału | Ocena bezpieczeństwa miejsca, trening wezwania pomocy, pokaz odpowiednich podstawowych czynności | Kursant nie wchodzi w niebezpieczną strefę, zgłasza informacje, działa w zakresie przeszkolenia |
| P3 — wypadek/awaria | Sucha symulacja miejsca zdarzenia, bez rzeczywistego zagrożenia i ruchu drogowego | Instruktaż alarmowania, ostrzegania i odtwarzania działań z instrukcji pisemnych | Kursant rozpoznaje konieczność bezpiecznego zatrzymania, zachowania strony nawietrznej i współpracy ze służbami |

**Protokół i nadzór:** przed rozpoczęciem instruktor sprawdza środki bezpieczeństwa; po realnym wykonaniu może osobno odnotować datę, miejsce, uczestnika, zakres, obserwacje i swój podpis w istniejącym formularzu powyżej. Nie dopisywać fikcyjnych ocen ani dat. Przebieg i warunki ćwiczenia muszą być zgodne z prawem i programem kursu, a tekst wymaga niezależnej kontroli instruktorskiej. Podstawa do weryfikacji: zał. 1 Dz.U. 2021 poz. 2150 i ADR 2025 5.4.3.4. Żadne pytanie internetowe nie zalicza P1–P3.

## Wariant ćwiczenia instruktorskiego P3 — rozpoznanie ryzyka załadunku (23.10.2026)

Na bezpiecznych atrapach kursant wybiera, które przesyłki wymagają sprawdzenia tabeli wspólnego ładowania (ADR 7.5.2.1), a które ładunki dopuszczenia do przewozu luzem (7.3.1.1). Instruktor ocenia rozumienie procedury, bez fikcyjnego poświadczania wykonania obowiązkowych czynności P1–P3. Brak prawdziwych towarów niebezpiecznych.

## Rozszerzenie P3 — procedura bezpiecznej ewakuacji przy wycieku (projekt 23.10.2026)

Instruktor przedstawia makietę zdarzenia i bezpiecznie zasymulowany rozlew. Kursant wskazuje stronę nawietrzną, źródła zapłonu, strefę bez dostępu dla osób postronnych oraz konieczność wezwania służb; pytania powiązane: ADR-B-0295–0297, ADR 5.4.3.4. Nie używać rzeczywistych materiałów i nie zaliczać zdalnie czynności P1–P3.

## Stanowisko szkoleniowe P3 — rozpoznanie oznakowania i identyfikacja (szkic 23.10.2026)

Instruktor przygotowuje własną, legalnie używaną makietę kontenera z miejscami na nalepki i tablicę „80” oraz sprawdza, czy kursant umie nazwać zagrożenie i właściwe miejsca nalepek. Następnie ćwiczy procedurę kontroli tożsamości załogi przy fikcyjnych danych. Powiązanie ADR-B-0298–0300, ADR 5.3.1.2, 5.3.2.3.2, 1.10.1.4. Brak rzeczywistych towarów, brak automatycznego zaliczenia P1–P3.

## Kryteria obserwacji instruktorskiej P1–P3 (uzupełnienie 23.10.2026)

**P1 — użycie gaśnicy:** instruktor obserwuje, czy kursant (1) rozpoznaje bezpieczne warunki rozpoczęcia ćwiczenia, (2) dobiera sprzęt wskazany przez instruktora, (3) demonstruje chwyt i uruchomienie zgodnie z instruktażem, (4) przerywa działanie na sygnał bezpieczeństwa. Każdy element: `zaliczone / do powtórzenia / nieocenione`, z odnotowaniem konkretnych obserwacji.

**P2 — pierwsza pomoc:** instruktor obserwuje (1) kontrolę bezpieczeństwa miejsca, (2) wezwanie odpowiedniej pomocy, (3) bezpieczne postępowanie z poszkodowanym w zakresie ćwiczenia, (4) właściwe przekazanie informacji służbom. Nie wchodzi się do strefy skażenia i nie wykonuje czynności bez przeszkolenia; ćwiczenie wyłącznie na symulatorze lub pod nadzorem.

**P3 — wypadek i awaria:** instruktor obserwuje (1) bezpieczne zatrzymanie i ocenę miejsca, (2) wybór miejsca osłoniętego od oparów / strony nawietrznej, (3) ostrzeżenie innych i wezwanie służb, (4) wyjaśnienie ograniczeń samodzielnych działań przy wycieku i zapłonie. Łączy ocenę z instrukcjami ADR 5.4.3.4.

**Rejestr oceny:** dla każdego z P1–P3 instruktor wypełnia w rzeczywistych zajęciach: identyfikator kursanta, datę, miejsce, nazwisko instruktora, warunki ćwiczenia, wyniki poszczególnych punktów, uwagi i podpis. Przed zajęciami pole pozostaje puste; w repozytorium nie zapisuje się fikcyjnych zaliczeń. Cała matryca wymaga weryfikacji z obowiązującym urzędowym programem szkolenia i akceptacji kompetentnego instruktora. 

## Kryterium P3: kontrola ochrony postoju i dokumentów (23.10.2026)

Instruktor przedstawia fikcyjną kartę przewozu towaru dużego ryzyka. Kursant: 1) identyfikuje podstawę zastosowania planu ochrony, 2) wskazuje sposób zapobiegania kradzieży bez blokowania pomocy, 3) dobiera dokumenty kabinowe z ADR 8.1.2, 4) wyjaśnia eskalację naruszenia ochrony. Ocena osobno: zaliczone/do powtórzenia/nieocenione, data, instruktor i obserwacja. Nie jest to automatyczne zaliczenie P1–P3; bez realnych towarów.

## P3: obserwowalna decyzja podczas pożaru ładunku (scenariusz 0308)

Instruktor na symulowanej planszy tunelu ocenia: 1) zakaz gaszenia przestrzeni ładunkowej przez załogę, 2) bezpieczne oddalenie uczestników, 3) wezwanie służb i przekazanie informacji o ładunku, 4) stosowanie się do poleceń ratowników. Wynik każdego elementu: zaliczone / do powtórzenia / nieocenione, z uzasadnieniem obserwacji. Nie używać ognia ani prawdziwych substancji.

## Wariant instruktażu P3 — decyzja o postoju (0310)

Instruktor przedstawia fikcyjną trasę i scenariusz z zastosowaniem ADR 8.4.1. Kursant (1) identyfikuje potrzebę nadzoru, (2) wybiera bezpieczną bazę, (3) uzasadnia warunki kolejnych alternatyw i (4) wskazuje procedurę zgłoszenia problemu. Każdy element dokumentować jako zaliczone/do powtórzenia/nieocenione; bez faktycznego przewozu i automatycznego zaliczania P3.

## Instruktorski wariant P3 — prywatny przewóz (0313)

Na fikcyjnych kartach ładunków kursant (1) wskazuje cel wykorzystania, (2) sprawdza opakowanie detaliczne, (3) ocenia zabezpieczenie przed wyciekiem, (4) wskazuje potrzebę dodatkowej oceny ilości cieczy łatwopalnych. Instruktor notuje obserwacje i zaliczone/do powtórzenia/nieocenione. Brak rzeczywistego towaru i fikcyjnych zaliczeń.

## Arkusz obserwacyjny P1–P3 (uzupełnienie 23.10.2026)

Ten arkusz pozostaje pustym wzorcem. **Nie wpisywać wyników przed rzeczywistymi zajęciami i nie uznawać quizu za zaliczenie praktyki.** Instruktor zatwierdza warunki stanowiska i ostateczne kryteria, a następnie dokumentuje realne wykonanie.

| Ćwiczenie | Stanowisko | Obserwacja instruktora | Przerwać, gdy… |
|---|---|---|---|
| P1 — gaśnica | Zabezpieczone stanowisko szkoleniowe, odpowiedni sprzęt | Kursant określa granice bezpiecznego gaszenia, demonstruje użycie pod instruktażem, przerywa na sygnał | Niebezpieczne warunki, brak nadzoru, ryzyko dla ludzi lub ogień w przestrzeni ładunkowej |
| P2 — pierwsza pomoc | Fantom, karta symulacji, bez substancji niebezpiecznych | Kursant ocenia bezpieczeństwo, zgłasza zdarzenie, wykonuje ćwiczone czynności na fantomie | Realna ekspozycja, zagrożenie ratownika, działania poza zakresem przeszkolenia |
| P3 — awaria/wypadek | Makieta zdarzenia, fikcyjny dokument przewozowy, instrukcje pisemne | Kursant wskazuje bezpieczny dystans, ostrzega, wzywa służby, przekazuje informacje i nie otwiera przesyłek | Wchodzenie w strefę zagrożenia lub próba gaszenia ładowni przez załogę |

**Wypełnia prowadzący po zajęciach:** identyfikator kursanta, data, miejsce, instruktor i kwalifikacje, stanowisko, obserwowane punkty, `wykonano / do powtórzenia / nieocenione`, zauważony błąd, instruktaż korygujący, podpis. Przed zajęciami wszystkie pola ocen są puste.

Podstawa do szczegółowej weryfikacji: Dz.U. 2021 poz. 2150, zał. 1; ADR 2025, 5.4.3.4 i 8.1.4–8.1.5. Wymagana niezależna recenzja programu i rzeczywisty instruktor. Brak realnego ognia i materiałów niebezpiecznych bez zatwierdzonego stanowiska oraz odpowiedniego nadzoru.

## Karta obserwacji praktyki P1–P3 (aktualizacja 23.10.2026)

Program kursu początkowego podstawowego przewiduje rzeczywiste ćwiczenia z używania sprzętu gaśniczego, pierwszej pomocy i zachowania po wypadku/awarii. Dodatkowy czas części praktycznej oraz podział na grupy organizator wyznacza zgodnie z aktualnym § 8 rozporządzenia o kursach ADR. Samo pytanie testowe nie jest dowodem odbycia ćwiczenia.

| Ćwiczenie | Bezpieczny przebieg pod nadzorem | Kryterium obserwacji |
|---|---|---|
| P1 — sprzęt gaśniczy | Instruktor omawia i demonstruje gaśnicę na przygotowanym stanowisku; kursant ćwiczy wyłącznie na polecenie prowadzącego | Prawidłowo rozpoznaje ograniczenia działania, potrafi obsłużyć sprzęt treningowy i nie podejmuje gaszenia pożaru przestrzeni ładunkowej |
| P2 — pierwsza pomoc | Instruktor stawia fikcyjne zdarzenie, ćwiczenia na fantomie i z bezpieczną strefą | Kursant ocenia bezpieczeństwo, alarmuje służby, wykonuje czynności na fantomie zgodnie z instrukcją |
| P3 — wypadek i awaria | Karty zdarzenia, atrapy oznakowania, fikcyjna przestrzeń zagrożenia i dokumenty | Kursant zachowuje kolejność reakcji, nie zbliża się do wycieku i przekazuje dane służbom |

### Dokumentacja do rzeczywistego wypełnienia przez instruktora

- identyfikator kursanta i dzień zajęć, rzeczywisty czas i miejsce;
- numer ćwiczenia, sprzęt treningowy, przebieg i wykazane umiejętności;
- status „wykonano / wymaga powtórzenia / nieocenione”, konkretna informacja zwrotna;
- imię i rzeczywisty podpis prowadzącego, odniesienie do dziennika zajęć kursu.

**Zasady bezpieczeństwa:** żadnych prawdziwych materiałów niebezpiecznych, niećwiczonych pożarów ani kontaktu z wyciekiem. Stanowisko szkoleniowe przygotowuje uprawniony prowadzący zgodnie z oceną ryzyka i wymaganiami ośrodka. Niniejsza karta jest projektem do zatwierdzenia, nie wygenerowanym dowodem uczestnictwa ani instrukcją medyczną.

## Protokół instruktora i bezpieczne przeprowadzenie P1–P3 — dopracowanie 24.10.2026

**Ten protokół jest narzędziem przygotowawczym, a nie potwierdzeniem wykonania ćwiczenia.** Instruktor uzupełnia go wyłącznie w trakcie rzeczywistych zajęć. Nie wpisuj z góry obecności, oceny ani podpisu.

### Zasady wspólne przed każdym ćwiczeniem

1. Sprawdź miejsce, sprzęt szkoleniowy, dostęp do pomocy i plan przerwania ćwiczenia; nie używaj prawdziwych towarów niebezpiecznych ani nie twórz niekontrolowanego ognia, wycieku czy ekspozycji.
2. Przed rozpoczęciem wyjaśnij kursantom cel, zagrożenia i granice samodzielnego działania. Każdy może zgłosić niebezpieczne warunki i przerwać działanie.
3. Zapisuj faktycznie zaobserwowane czynności, nie samą odpowiedź w quizie. W razie błędu krytycznego zatrzymaj scenariusz, wyjaśnij bezpieczne postępowanie i odnotuj potrzebę ponownej próby.

### P1 — sprzęt gaśniczy

- **Warunek zaliczenia obserwacji:** kursant rozpoznaje różnicę między niewielkim pożarem elementu pojazdu a pożarem obejmującym przestrzeń ładunkową; potrafi wskazać, kiedy nie wolno podejmować gaszenia i trzeba się oddalić oraz wezwać służby.
- **Błąd krytyczny:** wejście do ładowni, otwieranie przesyłek albo gaszenie bez zapewnienia własnego bezpieczeństwa.
- **Dowód:** instruktor zapisuje, czy kursant wykonał demonstrację i ćwiczenie na stanowisku szkoleniowym, jaki błąd zaobserwowano i czy potrzebna jest ponowna próba.

### P2 — pierwsza pomoc

- **Warunek zaliczenia obserwacji:** kursant ocenia bezpieczeństwo miejsca, wzywa pomoc, przekazuje informacje o zdarzeniu i wykonuje wyłącznie czynności objęte szkoleniem oraz możliwe do wykonania bez narażenia siebie.
- **Błąd krytyczny:** podejście do poszkodowanego przez strefę skażenia bez oceny zagrożenia lub bezpośrednie dotykanie nieznanej substancji.
- **Dowód:** opis scenariusza, obserwowane kroki, uwagi instruktora i wynik rzeczywistej próby.

### P3 — awaria lub wypadek

- **Warunek zaliczenia obserwacji:** kursant wskazuje bezpieczne miejsce, ostrzega innych, powiadamia służby, odczytuje dostępne dane o ładunku i przekazuje dokumenty/informacje ratownikom, jeśli można to zrobić bezpiecznie.
- **Błąd krytyczny:** samowolne otwieranie przesyłek, wchodzenie w opary albo podejmowanie działań wykraczających poza własne możliwości.
- **Dowód:** karta sytuacji, lista zaobserwowanych działań i konkretne uwagi do poprawy.

### Minimalny formularz obserwacji (do wypełnienia na zajęciach)

| Pole | Zapis rzeczywisty |
|---|---|
| Data, miejsce i ośrodek | Do uzupełnienia podczas zajęć |
| Instruktor prowadzący | Imię, nazwisko i właściwe uprawnienia |
| Kursant / identyfikacja według procedury OSK | Do uzupełnienia na miejscu |
| Ćwiczenie | P1 / P2 / P3 |
| Wykonane czynności | Opis obserwacji, nie deklaracja |
| Błędy krytyczne lub uwagi | Konkretne zachowanie i wyjaśnienie |
| Wynik | Wykonał / wymaga ponownej próby / nieocenione |
| Potwierdzenie instruktora | Uzupełnia wyłącznie rzeczywisty prowadzący |

Nie przekształcaj wyniku testu online w zaliczenie praktyki. Wymagania formalne i dokumentowanie zajęć należy sprawdzić z aktualnym prawem i procedurą ośrodka.

## Scenariusze sytuacyjne dla wszystkich 13 działów — etap 4t (25.10.2026)

Poniższe scenariusze uzupełniają ćwiczenia P1–P3. Każdy jest symulacją na fikcyjnych dokumentach, mapach lub pustych makietach. Nie używaj prawdziwych towarów niebezpiecznych, nie twórz wycieków ani pożarów i nie traktuj quizu jako zaliczenia praktyki.

Pełna, maszynowo sprawdzana mapa kroków i ID pytań znajduje się w `scenariusze-13-dzialow.json`. Każdy dział ma własny scenariusz z co najmniej czterema krokami i odwołaniami do pytań z tego samego działu.

| Dział | Sytuacja | Pytania do powtórki |
|---|---|---|
| ADR-B-01 | Kontrola zwolnień, ilości i dopuszczalności przewozu | ADR-B-0002, ADR-B-0259, ADR-B-0526, ADR-B-0570–0573, ADR-B-0595, ADR-B-0605–0609 |
| ADR-B-02 | Rozładunek: mokre opakowanie z nalepką 4.3 | ADR-B-0006, ADR-B-0510 |
| ADR-B-03 | Wyciek przy kratce kanalizacyjnej | ADR-B-0009, ADR-B-0514 |
| ADR-B-04 | Załadunek, źródła zapłonu i wymagany nadzór postoju | ADR-B-0010, ADR-B-0012, ADR-B-0310, ADR-B-0347, ADR-B-0580–0581 |
| ADR-B-05 | Awaria: bezpieczne zgłoszenie i dostępność sprzętu | ADR-B-0013, ADR-B-0015, ADR-B-0169, ADR-B-0585, ADR-B-0593–0594 |
| ADR-B-06 | Kontrola oznakowania kontenera | ADR-B-0016, ADR-B-0217, ADR-B-0507, ADR-B-0546, ADR-B-0562 |
| ADR-B-07 | Niezgodne opakowanie i uszkodzona sztuka przesyłki | ADR-B-0020, ADR-B-0517, ADR-B-0567–0569, ADR-B-0583–0584 |
| ADR-B-08 | Kontrola wyposażenia pojazdu i każdego członka załogi | ADR-B-0418, ADR-B-0551, ADR-B-0566, ADR-B-0596–0597 |
| ADR-B-09 | Kontrola przed załadunkiem i mocowania | ADR-B-0026, ADR-B-0080, ADR-B-0235, ADR-B-0518, ADR-B-0554 |
| ADR-B-10 | Kontener po rejsie morskim — dalszy odcinek drogowy | ADR-B-0396, ADR-B-0511 |
| ADR-B-11 | Planowanie trasy i ograniczenia tunelowe | ADR-B-0487, ADR-B-0539–0540, ADR-B-0574–0576, ADR-B-0591–0604 |
| ADR-B-12 | Ochrona przewozu i weryfikacja przewoźnika oraz postoju | ADR-B-0120, ADR-B-0211, ADR-B-0304–0305, ADR-B-0407, ADR-B-0414, ADR-B-0582 |
| ADR-B-13 | Kontrola dokumentów i instrukcji przed wyjazdem | ADR-B-0508, ADR-B-0525, ADR-B-0530, ADR-B-0577–0579, ADR-B-0586–0590, ADR-B-0598–0601 |

### Wspólny schemat pracy kursanta

1. **Zatrzymaj się i oceń bezpieczeństwo** — nie wykonuj czynności, która może narazić ludzi lub środowisko.
2. **Ustal fakty** — dokument, oznakowanie, rodzaj operacji, stan opakowania i wymagany sposób przewozu.
3. **Znajdź właściwy przepis** — nie zakładaj wyjątku i nie zgaduj brakujących danych.
4. **Podejmij bezpieczną decyzję** — zgłoś niezgodność, jeśli nie można jej rozstrzygnąć.
5. **Uzasadnij odpowiedź** — odwołaj się do pytań wskazanych przy scenariuszu i wyjaśnij, dlaczego pozostałe opcje są błędne.

### Kryteria instruktora

Dla każdego scenariusza instruktor zapisuje faktycznie zaobserwowane kroki, błędy krytyczne i potrzebę ponownej próby. Formularz uzupełnia się wyłącznie podczas rzeczywistych zajęć. Wszystkie pytania i scenariusze pozostają materiałami roboczymi `needs_review`; nie stanowią niezależnej recenzji prawnej.


## Dodatkowe scenariusze B-01–B-04

Każdy z działów B-01–B-04 ma teraz trzy scenariusze w pliku JSON: scenariusz bazowy oraz dwa nowe przypadki sytuacyjne. Scenariusze są symulacjami, nie potwierdzają odbycia zajęć praktycznych.

| ID scenariusza | Dział | Sytuacja | Pytania do powtórki |
|---|---|---|---|
| `SC-ADR-B-01-02` | ADR-B-01 | Przed wyjazdem: ustalenie, czy można skorzystać ze zwolnienia | ADR-B-0001, ADR-B-0002, ADR-B-0003, ADR-B-0259, ADR-B-0570 |
| `SC-ADR-B-01-03` | ADR-B-01 | Kontrola dokumentów: polecenie nie uchyla zakazu | ADR-B-0001, ADR-B-0002, ADR-B-0003 |
| `SC-ADR-B-02-02` | ADR-B-02 | Przy rozładunku: nieznana substancja na opakowaniu | ADR-B-0004, ADR-B-0005, ADR-B-0006, ADR-B-0510 |
| `SC-ADR-B-02-03` | ADR-B-02 | Sprawdzenie klasy i grupy pakowania przed przyjęciem | ADR-B-0004, ADR-B-0005, ADR-B-0006 |
| `SC-ADR-B-03-02` | ADR-B-03 | Nieznany wyciek podczas postoju | ADR-B-0007, ADR-B-0008, ADR-B-0009, ADR-B-0514 |
| `SC-ADR-B-03-03` | ADR-B-03 | Pozostałości po rozładunku przed kolejnym ładunkiem | ADR-B-0007, ADR-B-0008, ADR-B-0009 |
| `SC-ADR-B-04-02` | ADR-B-04 | Załadunek: e-papieros i pracujący silnik | ADR-B-0010, ADR-B-0012 |
| `SC-ADR-B-04-03` | ADR-B-04 | Postój zaplanowany, ale miejsce nie spełnia wymagań | ADR-B-0010, ADR-B-0011, ADR-B-0012, ADR-B-0310, ADR-B-0347 |

Każdy nowy rekord zawiera opis sytuacji, kroki kierowcy, typowe błędy wraz z wyjaśnieniem, podstawę ADR, powiązane pytania, kryteria oceny i granice bezpieczeństwa. Powiązania sprawdzono względem banku: wszystkie wskazane ID istnieją i należą do wskazanego działu.


## Dodatkowe scenariusze B-05–B-08

| ID scenariusza | Dział | Sytuacja | Pytania do powtórki |
|---|---|---|---|
| `SC-ADR-B-05-02` | ADR-B-05 | Awaria na poboczu: pierwsze decyzje kierowcy | ADR-B-0013, ADR-B-0015, ADR-B-0169, ADR-B-0220 |
| `SC-ADR-B-05-03` | ADR-B-05 | Pożar przy przestrzeni ładunkowej | ADR-B-0013, ADR-B-0015, ADR-B-0169, ADR-B-0222, ADR-B-0223 |
| `SC-ADR-B-06-02` | ADR-B-06 | Rozbieżność numeru na tablicy i w dokumentach | ADR-B-0016, ADR-B-0507, ADR-B-0217 |
| `SC-ADR-B-06-03` | ADR-B-06 | Nalepka zasłonięta podczas załadunku | ADR-B-0016, ADR-B-0017, ADR-B-0018 |
| `SC-ADR-B-07-02` | ADR-B-07 | Niejasny podział obowiązków przy uszkodzonym opakowaniu | ADR-B-0019, ADR-B-0020, ADR-B-0021, ADR-B-0517, ADR-B-0567 |
| `SC-ADR-B-07-03` | ADR-B-07 | Przekazanie instrukcji pisemnych nowemu członkowi załogi | ADR-B-0019, ADR-B-0020, ADR-B-0021 |
| `SC-ADR-B-08-02` | ADR-B-08 | Kontrola gaśnicy przed wyjazdem | ADR-B-0074, ADR-B-0423, ADR-B-0283 |
| `SC-ADR-B-08-03` | ADR-B-08 | Wyposażenie osobiste dla całej załogi | ADR-B-0022, ADR-B-0023, ADR-B-0024, ADR-B-0418 |

Każdy scenariusz zawiera sytuację, kroki kierowcy, błędy z wyjaśnieniem, podstawę ADR, pytania, kryteria oceny i granice bezpieczeństwa. Ćwiczenia są symulacjami, nie potwierdzają odbycia zajęć praktycznych.


## Dodatkowe scenariusze B-09–B-13

| ID scenariusza | Dział | Sytuacja | Pytania do powtórki |
|---|---|---|---|
| `SC-ADR-B-09-02` | ADR-B-09 | Oględziny przed załadunkiem | ADR-B-0554, ADR-B-0080 |
| `SC-ADR-B-09-03` | ADR-B-09 | Mocowanie przed dłuższą trasą | ADR-B-0026, ADR-B-0518, ADR-B-0235 |
| `SC-ADR-B-10-02` | ADR-B-10 | Dokumenty po rejsie morskim | ADR-B-0028, ADR-B-0029, ADR-B-0030, ADR-B-0396, ADR-B-0511 |
| `SC-ADR-B-10-03` | ADR-B-10 | Niezgodność certyfikatu pakowania | ADR-B-0028, ADR-B-0029, ADR-B-0030 |
| `SC-ADR-B-11-02` | ADR-B-11 | Objazd tunelu z ograniczeniem | ADR-B-0031, ADR-B-0032, ADR-B-0033, ADR-B-0487, ADR-B-0539, ADR-B-0540 |
| `SC-ADR-B-11-03` | ADR-B-11 | Różne kody tunelowe w jednym ładunku | ADR-B-0031, ADR-B-0032, ADR-B-0033, ADR-B-0574 |
| `SC-ADR-B-12-02` | ADR-B-12 | Zmiana planowanego postoju | ADR-B-0304, ADR-B-0582, ADR-B-0407 |
| `SC-ADR-B-12-03` | ADR-B-12 | Niezweryfikowany przewoźnik przy odbiorze ładunku | ADR-B-0120, ADR-B-0211, ADR-B-0414 |
| `SC-ADR-B-13-02` | ADR-B-13 | Brak danych w dokumencie przewozowym | ADR-B-0037, ADR-B-0038, ADR-B-0039, ADR-B-0508, ADR-B-0525, ADR-B-0530 |
| `SC-ADR-B-13-03` | ADR-B-13 | Instrukcje pisemne w nieznanym języku | ADR-B-0037, ADR-B-0038, ADR-B-0039, ADR-B-0577, ADR-B-0578, ADR-B-0579 |

Każdy scenariusz zawiera sytuację, kroki kierowcy, błędy z wyjaśnieniem, podstawę ADR, pytania, kryteria oceny i granice bezpieczeństwa. Ćwiczenia są symulacjami, nie potwierdzają odbycia zajęć praktycznych.


## Indeks wszystkich 39 scenariuszy

W każdym dziale są dokładnie trzy scenariusze. Pełny opis, kroki, pytania, kryteria i granice bezpieczeństwa znajdują się w [scenariusze-13-dzialow.json](scenariusze-13-dzialow.json). Instruktor korzysta z odpowiedniego pliku `podstawowy/instruktor/ADR-B-XX.md`; kursant przechodzi scenariusze po lekcji i pytaniach działu.

| Dział | Scenariusze |
|---|---|
| ADR-B-01 | `SC-ADR-B-01`, `SC-ADR-B-01-02`, `SC-ADR-B-01-03` |
| ADR-B-02 | `SC-ADR-B-02`, `SC-ADR-B-02-02`, `SC-ADR-B-02-03` |
| ADR-B-03 | `SC-ADR-B-03`, `SC-ADR-B-03-02`, `SC-ADR-B-03-03` |
| ADR-B-04 | `SC-ADR-B-04`, `SC-ADR-B-04-02`, `SC-ADR-B-04-03` |
| ADR-B-05 | `SC-ADR-B-05`, `SC-ADR-B-05-02`, `SC-ADR-B-05-03` |
| ADR-B-06 | `SC-ADR-B-06`, `SC-ADR-B-06-02`, `SC-ADR-B-06-03` |
| ADR-B-07 | `SC-ADR-B-07`, `SC-ADR-B-07-02`, `SC-ADR-B-07-03` |
| ADR-B-08 | `SC-ADR-B-08`, `SC-ADR-B-08-02`, `SC-ADR-B-08-03` |
| ADR-B-09 | `SC-ADR-B-09`, `SC-ADR-B-09-02`, `SC-ADR-B-09-03` |
| ADR-B-10 | `SC-ADR-B-10`, `SC-ADR-B-10-02`, `SC-ADR-B-10-03` |
| ADR-B-11 | `SC-ADR-B-11`, `SC-ADR-B-11-02`, `SC-ADR-B-11-03` |
| ADR-B-12 | `SC-ADR-B-12`, `SC-ADR-B-12-02`, `SC-ADR-B-12-03` |
| ADR-B-13 | `SC-ADR-B-13`, `SC-ADR-B-13-02`, `SC-ADR-B-13-03` |

**Kolejność nauki:** lekcja → pytania działu i explanation → trzy scenariusze → warianty egzaminu próbnego 001–005 z odpowiadającymi im kluczami. Scenariusze i egzaminy są treningowe; nie zastępują zajęć praktycznych ani niezależnej kontroli prawnej.


## Etap 4x53 — dopasowanie scenariuszy do pytań (26.10.2026)

Porównano tytuł, sytuację, kroki i cel każdego scenariusza z treścią powiązanych pytań. Potwierdzono i poprawiono siedem niedopasowań w zestawach pytań lub opisie:

- `SC-ADR-B-04-02`: usunięto pytanie o nadzór postoju z ćwiczenia o e-papierosie i pracującym silniku.
- `SC-ADR-B-06-02`: zastąpiono pytanie o reakcję na wodę przy numerze zaczynającym się od X pytaniem o znaczenie cyfry 8 w numerze zagrożenia.
- `SC-ADR-B-08-02`: usunięto pytanie o kamizelkę, dodano pytanie o brak oznaczenia terminu kontroli gaśnicy.
- `SC-ADR-B-09-02`: usunięto pytania o ogólne mocowanie, dodano pytanie o termin oczyszczenia po pozostałościach.
- `SC-ADR-B-09-03`: usunięto pytanie o zamknięcia przewozu luzem; dodano pytanie o niezamocowane skrzynie i usunięto niepasującą podstawę ADR 7.3.1.1.
- `SC-ADR-B-12-02`: zastąpiono pytanie o dokument tożsamości członka załogi pytaniem o skuteczność urządzeń zabezpieczających w trakcie przewozu.
- `SC-ADR-B-12-03`: dopasowano nazwę, sytuację, kroki, błędy i podstawę do weryfikacji tożsamości przewoźnika według ADR 1.10.1.2; usunięto nieprecyzyjne przedstawienie tego jako wymogu identyfikacji odbiorcy.

Po zmianach wszystkie 39 scenariuszy ma istniejące `question_ids` z właściwego `module_id`; nie zmieniano banku, kluczy ani statusów pytań. Raport szczegółowy: [etap 4x53](../raporty/etap-4x53-spojnosc-scenariuszy-pytania-2026-10-26.md).


## Etap 4x54 — synchronizacja starszych indeksów (26.10.2026)

Przejrzano powtórzone podsumowania w tym pliku i dopasowano je do aktualnych rekordów JSON po etapie 4x53. Zmieniono trzy zbiorcze wiersze pytań (B-06, B-09, B-12) oraz skrót opisu scenariusza B-09-03. Usunięto z aktualnego opisu B-09-03 nieaktualną wskazówkę o przewozie luzem; uzupełniono B-06 o pytanie wyjaśniające numer rozpoznawczy zagrożenia, a B-12 o pytania dotyczące weryfikacji przewoźnika i zabezpieczeń postoju.

Nie zmieniono rekordów scenariuszy, banku pytań, poprawnych odpowiedzi ani statusów. Szczegółowa kontrola zgodności znajduje się w [raporcie etapu 4x53](../raporty/etap-4x53-spojnosc-scenariuszy-pytania-2026-10-26.md). Ten wpis usuwa rozbieżności redakcyjne między starszym indeksem a aktualnym JSON; nie jest recenzją prawną.
