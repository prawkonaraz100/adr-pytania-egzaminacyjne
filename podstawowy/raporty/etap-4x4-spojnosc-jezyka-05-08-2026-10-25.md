# ETAP 4x4 — kontrola spójności i języka kursanta: B-05–B-08

- Data: 25.10.2026.
- Bazowy `main`: `4a1aa1a56bc357edbff7bf79c1c5447bc603f7b1`.
- Zakres: 178 pytań B-05–B-08; porównano stem, A/B/C, klucz, explanation, źródła wskazane w rekordzie i odpowiednią lekcję.
- Kontrola referencji jest audytem redakcyjnym; nie oznacza niezależnej akceptacji prawnej.

## Wynik ilościowy

- Bank: 609 pytań; duplikaty ID: 0.
- Poprawna odpowiedź jest jedyną najdłuższą: 85/609 = 13.96% (limit 18%).
- Explanation w całym banku: 300–457 znaków; poniżej 200: 0; powyżej 500: 0; poza zakresem 2–5 zdań: 0.
- Statusy: 609 `needs_review`, 0 `verified`. Nie zmieniano statusów.
- Brak zmian ID, `module_id` i kluczy odpowiedzi. Egzaminy próbne nie wymagają regeneracji.

## Problemy i poprawki

1. **B-05 — instrukcje pisemne i dostęp do dokumentów.** Doprecyzowano przekazanie instrukcji przed przewozem, zrozumiały język, obowiązek zapoznania się z nimi przez załogę oraz udostępnianie ratownikom dokumentów, o ile jest to bezpieczne (ADR 5.4.3.1–5.4.3.4). Treść nie zachęca do wejścia w strefę zagrożenia.
2. **B-06 — tablica pomarańczowa.** Dodano wymiary standardowe 400 × 300 mm i warunkowy format 300 × 120 mm, gdy zastosowanie ma wyjątek z ADR 5.3.2.2.1. Doprecyzowano też odwołania do reguł położenia/usuwania nalepek i tablic.
3. **B-07 — obowiązki uczestników.** Dodano konkretne punkty ADR dla nadawcy, przewoźnika, załadowcy, rozładowcy i odbiorcy; podkreślono kontrolę masy, usuwanie pozostałości i brak automatycznego przeniesienia obowiązków po zleceniu czynności. Przypomniano o przewozie pasażerów i umiejętności użycia gaśnic (ADR 8.3.1–8.3.2).
4. **B-08 — gaśnice przy 1.1.3.6.** Doprecyzowano minimum jednej gaśnicy 2 kg proszku lub środka o równoważnej skuteczności (ADR 8.1.4.2).
5. **B-08 — świadectwo pojazdu.** Uzupełniono odwołania do ADR 9.1.3.1 i 8.1.2.2(a). Zaznaczono, że wyjątki umów wielostronnych, w tym M364 wymieniona w banku z datą 31.12.2026, wolno stosować tylko po sprawdzeniu aktualności i wszystkich warunków konkretnego pojazdu/przewozu.
6. **Dystraktory — ADR-B-0229.** Usunięto oczywiście niepasujące odpowiedzi o planie urlopów i rachunku paliwowym; zastąpiono je błędnymi, ale wiarygodnymi pomyłkami dotyczącymi dokumentów i momentu ich udostępnienia.
7. **Dystraktory — ADR-B-0190.** Zastąpiono odpowiedź o numerze zaświadczenia kierowcy bardziej wiarygodną pomyłką z numerem klasy. 
8. **Dystraktory — ADR-B-0379.** Zastąpiono odpowiedź o pojazdach elektrycznych mylnym ograniczeniem obowiązku do cystern.
9. **Dystraktory — ADR-B-0023.** Zastąpiono „zapasowy silnik/akumulator” wiarygodnymi, ale błędnymi uogólnieniami dotyczącymi progu DMC i doboru klina.

Po zmianach zsynchronizowano `exact_record_snapshot` w `review/sequential` oraz `question_snapshot` i uzasadnienia A/B/C w `review/legal-clauses` dla ADR-B-0023, 0190, 0229 i 0379. Dzięki temu mechaniczne kontrole audytu odzwierciedlają bieżące pytania, bez nadawania statusu weryfikacji prawnej.

Nie znaleziono potwierdzonej sprzeczności wymagającej zmiany klucza lub przypisania pytania do działu. Nie jest to równoznaczne z niezależną recenzją polskiego tekstu ADR.

## Pełna lista sprawdzonych pytań

Poniższa tabela zawiera wszystkie ID z B-05–B-08, skrócony temat, fragment lekcji porównany podczas audytu i podstawę prawną zapisaną w rekordzie banku.

## ADR-B-05 — 43 pytań

| ID | Pytanie / kompetencja sprawdzana | Fragment lekcji porównany | Podstawa z rekordu |
|---|---|---|---|
| `ADR-B-0013` | Gdzie podczas przewozu powinny znajdować się instrukcje pisemne ADR? | § 2 — Działania po zdarzeniu i instrukcje pisemne | 5.4.3.1 |
| `ADR-B-0014` | Co powinni zrobić członkowie załogi przed rozpoczęciem przewozu ADR? | § 2 — Działania po zdarzeniu i instrukcje pisemne | 5.4.3.3 |
| `ADR-B-0015` | Jak powinny być zamontowane gaśnice wymagane przez ADR? | § 3 — Pożar i wyposażenie | 8.1.4.5 |
| `ADR-B-0049` | Kiedy załoga powinna zapoznać się z pisemnymi instrukcjami ADR dotyczącymi postępowania w razie wypadku? | § 2 — Działania po zdarzeniu i instrukcje pisemne | 5.4.3.3 |
| `ADR-B-0050` | W jakim języku przewoźnik ma zapewnić załodze instrukcje pisemne ADR? | § 2 — Działania po zdarzeniu i instrukcje pisemne | 5.4.3.2 |
| `ADR-B-0104` | Po kolizji pojazdu ADR, jeśli jest to możliwe i bezpieczne, co należy zrobić z pojazdem zgodnie z instrukcjami pisem… | § 2 — Działania po zdarzeniu i instrukcje pisemne | 5.4.3.4 |
| `ADR-B-0105` | Do jakich informacji kierowca powinien sięgnąć, zgłaszając służbom wypadek z towarem niebezpiecznym? | § 2 — Działania po zdarzeniu i instrukcje pisemne | 5.4.3.4 |
| `ADR-B-0106` | Kierowca widzi chmurę par wydobywających się z uszkodzonej przesyłki ADR. Po której stronie miejsca zdarzenia powini… | § 2 — Działania po zdarzeniu i instrukcje pisemne | 5.4.3.4 |
| `ADR-B-0107` | Po awarii zapalają się towary niebezpieczne wewnątrz przedziału ładunkowego. Co zalecają instrukcje pisemne załodze? | § 2 — Działania po zdarzeniu i instrukcje pisemne | 5.4.3.4 |
| `ADR-B-0108` | W którym przypadku instrukcje pisemne dopuszczają użycie gaśnicy przez członków załogi, jeżeli działanie jest odpowi… | § 3 — Pożar i wyposażenie | 5.4.3.4 |
| `ADR-B-0109` | Jaki obowiązek informacyjny wobec ratowników mają członkowie załogi po wypadku z ADR? | § 2 — Działania po zdarzeniu i instrukcje pisemne | 5.4.3.4 |
| `ADR-B-0110` | Kierowca miał kontakt z uwolnioną substancją i jego ubranie zostało skażone. Co przewidują instrukcje pisemne ADR? | § 2 — Działania po zdarzeniu i instrukcje pisemne | 5.4.3.4 |
| `ADR-B-0111` | Co należy zrobić w razie zagrożenia dla osób postronnych wokół wypadku z ADR? | § 2 — Działania po zdarzeniu i instrukcje pisemne | 5.4.3.4 |
| `ADR-B-0112` | Jakich środków załoga powinna użyć podczas zabezpieczania miejsca zdarzenia, jeżeli jest to bezpieczne? | § 2 — Działania po zdarzeniu i instrukcje pisemne | 5.4.3.4 |
| `ADR-B-0113` | Czy pomoc rannemu po kontakcie z niebezpieczną substancją zawsze polega na natychmiastowym wejściu ratownika do skaż… | § 2 — Działania po zdarzeniu i instrukcje pisemne | 5.4.3.4; program praktyczny zał. 1 (Dz.U. 2021 poz. 2150) |
| `ADR-B-0165` | Dyspozytor numeru alarmowego pyta kierowcę o przewożoną substancję. Co należy mu przekazać? | § 2 — Działania po zdarzeniu i instrukcje pisemne | 5.4.3.4 |
| `ADR-B-0166` | Załoga pojazdu ADR widzi płomienie obejmujące już przestrzeń ładunkową. Co przewidują instrukcje pisemne? | § 2 — Działania po zdarzeniu i instrukcje pisemne | 5.4.3.4 |
| `ADR-B-0167` | Po bezpiecznym opuszczeniu miejsca awarii załoga zauważa skażone ubrania ochronne. Jak postąpić? | § 2 — Działania po zdarzeniu i instrukcje pisemne | 5.4.3.4 |
| `ADR-B-0168` | Przy zdarzeniu ADR kierowca może bezpiecznie wyjść z kabiny. Co powinien wykorzystać do ostrzeżenia innych? | § 3 — Pożar i wyposażenie | 5.4.3.4; 8.1.5.2 |
| `ADR-B-0169` | Gaśnica ADR w pojeździe jest zasłonięta ładunkiem i nie można jej szybko wyjąć. Co trzeba poprawić? | § 3 — Pożar i wyposażenie | 8.1.4.5 |
| `ADR-B-0182` | Po niewielkiej kolizji pojazd ADR jest unieruchomiony, a kierowca może bezpiecznie podejść do przełącznika wyłączają… | § 2 — Działania po zdarzeniu i instrukcje pisemne | 5.4.3.4 |
| `ADR-B-0183` | Z uszkodzonego opakowania ADR wydobywa się chmura oparów. Wiatr wieje od ładowni w stronę kierowcy. Gdzie powinien s… | § 2 — Działania po zdarzeniu i instrukcje pisemne | 5.4.3.4 |
| `ADR-B-0184` | Pali się niewielka część hamulca pojazdu ADR, ogień jest w początkowej fazie, a droga ewakuacji pozostaje bezpieczna… | § 2 — Działania po zdarzeniu i instrukcje pisemne | 5.4.3.4 |
| `ADR-B-0185` | Straż pożarna dojeżdża do uszkodzonego pojazdu ADR. Dokument przewozowy jest bezpiecznie dostępny w kabinie. Co jest… | § 2 — Działania po zdarzeniu i instrukcje pisemne | 5.4.3.4 |
| `ADR-B-0186` | W pobliżu awarii ADR zbierają się obserwatorzy. Kierowca sam znajduje się już w bezpiecznym miejscu. Co powinien zro… | § 2 — Działania po zdarzeniu i instrukcje pisemne | 5.4.3.4 |
| `ADR-B-0187` | Poszkodowany leży obok uszkodzonej przesyłki ADR, a w powietrzu widać chmurę gazu. Co jest pierwszym obowiązkiem oso… | § 2 — Działania po zdarzeniu i instrukcje pisemne | 5.4.3.4; program szkolenia praktycznego |
| `ADR-B-0219` | Gdy w trakcie przewozu ADR doszło do awarii i pojazd można bezpiecznie zatrzymać, co zgodnie z instrukcjami pisemnym… | § 2 — Działania po zdarzeniu i instrukcje pisemne | 5.4.3.4 |
| `ADR-B-0220` | Po zdarzeniu z towarem niebezpiecznym trzeba powiadomić służby. Jaką informację kierowca powinien przekazać oprócz l… | § 2 — Działania po zdarzeniu i instrukcje pisemne | 5.4.3.4 |
| `ADR-B-0221` | Z uszkodzonego opakowania wydostają się opary, a kierowca jest już w bezpiecznej odległości. Gdzie powinien pozostać… | § 2 — Działania po zdarzeniu i instrukcje pisemne | 5.4.3.4 |
| `ADR-B-0222` | Podczas przewozu ADR ogień objął przedział ładunkowy z towarami niebezpiecznymi. Co powinien zrobić członek załogi? | § 2 — Działania po zdarzeniu i instrukcje pisemne | 5.4.3.4 |
| `ADR-B-0223` | Pojawia się niewielki pożar opony, który jeszcze nie objął ładunku ADR. Kiedy członek załogi może rozważyć użycie ga… | § 3 — Pożar i wyposażenie | 5.4.3.4 |
| `ADR-B-0224` | Po awarii ADR obok pojazdu gromadzą się osoby postronne. Jakie działanie załogi jest zgodne z instrukcjami pisemnymi… | § 2 — Działania po zdarzeniu i instrukcje pisemne | 5.4.3.4 |
| `ADR-B-0225` | W ćwiczeniu P2 instruktor przedstawia poszkodowanego leżącego obok niezidentyfikowanego wycieku. Co kursant powinien… | § 2 — Działania po zdarzeniu i instrukcje pisemne | 5.4.3.4 |
| `ADR-B-0229` | Po wypadku służby ratownicze przyjeżdżają do bezpiecznie zatrzymanego pojazdu ADR. Co kierowca powinien udostępnić r… | § 2 — Działania po zdarzeniu i instrukcje pisemne | 5.4.3.4 |
| `ADR-B-0230` | W czasie zdarzenia ADR ubranie członka załogi zostało skażone substancją. Co należy zrobić zgodnie z instrukcjami pi… | § 2 — Działania po zdarzeniu i instrukcje pisemne | 5.4.3.4 |
| `ADR-B-0231` | Podczas awarii ADR kierowca musi ostrzec innych uczestników ruchu, ale w pobliżu są widoczne opary. Która zasada jes… | § 3 — Pożar i wyposażenie | 5.4.3.4; 8.1.5.2 |
| `ADR-B-0232` | Podczas kontroli gaśnica wymagana w pojeździe ADR leży luzem za siedzeniem, skąd może wypaść podczas hamowania. Co n… | § 3 — Pożar i wyposażenie | 8.1.4.5 |
| `ADR-B-0493` | Po wypadku przewożonego ADR materiału widać niewielki pożar hamulców, który nie objął ładunku. Kiedy załoga może roz… | § 3 — Pożar i wyposażenie | 5.4.3.4 (instrukcje pisemne) |
| `ADR-B-0494` | Wyciek ADR dostaje się do kratki kanalizacyjnej, a dostęp jest niebezpieczny ze względu na opary. Czy instrukcje pis… | § 2 — Działania po zdarzeniu i instrukcje pisemne | 5.4.3.4 (instrukcje pisemne) |
| `ADR-B-0516` | Przed odjazdem kierowca odbiera od przewoźnika instrukcje pisemne ADR, ale nie zdążył zapoznać się z działaniami na … | § 2 — Działania po zdarzeniu i instrukcje pisemne | 5.4.3.3 |
| `ADR-B-0585` | Gaśnica wymagana w pojeździe ADR jest schowana pod ładunkiem i nie można jej szybko wyjąć. Co należy poprawić? | § 3 — Pożar i wyposażenie | 8.1.4.5 |
| `ADR-B-0593` | Po awarii kierowca zatrzymał pojazd w bezpiecznym miejscu. Co powinien zrobić z silnikiem, jeśli nie jest potrzebny … | § 2 — Działania po zdarzeniu i instrukcje pisemne | 5.4.3.4 |
| `ADR-B-0594` | Wzywając pomoc po zdarzeniu z towarem ADR, kierowca nie zna jeszcze pełnej przyczyny awarii. Jakie informacje powini… | § 2 — Działania po zdarzeniu i instrukcje pisemne | 5.4.3.4 |

## ADR-B-06 — 45 pytań

| ID | Pytanie / kompetencja sprawdzana | Fragment lekcji porównany | Podstawa z rekordu |
|---|---|---|---|
| `ADR-B-0016` | Na numerowanej pomarańczowej tablicy ADR, gdzie znajduje się numer UN? | § 2 — Tablice pomarańczowe i numer zagrożenia | 5.3.2.2.2 |
| `ADR-B-0017` | Co oznacza litera X przed numerem rozpoznawczym zagrożenia na tablicy ADR? | § 2 — Tablice pomarańczowe i numer zagrożenia | 5.3.2.3.1 |
| `ADR-B-0018` | Jakie są standardowe wymiary tablicy pomarańczowej ADR? | § 2 — Tablice pomarańczowe i numer zagrożenia | 5.3.2.2.1 |
| `ADR-B-0051` | Co oznacza powtórzenie cyfry w numerze rozpoznawczym zagrożenia na tablicy ADR? | § 2 — Tablice pomarańczowe i numer zagrożenia | 5.3.2.3.1 |
| `ADR-B-0052` | Jaki jest podstawowy kolor tablicy ADR z numerem UN i numerem rozpoznawczym zagrożenia? | § 2 — Tablice pomarańczowe i numer zagrożenia | 5.3.2.2.2 |
| `ADR-B-0053` | Co może oznaczać numer rozpoznawczy zagrożenia rozpoczynający się od cyfry 8? | § 2 — Tablice pomarańczowe i numer zagrożenia | 5.3.2.3.1 |
| `ADR-B-0114` | Na opakowaniu zawierającym materiał niebezpieczny, dla którego ADR wymaga oznakowania numerem UN, jak należy podać t… | § 3–4 — Nalepki i kontrola oznakowania | 5.2.1.1 |
| `ADR-B-0115` | Kierowca zauważa, że na sztuce przesyłki brakuje wymaganej nalepki ostrzegawczej. Co jest poprawne? | § 3–4 — Nalepki i kontrola oznakowania | 5.2.2.1.1 |
| `ADR-B-0132` | Na jakich powierzchniach kontenera wymagającego nalepek dużego formatu ADR co do zasady się je umieszcza? | § 3–4 — Nalepki i kontrola oznakowania | 5.3.1.2 |
| `ADR-B-0133` | Nalepki kontenera ADR są niewidoczne z zewnątrz pojazdu. Co może być wymagane według 5.3.1.3? | § 3–4 — Nalepki i kontrola oznakowania | 5.3.1.3 |
| `ADR-B-0170` | Na numerowanej pomarańczowej tablicy ADR numer zagrożenia zaczyna się od X. Co to oznacza dla prób użycia wody? | § 2 — Tablice pomarańczowe i numer zagrożenia | 5.3.2.3.1 |
| `ADR-B-0188` | Na przesyłce, dla której ADR wymaga numeru UN, naniesiono same cyfry „1203” bez poprzedzających liter. Co jest prawi… | § 1 — Numer UN i oznakowanie sztuki przesyłki | 5.2.1.1 |
| `ADR-B-0189` | Paczka jest oznaczona główną nalepką ADR, ale według odpowiedniej pozycji w tabeli A wymaga też nalepki zagrożenia d… | § 3–4 — Nalepki i kontrola oznakowania | 3.2 tabela A kol. (5); 5.2.2.1 |
| `ADR-B-0190` | Na numerowanej pomarańczowej tablicy ADR dwa oznaczenia są rozdzielone poziomą czarną linią. Co oznacza górne oznacz… | § 2 — Tablice pomarańczowe i numer zagrożenia | 5.3.2.2.2 |
| `ADR-B-0191` | Standardowa pomarańczowa tablica ADR ma 400 × 300 mm. Czy w 5.3.2.2.1 przewidziano też dopuszczalne rozwiązanie dla … | § 2 — Tablice pomarańczowe i numer zagrożenia | 5.3.2.2.1 |
| `ADR-B-0192` | Na pomarańczowej tablicy ADR występuje dwukrotnie cyfra 3 w numerze rozpoznawczym zagrożenia, np. „33”. Jaką zasadę … | § 2 — Tablice pomarańczowe i numer zagrożenia | 5.3.2.3.1 |
| `ADR-B-0193` | Przed przewozem wymagana tablica ADR na pojeździe jest zabrudzona i jej cyfry stały się nieczytelne. Co trzeba zrobi… | § 2 — Tablice pomarańczowe i numer zagrożenia | 5.3.2.2.2 |
| `ADR-B-0194` | Numer rozpoznawczy zagrożenia na tablicy ADR zaczyna się cyfrą 8. Jakie zagrożenie sygnalizuje ta cyfra? | § 2 — Tablice pomarańczowe i numer zagrożenia | 5.3.2.3.1 |
| `ADR-B-0217` | Na tablicy pomarańczowej w górnym polu jest numer rozpoznawczy zagrożenia 88. Co informuje kierowcę podwójna cyfra 8… | § 2 — Tablice pomarańczowe i numer zagrożenia | 5.3.2.3.1 |
| `ADR-B-0255` | Na opisanej pomarańczowej tablicy ADR widnieje u góry „33”, a na dole „1203”. Które pole zawiera numer UN? | § 2 — Tablice pomarańczowe i numer zagrożenia | 5.3.2.2.2 |
| `ADR-B-0256` | Na górnym polu pomarańczowej tablicy ADR przed cyframi widnieje litera „X”. Co oznacza to dodatkowe oznaczenie? | § 2 — Tablice pomarańczowe i numer zagrożenia | 5.3.2.3.1 |
| `ADR-B-0257` | Uczeń opisuje tablicę ADR: pomarańczowy prostokąt, czarne cyfry w dwóch poziomych polach. Który opis rozdziału jest … | § 2 — Tablice pomarańczowe i numer zagrożenia | 5.3.2.2.2 |
| `ADR-B-0258` | Zespół przygotowuje standardową pomarańczową tablicę ADR o szerokości 40 cm. Jaka jest jej standardowa wysokość prze… | § 2 — Tablice pomarańczowe i numer zagrożenia | 5.3.2.2.1 |
| `ADR-B-0281` | Na sztuce przesyłki ADR zamiast oznaczenia „UN 1203” zapisano jedynie „1203”. Co należy sprawdzić i poprawić przy st… | § 3–4 — Nalepki i kontrola oznakowania | 5.2.1.1 |
| `ADR-B-0298` | Górne pole pomarańczowej tablicy ADR zawiera numer rozpoznawczy zagrożenia „80”. Jakie zagrożenie wskazuje ten numer… | § 2 — Tablice pomarańczowe i numer zagrożenia | 5.3.2.3.2 |
| `ADR-B-0299` | Kontener przewożący towary niebezpieczne wymaga dużych nalepek ostrzegawczych zgodnie z ADR 5.3.1.2. Gdzie zasadnicz… | § 3–4 — Nalepki i kontrola oznakowania | 5.3.1.2 |
| `ADR-B-0303` | Na sztuce przesyłki ADR wymagane są dwie różne nalepki zagrożeń. Jak należy ją oznakować? | § 3–4 — Nalepki i kontrola oznakowania | 5.2.2.1.1 |
| `ADR-B-0503` | Na górze tablicy pomarańczowej widnieje numer rozpoznawczy zagrożenia 30. Co oznacza cyfra 3 w tym numerze? | § 2 — Tablice pomarańczowe i numer zagrożenia | 5.3.2.3.1 |
| `ADR-B-0504` | Numer rozpoznawczy zagrożenia rozpoczyna się cyfrą 5. Którą właściwość ta cyfra zwykle oznacza? | § 2 — Tablice pomarańczowe i numer zagrożenia | 5.3.2.3.1 |
| `ADR-B-0505` | Na tablicy pomarańczowej numer zagrożenia zawiera cyfrę 9. Które zagrożenie ta cyfra ogólnie sygnalizuje? | § 2 — Tablice pomarańczowe i numer zagrożenia | 5.3.2.3.1 |
| `ADR-B-0506` | Kierowca widzi w numerze rozpoznawczym zagrożenia cyfrę 6. Jakie ogólne zagrożenia odpowiadają tej cyfrze? | § 2 — Tablice pomarańczowe i numer zagrożenia | 5.3.2.3.1 |
| `ADR-B-0507` | Kierowca przed odjazdem zauważa, że na numerowanej tablicy pomarańczowej górne pole zawiera „1203”, a dolne „33”. Do… | § 2 — Tablice pomarańczowe i numer zagrożenia | 5.3.2.2.2 |
| `ADR-B-0543` | Podczas kontroli kierowca odczytuje na tablicy pomarańczowej numer zagrożenia zaczynający się od cyfry 2. Jakie ogól… | § 2 — Tablice pomarańczowe i numer zagrożenia | 5.3.2.3.1 |
| `ADR-B-0544` | Kierowca porównuje dwa numery rozpoznawcze zagrożenia; jeden rozpoczyna się cyfrą 4. Z jaką właściwością powinien sk… | § 2 — Tablice pomarańczowe i numer zagrożenia | 5.3.2.3.1 |
| `ADR-B-0545` | Na szkoleniowym schemacie tablicy pomarańczowej numer zagrożenia zawiera cyfrę 7. Co ogólnie oznacza ona według ADR … | § 2 — Tablice pomarańczowe i numer zagrożenia | 5.3.2.3.1 |
| `ADR-B-0546` | Po załadunku opakowań ADR do kontenera stwierdzono, że wymagane nalepki dużego formatu są nieczytelne. Co należy zro… | § 3–4 — Nalepki i kontrola oznakowania | 5.3.1.1; 5.3.1.2 |
| `ADR-B-0547` | Kontener zawiera towary niebezpieczne należące do więcej niż jednej klasy. Jak ustalić, jakie nalepki dużego formatu… | § 3–4 — Nalepki i kontrola oznakowania | 5.3.1.1–5.3.1.4 |
| `ADR-B-0548` | Po rozładunku kontenera usunięto część towaru, ale pozostały niebezpieczne pozostałości. Czy można od razu usunąć na… | § 3–4 — Nalepki i kontrola oznakowania | 5.3.1.1.5 |
| `ADR-B-0549` | Ktoś proponuje namalować wymagany znak na kontenerze w kolorze i kształcie dowolnie dobranym przez firmę. Czy taki z… | § 3–4 — Nalepki i kontrola oznakowania | 5.3.1.7 |
| `ADR-B-0550` | Na pojeździe przewożącym towary niebezpieczne w kontenerze nalepki dużego formatu są zasłonięte przez inne ładunki. … | § 3–4 — Nalepki i kontrola oznakowania | 5.3.1.1; 5.3.1.7 |
| `ADR-B-0561` | Kontener z towarem ADR wymaga nalepek dużego formatu. Gdzie co do zasady należy je umieścić? | § 3–4 — Nalepki i kontrola oznakowania | 5.3.1.1.4 |
| `ADR-B-0562` | Nalepka dużego formatu na kontenerze została uszkodzona tak, że nie można rozpoznać jej symbolu. Co należy zrobić pr… | § 3–4 — Nalepki i kontrola oznakowania | 5.3.1.7 |
| `ADR-B-0563` | Kontener został rozładowany, ale nie został oczyszczony z niebezpiecznych pozostałości. Czy można usunąć jego nalepk… | § 3–4 — Nalepki i kontrola oznakowania | 5.3.1.1.5 |
| `ADR-B-0564` | Kontener przewozi towar, dla którego wymagane są nalepki dużego formatu. Na jednym boku umieszczono nalepkę innej kl… | § 3–4 — Nalepki i kontrola oznakowania | 5.3.1.1; 5.3.1.7 |
| `ADR-B-0565` | Pojazd ma pomarańczowe tablice wymagane dla przewozu. Po zakończeniu przewozu niebezpieczny towar usunięto, ale zbio… | § 2 — Tablice pomarańczowe i numer zagrożenia | 5.3.2.1.7 |

## ADR-B-07 — 48 pytań

| ID | Pytanie / kompetencja sprawdzana | Fragment lekcji porównany | Podstawa z rekordu |
|---|---|---|---|
| `ADR-B-0019` | Kto zgodnie z ADR przekazuje załodze pojazdu wymagane instrukcje pisemne? | § 1 — Obowiązki przewoźnika | 1.4.2.2.6; 5.4.3.2 |
| `ADR-B-0020` | Czy załadowca może przekazać do przewozu uszkodzone opakowanie z wyciekającym towarem niebezpiecznym? | § 2–3 — Załadowca, opakowanie i praktyczne przykłady | 1.4.3.1.1 (b) |
| `ADR-B-0021` | Kto przede wszystkim ma zadbać, by towar niebezpieczny był prawidłowo sklasyfikowany przed nadaniem? | § 1 — Nadawca i podział obowiązków | 1.4.2.1.1 (a) |
| `ADR-B-0054` | Czy załadowca może wydać przewoźnikowi uszkodzone opakowanie, z którego może wyciekać towar niebezpieczny? | § 1 — Obowiązki przewoźnika | 1.4.3.1.1 (b) |
| `ADR-B-0055` | Który uczestnik przewozu odpowiada m.in. za przekazanie przewoźnikowi informacji i danych wymaganych do przewozu ADR… | § 1 — Nadawca i podział obowiązków | 1.4.2.1.1 |
| `ADR-B-0116` | Przewoźnik widzi uszkodzoną przesyłkę ADR, z której wycieka substancja. Co należy zrobić przed przewozem? | § 1 — Obowiązki przewoźnika | 1.4.2.2.1(c); 1.4.2.2.3–1.4.2.2.4 |
| `ADR-B-0117` | Który uczestnik powinien udostępnić przewoźnikowi dane i dokumenty wymagane do wykonania przewozu ADR? | § 1 — Nadawca i podział obowiązków | 1.4.2.1.1 |
| `ADR-B-0118` | Odbiorca towaru ADR chce odmówić przyjęcia przesyłki wyłącznie z powodu wygody, mimo braku ważnego powodu. Jaką zasa… | § 3 — Pakujący, napełniający, rozładowca i odbiorca | 1.4.2.3.1 |
| `ADR-B-0134` | Kto odpowiada za spełnienie wymagań pakowania i wspólnego pakowania w ADR 1.4.3.2? | § 2–3 — Załadowca, opakowanie i praktyczne przykłady | 1.4.3.2 |
| `ADR-B-0135` | Przed rozładunkiem rozładowca widzi uszkodzenie mogące spowodować niebezpieczny wyciek. Co robi? | § 3 — Pakujący, napełniający, rozładowca i odbiorca | 1.4.3.7.1(b) |
| `ADR-B-0136` | Czy jednostka transportowa przewożąca ADR na zasadach 8.3.1 może zabrać pasażera niebędącego członkiem załogi? | § 2–3 — Załadowca, opakowanie i praktyczne przykłady | 8.3.1 |
| `ADR-B-0195` | Po rozładunku kontenera ADR odbiorca stwierdza niezgodność z wymaganiami, za którą odpowiada zgodnie z 1.4.2.3.2. Cz… | § 1 — Obowiązki przewoźnika | 1.4.2.3.2 |
| `ADR-B-0196` | Kierowca ADR stwierdza, że osoba niezwiązana z załogą chce jechać pojazdem jako pasażer podczas przewozu objętego 8.… | § 2–3 — Załadowca, opakowanie i praktyczne przykłady | 8.3.1 |
| `ADR-B-0245` | Załadowca widzi uszkodzoną sztukę przesyłki z wyciekiem ADR. Jak powinien zareagować? | § 2–3 — Załadowca, opakowanie i praktyczne przykłady | 1.4.3.1 |
| `ADR-B-0246` | Odbiorca chce bez ważnej przyczyny opóźniać przyjęcie dostarczonych towarów ADR. Co mówi zasada ADR? | § 3 — Pakujący, napełniający, rozładowca i odbiorca | 1.4.2.3.1 |
| `ADR-B-0285` | Przed przewozem ADR przewoźnik nie otrzymał wymaganych informacji o towarze od nadawcy. Co powinien zrobić? | § 1 — Obowiązki przewoźnika | 1.4.2.2.1(b) |
| `ADR-B-0290` | Pakujący przygotowuje sztuki przesyłek z towarami niebezpiecznymi do transportu ADR. Który obowiązek należy do pakuj… | § 2–3 — Załadowca, opakowanie i praktyczne przykłady | 1.4.3.2 |
| `ADR-B-0293` | Do jednostki transportowej przewożącej towary niebezpieczne ma wsiąść przypadkowy pasażer, który nie należy do załog… | § 2–3 — Załadowca, opakowanie i praktyczne przykłady | 8.3.1 |
| `ADR-B-0363` | Przewoźnik stwierdził przed wyjazdem naruszenie wymagań ADR. Kiedy według 1.4.2.2.3 może przekazać przesyłkę do dals… | § 1 — Obowiązki przewoźnika | 1.4.2.2.3 |
| `ADR-B-0364` | W drodze wykryto naruszenie ADR, które może zagrażać bezpieczeństwu. Co powinien zrobić przewoźnik? | § 1 — Obowiązki przewoźnika | 1.4.2.2.4 |
| `ADR-B-0365` | Nadawca korzysta z pracy innych uczestników przewozu ADR. Czy to automatycznie usuwa obowiązek nadawcy dbania o zgod… | § 1 — Nadawca i podział obowiązków | 1.4.2.1.2 |
| `ADR-B-0366` | Nadawca działa w imieniu innej firmy i nie poinformowano go o niebezpiecznym charakterze ładunku. Kto powinien przek… | § 1 — Nadawca i podział obowiązków | 1.4.2.1.3 |
| `ADR-B-0367` | Pakujący ukończył pakowanie ADR, lecz sztuki przesyłek nie mają wymaganego oznakowania. Co jest jego obowiązkiem? | § 2–3 — Załadowca, opakowanie i praktyczne przykłady | 1.4.3.2(b) |
| `ADR-B-0368` | Pakujący zamierza umieścić razem dwa towary niebezpieczne. Czego musi przestrzegać? | § 2–3 — Załadowca, opakowanie i praktyczne przykłady | 1.4.3.2(a) |
| `ADR-B-0369` | Rozładowca zamierza wyładować przesyłki ADR z innego pojazdu niż podany w dokumentach. Co należy zweryfikować przed … | § 3 — Pakujący, napełniający, rozładowca i odbiorca | 1.4.3.7.1(a) |
| `ADR-B-0370` | Podczas rozładunku ADR stwierdzono poważne uszkodzenie opakowania. Co rozładowca powinien zrobić zgodnie z 1.4.3.7.1… | § 3 — Pakujący, napełniający, rozładowca i odbiorca | 1.4.3.7.1(b) |
| `ADR-B-0371` | Po wyładunku ADR w pojeździe zostały niebezpieczne pozostałości, które wymagają oczyszczenia. Kto ma zapewnić ich us… | § 3 — Pakujący, napełniający, rozładowca i odbiorca | 1.4.3.7.1(d) |
| `ADR-B-0372` | Po całkowitym rozładowaniu i oczyszczeniu kontenera ADR pozostawiono nalepki wielkiego formatu, które nie są już wym… | § 3 — Pakujący, napełniający, rozładowca i odbiorca | 1.4.3.7.1(e) |
| `ADR-B-0373` | Załadowca ma przygotować do przewozu sztuki ADR i żywność w jednym pojeździe. Co powinien sprawdzić? | § 2–3 — Załadowca, opakowanie i praktyczne przykłady | 1.4.3.1.1(e) |
| `ADR-B-0374` | Przewoźnik ma przewieźć towary niebezpieczne, ale nie sprawdził wymaganych nalepek i tablic pojazdu. Co powinien zro… | § 1 — Obowiązki przewoźnika | 1.4.2.2.1(f) |
| `ADR-B-0375` | Przewoźnik chce oprzeć się na informacjach przekazanych przez nadawcę w zakresie dopuszczalności przewozu. Czy ADR t… | § 1 — Obowiązki przewoźnika | 1.4.2.2.2 |
| `ADR-B-0376` | Kierowca przewozu ADR nie zna sposobu używania wymaganej gaśnicy. Co mówi 8.3.2? | § 2–3 — Załadowca, opakowanie i praktyczne przykłady | 8.3.2 |
| `ADR-B-0377` | Odbiorca zauważył, że rozładunek powinien poprzedzać wymagane usunięcie zagrożenia. Czy może pominąć obowiązki rozła… | § 3 — Pakujący, napełniający, rozładowca i odbiorca | 1.4.2.3.1–1.4.2.3.2 |
| `ADR-B-0378` | Załadowca umieszcza towar ADR w kontenerze, po czym kontener wymaga oznakowania. Kto ma dopełnić wymogów oznakowania… | § 2–3 — Załadowca, opakowanie i praktyczne przykłady | 1.4.3.1.1(c) |
| `ADR-B-0379` | Przewoźnik kontroluje masę i załadunek pojazdu ADR. Czy jego obowiązki obejmują sprawdzenie, czy pojazd nie jest prz… | § 1 — Obowiązki przewoźnika | 1.4.2.2.1(e) |
| `ADR-B-0380` | Nadawca korzysta z danych technicznych dostarczonych przez pakującego. Czy może je wykorzystać do spełnienia części … | § 1 — Nadawca i podział obowiązków | 1.4.2.1.2 |
| `ADR-B-0477` | Odbiorca ADR korzysta z zewnętrznej firmy rozładunkowej. Czy przez samo zlecenie rozładunku przestaje odpowiadać za … | § 3 — Pakujący, napełniający, rozładowca i odbiorca | 1.4.2.3.3 |
| `ADR-B-0478` | Rozładowca korzysta ze specjalistycznego zakładu odkażania kontenera po przewozie ADR. Które stwierdzenie oddaje jeg… | § 3 — Pakujący, napełniający, rozładowca i odbiorca | 1.4.3.7.2 |
| `ADR-B-0479` | Załadowca ocenia zakaz wspólnego załadunku, wykorzystując zgodne dane przekazane mu przez nadawcę. Czy ADR dopuszcza… | § 2–3 — Załadowca, opakowanie i praktyczne przykłady | 1.4.3.1.2 |
| `ADR-B-0480` | Rozładowca zakończył rozładunek pojazdu i na jego zewnętrznej powierzchni pozostały niebezpieczne resztki powstałe p… | § 3 — Pakujący, napełniający, rozładowca i odbiorca | 1.4.3.7.1(d)(i) |
| `ADR-B-0481` | Po operacji rozładunku odpowiedniej jednostki ADR pracownik zamierza pozostawić otwarte zawory i otwory inspekcyjne.… | § 3 — Pakujący, napełniający, rozładowca i odbiorca | 1.4.3.7.1(d)(ii) |
| `ADR-B-0482` | Załadowca odebrał dane o ładunku ADR od innego uczestnika i chce na ich podstawie zweryfikować wymagane oznakowanie … | § 2–3 — Załadowca, opakowanie i praktyczne przykłady | 1.4.3.1.2; 1.4.3.1.1(d) |
| `ADR-B-0517` | Załadowca dostaje do przewozu sztukę przesyłki ADR z pęknięciem opakowania i możliwością wydostania się zawartości. … | § 1 — Nadawca i podział obowiązków | 1.4.3.1.1(b) |
| `ADR-B-0567` | Kierowca podczas manewru na placu przez własną nieuwagę uszkodził zaparkowany samochód. Co ogólnie może wynikać z od… | § 2–3 — Załadowca, opakowanie i praktyczne przykłady | 8.2.2.3.2(k); Kodeks cywilny art. 415; ADR 8.2.2.3.2(k) |
| `ADR-B-0568` | Przewoźnik nie wykonał prawidłowo umowy dostawy, a kontrahent wskazuje, że poniósł z tego powodu szkodę. Jaka zasada… | § 1 — Obowiązki przewoźnika | 8.2.2.3.2(k); Kodeks cywilny art. 471; ADR 8.2.2.3.2(k) |
| `ADR-B-0569` | Po naruszeniu wymogu ADR firma pyta, czy kierowca musi automatycznie osobiście zapłacić każdą szkodę związaną ze zda… | § 2–3 — Załadowca, opakowanie i praktyczne przykłady | 8.2.2.3.2(k); Kodeks cywilny art. 415 i 471; ADR 8.2.2.3.2(k) |
| `ADR-B-0583` | Pakujący zauważa przed wysyłką, że opakowanie nie spełnia wymagań dla danego towaru ADR. Co powinien zrobić? | § 2–3 — Załadowca, opakowanie i praktyczne przykłady | 1.4.3.2.1 |
| `ADR-B-0584` | Załadowca widzi uszkodzoną sztukę przesyłki ADR jeszcze przed umieszczeniem jej w pojeździe. Jak powinien postąpić? | § 2–3 — Załadowca, opakowanie i praktyczne przykłady | 1.4.3.1.1; 7.5.1 |

## ADR-B-08 — 42 pytań

| ID | Pytanie / kompetencja sprawdzana | Fragment lekcji porównany | Podstawa z rekordu |
|---|---|---|---|
| `ADR-B-0022` | Jaka jest minimalna łączna pojemność gaśnic (w przeliczeniu na proszek) dla jednostki transportowej ADR o DMC powyże… | § 1 — Gaśnice, DMC i terminy kontroli | 8.1.4.1 |
| `ADR-B-0023` | Jakiego wyposażenia wymaga ADR dla każdego pojazdu jednostki transportowej, gdy zastosowanie ma 8.1.5.2? | § 2 — Wyposażenie osobiste i dodatkowe | 8.1.5.2 |
| `ADR-B-0024` | Co musi być dostępne dla każdego członka załogi zgodnie z wykazem podstawowego wyposażenia ochronnego 8.1.5.2? | § 2 — Wyposażenie osobiste i dodatkowe | 8.1.5.2 |
| `ADR-B-0056` | Jaki przedmiot służy do zabezpieczenia koła pojazdu przed niekontrolowanym przetoczeniem, jeżeli jest wymagany w ADR… | § 2 — Wyposażenie osobiste i dodatkowe | 8.1.5.2 |
| `ADR-B-0057` | Czy podstawowy wykaz wyposażenia ADR wymaga dla załogi kamizelek ostrzegawczych? | § 2 — Wyposażenie osobiste i dodatkowe | 8.1.5.2 |
| `ADR-B-0071` | Jednostka transportowa o DMC 3,5 t przewozi ADR na pełnych zasadach 8.1.4.1. Jaka minimalna łączna pojemność gaśnic … | § 1 — Gaśnice, DMC i terminy kontroli | 8.1.4.1 |
| `ADR-B-0072` | Jednostka transportowa ma DMC 6 t i przewozi ADR na pełnych zasadach 8.1.4.1. Jaka jest minimalna łączna pojemność g… | § 1 — Gaśnice, DMC i terminy kontroli | 8.1.4.1 |
| `ADR-B-0073` | Jaka jest **minimalna** pojemność przenośnej gaśnicy proszkowej wymagana przez ADR 8.1.4.2 dla jednostki transportow… | § 1 — Gaśnice, DMC i terminy kontroli | 8.1.4.2 |
| `ADR-B-0074` | Podczas kontroli okazuje się, że termin przeglądu jednej z wymaganych gaśnic ADR minął. Co powinien zrobić kierowca? | § 1 — Gaśnice, DMC i terminy kontroli | 8.1.4.4; 8.1.4.5 |
| `ADR-B-0075` | W jednostce transportowej przewożącej towary, dla których obowiązuje 8.1.5.2, znajduje się kierowca i drugi członek … | § 2 — Wyposażenie osobiste i dodatkowe | 8.1.5.2 |
| `ADR-B-0076` | Jaką podstawową ochronę oczu wymaga 8.1.5.2 dla członka załogi, gdy mają zastosowanie te przepisy? | § 2 — Wyposażenie osobiste i dodatkowe | 8.1.5.2 |
| `ADR-B-0077` | Dla jakich nalepek ostrzegawczych ADR 8.1.5.3 wymaga maski ucieczkowej dla każdego członka załogi? | § 2 — Wyposażenie osobiste i dodatkowe | 8.1.5.3 |
| `ADR-B-0137` | Dla jakich kategorii pojazdów ADR przewiduje szczególne dopuszczenie według części 9? | § 3 — Typ pojazdu i świadectwo dopuszczenia | 9.1.2.1; 9.1.3 |
| `ADR-B-0171` | Zgodnie z 8.1.5.3, dla sztuk przesyłki oznaczonych nalepką 6.1 jakie dodatkowe wyposażenie dla każdego członka załog… | § 2 — Wyposażenie osobiste i dodatkowe | 8.1.5.3 |
| `ADR-B-0176` | Kontrolujesz wymaganą gaśnicę ADR. Plomba jest nienaruszona, ale nie ma oznaczenia terminu kolejnego przeglądu ani m… | § 1 — Gaśnice, DMC i terminy kontroli | 8.1.4.4 |
| `ADR-B-0197` | Pojazd jedzie z towarami ADR na warunkach zwolnienia 1.1.3.6. Zamiast gaśnicy proszkowej 2 kg przewoźnik proponuje g… | § 1 — Gaśnice, DMC i terminy kontroli | 8.1.4.2 |
| `ADR-B-0198` | Przewóz wykonuje samochód ciężarowy typu FL (pojazd silnikowy, nie naczepa), dla którego ADR wymaga świadectwa dopus… | § 3 — Typ pojazdu i świadectwo dopuszczenia | 8.1.2.2(a); 9.1.3; Umowa wielostronna M364, pkt 1 (warunkowy wyjątek dla naczepy do 31.12.2026) |
| `ADR-B-0251` | W jednostce transportowej ADR są dwa pojazdy. Ile klinów pod koła wymaga ogólna lista wyposażenia ADR 8.1.5.2? | § 2 — Wyposażenie osobiste i dodatkowe | 8.1.5.2 |
| `ADR-B-0252` | W pojeździe ADR jedzie dwóch członków załogi, ale jest tylko jedna kamizelka ostrzegawcza. Jak ocenić wyposażenie we… | § 2 — Wyposażenie osobiste i dodatkowe | 8.1.5.2 |
| `ADR-B-0253` | Przed przewozem ADR kierowca sprawdza wyposażenie załogi: są rękawice ochronne, ale brak ochrony oczu. Co wynika z 8… | § 2 — Wyposażenie osobiste i dodatkowe | 8.1.5.2 |
| `ADR-B-0254` | Ładunek wymaga nalepek zagrożenia 2.3 lub 6.1. Jakie dodatkowe wyposażenie przewiduje ADR 8.1.5.3? | § 2 — Wyposażenie osobiste i dodatkowe | 8.1.5.3 |
| `ADR-B-0282` | Drogowy przewóz ADR korzysta z wyłączenia 1.1.3.6, a jednostka transportowa nie ma żadnej gaśnicy. Jakie jest minima… | § 1 — Gaśnice, DMC i terminy kontroli | 8.1.4.2 |
| `ADR-B-0283` | Wymagana gaśnica w pojeździe ADR ma brakujące oznaczenie następnego terminu kontroli. Co należy zrobić? | § 1 — Gaśnice, DMC i terminy kontroli | 8.1.4.4 |
| `ADR-B-0319` | Jakie oznaczenie typu pojazdu stosuje ADR 9.1.1.2 do pojazdu przeznaczonego do przewozu materiałów i przedmiotów wyb… | § 3 — Typ pojazdu i świadectwo dopuszczenia | 9.1.1.2 (definicje pojazdów EX/II i EX/III) |
| `ADR-B-0417` | Jednostka transportowa ADR o DMC dokładnie 3,5 t jest objęta pełnym reżimem 8.1.4.1. Ile gaśnic minimalnie wymaga ta… | § 1 — Gaśnice, DMC i terminy kontroli | 8.1.4.1 |
| `ADR-B-0418` | Pojazd ADR DMC 6 t w pełnym reżimie 8.1.4.1 ma jedną gaśnicę 8 kg. Czy spełnia minimalną liczbę? | § 1 — Gaśnice, DMC i terminy kontroli | 8.1.4.1 |
| `ADR-B-0419` | Dla jednostki ADR o DMC dokładnie 7,5 t stosuje się pełny reżim 8.1.4.1. Jaka minimalna łączna pojemność gaśnic? | § 1 — Gaśnice, DMC i terminy kontroli | 8.1.4.1 |
| `ADR-B-0420` | Jednostka ADR powyżej 7,5 t ma dwie gaśnice: 2 kg i 6 kg. Czy łączna masa proszku spełnia minimum pełnego reżimu? | § 1 — Gaśnice, DMC i terminy kontroli | 8.1.4.1 |
| `ADR-B-0421` | Towary ADR jadą w ilościach korzystających z wyłączenia 1.1.3.6. Ile minimum przenośnych gaśnic według 8.1.4.2? | § 1 — Gaśnice, DMC i terminy kontroli | 8.1.4.2 |
| `ADR-B-0422` | Gaśnica w pojeździe ADR ma miniony termin następnej wymaganej kontroli. Czy można uznać ją za właściwie przygotowaną… | § 1 — Gaśnice, DMC i terminy kontroli | 8.1.4.4–8.1.4.5 |
| `ADR-B-0423` | W pojeździe ADR gaśnice umieszczono w zamkniętej skrzyni bez szybkiego dostępu dla załogi. Co wymaga 8.1.4.5? | § 1 — Gaśnice, DMC i terminy kontroli | 8.1.4.5 |
| `ADR-B-0483` | Przewóz ADR wymaga standardowego wyposażenia 8.1.5, a ładunek ma wyłącznie nalepkę 2.3. Czy płyn do płukania oczu je… | § 2 — Wyposażenie osobiste i dodatkowe | 8.1.5.2, przypis 2 |
| `ADR-B-0484` | W pojeździe ADR przewożona jest ciecz oznaczona wyłącznie nalepką nr 8. Czy według 8.1.5.3 zestaw do ograniczenia ro… | § 2 — Wyposażenie osobiste i dodatkowe | 8.1.5.3, przypis 4 |
| `ADR-B-0485` | Towar ma nalepkę 2.3, a załoga liczy dwie osoby. Ile masek ucieczkowych wymaga 8.1.5.3 dla tak oznaczonego przewozu? | § 2 — Wyposażenie osobiste i dodatkowe | 8.1.5.3 |
| `ADR-B-0486` | Przewożony jest wyłącznie gaz z nalepką 2.2. Czy 8.1.5.3 nakazuje wozić łopatę i pojemnik do zbierania uwolnionego g… | § 2 — Wyposażenie osobiste i dodatkowe | 8.1.5.3, przypis 4 |
| `ADR-B-0509` | Przed wyjazdem zestaw ADR składa się z samochodu ciężarowego i przyczepy. Na wyposażeniu jest jeden klin pod koło, d… | § 2 — Wyposażenie osobiste i dodatkowe | 8.1.5.2 |
| `ADR-B-0551` | Przewóz wymaga pojazdu, dla którego ADR przewiduje świadectwo dopuszczenia. Kierowca nie ma dokumentu przy sobie, ch… | § 3 — Typ pojazdu i świadectwo dopuszczenia | 9.1.3.1; 8.1.2.2 |
| `ADR-B-0552` | Czy każdy samochód przewożący dowolną ilość towarów niebezpiecznych musi automatycznie posiadać świadectwo dopuszcze… | § 3 — Typ pojazdu i świadectwo dopuszczenia | 9.1.3.1 |
| `ADR-B-0553` | Przed wyjazdem pojazdem wymagającym świadectwa dopuszczenia kierowca zauważa, że dokument stracił ważność. Co jest w… | § 3 — Typ pojazdu i świadectwo dopuszczenia | 9.1.3.1 |
| `ADR-B-0566` | Pojazd należy do rodzaju, dla którego wymagane jest świadectwo dopuszczenia ADR. Jakie znaczenie ma ważność tego świ… | § 3 — Typ pojazdu i świadectwo dopuszczenia | 9.1.3.1; 8.1.2.2 |
| `ADR-B-0596` | Wymagane wyposażenie ochronne ADR obejmuje kamizelkę ostrzegawczą dla członka załogi. Jedna kamizelka jest wspólna d… | § 2 — Wyposażenie osobiste i dodatkowe | 8.1.5.2 |
| `ADR-B-0597` | Załoga ma latarkę, ale nie ma wymaganych rękawic ochronnych ani ochrony oczu. Czy jedna rzecz może zastąpić pozostał… | § 2 — Wyposażenie osobiste i dodatkowe | 8.1.5.2 |


## Status

- Zmiany dotyczą tylko kursu podstawowego.
- Żadnego pytania nie oznaczono jako `verified`.
- Po scaleniu tej partii nastąpi audyt B-09–B-12, a potem B-13.
