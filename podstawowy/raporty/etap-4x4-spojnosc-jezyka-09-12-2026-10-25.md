# ETAP 4x4 — kontrola spójności i języka kursanta: B-09–B-12

- Data: 25.10.2026.
- Bazowy `main`: `a1ae267aae3743e738c1830f9336c1ee107c95b0`.
- Zakres: 188 pytań B-09–B-12; porównano treść, opcje A/B/C, klucz, explanation, wskazane źródła i podręcznik.
- Kontrola redakcyjna nie jest formalnym zatwierdzeniem prawnym ani opinią specjalisty ADR.

## Wynik ilościowy

- Bank: 609 pytań; duplikaty ID: 0.
- Poprawna odpowiedź jest jedyną najdłuższą: 85/609 = 13.96% (limit 18%).
- Explanation w całym banku: 300–457 znaków; poniżej 200: 0; powyżej 500: 0; poza zakresem 2–5 zdań: 0.
- Statusy: 609 `needs_review`, 0 `verified`.
- Brak zmian ID, `module_id` i kluczy odpowiedzi. Egzaminy próbne 001–002 zsynchronizowano z nową treścią pytań i explanation; nie zmieniano zestawów ID.

## Problemy i poprawki

1. **B-09 — oddzielenie od żywności.** Doprecyzowano, że 0,8 m wolnej przestrzeni jest jedną z metod z ADR 7.5.4(c), a nie uniwersalnym wymogiem dla każdego przewozu. Dodano odwołanie do CV28 w kolumnie 18 tabeli A oraz ADR 7.5.11.
2. **B-10 — dokumentacja i wyjątki transportu kombinowanego.** Dopisano warunki dla łańcucha droga–kolej/żegluga śródlądowa (1.1.4.5), historycznego wyjątku dla niektórych cystern IMO zbudowanych przed 1 stycznia 2003 r. (1.1.4.3) oraz warunków dla butli DOT przy imporcie/eksporcie (1.1.4.7.1–1.1.4.7.2). Wskazano wymagane dodatkowe wpisy 5.4.1.1.24, badania okresowe i ograniczenia wyjątku.
3. **B-11 — kategorie i kody tunelowe.** Doprecyzowano, że A nie wprowadza ograniczeń tunelowych wynikających z systemu A–E, a E jest najbardziej restrykcyjna. Dodano regułę kodu B1000C dla progu 1000 kg netto materiału wybuchowego i ograniczenie tuneli E dla oznakowanych jednostek LQ na warunkach 3.4.13–3.4.14 oraz 8.6.3.3–8.6.4.
4. **B-12 — ochrona przewozu.** Dodano zasadę czytania progów z tabeli 1.10.3.1.2 według sposobu przewozu; 3000 l dla cystern nie jest automatycznie progiem dla sztuk przesyłek. Doprecyzowano elementy planu ochrony 1.10.3.2.2, identyfikację przewoźnika i członków załogi (1.10.1.2 i 1.10.1.4), zabezpieczenia podczas przewozu (1.10.3.3) oraz zasady postoju, gdy stosuje się ADR 8.4.1.
5. **Dystraktory — ADR-B-0391.** Zastąpiono oczywiście niepasujące role „kierowcy autobusu” i pracownika ochrony wariantami, które mylą odpowiedzialność przewoźnika, pakującego i odbiorcy.
6. **Dystraktory — ADR-B-0434.** Zastąpiono niepasujące identyfikatory pasażera i kod pocztowy błędnym wskazaniem kolumn 18 i 12 tabeli A, co lepiej sprawdza rozumienie struktury tabeli.
7. **Dystraktory — ADR-B-0212.** Zastąpiono ogólnik o „jednym kierowcy” niepełnym planem ograniczonym do plomb i zabezpieczenia pojazdu. Explanation wskazuje, których elementów planu nadal brakuje.

Po pierwszym uruchomieniu CI kontrola per-moduł wykryła wskaźnik „poprawna = najdłuższa” 8/43 w B-11 i 8/44 w B-12. Po wydłużeniu wiarygodnych dystraktorów wynik wynosi odpowiednio 7/43 = 16,28% i 7/44 = 15,91%; oba działy mieszczą się poniżej limitu 18%. Po edycji zsynchronizowano snapshoty w `review/sequential` i `review/legal-clauses` dla ADR-B-0212, 0391 i 0434, bez zmiany statusu recenzji. Zsynchronizowano też treść pytań i klucze wariantów próbnych 001–002. Nie stwierdzono potwierdzonego błędu wymagającego zmiany klucza ani przypisania działu.

## Pełna lista sprawdzonych pytań

Poniżej wszystkie ID z B-09–B-12, skrócony temat, fragment lekcji porównany podczas audytu oraz podstawa zapisana w rekordzie banku.

## ADR-B-09 — 46 pytań

| ID | Pytanie / kompetencja sprawdzana | Fragment lekcji porównany | Podstawa z rekordu |
|---|---|---|---|
| `ADR-B-0025` | Na jakiej podstawie należy ustalić, czy sztuki przesyłek z różnymi nalepkami ostrzegawczymi ADR wolno załadować do j… | § 2 — Wspólny załadunek i oddzielenie żywności | 7.5.2 |
| `ADR-B-0026` | Jak należy zabezpieczyć sztuki przesyłki ADR na pojeździe? | § 3 — Mocowanie i piętrzenie | 7.5.7.1 |
| `ADR-B-0027` | Czy ograniczenia dotyczące kontaktu określonych towarów niebezpiecznych z żywnością mogą mieć znaczenie podczas zała… | § 2 — Wspólny załadunek i oddzielenie żywności | 7.5.4; 7.5.11 CV28; tabela A kolumna (18) |
| `ADR-B-0058` | Na przesyłce ADR widnieją strzałki kierunkowe wskazujące górę. Jak należy ją ustawić? | § 1 — Kontrola przed załadunkiem | 7.5.1.5 |
| `ADR-B-0059` | Czy wolno piętrzyć sztuki przesyłek ADR, których konstrukcja nie przewiduje piętrzenia? | § 3 — Mocowanie i piętrzenie | 7.5.7.2 |
| `ADR-B-0060` | Czy zbyt mocno zaciągnięty pas mocujący może naruszać wymagania ADR? | § 3 — Mocowanie i piętrzenie | 7.5.7.1 |
| `ADR-B-0078` | Pracownik chce ustawić karton ADR na innym kartonie, choć opakowania nie przewidują piętrzenia. Czy wolno? | § 3 — Mocowanie i piętrzenie | 7.5.7.2 |
| `ADR-B-0079` | Na palecie ADR pasy mocujące zaczynają odkształcać opakowania. Jaka jest prawidłowa reakcja? | § 3 — Mocowanie i piętrzenie | 7.5.7.1 |
| `ADR-B-0080` | Po rozładunku beczki ADR widać pozostałości jej zawartości na skrzyni ładunkowej. Kiedy najpóźniej należy oczyścić p… | § 4 — Pozostałości i czyszczenie | 7.5.8.1 |
| `ADR-B-0081` | Ładujesz towary ADR wymagające środków ostrożności względem żywności zgodnie z 7.5.4. Jaką minimalną wolną przestrze… | § 2 — Wspólny załadunek i oddzielenie żywności | 7.5.4 (c) |
| `ADR-B-0082` | Planujesz doładować do żywności przesyłki ADR z nalepką 6.1. Co trzeba ustalić, zanim zastosujesz zasady oddzielenia… | § 2 — Wspólny załadunek i oddzielenie żywności | 7.5.4; 7.5.11 CV28; tabela A kol. (18) |
| `ADR-B-0138` | Kontrola przed załadunkiem ADR wykazuje niezgodność wyposażenia pojazdu z wymaganiami. Co należy zrobić? | § 1 — Kontrola przed załadunkiem | 7.5.1.2 |
| `ADR-B-0139` | W jakim przypadku ADR 7.3.1.1 dopuszcza przewóz towarów niebezpiecznych luzem w pojeździe lub kontenerze? | § 5 — Przewóz luzem | 7.3.1.1; 3.2 tabela A kol. (10),(17) |
| `ADR-B-0172` | Opakowanie ADR ma strzałki kierunkowe, a pracownik chce je położyć na boku, aby zmieściło się pod pasem. Co jest wła… | § 1 — Kontrola przed załadunkiem | 7.5.1.5 |
| `ADR-B-0173` | Dla danego towaru nie znaleziono w kolumnach 10 i 17 tabeli A ani kodu BK/VC, ani wyraźnego odesłania dopuszczająceg… | § 5 — Przewóz luzem | 7.3.1.1; 3.2 tabela A kol. (10),(17) |
| `ADR-B-0199` | Na jedną ciężarówkę mają trafić sztuki przesyłek ADR oznaczone różnymi nalepkami ostrzegawczymi. Pracownik twierdzi,… | § 2 — Wspólny załadunek i oddzielenie żywności | 7.5.2.1; 7.5.2.2 |
| `ADR-B-0200` | Obok kartonów ADR załadowano ciężką maszynę niebędącą towarem niebezpiecznym. Co wymaga ADR przy jej mocowaniu? | § 3 — Mocowanie i piętrzenie | 7.5.7.1 |
| `ADR-B-0201` | Po rozładunku towaru niebezpiecznego przewożonego luzem pojazd ma zostać ponownie załadowany dokładnie tym samym tow… | § 4 — Pozostałości i czyszczenie | 7.5.8.2 |
| `ADR-B-0202` | Przed załadunkiem ADR kierowca pokazuje jedynie fakturę handlową, a wymaganych dokumentów przewozowych nie da się sk… | § 1 — Kontrola przed załadunkiem | 7.5.1.2 |
| `ADR-B-0235` | W czasie załadunku ADR widzisz niezamocowane skrzynie, które mogą przesunąć się podczas hamowania. Co należy zrobić … | § 3 — Mocowanie i piętrzenie | 7.5.7.1 |
| `ADR-B-0236` | Podczas mocowania sztuk przesyłek ADR pas transportowy zaczyna zgniatać opakowanie. Jak powinien zareagować kierowca… | § 3 — Mocowanie i piętrzenie | 7.5.7.1 |
| `ADR-B-0237` | Przedsiębiorstwo chce piętrzyć sztuki przesyłek ADR, które nie zostały zaprojektowane do piętrzenia. Czy takie ułoże… | § 3 — Mocowanie i piętrzenie | 7.5.7.2 |
| `ADR-B-0238` | Po rozładunku zapakowanych towarów ADR zauważono, że zawartość jednej przesyłki wyciekła do przestrzeni ładunkowej. … | § 4 — Pozostałości i czyszczenie | 7.5.8.1 |
| `ADR-B-0239` | Przed rozpoczęciem załadunku towarów niebezpiecznych stwierdzono uszkodzenie pojazdu zagrażające bezpieczeństwu prze… | § 1 — Kontrola przed załadunkiem | 7.5.1.2 |
| `ADR-B-0240` | Samochód po przewozie niebezpiecznego towaru luzem ma przyjąć kolejny, inny ładunek. Kiedy może odstąpić od czyszcze… | § 4 — Pozostałości i czyszczenie | 7.5.8.2 |
| `ADR-B-0286` | Sztuka przesyłki ADR ma strzałki kierunkowe na dwóch przeciwległych bokach. W jakiej pozycji należy co do zasady ust… | § 1 — Kontrola przed załadunkiem | 7.5.1.5 |
| `ADR-B-0291` | Załadowca chce umieścić w jednym pojeździe sztuki przesyłek z różnymi nalepkami zagrożeń. Od czego zależy dopuszczal… | § 2 — Wspólny załadunek i oddzielenie żywności | 7.5.2.1 |
| `ADR-B-0292` | W tabeli A ADR przy towarze nie ma zezwolenia na przewóz luzem kodem BK w kolumnie 10 ani VC w kolumnie 17. Co oznac… | § 5 — Przewóz luzem | 7.3.1.1 |
| `ADR-B-0324` | Jedna sztuka przesyłki ADR ma jednocześnie nalepki 5.2 i 1 (oznaczenie „5.2 + 1”), a druga ma wyłącznie nalepkę 5.2.… | § 2 — Wspólny załadunek i oddzielenie żywności | 7.5.2.1 (tabela: 5.2 + 1 z 5.2) |
| `ADR-B-0424` | Przed załadunkiem kierowca widzi sztukę przesyłki oznaczoną nalepkami klasy 1 i inną oznaczoną klasą 3. Czy może oce… | § 2 — Wspólny załadunek i oddzielenie żywności | 7.5.2.1 |
| `ADR-B-0425` | Na przesyłce z materiałami klasy 1 występuje kod zgodności 1.4S. Jakie znaczenie może mieć to dla ładowania z towara… | § 2 — Wspólny załadunek i oddzielenie żywności | 7.5.2.1, uwaga (a) |
| `ADR-B-0426` | Jedna paleta ma nalepkę 4.1 oraz dodatkową 1. Czy kolumna '4.1 + 1' tabeli 7.5.2.1 oznacza dwie niezależne palety? | § 2 — Wspólny załadunek i oddzielenie żywności | 7.5.2.1 tabela |
| `ADR-B-0427` | Ładowca próbuje uzasadnić wspólny załadunek materiału wybuchowego i dowolnego materiału utleniającego, powołując się… | § 2 — Wspólny załadunek i oddzielenie żywności | 7.5.2.1, uwaga (d) |
| `ADR-B-0428` | Załadowca przewozi wyłącznie sztuki przesyłek klasy 1 o różnych grupach zgodności. Która reguła decyduje o wspólnym … | § 2 — Wspólny załadunek i oddzielenie żywności | 7.5.2.2 |
| `ADR-B-0429` | Sztuki przesyłek ADR mają zostać załadowane razem, lecz nie spełniają warunków tabeli 7.5.2.1. Czy odrębne dokumenty… | § 2 — Wspólny załadunek i oddzielenie żywności | 7.5.2.1 |
| `ADR-B-0436` | Do załadunku ADR przygotowano uszkodzoną sztukę przesyłki. Kierowca proponuje przykrycie jej czystą plandeką zamiast… | § 1 — Kontrola przed załadunkiem | 7.5.1.2; 1.4.3.1.1(b) |
| `ADR-B-0491` | W pojeździe mają znaleźć się sztuki przesyłek wyłącznie klasy 1 z nalepkami wzorów 1 i 1.4. Gdzie szuka się oceny ws… | § 2 — Wspólny załadunek i oddzielenie żywności | 7.5.2.1 uwaga 2; 7.5.2.2 |
| `ADR-B-0492` | Dwie przesyłki nie mogą zostać załadowane razem na podstawie ADR 7.5.2. Czy wystawienie dwóch oddzielnych dokumentów… | § 2 — Wspólny załadunek i oddzielenie żywności | 7.5.2.1 uwaga 1; 5.4.1.4.2 |
| `ADR-B-0518` | Kierowca kontroluje mocowanie palety ADR. Pas jest tak silnie napięty, że widocznie deformuje jedno z opakowań. Jak … | § 3 — Mocowanie i piętrzenie | 7.5.7.1 |
| `ADR-B-0554` | Przed załadunkiem kierowca widzi, że podłoga pojazdu jest zabrudzona pozostałościami poprzedniego ładunku, które mog… | § 1 — Kontrola przed załadunkiem | 7.5.1.2 |
| `ADR-B-0555` | Podczas kontroli przed załadunkiem stwierdzono, że opakowanie jednej sztuki przesyłki jest uszkodzone i może przecie… | § 1 — Kontrola przed załadunkiem | 7.5.1.2 |
| `ADR-B-0556` | W dokumentach towar ma kod dopuszczający przewóz luzem, ale dostępny pojazd nie spełnia wymagań dla tego rodzaju prz… | § 5 — Przewóz luzem | 7.3.1.1; 7.3.2 |
| `ADR-B-0557` | Przygotowano ładunek do przewozu luzem, lecz nie sprawdzono, czy tabela A ADR dopuszcza taki sposób przewozu dla dan… | § 5 — Przewóz luzem | 3.2.1 tabela A kolumna 17; 7.3 |
| `ADR-B-0558` | Po załadunku luzem kierowca zauważa, że zamknięcia przestrzeni ładunkowej nie zabezpieczają przed wysypaniem towaru.… | § 3 — Mocowanie i piętrzenie | 7.3.3; 7.5.7.1 |
| `ADR-B-0559` | Załadowca proponuje przewóz luzem, ponieważ pozwoli to zaoszczędzić czas, ale wpis ADR dla towaru nie przewiduje tak… | § 5 — Przewóz luzem | 7.3.1.1; 3.2.1 tabela A |
| `ADR-B-0560` | Przed załadunkiem pojazdu ADR kontrolujący stwierdza, że wyposażenie lub stan pojazdu nie pozwalają bezpiecznie wyko… | § 1 — Kontrola przed załadunkiem | 7.5.1.2 |

## ADR-B-10 — 55 pytań

| ID | Pytanie / kompetencja sprawdzana | Fragment lekcji porównany | Podstawa z rekordu |
|---|---|---|---|
| `ADR-B-0028` | Jeśli przewóz towarów niebezpiecznych obejmuje odcinek drogowy i morski, które przepisy mogą być istotne? | § 1–3 — ADR/IMDG, warunki uznania i dokumentacja | 1.1.4.2 |
| `ADR-B-0029` | Czy sztuka przesyłki przygotowana zgodnie z kodeksem morskim IMDG może, w określonych warunkach ADR, uczestniczyć w … | § 1–3 — ADR/IMDG, warunki uznania i dokumentacja | 1.1.4.2.1 |
| `ADR-B-0030` | Co należy sprawdzić przed rozpoczęciem drogowego odcinka przewozu kontenera z towarami niebezpiecznymi po transporci… | § 1–3 — ADR/IMDG, warunki uznania i dokumentacja | 1.1.4.2 |
| `ADR-B-0061` | Jaki dodatkowy zapis przewiduje ADR w dokumencie przewozowym, jeśli przewóz odbywa się zgodnie z 1.1.4.2.1? | § 1–3 — ADR/IMDG, warunki uznania i dokumentacja | 5.4.1.1.7 |
| `ADR-B-0062` | Dlaczego przy drogowym etapie transportu morskiego nie należy automatycznie usuwać oznakowania zagrożeń z kontenera? | § 1–3 — ADR/IMDG, warunki uznania i dokumentacja | 1.1.4.2 |
| `ADR-B-0119` | Ładunek był transportowany morzem i ma oznakowanie według IMDG. Co należy ustalić przed jego drogową częścią przewoz… | § 1–3 — ADR/IMDG, warunki uznania i dokumentacja | 1.1.4.2 |
| `ADR-B-0140` | Zwykły kontener ładunkowy ze sztukami przesyłek ADR (nie kontener-cysterna) będzie najpierw przewożony drogą, a nast… | § 4 — Certyfikat pakowania | 5.4.2 |
| `ADR-B-0141` | Który zestaw odpowiada gałęziom transportu towarów niebezpiecznych? | § 5 — Cysterny przenośne IMO | 1.1.4.2; 1.1.4.3 |
| `ADR-B-0142` | Kontener z oznakowaniem IMDG po rejsie morskim jedzie drogą. Co trzeba sprawdzić? | § 1–3 — ADR/IMDG, warunki uznania i dokumentacja | 1.1.4.2.1 |
| `ADR-B-0203` | Przesyłka ADR jedzie ciężarówką do portu, ale nie korzysta z warunkowego uznania przepisów transportu morskiego z 1.… | § 1–3 — ADR/IMDG, warunki uznania i dokumentacja | 5.4.1.1.7 |
| `ADR-B-0204` | Kontener z towarami niebezpiecznymi jedzie drogą, a następnie ma być załadowany na statek. Kto, zgodnie z ADR 5.4.2,… | § 4 — Certyfikat pakowania | 5.4.2 |
| `ADR-B-0205` | Ładunek niebezpieczny najpierw jest przewożony koleją, a potem dalej ciężarówką. Jaką zasadę należy przyjąć przy oce… | § 5 — Cysterny przenośne IMO | 1.1.4.2; 1.1.4.3 |
| `ADR-B-0206` | Kontener po rejsie morskim jest oznakowany zgodnie z IMDG, ale inaczej niż w typowym przewozie drogowym. Kiedy można… | § 1–3 — ADR/IMDG, warunki uznania i dokumentacja | 1.1.4.2.1 |
| `ADR-B-0247` | Kontener z towarem ADR jedzie najpierw drogą, później statkiem. Czy samo przejście do transportu morskiego zawsze zw… | § 1–3 — ADR/IMDG, warunki uznania i dokumentacja | 1.1.4.2.1 |
| `ADR-B-0277` | Przewóz drogowy towarów niebezpiecznych stanowi część łańcucha z transportem morskim, a przewóz realizuje się na war… | § 1–3 — ADR/IMDG, warunki uznania i dokumentacja | 5.4.1.1.7 |
| `ADR-B-0278` | Certyfikat pakowania kontenera przekazano przez EDI, a kolejny przewoźnik wymaga papierowego egzemplarza. Co, według… | § 5 — Inne gałęzie i umowy | 5.4.2, przypis dotyczący IMDG 5.4.2.4 |
| `ADR-B-0320` | Transport obejmuje drogowy odcinek podróży morskiej. Sztuki przesyłek oznakowano zgodnie z IMDG, lecz nie w pełni zg… | § 1–3 — ADR/IMDG, warunki uznania i dokumentacja | 1.1.4.2.1 |
| `ADR-B-0321` | W morsko-drogowym łańcuchu przewozu dokument IMDG zastępuje dokument ADR na podstawie 1.1.4.2.3. Co z informacjami d… | § 1–3 — ADR/IMDG, warunki uznania i dokumentacja | 1.1.4.2.3 |
| `ADR-B-0381` | W łańcuchu drogowym i morskim opakowanie nie jest oznaczone zgodnie z ADR, lecz podlega dopuszczeniu według 1.1.4.2.… | § 1–3 — ADR/IMDG, warunki uznania i dokumentacja | 1.1.4.2.1(a) |
| `ADR-B-0382` | W łańcuchu z etapem morskim zastosowano przywilej 1.1.4.2.1 dla wspólnego pakowania w jednej sztuce przesyłki. Które… | § 1–3 — ADR/IMDG, warunki uznania i dokumentacja | 1.1.4.2.1(b) |
| `ADR-B-0383` | Kontener w łańcuchu morskim oznakowano według IMDG zamiast oznaczeń wymaganych w ADR 5.3. Co może dopuścić 1.1.4.2.1… | § 1–3 — ADR/IMDG, warunki uznania i dokumentacja | 1.1.4.2.1(c) |
| `ADR-B-0384` | Kontener w łańcuchu morskim korzysta z oznakowania IMDG na podstawie 1.1.4.2.1(c). Co z oznakowaniem pojazdu drogowe… | § 1–3 — ADR/IMDG, warunki uznania i dokumentacja | 1.1.4.2.1(c); 5.3.2.1.1 |
| `ADR-B-0385` | Pusty, nieoczyszczony kontener-cysterna przybywa morzem i jedzie do punktu czyszczenia. Jak długo określona reguła o… | § 1–3 — ADR/IMDG, warunki uznania i dokumentacja | 1.1.4.2.1(c) |
| `ADR-B-0386` | Towar jest niebezpieczny według klas 1–9 ADR, ale nie jest uznawany za niebezpieczny według właściwego IMDG/ICAO. Cz… | § 1–3 — ADR/IMDG, warunki uznania i dokumentacja | 1.1.4.2.1 akapit końcowy |
| `ADR-B-0387` | Pojazd inny niż przewożący wskazane kontenery ma nalepki wielkiego formatu według IMDG, ale nie zgodnie z ADR 5.3.1.… | § 1–3 — ADR/IMDG, warunki uznania i dokumentacja | 1.1.4.2.2 |
| `ADR-B-0388` | Dokument IMDG/ICAO może w określonym łańcuchu zastępować dokument przewozowy ADR. Co trzeba sprawdzić? | § 1–3 — ADR/IMDG, warunki uznania i dokumentacja | 1.1.4.2.3 |
| `ADR-B-0389` | Łańcuch obejmuje przewóz drogą i morzem. Czy dopuszczenie z 1.1.4.2.1 oznacza, że nie trzeba spełniać żadnych wymaga… | § 1–3 — ADR/IMDG, warunki uznania i dokumentacja | 1.1.4.2.1 |
| `ADR-B-0390` | Towar niebezpieczny ma jechać w zwykłym kontenerze drogą, a następnie statkiem. Jaki dokument przewiduje 5.4.2? | § 4 — Certyfikat pakowania | 5.4.2 |
| `ADR-B-0391` | Kto według ADR 5.4.2 ma przekazać przewoźnikowi morskiemu świadectwo pakowania kontenera? | § 4 — Certyfikat pakowania | 5.4.2 |
| `ADR-B-0392` | Czy funkcję świadectwa pakowania kontenera i dokumentu przewozowego ADR wolno w określonych warunkach połączyć w jed… | § 4 — Certyfikat pakowania | 5.4.2 |
| `ADR-B-0393` | W morskim łańcuchu transportowym ładunek jest przewożony w pojeździe, a nie kontenerze. Co mówi ADR 5.4.2 o świadect… | § 4 — Certyfikat pakowania | 5.4.2 |
| `ADR-B-0394` | Czy ADR 5.4.2 wymaga świadectwa pakowania kontenera dla przenośnej cysterny wyłącznie z tego powodu, że będzie przew… | § 4 — Certyfikat pakowania | 5.4.2 |
| `ADR-B-0395` | Kierowca korzysta z odstępstwa ADR 1.1.4.2.1. Jaki wpis dokumentowy przewiduje 5.4.1.1.7? | § 1–3 — ADR/IMDG, warunki uznania i dokumentacja | 5.4.1.1.7 |
| `ADR-B-0396` | Kontener z towarem niebezpiecznym wyrusza drogą do portu. Czy sam przejazd do portu uprawnia do niestosowania całego… | § 1–3 — ADR/IMDG, warunki uznania i dokumentacja | 1.1.4.2 |
| `ADR-B-0397` | W łańcuchu obejmującym transport lotniczy paczka spełnia ICAO TI zamiast części wymagań oznakowania ADR. Która zasad… | § 1–3 — ADR/IMDG, warunki uznania i dokumentacja | 1.1.4.2.1(a) |
| `ADR-B-0398` | W transporcie drogowym z odcinkiem morskim przed przewozem ktoś proponuje zastąpić dokument transportowy IMDG ustnym… | § 1–3 — ADR/IMDG, warunki uznania i dokumentacja | 1.1.4.2.3 |
| `ADR-B-0437` | Ciężarówka z ładunkiem ADR jest przewożona na wagonie kolejowym na jednym odcinku trasy. Jakie przepisy zgodnie z AD… | § 5 — Inne gałęzie i umowy | 1.1.4.5.1 |
| `ADR-B-0438` | Samochód ADR jest transportowany promem, a później kontynuuje jazdę drogą. Którego odcinka dotyczy reguła 1.1.4.5.1 … | § 5 — Butle DOT i szczególne wyjątki | 1.1.4.5.1 |
| `ADR-B-0439` | Państwa będące stronami ADR chcą uzgodnić stosowanie ADR na odcinku, na którym pojazdy przewożone są koleją. Czy 1.1… | § 5 — Inne gałęzie i umowy | 1.1.4.5.2 |
| `ADR-B-0440` | Uzgodnienie z 1.1.4.5.2 rozszerza stosowanie ADR na niedrogowy etap podróży. Czy strony mogą dołączyć do niego wymag… | § 5 — Inne gałęzie i umowy | 1.1.4.5.2 |
| `ADR-B-0441` | Kto zgodnie z ADR 1.1.4.5.2 zgłasza uzgodnienie dotyczące stosowania ADR na niedrogowym odcinku do sekretariatu UNEC… | § 5 — Butle DOT i szczególne wyjątki | 1.1.4.5.2 |
| `ADR-B-0442` | Umowa międzynarodowa dotycząca innej gałęzi transportu zgodnie ze swoim zakresem obejmuje także określony odcinek dr… | § 5 — Butle DOT i szczególne wyjątki | 1.1.4.5.3 |
| `ADR-B-0443` | W sytuacji opisanej w ADR 1.1.4.5.3 wymaganie ADR jest sprzeczne z odpowiednią konwencją regulującą inną gałąź przew… | § 5 — Inne gałęzie i umowy | 1.1.4.5.3 |
| `ADR-B-0444` | W dokumencie opisano cysternę przenośną IMO typu 2 zbudowaną i zatwierdzoną przed 1 stycznia 2003 r., ale niezgodną … | § 5 — Cysterny przenośne IMO | 1.1.4.3 |
| `ADR-B-0445` | Cysterna przenośna IMO z 2001 r. spełnia część warunków historycznego wyjątku ADR 1.1.4.3. Które przepisy dotyczące … | § 5 — Butle DOT i szczególne wyjątki | 1.1.4.3 |
| `ADR-B-0446` | Dwie cysterny przenośne IMO zostały zbudowane według IMDG: jedna przed 2003 r., druga w 2005 r. Czy można automatycz… | § 5 — Cysterny przenośne IMO | 1.1.4.3 |
| `ADR-B-0447` | Do Polski drogą morską sprowadzono gaz w butli wielokrotnego napełniania zatwierdzonej przez amerykański DOT według … | § 5 — Butle DOT i szczególne wyjątki | 1.1.4.7.1 |
| `ADR-B-0448` | Butla wielokrotnego napełniania dopuszczona w USA ma być napełniona w Polsce w celu eksportu zgodnie z ADR 1.1.4.7.2… | § 5 — Butle DOT i szczególne wyjątki | 1.1.4.7.2 |
| `ADR-B-0449` | Przy korzystaniu z ADR 1.1.4.7.2 dla butli DOT przeznaczonej na eksport, według jakich zasad musi odbywać się napełn… | § 5 — Butle DOT i szczególne wyjątki | 1.1.4.7.2(a) |
| `ADR-B-0450` | Naczynie ciśnieniowe DOT korzysta z wyjątku eksportowego ADR 1.1.4.7.2. Jakie przepisy wyznaczają jego oznakowanie i… | § 5 — Butle DOT i szczególne wyjątki | 1.1.4.7.2(b) |
| `ADR-B-0451` | Dla butli DOT przeznaczonej do eksportu w reżimie 1.1.4.7.2 upłynął termin badania okresowego. Czy można ją ponownie… | § 5 — Butle DOT i szczególne wyjątki | 1.1.4.7.2(c) |
| `ADR-B-0452` | Termin badania butli DOT objętej 1.1.4.7.2 upłynął. Czy przepis przewiduje możliwość przewozu jej do wykonania wymag… | § 5 — Butle DOT i szczególne wyjątki | 1.1.4.7.2(c) |
| `ADR-B-0453` | W łańcuchu importu gazu w butli DOT przewoźnik korzysta z ADR 1.1.4.7.1. Jaką specjalną wzmiankę powinien przewidywa… | § 5 — Butle DOT i szczególne wyjątki | 5.4.1.1.24 |
| `ADR-B-0454` | W wywozie gazów w butlach DOT korzystającym z ADR 1.1.4.7.2 jaki wariant wpisu z 5.4.1.1.24 jest właściwy? | § 5 — Butle DOT i szczególne wyjątki | 5.4.1.1.24 |
| `ADR-B-0511` | Po rejsie morskim kierowca przejmuje kontener z opakowanym towarem niebezpiecznym. Sztuki przesyłek są oznakowane zg… | § 1–3 — ADR/IMDG, warunki uznania i dokumentacja | 1.1.4.2.1(a) |

## ADR-B-11 — 43 pytań

| ID | Pytanie / kompetencja sprawdzana | Fragment lekcji porównany | Podstawa z rekordu |
|---|---|---|---|
| `ADR-B-0031` | Co oznacza dla ograniczeń ADR kategoria tunelu A? | § 1 — Kategorie tuneli | 1.9.5.2.2; 8.6 |
| `ADR-B-0032` | Co oznacza kod ograniczeń tunelowych E, jeżeli zgodnie z ADR 8.6 przewóz podlega ograniczeniom tunelowym? | § 2–3 — Kod, sposób przewozu i progi | 8.6.4 |
| `ADR-B-0033` | Przewozisz towar w sztukach przesyłek z kodem ograniczenia tunelowego D/E, a przewóz podlega ograniczeniom tunelowym… | § 2–3 — Kod, sposób przewozu i progi | 8.6.4 |
| `ADR-B-0063` | Gdzie w tabeli A ADR szuka się kodu ograniczeń tunelowych dla danego towaru? | § 2 — Kolumna 15 tabeli A i kod dla całego ładunku | 8.6.3.1 |
| `ADR-B-0064` | Dla jednostki transportowej objętej ograniczeniami ADR przewozisz różne towary mające różne kody tunelowe. Jak ustal… | § 2 — Kolumna 15 tabeli A i kod dla całego ładunku | 8.6.3.2–8.6.3.3 |
| `ADR-B-0065` | Co oznacza zapis „(-)” jako kod ograniczeń tunelowych dla danego towaru? | § 2 — Kolumna 15 tabeli A i kod dla całego ładunku | 8.6.3.1 |
| `ADR-B-0083` | Na trasie znajduje się tunel kategorii E. Przewozisz sztuki przesyłek z kodem tunelowym E, a jednostka podlega ogran… | § 1 — Kategorie tuneli | 8.6.4 |
| `ADR-B-0084` | Jednostka transportowa podlega ograniczeniom tunelowym ADR i przewozi sztuki przesyłek z kodem D/E. Czy wolno jej wj… | § 1 — Kategorie tuneli | 8.6.4 |
| `ADR-B-0085` | Towary są rzeczywiście przewożone zgodnie z wyłączeniami rozdziału ADR 1.1.3. Jednostka transportowa nie wymaga ozna… | § 2 — Kolumna 15 tabeli A i kod dla całego ładunku | 8.6.3.3 |
| `ADR-B-0086` | W jednostce transportowej objętej ADR masz dwa towary z różnymi kodami tunelowymi. Jaki kod obowiązuje dla całego ła… | § 2 — Kolumna 15 tabeli A i kod dla całego ładunku | 8.6.3.2–8.6.3.3 |
| `ADR-B-0143` | W tunelu podczas przewozu ADR wybucha rozwinięty pożar przedziału ładunkowego. Co jest właściwym priorytetem załogi? | § 2 — Kolumna 15 tabeli A i kod dla całego ładunku | 5.4.3.4; program kursu lit. k |
| `ADR-B-0174` | Dla towaru w kolumnie 15 tabeli A widnieje kod tunelowy (-). Jakie znaczenie ma ten zapis? | § 2–3 — Kod, sposób przewozu i progi | 8.6.3.1 |
| `ADR-B-0207` | Na trasie znajdują się tunele kategorii B i E. Które twierdzenie prawidłowo opisuje znaczenie ich kategorii ADR? | § 1 — Kategorie tuneli | 1.9.5.2.2; 8.6.4 |
| `ADR-B-0208` | W dolnej części komórki kolumny 15 tabeli A widnieje zapis „(D/E)”. Czego dotyczy to oznaczenie? | § 2–3 — Kod, sposób przewozu i progi | 8.6.3.1; 8.6.4 |
| `ADR-B-0209` | Jednostka transportowa z towarami pakowanymi w ilościach ograniczonych LQ wymaga oznakowania zgodnie z 3.4.13, z uwz… | § 2–3 — Kod, sposób przewozu i progi | 8.6.3.3; 8.6.4 |
| `ADR-B-0210` | Przy pożarze ciężarówki ADR w tunelu kierowca ma dostęp do oznakowanego wyjścia ewakuacyjnego, a przedział ładunkowy… | § 1 — Kategorie tuneli | 5.4.3.4; 1.9.5 |
| `ADR-B-0248` | Spedytor planuje trasę przez tunel. Gdzie w tabeli A ADR sprawdza się kod ograniczenia tunelowego konkretnego towaru… | § 2 — Kolumna 15 tabeli A i kod dla całego ładunku | 3.2.1 tabela A kolumna (15); 8.6.3.1 |
| `ADR-B-0262` | Znak tunelu podaje kategorię E. Co oznacza taka kategoria w systemie ograniczeń ADR? | § 1 — Kategorie tuneli | 1.9.5.3.6; 8.6.4 |
| `ADR-B-0263` | W jednej jednostce transportowej przewożone są różne towary niebezpieczne o odmiennych kodach tunelowych. Którą zasa… | § 2 — Kolumna 15 tabeli A i kod dla całego ładunku | 8.6.3.2 |
| `ADR-B-0264` | W kolumnie 15 tabeli A dla pozycji UN w miejscu kodu ograniczenia tunelowego występuje znak „(-)”. Co oznacza ten za… | § 2 — Kolumna 15 tabeli A i kod dla całego ładunku | 8.6.3.1 |
| `ADR-B-0308` | W tunelu dochodzi do pożaru przestrzeni ładunkowej pojazdu ADR. Co wynika z instrukcji pisemnych ADR dla załogi? | § 2 — Kolumna 15 tabeli A i kod dla całego ładunku | 5.4.3.4 |
| `ADR-B-0322` | Jednostka transportowa przewozi towary niebezpieczne w ilościach ograniczonych LQ i wymaga oznakowania według 3.4.13… | § 2–3 — Kod, sposób przewozu i progi | 8.6.3.3 i 8.6.4 w związku z 3.4.13–3.4.14 |
| `ADR-B-0430` | Na odcinku trasy znajduje się tunel kategorii A. Jaką ogólną rolę pełni ta kategoria w systemie ograniczeń? | § 1 — Kategorie tuneli | 8.6.3.1; 8.6.4 |
| `ADR-B-0431` | Towar ma kod ograniczenia tunelowego (-) w kolumnie (15) tabeli A. Jak interpretować ten znak? | § 2 — Kolumna 15 tabeli A i kod dla całego ładunku | 8.6.3.1 |
| `ADR-B-0432` | Jednostka przewozi dwa towary ADR z różnymi kodami ograniczeń tunelowych. Jak ustala się zakres ograniczeń? | § 2 — Kolumna 15 tabeli A i kod dla całego ładunku | 8.6.3.2 |
| `ADR-B-0433` | Znak przed tunelem zawiera literę E dla przewozu towarów niebezpiecznych. Do czego odnosi się ograniczenie? | § 1 — Kategorie tuneli | 1.9.5.3.5 |
| `ADR-B-0434` | Jaki element dokumentacji pomaga ustalić kod ograniczenia tunelowego dla towaru ADR? | § 2 — Kolumna 15 tabeli A i kod dla całego ładunku | 8.6.3.1; 3.2 tabela A kol. (15) |
| `ADR-B-0435` | Podczas pożaru przestrzeni ładunkowej w tunelu członek załogi chce ją otworzyć i samodzielnie gasić. Co wynika z ins… | § 2 — Kolumna 15 tabeli A i kod dla całego ładunku | 5.4.3.4 |
| `ADR-B-0487` | Towar ma kod tunelowy D/E i jest przewożony w sztukach przesyłek, z zastosowaniem ograniczeń tunelowych. Do którego … | § 2–3 — Kod, sposób przewozu i progi | 8.6.4, kod D/E |
| `ADR-B-0488` | Dla tego samego kodu tunelowego D/E towar jest przewożony luzem, przy spełnieniu warunków takiego przewozu. Które tu… | § 2–3 — Kod, sposób przewozu i progi | 8.6.4, kod D/E |
| `ADR-B-0489` | Przewóz w sztukach przesyłek ma kod B/D. Jakie tunele wyklucza taki kod dla transportu nieprowadzonego w cysternie? | § 2–3 — Kod, sposób przewozu i progi | 8.6.4, kod B/D |
| `ADR-B-0490` | Materiały wybuchowe objęte kodem tunelowym B1000C mają 1000 kg netto materiału wybuchowego w jednostce transportowej… | § 2–3 — Kod, sposób przewozu i progi | 8.6.4, kod B1000C |
| `ADR-B-0512` | Dyspozytor planuje przejazd przez tunel kategorii E. Jednostka transportowa przewozi towary w ilościach ograniczonyc… | § 1 — Kategorie tuneli | 8.6.4; 3.4.13; 3.4.14 |
| `ADR-B-0539` | Kierowca przewozi na jednej jednostce transportowej dwie przesyłki w sztukach: z kodami tunelowymi D/E i B/D. Na tra… | § 1 — Kategorie tuneli | 8.6.3.2; 8.6.4 |
| `ADR-B-0540` | Ciężarówka przewozi tylko towary w ilościach ograniczonych LQ. Z powodu masy ładunku wymaga oznakowania z ADR 3.4.13… | § 1 — Kategorie tuneli | 3.4.13; 3.4.14; 8.6.4 |
| `ADR-B-0574` | Jedna jednostka transportowa przewozi towary o kodach tunelowych D i E. Jak należy ustalić kod ograniczenia dla całe… | § 2 — Kolumna 15 tabeli A i kod dla całego ładunku | 8.6.3.2 |
| `ADR-B-0575` | Gdzie znaleźć przypisany towarowi ADR kod ograniczenia przewozu przez tunele? | § 2 — Kolumna 15 tabeli A i kod dla całego ładunku | 3.2.1 kolumna 15; 8.6.3.1 |
| `ADR-B-0576` | Towar z kodem D/E jedzie w sztukach przesyłek. Których tuneli nie wolno użyć ze względu na ten kod? | § 2–3 — Kod, sposób przewozu i progi | 8.6.4 |
| `ADR-B-0591` | Pojazd z towarem ADR dojeżdża do tunelu, którego oznakowanie ogranicza przejazd danego rodzaju przewozu. Co powinien… | § 2–3 — Kod, sposób przewozu i progi | 8.6.3; 8.6.4 |
| `ADR-B-0592` | Podczas przejazdu przez tunel dochodzi do pożaru lub innego zdarzenia. Jaka powinna być pierwsza decyzja kierowcy? | § 2 — Kolumna 15 tabeli A i kod dla całego ładunku | 5.4.3.4 |
| `ADR-B-0602` | Na planowanej trasie znajduje się tunel kategorii E, a przewożony towar ma kod tunelowy ograniczający przejazd przez… | § 1 — Kategorie tuneli | 1.9.5.3; 8.6.4 |
| `ADR-B-0603` | W kolumnie 15 tabeli A przy towarze widnieje kod tunelowy „(-)”. Co oznacza to dla ograniczeń tunelowych ADR? | § 2–3 — Kod, sposób przewozu i progi | 3.2.1, kolumna 15; 8.6.3.1 |
| `ADR-B-0604` | Towar ma kod tunelowy D/E i jest przewożony w cysternie. Jakie ograniczenie wynika z tego kodu dla przejazdu przez t… | § 2–3 — Kod, sposób przewozu i progi | 8.6.4 |

## ADR-B-12 — 44 pytań

| ID | Pytanie / kompetencja sprawdzana | Fragment lekcji porównany | Podstawa z rekordu |
|---|---|---|---|
| `ADR-B-0034` | Jaki dokument tożsamości członek załogi powinien posiadać przy sobie podczas przewozu towarów niebezpiecznych objęte… | § 2 — Weryfikacja osób i dostępu | 1.10.1.4 |
| `ADR-B-0035` | Jak według ADR należy zabezpieczyć obszary w terminalach, bazach i na placach wykorzystywane do czasowego składowani… | § 2 — Weryfikacja osób i dostępu | 1.10.1.3 |
| `ADR-B-0036` | Czego powinno dotyczyć szkolenie z ochrony towarów niebezpiecznych? | § 3 — Postój, zabezpieczenia i incydenty | 1.10.2.2 |
| `ADR-B-0066` | Dlaczego obszar terminalu, na którym czasowo składuje się niebezpieczny ładunek podczas transportu, powinien być odp… | § 2 — Weryfikacja osób i dostępu | 1.10.1.3 |
| `ADR-B-0067` | Dwóch członków załogi wykonuje przewóz ADR objęty wymaganiem 1.10.1.4. Drugi ma tylko kartę zakładową bez fotografii… | § 2 — Weryfikacja osób i dostępu | 1.10.1.4 |
| `ADR-B-0120` | Nadawca chce przekazać towary niebezpieczne firmie przewozowej, której tożsamości nie zweryfikowano. Co wynika z ADR… | § 2 — Weryfikacja osób i dostępu | 1.10.1.2 |
| `ADR-B-0121` | Pracownik zauważa ślady możliwej próby nieuprawnionego dostępu do przesyłki ADR. Które działanie powinno obejmować j… | § 3 — Postój, zabezpieczenia i incydenty | 1.10.2.2 |
| `ADR-B-0122` | Firma przewozi towary niebezpieczne dużego ryzyka objęte wymaganiami 1.10.3.2. Co powinna wdrożyć? | § 1 — Tabela towarów dużego ryzyka | 1.10.3.2.1 |
| `ADR-B-0144` | Przy przewozie objętym 8.4.1 ADR jaki postój bez bezpośredniego nadzoru może być dopuszczony? | § 3 — Postój, zabezpieczenia i incydenty | 8.4.1 |
| `ADR-B-0211` | Na rampie pojawia się podwykonawca, który chce odebrać niebezpieczny ładunek. Przedsiębiorstwo nie ustaliło, czy to … | § 2 — Weryfikacja osób i dostępu | 1.10.1.2 |
| `ADR-B-0212` | Przedsiębiorstwo przewozi towary dużego ryzyka objęte 1.10.3.2.2. Czy plan ochrony może ograniczać się do listy nume… | § 1 — Tabela towarów dużego ryzyka | 1.10.3.2.2 |
| `ADR-B-0213` | Firma przewozi towary niebezpieczne dużego ryzyka, do których odnosi się ADR 1.10.3.3. Jak należy traktować zabezpie… | § 1 — Tabela towarów dużego ryzyka | 1.10.3.3 |
| `ADR-B-0249` | Do odbioru towaru ADR zgłasza się niezidentyfikowany przewoźnik, który zna numer zamówienia. Co wynika z zasad ochro… | § 2 — Weryfikacja osób i dostępu | 1.10.1.2 |
| `ADR-B-0274` | Na terminalu tymczasowo składuje się towary niebezpieczne ADR. Plac jest nieoświetlony i ogólnodostępny. Co wymaga p… | § 2 — Weryfikacja osób i dostępu | 1.10.1.3 |
| `ADR-B-0275` | Nowy pracownik ma wykonywać zadania związane z przewozem ADR. Która zasada dotyczy szkolenia z ochrony przed niewłaś… | § 3 — Postój, zabezpieczenia i incydenty | 1.10.2.3 |
| `ADR-B-0300` | Podczas przewozu ADR pasażer pełniący rolę członka załogi nie ma żadnego dokumentu tożsamości ze zdjęciem. Co wymaga… | § 2 — Weryfikacja osób i dostępu | 1.10.1.4 |
| `ADR-B-0304` | Firma przewozi towary niebezpieczne dużego ryzyka w zakresie objętym ADR 1.10.3.2. Który element powinien zawierać p… | § 1 — Tabela towarów dużego ryzyka | 1.10.3.2.2(a) |
| `ADR-B-0305` | Przewożone są towary niebezpieczne dużego ryzyka, do których ma zastosowanie ADR 1.10.3.3. Jakie zabezpieczenie jest… | § 1 — Tabela towarów dużego ryzyka | 1.10.3.3 |
| `ADR-B-0399` | Firma opracowuje plan ochrony dla towarów dużego ryzyka. Jak ma określić odpowiedzialność za ochronę? | § 1 — Tabela towarów dużego ryzyka | 1.10.3.2.2(a) |
| `ADR-B-0400` | Co plan ochrony towarów dużego ryzyka powinien zawierać w zakresie przewożonych materiałów? | § 1 — Tabela towarów dużego ryzyka | 1.10.3.2.2(b) |
| `ADR-B-0401` | Przy ocenie zagrożeń w planie ochrony przeanalizowano tylko jazdę autostradą. Jakie inne miejsca lub etapy trzeba uw… | § 1 i § 3 — Plan ochrony i postój | 1.10.3.2.2(c) |
| `ADR-B-0402` | Plan ochrony towarów dużego ryzyka obejmuje ryzyko na trasie. Co powinien określać w zakresie przeciwdziałania ryzyk… | § 1 — Tabela towarów dużego ryzyka | 1.10.3.2.2(d) |
| `ADR-B-0403` | Firma odnotowała próbę nieuprawnionego dostępu do ładunku dużego ryzyka. Jakie procedury muszą być zawarte w planie … | § 1 — Tabela towarów dużego ryzyka | 1.10.3.2.2(e) |
| `ADR-B-0404` | Firma ma plan ochrony od kilku lat, lecz zmieniła trasę i charakter ładunków. Jakie działania przewiduje ADR? | § 1 i § 3 — Plan ochrony i postój | 1.10.3.2.2(f) |
| `ADR-B-0405` | Dokumenty planu ochrony zawierają informacje o przewozach wysokiego ryzyka. Co powinno być opisane w planie? | § 1 i § 3 — Plan ochrony i postój | 1.10.3.2.2(g) |
| `ADR-B-0406` | Kto powinien otrzymywać szczegółowe informacje o przewozie dużego ryzyka w ramach zasad ochrony? | § 1 — Tabela towarów dużego ryzyka | 1.10.3.2.2(h) |
| `ADR-B-0407` | Pojazd przewozi towary dużego ryzyka objęte 1.10.3.3. Kiedy urządzenia zabezpieczające przed kradzieżą mają być skut… | § 1 — Tabela towarów dużego ryzyka | 1.10.3.3 |
| `ADR-B-0408` | Montaż blokady antykradzieżowej pojazdu dużego ryzyka uniemożliwiłby ratownikom dostęp w wypadku. Jak ocenić takie r… | § 1 — Tabela towarów dużego ryzyka | 1.10.3.3 |
| `ADR-B-0409` | Nowy pracownik poznaje zagrożenia związane z niewłaściwym wykorzystaniem towarów niebezpiecznych. Co obejmuje właści… | § 3 — Postój, zabezpieczenia i incydenty | 1.10.2.2 |
| `ADR-B-0410` | Pracownik ma dostęp do planu ochrony dotyczącego swoich zadań. Co powinno obejmować jego szkolenie? | § 3 — Postój, zabezpieczenia i incydenty | 1.10.2.2 |
| `ADR-B-0411` | Kiedy należy przeprowadzać wymagane szkolenie z ochrony dla osób uczestniczących w przewozie ADR? | § 3 — Postój, zabezpieczenia i incydenty | 1.10.2.3 |
| `ADR-B-0412` | Inspektor wymaga dokumentacji szkoleń dotyczących ochrony. Jak powinien postąpić pracodawca? | § 3 — Postój, zabezpieczenia i incydenty | 1.10.2.4 |
| `ADR-B-0413` | Do terminalu zgłasza się kierowca po odbiór towarów niebezpiecznych. Skąd można ustalić, czy reprezentuje właściwego… | § 2 — Weryfikacja osób i dostępu | 1.10.1.2 |
| `ADR-B-0414` | Przedsiębiorstwo przekazuje ładunek ADR nowemu przewoźnikowi. Ten zna numer zlecenia, ale jego tożsamość nie została… | § 2 — Weryfikacja osób i dostępu | 1.10.1.2 |
| `ADR-B-0415` | W terminalu do czasowego składowania niebezpiecznych przesyłek prowadzi niekontrolowane wejście od ulicy. Jakie dzia… | § 2 — Weryfikacja osób i dostępu | 1.10.1.3 |
| `ADR-B-0416` | W trakcie przewozu ADR kierowca ma dowód ze zdjęciem, ale drugi członek załogi ma wyłącznie identyfikator bez fotogr… | § 2 — Weryfikacja osób i dostępu | 1.10.1.4 |
| `ADR-B-0455` | Dla towarów niebezpiecznych innych niż klasa 7, gdzie ADR określa wykaz i progi uznania za towary dużego ryzyka? | § 1 — Tabela towarów dużego ryzyka | 1.10.3.1.2 |
| `ADR-B-0456` | W tabeli 1.10.3.1.2 obok zagrożenia podano próg 3000 l dla przewozu w cysternie. Czy taki próg wolno automatycznie z… | § 1 — Tabela towarów dużego ryzyka | 1.10.3.1.2 (tabela i przypis c) |
| `ADR-B-0457` | W tabeli 1.10.3.1.2 przy danym zagrożeniu w kolumnie przewozu w sztukach przesyłek podano oznaczenie przypisu b. Co … | § 1 — Tabela towarów dużego ryzyka | 1.10.3.1.2 przypis b |
| `ADR-B-0458` | W tabeli 1.10.3.1.2 przy rodzaju przewozu wpisano literę a. Jak rozumieć taki zapis? | § 1 — Tabela towarów dużego ryzyka | 1.10.3.1.2 przypis a |
| `ADR-B-0459` | Dla danego towaru w tabeli ochrony 1.10.3.1.2 występuje próg 0 kg dla sztuk przesyłek. Co to oznacza przy przewozie … | § 1 — Tabela towarów dużego ryzyka | 1.10.3.1.2 |
| `ADR-B-0460` | Czy fakt, że materiał jest w klasie 3, automatycznie oznacza zaliczenie do towarów niebezpiecznych dużego ryzyka we … | § 1 — Tabela towarów dużego ryzyka | 1.10.3.1.2 tabela klasa 3 |
| `ADR-B-0519` | Na parkingu przed rozpoczęciem dalszego przewozu ADR kontrolujący prosi obu członków załogi o okazanie dokumentu toż… | § 2 — Weryfikacja osób i dostępu | 1.10.1.4 |
| `ADR-B-0582` | Przewóz towaru dużego ryzyka wymaga uwzględnienia zabezpieczenia podczas postoju. Co powinien obejmować plan ochrony… | § 1 — Tabela towarów dużego ryzyka | 1.10.3.2; 1.10.3.3 |


## Status

- Zmiany dotyczą wyłącznie kursu podstawowego.
- Wszystkie pytania pozostają `needs_review`; niczego nie oznaczono jako `verified`.
- Następna partia: B-13.
