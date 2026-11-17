# Kontrola druga – partia 48 (ADR-B-0706–0720)

Main 8f28426d3 (po scaleniu #927), bank blob `e92048bdde4e05422e3265542636b6213f3e10b4`. Źródło: Dz.U. 2025 poz. 642 (+ sprostowanie poz. 1575); strony według nagłówka „Dziennik Ustaw — NNN —”. Nic nie oznaczono jako verified.

**Wynik: OK 0 / POPRAW 15 / BLOKUJ 0.** 8 nowych elementów z tej samej kompetencji (0706, 0707, 0708, 0709, 0712, 0714, 0717, 0719), 7 przeredagowań z zachowaniem tematu (0710, 0711, 0713, 0715, 0716, 0718, 0720). Bez cystern; litery kluczy, moduły i kompetencje bez zmian; liczba pytań 780 bez zmian.

**Pozostało pytań bez porównania dosłownego: 60** (0721–0780).

| ID | Kompetencja | Klucz | #927 | Kontrola 2 | Decyzja | Długości A/B/C |
|---|---|---|---|---|---|---|
| ADR-B-0706 | 09-K07 | B | BLOKUJ | POPRAW | NOWY ELEMENT (stare: brak możliwości oczyszczenia po rozładunku → jazda do miejsca czyszczenia = 0177/0240; nowe: kiedy środki ostrożności są „odpowiednie” – brak niekontrolowanego wycieku) | 72/63/62 |
| ADR-B-0707 | 05-K08 | B | BLOKUJ | POPRAW | NOWY ELEMENT (stare: bezpieczne usunięcie skażonej odzieży = 0110/0167; nowe: skażona kamizelka – usunąć i uzupełnić przed jazdą, 5.4.3.4 + 8.1.5.2) | 74/69/60 |
| ADR-B-0708 | 10-K02 | B | BLOKUJ | POPRAW | NOWY ELEMENT (stare: brak wpisu 1.1.4.2.1 → uzyskać dokument z wpisem = 0714/0779, też 0061/0089; nowe: zapis wymagany także przy samym pakowaniu razem według IMDG, 1.1.4.2.1 (b)) | 61/61/60 |
| ADR-B-0709 | 01-K01 | B | POPRAW | POPRAW | NOWY ELEMENT (stare: jednostka transportowa samochód + przyczepa = 0147; nowe: definicja „sztuka przesyłki” – pusty karton UN a karton przygotowany do wysyłki) | 61/61/62 |
| ADR-B-0710 | 08-K07 | C | POPRAW | POPRAW | PRZEREDAGOWANIE (temat zachowany: dobór wyposażenia według numerów obu nalepek z dokumentu, 8.1.5.1) | 61/71/63 |
| ADR-B-0711 | 08-K02 | B | BLOKUJ | POPRAW | PRZEREDAGOWANIE (temat zachowany: ciągnik + naczepa = jedna jednostka, jedna gaśnica 2 kg przy 1.1.3.6) | 61/61/63 |
| ADR-B-0712 | 05-K11 | B | BLOKUJ | POPRAW | NOWY ELEMENT (stare: opatrywanie krwawiącej rany – technika spoza ADR; nowe: rękawice ochronne przed pomocą koledze skażonemu materiałem 6.1) | 63/61/57 |
| ADR-B-0713 | 07-K07 | B | BLOKUJ | POPRAW | PRZEREDAGOWANIE (temat zachowany: ogólna zasada odpowiedzialności za opóźnienie – KC art. 471; do oceny prawnika) | 60/63/63 |
| ADR-B-0714 | 13-K06 | A | BLOKUJ | POPRAW | NOWY ELEMENT (stare: brak wpisu 1.1.4.2.1 → wstrzymać = 0779, też 0708; nowe: przewoźnik może polegać na danych nadawcy i sprawdza obecność dokumentu, 1.4.2.2.2) | 75/62/76 |
| ADR-B-0715 | 05-K14 | B | BLOKUJ | POPRAW | PRZEREDAGOWANIE (temat zachowany: brak oddechu → 112 na głośniku, RKO, AED – ERC 2025; dystraktor „pozycja boczna” = 0748 zastąpiony) | 68/63/63 |
| ADR-B-0716 | 05-K01 | B | BLOKUJ | POPRAW | PRZEREDAGOWANIE (temat zachowany: przewoźnik zapewnia zrozumienie instrukcji, 5.4.3.2 zd. 2) | 69/73/75 |
| ADR-B-0717 | 05-K13 | C | POPRAW | POPRAW | NOWY ELEMENT (stare: ochrona gaśnicy przed pogodą = 0749, 8.1.4.5; nowe: indywidualne ćwiczenia z gaszenia na kursie, 8.2.2.3.8) | 66/55/65 |
| ADR-B-0718 | 05-K15 | A | POPRAW | POPRAW | PRZEREDAGOWANIE (temat zachowany: UWAGA 1 – ładunek mieszany; 4.3 obok cieczy z nalepką 3 – nie spłukiwać, utrzymać w stanie suchym) | 73/76/70 |
| ADR-B-0719 | 01-K03 | A | BLOKUJ | POPRAW | NOWY ELEMENT (stare: firmowe potwierdzenie zamiast zaświadczenia = 0513/0003; nowe: kurs specjalistyczny dla klasy 1 poza 1.4S, 8.2.1.4) | 63/66/59 |
| ADR-B-0720 | 01-K04 | B | POPRAW | POPRAW | PRZEREDAGOWANIE (temat zachowany: 1.1.3.1 (c) nie obejmuje przewozu w celu zaopatrzenia – jedyne pytanie banku o ten przypadek) | 67/66/63 |

## Błędy w raporcie #927

1. **Nadużycie BLOKUJ**: 10 z 15 pytań (0706, 0707, 0708, 0711–0716, 0719) oznaczono BLOKUJ bez zamiennika, choć każde dało się wymienić lub przeredagować w tej samej kompetencji. 0711, 0713, 0715 i 0716 wymagały jedynie przeredagowania.
2. **Przeoczone duplikaty**: 0717 = 0749 (ochrona gaśnicy, 8.1.4.5); 0719 = 0513 (też 0003); 0714 = 0779.
3. **Cytaty**: 0709 i 0717 – cytat przepisu ZAMIENNIKA (8.1.1, 8.1.4.4), a nie pytania z banku (1.2.1 s. 46, 8.1.4.5 s. 1325); 0706 – połączenie i parafraza dwóch akapitów 7.5.8.1 (s. 1309 i 1310); 0716 (5.4.3.2) i 0720 (1.1.3.1 (c)) – parafrazy zamiast cytatów dosłownych.
4. **Zamienniki** (5 propozycji POPRAW) – żadnego nie przejęto: 0709 (8.1.1) wychodził poza 01-K01; 0717 (8.1.4.4) dublował 0421/0640; 0718 zostawiał słowa absolutne; 0720 (przypadek pozytywny) dublowałby istniejące pytania o 1.1.3.1 (c); 0710 przeredagowano inaczej.
5. **Słusznie**: licznik 75 → 60; strony 965, 974–977, 1325, 1326, 1327, 1328 trafne; duplikat 0708 = 0714/0779 wskazany.

## Szczegóły

### ADR-B-0706 – POPRAW (NOWY ELEMENT (stare: brak możliwości oczyszczenia po rozładunku → jazda do miejsca czyszczenia = 0177/0240; nowe: kiedy środki ostrożności są „odpowiednie” – brak niekontrolowanego wycieku))

- Cytaty i strony Dz.U. (nagłówek strony): 7.5.8.1 (s. 1309–1310): pierwsze zdanie na s. 1309; „Jeżeli czyszczenia nie można przeprowadzić w miejscu rozładunku …” i „Środki ostrożności uważa się za odpowiednie, jeżeli gwarantują one, że nie nastąpi niekontrolowany wyciek uwolnionych wcześniej materiałów.” – s. 1310.
- Raport #927 (BLOKUJ): BLOKUJ bez zamiennika – niezasadne (wymiana w tej samej kompetencji możliwa); cytat 7.5.8.1 łączy i parafrazuje dwa akapity z dwóch stron (1309 i 1310)
- Nowa treść: Po rozładunku beczek w skrzyni pojazdu została kałuża cieczy, która wyciekła z jednej beczki. W miejscu rozładunku nie da się oczyścić pojazdu, więc kierowca pojedzie do najbliższego miejsca czyszczenia. Kiedy ADR uznaje środki ostrożności na ten przejazd za odpowiednie?
- Klucz B: Gdy gwarantują, że uwolniona ciecz nie wycieknie w czasie jazdy
- Źródło: ADR 2025, 7.5.8.1 (przewóz do najbliższego miejsca czyszczenia; środki ostrożności są odpowiednie, gdy gwarantują brak niekontrolowanego wycieku)
- Uwagi: 7.5.8.1 s. 1309–1310. Odrębne od 0177 (dojazd do czyszczenia), 0240, 0021 (obowiązek czyszczenia).

### ADR-B-0707 – POPRAW (NOWY ELEMENT (stare: bezpieczne usunięcie skażonej odzieży = 0110/0167; nowe: skażona kamizelka – usunąć i uzupełnić przed jazdą, 5.4.3.4 + 8.1.5.2))

- Cytaty i strony Dz.U. (nagłówek strony): 5.4.3.4 (s. 975): zdjąć zanieczyszczone ubranie i użyte zanieczyszczone wyposażenie ochronne oraz usunąć je w sposób bezpieczny; 8.1.5.2 (s. 1325): kamizelka ostrzegawcza dla każdego członka załogi.
- Raport #927 (BLOKUJ): BLOKUJ bez zamiennika – niezasadne; temat skażonej odzieży wyczerpany (0110/0167/0745), stąd nowy element o kamizelce
- Nowa treść: Podczas działań przy pękniętym kanistrze z nalepką 6.1 ciecz oblała kamizelkę ostrzegawczą kierowcy. Zapasowej kamizelki w pojeździe nie ma. Kierowca chce nosić skażoną kamizelkę dalej, bo jest obowiązkowym wyposażeniem. Jak powinien postąpić?
- Klucz B: Zdjąć ją, bezpiecznie usunąć i przed dalszą jazdą uzupełnić kamizelkę
- Źródło: ADR 2025, 5.4.3.4 (zdjąć zanieczyszczone ubranie i użyte zanieczyszczone wyposażenie ochronne oraz usunąć je w sposób bezpieczny; nalepka 6.1); 8.1.5.2 (kamizelka ostrzegawcza dla każdego członka załogi)
- Uwagi: 5.4.3.4 s. 975; 8.1.5.2 s. 1325. Odrębne od 0110/0167 (odzież ogólnie), 0745 (kamizelka przed znakami).

### ADR-B-0708 – POPRAW (NOWY ELEMENT (stare: brak wpisu 1.1.4.2.1 → uzyskać dokument z wpisem = 0714/0779, też 0061/0089; nowe: zapis wymagany także przy samym pakowaniu razem według IMDG, 1.1.4.2.1 (b)))

- Cytaty i strony Dz.U. (nagłówek strony): 1.1.4.2.1 (s. 29): „(b) w odniesieniu do pakowania razem w do jednej sztuki przesyłki, powinny być stosowane wymagania Kodeksu IMDG lub Instrukcji Technicznych ICAO”; 5.4.1.1.7 (s. 965): „W przypadku przewozu zgodnie z 1.1.4.2.1, w dokumencie przewozowym powinien być zamieszczony dodatkowo następujący zapis: „PRZEWÓZ ZGODNY Z 1.1.4.2.1”.”
- Raport #927 (BLOKUJ): BLOKUJ bez zamiennika – niezasadne; duplikat 0714/0779 wskazany trafnie; strona 965 trafna
- Nowa treść: Sztuki przesyłek mają znaki i nalepki według ADR. W jednej z nich nadawca zapakował razem dwa różne towary niebezpieczne zgodnie z Kodeksem IMDG, choć ADR takiego pakowania razem nie dopuszcza. Przesyłki jadą ciężarówką do portu na statek. Czy w dokumencie przewozowym potrzebny jest zapis z 5.4.1.1.7?
- Klucz B: Tak, bo pakowanie razem korzysta z odstępstwa z 1.1.4.2.1 (b)
- Źródło: ADR 2025, 1.1.4.2.1 (b) (pakowanie razem według Kodeksu IMDG); 5.4.1.1.7 (zapis „PRZEWÓZ ZGODNY Z 1.1.4.2.1”)
- Uwagi: 1.1.4.2.1 s. 29–30; 5.4.1.1.7 s. 965. Odrębne od 0395 (kontener, lit. c), 0203, 0061, 0119, 0382.

### ADR-B-0709 – POPRAW (NOWY ELEMENT (stare: jednostka transportowa samochód + przyczepa = 0147; nowe: definicja „sztuka przesyłki” – pusty karton UN a karton przygotowany do wysyłki))

- Cytaty i strony Dz.U. (nagłówek strony): 1.2.1 (s. 46): „Sztuka przesyłki oznacza końcowy produkt operacji pakowania składający się z opakowania, opakowania dużego lub DPPL, wraz z jego zawartością, który jest przygotowany do wysyłki.”; „przesyłka” – s. 44.
- Raport #927 (POPRAW): zgoda co do POPRAW; ale cytat to 8.1.1 (s. 1324) – przepis ZAMIENNIKA, a nie pytania z banku (1.2.1 s. 46); zamiennik 8.1.1 wychodził poza kompetencję 01-K01 – nie przejęto
- Nowa treść: Na rampie stoją dwa takie same kartony z oznakowaniem UN. Pierwszy jest pusty i czeka na zapakowanie. Drugi zawiera puszki z farbą, jest zamknięty i przygotowany do wysyłki. Który z nich jest sztuką przesyłki według definicji z 1.2.1?
- Klucz B: Drugi, bo to opakowanie z zawartością przygotowane do wysyłki
- Źródło: ADR 2025, 1.2.1 (definicje „sztuka przesyłki” i „przesyłka”)
- Uwagi: 1.2.1 s. 46 (sztuka przesyłki), s. 44 (przesyłka). Odrębne od 0147 (jednostka transportowa).

### ADR-B-0710 – POPRAW (PRZEREDAGOWANIE (temat zachowany: dobór wyposażenia według numerów obu nalepek z dokumentu, 8.1.5.1))

- Cytaty i strony Dz.U. (nagłówek strony): 8.1.5.1 (s. 1325): „Elementy wyposażenia powinny być dobrane odpowiednio do numerów nalepek ostrzegawczych właściwych dla załadowanych towarów. Numery nalepek ostrzegawczych mogą być odczytane z dokumentu przewozowego.”
- Raport #927 (POPRAW): zgoda co do POPRAW (klucz jedyną najkrótszą, słowa absolutne); strona 1325 trafna
- Nowa treść: Przed wyjazdem kierowca sprawdza, czy jednostka ma wymagane wyposażenie ochronne. W dokumencie przewozowym przy towarze podano numery dwóch nalepek ostrzegawczych: nalepki głównej i dodatkowej. Jak powinien ustalić, jakie wyposażenie jest potrzebne?
- Klucz C: Według numerów obu nalepek z dokumentu i wykazu wyposażenia ADR
- Źródło: ADR 2025, 8.1.5.1 (dobór wyposażenia według numerów nalepek ostrzegawczych, które mogą być odczytane z dokumentu przewozowego); 8.1.5.2; 8.1.5.3
- Uwagi: 8.1.5.1–8.1.5.3 s. 1325. Przeredagowanie – usunięto jedyną najkrótszą poprawną odpowiedź.

### ADR-B-0711 – POPRAW (PRZEREDAGOWANIE (temat zachowany: ciągnik + naczepa = jedna jednostka, jedna gaśnica 2 kg przy 1.1.3.6))

- Cytaty i strony Dz.U. (nagłówek strony): 1.2.1 – definicja „jednostka transportowa”; 8.1.4.2 (s. 1325) – przy przewozie zgodnie z 1.1.3.6 co najmniej jedna gaśnica przenośna 2 kg (cytat #927 skrócony, ale dosłowny).
- Raport #927 (BLOKUJ): BLOKUJ niezasadne – wystarczyło przeredagowanie; cytat skrócony, ale dosłowny (s. 1325)
- Nowa treść: Ciągnik z dołączoną naczepą wiezie towary w ilościach objętych wyłączeniem 1.1.3.6. W kabinie ciągnika jest jedna sprawna, łatwo dostępna gaśnica proszkowa 2 kg dla grup pożarów A, B i C. Na naczepie nie ma drugiej gaśnicy. Czy zestaw spełnia 8.1.4.2?
- Klucz B: Tak, bo ciągnik z naczepą tworzy jedną jednostkę transportową
- Źródło: ADR 2025, 1.2.1 (definicja „jednostka transportowa”); 8.1.4.2 (co najmniej jedna gaśnica przenośna 2 kg przy przewozie zgodnie z 1.1.3.6)
- Uwagi: 1.2.1 s. 42; 8.1.4.2 s. 1325. Przeredagowanie bez wyrazów absolutnych.

### ADR-B-0712 – POPRAW (NOWY ELEMENT (stare: opatrywanie krwawiącej rany – technika spoza ADR; nowe: rękawice ochronne przed pomocą koledze skażonemu materiałem 6.1))

- Cytaty i strony Dz.U. (nagłówek strony): 5.4.3.4 (s. 975–977): nie dotykać uwolnionych materiałów; nalepka 6.1 – zatrucie przez wdychanie, kontakt ze skórą lub spożycie; 8.1.5.2 (s. 1325): para rękawic ochronnych dla każdego członka załogi; 8.2.2.3.2 (e) (s. 1327).
- Raport #927 (BLOKUJ): BLOKUJ niezasadne – pytanie o technikę opatrunku spoza ADR wymienione na rękawice przed pomocą skażonemu (5.4.3.4, 8.1.5.2); strona 1327 trafna
- Nowa treść: Z pękniętego kanistra z nalepką 6.1 ciecz oblała rękaw kurtki pomocnika. Obaj stoją już po stronie nawietrznej, z dala od wycieku. Pomocnik prosi kierowcę, by pomógł mu zdjąć kurtkę. Co kierowca powinien zrobić najpierw?
- Klucz B: Założyć rękawice ochronne z wyposażenia, zanim dotknie kurtki
- Źródło: ADR 2025, 5.4.3.4 (nie dotykać uwolnionych materiałów; nalepka 6.1 – zatrucie przez kontakt ze skórą); 8.1.5.2 (para rękawic ochronnych dla każdego członka załogi); 8.2.2.3.2 (e)
- Uwagi: 5.4.3.4 s. 975–977; 8.1.5.2 s. 1325; 8.2.2.3.2 s. 1327. Odrębne od 0110/0167 i 0705.

### ADR-B-0713 – POPRAW (PRZEREDAGOWANIE (temat zachowany: ogólna zasada odpowiedzialności za opóźnienie – KC art. 471; do oceny prawnika))

- Cytaty i strony Dz.U. (nagłówek strony): 8.2.2.3.2 (k) (s. 1327): ogólne informacje na temat odpowiedzialności cywilnej; Kodeks cywilny art. 471 (Dz.U. 2026 poz. 795).
- Raport #927 (BLOKUJ): BLOKUJ niezasadne – przeredagowanie z KC art. 471 jako drugim źródłem; kwestia Prawo przewozowe art. 65 / CMR art. 17 – do prawnika
- Nowa treść: Przewoźnik zobowiązał się dostarczyć ładunek w określonym terminie. W drodze służby zamknęły drogę po osunięciu ziemi, a bezpieczny objazd nie pozwolił zdążyć na czas. Odbiorca żąda odszkodowania za opóźnienie. Jaką ogólną zasadę odpowiedzialności za niewykonanie umowy trzeba tu zastosować?
- Klucz B: Trzeba ocenić, czy przewoźnik odpowiada za przyczynę opóźnienia
- Źródło: ADR 2025, 8.2.2.3.2 (k) (ogólne informacje na temat odpowiedzialności cywilnej); Kodeks cywilny, t.j. Dz.U. 2026 poz. 795, art. 471
- Uwagi: 8.2.2.3.2 (k) s. 1327; KC art. 471. Do oceny prawnika: Prawo przewozowe art. 65, CMR art. 17.

### ADR-B-0714 – POPRAW (NOWY ELEMENT (stare: brak wpisu 1.1.4.2.1 → wstrzymać = 0779, też 0708; nowe: przewoźnik może polegać na danych nadawcy i sprawdza obecność dokumentu, 1.4.2.2.2))

- Cytaty i strony Dz.U. (nagłówek strony): 1.4.2.2.2 (s. 56): „W przypadku wymagań podanych w 1.4.2.2.1 (a), (b), (e) i (f), przewoźnik może polegać na informacjach i danych udostępnionych mu przez innych uczestników przewozu.”; 1.4.2.2.1 (b) i 1.4.2.2.3 – s. 56.
- Raport #927 (BLOKUJ): BLOKUJ bez zamiennika; przeoczony duplikat 0714 = 0779; nowy element o 1.4.2.2.2
- Nowa treść: Nadawca przekazał przewoźnikowi dokument przewozowy z wpisem „PRZEWÓZ ZGODNY Z 1.1.4.2.1” dla kartonów pakowanych razem według Kodeksu IMDG. Kartony jadą ciężarówką do portu. Przewoźnik pyta, czy musi sam sprawdzić w Kodeksie IMDG, czy to pakowanie razem jest dozwolone. Co wynika z ADR?
- Klucz A: Może polegać na danych od nadawcy i sprawdza, czy dokument jest w pojeździe
- Źródło: ADR 2025, 1.4.2.2.1 (b); 1.4.2.2.2 (przewoźnik może polegać na informacjach i danych od innych uczestników przewozu); 1.4.2.2.3; 1.1.4.2.1 (b); 5.4.1.1.7
- Uwagi: 1.4.2.2.1–1.4.2.2.3 s. 56; 1.1.4.2.1 s. 29–30. Bliskie 0375 – do oceny specjalisty.

### ADR-B-0715 – POPRAW (PRZEREDAGOWANIE (temat zachowany: brak oddechu → 112 na głośniku, RKO, AED – ERC 2025; dystraktor „pozycja boczna” = 0748 zastąpiony))

- Cytaty i strony Dz.U. (nagłówek strony): 8.2.2.3.2 (e) (s. 1327) i 8.2.2.3.8 (s. 1328); treść medyczna – ERC Guidelines 2025 (BLS).
- Raport #927 (BLOKUJ): BLOKUJ niezasadne – przeredagowanie; dystraktor „pozycja boczna” dublował 0748; strona 1328 trafna
- Nowa treść: Podczas ćwiczenia z pierwszej pomocy po wypadku kierowca podchodzi do dorosłego poszkodowanego, który nie reaguje na głos i nie oddycha prawidłowo. Miejsce jest bezpieczne. Jak powinien postąpić według wytycznych ERC 2025?
- Klucz B: Wezwać 112 na głośniku, zacząć RKO i użyć AED, gdy je przyniosą
- Źródło: ADR 2025, 8.2.2.3.2 (e); 8.2.2.3.8; ERC Guidelines 2025 Adult Basic Life Support (112 z głośnikiem, RKO według dyspozytora, AED)
- Uwagi: 8.2.2.3.2 s. 1327; 8.2.2.3.8 s. 1328; podstawa medyczna ERC 2025 – do potwierdzenia specjalisty.

### ADR-B-0716 – POPRAW (PRZEREDAGOWANIE (temat zachowany: przewoźnik zapewnia zrozumienie instrukcji, 5.4.3.2 zd. 2))

- Cytaty i strony Dz.U. (nagłówek strony): 5.4.3.2 (s. 974): „Przed rozpoczęciem przewozu przewoźnik powinien dostarczyć załodze pojazdu instrukcje sporządzone w języku(-ach), które każdy członek załogi pojazdu może przeczytać i zrozumieć przed rozpoczęciem przewozu. Przewoźnik powinien zapewnić, aby każdy członek załogi pojazdu, którego to dotyczy, rozumiał instrukcje i potrafił je prawidłowo wykonywać.”
- Raport #927 (BLOKUJ): BLOKUJ niezasadne – przeredagowanie; cytat 5.4.3.2 nie jest dosłowny (parafraza)
- Nowa treść: Przewoźnik dał załodze instrukcje pisemne po polsku. Pomocnik czyta po polsku, ale nie rozumie, co ma zrobić przy kilku poleceniach na wypadek awarii. Dyspozytor mówi, że wystarczy, że instrukcje leżą w kabinie. Co powinno się stać przed wyjazdem?
- Klucz B: Przewoźnik ma zapewnić, by pomocnik rozumiał polecenia i umiał je wykonać
- Źródło: ADR 2025, 5.4.3.2 (przewoźnik zapewnia, aby każdy członek załogi rozumiał instrukcje i potrafił je prawidłowo wykonywać)
- Uwagi: 5.4.3.2 s. 974. Przeredagowanie – usunięto wyrazy absolutne i podpowiedź w treści.

### ADR-B-0717 – POPRAW (NOWY ELEMENT (stare: ochrona gaśnicy przed pogodą = 0749, 8.1.4.5; nowe: indywidualne ćwiczenia z gaszenia na kursie, 8.2.2.3.8))

- Cytaty i strony Dz.U. (nagłówek strony): 8.2.2.3.8 (s. 1328): „W powiązaniu ze szkoleniem teoretycznym powinny być organizowane indywidualne ćwiczenia praktyczne, obejmujące co najmniej sposoby udzielania pierwszej pomocy, gaszenie pożaru oraz postępowanie w razie zaistnienia wypadku lub awarii.” (stare pytanie: 8.1.4.5, s. 1325).
- Raport #927 (POPRAW): zgoda co do POPRAW, ale przeoczony duplikat 0717 = 0749; cytat to 8.1.4.4 (przepis zamiennika, parafraza), a nie 8.1.4.5 z pytania; zamiennik 8.1.4.4 dublował 0421/0640 – nie przejęto
- Nowa treść: Na kursie podstawowym ADR jest jedna gaśnica ćwiczebna. Instruktor proponuje, by gaszenie tacy z płonącym olejem wykonał jeden kursant, a reszta grupy tylko patrzyła. Czy takie zajęcia spełniają wymagania ADR dla ćwiczeń z gaszenia pożaru?
- Klucz C: Nie, ćwiczenia praktyczne z gaszenia pożaru mają być indywidualne
- Źródło: ADR 2025, 8.2.2.3.8 (indywidualne ćwiczenia praktyczne obejmujące co najmniej gaszenie pożaru)
- Uwagi: 8.2.2.3.8 s. 1328. Odrębne od 0749 (ochrona gaśnicy) i 0421/0640 (gaśnica w kabinie).

### ADR-B-0718 – POPRAW (PRZEREDAGOWANIE (temat zachowany: UWAGA 1 – ładunek mieszany; 4.3 obok cieczy z nalepką 3 – nie spłukiwać, utrzymać w stanie suchym))

- Cytaty i strony Dz.U. (nagłówek strony): 5.4.3.4 (s. 977, tabela instrukcji pisemnych – obraz strony): UWAGA 1 – ładunki mieszane; nalepka 4.3 (s. 976): „Uwolniony materiał powinien być utrzymywany w stanie suchym, pod przykryciem.”
- Raport #927 (POPRAW): zgoda co do POPRAW; zamiennik #927 zostawiał słowa absolutne i jedyną najdłuższą – nie przejęto; strona 977 trafna
- Nowa treść: Po kolizji z pękniętego kanistra z nalepką 3 wycieka ciecz, a z rozdartego worka z nalepką 4.3 obok wysypał się proszek. Pomocnik chce spłukać całe miejsce wodą, bo dla nalepki 3 instrukcje pisemne nie zabraniają wody. Co wynika z instrukcji?
- Klucz A: Nie spłukiwać, bo stosuje się też wskazówki dla 4.3: proszek ma być suchy
- Źródło: ADR 2025, 5.4.3.4 (instrukcje pisemne: UWAGA 1 – ładunki mieszane; nalepka 4.3 – uwolniony materiał utrzymywać w stanie suchym, pod przykryciem)
- Uwagi: 5.4.3.4 s. 976–977 (UWAGA 1). Odrębne od 0362 (towar jednorodny).

### ADR-B-0719 – POPRAW (NOWY ELEMENT (stare: firmowe potwierdzenie zamiast zaświadczenia = 0513/0003; nowe: kurs specjalistyczny dla klasy 1 poza 1.4S, 8.2.1.4))

- Cytaty i strony Dz.U. (nagłówek strony): 8.2.1.4 (s. 1326): „Kierowcy pojazdów przewożących towary niebezpieczne klasy 1, inne niż materiały lub przedmioty należące do podklasy 1.4 grupy zgodności S lub przewożący materiały klasy 7 powinni ukończyć w stosownych przypadkach kurs specjalistyczny obejmujący co najmniej tematy podane w 8.2.2.3.4 lub 8.2.2.3.5.”
- Raport #927 (BLOKUJ): BLOKUJ bez zamiennika; przeoczony duplikat 0719 = 0513 (też 0003); nowy element o 8.2.1.4; strona 1326 trafna
- Nowa treść: Kierowca ma ważne zaświadczenie ADR z kursu podstawowego. Ma przewieźć na pełnych zasadach ADR skrzynie z materiałami wybuchowymi podklasy 1.1. Czy obecne zaświadczenie wystarczy do tego przewozu?
- Klucz A: Nie, potrzebny jest też kurs specjalistyczny w zakresie klasy 1
- Źródło: ADR 2025, 8.2.1.4 (kurs specjalistyczny dla klasy 1, z wyjątkiem podklasy 1.4 grupy zgodności S); 8.2.1.2
- Uwagi: 8.2.1.4 s. 1326; 8.2.1.2 s. 1326. Uwaga: „w stosownych przypadkach” – do oceny specjalisty.

### ADR-B-0720 – POPRAW (PRZEREDAGOWANIE (temat zachowany: 1.1.3.1 (c) nie obejmuje przewozu w celu zaopatrzenia – jedyne pytanie banku o ten przypadek))

- Cytaty i strony Dz.U. (nagłówek strony): 1.1.3.1 (c) (s. 23): „… charakter pomocniczy wobec ich zasadniczej działalności, np. dostaw na teren budów, zwrotów z terenów budów oraz dostaw lub zwrotów w związku z przeglądami, naprawami i konserwacją urządzeń, w ilościach nie większych niż 450 litrów na opakowanie … Przewóz wykonywany przez przedsiębiorstwa, o których mowa, w celu ich zaopatrzenia lub wewnętrznej i zewnętrznej dystrybucji, nie podlega niniejszemu wyłączeniu”.
- Raport #927 (POPRAW): zgoda co do POPRAW; cytat 1.1.3.1 (c) to parafraza; zamiennik (przypadek pozytywny) zbędny – przeredagowano z zachowaniem przypadku zaopatrzenia
- Nowa treść: Firma serwisowa odbiera od dostawcy 200 litrów towaru niebezpiecznego i wiezie go do własnego magazynu jako zapas do przyszłych napraw. Opakowania mają mniej niż 450 litrów, a ilość mieści się w limitach z 1.1.3.6. Czy przewóz korzysta z wyłączenia 1.1.3.1 (c)?
- Klucz B: Nie, bo wyłączenie nie obejmuje przewozu w celu zaopatrzenia firmy
- Źródło: ADR 2025, 1.1.3.1 (c) (przewóz pomocniczy; wyłączenie nie obejmuje przewozu w celu zaopatrzenia ani dystrybucji)
- Uwagi: 1.1.3.1 (c) s. 23. Jedyne pytanie banku o przypadek zaopatrzenia z 1.1.3.1 (c).

## Wskaźniki

- „Poprawna = jedyna najdłuższa”: **17/780 = 2,18% → 15/780 = 1,92%** (stare 0713 i 0718 miały klucz jako jedyną najdłuższą opcję); maksimum działu 5,66% bez zmian. Wskaźnik poprawiony w docs/POKRYCIE-KURSU.md, docs/STAN-KONCOWY-BANKU-ADR-PODSTAWOWY-2026-11-03.md i podstawowy/README.md.
- „Poprawna = jedyna najkrótsza”: **83/780 → 80/780** (stare 0708, 0710, 0717); każdy dział ≤ 38% (maks. 17,2% → 16,1%; dział 05: 15 → 14/87, dział 08: 9 → 8/53, dział 10: 5 → 4/57).
- Żadna opcja nowych rekordów nie kończy się kropką, nie ma średnika ani słów absolutnych, wszystkie ≤ 80 zn.; klucz nigdy nie jest jedyną najdłuższą ani jedyną najkrótszą. Objaśnienia: 5–5 zdań, 381–501 znaków, ≤ 26 słów w zdaniu, ostatnie zdanie „Podstawa: ADR …”.
- similarity.py: cały bank – main **7 par ≥ 0,45 / 154 ≥ 0,25**; po poprawkach **7 / 156**. Pary z partią: main **0 / 3** (0715/0748 = 0,409; 0717/0749 = 0,261; 0714/0779 = 0,250); po poprawkach **0 / 5** (0715/0748 = 0,409 – brak oddechu a oddech prawidłowy; 0650/0718 = 0,375 – nalepka 8 a ładunek mieszany 3 + 4.3; 0203/0708 = 0,314 i 0395/0708 = 0,303 – inne warianty zapisu 5.4.1.1.7; 0642/0715 = 0,259 – technika uciśnięć). check_near_duplicates (0,60) i check_cross_module_duplicates (0,80) – bez kandydatów. Wariant 0708 „wpis także po rejsie” odrzucono jako tożsamy z kluczem 0119. Wyszukiwanie po temacie: środki ostrożności 7.5.8.1, skażona kamizelka, pakowanie razem a zapis 5.4.1.1.7, definicja sztuki przesyłki, rękawice przed pomocą, poleganie przewoźnika na danych nadawcy, indywidualne ćwiczenia kursu, kurs specjalistyczny klasy 1 – brak duplikatów (pokrewne: 0177, 0240, 0745, 0395, 0203, 0147, 0375, 0749, 0513).
- Kompetencje: liczby bez zmian; 05-K13, 05-K14, 05-K15 nadal po 5; kompetencje.json bez zmian.

## Synchronizacja (test na kopii repo)

- review/sequential/ i review/legal-clauses/: 706-706.json … 720-720.json – snapshoty; w legal-clauses clause, answer_review A/B/C, notes_on_conditions.
- Ledgery z PAKIET-0780-MANIFEST (stage4w4-literal-verification-ledger-0001-0609.json i 0610-0678.json) – 15 wpisów.
- Egzaminy 001–005: ŻADEN wariant nie zawiera 0706–0720 – zmienia się tylko SHA (10 plików). Kolejki 4X40/4X44 – tylko SHA. Scenariusze bez zmian.
- SHA e92048bd… → 884f19a0… w 51 plikach; zostaje tylko w review/literal-pl/ i jako FIRST_PASS_BANK_SHA w tests/test_literal_review_0706_0720.py (stała dodana – test z #927 miał jedną stałą).
- REJESTR-AKTUALNY-0001-0765.md i 0001-0780.md – wiersze 0706–0720.
- Lekcje i instruktor: ADR-B-01 (jednostka transportowa → 0147 + sekcja sztuki przesyłki 0709; firmowe potwierdzenie → 0513 + sekcja kursu klasy 1 0719), ADR-B-05 (skażona odzież → 0167 + kamizelka 0707; pierwsza pomoc → 0187 + rękawice 0712; ochrona gaśnicy → 0749 + indywidualne ćwiczenia 0717), ADR-B-09 (dojazd do czyszczenia → 0240 + sekcja 0706), ADR-B-10 (wpis 1.1.4.2.1 → 0061 + pakowanie razem 0708), ADR-B-13 (brak wpisu → 0779 + poleganie na danych nadawcy 0714).

## Wynik testu

Git worktree z main 8f28426d3 + POPRAWKI + synchronizacja: 14 skryptów CI zielonych (validate, coverage, check_mock_exam_variants, answer_leakage_metrics, answer_length_bias --threshold 0.16 --strict, check_explanation_quality --minimum 300, check_near_duplicates 0.60, check_cross_module_duplicates 0.80, similarity, check_explanation_heuristics, release_gate --report, check_sequential_audit, check_legal_clause_review, course_consistency); `python3 -m unittest discover -s tests` – **259/259 OK**. Blob banku po zastosowaniu: `884f19a050315bef28c614aa0f4aae9533ed14a9`.

## Do pakietu dla specjalistów

- 0713 – do oceny prawnika: ogólna zasada KC art. 471 a szczególne reżimy (Prawo przewozowe art. 65, CMR art. 17 – odpowiedzialność przewoźnika za opóźnienie i okoliczności zwalniające); czy pytanie może zostać w module 07.
- 0714 – bliskość 0375 (1.4.2.2.2 / obowiązki przewoźnika); czy oba pytania mogą zostać obok siebie.
- 0706 – temat 7.5.8 wyczerpany (0021, 0177, 0201, 0238, 0240); nowy element dotyczy definicji „odpowiednich środków ostrożności” – czy nie jest zbyt bliski 0177/0240.
- 0707 – relacja do 0745 (kamizelka przed ustawieniem znaków) i 0110/0167 (skażona odzież ogólnie).
- 0708 – bliskość 0395 (zapis 5.4.1.1.7 przy kontenerze z nalepkami IMDG, lit. c) i 0203; similarity 0,303/0,314.
- 0715 – podstawa medyczna ERC 2025 (ADR 8.2.2.3.2 (e) i 8.2.2.3.8 tylko ogólnie); similarity z 0748 = 0,409 (inny przypadek: brak oddechu a oddech prawidłowy).
- 0717 – organizacja kursu (8.2.2.3.8) w kompetencji 05-K13 – czy pasuje do kompetencji.
- 0719 – „w stosownych przypadkach” w 8.2.1.4 – potwierdzić odczyt dla pełnego przewozu podklasy 1.1.
- poza partią: 0769 dubluje 0514; 0247 = 0770; partia 49 – 0733 = 0201 (7.5.8.2, ten sam towar), 0735 = 0696 (dokumenty w kabinie przy rozlewie), 0722 – merytoryczna poprawność klucza (temperatura otoczenia 8 °C poniżej temperatury zapłonu 18 °C).