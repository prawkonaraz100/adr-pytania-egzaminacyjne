# Kontrola druga – partia 47 (ADR-B-0691–0705)

Main 66dac0440 (po scaleniu #925), bank blob `092325a21fe95a47406e2d28e4947885c19dc0dc`. Źródło: Dz.U. 2025 poz. 642 (+ sprostowanie poz. 1575); strony według nagłówka „Dziennik Ustaw — NNN —”. Nic nie oznaczono jako verified.

**Wynik: OK 0 / POPRAW 15 / BLOKUJ 0.** 10 nowych elementów z tej samej kompetencji (0692, 0693, 0695, 0697, 0698, 0699, 0701, 0702, 0704, 0705), 5 przeredagowań z zachowaniem tematu (0691, 0694, 0696, 0700, 0703). Bez cystern; litery kluczy, moduły i kompetencje bez zmian; liczba pytań 780 bez zmian.

**Pozostało pytań bez porównania dosłownego: 75** (0706–0780).

| ID | Kompetencja | Klucz | #925 | Kontrola 2 | Decyzja | Długości A/B/C |
|---|---|---|---|---|---|---|
| ADR-B-0691 | 05-K03 | B | POPRAW | POPRAW | PRZEREDAGOWANIE (temat zachowany: powiadomienie służb bez zwłoki mimo prośby dyspozytora; dopisany 1.4.1.2 „niezwłocznie”) | 73/70/64 |
| ADR-B-0692 | 05-K04 | B | POPRAW | POPRAW | NOWY ELEMENT (stare: zmiana kierunku wiatru → ponownie strona nawietrzna = 0741, też 0106/0183) | 60/65/68 |
| ADR-B-0693 | 05-K10 | B | POPRAW | POPRAW | NOWY ELEMENT (stare: kamizelka przed ustawieniem znaków = 0112/0168 – temat wyczerpany) | 80/76/72 |
| ADR-B-0694 | 06-K05 | B | POPRAW | POPRAW | PRZEREDAGOWANIE (temat zachowany: tylna tablica zasłonięta kołem zapasowym) | 66/73/73 |
| ADR-B-0695 | 05-K05 | A | POPRAW | POPRAW | NOWY ELEMENT (stare: mały pożar komory silnika = 0108/0184 – temat K06 w kompetencji K05) | 64/67/62 |
| ADR-B-0696 | 05-K07 | C | POPRAW | POPRAW | PRZEREDAGOWANIE (temat zachowany: dokument w zadymionej kabinie) | 70/55/66 |
| ADR-B-0697 | 05-K09 | B | POPRAW | POPRAW | NOWY ELEMENT (stare: ostrzeganie osób z bezpiecznego miejsca = 0111/0186 – temat wyczerpany) | 64/64/58 |
| ADR-B-0698 | 06-K04 | B | POPRAW | POPRAW | NOWY ELEMENT (stare: litera X – woda tylko za zgodą specjalistów = 0170/0752) | 61/68/69 |
| ADR-B-0699 | 08-K04 | B | POPRAW | POPRAW | NOWY ELEMENT (stare: rozmiar klina do masy i kół = 0023) | 65/70/74 |
| ADR-B-0700 | 09-K06 | B | POPRAW | POPRAW | PRZEREDAGOWANIE (temat zachowany: pasy deformują elastyczny kontener do przewozu luzem, 7.5.7.6.2) | 70/65/65 |
| ADR-B-0701 | 12-K02 | B | POPRAW | POPRAW | NOWY ELEMENT (stare: plac czasowego składowania zabezpieczony i oświetlony = 0035/0775) | 72/70/68 |
| ADR-B-0702 | 05-K06 | B | POPRAW | POPRAW | NOWY ELEMENT (stare: pożar opony przechodzi na ładownię = 0742 – pożar ładowni wyczerpany; wariant „podejście od strony nawietrznej” = 0641) | 63/64/75 |
| ADR-B-0703 | 09-K02 | A | POPRAW | POPRAW | PRZEREDAGOWANIE (temat zachowany: ponowne unieruchomienie po częściowym rozładunku) | 68/71/63 |
| ADR-B-0704 | 05-K12 | B | POPRAW | POPRAW | NOWY ELEMENT (stare: gaśnica w uchwycie na klucz = 0169/0585/0015 – 8.1.4.5 wyczerpany) | 64/64/64 |
| ADR-B-0705 | 08-K06 | B | POPRAW | POPRAW | NOWY ELEMENT (stare: rękawice i ochrona oczu dla drugiego członka załogi = 0763/0024) | 73/69/66 |

## Błędy w raporcie #925

1. **Zamienniki wracają do zdublowanego tematu**: w 11 z 15 propozycji (0691, 0692, 0693, 0695, 0697, 0698, 0699, 0701, 0702, 0704, 0705) zamiennik powtarzał ten sam, już zdublowany temat albo temat wyczerpany; 0695 przeniesiono na pożar przedziału ładunkowego (0107/0166/0614).
2. **Przeoczone duplikaty**: 0702 = 0742 (wskazano 0743); 0695 = 0108/0184 (temat K06 w kompetencji K05); przy 0691 błędnie wskazano 0588 (moduł 13), pominięto 0220/0594. Także pierwszy wariant mojego zamiennika 0702 (podejście od strony nawietrznej) okazał się = 0641 – wykrył to check_near_duplicates, więc wymieniłem go na gaśnicę 2 kg do pożaru kabiny.
3. **Forma**: wszystkie 15 oryginałów miało kropki na końcu opcji, 14 – opcje > 80 zn.; w sources wpisy angielskie i „tom II, s. 248/251/270” (strony wydania angielskiego) – w nowych rekordach jeden polski wpis na punkt.
4. **Słusznie**: wszystkie 15 POPRAW; duplikaty 0692 – 0741, 0698 – 0170/0752, 0699 – 0023, 0701 – 0035/0775, 0705 – 0763; licznik 90 → 75; strony Dz.U. 953, 956, 975, 1308, 1309, 1325 i 110 trafne.

## Szczegóły

### ADR-B-0691 – POPRAW (PRZEREDAGOWANIE (temat zachowany: powiadomienie służb bez zwłoki mimo prośby dyspozytora; dopisany 1.4.1.2 „niezwłocznie”))

- Cytaty i strony Dz.U. (nagłówek strony): 5.4.3.4 (s. 975): „Powiadomić właściwe służby ratownicze, podając możliwie wszystkie dostępne informacje o wypadku lub awarii oraz towarach niebezpiecznych”; 1.4.1.2 (s. 55): w razie bezpośredniego zagrożenia bezpieczeństwa publicznego uczestnicy przewozu „powinni niezwłocznie powiadomić służby ratownicze i bezpieczeństwa …”.
- Raport #925: zgoda co do POPRAW; jako pokrewne błędnie wskazano 0588 (moduł 13), pominięto 0220/0594
- Nowa treść: Po awarii kierowca stoi już w bezpiecznym miejscu, a z pojazdu wydobywa się dym. Dyspozytor przewoźnika prosi przez telefon, by nie wzywał służb, dopóki firma nie ustali przyczyny. Jak powinien postąpić kierowca?
- Klucz B: Niezwłocznie powiadomić służby ratownicze i przekazać im dostępne dane
- Źródło: ADR 2025, 5.4.3.4 (instrukcje pisemne: powiadomienie właściwych służb ratowniczych); 1.4.1.2
- Uwagi: 5.4.3.4 s. 975; 1.4.1.2 s. 55. Odrębne od 0105/0165 (treść zgłoszenia), 0220 (kto zgłasza), 0594, 0740.

### ADR-B-0692 – POPRAW (NOWY ELEMENT (stare: zmiana kierunku wiatru → ponownie strona nawietrzna = 0741, też 0106/0183))

- Cytaty i strony Dz.U. (nagłówek strony): 5.4.3.4 (s. 975): „Oddalić się z miejsca wypadku lub awarii …”, „unikać wdychania oparów, dymu, pyłu i pary, pozostając po stronie nawietrznej”, „unikać źródeł zapłonu … nie włączać i nie wyłączać urządzeń elektrycznych”; nalepka 8 (s. 977): uwolnione materiały mogą wydzielać żrące pary.
- Raport #925: zgoda (= 0741); zamiennik nadal o zmianie kierunku wiatru
- Nowa treść: Z pękniętego kanistra z nalepką 8 na skrzyni wycieka ciecz, która wydziela drażniące opary. Wiatr niesie je od skrzyni w stronę kabiny. Pomocnik proponuje przeczekać w kabinie do przyjazdu służb. Co zalecają instrukcje pisemne?
- Klucz B: Wysiąść i odejść na stronę nawietrzną, z dala od wycieku i oparów
- Źródło: ADR 2025, 5.4.3.4 (instrukcje pisemne: oddalić się, pozostawać po stronie nawietrznej, unikać źródeł zapłonu; tabela nalepek – nalepka 8)
- Uwagi: 5.4.3.4: czynności ogólne s. 975, nalepka 8 („uwolnione materiały mogą wydzielać żrące pary”) s. 977. Do oceny specjalisty: 0183 ma kabinę jako dystraktor; K04 nasycona.

### ADR-B-0693 – POPRAW (NOWY ELEMENT (stare: kamizelka przed ustawieniem znaków = 0112/0168 – temat wyczerpany))

- Cytaty i strony Dz.U. (nagłówek strony): 8.1.5.2 (s. 1325): w jednostce transportowej „dwa stojące znaki ostrzegawcze”; 5.4.3.4 (s. 978) – ten sam wykaz wyposażenia w instrukcjach pisemnych.
- Raport #925: zgoda (temat wyczerpany); zamiennik nadal o kamizelce i znakach
- Nowa treść: Przed wyjazdem kierowca sprawdza wyposażenie ADR. W kabinie nie ma stojących znaków ostrzegawczych. Kierownik twierdzi, że zastępuje je odblaskowe oznakowanie konturowe naczepy razem ze światłami awaryjnymi. Co wynika z ADR?
- Klucz B: Przed wyjazdem trzeba uzupełnić wyposażenie o dwa stojące znaki ostrzegawcze
- Źródło: ADR 2025, 8.1.5.2 (dwa stojące znaki ostrzegawcze); 5.4.3.4 (instrukcje pisemne: odpowiednio umieścić stojące znaki ostrzegawcze)
- Uwagi: 8.1.5.2 s. 1325; 5.4.3.4 s. 975 i 978 (wykaz wyposażenia). Odrębne od 0112/0168/0633 (czynności) i 0747 (liczba kamizelek).

### ADR-B-0694 – POPRAW (PRZEREDAGOWANIE (temat zachowany: tylna tablica zasłonięta kołem zapasowym))

- Cytaty i strony Dz.U. (nagłówek strony): 5.3.2.1.1 (s. 953): dwie prostokątne tablice barwy pomarańczowej, jedna z przodu, druga z tyłu jednostki transportowej, umieszczone prostopadle do osi podłużnej i „dobrze widoczne”.
- Raport #925: zgoda; temat zachowany
- Nowa treść: Przed wyjazdem kierowca sprawdza oznakowanie. Przednia tablica barwy pomarańczowej jest dobrze widoczna, ale tylną zasłania koło zapasowe zamontowane z tyłu pojazdu. Co powinien zrobić?
- Klucz B: Odsłonić tylną tablicę, tak aby była dobrze widoczna i prostopadła do osi
- Źródło: ADR 2025, 5.3.2.1.1
- Uwagi: 5.3.2.1.1 s. 953. Temat bez odpowiednika (0018/0191/0258/0753 – wymiary, 0634 – odłączona przyczepa).

### ADR-B-0695 – POPRAW (NOWY ELEMENT (stare: mały pożar komory silnika = 0108/0184 – temat K06 w kompetencji K05))

- Cytaty i strony Dz.U. (nagłówek strony): 5.4.3.4 (s. 975): „Członkowie załogi pojazdu nie powinni gasić pożaru obejmującego przedział ładunkowy”; 8.1.4.1 (s. 1324, tabela – obraz strony): pojazd > 7,5 t – co najmniej 2 gaśnice, 12 kg, w tym co najmniej jedna 6 kg.
- Raport #925: zgoda co do POPRAW, ale przeoczono 0108/0184 (temat K06); zamiennik przeniesiony na pożar ładowni (temat wyczerpany: 0107/0166/0614)
- Nowa treść: Ciężarówka o dopuszczalnej masie całkowitej 18 t ma gaśnice o łącznej pojemności 12 kg, w tym jedną 6 kg. Na postoju zaczynają się palić beczki w przestrzeni ładunkowej. Pomocnik uważa, że duża gaśnica służy właśnie do gaszenia ładunku. Co mówią instrukcje pisemne?
- Klucz A: Załoga nie powinna gasić pożaru obejmującego przedział ładunkowy
- Źródło: ADR 2025, 5.4.3.4 (instrukcje pisemne: członkowie załogi nie powinni gasić pożaru obejmującego przedział ładunkowy); 8.1.4.1
- Uwagi: 5.4.3.4 s. 975; 8.1.4.1 s. 1324–1325 (tabela – obraz strony). Odrębne od 0107/0166/0222/0614/0742 (nowe nieporozumienie: duża gaśnica).

### ADR-B-0696 – POPRAW (PRZEREDAGOWANIE (temat zachowany: dokument w zadymionej kabinie))

- Cytaty i strony Dz.U. (nagłówek strony): 5.4.3.4 (s. 975): czynności wykonuje się, „jeżeli jest to możliwe i bezpieczne”; dokumenty przewozowe mają być łatwo dostępne dla służb ratowniczych po ich przybyciu.
- Raport #925: zgoda; temat zachowany
- Nowa treść: Po awarii kierowca stoi w bezpiecznym miejscu. Dokument przewozowy został w kabinie, do której zbliża się dym. Przyjeżdżają ratownicy. Jak kierowca powinien zapewnić im dostęp do informacji o ładunku?
- Klucz C: Podać, co wie o ładunku, i wskazać ratownikom, gdzie leży dokument
- Źródło: ADR 2025, 5.4.3.4 (instrukcje pisemne: czynności, jeżeli jest to możliwe i bezpieczne; łatwy dostęp ratowników do dokumentów przewozowych)
- Uwagi: 5.4.3.4 s. 975. Odrębne od 0185 (dostęp bezpieczny) i 0109/0229/0630/0744.

### ADR-B-0697 – POPRAW (NOWY ELEMENT (stare: ostrzeganie osób z bezpiecznego miejsca = 0111/0186 – temat wyczerpany))

- Cytaty i strony Dz.U. (nagłówek strony): 5.4.3.4 (s. 975): „Oddalić się z miejsca wypadku lub awarii, poinformować inne osoby o konieczności oddalenia się …”, „unikać wdychania oparów … pozostając po stronie nawietrznej”; nalepka 6.1 (s. 977): zagrożenie zatruciem w wyniku wdychania, kontaktu ze skórą lub spożycia.
- Raport #925: zgoda (temat wyczerpany); zamiennik nadal o ostrzeganiu osób
- Nowa treść: Po wypadku z uszkodzonej beczki z nalepką 6.1 wydobywają się opary. Wiatr niesie je wzdłuż drogi w stronę przystanku, na którym czekają ludzie. Kierowca może ich bezpiecznie zawołać. Dokąd powinien ich odesłać?
- Klucz B: W bok, poza pas oparów niesionych przez wiatr, z dala od wypadku
- Źródło: ADR 2025, 5.4.3.4 (instrukcje pisemne: oddalić się i poinformować inne osoby, unikać wdychania oparów; tabela nalepek – nalepka 6.1)
- Uwagi: 5.4.3.4: czynności s. 975, nalepka 6.1 s. 977. Odrębne od 0111/0186/0224/0632/0746. Do oceny specjalisty: kierunek ewakuacji osób postronnych.

### ADR-B-0698 – POPRAW (NOWY ELEMENT (stare: litera X – woda tylko za zgodą specjalistów = 0170/0752))

- Cytaty i strony Dz.U. (nagłówek strony): 5.3.2.3.1 (s. 956): litera X przed numerem rozpoznawczym zagrożenia oznacza, że materiał reaguje niebezpiecznie z wodą; 5.3.2.3.2 (s. 957–958): „423 materiał stały, reagujący z wodą, wydzielający gazy palne …”; nalepka 4.3 (s. 976): „Utrzymywać uwolnione materiały w stanie suchym, pod przykryciem”.
- Raport #925: zgoda (= 0170/0752); zamiennik nadal o literze X i zgodzie specjalistów
- Nowa treść: Na tablicy barwy pomarańczowej u góry jest numer 423, bez litery X. Z pękniętego worka wysypał się materiał. Pracownik chce go spłukać wodą, bo skoro nie ma X, woda nie zaszkodzi. Co kierowca powinien mu odpowiedzieć?
- Klucz B: Nie, bo 423 oznacza materiał stały, który z wodą wydziela gazy palne
- Źródło: ADR 2025, 5.3.2.3.1 (litera X); 5.3.2.3.2 (numer 423); 5.4.3.4 (instrukcje pisemne – nalepka 4.3)
- Uwagi: 5.3.2.3.1 (zdanie o X) s. 956; 423 s. 957–958; nalepka 4.3 s. 976. Odrębne od 0017/0170/0256/0615/0752.

### ADR-B-0699 – POPRAW (NOWY ELEMENT (stare: rozmiar klina do masy i kół = 0023))

- Cytaty i strony Dz.U. (nagłówek strony): 3.4.1 (h) (s. 686, obraz strony): przy przewozie towarów zapakowanych w ilościach ograniczonych nie stosuje się przepisów „Części 8, z wyjątkiem 8.2.3, 8.6.3.3 i 8.6.4”; 8.1.5.2 (s. 1325) – klin pod koło w wyposażeniu.
- Raport #925: zgoda (= 0023); zamiennik nadal o rozmiarze klina
- Nowa treść: Ciężarówka wiezie same kartony z towarami niebezpiecznymi zapakowanymi w ilościach ograniczonych (LQ) zgodnie z działem 3.4. Kontroler zauważa, że w pojeździe nie ma klina pod koła. Czy to naruszenie ADR?
- Klucz B: Nie, przy przewozie LQ nie stosuje się wymagań 8.1.5 co do wyposażenia
- Źródło: ADR 2025, 3.4.1 (h) (część 8: tylko 8.2.3, 8.6.3.3 i 8.6.4); 8.1.5.2
- Uwagi: 3.4.1 s. 686 (sprawdzone na obrazie strony: „Części 8, 8.2.3, 8.6.3.3 i 8.6.4”); 8.1.5.2 s. 1325. Odrębne od 0761 (1.1.3.6).

### ADR-B-0700 – POPRAW (PRZEREDAGOWANIE (temat zachowany: pasy deformują elastyczny kontener do przewozu luzem, 7.5.7.6.2))

- Cytaty i strony Dz.U. (nagłówek strony): 7.5.7.6.2 (s. 1309): elastyczne kontenery do przewozu luzem mocuje się tak, aby nie uległy uszkodzeniu – środki mocujące nie mogą ich deformować ani uszkadzać.
- Raport #925: zgoda; temat zachowany
- Nowa treść: Kierowca mocuje elastyczny kontener do przewozu luzem na skrzyni o sztywnych burtach. Pasy są tak mocno napięte, że widocznie wgniatają ściany kontenera. Co powinien zrobić przed wyjazdem?
- Klucz B: Poluzować pasy i unieruchomić kontener tak, by go nie deformowały
- Źródło: ADR 2025, 7.5.7.6.2
- Uwagi: 7.5.7.6.2 s. 1309. Odrębne od 0060/0079/0236 (sztuki przesyłek, 7.5.7.1).

### ADR-B-0701 – POPRAW (NOWY ELEMENT (stare: plac czasowego składowania zabezpieczony i oświetlony = 0035/0775))

- Cytaty i strony Dz.U. (nagłówek strony): 1.2.1 (s. 44), definicja „przewóz”: obejmuje także krótkotrwałe składowanie towarów niebezpiecznych w związku ze zmianą rodzaju lub środka transportu (przeładunek), pod warunkiem okazania na żądanie dokumentów przewozowych z miejscem wydania i odbioru oraz że sztuki przesyłek nie były otwierane, z wyjątkiem kontroli przez właściwe władze; 1.10.1.3 (s. 110) – miejsca czasowego składowania.
- Raport #925: zgoda (= 0035/0775); zamiennik nadal o zabezpieczeniu placu
- Nowa treść: Kartony z towarami niebezpiecznymi czekają kilka godzin w terminalu na przeładunek na inną ciężarówkę. Kiedy według definicji „przewóz” w 1.2.1 takie krótkotrwałe składowanie jest częścią przewozu, do której stosuje się 1.10.1.3?
- Klucz B: Gdy są dokumenty przewozowe, a sztuk nie otwierano poza kontrolą władz
- Źródło: ADR 2025, 1.2.1 (definicja „przewóz” – krótkotrwałe składowanie przy przeładunku); 1.10.1.3
- Uwagi: 1.2.1 s. 44; 1.10.1.3 s. 110. Odrębne od 0035/0066/0274/0415/0775. Do oceny specjalisty: definicja przewozu w module ochrony.

### ADR-B-0702 – POPRAW (NOWY ELEMENT (stare: pożar opony przechodzi na ładownię = 0742 – pożar ładowni wyczerpany; wariant „podejście od strony nawietrznej” = 0641))

- Cytaty i strony Dz.U. (nagłówek strony): 8.1.4.1 (s. 1324, tabela – obraz strony), kolumna (3): „Gaśnica do gaszenia pożaru silnika lub kabiny. Co najmniej jedna o minimalnej pojemności: 2 kg”; 5.4.3.4 (s. 975): załoga nie gasi pożaru przedziału ładunkowego.
- Raport #925: zgoda co do POPRAW, ale duplikat wskazany błędnie (0743 zamiast 0742); zamiennik nadal o pożarze przechodzącym na ładownię
- Nowa treść: Na parkingu pod deską rozdzielczą w kabinie zaczyna się tlić przewód. Ogień jest mały, ładunek nie jest zagrożony, a kierowca może działać bez narażania się. Do jakiego pożaru ADR przeznacza wymaganą gaśnicę 2 kg?
- Klucz B: Do pożaru silnika lub kabiny, więc w tej sytuacji można jej użyć
- Źródło: ADR 2025, 8.1.4.1 (tabela, kolumna 3: gaśnica do gaszenia pożaru silnika lub kabiny, co najmniej 2 kg); 5.4.3.4 (instrukcje pisemne: nie gasić pożaru przedziału ładunkowego)
- Uwagi: 8.1.4.1 s. 1324 (kolumna 3); 5.4.3.4 s. 975. Podejście od strony nawietrznej = 0641 (pierwszy projekt odrzucony). Blisko 0223 (gaśnica 2 kg do pożaru silnika) – do oceny specjalisty; instrukcje pisemne wymieniają pożar opon, hamulców i silnika, nie kabiny.

### ADR-B-0703 – POPRAW (PRZEREDAGOWANIE (temat zachowany: ponowne unieruchomienie po częściowym rozładunku))

- Cytaty i strony Dz.U. (nagłówek strony): 7.5.7.1 (s. 1308–1309): sztuki przesyłek powinny być zabezpieczone (pasy, przekładki, wypełnienie wolnych przestrzeni) tak, aby podczas przewozu nie zmieniły położenia.
- Raport #925: zgoda; temat zachowany
- Nowa treść: W trakcie dostawy do kilku odbiorców kierowca rozładował część skrzyń z towarami niebezpiecznymi. Pozostałe skrzynie stoją luzem, a obok nich powstała wolna przestrzeń, w którą mogą się przesunąć przy hamowaniu. Co powinien zrobić przed dalszą jazdą?
- Klucz A: Ułożyć pozostałe skrzynie ponownie i unieruchomić je na resztę trasy
- Źródło: ADR 2025, 7.5.7.1
- Uwagi: 7.5.7.1 s. 1308–1309. Odrębne od 0026/0079/0235/0628/0764.

### ADR-B-0704 – POPRAW (NOWY ELEMENT (stare: gaśnica w uchwycie na klucz = 0169/0585/0015 – 8.1.4.5 wyczerpany))

- Cytaty i strony Dz.U. (nagłówek strony): 8.1.4.3 (s. 1325): „Jeżeli pojazd wyposażony jest w gaśnicę stałą, uruchamianą automatycznie w przypadku pożaru silnika lub w inny łatwy sposób, to gaśnica przenośna odpowiednia do zwalczania pożaru silnika nie jest wymagana.”; 8.1.4.5 (s. 1325): gaśnice „łatwo dostępne dla załogi pojazdu”.
- Raport #925: zgoda (8.1.4.5 wyczerpany); zamiennik nadal o dostępności gaśnicy
- Nowa treść: Pojazd ADR ma w komorze silnika stałą instalację gaśniczą, która uruchamia się automatycznie w razie pożaru silnika. Przewoźnik pyta, czy przenośna gaśnica odpowiednia do zwalczania pożaru silnika jest wtedy nadal wymagana. Co wynika z 8.1.4.3?
- Klucz B: Nie, wtedy przenośna gaśnica do pożaru silnika nie jest wymagana
- Źródło: ADR 2025, 8.1.4.3 (gaśnica stała do pożaru silnika); 8.1.4.1; 8.1.4.5
- Uwagi: 8.1.4.3 i 8.1.4.5 s. 1325; 8.1.4.1 s. 1324–1325. Do oceny specjalisty: wpływ na łączną pojemność z tabeli 8.1.4.1; kompetencja K12 – przepis sąsiedni.

### ADR-B-0705 – POPRAW (NOWY ELEMENT (stare: rękawice i ochrona oczu dla drugiego członka załogi = 0763/0024))

- Cytaty i strony Dz.U. (nagłówek strony): 8.1.5.2 (s. 1325): dla każdego członka załogi „para rękawic ochronnych” i „środek ochrony oczu (np. okulary ochronne)”; „płyn do płukania oczu” z przypisem – niewymagany przy nalepkach 1, 1.4, 1.5, 1.6, 2.1, 2.2 i 2.3.
- Raport #925: zgoda (= 0763); zamiennik nadal o wyposażeniu każdego członka załogi
- Nowa treść: Jednostka wiezie na pełnych zasadach ADR same butle z gazem z nalepką 2.2. Przewoźnik wie, że płyn do płukania oczu nie jest wtedy wymagany, i chce zabrać z pojazdu także rękawice i okulary ochronne. Czy może?
- Klucz B: Nie, przypis zwalnia z płynu, ale nie z rękawic i ochrony oczu załogi
- Źródło: ADR 2025, 8.1.5.2 (rękawice i ochrona oczu dla każdego członka załogi; przypis: płyn do płukania oczu niewymagany m.in. przy nalepce 2.2)
- Uwagi: 8.1.5.2 s. 1325. Odrębne od 0483 (płyn przy 2.3), 0763, 0024, 0076.

## Wskaźniki

- „Poprawna = jedyna najdłuższa”: **20/780 = 2,56% → 17/780 = 2,18%** (stare 0698, 0700, 0702 miały klucz jako jedyną najdłuższą opcję); maksimum działu 5,66% bez zmian. Wskaźnik poprawiony w docs/POKRYCIE-KURSU.md, docs/STAN-KONCOWY-BANKU-ADR-PODSTAWOWY-2026-11-03.md i podstawowy/README.md.
- „Poprawna = jedyna najkrótsza”: **85/780 → 83/780**; każdy dział ≤ 38% (maks. 17,2%; dział 05: 16 → 15/87, dział 09: 6 → 5/62).
- Żadna opcja nowych rekordów nie kończy się kropką, nie ma średnika ani słów absolutnych, wszystkie ≤ 80 zn.; klucz nigdy nie jest jedyną najdłuższą ani jedyną najkrótszą. Objaśnienia: 4–5 zdań, 352–502 znaków, ≤ 28 słów w zdaniu, ostatnie zdanie „Podstawa: ADR …”.
- similarity.py: cały bank – main **7 par ≥ 0,45 / 154 ≥ 0,25**; po poprawkach **7 / 154**. Pary z partią: main **0 / 3** (0691/0746 = 0,286; 0185/0696 = 0,278; 0695/0743 = 0,261); po poprawkach **0 / 3** (0483/0705 = 0,385 – płyn do płukania oczu przy 2.3, inny przypadek; 0698/0752 = 0,267 – X a numer 423; 0484/0705 = 0,250). check_near_duplicates (0,60) i check_cross_module_duplicates (0,80) – bez kandydatów. Wyszukiwanie po temacie w całym banku: kabina jako schronienie, oznakowanie konturowe a znaki, duża gaśnica a ładunek, kierunek ewakuacji osób, 423 bez X, LQ a klin, przypis do płynu do płukania oczu, definicja przewozu przy przeładunku, gaśnica do kabiny, gaśnica stała silnika – brak duplikatów (pokrewne: 0183, 0223, 0483, 0641, 0761).
- Kompetencje: liczby bez zmian; 05-K13, 05-K14, 05-K15 nadal po 5; kompetencje.json bez zmian.

## Synchronizacja (test na kopii repo)

- review/sequential/ i review/legal-clauses/: 691-691.json … 705-705.json – snapshoty; w legal-clauses clause, answer_review A/B/C, notes_on_conditions.
- Ledger z PAKIET-0780-MANIFEST (review/legal-polish/stage4w4-literal-verification-ledger-0610-0678.json) – 15 wpisów.
- Egzaminy 001–005: ŻADEN wariant nie zawiera 0691–0705 – zmienia się tylko SHA (10 plików). Kolejki 4X40/4X44 – tylko SHA. Scenariusze bez zmian.
- SHA 092325a2… → e92048bd… w 50 plikach; zostaje tylko w review/literal-pl/ i jako FIRST_PASS_BANK_SHA w tests/test_literal_review_0691_0705.py.
- REJESTR-AKTUALNY-0001-0765.md i 0001-0780.md – po 15 wierszy.
- Lekcje i instruktor: ADR-B-05 (stare sekcje przepięte na 0741, 0168, 0108, 0186, 0742, 0169 + nowe sekcje 0692, 0693, 0695, 0697, 0702, 0704; 0691 – dopisany 1.4.1.2; usunięte „tom II, s. 270”), ADR-B-06 (stara sekcja X → 0170 + nowa sekcja 423 bez X; 0694 – „tom II, s. 248” usunięte), ADR-B-08 (klin → 0023 + sekcja LQ; wyposażenie załogi → 0763 + sekcja przypisu), ADR-B-12 (plac składowania → 0035 + sekcja definicji przewozu).

## Wynik testu

Git worktree z main 66dac0440 + POPRAWKI + synchronizacja: 14 skryptów CI zielonych (validate, coverage, check_mock_exam_variants, answer_leakage_metrics, answer_length_bias --threshold 0.16 --strict, check_explanation_quality --minimum 300, check_near_duplicates 0.60, check_cross_module_duplicates 0.80, similarity, check_explanation_heuristics, release_gate --report, check_sequential_audit, check_legal_clause_review, course_consistency); `python3 -m unittest discover -s tests` – **255/255 OK**. Blob banku po zastosowaniu: `e92048bdde4e05422e3265542636b6213f3e10b4`.

## Do pakietu dla specjalistów

- 0692 – kompetencja 05-K04 nasycona; 0183 ma „pozostanie w kabinie” jako dystraktor – czy oba pytania mogą zostać obok siebie.
- 0697 – kierunek ewakuacji osób postronnych („w bok, poza pas oparów”) – ADR mówi tylko o oddaleniu się i stronie nawietrznej.
- 0699 – 3.4.1 (h): przy samych przesyłkach LQ z części 8 stosuje się tylko 8.2.3, 8.6.3.3 i 8.6.4 (bez 8.1.5) – potwierdzić odczyt.
- 0701 – definicja „przewóz” (1.2.1) w module ochrony (12-K02) – czy pytanie pasuje do kompetencji.
- 0702 – gaśnica 2 kg „do pożaru silnika lub kabiny” (8.1.4.1, kolumna 3) a instrukcje pisemne (wymieniają opony, hamulce i silnik, nie kabinę); bliskość 0223 (gaśnica 2 kg do pożaru silnika).
- 0704 – 8.1.4.3: czy brak przenośnej gaśnicy do silnika zmienia łączną pojemność z tabeli 8.1.4.1; kompetencja 05-K12 – przepis sąsiedni.
- 0705 – relacja do 0483 (płyn do płukania oczu przy 2.3; similarity 0,385).
- poza partią (partia 48): 0706 dubluje 0177; 0708 (moduł 10) dubluje 0714; 0713 – KC art. 471 a Prawo przewozowe art. 65 (do oceny prawnika); 0712 i 0715 – źródła spoza ADR (pierwsza pomoc, wytyczne ERC); 0769 dubluje 0514; 0247 = 0770.