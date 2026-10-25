# ETAP 4x4 — kontrola spójności i języka kursanta: B-13

- Data: 25.10.2026.
- Bazowy `main`: `01539537c525d5fb792e4c1ad2ca8d68337f29d2`.
- Zakres: wszystkie 47 pytań B-13; sprawdzono pytanie, A/B/C, klucz, explanation, wskazane podstawy ADR i treść lekcji.
- Status pozostaje `needs_review`; ten raport nie stanowi niezależnej opinii prawnej.

## Wynik ilościowy

- Bank: 609 pytań; duplikaty ID: 0.
- Poprawna odpowiedź jest jedyną najdłuższą: 83/609 = 13.63% (limit 18%).
- Explanation w całym banku: 300–457 znaków; poniżej 200: 0; powyżej 500: 0; poza zakresem 2–5 zdań: 0.
- W module B-13: 47 pytań; explanation 304–415 znaków, wszystkie 2–5 zdań.
- Statusy: 609 `needs_review`, 0 `verified`.

## Znalezione braki i poprawki

1. **Pola dokumentu przewozowego.** Lekcję uzupełniono o jawne mapowanie punktów ADR 5.4.1.1.1(a)–(k): numer UN, prawidłowa nazwa przewozowa, nalepki zagrożenia, grupa pakowania, kod tunelowy, liczba/rodzaj sztuk przesyłek, ilość, nadawca i odbiorca. Dodano zastrzeżenie, że zakres zależy od towaru i wyjątków.
2. **Dodatkowe określenia i przypadki.** Doprecyzowano odwołania do ADR 5.4.1.1.3 (ODPAD), 5.4.1.1.5 (SALVAGE PACKAGING), 5.4.1.1.6.1 (puste nieoczyszczone opakowanie) i 5.4.1.1.7 (wpis dla określonego przewozu morsko-drogowego).
3. **Dokumenty w kabinie.** Uzupełniono konkretne punkty 8.1.2.1, 8.1.2.2(a)–(b), 8.1.2.3 i 8.2.1 oraz wymóg dokumentu tożsamości ze zdjęciem z 1.10.1.4. Podkreślono, że dokumenty zależą od konkretnego pojazdu i przewozu.
4. **Język dokumentu.** Dodano regułę ADR 5.4.1.4.1 dla przewozu międzynarodowego, z zastrzeżeniem porozumień i wyjątków.
5. **M364.** Lekcja wskazuje datę 31 grudnia 2026 r. podaną w rekordzie banku jako koniec warunkowego wyjątku, ale wyraźnie ogranicza go do naczepy i wymaga sprawdzenia aktualnego tekstu, zakresu, sygnatariuszy oraz spełnienia warunków. Nie przeniesiono wyjątku na pojazd silnikowy typu FL.
6. **Powtórzenia w lekcji.** Usunięto powtarzający się podrozdział o wzorze, języku i przygotowaniu załogi, ponieważ jego treść już w całości znajdowała się w sekcji „Instrukcje pisemne ADR”.
7. **Dystraktory i explanation.**
   - ADR-B-0037: opcje o numerze rejestracyjnym i ogólnym słowie „niebezpieczny” zastąpiono wiarygodnymi pomyłkami dotyczącymi zapisu numeru UN.
   - ADR-B-0038: zastąpiono oczywiście niepasujące „imię kierowcy” i „numer faktury” pomyłkami z numerem UN i nazwą handlową.
   - ADR-B-0039: „jedną” i „dziesięć” stron zastąpiono wiarygodniejszymi pomyłkami „trzy” i „pięć”.
   - ADR-B-0087: pytanie przepisano tak, by sprawdzało właściwy dokument ze zdjęciem, a opcje dotyczyły karty bez fotografii, wspólnej listy i indywidualnego dokumentu.
   - ADR-B-0088: opcje o mapie i samej znajomości klas zastąpiono pomyłkami dotyczącymi notatki i streszczenia firmowego.
   - ADR-B-0145: opcje o archiwum i dokumentacji ośrodka zastąpiono wiarygodniejszymi, lecz błędnymi pomysłami na zastąpienie dokumentu wymaganego w pojeździe.
   - ADR-B-0250: opcje o karcie rabatowej i historii przeglądarki zastąpiono wspólną listą bez zdjęć i dokumentem tylko dla kierowcy.

Po zmianach zsynchronizowano `exact_record_snapshot` w `review/sequential` oraz `question_snapshot` i uzasadnienia A/B/C w `review/legal-clauses` dla siedmiu zmienionych pytań. Zsynchronizowano także treść pytań i explanation w wariantach próbnych 001–002 i ich kluczach. Nie zmieniono ID, `module_id`, ani klucza poprawnej odpowiedzi.

## Pełna lista sprawdzonych pytań

| ID | Pytanie / kompetencja sprawdzana | Fragment lekcji porównany | Podstawa z rekordu |
|---|---|---|---|
| `ADR-B-0037` | W jaki sposób numer identyfikacyjny towaru niebezpiecznego podaje się w dokumencie przewozowym ADR? | § 1 — Opis towaru, pola i kolejność | 5.4.1.1.1 (a) |
| `ADR-B-0038` | Czy w dokumencie przewozowym ADR potrzebna jest prawidłowa nazwa przewozowa towaru? | § 1 — Opis towaru, pola i kolejność | 5.4.1.1.1 (b) |
| `ADR-B-0039` | Ile stron liczy standardowy wzór instrukcji pisemnych ADR? | § 3 — Instrukcje pisemne | 5.4.3.4 |
| `ADR-B-0068` | Którą informację o odbiorcy trzeba co do zasady zamieścić w dokumencie przewozowym ADR? | § 1 — Opis towaru, pola i kolejność | 5.4.1.1.1 (h) |
| `ADR-B-0069` | Jakie informacje o opakowanych towarach niebezpiecznych powinny się znaleźć w dokumencie przewozowym ADR? | § 1 — Opis towaru, pola i kolejność | 5.4.1.1.1 (e) |
| `ADR-B-0070` | Czy w standardowym dokumencie ADR podaje się całkowitą ilość przewożonego towaru niebezpiecznego? | § 1 — Opis towaru, pola i kolejność | 5.4.1.1.1 (f) |
| `ADR-B-0087` | Który dokument spełnia wymóg identyfikacji członka załogi ze zdjęciem, gdy ma zastosowanie ADR 1.10.1.4? | § 2 — Dokumenty w kabinie i identyfikacja | 8.1.2.1(d); 1.10.1.4 |
| `ADR-B-0088` | Czy kierowca zawsze może zastąpić instrukcje pisemne ADR własnoręcznie sporządzoną notatką? | § 3 — Instrukcje pisemne | 5.4.3.4 |
| `ADR-B-0089` | Przewóz drogowy odbywa się na szczególnych warunkach 1.1.4.2.1 w łańcuchu morsko-drogowym. Jaki dodatkowy zapis jes… | § 2–4 — Dokumenty dodatkowe i sytuacje szczególne | 5.4.1.1.7 |
| `ADR-B-0090` | Gdzie w jednostce transportowej należy przechowywać instrukcje pisemne ADR zgodnie z 8.1.2.3? | § 3 — Instrukcje pisemne | 5.4.3.1; 8.1.2.3 |
| `ADR-B-0145` | Gdzie podczas przewozu powinno znajdować się wymagane świadectwo dopuszczenia samochodu ciężarowego typu FL (pojazd… | § 2 — Dokumenty w kabinie i identyfikacja | 8.1.2.2(a); Umowa wielostronna M364, pkt 1 (warunkowy wyjątek dla naczepy do 31.12.2026) |
| `ADR-B-0146` | Czy w kabinie trzeba mieć zaświadczenie o przeszkoleniu kierowcy ADR, gdy jest ono wymagane według 8.2.1? | § 2 — Dokumenty w kabinie i identyfikacja | 8.1.2.2(b); 8.2.1 |
| `ADR-B-0175` | W kabinie pojazdu ADR dwaj członkowie załogi mają po jednym dokumencie tożsamości, ale tylko jeden zawiera fotograf… | § 2 — Dokumenty w kabinie i identyfikacja | 1.10.1.4; 8.1.2.1 (d) |
| `ADR-B-0214` | Wymagany dokument przewozowy ADR podaje prawidłowy numer UN i nazwę towaru, lecz nie ma danych nadawcy. Co należy p… | § 1 — Opis towaru, pola i kolejność | 5.4.1.1.1(g),(h) |
| `ADR-B-0215` | Dokument przewozowy zawiera wzmiankę „PRZEWÓZ ZGODNY Z 1.1.4.2.1” dla odpowiedniego łańcucha morsko-drogowego. Czy … | § 1 — Opis towaru, pola i kolejność | 5.4.1.1.7; 5.4.1.1.1 |
| `ADR-B-0216` | Kierowca ma wymagane instrukcje pisemne ADR w kabinie, lecz schował je pod stertą dokumentów i nie jest w stanie sz… | § 2 — Dokumenty w kabinie i identyfikacja | 8.1.2.1(b); 8.1.2.3 |
| `ADR-B-0226` | W dokumencie przewozowym ADR wpisano prawidłową nazwę przewozową, lecz pominięto litery UN przed czterocyfrowym num… | § 1 — Opis towaru, pola i kolejność | 5.4.1.1.1(a) |
| `ADR-B-0227` | Sprawdzasz wymagany dokument przewozowy ADR dla zapakowanego towaru. Podano numer UN i nazwę, lecz nie podano liczb… | § 1 — Opis towaru, pola i kolejność | 5.4.1.1.1(e) |
| `ADR-B-0228` | Instrukcje pisemne ADR znajdują się w wymaganym pojeździe, lecz są zamknięte w niedostępnej podczas jazdy skrzynce … | § 3 — Instrukcje pisemne | 5.4.3.1; 8.1.2.3 |
| `ADR-B-0233` | W wymaganym dokumencie przewozowym ADR znajduje się numer UN, ale brakuje nazwy i adresu odbiorcy. Co trzeba uzupeł… | § 1 — Opis towaru, pola i kolejność | 5.4.1.1.1(h) |
| `ADR-B-0234` | Kierowca otrzymał skróconą, jednostronicową instrukcję sporządzoną przez firmę zamiast wymaganego wzoru instrukcji … | § 3 — Instrukcje pisemne | 5.4.3.2; 5.4.3.4 |
| `ADR-B-0250` | Załoga wykonuje przewóz ADR podlegający wymaganiom 1.10.1.4. Jakiego dokumentu nie należy pomijać podczas kontroli? | § 2 — Dokumenty w kabinie i identyfikacja | 1.10.1.4; 8.1.2.1 |
| `ADR-B-0287` | Wymagany dokument przewozowy dotyczy przewozu ADR realizowanego zgodnie z 1.1.4.2.1 w łańcuchu morskim lub lotniczy… | § 2–4 — Dokumenty dodatkowe i sytuacje szczególne | 5.4.1.1.7 |
| `ADR-B-0306` | Kierowca prowadzi przewóz ADR, dla którego wymagane są dokumenty przewidziane w 8.1.2. Który zestaw powinien znajdo… | § 2 — Dokumenty w kabinie i identyfikacja | 8.1.2.1–8.1.2.2 |
| `ADR-B-0508` | Przed wyjazdem kierowca sprawdza dokument przewozowy dla benzyny. W polu identyfikacji zapisano „1203 BENZYNA”, bez… | § 1 — Opis towaru, pola i kolejność | 5.4.1.1.1(a) |
| `ADR-B-0523` | W dokumencie przewozowym kierowca widzi klasę zagrożenia głównego, ale towar ma też nalepkę zagrożenia dodatkowego … | § 1 — Opis towaru, pola i kolejność | 5.4.1.1.1(c) |
| `ADR-B-0524` | Dla przewożonego towaru tabela A podaje grupę pakowania II. Kierowca sprawdza opis towaru w dokumencie przewozowym.… | § 1 — Opis towaru, pola i kolejność | 5.4.1.1.1(d) |
| `ADR-B-0525` | Plan przewozu ADR prowadzi przez tunel z ograniczeniami, a dla towaru w kolumnie (15) podano kod D/E. Co należy umi… | § 1 — Opis towaru, pola i kolejność | 5.4.1.1.1(k) |
| `ADR-B-0530` | Kierowca odbiera odpad niebezpieczny inny niż radioaktywny. Nazwa przewozowa w dokumencie nie zawiera wymaganego sł… | § 1 — Odpady, opakowanie awaryjne i puste nieoczyszczone opakowanie | 5.4.1.1.3 |
| `ADR-B-0531` | Uszkodzoną sztukę przesyłki ADR umieszczono zgodnie z przepisami w opakowaniu awaryjnym typu salvage packaging. Co … | § 1 — Odpady, opakowanie awaryjne i puste nieoczyszczone opakowanie | 5.4.1.1.5 |
| `ADR-B-0532` | Po opróżnieniu pojemnika, który pozostaje nieoczyszczony i zawiera pozostałości materiału ADR klasy innej niż 7, sp… | § 1 — Odpady, opakowanie awaryjne i puste nieoczyszczone opakowanie | 5.4.1.1.6.1 |
| `ADR-B-0533` | Towary ADR nadawane są w Polsce do innego państwa. Dokument przewozowy sporządzono wyłącznie po polsku, bez zastoso… | § 4 — Język dokumentu i kopie | 5.4.1.4.1 |
| `ADR-B-0536` | Na kontroli dokumentów stwierdzono, że opis pozycji ADR zawiera właściwe dane UN, nazwę przewozową, klasę, grupę pa… | § 1 — Opis towaru, pola i kolejność | 5.4.1.1.1 |
| `ADR-B-0537` | W jednym dokumencie przewozowym wykazano dwa różne towary niebezpieczne, o innych numerach UN. Co należy sprawdzić … | § 1 — Opis towaru, pola i kolejność | 5.4.1.1.1(f) |
| `ADR-B-0538` | Nadawca dzieli przesyłkę między dwa pojazdy, bo nie mieści się w jednym. Jak rozwiązuje kwestię dokumentów przewozo… | § 4 — Język dokumentu i kopie | 5.4.1.4.2 |
| `ADR-B-0577` | W dokumencie ADR podano czterocyfrowy identyfikator towaru, lecz nie dopisano liter UN. Jak należy poprawić wpis? | § 1 — Opis towaru, pola i kolejność | 5.4.1.1.1(a) |
| `ADR-B-0578` | W dokumencie podano numer UN i klasę, ale brakuje wymaganej liczby oraz rodzaju sztuk przesyłek. Co należy zrobić? | § 1 — Opis towaru, pola i kolejność | 5.4.1.1.1(e) |
| `ADR-B-0579` | Dokument ADR nie zawiera adresu odbiorcy, choć nie zachodzi żaden przewidziany wyjątek. Co zrobić przed wyjazdem? | § 1 — Opis towaru, pola i kolejność | 5.4.1.1.1(h) |
| `ADR-B-0586` | Instrukcje pisemne ADR mają ustalony wzór. Firma chce zastąpić je krótką kartką z własnym logo. Co należy zrobić? | § 3 — Instrukcje pisemne | 5.4.3.4 |
| `ADR-B-0587` | Instrukcje pisemne są w kabinie, ale kierowca nie przeczytał ich i nie wie, gdzie znaleźć informacje o zagrożeniu ł… | § 3 — Instrukcje pisemne | 5.4.3.3 |
| `ADR-B-0588` | Kierowca przewozi towary niebezpieczne i podczas kontroli ma okazać dokumenty wymagane dla tego przewozu. Gdzie pow… | § 2 — Dokumenty w kabinie i identyfikacja | 8.1.2.1 |
| `ADR-B-0589` | Kierowca otrzymał instrukcje pisemne w języku, którego nie rozumie. Co powinien zrobić przed rozpoczęciem przewozu? | § 3 — Instrukcje pisemne | 5.4.3.2 |
| `ADR-B-0590` | Instrukcje pisemne ADR znajdują się w kabinie, ale są zamknięte w schowku, do którego załoga nie ma dostępu podczas… | § 3 — Instrukcje pisemne | 5.4.3.1; 8.1.2.3 |
| `ADR-B-0598` | W dokumencie przewozowym wpisano numer UN i nazwę handlową produktu, ale brakuje wymaganej nazwy przewozowej ADR. C… | § 1 — Opis towaru, pola i kolejność | 5.4.1.1.1(a)–(b) |
| `ADR-B-0599` | W dokumencie przewozowym podano liczbę opakowań, ale pominięto wymaganą informację o ilości towaru. Co powinien zro… | § 1 — Opis towaru, pola i kolejność | 5.4.1.1.1(e)–(f) |
| `ADR-B-0600` | Dokument przewozowy zawiera dane odbiorcy, ale brakuje nazwy i adresu nadawcy. Nie wskazano żadnego wyjątku. Jak po… | § 1 — Opis towaru, pola i kolejność | 5.4.1.1.1(g)–(h) |
| `ADR-B-0601` | Ładunek przyjechał drogą morską, a dokumenty przygotowano według IMDG. Przewoźnik rozpoczyna dalszy odcinek drogowy… | § 4 — Dokumenty i wyjątki transportu kombinowanego | 1.1.4.2.1; 5.4.1.1.7 |

## Status

- Wyłącznie kurs podstawowy; nie rozpoczęto kursu cystern.
- Żadne pytanie nie zostało oznaczone jako `verified`.
- Wymagany jest PASS pełnego Quality Gate CI przed scaleniem.


## Naprawa czerwonego Quality Gate — potwierdzone logi CI

Pierwszy czerwony przebieg: [run 40194287828](https://github.com/prawkonaraz100/adr-pytania-egzaminacyjne/actions/runs/40194287828) oraz równoległy [run 40194269443](https://github.com/prawkonaraz100/adr-pytania-egzaminacyjne/actions/runs/40194269443). Oba zatrzymały się na dwóch testach jednostkowych:

1. `test_variant_003_ids_answer_key_and_no_overlap`: wariant 003 miał stare opcje dla `ADR-B-0039` („Jedną/Cztery/Dziesięć”), podczas gdy bank zawierał „Trzy/Cztery/Pięć”; klucz 003 miał też stare explanation. Zsynchronizowano opcje wariantu i wyjaśnienie klucza z bankiem, bez zmiany poprawnej litery B.
2. `test_shortest_and_absolute_rates_per_module`: w B-13 poprawna odpowiedź była najkrótszą opcją w 21/47 pytań, powyżej progu 38%. W pięciu pytaniach (`ADR-B-0037`, `0038`, `0087`, `0088`, `0145`) skrócono mylące, lecz realistyczne dystraktory tak, by nie dało się zgadywać po samej długości. Nie zmieniono kluczy ani sensu prawnego.

Po poprawkach odświeżono techniczne snapshoty w `review/sequential` i `review/legal-clauses`; nie ustawiono żadnego statusu na `verified`.

### Kontrola ilościowa po poprawce
- Bank: 609 pytań, duplikaty ID: 0.
- Poprawna odpowiedź jest jedyną najdłuższą: 83/609 = 13.63% (próg 18%).
- B-13: poprawna odpowiedź jest najkrótsza w 16/47 = 34.04% (próg 38%).
- Explanation: minimum 300 znaków; poniżej 200: 0. Wszystkie pytania pozostają `needs_review`.

Pełny status końcowego CI odczytaj z historii PR #318; raport nie deklaruje PASS, dopóki ostatni commit gałęzi nie przejdzie obu jobów.
