# Etap 4x156 — drugi przegląd jakości explanation (partia 1)

Data: 29.10.2026. Zakres: wyłącznie kurs podstawowy ADR. Baza przed zmianą: 651 pytań, ostatnie ID ADR-B-0651.

## Wynik

- Przepisano 30 wyjaśnień: ADR-B-0611–0638 oraz ADR-B-0646–0647.
- Zachowano treść pytań, warianty A/B/C, klucze odpowiedzi, podstawy prawne i wszystkie statusy `needs_review`.
- Każde wyjaśnienie napisano ponownie w języku kursanta: najpierw sens praktyczny, potem wyjaśnienie mylących dystraktorów, a na końcu podstawa ADR.
- Wyjaśnienia mają 311–414 znaków; kontrola lokalna skryptem przed scaleniem powinna potwierdzić 2–5 zdań, minimum 200 znaków i statusy.
- Nie wykryto w ramach tej redakcji potwierdzonego błędu merytorycznego wymagającego zmiany pytania lub klucza. Nie jest to jednak niezależna weryfikacja prawna.
- Wszystkie rekordy pozostają `needs_review`; nic nie oznaczono jako `verified`.

## Lista zmian — przed / po w skrócie

| ID | Przed | Po |
|---|---|---|
| ADR-B-0611 | Zwięzłe porównanie klas 4.1 i 4.2 | Doprecyzowano ryzyko samozapalenia i pomyłki z klasami 4.3, 5.1 i 8 |
| ADR-B-0612 | Ogólna rada o rozlewie przy kanalizacji | Wyjaśniono priorytet bezpieczeństwa i ryzyko spłukiwania substancji |
| ADR-B-0613 | Ogólne ostrzeżenie przed nieznaną substancją | Rozwinięto ryzyko wdychania/kontaktu i kolejność działań |
| ADR-B-0614 | Zakaz gaszenia pożaru ładowni | Uzasadniono, dlaczego nawet mały ogień nie usprawiedliwia otwierania ładowni |
| ADR-B-0615 | Znaczenie litery X | Wyraźnie odróżniono reakcję z wodą od wybuchowości i doboru środka gaśniczego |
| ADR-B-0616 | Numer UN jako identyfikator | Rozdzielono numer zagrożenia od identyfikacji towaru i dodano praktyczne porównanie dokumentów |
| ADR-B-0617 | Miejsce umieszczenia strzałek | Dodano cel oznaczenia i wyjaśnienie, czemu jeden bok/góra nie wystarczą |
| ADR-B-0618 | Ogólne ostrzeżenie o uginającym się opakowaniu | Dodano przykłady obciążeń podczas jazdy i wyjaśniono ryzyko dodatkowej warstwy |
| ADR-B-0619 | Okres ważności zaświadczenia | Rozdzielono okres ważności, konkretną datę i procedurę odnowienia |
| ADR-B-0620 | Wymóg zrozumiałego języka instrukcji | Wyjaśniono, dlaczego ustne streszczenie nie zastępuje instrukcji dla każdego członka załogi |
| ADR-B-0621 | Definicja klasy 4.2 | Wyraźniej porównano klasy 4.1/4.3 i powiązano je z praktycznym odczytem oznaczeń |
| ADR-B-0622 | Definicja klasy 5.2 | Wyjaśniono rozkład pod wpływem ciepła i różnicę względem klas 5.1/3 |
| ADR-B-0623 | Definicja klasy 6.1 | Dodano proste rozróżnienie klas 6.1/6.2/8 i ostrzeżenie przed kontaktem |
| ADR-B-0624 | Definicja klasy 7 | Doprecyzowano odróżnienie od klas 6.2 i 8 oraz kontrolę dokumentów |
| ADR-B-0625 | Definicja klasy 8 | Dodano praktyczne ostrzeżenie i wyjaśnienie mylących klas 6.1/6.2 |
| ADR-B-0626 | Ogólna zasada oceny bezpieczeństwa | Wyraźniej wyjaśniono ryzyko powstania kolejnego poszkodowanego |
| ADR-B-0627 | Brak wymaganej nalepki | Rozdzielono funkcję nalepek od numeru UN i wpisu w dokumencie |
| ADR-B-0628 | Mocowanie nie może wgniatać opakowania | Dodano działania korygujące i wyjaśniono, czemu mocniejsze pasy pogarszają sytuację |
| ADR-B-0629 | Rozbieżność w oznaczeniu odpadu | Wyjaśniono ograniczenia samodzielnej zmiany dokumentu i potrzebę uzgodnienia |
| ADR-B-0630 | Przekazanie informacji ratownikom | Dodano warunek bezpiecznego dostępu do dokumentów i priorytet ochrony kierowcy |
| ADR-B-0631 | Ogólne postępowanie ze skażoną odzieżą | Doprecyzowano ryzyko przeniesienia substancji i zakaz samodzielnego czyszczenia |
| ADR-B-0632 | Ostrzeżenie osób postronnych | Wyjaśniono, że brak płomieni nie oznacza braku zagrożenia |
| ADR-B-0633 | Użycie kamizelki ostrzegawczej | Doprecyzowano rolę widzialności i warunek bezpiecznego założenia |
| ADR-B-0634 | Niezgodny rozmiar tablicy | Wyjaśniono, że mniejszy format jest dopuszczalny tylko w określonych warunkach |
| ADR-B-0635 | Powtórzona cyfra w numerze zagrożenia | Rozdzielono nasilenie zagrożenia, zakaz przewozu i rolę numeru UN |
| ADR-B-0636 | Nieczytelna tablica | Wyjaśniono, dlaczego dokument kierowcy i dopisanie markerem nie zastępują prawidłowej tablicy |
| ADR-B-0637 | Znaczenie cyfry 8 | Uproszczono definicję działania żrącego i rolę pozostałych cyfr kodu |
| ADR-B-0638 | Wspólny załadunek z żywnością | Dodano praktyczną decyzję w razie braku potwierdzenia zgodności |
| ADR-B-0646 | Test nie zastępuje ćwiczenia | Wyraźniej rozdzielono sprawdzanie wiedzy od praktycznej umiejętności użycia gaśnicy |
| ADR-B-0647 | Dobór i użycie gaśnicy w ćwiczeniu | Doprecyzowano ryzyko niewłaściwego środka i konieczność instruktażu |

## Kontrole i ograniczenia

- W tym PR zmieniono wyłącznie pole `explanation` dla wskazanych 30 rekordów i dodano niniejszy raport.
- Przed scaleniem wymagane są testy/Quality Gate i CI na dokładnym SHA PR, w tym kontrola schematu JSONL, unikalności ID, minimum 200 znaków, 2–5 zdań, statusów i integralności snapshotów/referencji banku.
- Jeśli kontrola ujawni nieaktualne snapshoty zależne od SHA banku, trzeba je odświeżyć w tej samej partii i ponownie uruchomić pełny Quality Gate.
- Przegląd dydaktyczny nie jest formalną recenzją prawną. Podstawy prawne pozostają do niezależnego potwierdzenia przez specjalistę ADR.
