# Etap 4w — audyt pokrycia programu kursu podstawowego ADR

**Punkt odniesienia:** `main` `efd48dd4a849729864dc5ac8b1ed9d6abb13a988`, bank 569 pytań (ADR-B-0001–0569); 13 działów, 106 roboczych kompetencji. Data audytu: 25.10.2026.

**Dokumenty nadrzędne:** [ADR 2025, 8.2.2.3.2](https://unece.org/adr-2025-files), [polski ramowy program kursu początkowego podstawowego, Dz.U. 2021 poz. 2150, zał. 1](https://www.dziennikustaw.gov.pl/DU/2021/2150), [program redakcyjny](../docs/PROGRAM-PODSTAWOWY.md) i [mapa kompetencji](../podstawowy/kompetencje.json).

## Wniosek i interpretacja

- **103/103 kompetencji teoretycznych ma co najmniej jedno istniejące ID pytania, 0 luk typu „brak jakiegokolwiek pytania” w aktualnej mapie.** Liczba pytań i pokrycie tematyczne nie dowodzą poprawności ani rzeczywistej głębokości nauczania.
- **3 kompetencje praktyczne nie mają pytań z założenia:** odpowiadają im ćwiczenia P1–P3 w `podstawowy/praktyka/SCENARIUSZE.md`. Oznaczono je „nie dotyczy quizu”, a nie „uzupełnione testem”. Obecność scenariusza nie jest potwierdzeniem wykonania praktyki.
- **0 pytań bez przypisania i 0 nieistniejących ID w mapie.** Wszystkie pytania pozostają `needs_review` — brak podstaw do automatycznego `verified`.
- Polski program to 13 tematów (a–m), a ADR 8.2.2.3.2 wymienia minimalne zagadnienia, które nie muszą mieć identycznego porządku z wewnętrznymi 13 działami. Dotyczy to zwłaszcza odpowiedzialności cywilnej, przewozu kombinowanego, załadunku i rozładunku; nie wolno porównywać tematów tylko po numerze litery.
- **Luka jakościowa nadal otwarta:** brak formalnego zatwierdzenia zgodności każdej odpowiedzi A/B/C i każdego akapitu z aktualnym polskim brzmieniem prawa; nie da się oznaczyć „pełnego pokrycia prawa” na podstawie samego JSON.
- **Decyzja wydawnicza tej partii:** nie dopisywać pytań 0570+ bez wskazania konkretnego niepokrytego zagadnienia potwierdzonego w przepisie. Priorytet pogłębiania: B-01, B-11, B-13 — po 35 pytań, ale sama liczba nie jest luką merytoryczną.

## Mapa 13 tematów programu → pytania → luka

| Temat polski | Dział projektu | Zakres skrócony | Liczba pytań | Kompetencje teorii | Luka: brak pytania? | Otwarta kontrola jakości |
|---|---|---|---:|---:|---|---|
| a | ADR-B-01 | Przepisy ogólne, pojęcia i wyłączenia | 35 | 7 | NIE | Pełna recenzja ADR i dydaktyki: otwarta |
| b | ADR-B-02 | Klasyfikacja i główne rodzaje zagrożeń | 56 | 14 | NIE | Pełna recenzja ADR i dydaktyki: otwarta |
| c | ADR-B-03 | Ochrona środowiska i odpady | 49 | 6 | NIE | Pełna recenzja ADR i dydaktyki: otwarta |
| d | ADR-B-04 | Zapobieganie zdarzeniom | 44 | 6 | NIE | Pełna recenzja ADR i dydaktyki: otwarta |
| e | ADR-B-05 | Postępowanie po wypadku, pierwsza pomoc | 40 | 12 | NIE | Pełna recenzja ADR i dydaktyki: otwarta |
| f | ADR-B-06 | Nalepki, znaki i tablice | 45 | 9 | NIE | Pełna recenzja ADR i dydaktyki: otwarta |
| g | ADR-B-07 | Obowiązki kierowcy i uczestników, odpowiedzialność cywilna | 46 | 7 | NIE | Pełna recenzja ADR i dydaktyki: otwarta |
| h | ADR-B-08 | Wyposażenie pojazdu i ochronne | 40 | 8 | NIE | Pełna recenzja ADR i dydaktyki: otwarta |
| i | ADR-B-09 | Załadunek, rozładunek, zakazy łączenia | 46 | 9 | NIE | Pełna recenzja ADR i dydaktyki: otwarta |
| j | ADR-B-10 | Przewóz kombinowany | 55 | 5 | NIE | Pełna recenzja ADR i dydaktyki: otwarta |
| k | ADR-B-11 | Ograniczenia tunelowe i zachowanie w tunelu | 35 | 7 | NIE | Pełna recenzja ADR i dydaktyki: otwarta |
| l | ADR-B-12 | Ochrona przewozu przed nieuprawnionym dostępem | 43 | 6 | NIE | Pełna recenzja ADR i dydaktyki: otwarta |
| m | ADR-B-13 | Dokumentacja przewozowa | 35 | 8 | NIE | Pełna recenzja ADR i dydaktyki: otwarta |

## Mapa wszystkich 106 kompetencji → istniejące ID pytań → luka

**Definicja luki w tej tabeli:** „TAK” tylko przy teoretycznej kompetencji bez istniejącego ID w banku. „N/D — praktyka” oznacza ćwiczenie wymagające instruktora, nie brak pytań. Status recenzji merytorycznej nie wynika z tej kolumny.

| Dział | ID kompetencji | Temat / umiejętność | Punkt prawa z mapy | ID pytań | Luka? |
|---|---|---|---|---|---|
| ADR-B-01 | ADR-B-01-K01 | Ramy prawne i definicje ADR | 1.1, 1.2 | `ADR-B-0123`, `ADR-B-0147`, `ADR-B-0312` | NIE |
| ADR-B-01 | ADR-B-01-K02 | Szkolenie osób uczestniczących w przewozie | 1.3 | `ADR-B-0001`, `ADR-B-0040`, `ADR-B-0041`, `ADR-B-0092`, `ADR-B-0513`, `ADR-B-0520`, `ADR-B-0521`, `ADR-B-0522`, `ADR-B-0529` | NIE |
| ADR-B-01 | ADR-B-01-K03 | Kiedy kierowca potrzebuje zaświadczenia ADR | 8.2.1 | `ADR-B-0003`, `ADR-B-0148`, `ADR-B-0301` | NIE |
| ADR-B-01 | ADR-B-01-K04 | Wyłączenia ze względu na charakter przewozu | 1.1.3.1 | `ADR-B-0002`, `ADR-B-0091`, `ADR-B-0313` | NIE |
| ADR-B-01 | ADR-B-01-K05 | Ilości ograniczone LQ i wyłączone EQ | 3.4, 3.5 | `ADR-B-0093`, `ADR-B-0149`, `ADR-B-0260`, `ADR-B-0261`, `ADR-B-0273`, `ADR-B-0526`, `ADR-B-0527`, `ADR-B-0528`, `ADR-B-0534`, `ADR-B-0535` | NIE |
| ADR-B-01 | ADR-B-01-K06 | Progi i kategorie transportowe 1.1.3.6 | 1.1.3.6 | `ADR-B-0002`, `ADR-B-0093`, `ADR-B-0259`, `ADR-B-0271`, `ADR-B-0272`, `ADR-B-0323` | NIE |
| ADR-B-01 | ADR-B-01-K07 | Towary zabronione i dopuszczone do przewozu | 2.1, 3.2, 3.3 | `ADR-B-0124`, `ADR-B-0125`, `ADR-B-0314` | NIE |
| ADR-B-02 | ADR-B-02-K01 | Klasa 1: materiały i przedmioty wybuchowe (rozpoznawanie) | 2.2.1 | `ADR-B-0126`, `ADR-B-0150`, `ADR-B-0316`, `ADR-B-0495`, `ADR-B-0496`, `ADR-B-0497`, `ADR-B-0498` | NIE |
| ADR-B-02 | ADR-B-02-K02 | Klasa 2: gazy | 2.2.2 | `ADR-B-0042`, `ADR-B-0151`, `ADR-B-0284`, `ADR-B-0541` | NIE |
| ADR-B-02 | ADR-B-02-K03 | Klasa 3: materiały ciekłe zapalne | 2.2.3 | `ADR-B-0004`, `ADR-B-0152`, `ADR-B-0288`, `ADR-B-0542` | NIE |
| ADR-B-02 | ADR-B-02-K04 | Klasa 4.1: materiały stałe zapalne | 2.2.41 | `ADR-B-0094`, `ADR-B-0153`, `ADR-B-0268` | NIE |
| ADR-B-02 | ADR-B-02-K05 | Klasa 4.2: materiały samonagrzewające się / samozapalne | 2.2.42 | `ADR-B-0095`, `ADR-B-0154`, `ADR-B-0302` | NIE |
| ADR-B-02 | ADR-B-02-K06 | Klasa 4.3: reagujące z wodą | 2.2.43 | `ADR-B-0006`, `ADR-B-0155`, `ADR-B-0265`, `ADR-B-0269`, `ADR-B-0510` | NIE |
| ADR-B-02 | ADR-B-02-K07 | Klasa 5.1: materiały utleniające | 2.2.51 | `ADR-B-0044`, `ADR-B-0156`, `ADR-B-0266`, `ADR-B-0270` | NIE |
| ADR-B-02 | ADR-B-02-K08 | Klasa 5.2: nadtlenki organiczne | 2.2.52 | `ADR-B-0096`, `ADR-B-0157`, `ADR-B-0307` | NIE |
| ADR-B-02 | ADR-B-02-K09 | Klasa 6.1: materiały trujące | 2.2.61 | `ADR-B-0097`, `ADR-B-0158`, `ADR-B-0289` | NIE |
| ADR-B-02 | ADR-B-02-K10 | Klasa 6.2: materiały zakaźne | 2.2.62 | `ADR-B-0043`, `ADR-B-0159`, `ADR-B-0309`, `ADR-B-0311` | NIE |
| ADR-B-02 | ADR-B-02-K11 | Klasa 7: materiały promieniotwórcze (rozpoznawanie) | 2.2.7 | `ADR-B-0098`, `ADR-B-0160`, `ADR-B-0317` | NIE |
| ADR-B-02 | ADR-B-02-K12 | Klasa 8: materiały żrące | 2.2.8 | `ADR-B-0005`, `ADR-B-0161`, `ADR-B-0267` | NIE |
| ADR-B-02 | ADR-B-02-K13 | Klasa 9 i 9A: różne zagrożenia | 2.2.9 | `ADR-B-0099`, `ADR-B-0162`, `ADR-B-0315`, `ADR-B-0499`, `ADR-B-0500`, `ADR-B-0501`, `ADR-B-0502` | NIE |
| ADR-B-02 | ADR-B-02-K14 | Grupy pakowania, zagrożenia dodatkowe, tabela A | 2.1, 3.2 | `ADR-B-0127`, `ADR-B-0128`, `ADR-B-0218` | NIE |
| ADR-B-03 | ADR-B-03-K01 | Rozpoznawanie zagrożenia dla środowiska | 2.2.9.1.10, 5.2.1.8; 5.2.1.8, 5.3.6, 5.4.1.1.18 | `ADR-B-0007`, `ADR-B-0045`, `ADR-B-0276`, `ADR-B-0461`, `ADR-B-0462`, `ADR-B-0463`, `ADR-B-0464`, `ADR-B-0465`, `ADR-B-0466`, `ADR-B-0467`, `ADR-B-0468`, `ADR-B-0469`, `ADR-B-0470` | NIE |
| ADR-B-03 | ADR-B-03-K02 | Odpady niebezpieczne w dokumencie przewozowym | 5.4.1.1.3.1 | `ADR-B-0008`, `ADR-B-0046`, `ADR-B-0294` | NIE |
| ADR-B-03 | ADR-B-03-K03 | Obowiązek oczyszczenia pojazdu po wycieku | 7.5.8.1 | `ADR-B-0009`, `ADR-B-0177`, `ADR-B-0241`, `ADR-B-0514` | NIE |
| ADR-B-03 | ADR-B-03-K04 | Ochrona kanalizacji i wód podczas wypadku | 5.4.3.4 | `ADR-B-0100`, `ADR-B-0163`, `ADR-B-0242` | NIE |
| ADR-B-03 | ADR-B-03-K05 | Unikanie skażenia przy rozlewie | 5.4.3.4 | `ADR-B-0101`, `ADR-B-0178`, `ADR-B-0295` | NIE |
| ADR-B-03 | ADR-B-03-K06 | Szczególne zasady klasyfikowania odpadów | 2.1, 3.3, 5.4.1.1.3 | `ADR-B-0129`, `ADR-B-0179`, `ADR-B-0318`, `ADR-B-0325`, `ADR-B-0326`, `ADR-B-0327`, `ADR-B-0328`, `ADR-B-0329`, `ADR-B-0330`, `ADR-B-0331`, `ADR-B-0332`, `ADR-B-0333`, `ADR-B-0334`, `ADR-B-0335`, `ADR-B-0336`, `ADR-B-0337`, `ADR-B-0338`, `ADR-B-0339`, `ADR-B-0340`, `ADR-B-0341`, `ADR-B-0342`, `ADR-B-0343`, `ADR-B-0344` | NIE |
| ADR-B-04 | ADR-B-04-K01 | Zakaz palenia i używania e-papierosów | 8.3.5 | `ADR-B-0010`, `ADR-B-0103`, `ADR-B-0279`, `ADR-B-0280`, `ADR-B-0360` | NIE |
| ADR-B-04 | ADR-B-04-K02 | Zakaz otwierania przesyłek przez załogę | 8.3.3 | `ADR-B-0011`, `ADR-B-0048`, `ADR-B-0243`, `ADR-B-0357` | NIE |
| ADR-B-04 | ADR-B-04-K03 | Wyłączanie silnika przy załadunku/rozładunku | 8.3.6 | `ADR-B-0012`, `ADR-B-0047`, `ADR-B-0244`, `ADR-B-0358`, `ADR-B-0359`, `ADR-B-0515` | NIE |
| ADR-B-04 | ADR-B-04-K04 | Unikanie źródeł zapłonu przy awarii | 5.4.3.4 | `ADR-B-0102`, `ADR-B-0164`, `ADR-B-0296`, `ADR-B-0353`, `ADR-B-0361` | NIE |
| ADR-B-04 | ADR-B-04-K05 | Zapobieganie kontakcie z niebezpieczną substancją | 5.4.3.4; 8.3.2, 7.5.1.2, 7.5.1.3 | `ADR-B-0130`, `ADR-B-0180`, `ADR-B-0297`, `ADR-B-0354`, `ADR-B-0355`, `ADR-B-0356`, `ADR-B-0362`, `ADR-B-0472`, `ADR-B-0474`, `ADR-B-0475`, `ADR-B-0476` | NIE |
| ADR-B-04 | ADR-B-04-K06 | Bezpieczny postój i nadzorowanie pojazdu | 8.4, 8.5; 8.3.1, 8.3.8 | `ADR-B-0131`, `ADR-B-0181`, `ADR-B-0310`, `ADR-B-0345`, `ADR-B-0346`, `ADR-B-0347`, `ADR-B-0348`, `ADR-B-0349`, `ADR-B-0350`, `ADR-B-0351`, `ADR-B-0352`, `ADR-B-0471`, `ADR-B-0473` | NIE |
| ADR-B-05 | ADR-B-05-K01 | Lokalizacja i znajomość instrukcji pisemnych | 5.4.3 | `ADR-B-0013`, `ADR-B-0014`, `ADR-B-0049`, `ADR-B-0050`, `ADR-B-0516` | NIE |
| ADR-B-05 | ADR-B-05-K02 | Bezpieczne zatrzymanie i wyłączenie silnika | 5.4.3.4 | `ADR-B-0104`, `ADR-B-0182`, `ADR-B-0219` | NIE |
| ADR-B-05 | ADR-B-05-K03 | Powiadomienie służb i informacje o ładunku | 5.4.3.4 | `ADR-B-0105`, `ADR-B-0165`, `ADR-B-0220` | NIE |
| ADR-B-05 | ADR-B-05-K04 | Unikanie oparów i wybór strony nawietrznej | 5.4.3.4 | `ADR-B-0106`, `ADR-B-0183`, `ADR-B-0221`, `ADR-B-0494` | NIE |
| ADR-B-05 | ADR-B-05-K05 | Zakaz gaszenia pożaru ładowni | 5.4.3.4 | `ADR-B-0107`, `ADR-B-0166`, `ADR-B-0222` | NIE |
| ADR-B-05 | ADR-B-05-K06 | Mały pożar opon, hamulców lub silnika | 5.4.3.4 | `ADR-B-0108`, `ADR-B-0184`, `ADR-B-0223`, `ADR-B-0493` | NIE |
| ADR-B-05 | ADR-B-05-K07 | Przekazanie dokumentów ratownikom | 5.4.3.4 | `ADR-B-0109`, `ADR-B-0185`, `ADR-B-0229` | NIE |
| ADR-B-05 | ADR-B-05-K08 | Skażona odzież i środki ochrony | 5.4.3.4 | `ADR-B-0110`, `ADR-B-0167`, `ADR-B-0230` | NIE |
| ADR-B-05 | ADR-B-05-K09 | Ostrzeganie osób postronnych i ewakuacja | 5.4.3.4 | `ADR-B-0111`, `ADR-B-0186`, `ADR-B-0224` | NIE |
| ADR-B-05 | ADR-B-05-K10 | Kamizelka i znaki ostrzegawcze | 5.4.3.4 | `ADR-B-0112`, `ADR-B-0168`, `ADR-B-0231` | NIE |
| ADR-B-05 | ADR-B-05-K11 | Ocena bezpieczeństwa udzielania pierwszej pomocy | 5.4.3.4; program praktyczny | `ADR-B-0113`, `ADR-B-0187`, `ADR-B-0225` | NIE |
| ADR-B-05 | ADR-B-05-K12 | Mocowanie/dostępność gaśnic | 8.1.4.5 | `ADR-B-0015`, `ADR-B-0169`, `ADR-B-0232` | NIE |
| ADR-B-05 | ADR-B-05-K13 | Praktyczne używanie gaśnicy (instruktaż) | program praktyczny, zał. 1 | — | N/D — praktyka |
| ADR-B-05 | ADR-B-05-K14 | Praktyczne czynności pierwszej pomocy (instruktaż) | program praktyczny, zał. 1 | — | N/D — praktyka |
| ADR-B-05 | ADR-B-05-K15 | Praktyczny scenariusz wypadku/awarii | program praktyczny, zał. 1 | — | N/D — praktyka |
| ADR-B-06 | ADR-B-06-K01 | Numer UN na sztuce przesyłki | 5.2.1.1 | `ADR-B-0114`, `ADR-B-0188`, `ADR-B-0281` | NIE |
| ADR-B-06 | ADR-B-06-K02 | Nalepki zagrożeń na opakowaniach | 5.2.2.1.1 | `ADR-B-0115`, `ADR-B-0189`, `ADR-B-0303` | NIE |
| ADR-B-06 | ADR-B-06-K03 | Tablice ADR: numer UN i zagrożenia | 5.3.2.2.2; 5.3.2.3.1 | `ADR-B-0016`, `ADR-B-0190`, `ADR-B-0255`, `ADR-B-0503`, `ADR-B-0504`, `ADR-B-0505`, `ADR-B-0506`, `ADR-B-0507`, `ADR-B-0543`, `ADR-B-0544`, `ADR-B-0545` | NIE |
| ADR-B-06 | ADR-B-06-K04 | Znaczenie litery X | 5.3.2.3.1 | `ADR-B-0017`, `ADR-B-0170`, `ADR-B-0256` | NIE |
| ADR-B-06 | ADR-B-06-K05 | Wymiary i rozmieszczenie tablic | 5.3.2.2.1 | `ADR-B-0018`, `ADR-B-0191`, `ADR-B-0258` | NIE |
| ADR-B-06 | ADR-B-06-K06 | Nasilenie zagrożenia przy powtórzeniu cyfry | 5.3.2.3.1 | `ADR-B-0051`, `ADR-B-0192`, `ADR-B-0217` | NIE |
| ADR-B-06 | ADR-B-06-K07 | Kolor i budowa tablicy | 5.3.2.2.2 | `ADR-B-0052`, `ADR-B-0193`, `ADR-B-0257` | NIE |
| ADR-B-06 | ADR-B-06-K08 | Znaczenie cyfry 8 | 5.3.2.3.1 | `ADR-B-0053`, `ADR-B-0194`, `ADR-B-0298` | NIE |
| ADR-B-06 | ADR-B-06-K09 | Nalepki na pojazdach i kontenerach | 5.3.1 | `ADR-B-0132`, `ADR-B-0133`, `ADR-B-0299`, `ADR-B-0546`, `ADR-B-0547`, `ADR-B-0548`, `ADR-B-0549`, `ADR-B-0550`, `ADR-B-0561`, `ADR-B-0562`, `ADR-B-0563`, `ADR-B-0564`, `ADR-B-0565` | NIE |
| ADR-B-07 | ADR-B-07-K01 | Nadawca: klasyfikacja, dane i dokumenty | 1.4.2.1 | `ADR-B-0021`, `ADR-B-0055`, `ADR-B-0117`, `ADR-B-0365`, `ADR-B-0366`, `ADR-B-0380` | NIE |
| ADR-B-07 | ADR-B-07-K02 | Przewoźnik: instrukcje pisemne i kontrola bezpieczeństwa | 1.4.2.2 | `ADR-B-0019`, `ADR-B-0116`, `ADR-B-0285`, `ADR-B-0363`, `ADR-B-0364`, `ADR-B-0374`, `ADR-B-0375`, `ADR-B-0379` | NIE |
| ADR-B-07 | ADR-B-07-K03 | Załadowca: stan opakowań | 1.4.3.1 | `ADR-B-0020`, `ADR-B-0054`, `ADR-B-0245`, `ADR-B-0373`, `ADR-B-0378`, `ADR-B-0517` | NIE |
| ADR-B-07 | ADR-B-07-K04 | Odbiorca: przyjęcie i dalsze obowiązki | 1.4.2.3 | `ADR-B-0118`, `ADR-B-0195`, `ADR-B-0246`, `ADR-B-0377`, `ADR-B-0477` | NIE |
| ADR-B-07 | ADR-B-07-K05 | Pakujący, napełniający i rozładowca | 1.4.3 | `ADR-B-0134`, `ADR-B-0135`, `ADR-B-0290`, `ADR-B-0367`, `ADR-B-0368`, `ADR-B-0369`, `ADR-B-0370`, `ADR-B-0371`, `ADR-B-0372`, `ADR-B-0478`, `ADR-B-0479`, `ADR-B-0480`, `ADR-B-0481`, `ADR-B-0482` | NIE |
| ADR-B-07 | ADR-B-07-K06 | Kierowca/załoga: obowiązki w drodze | 8.1–8.5 | `ADR-B-0136`, `ADR-B-0196`, `ADR-B-0293`, `ADR-B-0376` | NIE |
| ADR-B-07 | ADR-B-07-K07 | Podstawowe rozróżnienie odpowiedzialności cywilnej za szkodę i za niewykonanie zobowiązania | ADR 8.2.2.3.2(k); Kodeks cywilny art. 415, 471 | `ADR-B-0567`, `ADR-B-0568`, `ADR-B-0569` | NIE |
| ADR-B-08 | ADR-B-08-K01 | Gaśnice pełny reżim i masa jednostki | 8.1.4.1 | `ADR-B-0022`, `ADR-B-0071`, `ADR-B-0072`, `ADR-B-0417`, `ADR-B-0418`, `ADR-B-0419`, `ADR-B-0420` | NIE |
| ADR-B-08 | ADR-B-08-K02 | Gaśnica przy 1.1.3.6 | 8.1.4.2 | `ADR-B-0073`, `ADR-B-0197`, `ADR-B-0282`, `ADR-B-0421` | NIE |
| ADR-B-08 | ADR-B-08-K03 | Stan techniczny, ważność i dostępność gaśnic | 8.1.4.4–5 | `ADR-B-0074`, `ADR-B-0176`, `ADR-B-0283`, `ADR-B-0422`, `ADR-B-0423` | NIE |
| ADR-B-08 | ADR-B-08-K04 | Klin pod koło | 8.1.5.2 | `ADR-B-0023`, `ADR-B-0056`, `ADR-B-0251`, `ADR-B-0509` | NIE |
| ADR-B-08 | ADR-B-08-K05 | Kamizelki i latarki dla członków załogi | 8.1.5.2 | `ADR-B-0057`, `ADR-B-0075`, `ADR-B-0252` | NIE |
| ADR-B-08 | ADR-B-08-K06 | Rękawice i ochrona oczu | 8.1.5.2 | `ADR-B-0024`, `ADR-B-0076`, `ADR-B-0253` | NIE |
| ADR-B-08 | ADR-B-08-K07 | Wyposażenie dodatkowe właściwe dla nalepek | 8.1.5.3 | `ADR-B-0077`, `ADR-B-0171`, `ADR-B-0254`, `ADR-B-0483`, `ADR-B-0484`, `ADR-B-0485`, `ADR-B-0486` | NIE |
| ADR-B-08 | ADR-B-08-K08 | Wyposażenie techniczne i wymagania pojazdu | 9.1, 9.2 | `ADR-B-0137`, `ADR-B-0198`, `ADR-B-0319`, `ADR-B-0551`, `ADR-B-0552`, `ADR-B-0553`, `ADR-B-0566` | NIE |
| ADR-B-09 | ADR-B-09-K01 | Zgodność przy ładowaniu razem | 7.5.2 | `ADR-B-0025`, `ADR-B-0199`, `ADR-B-0291`, `ADR-B-0324`, `ADR-B-0424`, `ADR-B-0425`, `ADR-B-0426`, `ADR-B-0427`, `ADR-B-0428`, `ADR-B-0429`, `ADR-B-0491`, `ADR-B-0492` | NIE |
| ADR-B-09 | ADR-B-09-K02 | Mocowanie sztuk przesyłek | 7.5.7.1 | `ADR-B-0026`, `ADR-B-0079`, `ADR-B-0235` | NIE |
| ADR-B-09 | ADR-B-09-K03 | Kontakt z żywnością i paszami | 7.5.4 | `ADR-B-0027`, `ADR-B-0081`, `ADR-B-0082` | NIE |
| ADR-B-09 | ADR-B-09-K04 | Strzałki kierunkowe | 7.5.1.5 | `ADR-B-0058`, `ADR-B-0172`, `ADR-B-0286` | NIE |
| ADR-B-09 | ADR-B-09-K05 | Piętrzenie opakowań | 7.5.7.2 | `ADR-B-0059`, `ADR-B-0078`, `ADR-B-0237` | NIE |
| ADR-B-09 | ADR-B-09-K06 | Unikanie nadmiernego naprężenia pasów | 7.5.7.1 | `ADR-B-0060`, `ADR-B-0200`, `ADR-B-0236`, `ADR-B-0518` | NIE |
| ADR-B-09 | ADR-B-09-K07 | Czyszczenie pojazdu po rozładunku, także po wycieku | 7.5.8.1–7.5.8.2 | `ADR-B-0080`, `ADR-B-0201`, `ADR-B-0238`, `ADR-B-0240` | NIE |
| ADR-B-09 | ADR-B-09-K08 | Wstępna kontrola przed załadunkiem | 7.5.1 | `ADR-B-0138`, `ADR-B-0202`, `ADR-B-0239`, `ADR-B-0436`, `ADR-B-0554`, `ADR-B-0555`, `ADR-B-0560` | NIE |
| ADR-B-09 | ADR-B-09-K09 | Towary luzem: ogólne zasady podstawowe | 7.3 | `ADR-B-0139`, `ADR-B-0173`, `ADR-B-0292`, `ADR-B-0556`, `ADR-B-0557`, `ADR-B-0558`, `ADR-B-0559` | NIE |
| ADR-B-10 | ADR-B-10-K01 | Zasady uznawania IMDG przy odcinku drogowym | 1.1.4.2 | `ADR-B-0028`, `ADR-B-0029`, `ADR-B-0030`, `ADR-B-0062`, `ADR-B-0119`, `ADR-B-0247`, `ADR-B-0381`, `ADR-B-0382`, `ADR-B-0383`, `ADR-B-0397`, `ADR-B-0511` | NIE |
| ADR-B-10 | ADR-B-10-K02 | Dodatkowy wpis w dokumencie przy 1.1.4.2.1 | 5.4.1.1.7 | `ADR-B-0061`, `ADR-B-0203`, `ADR-B-0277`, `ADR-B-0395` | NIE |
| ADR-B-10 | ADR-B-10-K03 | Dokumentacja i certyfikat pakowania kontenera | 5.4.2 | `ADR-B-0140`, `ADR-B-0204`, `ADR-B-0278`, `ADR-B-0388`, `ADR-B-0390`, `ADR-B-0391`, `ADR-B-0392`, `ADR-B-0393`, `ADR-B-0394`, `ADR-B-0398` | NIE |
| ADR-B-10 | ADR-B-10-K04 | Różnice między wymaganiami ADR, RID i IMDG | 1.1.4 | `ADR-B-0141`, `ADR-B-0205`, `ADR-B-0320`, `ADR-B-0387`, `ADR-B-0437`, `ADR-B-0438`, `ADR-B-0439`, `ADR-B-0440`, `ADR-B-0441`, `ADR-B-0442`, `ADR-B-0443` | NIE |
| ADR-B-10 | ADR-B-10-K05 | Warunki zwolnień oraz obowiązki drogowego odcinka | 1.1.4.2; 1.1.4.7, 5.4.1.1.24 | `ADR-B-0142`, `ADR-B-0206`, `ADR-B-0321`, `ADR-B-0384`, `ADR-B-0385`, `ADR-B-0386`, `ADR-B-0389`, `ADR-B-0396`, `ADR-B-0444`, `ADR-B-0445`, `ADR-B-0446`, `ADR-B-0447`, `ADR-B-0448`, `ADR-B-0449`, `ADR-B-0450`, `ADR-B-0451`, `ADR-B-0452`, `ADR-B-0453`, `ADR-B-0454` | NIE |
| ADR-B-11 | ADR-B-11-K01 | Kategorie tuneli A–E | 1.9.5.3 | `ADR-B-0031`, `ADR-B-0207`, `ADR-B-0262`, `ADR-B-0430`, `ADR-B-0433`, `ADR-B-0490` | NIE |
| ADR-B-11 | ADR-B-11-K02 | Kod E, D/E i rodzaj przewozu | 8.6.4 | `ADR-B-0032`, `ADR-B-0033`, `ADR-B-0083`, `ADR-B-0084`, `ADR-B-0487`, `ADR-B-0488`, `ADR-B-0489` | NIE |
| ADR-B-11 | ADR-B-11-K03 | Kod w kolumnie 15 tabeli A | 8.6.3.1 | `ADR-B-0063`, `ADR-B-0208`, `ADR-B-0248`, `ADR-B-0434`, `ADR-B-0539` | NIE |
| ADR-B-11 | ADR-B-11-K04 | Najbardziej restrykcyjny kod w jednostce | 8.6.3.2 | `ADR-B-0064`, `ADR-B-0086`, `ADR-B-0263`, `ADR-B-0432` | NIE |
| ADR-B-11 | ADR-B-11-K05 | Rozumienie znaczenia kodu tunelowego (-) i jego ograniczeń | 8.6.3.1 | `ADR-B-0065`, `ADR-B-0174`, `ADR-B-0264`, `ADR-B-0431`, `ADR-B-0540` | NIE |
| ADR-B-11 | ADR-B-11-K06 | Wyłączenia 1.1.3 i przypadek 3.4.13 | 8.6.3.3 | `ADR-B-0085`, `ADR-B-0209`, `ADR-B-0322`, `ADR-B-0512` | NIE |
| ADR-B-11 | ADR-B-11-K07 | Zachowanie podczas pożaru w tunelu | program kursu lit. k, 5.4.3.4 | `ADR-B-0143`, `ADR-B-0210`, `ADR-B-0308`, `ADR-B-0435` | NIE |
| ADR-B-12 | ADR-B-12-K01 | Dokument tożsamości ze zdjęciem | 1.10.1.4 | `ADR-B-0034`, `ADR-B-0067`, `ADR-B-0300`, `ADR-B-0416`, `ADR-B-0519` | NIE |
| ADR-B-12 | ADR-B-12-K02 | Zabezpieczenie placów i składowania | 1.10.1.3 | `ADR-B-0035`, `ADR-B-0066`, `ADR-B-0274`, `ADR-B-0415` | NIE |
| ADR-B-12 | ADR-B-12-K03 | Szkolenie z ochrony i przeciwdziałania zagrożeniom | 1.10.2 | `ADR-B-0036`, `ADR-B-0121`, `ADR-B-0275`, `ADR-B-0409`, `ADR-B-0410`, `ADR-B-0411`, `ADR-B-0412` | NIE |
| ADR-B-12 | ADR-B-12-K04 | Weryfikacja tożsamości przewoźnika | 1.10.1.2 | `ADR-B-0120`, `ADR-B-0211`, `ADR-B-0249`, `ADR-B-0413`, `ADR-B-0414` | NIE |
| ADR-B-12 | ADR-B-12-K05 | Plan ochrony towarów dużego ryzyka | 1.10.3.2; 1.10.3.1.2 | `ADR-B-0122`, `ADR-B-0212`, `ADR-B-0304`, `ADR-B-0399`, `ADR-B-0400`, `ADR-B-0401`, `ADR-B-0402`, `ADR-B-0403`, `ADR-B-0404`, `ADR-B-0405`, `ADR-B-0406`, `ADR-B-0455`, `ADR-B-0456`, `ADR-B-0457`, `ADR-B-0458`, `ADR-B-0459`, `ADR-B-0460` | NIE |
| ADR-B-12 | ADR-B-12-K06 | Zabezpieczenie postoju i przed kradzieżą pojazdu | 1.10.3.3, 8.4 | `ADR-B-0144`, `ADR-B-0213`, `ADR-B-0305`, `ADR-B-0407`, `ADR-B-0408` | NIE |
| ADR-B-13 | ADR-B-13-K01 | Numer UN i właściwa nazwa przewozowa | 5.4.1.1.1(a),(b) | `ADR-B-0037`, `ADR-B-0038`, `ADR-B-0226`, `ADR-B-0508`, `ADR-B-0523`, `ADR-B-0536` | NIE |
| ADR-B-13 | ADR-B-13-K02 | Dokument: liczba, rodzaj przesyłek i ilość | 5.4.1.1.1(e),(f) | `ADR-B-0069`, `ADR-B-0070`, `ADR-B-0227`, `ADR-B-0537` | NIE |
| ADR-B-13 | ADR-B-13-K03 | Dane odbiorcy i nadawcy | 5.4.1.1.1(g),(h) | `ADR-B-0068`, `ADR-B-0214`, `ADR-B-0233` | NIE |
| ADR-B-13 | ADR-B-13-K04 | Wzór i liczba stron instrukcji pisemnych | 5.4.3.4 | `ADR-B-0039`, `ADR-B-0088`, `ADR-B-0234` | NIE |
| ADR-B-13 | ADR-B-13-K05 | Dokumenty i dowód tożsamości załogi | 8.1.2.1 | `ADR-B-0087`, `ADR-B-0175`, `ADR-B-0250` | NIE |
| ADR-B-13 | ADR-B-13-K06 | Dodatkowy wpis w transporcie kombinowanym | 5.4.1.1.7 | `ADR-B-0089`, `ADR-B-0215`, `ADR-B-0287` | NIE |
| ADR-B-13 | ADR-B-13-K07 | Dostępność dokumentów w kabinie | 8.1.2.3 | `ADR-B-0090`, `ADR-B-0216`, `ADR-B-0228` | NIE |
| ADR-B-13 | ADR-B-13-K08 | Dodatkowe dokumenty zależnie od rodzaju ładunku | 8.1.2, 5.4 | `ADR-B-0145`, `ADR-B-0146`, `ADR-B-0306`, `ADR-B-0524`, `ADR-B-0525`, `ADR-B-0530`, `ADR-B-0531`, `ADR-B-0532`, `ADR-B-0533`, `ADR-B-0538` | NIE |

## Dalsze działania po audycie

1. Kontrola redakcyjna lekcji B-01, B-11 i B-13: porównać wyjaśnienia z ID i dodać **tylko potwierdzone** objaśnienia pojęć i przykłady; nie zmieniać prawnych warunków bez źródła.
2. Praktyka: sprawdzić P1–P3 z wymaganiami programu; ich zaliczenie należy do rzeczywistego instruktora.
3. Przy nowej potwierdzonej luce tworzyć pytania od wolnego ID 0570, po 10–15 z oceną A/B/C, wymaganą długością explanation i testem wskaźników działowych 38%/38%/18%; każdą partię scalać wyłącznie po PASS.
4. Udokumentować powiązania odsyłaczy lekcja → pytania i regenerować próbne arkusze dopiero po zmianie banku; brak zmian banku nie uzasadnia nowych wariantów egzaminu.

**Ograniczenia:** jest to audyt kompletności mapowania celów, a nie niezależna kontrola dosłownego brzmienia całego ADR 2025 ani dowód, że nawet liczne pytania wyczerpują każdy wyjątek prawny. Zero zmian kluczy i `verification_status`.
