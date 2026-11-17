# Kontrola druga – partia 49 (ADR-B-0721–0735)

Main 0a2469d60 (po scaleniu #929), bank blob `884f19a050315bef28c614aa0f4aae9533ed14a9`. Źródło: Dz.U. 2025 poz. 642 (+ sprostowanie poz. 1575); strony według nagłówka „Dziennik Ustaw — NNN —”. Nic nie oznaczono jako verified.

**Wynik: OK 0 / POPRAW 15 / BLOKUJ 0.** 10 nowych elementów z tej samej kompetencji (0722, 0724, 0725, 0726, 0727, 0728, 0729, 0733, 0734, 0735), 5 przeredagowań z zachowaniem tematu (0721, 0723, 0730, 0731, 0732). Bez cystern; litery kluczy, moduły i kompetencje bez zmian; liczba pytań 780 bez zmian.

**Pozostało pytań bez porównania dosłownego: 45** (0736–0780; licznik 60 → 45).

| ID | Kompetencja | Klucz | #929 | Kontrola 2 | Decyzja | Długości A/B/C |
|---|---|---|---|---|---|---|
| ADR-B-0721 | 01-K07 | C | POPRAW | POPRAW | PRZEREDAGOWANIE (temat zachowany: numer przepisu szczególnego w kolumnie (6) → treść w dziale 3.3; opcje >80 zn. z kropkami) | 60/64/61 |
| ADR-B-0722 | 02-K03 | B | POPRAW | POPRAW | NOWY ELEMENT (stare: 8 °C a temperatura zapłonu 18 °C – klucz sporny wobec definicji 1.2.1, bliskie 0658; nowe: grupa pakowania cieczy klasy 3 z tabeli 2.2.3.1.3) | 56/56/57 |
| ADR-B-0723 | 02-K04 | C | POPRAW | POPRAW | PRZEREDAGOWANIE (temat zachowany: materiał łatwo zapalny stały zapala się od krótkiego kontaktu ze źródłem zapłonu – iskry ze szlifierki) | 65/65/65 |
| ADR-B-0724 | 02-K05 | A | POPRAW | POPRAW | NOWY ELEMENT (stare: ciepło własne i samozapalenie = 0154; nowe: kiedy samonagrzewanie kończy się samozapaleniem – bilans ciepła, 2.2.42.1.3) | 61/66/61 |
| ADR-B-0725 | 02-K07 | B | POPRAW | POPRAW | NOWY ELEMENT (stare: utleniacz nasila spalanie innych materiałów = 0156; nowe: materiał niedopuszczony – niestabilizowany roztwór nadtlenku wodoru > 60%, 2.2.51.2.2) | 71/61/58 |
| ADR-B-0726 | 02-K08 | C | POPRAW | POPRAW | NOWY ELEMENT (stare: reakcja na wzrost temperatury ≈ 0667, „powiadomić” spoza ADR; nowe: dwa czujniki, sprawdzanie co 4–6 godzin i zapis, 7.1.7.4.2) | 54/58/54 |
| ADR-B-0727 | 02-K09 | B | POPRAW | POPRAW | NOWY ELEMENT (stare: brak zapachu nie wyklucza zatrucia – reguła spoza ADR; nowe: kod klasyfikacyjny TF1 = trujący zapalny ciekły, 2.2.61.1.2) | 68/61/58 |
| ADR-B-0728 | 02-K10 | C | POPRAW | POPRAW | NOWY ELEMENT (stare: zakaz otwierania przesyłki 6.2 = 0011, 8.3.3; nowe: krew do transfuzji nie podlega ADR, 2.2.62.1.5.7) | 50/65/54 |
| ADR-B-0729 | 02-K11 | B | POPRAW | POPRAW | NOWY ELEMENT (stare: rozpoznanie klasy 7 = 0098, rdzeń podawał „7”; nowe: nalepki 7A/7B/7C na dwóch przeciwległych powierzchniach, 5.2.2.1.11.1) | 74/68/60 |
| ADR-B-0730 | 02-K12 | A | POPRAW | POPRAW | PRZEREDAGOWANIE (temat zachowany: żrąca mgła przy naturalnej wilgoci powietrza – klasa 8, 2.2.8.1.1; usunięto formę „Tak.”) | 60/66/57 |
| ADR-B-0731 | 02-K14 | A | POPRAW | POPRAW | PRZEREDAGOWANIE (temat zachowany: gazy klasy 2 bez grupy pakowania, 2.1.1.3) | 65/66/63 |
| ADR-B-0732 | 03-K02 | B | POPRAW | POPRAW | PRZEREDAGOWANIE (temat zachowany: zapis „ODPAD ZGODNY Z 2.1.3.5.5”, 5.4.1.1.3.1) | 61/58/58 |
| ADR-B-0733 | 03-K03 | B | POPRAW | POPRAW | NOWY ELEMENT (stare: inny towar luzem → czyścić = lustro 0201, 7.5.8 wyczerpany; nowe: próżny nieoczyszczony pojazd po przewozie luzem jak ładowny, 7.3.1.10) | 71/69/69 |
| ADR-B-0734 | 03-K04 | A | POPRAW | POPRAW | NOWY ELEMENT (stare: wyposażenie kanalizacyjne przy nalepce 9 ≈ 0612/0486, błędny punkt 8.1.5.2; nowe: wiersz 6.1 instrukcji pisemnych – zagrożenie dla wód bez znaku ryby i drzewa) | 67/65/67 |
| ADR-B-0735 | 03-K05 | A | POPRAW | POPRAW | NOWY ELEMENT (stare: nie wchodzić w strefę po dokumenty = 0696/0494; nowe: ciecze ładowane pod materiałami stałymi – UWAGA do 7.5.1.5) | 51/51/53 |

## Błędy w raporcie #929 (do poprawienia przy wdrożeniu)

1. **Strony Dz.U.**: definicja temperatury zapłonu 1.2.1 – s. 46 (nie 47); 2.2.41.1.3 – s. 171 (nie 172); 2.2.42.1.3 – s. 182 (nie 183); 2.2.52.1.15 – s. 198 (nie 199; przy zamienniku podano 1286); 5.2.2.1.11.1 – s. 940 (nie 941); 8.1.5.3 – s. 1325 (nie 1326).
2. **Przeoczone duplikaty**: 0728 = 0011 (zakaz otwierania, 8.3.3); 0733 = 0201 (lustro 7.5.8.2); 0735 = 0696/0494; 0724 z 0154; 0725 z 0156. 0729 = 0098 wskazany słusznie.
3. **Merytoryka**: 0728 – twierdzenie, że brak szczególnego przepisu, jest błędne (8.3.3); 0727 – reguła „zapachu” spoza ADR niewskazana wprost; 0722 – klucz sporny wobec definicji 1.2.1.
4. **Zamienniki**: przejęto tylko tematy 0724 (mechanizm samonagrzewania) i 0729 (rozmieszczenie nalepek 7A/7B/7C), z własną treścią. Nie przejęto: 0725 (kod O2 ≈ 0266), 0727 (drogi narażenia = 0623/0158), 0728 (UN 2900 = lustro 0311), 0733 (ten sam temat 7.5.8.2), 0734 (zakres 8.1.5.3 = 0612/0486), 0735 (= 0100/0696), 0726 („plan przewozu”), 0722 (uwaga 1 do 2.2.3.1.1).
5. **Słusznie**: wszystkie 15 POPRAW; licznik 60 → 45; strony 119, 165, 191, 214, 227/228, 234, 264, 626, 963, 974/975, 1286, 1310 trafne; błędny punkt 8.1.5.2 przy 0734 wskazany.

## Szczegóły

### ADR-B-0721 – POPRAW (PRZEREDAGOWANIE (temat zachowany: numer przepisu szczególnego w kolumnie (6) → treść w dziale 3.3; opcje >80 zn. z kropkami))

- Cytaty i strony Dz.U. (nagłówek strony): 3.2.1, objaśnienie kolumny (6): „Zawiera kody numeryczne przepisów szczególnych, które powinny być stosowane.”; 3.3.1 (s. 626).
- Raport #929 (POPRAW): zgoda co do POPRAW; strona 626 trafna; zamiennik #929 przeredagowany inaczej (nasze opcje bez kropek, klucz nie jest jedyną najkrótszą)
- Nowa treść: Przewoźnik sprawdza, czy towar jest dopuszczony do przewozu. W tabeli A przy jego numerze UN w kolumnie (6) podano numer przepisu szczególnego. Nadawca nie sprawdził jego treści. Co trzeba zrobić, zanim uzna się przewóz za dopuszczony?
- Klucz C: Odczytać treść tego przepisu w dziale 3.3 i sprawdzić warunki
- Źródło: ADR 2025, 3.2.1 (objaśnienie kolumny (6) „Przepisy szczególne”); 3.3.1 (znaczenie i wymagania przepisów szczególnych)
- Uwagi: 3.2.1 kolumna (6); 3.3.1 s. 626. Przeredagowanie – opcje >80 znaków z kropkami; temat bez zmian, bez duplikatu.

### ADR-B-0722 – POPRAW (NOWY ELEMENT (stare: 8 °C a temperatura zapłonu 18 °C – klucz sporny wobec definicji 1.2.1, bliskie 0658; nowe: grupa pakowania cieczy klasy 3 z tabeli 2.2.3.1.3))

- Cytaty i strony Dz.U. (nagłówek strony): Pytanie z banku: 1.2.1 definicja temperatury zapłonu (s. 46); 2.2.3.1.1 (s. 165). Nowe: 2.2.3.1.3 – tabela grup pakowania (s. 165–166, czytana z obrazu strony): I – początek wrzenia ≤ 35 °C; II – zapłon < 23 °C, początek wrzenia > 35 °C; III – zapłon ≥ 23 °C i ≤ 60 °C, początek wrzenia > 35 °C; przypis a → 2.2.3.1.4 (ciecze lepkie).
- Raport #929 (POPRAW): zgoda co do POPRAW; strona definicji 1.2.1 to 46, nie 47; zamiennik #929 (uwaga 1 do 2.2.3.1.1 – brak podtrzymywania palenia) nie przejęty – wybrano podstawową regułę grup pakowania 2.2.3.1.3
- Nowa treść: Rozpuszczalnik bez zagrożeń dodatkowych ma temperaturę zapłonu 18 °C i temperaturę początku wrzenia 80 °C. Nie jest cieczą lepką. Do której grupy pakowania zalicza go tabela w 2.2.3.1.3?
- Klucz B: Do II grupy: zapłon poniżej 23 °C, wrzenie powyżej 35 °C
- Źródło: ADR 2025, 2.2.3.1.3 (tabela grup pakowania według temperatury zapłonu i temperatury początku wrzenia)
- Uwagi: 2.2.3.1.3 s. 165–166 (przypis a → 2.2.3.1.4 dla cieczy lepkich). Nowy element – stary klucz sporny w świetle 1.2.1 (s. 46), bliski 0658.

### ADR-B-0723 – POPRAW (PRZEREDAGOWANIE (temat zachowany: materiał łatwo zapalny stały zapala się od krótkiego kontaktu ze źródłem zapłonu – iskry ze szlifierki))

- Cytaty i strony Dz.U. (nagłówek strony): 2.2.41.1.3 (s. 171): materiały łatwo zapalne stałe – sproszkowane, granulowane lub w postaci pasty, które łatwo się zapalają przy krótkotrwałym kontakcie ze źródłem zapłonu.
- Raport #929 (POPRAW): zgoda co do POPRAW; strona 171, nie 172; zamiennik #929 (toksyczne produkty spalania) nie przejęty – przeredagowano z zachowaniem tematu
- Nowa treść: Przy załadunku worków z granulatem oznakowanych jako materiał zapalny stały klasy 4.1 pracownik szlifuje metal tuż obok pojazdu. Twierdzi, że iskry są groźne dla cieczy i gazów, a nie dla materiałów stałych. Jak ocenić to twierdzenie?
- Klucz C: Jest błędne, bo granulat może się łatwo zapalić od źródła zapłonu
- Źródło: ADR 2025, 2.2.41.1.1; 2.2.41.1.3 (materiały łatwo zapalne stałe – zapalenie po krótkotrwałym kontakcie ze źródłem zapłonu)
- Uwagi: 2.2.41.1.3 s. 171 (nie 172). Przeredagowanie – opcje >80 znaków, słowo „całkowicie”.

### ADR-B-0724 – POPRAW (NOWY ELEMENT (stare: ciepło własne i samozapalenie = 0154; nowe: kiedy samonagrzewanie kończy się samozapaleniem – bilans ciepła, 2.2.42.1.3))

- Cytaty i strony Dz.U. (nagłówek strony): Pytanie z banku: 2.2.42.1.1 (s. 182). Nowe: 2.2.42.1.3 (s. 182) – samonagrzewanie w reakcji z tlenem powietrza; samozapalenie, gdy szybkość generowania ciepła przewyższa szybkość jego wydzielania.
- Raport #929 (POPRAW): zgoda co do POPRAW; przeoczony duplikat z 0154; strona 2.2.42.1.3 to 182, nie 183; temat zamiennika (mechanizm samonagrzewania) przejęty w formie scenariusza
- Nowa treść: Worki z materiałem samonagrzewającym się klasy 4.2 leżą w dużym, ciasnym stosie. Kolega pyta, od czego zależy, czy samonagrzewanie skończy się samozapaleniem. Co wyjaśnia ADR?
- Klucz A: Od tego, czy ciepło powstaje szybciej, niż może zostać oddane
- Źródło: ADR 2025, 2.2.42.1.3 (samonagrzewanie: ciepło z reakcji z tlenem powietrza; samozapalenie, gdy szybkość generowania ciepła przewyższa szybkość jego wydzielania)
- Uwagi: 2.2.42.1.3 s. 182. Nowy element – stare pytanie = 0154; 0665 i 0361 dotyczą innych aspektów klasy 4.2.

### ADR-B-0725 – POPRAW (NOWY ELEMENT (stare: utleniacz nasila spalanie innych materiałów = 0156; nowe: materiał niedopuszczony – niestabilizowany roztwór nadtlenku wodoru > 60%, 2.2.51.2.2))

- Cytaty i strony Dz.U. (nagłówek strony): Pytanie z banku: 2.2.51.1.1 (s. 191). Nowe: 2.2.51.2.2 (s. 193) – niedopuszczony do przewozu: nadtlenek wodoru, niestabilizowany lub nadtlenek wodoru, roztwór wodny, niestabilizowany, zawierający więcej niż 60% nadtlenku wodoru.
- Raport #929 (POPRAW): zgoda co do POPRAW; przeoczony duplikat z 0156; zamiennik #929 (kod O2) bliski 0266 – nie przejęty
- Nowa treść: Nadawca chce wysłać kanistry z niestabilizowanym roztworem wodnym nadtlenku wodoru, który zawiera 70% nadtlenku wodoru. Kanistry są szczelne i oznakowane. Czy ADR dopuszcza ten materiał klasy 5.1 do przewozu?
- Klucz B: Nie, ADR nie dopuszcza takiego roztworu powyżej 60% nadtlenku
- Źródło: ADR 2025, 2.2.51.2.2 (materiały niedopuszczone do przewozu: nadtlenek wodoru, niestabilizowany lub roztwór wodny niestabilizowany, zawierający więcej niż 60% nadtlenku wodoru)
- Uwagi: 2.2.51.2.2 s. 193. Nowy element – stare pytanie = 0156 (utleniacz nasila spalanie). Znaczenie praktyczne do oceny specjalisty.

### ADR-B-0726 – POPRAW (NOWY ELEMENT (stare: reakcja na wzrost temperatury ≈ 0667, „powiadomić” spoza ADR; nowe: dwa czujniki, sprawdzanie co 4–6 godzin i zapis, 7.1.7.4.2))

- Cytaty i strony Dz.U. (nagłówek strony): Pytanie z banku: 2.2.52.1.15 (s. 198), 7.1.7 (s. 1285–1286). Nowe: 7.1.7.4.2 (s. 1286) – dwa niezależne czujniki, rejestracja, sprawdzanie co cztery do sześciu godzin i zapis.
- Raport #929 (POPRAW): zgoda co do POPRAW; strona 2.2.52.1.15 to 198, nie 199 (#929 podał 1286 jako stronę zamiennika z 2.2.52.1.15); zamiennik „plan przewozu” nie przejęty
- Nowa treść: Jednostka przewozi nadtlenek organiczny klasy 5.2 w temperaturze kontrolowanej. Temperaturę powietrza w przestrzeni ładunkowej mierzą dwa niezależne czujniki. Jak często według ADR trzeba ją sprawdzać i zapisywać?
- Klucz C: Co cztery do sześciu godzin, z zapisem wyników pomiaru
- Źródło: ADR 2025, 2.2.52.1.15 (nadtlenki organiczne wymagające kontrolowania temperatury); 7.1.7.4.2 (dwa niezależne czujniki; sprawdzanie co cztery do sześciu godzin i rejestracja)
- Uwagi: 7.1.7.4.2 s. 1286; 2.2.52.1.15 s. 198. Nowy element – stare ≈ 0667, „powiadomić” spoza ADR. Reguła z 7.1.7 przy kompetencji 2.2.52 – do oceny.

### ADR-B-0727 – POPRAW (NOWY ELEMENT (stare: brak zapachu nie wyklucza zatrucia – reguła spoza ADR; nowe: kod klasyfikacyjny TF1 = trujący zapalny ciekły, 2.2.61.1.2))

- Cytaty i strony Dz.U. (nagłówek strony): Pytanie z banku: 2.2.61.1.1 (s. 214) – nic o zapachu. Nowe: 2.2.61.1.2 (s. 214) – TF „Materiały trujące, zapalne”: TF1 Materiały ciekłe; T6 Materiały ciekłe stosowane jako pestycydy; TC – trujące żrące.
- Raport #929 (POPRAW): zgoda co do POPRAW; reguła zapachu spoza ADR nie wskazana wprost; zamiennik #929 (drogi narażenia) dubluje 0623/0158 – nie przejęty
- Nowa treść: W kolumnie (3b) tabeli A materiał klasy 6.1 ma kod klasyfikacyjny TF1. Kolega uważa, że skoro to materiał trujący, nie trzeba się obawiać pożaru. Co oznacza ten kod?
- Klucz B: Materiał trujący ciekły, który jest także materiałem zapalnym
- Źródło: ADR 2025, 2.2.61.1.2 (kody klasyfikacyjne klasy 6.1: TF1 – materiały trujące zapalne ciekłe; TC – trujące żrące; T6 – pestycydy ciekłe); 3.2.1 (kolumna (3b))
- Uwagi: 2.2.61.1.2 s. 214. Nowy element – stare (zapach) spoza ADR. Format kodu podobny do 0218/0265/0302/0266 – do oceny.

### ADR-B-0728 – POPRAW (NOWY ELEMENT (stare: zakaz otwierania przesyłki 6.2 = 0011, 8.3.3; nowe: krew do transfuzji nie podlega ADR, 2.2.62.1.5.7))

- Cytaty i strony Dz.U. (nagłówek strony): Pytanie z banku: 2.2.62.1.1 (s. 227), 8.3.3. Nowe: 2.2.62.1.5.7 (s. 230) – krew lub jej składniki pozyskane w celu transfuzji … nie podlegają przepisom ADR.
- Raport #929 (POPRAW): zgoda co do POPRAW; przeoczony duplikat 0728 = 0011; twierdzenie o braku przepisu błędne (8.3.3 istnieje); zamiennik UN 2900 to lustro 0311 – nie przejęty
- Nowa treść: Kierowca wiezie z centrum krwiodawstwa do szpitala krew pobraną w celu transfuzji. Pracownik szpitala twierdzi, że krew to zawsze materiał zakaźny klasy 6.2. Co mówi ADR o takiej przesyłce?
- Klucz C: Krew pozyskaną do transfuzji wyłączono z przepisów ADR
- Źródło: ADR 2025, 2.2.62.1.1; 2.2.62.1.5.7 (krew lub jej składniki pozyskane w celu transfuzji nie podlegają przepisom ADR)
- Uwagi: 2.2.62.1.5.7 s. 230. Nowy element – stare = 0011 (8.3.3). Pominięto 2.2.62.1.5.8 (wątpliwe tłumaczenie).

### ADR-B-0729 – POPRAW (NOWY ELEMENT (stare: rozpoznanie klasy 7 = 0098, rdzeń podawał „7”; nowe: nalepki 7A/7B/7C na dwóch przeciwległych powierzchniach, 5.2.2.1.11.1))

- Cytaty i strony Dz.U. (nagłówek strony): Pytanie z banku: 2.2.7.1.1 (s. 234). Nowe: 5.2.2.1.11.1 (s. 940, sprawdzone na obrazie strony) – nalepki 7A, 7B lub 7C na dwóch przeciwległych zewnętrznych powierzchniach sztuki przesyłki.
- Raport #929 (POPRAW): zgoda co do POPRAW; duplikat 0098 wskazany; strona 5.2.2.1.11.1 to 940, nie 941; temat zamiennika (rozmieszczenie nalepek) przejęty, treść własna
- Nowa treść: Kierowca odbiera sztukę przesyłki z materiałem promieniotwórczym kategorii II-ŻÓŁTA. Nalepkę wzoru 7B naklejono jedynie na wieku kartonu. Gdzie według ADR powinny być nalepki na takiej sztuce przesyłki?
- Klucz B: Na dwóch przeciwległych zewnętrznych powierzchniach sztuki przesyłki
- Źródło: ADR 2025, 5.2.2.1.11.1 (nalepki 7A, 7B lub 7C na dwóch przeciwległych zewnętrznych powierzchniach sztuki przesyłki)
- Uwagi: 5.2.2.1.11.1 s. 940 (nie 941). Nowy element – stare = 0098, rdzeń podawał numer 7.

### ADR-B-0730 – POPRAW (PRZEREDAGOWANIE (temat zachowany: żrąca mgła przy naturalnej wilgoci powietrza – klasa 8, 2.2.8.1.1; usunięto formę „Tak.”))

- Cytaty i strony Dz.U. (nagłówek strony): 2.2.8.1.1 (s. 264): również materiały, które … w obecności naturalnej wilgoci powietrza wydzielają żrące pary lub mgły.
- Raport #929 (POPRAW): zgoda co do POPRAW; strona 264 trafna; przeredagowano z zachowaniem tematu (zamiennik #929 zbyt ogólny)
- Nowa treść: Karta towaru podaje, że suchy materiał nie działa żrąco, ale przy naturalnej wilgoci powietrza wydziela żrącą mgłę. Magazynier uważa, że skoro suchy materiał nie jest żrący, nie może należeć do klasy 8. Jak to ocenić?
- Klucz A: Może należeć do klasy 8, bo obejmuje ona też takie materiały
- Źródło: ADR 2025, 2.2.8.1.1 (materiały tworzące żrącą parę lub mgłę w obecności naturalnej wilgoci powietrza)
- Uwagi: 2.2.8.1.1 s. 264. Przeredagowanie – forma „Tak.”, długości opcji.

### ADR-B-0731 – POPRAW (PRZEREDAGOWANIE (temat zachowany: gazy klasy 2 bez grupy pakowania, 2.1.1.3))

- Cytaty i strony Dz.U. (nagłówek strony): 2.1.1.3 (s. 119): grupy pakowania przypisuje się materiałom klas innych niż 1, 2, 5.2, 6.2 i 7 oraz innym niż samoreaktywne klasy 4.1.
- Raport #929 (POPRAW): zgoda co do POPRAW; strona 119 trafna; przeredagowano z zachowaniem tematu
- Nowa treść: Kierowca porównuje dokument przewozowy z tabelą A dla gazu klasy 2. W kolumnie (4) przy tym gazie nie podano grupy pakowania. Co z tego wynika?
- Klucz A: To prawidłowe, bo gazów klasy 2 nie zalicza się do grup pakowania
- Źródło: ADR 2025, 2.1.1.3 (grupy pakowania nie dotyczą klasy 2); 3.2.1 (kolumna (4))
- Uwagi: 2.1.1.3 s. 119. Przeredagowanie – długości opcji, kropki.

### ADR-B-0732 – POPRAW (PRZEREDAGOWANIE (temat zachowany: zapis „ODPAD ZGODNY Z 2.1.3.5.5”, 5.4.1.1.3.1))

- Cytaty i strony Dz.U. (nagłówek strony): 5.4.1.1.3.1 (s. 963): opis uzupełnia się zapisem „ODPAD ZGODNY Z 2.1.3.5.5”.
- Raport #929 (POPRAW): zgoda co do POPRAW; strona 963 trafna; przeredagowano z zachowaniem tematu
- Nowa treść: Zakład wysyła odpad, który sklasyfikowano według 2.1.3.5.5. W dokumencie przewozowym podano już numer UN, nazwę przewozową z wyrazem „ODPAD”, klasę i grupę pakowania. Jaki zapis trzeba jeszcze dodać do opisu towaru?
- Klucz B: Zapis „ODPAD ZGODNY Z 2.1.3.5.5” uzupełniający opis towaru
- Źródło: ADR 2025, 5.4.1.1.3.1 (zapis „ODPAD ZGODNY Z 2.1.3.5.5”); 2.1.3.5.5
- Uwagi: 5.4.1.1.3.1 s. 963. Przeredagowanie – długości opcji, kropki; temat unikatowy w banku.

### ADR-B-0733 – POPRAW (NOWY ELEMENT (stare: inny towar luzem → czyścić = lustro 0201, 7.5.8 wyczerpany; nowe: próżny nieoczyszczony pojazd po przewozie luzem jak ładowny, 7.3.1.10))

- Cytaty i strony Dz.U. (nagłówek strony): Pytanie z banku: 7.5.8.2 (s. 1310). Nowe: 7.3.1.10 (s. 1292) – próżne pojazdy … po przewozie luzem materiałów niebezpiecznych stałych spełniają wymagania jak w stanie ładownym, chyba że zastosowano odpowiednie środki eliminujące wszystkie zagrożenia.
- Raport #929 (POPRAW): zgoda co do POPRAW; przeoczony duplikat 0733 = 0201 (lustro, 7.5.8.2); zamiennik #929 (UN 1993 → UN 1203) to ten sam temat – nie przejęty
- Nowa treść: Wywrotka przewiozła luzem materiał stały, dla którego wymagane było przykrycie skrzyni opończą. Po rozładunku nie została oczyszczona. Kierowca chce wracać do bazy z odkrytą skrzynią, bo ładunku już nie ma. Co wynika z 7.3.1.10?
- Klucz B: Do usunięcia zagrożeń stosuje się wymagania jak dla pojazdu ładownego
- Źródło: ADR 2025, 7.3.1.10 (próżne pojazdy po przewozie luzem materiałów stałych spełniają wymagania jak w stanie ładownym, chyba że wyeliminowano wszystkie zagrożenia)
- Uwagi: 7.3.1.10 s. 1292. Nowy element – stare = lustro 0201 (7.5.8.2); 7.5.8 wyczerpany. Związek z 0563 (5.3.1.6.1) – do oceny.

### ADR-B-0734 – POPRAW (NOWY ELEMENT (stare: wyposażenie kanalizacyjne przy nalepce 9 ≈ 0612/0486, błędny punkt 8.1.5.2; nowe: wiersz 6.1 instrukcji pisemnych – zagrożenie dla wód bez znaku ryby i drzewa))

- Cytaty i strony Dz.U. (nagłówek strony): Pytanie z banku: 8.1.5.3 (s. 1325, z przypisem; w banku błędnie 8.1.5.2). Nowe: 5.4.3.4, wzór instrukcji pisemnych (s. 977, sprawdzone na obrazie strony) – nalepka 6.1: „Zagrożenie zatruciem w wyniku wdychania, kontaktu ze skórą lub połknięcia. Zagrożenie w przypadku przedostania się do środowiska wodnego lub kanalizacji.”
- Raport #929 (POPRAW): zgoda co do POPRAW i co do błędnego punktu 8.1.5.2; strona 8.1.5.3 to 1325, nie 1326; zamiennik #929 (zakres 8.1.5.3) dubluje 0612/0486 – nie przejęty
- Nowa treść: Po kolizji z przebitej beczki z nalepką 6.1 ciecz spływa w stronę rowu z wodą. Na kanistrze nie ma znaku ryby i drzewa. Pomocnik uważa, że bez tego znaku wyciek nie zagraża wodzie. Co podają instrukcje pisemne dla nalepki 6.1?
- Klucz A: Że grozi również szkoda po przedostaniu się do wody lub kanalizacji
- Źródło: ADR 2025, 5.4.3.4 (wzór instrukcji pisemnych: nalepka 6.1 – zagrożenie zatruciem oraz zagrożenie w przypadku przedostania się do środowiska wodnego lub kanalizacji)
- Uwagi: 5.4.3.4 s. 977. Nowy element – stare ≈ 0612/0486, punkt 8.1.5.2 błędny (właściwy 8.1.5.3, s. 1325). Związek z 0681/0651/0650 – do oceny.

### ADR-B-0735 – POPRAW (NOWY ELEMENT (stare: nie wchodzić w strefę po dokumenty = 0696/0494; nowe: ciecze ładowane pod materiałami stałymi – UWAGA do 7.5.1.5))

- Cytaty i strony Dz.U. (nagłówek strony): Pytanie z banku: 5.4.3.4 (s. 974–975). Nowe: 7.5.1.5 UWAGA (s. 1305) – „Jeżeli jest to możliwe, to towary niebezpieczne w stanie ciekłym powinny być załadowane pod towarami niebezpiecznymi w stanie stałym.”
- Raport #929 (POPRAW): zgoda co do POPRAW; przeoczone duplikaty 0696/0494; zamiennik #929 („jeżeli to możliwe i bezpieczne”) dubluje 0100/0696 – nie przejęty
- Nowa treść: Do jednego pojazdu trafiają kanistry z cieczą żrącą klasy 8 i kartony z materiałem stałym klasy 9. Oba rodzaje sztuk przesyłek można piętrzyć. Magazynier chce postawić kanistry na kartonach. Jak według ADR należy je ułożyć, jeżeli to możliwe?
- Klucz A: Kanistry z cieczą pod kartonami z materiałem stałym
- Źródło: ADR 2025, 7.5.1.5 (UWAGA: towary niebezpieczne w stanie ciekłym, jeżeli jest to możliwe, ładuje się pod towarami niebezpiecznymi w stanie stałym)
- Uwagi: 7.5.1.5 s. 1305. Nowy element – stare = 0696/0494 (5.4.3.4 wyczerpany). Dopasowanie do 03-K05 (5.4.3.4) – do oceny.

## Wskaźniki

- „Poprawna = jedyna najdłuższa”: **15/780 = 1,92% → 11/780 = 1,41%** (stare 0724, 0725, 0726, 0727 miały klucz jako jedyną najdłuższą opcję); maksimum działu 5,66% bez zmian. Wskaźnik poprawiony w docs/POKRYCIE-KURSU.md, docs/STAN-KONCOWY-BANKU-ADR-PODSTAWOWY-2026-11-03.md i podstawowy/README.md.
- „Poprawna = jedyna najkrótsza”: **80/780 → 75/780**; każdy dział ≤ 38% (maks. 16,1% bez zmian; dział 02: 7 → 4/89, dział 03: 6 → 4/60, dział 01: 7/54 bez zmian).
- Żadna opcja nowych rekordów nie kończy się kropką, nie ma średnika ani słów absolutnych, wszystkie ≤ 80 zn.; klucz nigdy nie jest jedyną najdłuższą ani jedyną najkrótszą. Objaśnienia: 5–5 zdań, 358–485 znaków, ≤ 27 słów w zdaniu, ostatnie zdanie „Podstawa: ADR …”.
- similarity.py: cały bank – po poprawkach przy 0,45 brak par z partią; przy 0,25 z partią 4 pary (0218/0727 = 0,278 – inny kod klasyfikacyjny; 0294/0732 = 0,267 i 0466/0732 = 0,250 – inne elementy opisu odpadu; 0681/0734 = 0,250 – nalepka 3 ze znakiem ryby i drzewa a nalepka 6.1 bez znaku). check_near_duplicates (0,60) i check_cross_module_duplicates (0,80) – bez kandydatów. Wyszukiwanie po temacie: grupy pakowania klasy 3, bilans ciepła 4.2, nadtlenek wodoru > 60%, pomiar co 4–6 godzin, kod TF1, krew do transfuzji, nalepki 7A/7B/7C na dwóch powierzchniach, próżny pojazd po przewozie luzem, wiersz 6.1 instrukcji pisemnych, ciecze pod materiałami stałymi – brak duplikatów (pokrewne: 0658, 0154, 0361, 0665, 0156, 0266, 0667, 0218, 0011, 0098, 0201, 0563, 0612, 0681, 0696).
- Kompetencje: liczby bez zmian (każda kompetencja partii nadal 6); 05-K13, 05-K14, 05-K15 nadal po 5; kompetencje.json bez zmian.

## Synchronizacja (test na kopii repo)

- review/sequential/ i review/legal-clauses/: 721-721.json … 735-735.json – snapshoty; w legal-clauses clause, answer_review A/B/C, notes_on_conditions.
- Ledgery z PAKIET-0780-MANIFEST (stage4w4-literal-verification-ledger-0001-0609.json i 0610-0678.json) – 15 wpisów.
- Egzaminy 001–005: ŻADEN wariant nie zawiera 0721–0735 – zmienia się tylko SHA (10 plików). Kolejki 4X40/4X44 – tylko SHA.
- SHA 884f19a0… → 5448ab43… we wszystkich plikach poza review/literal-pl/ i FIRST_PASS_BANK_SHA w tests/test_literal_review_0721_0735.py (test z #929 ma już dwie stałe – zmienia się tylko EXPECTED_BANK_SHA).
- REJESTR-AKTUALNY-0001-0765.md i 0001-0780.md – wiersze 0721–0735.
- tools/apply_poprawki.py – wpis „POPRAWKI-KONTROLA2-0706-0720.jsonl” miał wcięcie 8 spacji (poprawione na 4) i dopisany „POPRAWKI-KONTROLA2-0721-0735.jsonl”.
- Lekcje i instruktor (ID w lekcji tylko z modułu lekcji): ADR-B-01 (0721 – doprecyzowanie), ADR-B-02 (0722 – sekcja wymieniona na grupy pakowania; samonagrzewanie → 0154 + sekcja 0724; utleniacze → 0156 + sekcja 0725; kontrola temperatury → 0667 + sekcja 0726; materiały trujące → 0623 + sekcja TF1 0727; materiały zakaźne bez ID + sekcja krwi 0728; rozpoznawanie klasy 7 → 0098 + sekcja nalepek 0729; 0723 – doprecyzowanie), ADR-B-03 (czyszczenie po przewozie luzem + sekcja 7.3.1.10 0733; nalepka 9 → 0612 + sekcja 6.1 0734; dokumenty za rozlewem bez ID + sekcja 7.5.1.5 0735), instruktor ADR-B-02 (0725 → 0156) i ADR-B-03 (scenariusz SC-ADR-B-03-04 + 7.3.1.10; zadanie kanalizacyjne → 0612). Scenariusz SC-ADR-B-03-04 w scenariusze-13-dzialow.json: pytanie 0733 zostaje (pytania scenariusza muszą być z modułu 03), dodany krok, typowy błąd i podstawa 7.3.1.10.

## Wynik testu

Git worktree z origin/main 0a2469d60 (lokalna gałąź kontrola2-0721-0735-wdrozenie) + POPRAWKI + synchronizacja: 14 skryptów CI zielonych (validate, coverage, check_mock_exam_variants, answer_leakage_metrics, answer_length_bias --threshold 0.16 --strict, check_explanation_quality --minimum 300, check_near_duplicates 0.60, check_cross_module_duplicates 0.80, similarity, check_explanation_heuristics, release_gate --report, check_sequential_audit, check_legal_clause_review, course_consistency); `python3 -m unittest discover -s tests` – **263/263 OK**. Blob banku po zastosowaniu: `5448ab43d2bed3ac17abd384b6bdc1eb596ef93f`.

## Do pakietu dla specjalistów

- 0733 – 7.3.1.10 (próżny nieoczyszczony pojazd po przewozie luzem) a 0563 (tablice na próżnym pojeździe, 5.3.1.6.1) – czy oba mogą zostać; dopasowanie 7.3.1.10 do 03-K03 (legal_refs 7.5.8.1–7.5.8.2).
- 0734 – wiersz 6.1 instrukcji pisemnych a 0681 (nalepka 3 + znak ryby i drzewa), 0651 (6.2) i 0650 (8) – czy nie za bliskie.
- 0735 – UWAGA do 7.5.1.5 (zalecenie „jeżeli jest to możliwe”) w kompetencji 03-K05 (legal_refs 5.4.3.4) – dopasowanie do kompetencji.
- 0727 – format pytania o kod klasyfikacyjny podobny do 0218 (FC), 0265, 0302, 0266 – czy to nie nadmiar pytań o kody.
- 0725 – znaczenie praktyczne materiału niedopuszczonego dla kierowcy (2.2.51.2.2).
- 0726 – reguła z 7.1.7.4.2 w kompetencji 02-K08 (2.2.52) – dopasowanie; bez odniesień do cystern.
- 0728 – 2.2.62.1.5.7 a inne wyłączenia 2.2.62.1.5 (2.2.62.1.5.8 pominięto z powodu wątpliwego tłumaczenia).
- 0722 – nowy element; stary klucz (ciecz poniżej temperatury zapłonu) sporny wobec definicji 1.2.1 – potwierdzić decyzję o wymianie.
- poza partią (bez zmian teraz): 0769 dubluje 0514; 0247 = 0770 (partia 52); 0772 – wątpliwe; 0777 – „Delivery Sale”; 0708 a 0714; 0712 i 0715 – źródła spoza ADR.
