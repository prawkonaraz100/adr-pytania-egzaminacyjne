# Etap 4x253 — praktyczna kontrola numeru UN na sztuce przesyłki

Data: 31.10.2026  
Zakres: wyłącznie kurs podstawowy ADR  
Baza: świeży `main` po scaleniu PR #722, commit `0b2c1897a7e4b76cb08d48b4c92e61c3a52943e3`  
Kompetencja: `ADR-B-06-K01`  
Nowy scenariusz: `SC-ADR-B-06-04`

## Uzasadnienie luki

Audyt mapy kompetencji wykazał, że ADR-B-06-K01 („Numer UN na sztuce przesyłki”) ma cztery pytania, ale nie był powiązany z żadnym pełnym scenariuszem praktycznym. Trzy pytania (ADR-B-0114, 0188 i 0281) sprawdzają głównie zapamiętanie zapisu „UN” przed numerem; czwarte (ADR-B-0616) rozróżnia numer zagrożenia od numeru UN. Brakowało sytuacji łączącej oznakowanie opakowania, tablicę pomarańczową i dokument przewozowy przed wyjazdem.

## Zmiana

Dodano `SC-ADR-B-06-04`: na standardowej sztuce przesyłki wymagającej numeru UN widnieją same cyfry „1203”, dokument przewozowy zawiera „UN 1203”, a na tablicy pomarańczowej widnieje „33/1203”. Kursant ma rozpoznać, że „33” jest numerem rozpoznawczym zagrożenia, „1203” numerem UN, a na opakowaniu wymagającym oznakowania numerem UN musi być zapis „UN 1203”. Sam poprawny wpis w dokumencie ani tablica pojazdu nie zastępują oznakowania opakowania.

- Pytania powiązane: ADR-B-0114, ADR-B-0188 i ADR-B-0616. Nie dodano ani nie zmieniono pytań banku.
- Uzupełniono mapę kompetencji ADR-B-06-K01, lekcję ADR-B-06, materiał instruktora i indeks scenariuszy.
- Moduł ADR-B-06 ma teraz 4 scenariusze; cały kurs ma 43 scenariusze. Każdy z 13 działów ma co najmniej 3.
- Bank pozostaje bez zmian: 678 rekordów, wszystkie `needs_review`, zero `verified`; SHA `7c21fccb7d7e17e71fd98be534133582b54d52af`.

## Podstawa i granice obowiązków

ADR 5.2.1.1 — wymagane oznakowanie sztuki przesyłki numerem UN poprzedzonym literami „UN”; ADR 5.3.2.2.2 — układ numeru rozpoznawczego zagrożenia i numeru UN na tablicy pomarańczowej; ADR 5.4.1.1.1 — numer UN poprzedzony literami „UN” w dokumencie przewozowym. Jeżeli przewoźnik podczas wykonywania kontroli stwierdzi naruszenie wymagań ADR, 1.4.2.2.3 nakazuje nie rozpoczynać przewozu do czasu usunięcia naruszenia; zakres informacji i dokumentacji przed rozpoczęciem przewozu określa 1.4.2.2.1(b).

Scenariusz dotyczy opakowania, dla którego nie ma wyjątku od oznakowania numerem UN. Kursant nie klasyfikuje samodzielnie towaru i nie nanosi oznaczeń na rzeczywistą przesyłkę; zgłasza niezgodność odpowiedzialnemu podmiotowi. Ćwiczenie odbywa się na fikcyjnych dokumentach i pustej makiecie.

## Stan po partii

- Bank: 678 pytań ADR-B-0001–0678; wszystkie `needs_review`, 0 `verified`.
- SHA banku bez zmian; egzaminy próbne 001–005 i klucze nie wymagają aktualizacji.
- Scenariusze: 43 łącznie; B-03, B-04, B-05 i B-06 mają po 4, pozostałe działy po 3.
- Brak nowych snapshotów prawnych i sekwencyjnych, ponieważ nie zmieniono żadnego pytania. Zmiana scenariusza nie jest recenzją ani zatwierdzeniem prawnym.
- Pełny Quality Gate i CI wymagane przed scaleniem PR.
