# Kontrola druga – partia 46 (ADR-B-0676–0690)

Main 0bb465c6b (po scaleniu #923), bank blob `ff06e555f833fa3f679c7c145c1223395ae923db`. Źródło: Dz.U. 2025 poz. 642 (+ sprostowanie poz. 1575); strony według nagłówka „Dziennik Ustaw — NNN —”. Nic nie oznaczono jako verified.

**Wynik: OK 0 / POPRAW 15 / BLOKUJ 0.** 8 nowych elementów z tej samej kompetencji (0676, 0677, 0678, 0680, 0681, 0686, 0687, 0690), 7 przeredagowań z zachowaniem tematu (0679, 0682, 0683, 0684, 0685, 0688, 0689). Bez cystern; litery kluczy, moduły i kompetencje bez zmian; liczba pytań 780 bez zmian.

**Pozostało pytań bez porównania dosłownego: 90** (0691–0780).

| ID | Kompetencja | Klucz | #923 | Kontrola 2 | Decyzja | Długości A/B/C |
|---|---|---|---|---|---|---|
| ADR-B-0676 | 02-K06 | C | POPRAW | POPRAW | NOWY ELEMENT (stare: III grupa 4.3 według szybkości wydzielania gazu – kryterium laboratoryjne, trzecie z tego schematu) | 49/62/58 |
| ADR-B-0677 | 03-K03 | C | POPRAW | POPRAW | NOWY ELEMENT (stare: wyjątek dla tego samego towaru luzem, 7.5.8.2 = 0733) | 68/59/64 |
| ADR-B-0678 | 04-K02 | C | POPRAW | POPRAW | NOWY ELEMENT (stare: zakaz otwierania sztuki przesyłki – temat 0048/0357/0737) | 63/69/65 |
| ADR-B-0679 | 01-K07 | B | POPRAW | POPRAW | PRZEREDAGOWANIE (temat zachowany; pytanie kierowane do kierowcy działającego w imieniu przewoźnika) | 57/61/70 |
| ADR-B-0680 | 03-K02 | A | POPRAW | POPRAW | NOWY ELEMENT (stare: słowo „ODPAD”, 5.4.1.1.3.1 – temat wyczerpany) | 68/65/74 |
| ADR-B-0681 | 03-K04 | A | POPRAW | POPRAW | NOWY ELEMENT (stare: zestaw łopata/osłona/pojemnik przy nalepce 8 = 0734; wariant z 8.1.5.1 powielałby 0710; nalepka 8 w instrukcjach = 0650) | 65/61/66 |
| ADR-B-0682 | 09-K04 | B | POPRAW | POPRAW | PRZEREDAGOWANIE (temat 5.2.1.10.2 (b) zachowany; opcje > 80 zn., słowa absolutne) | 73/68/65 |
| ADR-B-0683 | 09-K05 | B | POPRAW | POPRAW | PRZEREDAGOWANIE (temat przekładek z 7.5.7.2; odróżnione od 0767 – zgodność konstrukcji) | 64/73/78 |
| ADR-B-0684 | 09-K03 | C | POPRAW | POPRAW | PRZEREDAGOWANIE (temat zachowany; „całkowicie”, średniki) | 63/68/64 |
| ADR-B-0685 | 06-K07 | B | POPRAW | POPRAW | PRZEREDAGOWANIE (temat zachowany; w #923 dwie prawdziwe opcje) | 72/67/64 |
| ADR-B-0686 | 08-K05 | A | POPRAW | POPRAW | NOWY ELEMENT (stare: liczba lamp dla załogi = 0596/0075) | 62/52/66 |
| ADR-B-0687 | 03-K05 | A | POPRAW | POPRAW | NOWY ELEMENT (stare: skażona odzież – temat wyczerpany, 0110/0167/0707/0745) | 67/76/60 |
| ADR-B-0688 | 06-K02 | B | POPRAW | POPRAW | PRZEREDAGOWANIE (temat zachowany; średniki, > 80 zn.) | 67/69/70 |
| ADR-B-0689 | 06-K01 | B | POPRAW | POPRAW | PRZEREDAGOWANIE (temat zachowany; polski tekst używa „OPAKOWANIE ZBIORCZE”, nie „OVERPACK”) | 63/62/61 |
| ADR-B-0690 | 05-K02 | C | POPRAW | POPRAW | NOWY ELEMENT (stare: hamulec, silnik, wyłącznik – 0104/0182/0219/0739; propozycja #923 8.3.6 – temat wyczerpany) | 57/64/63 |

## Błędy w raporcie #923

1. **Zmiana litery klucza w zamiennikach**: 0676 (C → B), 0678 (C → B), 0679 (B → A); pole original_correct_option w JSON podawało przy tym literę zamiennika, nie banku.
2. **Zdanie po „Podstawa”**: każde proponowane objaśnienie kończyło się dodatkowym zdaniem („Kierowca powinien porównać wymagania…”) po wskazaniu podstawy.
3. **Dwie prawdziwe opcje**: 0683 (A i B prawie identyczne), 0685.
4. **Zamienniki dublujące bank lub tematy wyczerpane**: 0677 = 0733 (wyjątek dla tego samego towaru); 0681 nadal = 0734 (a wariant z 8.1.5.1 = 0710); 0687 – skażona odzież (0110/0167/0707/0745); 0690 – 8.3.6 (temat wyczerpany); 0680 – nadal dokument odpadu, słabe dystraktory; 0686 – środki ochrony indywidualnej zamiast tematu kompetencji (lampy).
5. **Słusznie**: wszystkie 15 POPRAW; zestaw łopata/osłona/pojemnik wynika z 8.1.5.3 (pierwotne 0681 wskazywało 8.1.5.2); licznik 105 → 90 i liczby 0/15 spójne; test #923 ma DWIE stałe SHA.

## Szczegóły

### ADR-B-0676 – POPRAW (NOWY ELEMENT (stare: III grupa 4.3 według szybkości wydzielania gazu – kryterium laboratoryjne, trzecie z tego schematu))

- Cytaty i strony Dz.U. (nagłówek strony): 2.2.43.1.1 (s. 187): „Tytuł klasy 4.3 obejmuje materiały, które reagując z wodą wydzielają gazy palne mogące tworzyć z powietrzem mieszaniny wybuchowe, i przedmioty zawierające takie materiały.”; 2.2.43.1.2 – W3 Przedmioty; tabela A UN 3292 BATERIE ZAWIERAJĄCE SÓD METALICZNY LUB STOP SODU (s. 581, obraz strony): klasa 4.3, kod W3, nalepka 4.3. UN 3551 (baterie sodowo-jonowe) – klasa 9.
- Raport #923: zgoda co do POPRAW; zamiennik zmieniał literę klucza C → B (original_correct_option w JSON błędne)
- Nowa treść: Kierowca ma przewieźć UN 3292 BATERIE ZAWIERAJĄCE SÓD METALICZNY LUB STOP SODU. Magazynier twierdzi, że skoro to baterie, należą do klasy 9, tak jak baterie sodowo-jonowe UN 3551. Do której klasy zalicza je tabela A?
- Klucz C: Do klasy 4.3, bo sód w kontakcie z wodą wydziela gaz palny
- Źródło: ADR 2025, 2.2.43.1.1; 2.2.43.1.2 (W3); 3.2.1 tabela A (UN 3292: 4.3, W3, nalepka 4.3)

### ADR-B-0677 – POPRAW (NOWY ELEMENT (stare: wyjątek dla tego samego towaru luzem, 7.5.8.2 = 0733))

- Cytaty i strony Dz.U. (nagłówek strony): CV13 (7.5.11, s. 1311): „Jeżeli jakikolwiek materiał wydostał się z opakowania i rozlał się lub rozsypał wewnątrz pojazdu lub kontenera, to do czasu ich dokładnego oczyszczenia, a w razie potrzeby dezynfekcji lub odkażenia, pojazd lub kontener nie może być ponownie użyty. Wszystkie inne materiały i przedmioty przewożone w tym pojeździe lub kontenerze powinny być sprawdzone, czy nie zostały skażone.”; 7.5.8.1 (s. 1309–1310); tabela A UN 2810 (s. 519–520, obraz strony): kolumna (18) CV13, CV28.
- Raport #923: zgoda (= 0733); zamiennik (wyjątek dla tego samego towaru) nadal = 0733
- Nowa treść: Po rozładunku kanistrów z UN 2810 MATERIAŁ TRUJĄCY CIEKŁY ORGANICZNY I.N.O. widać, że jeden kanister przeciekł na podłogę skrzyni. Kolumna (18) tabeli A wskazuje dla tej pozycji CV13. Na skrzyni zostały kartony dla kolejnego odbiorcy. Co wymaga CV13 oprócz dokładnego oczyszczenia skrzyni?
- Klucz C: Sprawdzić, czy pozostałe kartony w pojeździe nie zostały skażone
- Źródło: ADR 2025, 7.5.11 (CV13); 7.5.8.1; 3.2.1 tabela A (UN 2810: 6.1, kolumna (18) CV13, CV28)

### ADR-B-0678 – POPRAW (NOWY ELEMENT (stare: zakaz otwierania sztuki przesyłki – temat 0048/0357/0737))

- Cytaty i strony Dz.U. (nagłówek strony): 8.3.3 (s. 1332): „Zabrania się kierowcy i jego pomocnikowi otwierania sztuk przesyłek zawierających towary niebezpieczne.”; 1.2.1 (s. 46) – definicja „sztuka przesyłki” (opakowanie z zawartością przygotowane do wysyłki).
- Raport #923: zgoda; zamiennik zmieniał literę klucza C → B
- Nowa treść: Odbiorca chce przed rozładunkiem obejrzeć nalepki na zamkniętych beczkach i prosi kierowcę o otwarcie drzwi przestrzeni ładunkowej furgonu. Pomocnik twierdzi, że zabrania tego przepis 8.3.3. Czy ma rację?
- Klucz C: Nie, 8.3.3 zakazuje otwierania sztuk przesyłek, nie drzwi pojazdu
- Źródło: ADR 2025, 8.3.3; 1.2.1 (definicja „sztuka przesyłki”)

### ADR-B-0679 – POPRAW (PRZEREDAGOWANIE (temat zachowany; pytanie kierowane do kierowcy działającego w imieniu przewoźnika))

- Cytaty i strony Dz.U. (nagłówek strony): 1.4.2.1.1 (s. 55): „(a) upewnić się, że towary niebezpieczne są sklasyfikowane i dopuszczone do przewozu zgodnie z ADR; (b) zaopatrzyć przewoźnika w informacje i dane …”; 1.4.2.2.1 (s. 56): „(b) upewnić się, że wszystkie informacje wymagane w ADR … zostały przed jego rozpoczęciem dostarczone przez nadawcę …”; 1.4.2.2.3 (s. 56): „… nie powinien on rozpoczynać przewozu do czasu usunięcia stwierdzonych naruszeń.”
- Raport #923: zgoda; zamiennik zmieniał literę klucza B → A
- Nowa treść: Kierowca przyjeżdża po nowy materiał. Nadawca podaje tylko jego nazwę handlową, bez numeru UN, klasy i innych danych ADR, i obiecuje, że resztę dośle później. Co powinien zrobić kierowca, który sprawdza ładunek w imieniu przewoźnika?
- Klucz B: Nie ruszać, dopóki nadawca nie przekaże wymaganych danych ADR
- Źródło: ADR 2025, 1.4.2.1.1 (a)–(b); 1.4.2.2.1 (a)–(b); 1.4.2.2.3

### ADR-B-0680 – POPRAW (NOWY ELEMENT (stare: słowo „ODPAD”, 5.4.1.1.3.1 – temat wyczerpany))

- Cytaty i strony Dz.U. (nagłówek strony): 5.4.1.1.3.2 (s. 963, obraz strony): „Jeżeli w miejscu załadunku nie ma możliwości dokładnego zmierzenia ilości odpadów to ilość wymagana w 5.4.1.1.1 (f) może być … oszacowana …”; „Takie oszacowanie ilości jest niedozwolone w przypadku: … odpadów zawierających materiały wymienione w 2.1.3.5.3 (…) lub materiałów klasy 4.3”; zapis „ILOŚĆ OSZACOWANA ZGODNIE Z 5.4.1.1.3.2”.
- Raport #923: zgoda (temat „ODPAD” wyczerpany); zamiennik (nazwa techniczna, 5.4.1.1.3.3) nadal przy dokumencie odpadu, dystraktory słabe
- Nowa treść: Zakład oddaje odpady w beczkach. W części beczek jest odpad zawierający materiał klasy 4.3, a na miejscu nie da się dokładnie zmierzyć jego ilości. Nadawca chce wpisać w dokumencie „ILOŚĆ OSZACOWANA ZGODNIE Z 5.4.1.1.3.2”. Czy może tak zrobić dla tych beczek?
- Klucz A: Nie, dla odpadów z materiałem klasy 4.3 szacowanie jest niedozwolone
- Źródło: ADR 2025, 5.4.1.1.3.2 (przypadki, w których oszacowanie jest niedozwolone); 5.4.1.1.1 (f)

### ADR-B-0681 – POPRAW (NOWY ELEMENT (stare: zestaw łopata/osłona/pojemnik przy nalepce 8 = 0734; wariant z 8.1.5.1 powielałby 0710; nalepka 8 w instrukcjach = 0650))

- Cytaty i strony Dz.U. (nagłówek strony): 5.4.3.4, instrukcje pisemne – tabela dodatkowych wskazówek dla znaków (s. 978, obraz strony): „Materiały zagrażające środowisku” – „Zagrożenie w przypadku przedostania się do środowiska wodnego lub kanalizacji”; czynności (s. 975): „Jeżeli jest to właściwe i bezpieczne, zapobiec przedostaniu się uwolnionych materiałów do środowiska wodnego lub kanalizacji …”; UWAGA 1 (s. 977): przy kilku zagrożeniach „stosuje się każdą z określonych dla nich wskazówek”.
- Raport #923: zgoda (= 0734); trafnie: zestaw wynika z 8.1.5.3, nie 8.1.5.2; zamiennik nadal dublował 0734
- Nowa treść: Z pękniętej beczki z nalepką 3 i znakiem ryby i drzewa wycieka ciecz w stronę kratki ściekowej. Pomocnik twierdzi, że ten znak dotyczy jedynie oznakowania przesyłek i instrukcje pisemne nic o nim nie mówią. Co według instrukcji pisemnych oznacza ten znak?
- Klucz A: Że grozi szkoda po przedostaniu się cieczy do wód lub kanalizacji
- Źródło: ADR 2025, 5.4.3.4 (instrukcje pisemne: tabela dodatkowych wskazówek – wiersz „Materiały zagrażające środowisku”; czynności ogólne – zapobieganie przedostaniu się do środowiska wodnego lub kanalizacji; UWAGA 1)

### ADR-B-0682 – POPRAW (PRZEREDAGOWANIE (temat 5.2.1.10.2 (b) zachowany; opcje > 80 zn., słowa absolutne))

- Cytaty i strony Dz.U. (nagłówek strony): 5.2.1.10.1 (a) (s. 938) – opakowania kombinowane z opakowaniami wewnętrznymi zawierającymi materiały ciekłe; 5.2.1.10.2 (s. 939): „Strzałki kierunkowe nie są wymagane na: … (b) opakowaniach zewnętrznych zawierających towary niebezpieczne w opakowaniach wewnętrznych o pojemności nie większej niż 120 ml, jeżeli pomiędzy tymi opakowaniami a opakowaniem zewnętrznym znajduje się materiał absorpcyjny w ilości wystarczającej do wchłonięcia całej zawartości ciekłej”; (c) – 6.2 do 50 ml.
- Raport #923: zgoda; temat zachowany
- Nowa treść: Karton zawiera plastikowe buteleczki z cieczą niebezpieczną, każda po 100 ml, zamknięte zwykłymi zakrętkami. Między buteleczkami a kartonem jest materiał chłonny, który wchłonie całą ciecz. Czy na kartonie muszą być strzałki kierunkowe?
- Klucz B: Nie, bo buteleczki mają do 120 ml, a materiał chłonny wchłonie ciecz
- Źródło: ADR 2025, 5.2.1.10.1 (a); 5.2.1.10.2 (b)

### ADR-B-0683 – POPRAW (PRZEREDAGOWANIE (temat przekładek z 7.5.7.2; odróżnione od 0767 – zgodność konstrukcji))

- Cytaty i strony Dz.U. (nagłówek strony): 7.5.7.2 (s. 1309): „W razie potrzeby, sztuki przesyłek znajdujące się pod innymi sztukami przesyłek powinny być zabezpieczone przed uszkodzeniem przy użyciu przekładek.”
- Raport #923: zgoda (≈ 0767); zamiennik – opcje A i B prawie identyczne, obie prawdziwe
- Nowa treść: Na palecie stoją kartony z farbą przystosowane do piętrzenia. Na nich mają stanąć drewniane skrzynie z towarem ADR, których wąskie płozy mogą wgnieść wieka kartonów. Jak według 7.5.7.2 ochronić kartony leżące niżej?
- Klucz B: Położyć między nimi przekładki, które ochronią kartony przed uszkodzeniem
- Źródło: ADR 2025, 7.5.7.2 (przekładki chroniące sztuki przesyłek ułożone niżej)

### ADR-B-0684 – POPRAW (PRZEREDAGOWANIE (temat zachowany; „całkowicie”, średniki))

- Cytaty i strony Dz.U. (nagłówek strony): 7.5.4 (s. 1307): sposoby oddzielenia (a)–(c) – przegroda, sztuki przesyłek bez nalepek 6.1/6.2/9, odstęp co najmniej 0,8 m – oraz wyjątek, gdy sztuki przesyłek mają dodatkowe opakowanie lub są całkowicie przykryte; CV28 (s. 1312): „Patrz 7.5.4”.
- Raport #923: zgoda; temat zachowany
- Nowa treść: Worki z nalepką 6.1, dla których kolumna (18) tabeli A wskazuje CV28, stoją na skrzyni tuż obok kartonów z żywnością. Worki są w pełni przykryte plandeką, a między ładunkami nie ma przegrody ani odstępu 0,8 m. Czy taki załadunek narusza 7.5.4?
- Klucz C: Nie, bo worki w pełni przykryte nie wymagają takiego oddzielenia
- Źródło: ADR 2025, 7.5.4 (oddzielenie (a)–(c) i wyjątek dla dodatkowego opakowania lub całkowitego przykrycia); 7.5.11 (CV28)

### ADR-B-0685 – POPRAW (PRZEREDAGOWANIE (temat zachowany; w #923 dwie prawdziwe opcje))

- Cytaty i strony Dz.U. (nagłówek strony): 5.3.2.2.1 (s. 955): „Tablica powinna pozostać w miejscu jej umocowania po 15 minutach przebywania w ogniu, niezależnie od pozycji, w której znajduje się pojazd.”
- Raport #923: zgoda; zamiennik – dwie prawdziwe opcje
- Nowa treść: Przewoźnik chce przymocować wymagane tablice barwy pomarańczowej do pojazdu opaskami z tworzywa, które miękną i topią się w wysokiej temperaturze. Jaki warunek mocowania tablicy podaje 5.3.2.2.1?
- Klucz B: Ma pozostać w miejscu umocowania po 15 minutach przebywania w ogniu
- Źródło: ADR 2025, 5.3.2.2.1 (tablica pozostaje w miejscu umocowania po 15 minutach przebywania w ogniu)

### ADR-B-0686 – POPRAW (NOWY ELEMENT (stare: liczba lamp dla załogi = 0596/0075))

- Cytaty i strony Dz.U. (nagłówek strony): 8.1.5.2 (s. 1325) – dla każdego członka załogi pojazdu: kamizelka ostrzegawcza, „przenośne urządzenie oświetleniowe”; 8.3.4 (s. 1332): „Przenośne urządzenia oświetleniowe nie powinny zawierać powierzchni metalowych mogących spowodować iskrę krzesaną.”; 1.2.1 (s. 33) – członek załogi pojazdu.
- Raport #923: zgoda (= 0596/0075); zamiennik (środki ochrony indywidualnej) poza tematem kompetencji
- Nowa treść: Pojazd ADR ma na zabudowie mocne reflektory robocze, które oświetlają teren wokół niego. Kierowca jedzie sam i uważa, że dzięki nim nie musi wozić przenośnej latarki z wykazu wyposażenia ADR. Czy ma rację?
- Klucz A: Nie, 8.1.5.2 wymaga przenośnego oświetlenia dla członka załogi
- Źródło: ADR 2025, 8.1.5.2 (przenośne urządzenia oświetleniowe dla każdego członka załogi); 8.3.4; 1.2.1 (członek załogi pojazdu)

### ADR-B-0687 – POPRAW (NOWY ELEMENT (stare: skażona odzież – temat wyczerpany, 0110/0167/0707/0745))

- Cytaty i strony Dz.U. (nagłówek strony): 5.4.3.4, instrukcje pisemne – tabela nalepek (s. 977, obraz strony): nalepki 7A–7D – „Zagrożenie napromieniowaniem po wchłonięciu i napromieniowaniem zewnętrznym”, wskazówka „Ograniczyć czas narażenia”; czynności (s. 975): „Nie wchodzić na uwolnione materiały, nie dotykać ich, unikać wdychania oparów, dymu, pyłu i pary …”.
- Raport #923: zgoda (temat wyczerpany); zamiennik nadal o skażonej odzieży
- Nowa treść: Po wypadku z rozbitej sztuki przesyłki z nalepką 7 wysypał się proszek. Kolega twierdzi, że materiał promieniotwórczy szkodzi tylko promieniowaniem z daleka, więc zbierze proszek gołymi rękami, byle szybko. Co wynika z instrukcji pisemnych?
- Klucz A: Grozi też napromieniowanie po wchłonięciu, więc proszku nie dotykać
- Źródło: ADR 2025, 5.4.3.4 (wzór instrukcji pisemnych: czynności w razie wypadku – nie dotykać uwolnionych materiałów; tabela nalepek – nalepka 7)

### ADR-B-0688 – POPRAW (PRZEREDAGOWANIE (temat zachowany; średniki, > 80 zn.))

- Cytaty i strony Dz.U. (nagłówek strony): 5.2.2.1.6 (s. 939–940), zdanie końcowe: „Jeżeli nieregularny kształt lub małe wymiary sztuki przesyłki uniemożliwiają odpowiednie umieszczenie na niej nalepki ostrzegawczej, to może być ona umieszczona na dobrze zamocowanej przywieszce lub w inny odpowiedni sposób.”; 5.2.2.1.1 (s. 939).
- Raport #923: zgoda; temat zachowany
- Nowa treść: Kierowca odbiera małą sztukę przesyłki o nieregularnym kształcie. Wymagana nalepka ostrzegawcza nie jest naklejona na nią samą, lecz na dobrze zamocowanej przywieszce. Czy takie oznakowanie jest zgodne z 5.2.2.1.6?
- Klucz B: Tak, gdy kształt lub wymiary nie pozwalają nakleić jej na samą sztukę
- Źródło: ADR 2025, 5.2.2.1.6 (zdanie końcowe: przywieszka przy nieregularnym kształcie lub małych wymiarach); 5.2.2.1.1

### ADR-B-0689 – POPRAW (PRZEREDAGOWANIE (temat zachowany; polski tekst używa „OPAKOWANIE ZBIORCZE”, nie „OVERPACK”))

- Cytaty i strony Dz.U. (nagłówek strony): 5.1.2.1 (a) (s. 928): „(i) oznaczyć napisem „OPAKOWANIE ZBIORCZE”. Litery napisu … nie mniej niż 12 mm … w języku urzędowym państwa pochodzenia, a także, jeżeli nie jest to język angielski, francuski lub niemiecki, to również w języku angielskim, francuskim lub niemieckim …; (ii) zaopatrzyć w nalepki ostrzegawcze oraz oznakować numerem UN … Każdy stosowany znak lub nalepka ostrzegawcza powinny być umieszczone tylko jednokrotnie.”
- Raport #923: zgoda; polski tekst wymaga „OPAKOWANIE ZBIORCZE”
- Nowa treść: Cztery kartony z UN 1263 FARBA, każdy z nalepką 3, owinięto na palecie nieprzezroczystą folią, która zasłania ich numery UN i nalepki. Na folii jest już wymagany napis „OPAKOWANIE ZBIORCZE”. Co jeszcze trzeba na niej umieścić według 5.1.2.1?
- Klucz B: Jeden numer UN 1263 i jedną nalepkę wzoru 3 na całe opakowanie
- Źródło: ADR 2025, 5.1.2.1 (a) (i)–(ii)

### ADR-B-0690 – POPRAW (NOWY ELEMENT (stare: hamulec, silnik, wyłącznik – 0104/0182/0219/0739; propozycja #923 8.3.6 – temat wyczerpany))

- Cytaty i strony Dz.U. (nagłówek strony): 5.4.3.4 (s. 975): „W razie zaistnienia podczas przewozu wypadku lub awarii, członkowie załogi pojazdu powinni wykonać następujące czynności, jeżeli jest to możliwe i bezpieczne: — Zahamować pojazd, wyłączyć silnik i odłączyć akumulator …”; 5.4.3.3 (s. 974); 1.2.1 (s. 33) – członek załogi pojazdu.
- Raport #923: zgoda; zamiennik (8.3.6) – temat wyczerpany
- Nowa treść: Po kolizji kierowca pojazdu ADR jest nieprzytomny, a siedzący obok pomocnik nie odniósł obrażeń. Silnik pracuje, a pojazd nie jest zahamowany. Kto według instrukcji pisemnych powinien zahamować pojazd i wyłączyć silnik?
- Klucz C: Pomocnik, bo instrukcje kierują te czynności do członków załogi
- Źródło: ADR 2025, 5.4.3.4 (wzór instrukcji pisemnych: czynności członków załogi pojazdu); 5.4.3.3; 1.2.1 (członek załogi pojazdu)

## Wskaźniki

- „Poprawna = jedyna najdłuższa”: **21/780 = 2,69% → 20/780 = 2,56%** (stare 0676 miało klucz jako jedyną najdłuższą opcję; dział 02: 5/89 → 4/89); maksimum działu 5,66% bez zmian. Wskaźnik poprawiony w docs/POKRYCIE-KURSU.md, docs/STAN-KONCOWY-BANKU-ADR-PODSTAWOWY-2026-11-03.md i podstawowy/README.md.
- „Poprawna = jedyna najkrótsza”: **88/780 → 85/780**; każdy dział ≤ 38% (maks. 18,4%).
- Żadna opcja nowych rekordów nie kończy się kropką, nie ma średnika ani słów absolutnych, wszystkie ≤ 80 zn.; klucz nigdy nie jest jedyną najdłuższą ani jedyną najkrótszą. Objaśnienia: 5 zdań, 445–579 znaków, ≤ 32 słowa w zdaniu, ostatnie zdanie „Podstawa: ADR …”.
- similarity.py: cały bank – main **7 par ≥ 0,45 / 158 ≥ 0,25**; po poprawkach **7 / 154**. Pary z partią: main **0 / 5** (0690/0739 = 0,400; 0681/0734 = 0,350; 0219/0690; 0690/0691; 0690/0746); po poprawkach **0 / 1** (0625/0676 = 0,267 – UN 2794 klasa 8 a UN 3292 klasa 4.3, różne treści). Wyszukiwanie po temacie w całym banku: UN 3292, CV13, drzwi przestrzeni ładunkowej, zakaz szacowania ilości odpadu z klasą 4.3, znak ryby i drzewa w instrukcjach pisemnych, reflektory robocze, nalepka 7 – wchłonięcie, pomocnik przy nieprzytomnym kierowcy – brak duplikatów (pokrewne: 0625, 0733, 0737, 0318, 0650/0651, 0596/0075, 0295, 0104/0182).
- Kompetencje: liczby bez zmian; 05-K13, 05-K14, 05-K15 nadal po 5; kompetencje.json bez zmian.

## Synchronizacja (test na kopii repo)

- review/sequential/ i review/legal-clauses/: 675-676.json (tylko 0676), 677-678.json, 679-679.json … 690-690.json – snapshoty; w legal-clauses clause, answer_review A/B/C, notes_on_conditions.
- Ledger z PAKIET-0780-MANIFEST (source_ledger / supplemental) – 15 wpisów.
- Egzaminy 001–005: ŻADEN wariant nie zawiera 0676–0690 – zmienia się tylko SHA (10 plików). Kolejki 4X40/4X44 – tylko SHA.
- SHA ff06e555… → 092325a2… w 49 plikach; zostaje tylko w review/literal-pl/ i jako FIRST_PASS_BANK_SHA w tests/test_literal_review_0676_0690.py.
- REJESTR-AKTUALNY-0001-0765.md i 0001-0780.md – po 15 wierszy.
- Scenariusze: SC-ADR-B-03-04 → ADR-B-0733 (było 0677), SC-ADR-B-04-04 → ADR-B-0048, 0357, 0737 (było 0678); SCENARIUSZE.md – zdanie o SC-ADR-B-04-04.
- Lekcje i instruktor: ADR-B-02 (stara sekcja grup pakowania 4.3 wskazuje 0127 + nowa sekcja UN 3292), ADR-B-03 (0681 → stara sekcja wskazuje 0734 + nowa sekcja o znaku ryby i drzewa; 0677 → 0733 + nowa sekcja CV13; 0680 → 0008 + nowa sekcja o szacowaniu; 0687 → nowa sekcja nalepki 7; instruktor: 8.1.5.2 → 8.1.5.3), ADR-B-04 (scenariusz → 0737 + nowa sekcja o drzwiach), ADR-B-05 (sekcja o pomocniku przy nieprzytomnym kierowcy), ADR-B-06 („OVERPACK” → „OPAKOWANIE ZBIORCZE”, 15 minut w ogniu według polskiego tekstu), ADR-B-08 (0596 + 0686 – reflektory robocze), ADR-B-09 („elementy nośne” → „przekładki”).

## Wynik testu

Git worktree z main 0bb465c6b + POPRAWKI + synchronizacja: 14 skryptów CI zielonych (validate, coverage, check_mock_exam_variants, answer_leakage_metrics, answer_length_bias --threshold 0.16 --strict, check_explanation_quality --minimum 300, check_near_duplicates 0.60, check_cross_module_duplicates 0.80, similarity, check_explanation_heuristics, release_gate --report, check_sequential_audit, check_legal_clause_review, course_consistency); `python3 -m unittest discover -s tests` – **251/251 OK**. Blob banku po zastosowaniu: `092325a21fe95a47406e2d28e4947885c19dc0dc`.

## Do pakietu dla specjalistów

- 0678 – zakres 8.3.3: czy otwarcie drzwi przestrzeni ładunkowej na prośbę odbiorcy jest dopuszczalne (zakaz dotyczy sztuk przesyłek).
- 0680 – relacja do 0318 (dopuszczalność szacowania ilości odpadów) – czy oba pytania mogą zostać obok siebie.
- 0684 – wyjątek 7.5.4 przy całkowitym przykryciu: czy zakaz „spiętrzania” nadal obowiązuje.
- 0687 – w objaśnieniu: zagrożenie „po wchłonięciu” (tekst ADR nie wymienia dróg wchłonięcia).
- 0689 – wymóg językowy napisu „OPAKOWANIE ZBIORCZE” (wersja angielska, francuska lub niemiecka).
- 0690 – rola pomocnika (członka załogi) przy nieprzytomnym kierowcy.
- kompetencje.json: 03-K04 ma w legal_refs „5.4.3.4; 8.1.5.2” – wyposażenie do ochrony kanalizacji wynika z 8.1.5.3 (nie zmieniano; do decyzji).
- poza partią: 0769 dubluje 0514, 0706 dubluje 0177; 0708 dubluje 0714; 0713 – KC 471 a Prawo przewozowe.