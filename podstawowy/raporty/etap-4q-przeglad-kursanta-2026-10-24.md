# Etap 4q — próbkowy przegląd „oczami kursanta”

- Data przeglądu: 24.10.2026
- Świeży `main` przed zmianą: `ead09fe1acb15273ea900bdf9e9a337e44e00ffa` (bank 566 pytań; ostatni commit to ead09fe).
- Metoda losowania: deterministyczny generator LCG (32-bit, parametry 1664525 i 1013904223), seed `202610242307`; osobne przetasowanie Fishera–Yatesa w każdym dziale, pierwsze 5 rekordów. Próbka: 65 pytań, po 5 z każdego z 13 działów.
- Zakres oceny: czy wyjaśnienie najpierw podaje sens i uzasadnienie poprawnej odpowiedzi, tłumaczy wszystkie błędne opcje, kończy krótką podstawą ADR, używa języka dostępnego dla początkującego i nie powtarza szablonów.

## Wynik próby

W 65 rekordach nie znaleziono powtarzającego się dosłownego szablonu „Ta odpowiedź jest błędna, ponieważ…” ani powtarzalnej konstrukcji tego rodzaju. Wyjaśnienia zwykle porównują konkretne dystraktory lub grupy błędnych założeń i kończą podstawą ADR. Wykryto natomiast żargon, który nie był objaśniony w samym wyjaśnieniu: „multimodalny”, „radionuklidy”, „inicjacja”, „DMC” oraz „butle DOT”. To potwierdzony problem dostępności dla kursanta bez wcześniejszej wiedzy. Uproszczono siedem wyjaśnień, bez zmiany treści pytań, kluczy, źródeł ani statusu.

## Próbka i identyfikatory

| Dział | Pięć deterministycznie wybranych pytań |
|---|---|
| ADR-B-01 | ADR-B-0522, ADR-B-0148, ADR-B-0513, ADR-B-0093, ADR-B-0301 |
| ADR-B-02 | ADR-B-0317, ADR-B-0128, ADR-B-0497, ADR-B-0510, ADR-B-0267 |
| ADR-B-03 | ADR-B-0326, ADR-B-0178, ADR-B-0329, ADR-B-0343, ADR-B-0045 |
| ADR-B-04 | ADR-B-0131, ADR-B-0350, ADR-B-0164, ADR-B-0351, ADR-B-0474 |
| ADR-B-05 | ADR-B-0112, ADR-B-0108, ADR-B-0186, ADR-B-0015, ADR-B-0222 |
| ADR-B-06 | ADR-B-0190, ADR-B-0258, ADR-B-0562, ADR-B-0016, ADR-B-0547 |
| ADR-B-07 | ADR-B-0368, ADR-B-0379, ADR-B-0371, ADR-B-0481, ADR-B-0378 |
| ADR-B-08 | ADR-B-0056, ADR-B-0022, ADR-B-0282, ADR-B-0251, ADR-B-0283 |
| ADR-B-09 | ADR-B-0292, ADR-B-0201, ADR-B-0236, ADR-B-0172, ADR-B-0238 |
| ADR-B-10 | ADR-B-0454, ADR-B-0392, ADR-B-0389, ADR-B-0203, ADR-B-0442 |
| ADR-B-11 | ADR-B-0264, ADR-B-0263, ADR-B-0489, ADR-B-0322, ADR-B-0432 |
| ADR-B-12 | ADR-B-0035, ADR-B-0407, ADR-B-0304, ADR-B-0456, ADR-B-0413 |
| ADR-B-13 | ADR-B-0215, ADR-B-0227, ADR-B-0523, ADR-B-0287, ADR-B-0538 |

## Ocena 13 lekcji — po jednym akapicie

- **ADR-B-01:** Czytelne przykłady uprawnień, szkoleń i wyłączeń; skrót „multimodalny” zastąpiono opisem ciężarówka–statek w pytaniu 0522.
- **ADR-B-02:** Wyjaśnia różnice między klasami, ale terminy „radionuklid” i „inicjacja” mogą blokować początkującego; uproszczono pytania 0317 i 0497.
- **ADR-B-03:** Przykłady awarii i odpadów są praktyczne; próbka tłumaczy, czemu nie należy wąchać oparów ani samowolnie klasyfikować odpadu.
- **ADR-B-04:** Zastosowanie w postoju, nadzorze i unikaniu źródeł zapłonu jest zrozumiałe; wyjaśnienia 0350 i 0351 wskazują, co kierowca ma faktycznie sprawdzić.
- **ADR-B-05:** Instrukcje dotyczące widoczności, gaśnicy i pożaru ładunku są konkretne oraz rozróżniają mały pożar od sytuacji wymagającej oddalenia się.
- **ADR-B-06:** Przykłady tablic, nalepek i pozostałości po rozładunku są użyteczne; wyjaśnienia 0190, 0016 i 0562 rozdzielają oznaczenia, nie traktując ich jako zamienników.
- **ADR-B-07:** Obowiązki uczestników pokazano na przykładach załadunku, pakowania i rozładunku; wyjaśnienia wskazują, dlaczego odpowiedzialności nie można automatycznie przerzucić na kierowcę.
- **ADR-B-08:** Gaśnice i kliny opisano praktycznie; skrót DMC w pytaniu 0022 wymagał rozwinięcia i został wyjaśniony wprost.
- **ADR-B-09:** Mocowanie, strzałki i czyszczenie po wycieku mają bezpośrednie zastosowanie; wyjaśnienia odróżniają bezpieczne mocowanie od uszkadzania opakowania.
- **ADR-B-10:** Przewóz łączony wyjaśniono przez port, dokumenty i odcinek drogowy; specjalistyczne odniesienia wymagają zachowania przykładu obok przepisu.
- **ADR-B-11:** Kody tunelowe i znak „(-)” są objaśnione praktycznie; próbka rozróżnia ograniczenia tunelowe od ogólnych znaków drogowych.
- **ADR-B-12:** Ochronę pokazano przez weryfikację odbiorcy i dobór progu do sposobu przewozu; przy tabelach trzeba czytać właściwą kolumnę, a nie zgadywać po klasie.
- **ADR-B-13:** Dokumenty przedstawiono przez porównanie papierów z rzeczywistym ładunkiem; próbka wyjaśnia, dlaczego numer UN, nazwa i wzmianka o wyjątku nie są zamienne.

Wszystkie 13 plików zawiera mapę odsyłającą do istniejących ID i przykład z pracy kierowcy. Głównym problemem strukturalnym jest nagromadzenie historycznych szkiców i sekcji roboczych w długich plikach; nie usuwano ich, ponieważ są częścią historii redakcyjnej. Dla kolejnego kroku warto wyodrębnić krótką ścieżkę czytania dla kursanta, pozostawiając szkice instruktorskie w dokumentacji.

## Konkretne korekty

| ID | Problem językowy | Zmiana |
|---|---|---|
| ADR-B-0522 | „operacja multimodalna” bez objaśnienia | Wyjaśniono na przykładzie trasy ciężarówką i statkiem. |
| ADR-B-0317 | „radionuklidy” i „stężenie aktywności” bez prostego wprowadzenia | Opisano substancje promieniotwórcze i porównanie z progami ADR. |
| ADR-B-0497 | „inicjacja” jako żargon | Zastąpiono opisem trudności doprowadzenia do wybuchu i możliwych skutków. |
| ADR-B-0379 | ogólnik o przeciążeniu bez praktycznego kontekstu | Wyjaśniono, że pasy nie zmniejszają masy ładunku i nie eliminują przeciążenia. |
| ADR-B-0022 | skrót „DMC” nieobjaśniony | Rozwinięto jako dopuszczalną masę całkowitą pojazdu razem z ładunkiem. |
| ADR-B-0454 | „butle DOT” bez objaśnienia | Dodano krótkie wyjaśnienie, że chodzi o butle według amerykańskich wymagań DOT i rozróżnienie importu/eksportu. |
| ADR-B-0456 | „sztuki przesyłek” bez przykładu | Dodano wyjaśnienie „towar w osobnych opakowaniach” i porównanie ze zbiornikiem. |

Wszystkie poprawione wyjaśnienia mają 300–500 znaków. Klucze A/B/C, treści pytań, podstawy źródłowe i `verification_status` pozostają niezmienione. Żadne pytanie nie zostało oznaczone jako `verified`.

## Kontrola wskaźnika długości odpowiedzi

Po zmianach poprawna odpowiedź jest jedyną ściśle najdłuższą opcją w **79/566 = 13.96%** pytań. Próg Quality Gate to 18%; wynik pozostaje poniżej progu. Zmiany dotyczyły wyłącznie pola `explanation`, więc nie zmieniły długości opcji.

## Ograniczenia

To próbkowy przegląd redakcyjny, nie ekspertyza prawna. Nie potwierdza prawidłowości wszystkich przepisów ani wszystkich kluczy. Status całego banku pozostaje `needs_review` (566), `verified` (0). Przed publikacją potrzebna jest niezależna recenzja specjalisty ADR oraz porównanie z polskim tekstem urzędowym i sprostowaniem.
