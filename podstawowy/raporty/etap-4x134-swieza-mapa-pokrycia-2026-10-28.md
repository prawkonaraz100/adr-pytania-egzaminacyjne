# Etap 4x134 — świeża mapa pokrycia kursu podstawowego ADR

**Data:** 28.10.2026. **Bazowy main:** `6fe44b3589f1408f05e6fe0dc45e689daca6c3a6` (po scaleniu PR #596). **Zakres:** tylko kurs podstawowy; nie cysterny.

## Metoda i wynik

Zestawiono każde z 609 pytań i jego przypisania do `podstawowy/kompetencje.json` z poprzednią mapą pokrycia ([PR #294](https://github.com/prawkonaraz100/adr-pytania-egzaminacyjne/pull/294), [raport 4t](etap-4t-pokrycie-programu-2026-10-25.md)), polskim programem z załącznika nr 1 do Dz.U. 2021 poz. 2150 i tematami ADR 8.2.2.3.2. Wewnętrzne 107 kompetencji nie jest odrębnym urzędowym programem.

- **609 unikalnych pytań, 609 `needs_review`, zero `verified`.**
- **104/104 kompetencji teoretycznych** mają co najmniej **3** przypisane pytania; minimum w kompetencji = 3. **0 kompetencji teoretycznych bez pytań lub z jednym pytaniem**.
- Pozostałe **3 kompetencje są praktyczne** (użycie gaśnicy, pierwsza pomoc, postępowanie po wypadku): mają 0 przypisanych pytań celowo, ponieważ ich zaliczenie wymaga rzeczywistych ćwiczeń, nie quizu.
- **39 scenariuszy**, po 3 na każdy z 13 działów; to materiały do ćwiczeń, nie poświadczenie praktyki.
- **0 odwołań do nieistniejących ID**, **0 przypisań pytań do kompetencji w innym dziale**, **0 pytań bez przypisania w mapie**.
- Kontrola ilościowa nie potwierdza niezależności semantycznej trzech pytań ani ich poprawności prawnej. Dlatego sam próg liczbowy nie jest wystarczającym warunkiem publikacji.

## Zestawienie wszystkich 13 działów

| Dział | Pytania | Kompetencje teoretyczne | Z min. 3 pytaniami | Kompetencje praktyczne | Scenariusze |
|---|---:|---:|---:|---:|---:|
| ADR-B-01 | 45 | 7 | 7 | 0 | 3 |
| ADR-B-02 | 56 | 14 | 14 | 0 | 3 |
| ADR-B-03 | 49 | 6 | 6 | 0 | 3 |
| ADR-B-04 | 46 | 6 | 6 | 0 | 3 |
| ADR-B-05 | 43 | 12 | 12 | 3 | 3 |
| ADR-B-06 | 45 | 9 | 9 | 0 | 3 |
| ADR-B-07 | 48 | 7 | 7 | 0 | 3 |
| ADR-B-08 | 42 | 8 | 8 | 0 | 3 |
| ADR-B-09 | 46 | 9 | 9 | 0 | 3 |
| ADR-B-10 | 55 | 5 | 5 | 0 | 3 |
| ADR-B-11 | 43 | 7 | 7 | 0 | 3 |
| ADR-B-12 | 44 | 6 | 6 | 0 | 3 |
| ADR-B-13 | 47 | 8 | 8 | 0 | 3 |
| **Razem** | **609** | **104** | **104** | **3** | **39** |

## Macierz wszystkich kompetencji i identyfikatorów pytań

| ID celu | Cel | Typ | Liczba pytań | Przypisane ID | Referencje do kontroli |
|---|---|---|---:|---|---|
| ADR-B-01-K01 | Ramy prawne i definicje ADR | teoria | 3 | ADR-B-0123, ADR-B-0147, ADR-B-0312 | 1.1, 1.2 |
| ADR-B-01-K02 | Szkolenie osób uczestniczących w przewozie | teoria | 9 | ADR-B-0001, ADR-B-0040, ADR-B-0041, ADR-B-0092, ADR-B-0513, ADR-B-0520, ADR-B-0521, ADR-B-0522, ADR-B-0529 | 1.3 |
| ADR-B-01-K03 | Kiedy kierowca potrzebuje zaświadczenia ADR | teoria | 4 | ADR-B-0003, ADR-B-0148, ADR-B-0301, ADR-B-0607 | 8.2.1 |
| ADR-B-01-K04 | Wyłączenia ze względu na charakter przewozu | teoria | 4 | ADR-B-0002, ADR-B-0091, ADR-B-0313, ADR-B-0595 | 1.1.3.1 |
| ADR-B-01-K05 | Ilości ograniczone LQ i wyłączone EQ | teoria | 14 | ADR-B-0093, ADR-B-0149, ADR-B-0260, ADR-B-0261, ADR-B-0273, ADR-B-0526, ADR-B-0527, ADR-B-0528, ADR-B-0534, ADR-B-0535, ADR-B-0572, ADR-B-0573, ADR-B-0605, ADR-B-0609 | 3.4, 3.5 |
| ADR-B-01-K06 | Progi i kategorie transportowe 1.1.3.6 | teoria | 9 | ADR-B-0002, ADR-B-0093, ADR-B-0259, ADR-B-0271, ADR-B-0272, ADR-B-0323, ADR-B-0570, ADR-B-0571, ADR-B-0606 | 1.1.3.6 |
| ADR-B-01-K07 | Towary zabronione i dopuszczone do przewozu | teoria | 4 | ADR-B-0124, ADR-B-0125, ADR-B-0314, ADR-B-0608 | 2.1, 3.2, 3.3 |
| ADR-B-02-K01 | Klasa 1: materiały i przedmioty wybuchowe (rozpoznawanie) | teoria | 7 | ADR-B-0126, ADR-B-0150, ADR-B-0316, ADR-B-0495, ADR-B-0496, ADR-B-0497, ADR-B-0498 | 2.2.1 |
| ADR-B-02-K02 | Klasa 2: gazy | teoria | 4 | ADR-B-0042, ADR-B-0151, ADR-B-0284, ADR-B-0541 | 2.2.2 |
| ADR-B-02-K03 | Klasa 3: materiały ciekłe zapalne | teoria | 4 | ADR-B-0004, ADR-B-0152, ADR-B-0288, ADR-B-0542 | 2.2.3 |
| ADR-B-02-K04 | Klasa 4.1: materiały stałe zapalne | teoria | 3 | ADR-B-0094, ADR-B-0153, ADR-B-0268 | 2.2.41 |
| ADR-B-02-K05 | Klasa 4.2: materiały samonagrzewające się / samozapalne | teoria | 3 | ADR-B-0095, ADR-B-0154, ADR-B-0302 | 2.2.42 |
| ADR-B-02-K06 | Klasa 4.3: reagujące z wodą | teoria | 5 | ADR-B-0006, ADR-B-0155, ADR-B-0265, ADR-B-0269, ADR-B-0510 | 2.2.43 |
| ADR-B-02-K07 | Klasa 5.1: materiały utleniające | teoria | 4 | ADR-B-0044, ADR-B-0156, ADR-B-0266, ADR-B-0270 | 2.2.51 |
| ADR-B-02-K08 | Klasa 5.2: nadtlenki organiczne | teoria | 3 | ADR-B-0096, ADR-B-0157, ADR-B-0307 | 2.2.52 |
| ADR-B-02-K09 | Klasa 6.1: materiały trujące | teoria | 3 | ADR-B-0097, ADR-B-0158, ADR-B-0289 | 2.2.61 |
| ADR-B-02-K10 | Klasa 6.2: materiały zakaźne | teoria | 4 | ADR-B-0043, ADR-B-0159, ADR-B-0309, ADR-B-0311 | 2.2.62 |
| ADR-B-02-K11 | Klasa 7: materiały promieniotwórcze (rozpoznawanie) | teoria | 3 | ADR-B-0098, ADR-B-0160, ADR-B-0317 | 2.2.7 |
| ADR-B-02-K12 | Klasa 8: materiały żrące | teoria | 3 | ADR-B-0005, ADR-B-0161, ADR-B-0267 | 2.2.8 |
| ADR-B-02-K13 | Klasa 9 i 9A: różne zagrożenia | teoria | 7 | ADR-B-0099, ADR-B-0162, ADR-B-0315, ADR-B-0499, ADR-B-0500, ADR-B-0501, ADR-B-0502 | 2.2.9 |
| ADR-B-02-K14 | Grupy pakowania, zagrożenia dodatkowe, tabela A | teoria | 3 | ADR-B-0127, ADR-B-0128, ADR-B-0218 | 2.1, 3.2 |
| ADR-B-03-K01 | Rozpoznawanie zagrożenia dla środowiska | teoria | 13 | ADR-B-0007, ADR-B-0045, ADR-B-0276, ADR-B-0461, ADR-B-0462, ADR-B-0463, ADR-B-0464, ADR-B-0465, ADR-B-0466, ADR-B-0467, ADR-B-0468, ADR-B-0469, ADR-B-0470 | 2.2.9.1.10, 5.2.1.8; 5.2.1.8, 5.3.6, 5.4.1.1.18 |
| ADR-B-03-K02 | Odpady niebezpieczne w dokumencie przewozowym | teoria | 3 | ADR-B-0008, ADR-B-0046, ADR-B-0294 | 5.4.1.1.3.1 |
| ADR-B-03-K03 | Obowiązek oczyszczenia pojazdu po wycieku | teoria | 4 | ADR-B-0009, ADR-B-0177, ADR-B-0241, ADR-B-0514 | 7.5.8.1 |
| ADR-B-03-K04 | Ochrona kanalizacji i wód podczas wypadku | teoria | 3 | ADR-B-0100, ADR-B-0163, ADR-B-0242 | 5.4.3.4 |
| ADR-B-03-K05 | Unikanie skażenia przy rozlewie | teoria | 3 | ADR-B-0101, ADR-B-0178, ADR-B-0295 | 5.4.3.4 |
| ADR-B-03-K06 | Szczególne zasady klasyfikowania odpadów | teoria | 23 | ADR-B-0129, ADR-B-0179, ADR-B-0318, ADR-B-0325, ADR-B-0326, ADR-B-0327, ADR-B-0328, ADR-B-0329, ADR-B-0330, ADR-B-0331, ADR-B-0332, ADR-B-0333, ADR-B-0334, ADR-B-0335, ADR-B-0336, ADR-B-0337, ADR-B-0338, ADR-B-0339, ADR-B-0340, ADR-B-0341, ADR-B-0342, ADR-B-0343, ADR-B-0344 | 2.1, 3.3, 5.4.1.1.3 |
| ADR-B-04-K01 | Zakaz palenia i używania e-papierosów | teoria | 5 | ADR-B-0010, ADR-B-0103, ADR-B-0279, ADR-B-0280, ADR-B-0360 | 8.3.5 |
| ADR-B-04-K02 | Zakaz otwierania przesyłek przez załogę | teoria | 4 | ADR-B-0011, ADR-B-0048, ADR-B-0243, ADR-B-0357 | 8.3.3 |
| ADR-B-04-K03 | Wyłączanie silnika przy załadunku/rozładunku | teoria | 6 | ADR-B-0012, ADR-B-0047, ADR-B-0244, ADR-B-0358, ADR-B-0359, ADR-B-0515 | 8.3.6 |
| ADR-B-04-K04 | Unikanie źródeł zapłonu przy awarii | teoria | 5 | ADR-B-0102, ADR-B-0164, ADR-B-0296, ADR-B-0353, ADR-B-0361 | 5.4.3.4 |
| ADR-B-04-K05 | Zapobieganie kontakcie z niebezpieczną substancją | teoria | 11 | ADR-B-0130, ADR-B-0180, ADR-B-0297, ADR-B-0354, ADR-B-0355, ADR-B-0356, ADR-B-0362, ADR-B-0472, ADR-B-0474, ADR-B-0475, ADR-B-0476 | 5.4.3.4; 8.3.2, 7.5.1.2, 7.5.1.3 |
| ADR-B-04-K06 | Bezpieczny postój i nadzorowanie pojazdu | teoria | 15 | ADR-B-0131, ADR-B-0181, ADR-B-0310, ADR-B-0345, ADR-B-0346, ADR-B-0347, ADR-B-0348, ADR-B-0349, ADR-B-0350, ADR-B-0351, ADR-B-0352, ADR-B-0471, ADR-B-0473, ADR-B-0580, ADR-B-0581 | 8.4, 8.5; 8.3.1, 8.3.8 |
| ADR-B-05-K01 | Lokalizacja i znajomość instrukcji pisemnych | teoria | 5 | ADR-B-0013, ADR-B-0014, ADR-B-0049, ADR-B-0050, ADR-B-0516 | 5.4.3 |
| ADR-B-05-K02 | Bezpieczne zatrzymanie i wyłączenie silnika | teoria | 4 | ADR-B-0104, ADR-B-0182, ADR-B-0219, ADR-B-0593 | 5.4.3.4 |
| ADR-B-05-K03 | Powiadomienie służb i informacje o ładunku | teoria | 4 | ADR-B-0105, ADR-B-0165, ADR-B-0220, ADR-B-0594 | 5.4.3.4 |
| ADR-B-05-K04 | Unikanie oparów i wybór strony nawietrznej | teoria | 4 | ADR-B-0106, ADR-B-0183, ADR-B-0221, ADR-B-0494 | 5.4.3.4 |
| ADR-B-05-K05 | Zakaz gaszenia pożaru ładowni | teoria | 3 | ADR-B-0107, ADR-B-0166, ADR-B-0222 | 5.4.3.4 |
| ADR-B-05-K06 | Mały pożar opon, hamulców lub silnika | teoria | 4 | ADR-B-0108, ADR-B-0184, ADR-B-0223, ADR-B-0493 | 5.4.3.4 |
| ADR-B-05-K07 | Przekazanie dokumentów ratownikom | teoria | 3 | ADR-B-0109, ADR-B-0185, ADR-B-0229 | 5.4.3.4 |
| ADR-B-05-K08 | Skażona odzież i środki ochrony | teoria | 3 | ADR-B-0110, ADR-B-0167, ADR-B-0230 | 5.4.3.4 |
| ADR-B-05-K09 | Ostrzeganie osób postronnych i ewakuacja | teoria | 3 | ADR-B-0111, ADR-B-0186, ADR-B-0224 | 5.4.3.4 |
| ADR-B-05-K10 | Kamizelka i znaki ostrzegawcze | teoria | 3 | ADR-B-0112, ADR-B-0168, ADR-B-0231 | 5.4.3.4 |
| ADR-B-05-K11 | Ocena bezpieczeństwa udzielania pierwszej pomocy | teoria | 3 | ADR-B-0113, ADR-B-0187, ADR-B-0225 | 5.4.3.4; program praktyczny |
| ADR-B-05-K12 | Mocowanie/dostępność gaśnic | teoria | 4 | ADR-B-0015, ADR-B-0169, ADR-B-0232, ADR-B-0585 | 8.1.4.5 |
| ADR-B-05-K13 | Praktyczne używanie gaśnicy (instruktaż) | praktyka | 0 | — (zajęcia praktyczne) | program praktyczny, zał. 1 |
| ADR-B-05-K14 | Praktyczne czynności pierwszej pomocy (instruktaż) | praktyka | 0 | — (zajęcia praktyczne) | program praktyczny, zał. 1 |
| ADR-B-05-K15 | Praktyczny scenariusz wypadku/awarii | praktyka | 0 | — (zajęcia praktyczne) | program praktyczny, zał. 1 |
| ADR-B-06-K01 | Numer UN na sztuce przesyłki | teoria | 3 | ADR-B-0114, ADR-B-0188, ADR-B-0281 | 5.2.1.1 |
| ADR-B-06-K02 | Nalepki zagrożeń na opakowaniach | teoria | 3 | ADR-B-0115, ADR-B-0189, ADR-B-0303 | 5.2.2.1.1 |
| ADR-B-06-K03 | Tablice ADR: numer UN i zagrożenia | teoria | 11 | ADR-B-0016, ADR-B-0190, ADR-B-0255, ADR-B-0503, ADR-B-0504, ADR-B-0505, ADR-B-0506, ADR-B-0507, ADR-B-0543, ADR-B-0544, ADR-B-0545 | 5.3.2.2.2; 5.3.2.3.1 |
| ADR-B-06-K04 | Znaczenie litery X | teoria | 3 | ADR-B-0017, ADR-B-0170, ADR-B-0256 | 5.3.2.3.1 |
| ADR-B-06-K05 | Wymiary i rozmieszczenie tablic | teoria | 3 | ADR-B-0018, ADR-B-0191, ADR-B-0258 | 5.3.2.2.1 |
| ADR-B-06-K06 | Nasilenie zagrożenia przy powtórzeniu cyfry | teoria | 3 | ADR-B-0051, ADR-B-0192, ADR-B-0217 | 5.3.2.3.1 |
| ADR-B-06-K07 | Kolor i budowa tablicy | teoria | 3 | ADR-B-0052, ADR-B-0193, ADR-B-0257 | 5.3.2.2.2 |
| ADR-B-06-K08 | Znaczenie cyfry 8 | teoria | 3 | ADR-B-0053, ADR-B-0194, ADR-B-0298 | 5.3.2.3.1 |
| ADR-B-06-K09 | Nalepki na pojazdach i kontenerach | teoria | 13 | ADR-B-0132, ADR-B-0133, ADR-B-0299, ADR-B-0546, ADR-B-0547, ADR-B-0548, ADR-B-0549, ADR-B-0550, ADR-B-0561, ADR-B-0562, ADR-B-0563, ADR-B-0564, ADR-B-0565 | 5.3.1 |
| ADR-B-07-K01 | Nadawca: klasyfikacja, dane i dokumenty | teoria | 6 | ADR-B-0021, ADR-B-0055, ADR-B-0117, ADR-B-0365, ADR-B-0366, ADR-B-0380 | 1.4.2.1 |
| ADR-B-07-K02 | Przewoźnik: instrukcje pisemne i kontrola bezpieczeństwa | teoria | 8 | ADR-B-0019, ADR-B-0116, ADR-B-0285, ADR-B-0363, ADR-B-0364, ADR-B-0374, ADR-B-0375, ADR-B-0379 | 1.4.2.2 |
| ADR-B-07-K03 | Załadowca: stan opakowań | teoria | 6 | ADR-B-0020, ADR-B-0054, ADR-B-0245, ADR-B-0373, ADR-B-0378, ADR-B-0517 | 1.4.3.1 |
| ADR-B-07-K04 | Odbiorca: przyjęcie i dalsze obowiązki | teoria | 5 | ADR-B-0118, ADR-B-0195, ADR-B-0246, ADR-B-0377, ADR-B-0477 | 1.4.2.3 |
| ADR-B-07-K05 | Pakujący, napełniający i rozładowca | teoria | 16 | ADR-B-0134, ADR-B-0135, ADR-B-0290, ADR-B-0367, ADR-B-0368, ADR-B-0369, ADR-B-0370, ADR-B-0371, ADR-B-0372, ADR-B-0478, ADR-B-0479, ADR-B-0480, ADR-B-0481, ADR-B-0482, ADR-B-0583, ADR-B-0584 | 1.4.3 |
| ADR-B-07-K06 | Kierowca/załoga: obowiązki w drodze | teoria | 4 | ADR-B-0136, ADR-B-0196, ADR-B-0293, ADR-B-0376 | 8.1–8.5 |
| ADR-B-07-K07 | Podstawowe rozróżnienie odpowiedzialności cywilnej za szkodę i za niewykonanie zobowiązania | teoria | 3 | ADR-B-0567, ADR-B-0568, ADR-B-0569 | ADR 8.2.2.3.2(k); Kodeks cywilny art. 415, 471 |
| ADR-B-08-K01 | Gaśnice pełny reżim i masa jednostki | teoria | 7 | ADR-B-0022, ADR-B-0071, ADR-B-0072, ADR-B-0417, ADR-B-0418, ADR-B-0419, ADR-B-0420 | 8.1.4.1 |
| ADR-B-08-K02 | Gaśnica przy 1.1.3.6 | teoria | 4 | ADR-B-0073, ADR-B-0197, ADR-B-0282, ADR-B-0421 | 8.1.4.2 |
| ADR-B-08-K03 | Stan techniczny, ważność i dostępność gaśnic | teoria | 5 | ADR-B-0074, ADR-B-0176, ADR-B-0283, ADR-B-0422, ADR-B-0423 | 8.1.4.4–5 |
| ADR-B-08-K04 | Klin pod koło | teoria | 4 | ADR-B-0023, ADR-B-0056, ADR-B-0251, ADR-B-0509 | 8.1.5.2 |
| ADR-B-08-K05 | Kamizelki i latarki dla członków załogi | teoria | 4 | ADR-B-0057, ADR-B-0075, ADR-B-0252, ADR-B-0596 | 8.1.5.2 |
| ADR-B-08-K06 | Rękawice i ochrona oczu | teoria | 4 | ADR-B-0024, ADR-B-0076, ADR-B-0253, ADR-B-0597 | 8.1.5.2 |
| ADR-B-08-K07 | Wyposażenie dodatkowe właściwe dla nalepek | teoria | 7 | ADR-B-0077, ADR-B-0171, ADR-B-0254, ADR-B-0483, ADR-B-0484, ADR-B-0485, ADR-B-0486 | 8.1.5.3 |
| ADR-B-08-K08 | Wyposażenie techniczne i wymagania pojazdu | teoria | 7 | ADR-B-0137, ADR-B-0198, ADR-B-0319, ADR-B-0551, ADR-B-0552, ADR-B-0553, ADR-B-0566 | 9.1, 9.2 |
| ADR-B-09-K01 | Zgodność przy ładowaniu razem | teoria | 12 | ADR-B-0025, ADR-B-0199, ADR-B-0291, ADR-B-0324, ADR-B-0424, ADR-B-0425, ADR-B-0426, ADR-B-0427, ADR-B-0428, ADR-B-0429, ADR-B-0491, ADR-B-0492 | 7.5.2 |
| ADR-B-09-K02 | Mocowanie sztuk przesyłek | teoria | 3 | ADR-B-0026, ADR-B-0079, ADR-B-0235 | 7.5.7.1 |
| ADR-B-09-K03 | Kontakt z żywnością i paszami | teoria | 3 | ADR-B-0027, ADR-B-0081, ADR-B-0082 | 7.5.4 |
| ADR-B-09-K04 | Strzałki kierunkowe | teoria | 3 | ADR-B-0058, ADR-B-0172, ADR-B-0286 | 7.5.1.5 |
| ADR-B-09-K05 | Piętrzenie opakowań | teoria | 3 | ADR-B-0059, ADR-B-0078, ADR-B-0237 | 7.5.7.2 |
| ADR-B-09-K06 | Unikanie nadmiernego naprężenia pasów | teoria | 4 | ADR-B-0060, ADR-B-0200, ADR-B-0236, ADR-B-0518 | 7.5.7.1 |
| ADR-B-09-K07 | Czyszczenie pojazdu po rozładunku, także po wycieku | teoria | 4 | ADR-B-0080, ADR-B-0201, ADR-B-0238, ADR-B-0240 | 7.5.8.1–7.5.8.2 |
| ADR-B-09-K08 | Wstępna kontrola przed załadunkiem | teoria | 7 | ADR-B-0138, ADR-B-0202, ADR-B-0239, ADR-B-0436, ADR-B-0554, ADR-B-0555, ADR-B-0560 | 7.5.1 |
| ADR-B-09-K09 | Towary luzem: ogólne zasady podstawowe | teoria | 7 | ADR-B-0139, ADR-B-0173, ADR-B-0292, ADR-B-0556, ADR-B-0557, ADR-B-0558, ADR-B-0559 | 7.3 |
| ADR-B-10-K01 | Zasady uznawania IMDG przy odcinku drogowym | teoria | 11 | ADR-B-0028, ADR-B-0029, ADR-B-0030, ADR-B-0062, ADR-B-0119, ADR-B-0247, ADR-B-0381, ADR-B-0382, ADR-B-0383, ADR-B-0397, ADR-B-0511 | 1.1.4.2 |
| ADR-B-10-K02 | Dodatkowy wpis w dokumencie przy 1.1.4.2.1 | teoria | 4 | ADR-B-0061, ADR-B-0203, ADR-B-0277, ADR-B-0395 | 5.4.1.1.7 |
| ADR-B-10-K03 | Dokumentacja i certyfikat pakowania kontenera | teoria | 10 | ADR-B-0140, ADR-B-0204, ADR-B-0278, ADR-B-0388, ADR-B-0390, ADR-B-0391, ADR-B-0392, ADR-B-0393, ADR-B-0394, ADR-B-0398 | 5.4.2 |
| ADR-B-10-K04 | Różnice między wymaganiami ADR, RID i IMDG | teoria | 11 | ADR-B-0141, ADR-B-0205, ADR-B-0320, ADR-B-0387, ADR-B-0437, ADR-B-0438, ADR-B-0439, ADR-B-0440, ADR-B-0441, ADR-B-0442, ADR-B-0443 | 1.1.4 |
| ADR-B-10-K05 | Warunki zwolnień oraz obowiązki drogowego odcinka | teoria | 19 | ADR-B-0142, ADR-B-0206, ADR-B-0321, ADR-B-0384, ADR-B-0385, ADR-B-0386, ADR-B-0389, ADR-B-0396, ADR-B-0444, ADR-B-0445, ADR-B-0446, ADR-B-0447, ADR-B-0448, ADR-B-0449, ADR-B-0450, ADR-B-0451, ADR-B-0452, ADR-B-0453, ADR-B-0454 | 1.1.4.2; 1.1.4.7, 5.4.1.1.24 |
| ADR-B-11-K01 | Kategorie tuneli A–E | teoria | 7 | ADR-B-0031, ADR-B-0207, ADR-B-0262, ADR-B-0430, ADR-B-0433, ADR-B-0490, ADR-B-0602 | 1.9.5.3 |
| ADR-B-11-K02 | Kod E, D/E i rodzaj przewozu | teoria | 9 | ADR-B-0032, ADR-B-0033, ADR-B-0083, ADR-B-0084, ADR-B-0487, ADR-B-0488, ADR-B-0489, ADR-B-0576, ADR-B-0604 | 8.6.4 |
| ADR-B-11-K03 | Kod w kolumnie 15 tabeli A | teoria | 6 | ADR-B-0063, ADR-B-0208, ADR-B-0248, ADR-B-0434, ADR-B-0539, ADR-B-0575 | 8.6.3.1 |
| ADR-B-11-K04 | Najbardziej restrykcyjny kod w jednostce | teoria | 5 | ADR-B-0064, ADR-B-0086, ADR-B-0263, ADR-B-0432, ADR-B-0574 | 8.6.3.2 |
| ADR-B-11-K05 | Rozumienie znaczenia kodu tunelowego (-) i jego ograniczeń | teoria | 6 | ADR-B-0065, ADR-B-0174, ADR-B-0264, ADR-B-0431, ADR-B-0540, ADR-B-0603 | 8.6.3.1 |
| ADR-B-11-K06 | Wyłączenia 1.1.3 i przypadek 3.4.13 | teoria | 5 | ADR-B-0085, ADR-B-0209, ADR-B-0322, ADR-B-0512, ADR-B-0591 | 8.6.3.3 |
| ADR-B-11-K07 | Zachowanie podczas pożaru w tunelu | teoria | 5 | ADR-B-0143, ADR-B-0210, ADR-B-0308, ADR-B-0435, ADR-B-0592 | program kursu lit. k, 5.4.3.4 |
| ADR-B-12-K01 | Dokument tożsamości ze zdjęciem | teoria | 5 | ADR-B-0034, ADR-B-0067, ADR-B-0300, ADR-B-0416, ADR-B-0519 | 1.10.1.4 |
| ADR-B-12-K02 | Zabezpieczenie placów i składowania | teoria | 4 | ADR-B-0035, ADR-B-0066, ADR-B-0274, ADR-B-0415 | 1.10.1.3 |
| ADR-B-12-K03 | Szkolenie z ochrony i przeciwdziałania zagrożeniom | teoria | 7 | ADR-B-0036, ADR-B-0121, ADR-B-0275, ADR-B-0409, ADR-B-0410, ADR-B-0411, ADR-B-0412 | 1.10.2 |
| ADR-B-12-K04 | Weryfikacja tożsamości przewoźnika | teoria | 5 | ADR-B-0120, ADR-B-0211, ADR-B-0249, ADR-B-0413, ADR-B-0414 | 1.10.1.2 |
| ADR-B-12-K05 | Plan ochrony towarów dużego ryzyka | teoria | 17 | ADR-B-0122, ADR-B-0212, ADR-B-0304, ADR-B-0399, ADR-B-0400, ADR-B-0401, ADR-B-0402, ADR-B-0403, ADR-B-0404, ADR-B-0405, ADR-B-0406, ADR-B-0455, ADR-B-0456, ADR-B-0457, ADR-B-0458, ADR-B-0459, ADR-B-0460 | 1.10.3.2; 1.10.3.1.2 |
| ADR-B-12-K06 | Zabezpieczenie postoju i przed kradzieżą pojazdu | teoria | 6 | ADR-B-0144, ADR-B-0213, ADR-B-0305, ADR-B-0407, ADR-B-0408, ADR-B-0582 | 1.10.3.3, 8.4 |
| ADR-B-13-K01 | Numer UN i właściwa nazwa przewozowa | teoria | 8 | ADR-B-0037, ADR-B-0038, ADR-B-0226, ADR-B-0508, ADR-B-0523, ADR-B-0536, ADR-B-0577, ADR-B-0598 | 5.4.1.1.1(a),(b) |
| ADR-B-13-K02 | Dokument: liczba, rodzaj przesyłek i ilość | teoria | 6 | ADR-B-0069, ADR-B-0070, ADR-B-0227, ADR-B-0537, ADR-B-0578, ADR-B-0599 | 5.4.1.1.1(e),(f) |
| ADR-B-13-K03 | Dane odbiorcy i nadawcy | teoria | 5 | ADR-B-0068, ADR-B-0214, ADR-B-0233, ADR-B-0579, ADR-B-0600 | 5.4.1.1.1(g),(h) |
| ADR-B-13-K04 | Wzór i liczba stron instrukcji pisemnych | teoria | 6 | ADR-B-0039, ADR-B-0088, ADR-B-0234, ADR-B-0586, ADR-B-0587, ADR-B-0589 | 5.4.3.4 |
| ADR-B-13-K05 | Dokumenty i dowód tożsamości załogi | teoria | 4 | ADR-B-0087, ADR-B-0175, ADR-B-0250, ADR-B-0588 | 8.1.2.1 |
| ADR-B-13-K06 | Dodatkowy wpis w transporcie kombinowanym | teoria | 4 | ADR-B-0089, ADR-B-0215, ADR-B-0287, ADR-B-0601 | 5.4.1.1.7 |
| ADR-B-13-K07 | Dostępność dokumentów w kabinie | teoria | 4 | ADR-B-0090, ADR-B-0216, ADR-B-0228, ADR-B-0590 | 8.1.2.3 |
| ADR-B-13-K08 | Dodatkowe dokumenty zależnie od rodzaju ładunku | teoria | 10 | ADR-B-0145, ADR-B-0146, ADR-B-0306, ADR-B-0524, ADR-B-0525, ADR-B-0530, ADR-B-0531, ADR-B-0532, ADR-B-0533, ADR-B-0538 | 8.1.2, 5.4 |

## Luki i decyzje edytorskie

Nie stwierdzono **potwierdzonego braku tematu programu** ani celu z jednym pytaniem w aktualnej mapie kompetencji, który uzasadniałby dopisanie pytań 0610+ bez uprzedniej kontroli prawnej. Z tego powodu **nie dopisano sztucznych pytań dla samego zwiększenia licznika**. Numeracja kończy się na ADR-B-0609.

**Do jakościowego przeglądu specjalisty w pierwszej kolejności:** 29 kompetencji z dokładnie 3 przypisanymi pytaniami; w szczególności wymagające rozróżnienia podobnych klas, wyjątków, wymiarów oznakowania, odpowiedzialności cywilnej oraz przypadków awaryjnych. Brak wystarczającej różnorodności pytań lub niepotwierdzonego wyjątku prawnego może uzasadnić nowy rekord w kolejnej partii, ale dopiero po weryfikacji treści w ADR 2025 i sprostowaniu.

**Ograniczenia:** nie wykonano nowego literalnego audytu 609 pozycji w polskim Dzienniku Ustaw ani niezależnej recenzji A/B/C. Podane powiązania są robocze, a każdy rekord pozostaje `needs_review`. Kursant musi faktycznie odbyć obowiązkowe ćwiczenia praktyczne; trzy cele praktyczne nie powinny być „zaliczone” wyłącznie pytaniami testowymi.

## Dalszy etap

Do weryfikacji specjalisty przekazać kompetencje z trzema pytaniami, ocenić różnorodność zadań i porównać przepisy w ADR 2025 oraz sprostowaniu; nowe pytania od ADR-B-0610 wyłącznie dla **potwierdzonych**, a nie domniemanych luk.
