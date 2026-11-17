# Kontrola druga – partia 50 (ADR-B-0736–0750)

Main 1aebc5f9a (po scaleniu #931), bank blob `5448ab43d2bed3ac17abd384b6bdc1eb596ef93f`. Źródło: Dz.U. 2025 poz. 642 (+ sprostowanie poz. 1575 – nie dotyczy punktów tej partii); strony według nagłówka „Dziennik Ustaw — NNN —”. Nic nie oznaczono jako verified.

**Wynik: OK 0 / POPRAW 15 / BLOKUJ 0.** 8 nowych elementów z tej samej kompetencji (0737, 0738, 0741, 0744, 0746, 0747, 0748, 0750), 7 przeredagowań z zachowaniem tematu (0736, 0739, 0740, 0742, 0743, 0745, 0749). Bez cystern (0738 – awaria cysterny zastąpiona rozlewem z kanistra; 0740 – wywrotka luzem); litery kluczy, moduły i kompetencje bez zmian; liczba pytań 780 bez zmian.

**Pozostało pytań bez porównania dosłownego: 30** (0751–0780; licznik 45 → 30).

| ID | Kompetencja | Klucz | #931 | Kontrola 2 | Decyzja | Długości A/B/C |
|---|---|---|---|---|---|---|
| ADR-B-0736 | 04-K01 | A | POPRAW | POPRAW | PRZEREDAGOWANIE (temat zachowany: zakaz palenia przy czynnościach ładunkowych obejmuje osobę spoza załogi; opcje >80 zn., kropki, średniki, „tylko”) | 75/71/75 |
| ADR-B-0737 | 04-K02 | A | POPRAW | POPRAW | NOWY ELEMENT (stare: zgoda odbiorcy ≈ 0048 i scenariusz SC-ADR-B-04-04; nowe: DPPL z zawartością jest sztuką przesyłki – 1.2.1 i 8.3.3) | 72/64/73 |
| ADR-B-0738 | 04-K04 | C | POPRAW | POPRAW | NOWY ELEMENT (stare: awaria cysterny – zakres kursu cysternowego, lampa robocza = dystraktor 0102; nowe: akumulatorowy odkurzacz przy rozlewie z kanistra – nie włączać urządzeń elektrycznych) | 70/57/66 |
| ADR-B-0739 | 05-K02 | C | POPRAW | POPRAW | PRZEREDAGOWANIE (temat zachowany: wyłącznik główny akumulatora przy wycieku – czynności, gdy możliwe i bezpieczne; „zawsze”, opcje >80 zn.) | 74/71/73 |
| ADR-B-0740 | 05-K03 | B | POPRAW | POPRAW | PRZEREDAGOWANIE (temat zachowany: przekazanie służbom obu numerów z tablicy; wywrotka luzem zamiast nieokreślonego pojazdu, bez cystern) | 63/65/77 |
| ADR-B-0741 | 05-K04 | C | POPRAW | POPRAW | NOWY ELEMENT (stare: pył, strona nawietrzna = 0613; nowe: zmiana kierunku wiatru – ponownie znaleźć stronę nawietrzną) | 71/73/73 |
| ADR-B-0742 | 05-K05 | B | POPRAW | POPRAW | PRZEREDAGOWANIE (temat zachowany: ogień przechodzi na przedział ładunkowy – przerwać gaszenie; opona zamiast silnika, opcja A >80 zn.) | 72/70/65 |
| ADR-B-0743 | 05-K06 | B | POPRAW | POPRAW | PRZEREDAGOWANIE (temat zachowany: mały pożar silnika, ale dojście przez gęsty dym – warunek „właściwe i bezpieczne”; „tylko”, średnik) | 75/68/66 |
| ADR-B-0744 | 05-K07 | A | POPRAW | POPRAW | NOWY ELEMENT (stare: dostępność danych EDP/EDI = 0363, 1.4.2.2.1 (b); nowe: instrukcje pisemne nie zastępują dokumentu przewozowego) | 72/70/74 |
| ADR-B-0745 | 05-K08 | B | POPRAW | POPRAW | PRZEREDAGOWANIE (temat zachowany: użyte rękawice bez widocznych śladów – skażone wyposażenie do bezpiecznego usunięcia; opcje >80 zn., średniki) | 68/65/64 |
| ADR-B-0746 | 05-K09 | A | POPRAW | POPRAW | NOWY ELEMENT (stare: „ostrzec ruch drogowy” spoza brzmienia 5.4.3.4, bliskie 0186/0111; nowe: nie wracać w strefę zagrożenia po rzeczy osobiste) | 68/71/68 |
| ADR-B-0747 | 05-K10 | A | POPRAW | POPRAW | NOWY ELEMENT (stare: dwa znaki + kamizelka dla każdego = 0075 + 0693; nowe: dwa znaki na całą jednostkę transportową, także z przyczepą) | 61/58/61 |
| ADR-B-0748 | 05-K11 | A | POPRAW | POPRAW | NOWY ELEMENT (stare: pozycja boczna według ERC 2025 – spoza ADR, bliskie 0715; nowe: maska ucieczkowa nie służy do wejścia w opary po poszkodowanego) | 64/64/64 |
| ADR-B-0749 | 05-K12 | B | POPRAW | POPRAW | PRZEREDAGOWANIE (temat zachowany: ochrona gaśnicy przed czynnikami atmosferycznymi i łatwy dostęp; klucz był jedyną najkrótszą, C >80, „wyłącznie”) | 67/67/68 |
| ADR-B-0750 | 06-K01 | C | POPRAW | POPRAW | NOWY ELEMENT (stare: kanister 20 l → 6 mm = lustro 0188; nowe: butla o pojemności wodnej 50 l → 6 mm) | 56/66/64 |

## Błędy w raporcie #931 (do poprawienia przy wdrożeniu)

1. **Przeoczone lub niedocenione duplikaty**: 0744 = 0363 (1.4.2.2.1 (b) – dostępność danych elektronicznych co najmniej jak papier); 0747 = 0075 (dwie kamizelki dla dwóch osób) + 0693 (dwa znaki); 0738 – „lampa robocza” to dystraktor 0102; 0742 – dystraktor C w 0592 opisuje to samo przejście ognia na ładownię (#931 uznał temat za odrębny).
2. **Zamienniki**: żaden nie przejęty wprost. 0741 (pył), 0744 (EDP), 0747 (znaki i kamizelki) i 0750 (kanister 20 l) powtarzały stary, zdublowany temat – wbrew ocenie w tym samym raporcie; 0737 (uchylenie wieka) ≈ 0357/0243; 0738 (lampa, „brak płomienia”) = 0102/0164; 0746 (gapie) = 0186/0111; 0748 (ocena bezpieczeństwa przed podejściem) = 0187/0113. 0736, 0739, 0740, 0742, 0743, 0745, 0749 – temat zachowany, treść własna.
3. **Merytoryka**: 0736 – nie dubluje 0010/0103/0279 (osoba spoza załogi to odrębny aspekt 8.3.5), dlatego przeredagowane, nie wymienione; 0740 – tablice z numerami występują przy cysternach i ładunku luzem, rodzaj pojazdu trzeba wskazać (wybrano wywrotkę luzem).
4. **Słusznie**: wszystkie 15 POPRAW; brak „ruchu drogowego” w 5.4.3.4 (0746); źródło ERC spoza ADR (0748); cysterna w 0738; licznik 45 → 30; strony 935, 955, 961, 975, 1325, 1327, 1332 trafne; sprostowanie poz. 1575 nie dotyczy partii.

## Szczegóły

### ADR-B-0736 – POPRAW (PRZEREDAGOWANIE (temat zachowany: zakaz palenia przy czynnościach ładunkowych obejmuje osobę spoza załogi; opcje >80 zn., kropki, średniki, „tylko”))

- Cytaty i strony Dz.U. (nagłówek strony): 8.3.5 (s. 1332): „W czasie manipułowania ładunkiem zabronione jest palenie zarówno w pobliżu, jak też wewnątrz pojazdów. Niniejszy zakaz palenia ma również zastosowanie do używania elektronicznych papierosów i podobnych urządzeń.”
- Raport #931 (POPRAW): zgoda co do POPRAW (forma); NIE zgadzam się, że temat dubluje 0010/0103/0279 – osoba spoza załogi to odrębny aspekt 8.3.5; zamiennik #931 bez zmiany tematu, ale z kluczem jedyną najdłuższą względem C – przeredagowano własną treścią
- Nowa treść: Trwa rozładunek kartonów z towarem ADR. Pracownik magazynu, który nie należy do załogi pojazdu, zapala papierosa tuż przy otwartej skrzyni. Twierdzi, że zakaz palenia z ADR dotyczy kierowcy i kabiny. Jak ocenić tę sytuację?
- Klucz A: Zakaz obejmuje palenie przy pojeździe podczas rozładunku, także przez niego
- Źródło: ADR 2025, 8.3.5 (w czasie manipulowania ładunkiem zabronione jest palenie w pobliżu i wewnątrz pojazdów; zakaz obejmuje też papierosy elektroniczne)
- Uwagi: 8.3.5 s. 1332. Przeredagowanie – opcje >80 zn. z kropkami, średniki, „tylko”; temat (osoba spoza załogi) odrębny od 0010/0103/0279/0280/0360.

### ADR-B-0737 – POPRAW (NOWY ELEMENT (stare: zgoda odbiorcy ≈ 0048 i scenariusz SC-ADR-B-04-04; nowe: DPPL z zawartością jest sztuką przesyłki – 1.2.1 i 8.3.3))

- Cytaty i strony Dz.U. (nagłówek strony): Pytanie z banku: 8.3.3 (s. 1332). Nowe: 8.3.3 (s. 1332) „Zabrania się kierowcy i jego pomocnikowi otwierania sztuk przesyłek zawierających towary niebezpieczne.”; 1.2.1 (s. 46) „Sztuka przesyłki oznacza końcowy produkt operacji pakowania składający się z opakowania, opakowania dużego lub DPPL, wraz z jego zawartością, który jest przygotowany do wysyłki.”
- Raport #931 (POPRAW): zgoda co do POPRAW; duplikat z 0048 i scenariuszem wskazany; zamiennik #931 (uchylenie wieka beczki) ≈ 0357/0243 (zajrzeć do kartonu) – nie przejęty
- Nowa treść: U odbiorcy na pojeździe stoi DPPL z cieczą żrącą klasy 8. Przed rozładunkiem kierowca chce odkręcić pokrywę otworu wlewowego, aby sprawdzić, ile cieczy jest w środku. Czy wolno mu to zrobić?
- Klucz A: Nie, bo DPPL z zawartością to sztuka przesyłki objęta zakazem otwierania
- Źródło: ADR 2025, 8.3.3 (zakaz otwierania sztuk przesyłek przez kierowcę i pomocnika); 1.2.1 (definicja sztuki przesyłki – także DPPL wraz z zawartością)
- Uwagi: 8.3.3 s. 1332; 1.2.1 s. 46. Nowy element – stare (zgoda odbiorcy) ≈ 0048 i scenariusz SC-ADR-B-04-04 (prośba odbiorcy).

### ADR-B-0738 – POPRAW (NOWY ELEMENT (stare: awaria cysterny – zakres kursu cysternowego, lampa robocza = dystraktor 0102; nowe: akumulatorowy odkurzacz przy rozlewie z kanistra – nie włączać urządzeń elektrycznych))

- Cytaty i strony Dz.U. (nagłówek strony): 5.4.3.4, wzór instrukcji pisemnych (s. 975): „Unikać źródeł zapłonu, w szczególności nie palić, nie używać papierosów elektronicznych lub podobnych urządzeń oraz nie włączać żadnych urządzeń elektrycznych;” oraz „…zebrać uwolnione materiały, używając wyposażenia przewożonego w jednostce transportowej;”.
- Raport #931 (POPRAW): zgoda co do POPRAW i co do cysterny; zamiennik #931 nadal „lampa” (= dystraktor 0102) z logiką „brak płomienia” jak 0164 – nie przejęty
- Nowa treść: Po kolizji z pękniętego kanistra z nalepką 3 wyciekła ciecz zapalna i czuć jej opary. Pomocnik chce zebrać kałużę akumulatorowym odkurzaczem do cieczy, który wozi w kabinie. Co wynika z instrukcji pisemnych?
- Klucz C: Nie powinien go włączać, bo to urządzenie elektryczne przy oparach
- Źródło: ADR 2025, 5.4.3.4 (instrukcje pisemne: unikać źródeł zapłonu, nie włączać żadnych urządzeń elektrycznych; uwolnione materiały zbierać wyposażeniem jednostki, jeżeli to właściwe i bezpieczne)
- Uwagi: 5.4.3.4 s. 975. Nowy element – stare: awaria cysterny (zakres kursu cysternowego) i lampa robocza = dystraktor 0102; nowe: urządzenie elektryczne przy zbieraniu rozlewu z kanistra.

### ADR-B-0739 – POPRAW (PRZEREDAGOWANIE (temat zachowany: wyłącznik główny akumulatora przy wycieku – czynności, gdy możliwe i bezpieczne; „zawsze”, opcje >80 zn.))

- Cytaty i strony Dz.U. (nagłówek strony): 5.4.3.4 (s. 975): „…jeżeli jest to możliwe i bezpieczne: — Zahamować pojazd, wyłączyć silnik i odłączyć akumulator za pomocą wyłącznika głównego, jeżeli jest on dostępny;”.
- Raport #931 (POPRAW): zgoda co do POPRAW; strona 975 trafna; zamiennik #931 bez zmiany tematu – przeredagowano własną treścią (wyciek przy wyłączniku)
- Nowa treść: Po awarii kierowca zahamował pojazd i wyłączył silnik. Wyłącznik główny akumulatora jest na ramie, tuż obok miejsca, gdzie z uszkodzonej beczki wycieka ciecz i unoszą się opary. Co powinien zrobić z akumulatorem?
- Klucz C: Nie podchodzić, bo te czynności wykonuje się, gdy są możliwe i bezpieczne
- Źródło: ADR 2025, 5.4.3.4 (instrukcje pisemne: czynności wykonuje się, jeżeli jest to możliwe i bezpieczne – zahamować pojazd, wyłączyć silnik, odłączyć akumulator wyłącznikiem głównym)
- Uwagi: 5.4.3.4 s. 975. Przeredagowanie – „zawsze”, opcje >80 zn.; temat (warunek bezpieczeństwa) odrębny od 0219 (brak wyłącznika) i 0104/0182.

### ADR-B-0740 – POPRAW (PRZEREDAGOWANIE (temat zachowany: przekazanie służbom obu numerów z tablicy; wywrotka luzem zamiast nieokreślonego pojazdu, bez cystern))

- Cytaty i strony Dz.U. (nagłówek strony): 5.4.3.4 (s. 975): „Powiadomić właściwe służby ratownicze, podając im możliwie wszystkie dostępne informacje dotyczące wypadku, awarii oraz towarów niebezpiecznych;”; 5.3.2.2.2 (s. 955): „Numer rozpoznawczy zagrożenia powinien znajdować się w górnej części tablicy, a numer UN w jej części dolnej;”; tablice z numerami przy przewozie luzem – 5.3.2.1.4 (s. 954).
- Raport #931 (POPRAW): zgoda co do POPRAW; strony 955/975 trafne; doprecyzowano rodzaj pojazdu (tablice z numerami mają cysterny i pojazdy z ładunkiem luzem – wybrano wywrotkę luzem)
- Nowa treść: Wywrotka przewozi luzem materiał stały i ma tablice barwy pomarańczowej z dwoma numerami. Po wypadku kierowca dzwoni po służby z bezpiecznego miejsca, ale nie może wrócić po dokumenty. Co przekaże o ładunku z tablicy?
- Klucz B: Oba numery: górny to numer zagrożenia, a dolny to numer UN towaru
- Źródło: ADR 2025, 5.4.3.4 (powiadomić służby, podając możliwie wszystkie dostępne informacje o towarach); 5.3.2.2.2 (numer rozpoznawczy zagrożenia u góry tablicy, numer UN u dołu)
- Uwagi: 5.3.2.2.2 s. 955; 5.4.3.4 s. 975; tablice z numerami przy przewozie luzem – 5.3.2.1.4 s. 954. Przeredagowanie – wywrotka luzem zamiast nieokreślonego pojazdu (bez cystern).

### ADR-B-0741 – POPRAW (NOWY ELEMENT (stare: pył, strona nawietrzna = 0613; nowe: zmiana kierunku wiatru – ponownie znaleźć stronę nawietrzną))

- Cytaty i strony Dz.U. (nagłówek strony): Pytanie z banku i nowe: 5.4.3.4 (s. 975): „Nie wchodzić na uwolnione materiały, nie dotykać ich, unikać wdychania oparów, dymu, pyłu i pary poprzez pozostawanie po stronie nawietrznej;”.
- Raport #931 (POPRAW): zgoda co do POPRAW i co do 0613; zamiennik #931 to nadal pył i strona nawietrzna (= 0613), wbrew własnej ocenie – nie przejęty
- Nowa treść: Kierowca stoi po stronie nawietrznej, z dala od pękniętego kanistra na skrzyni pojazdu, z którego unoszą się drażniące opary. Po kilku minutach wiatr zmienia kierunek i zaczyna nieść opary w jego stronę. Co powinien zrobić?
- Klucz C: Przejść, omijając opary, tak by znów mieć wiatr od siebie w stronę oparów
- Źródło: ADR 2025, 5.4.3.4 (instrukcje pisemne: unikać wdychania oparów, dymu, pyłu i pary poprzez pozostawanie po stronie nawietrznej)
- Uwagi: 5.4.3.4 s. 975. Nowy element – stare (pył, strona nawietrzna) = 0613; zgodne z lekcją ADR-B-05 i ćwiczeniem instruktora „zmiana kierunku wiatru”.

### ADR-B-0742 – POPRAW (PRZEREDAGOWANIE (temat zachowany: ogień przechodzi na przedział ładunkowy – przerwać gaszenie; opona zamiast silnika, opcja A >80 zn.))

- Cytaty i strony Dz.U. (nagłówek strony): 5.4.3.4 (s. 975): „Jeżeli jest to właściwe i bezpieczne, użyć gaśnic w celu ugaszenia małego lub będącego w fazie początkowej pożaru, obejmującego opony, hamulce lub przedział silnika;” i „Członkowie załogi pojazdu nie powinni gasić pożaru obejmującego przedział ładunkowy;”.
- Raport #931 (POPRAW): zgoda co do POPRAW; #931 uznał temat za odrębny – przeoczony dystraktor C w 0592 (to samo przejście ognia na ładownię); przeredagowano (opona), do oceny specjalisty
- Nowa treść: Kierowca gasi gaśnicą mały pożar opony naczepy. Po chwili płomienie przechodzą na podłogę przestrzeni ładunkowej, w której stoją beczki z towarem ADR. Gaśnica nie jest jeszcze pusta. Co powinien zrobić?
- Klucz B: Przerwać gaszenie, bo pali się już przestrzeń ładunkowa, i oddalić się
- Źródło: ADR 2025, 5.4.3.4 (instrukcje pisemne: gaśnice do małego lub początkowego pożaru opon, hamulców lub przedziału silnika; załoga nie powinna gasić pożaru obejmującego przedział ładunkowy)
- Uwagi: 5.4.3.4 s. 975. Przeredagowanie – opcja A >80, kropki; granica „opona → ładownia”. Do oceny: bliskość dystraktora C w 0592 (tunel, silnik → ładownia).

### ADR-B-0743 – POPRAW (PRZEREDAGOWANIE (temat zachowany: mały pożar silnika, ale dojście przez gęsty dym – warunek „właściwe i bezpieczne”; „tylko”, średnik))

- Cytaty i strony Dz.U. (nagłówek strony): 5.4.3.4 (s. 975): jak 0742 (warunek „Jeżeli jest to właściwe i bezpieczne”) oraz „…unikać wdychania oparów, dymu, pyłu i pary poprzez pozostawanie po stronie nawietrznej;”.
- Raport #931 (POPRAW): zgoda co do POPRAW; zamiennik #931 bez zmiany tematu – przeredagowano własną treścią
- Nowa treść: Na postoju kierowca zauważa mały, początkowy pożar w komorze silnika. Wiatr niesie gęsty dym od silnika w stronę miejsca, w którym zamocowano gaśnicę. Co wynika z instrukcji pisemnych?
- Klucz B: Nie gasić, gdy po gaśnicę trzeba wejść w gęsty dym, lecz się oddalić
- Źródło: ADR 2025, 5.4.3.4 (instrukcje pisemne: gaśnice do małego lub początkowego pożaru przedziału silnika, jeżeli jest to właściwe i bezpieczne; unikać wdychania dymu)
- Uwagi: 5.4.3.4 s. 975. Przeredagowanie – „tylko”, średnik, opcje >80 zn.; temat (warunek bezpieczeństwa) odrębny od 0493 (rozmiar pożaru).

### ADR-B-0744 – POPRAW (NOWY ELEMENT (stare: dostępność danych EDP/EDI = 0363, 1.4.2.2.1 (b); nowe: instrukcje pisemne nie zastępują dokumentu przewozowego))

- Cytaty i strony Dz.U. (nagłówek strony): Pytanie z banku: 5.4.0.2 (s. 961) – dostępność danych EDP/EDI „w stopniu co najmniej równoważnym dokumentacji papierowej” (tak samo 1.4.2.2.1 (b), s. 56 – pytanie 0363). Nowe: 5.4.3.4 (s. 974–975) „Forma i zawartość instrukcji pisemnych powinny odpowiadać czterostronicowemu wzorowi…”, „Zapewnić przybyłym ratownikom łatwy dostęp do dokumentów przewozowych;”; 5.4.1.1.1 (s. 961–962) – numer UN, nazwa, nalepki, grupa pakowania, ilość.
- Raport #931 (POPRAW): zgoda co do POPRAW; przeoczony duplikat 0363 (1.4.2.2.1 (b) – ta sama zasada równoważności z papierem); zamiennik #931 to ten sam temat – nie przejęty
- Nowa treść: Po wypadku ratownik prosi kierowcę o dane, z których odczyta, jaki towar jest w pojeździe. Kierowca stoi w bezpiecznym miejscu i ma przy sobie instrukcje pisemne oraz dokument przewozowy. Co powinien przekazać?
- Klucz A: Dokument przewozowy, bo to w nim opisano przewożone towary niebezpieczne
- Źródło: ADR 2025, 5.4.3.4 (zapewnić przybyłym ratownikom łatwy dostęp do dokumentów przewozowych; instrukcje pisemne według czterostronicowego wzoru); 5.4.1.1.1 (dane o towarze w dokumencie przewozowym)
- Uwagi: 5.4.3.4 s. 974–975; 5.4.1.1.1 s. 961. Nowy element – stare (dostępność danych EDP/EDI) = 0363 (1.4.2.2.1 (b), s. 56); pokrewne 0620 (karty charakterystyki ≠ instrukcje).

### ADR-B-0745 – POPRAW (PRZEREDAGOWANIE (temat zachowany: użyte rękawice bez widocznych śladów – skażone wyposażenie do bezpiecznego usunięcia; opcje >80 zn., średniki))

- Cytaty i strony Dz.U. (nagłówek strony): 5.4.3.4 (s. 975): „Zdjąć zanieczyszczone ubranie i użyte zanieczyszczone wyposażenie ochronne oraz usunąć je w sposób bezpieczny.”; 8.1.5.2 (s. 1325): dla każdego członka załogi „para rękawic ochronnych”.
- Raport #931 (POPRAW): zgoda co do POPRAW; bliskość 0707 wskazana; zamiennik #931 bez zmiany tematu – przeredagowano (rękawice bez widocznych śladów)
- Nowa treść: Kierowca zbierał rozlaną ciecz z nalepką 8 w rękawicach ochronnych z wyposażenia. Po akcji rękawice wyglądają na suche i czyste. Chce je schować do schowka w kabinie i użyć przy następnym rozlewie. Jak powinien postąpić?
- Klucz B: Zdjąć je jako skażone, usunąć bezpiecznie i uzupełnić wyposażenie
- Źródło: ADR 2025, 5.4.3.4 (zdjąć zanieczyszczone ubranie i użyte zanieczyszczone wyposażenie ochronne oraz usunąć je w sposób bezpieczny); 8.1.5.2 (para rękawic ochronnych dla każdego członka załogi)
- Uwagi: 5.4.3.4 s. 975; 8.1.5.2 s. 1325. Przeredagowanie – opcje >80, średniki; do oceny bliskość 0707 (skażona kamizelka).

### ADR-B-0746 – POPRAW (NOWY ELEMENT (stare: „ostrzec ruch drogowy” spoza brzmienia 5.4.3.4, bliskie 0186/0111; nowe: nie wracać w strefę zagrożenia po rzeczy osobiste))

- Cytaty i strony Dz.U. (nagłówek strony): 5.4.3.4 (s. 975): „Oddalić się od miejsca wypadku lub zagrożenia, poinformować inne osoby o konieczności oddalenia się od tego miejsca oraz stosować się do zaleceń służb ratowniczych;” – bez słów „ruch drogowy”.
- Raport #931 (POPRAW): zgoda co do POPRAW i co do braku „ruchu drogowego” w 5.4.3.4; zamiennik #931 (gapie przy opakowaniach) = 0186/0111 – nie przejęty
- Nowa treść: Po kolizji z uszkodzonych beczek z nalepką 3 wycieka ciecz zapalna. Załoga oddaliła się, ostrzegła przechodniów i wezwała służby. Pomocnik chce wrócić do kabiny po telefon i portfel, bo kałuża nie sięga jeszcze drzwi. Co powinien zrobić?
- Klucz A: Nie wracać, trzymać się z dala od zagrożenia i słuchać poleceń służb
- Źródło: ADR 2025, 5.4.3.4 (oddalić się od miejsca wypadku lub zagrożenia, poinformować inne osoby o konieczności oddalenia się, stosować się do zaleceń służb ratowniczych)
- Uwagi: 5.4.3.4 s. 975. Nowy element – stare: „ostrzec ruch drogowy” spoza brzmienia 5.4.3.4, bliskie 0186/0111; pokrewne 0696 (dokument w kabinie) i 0295 (klasa 7).

### ADR-B-0747 – POPRAW (NOWY ELEMENT (stare: dwa znaki + kamizelka dla każdego = 0075 + 0693; nowe: dwa znaki na całą jednostkę transportową, także z przyczepą))

- Cytaty i strony Dz.U. (nagłówek strony): 8.1.5.2 (s. 1325): „W jednostce transportowej powinno być przewożone następujące wyposażenie: klin pod koła, dla każdego pojazdu…; dwa stojące znaki ostrzegawcze; …”; 1.2.1 (s. 36): „Jednostka transportowa oznacza pojazd samochodowy bez przyczepy lub zespół pojazdów składający się z pojazdu samochodowego i dołączonej do niego przyczepy.”
- Raport #931 (POPRAW): zgoda co do POPRAW; przeoczony duplikat 0075 (dwie kamizelki dla dwóch osób); zamiennik #931 identyczny tematycznie – nie przejęty
- Nowa treść: Jednostka transportowa składa się z samochodu ciężarowego i przyczepy, a jedzie nią jeden kierowca. Kierownik twierdzi, że skoro są dwa pojazdy, potrzebne są cztery stojące znaki ostrzegawcze. Ile znaków wymaga 8.1.5.2?
- Klucz A: Dwa stojące znaki ostrzegawcze na całą jednostkę transportową
- Źródło: ADR 2025, 8.1.5.2 (w jednostce transportowej: klin pod koła dla każdego pojazdu, dwa stojące znaki ostrzegawcze); 1.2.1 (definicja jednostki transportowej)
- Uwagi: 8.1.5.2 s. 1325; 1.2.1 s. 36. Nowy element – stare (dwa znaki + kamizelka dla każdego) = 0075 + 0693; pokrewne 0509 (klin dla naczepy).

### ADR-B-0748 – POPRAW (NOWY ELEMENT (stare: pozycja boczna według ERC 2025 – spoza ADR, bliskie 0715; nowe: maska ucieczkowa nie służy do wejścia w opary po poszkodowanego))

- Cytaty i strony Dz.U. (nagłówek strony): Pytanie z banku: 8.2.2.3.2 (e) (s. 1327) – temat kursu „pierwsza pomoc”, bez procedury (klucz z ERC 2025). Nowe: 5.4.3.4 (s. 975) „…jeżeli jest to możliwe i bezpieczne”, „unikać wdychania oparów”; s. 977 (obraz strony) wiersz 6.1: „Użyć maski ucieczkowej.”; 8.1.5.3 (s. 1325) – maska ucieczkowa dla każdego członka załogi przy nalepkach 2.3 lub 6.1.
- Raport #931 (POPRAW): zgoda co do POPRAW i co do źródła spoza ADR; zamiennik #931 (ocenić bezpieczeństwo przed podejściem) = 0187/0113 – nie przejęty
- Nowa treść: Z uszkodzonej beczki z nalepką 6.1 ulatniają się opary. Pomocnik upadł w ich chmurze. Kierowca stoi po stronie nawietrznej, ma maskę ucieczkową i chce w niej wejść w opary, aby wyciągnąć pomocnika. Co wynika z ADR?
- Klucz A: Nie wchodzić w opary, bo maska ucieczkowa służy do oddalenia się
- Źródło: ADR 2025, 5.4.3.4 (czynności, jeżeli jest to możliwe i bezpieczne; unikać wdychania oparów; nalepka 6.1 – użyć maski ucieczkowej); 8.1.5.3 (maska ucieczkowa przy nalepkach 2.3 i 6.1)
- Uwagi: 5.4.3.4 s. 975 i 977 (wiersz 6.1: „Użyć maski ucieczkowej”); 8.1.5.3 s. 1325. Nowy element – stare (pozycja boczna wg ERC 2025) spoza ADR, bliskie 0715. Do oceny: wniosek z nazwy maski.

### ADR-B-0749 – POPRAW (PRZEREDAGOWANIE (temat zachowany: ochrona gaśnicy przed czynnikami atmosferycznymi i łatwy dostęp; klucz był jedyną najkrótszą, C >80, „wyłącznie”))

- Cytaty i strony Dz.U. (nagłówek strony): 8.1.4.5 (s. 1325): „Gaśnice powinny być zamontowane na jednostkach transportowych w taki sposób, aby były łatwo dostępne dla załogi pojazdu. Sposób zamontowania gaśnic powinien zapewniać ochronę przed działaniem czynników atmosferycznych gwarantującą ich bezpieczną eksploatację.”
- Raport #931 (POPRAW): zgoda co do POPRAW; strona 1325 trafna; temat zachowany, przeredagowano własną treścią
- Nowa treść: Gaśnica ADR jest zamocowana na zewnątrz pojazdu w otwartym uchwycie. Łatwo ją wyjąć, ale w czasie jazdy moczy ją deszcz i obryzguje sól drogowa. Co wymaga poprawy według 8.1.4.5?
- Klucz B: Mocowanie ma także chronić gaśnicę przed czynnikami atmosferycznymi
- Źródło: ADR 2025, 8.1.4.5 (gaśnice łatwo dostępne dla załogi; sposób zamontowania zapewnia ochronę przed działaniem czynników atmosferycznych)
- Uwagi: 8.1.4.5 s. 1325. Przeredagowanie – klucz był jedyną najkrótszą, C >80, „wyłącznie”; temat odrębny od 0015/0169/0585.

### ADR-B-0750 – POPRAW (NOWY ELEMENT (stare: kanister 20 l → 6 mm = lustro 0188; nowe: butla o pojemności wodnej 50 l → 6 mm))

- Cytaty i strony Dz.U. (nagłówek strony): 5.2.1.1 (s. 935): „Numer UN i litery „UN” powinny mieć nie mniej niż 12 mm wysokości, z wyłączeniem sztuk przesyłek o pojemności 30 l lub mniej, lub maksymalnej masie netto 30 kg oraz butli o pojemności wodnej 60 l lub mniej, w których to przypadkach … nie mniej niż 6 mm, oraz z wyłączeniem sztuk przesyłek o pojemności nie większej niż 5 l lub masie netto nie większej niż 5 kg, w których to przypadkach … właściwego rozmiaru.”
- Raport #931 (POPRAW): zgoda co do POPRAW i co do lustra 0188; zamiennik #931 nadal kanister 20 l, wbrew własnemu zaleceniu „inna wielkość” – nie przejęty
- Nowa treść: Nadawca oznakowuje butlę z gazem o pojemności wodnej 50 litrów. Pracownik twierdzi, że skoro butla ma ponad 30 litrów, litery „UN” i numer UN muszą mieć co najmniej 12 mm wysokości. Jakie minimum dopuszcza 5.2.1.1?
- Klucz C: 6 mm, bo dla butli do 60 litrów pojemności wodnej wystarcza 6 mm
- Źródło: ADR 2025, 5.2.1.1 (numer UN i litery „UN” co najmniej 12 mm; co najmniej 6 mm dla sztuk przesyłek do 30 l lub 30 kg netto i butli o pojemności wodnej do 60 l)
- Uwagi: 5.2.1.1 s. 935. Nowy element – stare (kanister 20 l → 6 mm) = lustro 0188 (beczka 200 l → 12 mm).

## Wskaźniki

- „Poprawna = jedyna najdłuższa”: **11/780 = 1,41%** bez zmian (żaden stary ani nowy rekord partii nie ma klucza jako jedynej najdłuższej); maksimum działu 5,66% bez zmian; dokumentacja bez zmian.
- „Poprawna = jedyna najkrótsza”: **75/780 → 67/780**; każdy dział ≤ 38% (maks. 16,1% → 15,1%; dział 04: 2 → 1/50, dział 05: 14 → 7/87, dział 06: 6/66 bez zmian).
- Żadna opcja nowych rekordów nie kończy się kropką, nie ma średnika ani słów absolutnych, wszystkie ≤ 80 zn.; klucz nigdy nie jest jedyną najdłuższą ani jedyną najkrótszą. Objaśnienia: 5–5 zdań, 349–459 znaków, ≤ 27 słów w zdaniu, ostatnie zdanie „Podstawa: ADR …”.
- similarity.py: cały bank – po poprawkach przy 0,45 brak par z partią; przy 0,25 z partią 4 pary (0229/0744 = 0,346 – ilość w dokumencie a instrukcje ≠ dokument; 0219/0739 = 0,300 – brak wyłącznika a wyłącznik przy wycieku; 0188/0750 = 0,250 – beczka 200 l a butla 50 l; 0632/0741 = 0,250 – gapie z papierosami a zmiana wiatru). Przed poprawkami: 0715/0748 = 0,409 i 0219/0739 = 0,370. check_near_duplicates (0,60) i check_cross_module_duplicates (0,80) – bez kandydatów. Wyszukiwanie po temacie: palenie przez osobę spoza załogi, DPPL a 8.3.3, urządzenie elektryczne przy rozlewie, wyłącznik przy wycieku, tablica luzem, zmiana kierunku wiatru, przejście ognia na ładownię, dym przy pożarze silnika, instrukcje a dokument, rękawice po akcji, powrót po rzeczy osobiste, znaki na zestaw z przyczepą, maska ucieczkowa a ratowanie, osłona gaśnicy, butla do 60 l – brak duplikatów (pokrewne: 0010, 0048, 0102, 0164, 0219, 0229, 0295, 0363, 0509, 0592, 0613, 0620, 0696, 0707, 0715, 0188).
- Kompetencje: liczby bez zmian (każda kompetencja partii nadal 6); 05-K13, 05-K14, 05-K15 nadal po 5; kompetencje.json bez zmian.

## Synchronizacja (test na kopii repo)

- review/sequential/ i review/legal-clauses/: 736-736.json … 750-750.json – snapshoty; w legal-clauses clause, answer_review A/B/C, notes_on_conditions.
- Ledgery z PAKIET-0780-MANIFEST (stage4w4-literal-verification-ledger-0001-0609.json i 0610-0678.json) – 15 wpisów.
- Egzaminy 001–005: ŻADEN wariant nie zawiera 0736–0750 – zmienia się tylko SHA (10 plików). Kolejki 4X40/4X44 – tylko SHA.
- SHA 5448ab43… → ff19af70… we wszystkich plikach poza review/literal-pl/ i FIRST_PASS_BANK_SHA w tests/test_literal_review_0736_0750.py (test z #931 ma już dwie stałe – zmienia się EXPECTED_BANK_SHA, a test banku sprawdza EXPECTED). W tests/test_literal_review_0721_0735.py zmienia się EXPECTED_BANK_SHA (FIRST_PASS 884f19a0… zostaje).
- REJESTR-AKTUALNY-0001-0765.md i 0001-0780.md – wiersze 0736–0750.
- tools/apply_poprawki.py – dopisany „POPRAWKI-KONTROLA2-0736-0750.jsonl” (wcięcie 4 spacje, jak pozostałe).
- Lekcje (ID w lekcji tylko z modułu lekcji): ADR-B-04 (zgoda odbiorcy → 0048 + sekcja DPPL 0737; źródła zapłonu → 0102 + sekcja urządzeń elektrycznych 0738), ADR-B-05 (pył → 0106 z odesłaniem do 0741; dokument elektroniczny bez ID + sekcja instrukcje ≠ dokument 0744; „ruch drogowy” → sekcja powrót po rzeczy osobiste 0746; znaki i kamizelki → sekcja zestaw z przyczepą 0747; pozycja boczna → uzupełnienie do 0715 + sekcja maski ucieczkowej 0748; pytanie kontrolne osłony gaśnicy 0717 → 0749), ADR-B-06 (wysokość numeru UN: 0188 + butla 0750). Instruktor i scenariusze bez zmian (ćwiczenia „zmiana kierunku wiatru” – 0741 i „granica użycia gaśnicy” – 0742 pasują do nowych treści).

## Wynik testu

Git worktree z origin/main 1aebc5f9a (lokalna gałąź kontrola2-0736-0750-wdrozenie) + POPRAWKI + synchronizacja: 14 skryptów CI zielonych (validate, coverage, check_mock_exam_variants, answer_leakage_metrics, answer_length_bias --threshold 0.16 --strict, check_explanation_quality --minimum 300, check_near_duplicates 0.60, check_cross_module_duplicates 0.80, similarity, check_explanation_heuristics, release_gate --report, check_sequential_audit, check_legal_clause_review, course_consistency) + json.tool schema; `python3 -m unittest discover -s tests` – **267/267 OK**. Blob banku po zastosowaniu: `ff19af70af76de006d2f58b1fbfed7c091d52590`.

## Do pakietu dla specjalistów

- 0748 – maska ucieczkowa nie służy do wejścia w opary: wniosek z nazwy maski i z wiersza 6.1 instrukcji pisemnych (s. 977) – potwierdzić; dopasowanie do 05-K11 (ocena bezpieczeństwa pierwszej pomocy).
- 0742 – przejście ognia z opony na przedział ładunkowy a dystraktor C w 0592 (tunel, silnik → ładownia) – czy oba mogą zostać.
- 0745 – użyte rękawice bez widocznych śladów a 0707 (skażona kamizelka) – czy nie za bliskie.
- 0744 – instrukcje pisemne a dokument przewozowy; pokrewne 0229 (similarity 0,346 – ilość w dokumencie) i 0620 (karty charakterystyki ≠ instrukcje).
- 0746 – powrót po rzeczy osobiste; pokrewne 0696 (dokument w kabinie przy dymie) i 0295 (klasa 7, pilnowanie miejsca).
- 0738 – „nie włączać żadnych urządzeń elektrycznych” zastosowane do urządzenia akumulatorowego – potwierdzić realizm przykładu.
- 0737 – DPPL jako sztuka przesyłki (1.2.1) w zakazie 8.3.3 – potwierdzić; scenariusz SC-ADR-B-04-04 nadal wskazuje 0737 (ten sam moduł i kompetencja).
- 0740 – tablice z numerami przy przewozie luzem (5.3.2.1.4/5.3.2.1.6) w kompetencji 05-K03 – zakres kursu podstawowego, bez cystern.
- lekcja ADR-B-05: sekcja o pozycji bezpiecznej (ERC 2025) zostaje jako materiał uzupełniający do 0715 – źródło spoza ADR.
- Pozostało 30 pytań bez porównania dosłownego (0751–0780) – do kontroli pierwszej i drugiej w partiach 51 (0751–0765) i 52 (0766–0780).
- poza partią (bez zmian teraz): 0752 ≈ 0170 (litera X a woda); 0764 ≈ 0200 (mocowanie zwykłego towaru); 0760 ≈ lustro 0711; 0763 ≈ 0024/0597, źródło po angielsku; 0769 dubluje 0514; 0247 = 0770; 0772 – wątpliwe; 0777 – „Delivery Sale”; 0712 i 0715 – źródła spoza ADR.