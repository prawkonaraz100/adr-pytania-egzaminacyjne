# Etap 4x157 — drugi przegląd explanation (partia 2)

Data: 29.10.2026. Zakres: wyłącznie kurs podstawowy ADR. Bank bazowy: 651 pytań ADR-B-0001–0651, wszystkie `needs_review`.

## Wynik

Przepisano 30 wyjaśnień z najsłabszego końca rozkładu długości i czytelności. Zmieniono wyłącznie pole `explanation`; nie zmieniano treści pytań, odpowiedzi A/B/C, kluczy, źródeł ani statusów weryfikacji.

Każde wyjaśnienie napisano prostym językiem, aby wskazywało sens praktyczny, wyjaśniało mylące warianty i kończyło się krótką podstawą ADR. Docelowa długość to 300–500 znaków zgodnie z aktualnym Quality Gate; 2–5 zdań. Żadne pytanie nie zostało oznaczone jako `verified`.

## Lista ID i zmiana w skrócie

| ID | Przed | Po |
|---|---|---|
| ADR-B-0002 | Ogólne ostrzeżenie, że mały ładunek nie daje zwolnienia | Doprecyzowano, że zwolnienie zależy od towaru, ilości i warunków ADR, a nie od wielkości pojazdu lub trasy |
| ADR-B-0010 | Zakaz e-papierosów w czasie załadunku | Wyjaśniono ryzyko źródeł zapłonu i brak wyjątku dla kierowcy |
| ADR-B-0013 | Miejsce przechowywania instrukcji | Dodano praktyczny powód dostępności i wyjaśniono, czemu biuro/odbiorca nie wystarczą |
| ADR-B-0043 | Definicja klasy 6.2 | Wyraźniej rozróżniono klasy zakaźne, trujące i samonagrzewające |
| ADR-B-0084 | Odczyt kodu tunelowego D/E | Doprecyzowano różnicę dla sztuk przesyłek i odrzucono nadmiernie szerokie zakazy |
| ADR-B-0096 | Definicja klasy 5.2 | Rozdzielono nadtlenki organiczne od klas 5.1 i 6.1 |
| ADR-B-0102 | Ogólna rada o źródłach zapłonu | Wyjaśniono, czemu zapalniczka i włączanie urządzeń mogą zwiększyć zagrożenie |
| ADR-B-0151 | Znaczenie nalepki 2.3 | Dodano wyraźne porównanie z gazami 2.2 i materiałami żrącymi klasy 8 |
| ADR-B-0167 | Ogólne postępowanie ze skażoną odzieżą | Wskazano drogi przeniesienia skażenia i ryzyko dla załogi oraz innych osób |
| ADR-B-0170 | Znaczenie litery X | Doprecyzowano, dlaczego nie wolno zakładać, że woda jest bezpieczna |
| ADR-B-0178 | Ostrzeżenie przed oparami | Dodano bezpieczną kolejność działania i wyjaśniono, czemu nie wolno wąchać substancji |
| ADR-B-0192 | Powtórzona cyfra w numerze zagrożenia | Rozdzielono nasilenie zagrożenia od kodu tunelowego i zwolnień ADR |
| ADR-B-0251 | Liczba klinów pod koła | Wyjaśniono, czemu jeden klin i sam hamulec nie wystarczają dla dwóch pojazdów |
| ADR-B-0259 | Limit dla kategorii transportowej 3 | Porównano limit 1000 z 333 i brakiem limitu oraz przypomniano o obliczeniu ilości |
| ADR-B-0267 | Definicja klasy 8 | Rozróżniono zagrożenie żrące od promieniowania i materiałów zakaźnych |
| ADR-B-0270 | Rozpoznanie nalepki 5.1 | Wyjaśniono rolę symbolu, koloru i numeru oraz różnicę względem 6.1/2.2 |
| ADR-B-0284 | Rozpoznanie nalepki 2.2 | Wyraźniej odróżniono gazy niepalne od palnych i klasy 8 |
| ADR-B-0289 | Rozpoznanie nalepki 6.1 | Uproszczono różnicę między materiałami trującymi, zakaźnymi i żrącymi |
| ADR-B-0300 | Dokument tożsamości ze zdjęciem | Dodano praktyczny cel wymogu i wyjaśniono, czemu telefon lub dokument bez zdjęcia nie wystarczą |
| ADR-B-0308 | Pożar przestrzeni ładunkowej | Podkreślono odejście w bezpieczne miejsce, wezwanie pomocy i zakaz powrotu po rzeczy |
| ADR-B-0326 | Wyłączenie uproszczonej procedury odpadu | Wyjaśniono, czemu nazwa odpadu i kod katalogowy nie uchylają wyłączenia klasy 4.3 |
| ADR-B-0342 | Pierwszeństwo klasy 7 przy klasyfikacji odpadu | Wyjaśniono, że to szczególna reguła z wyjątkami, nie porównanie mas składników |
| ADR-B-0344 | Wybór pozycji i.n.o. | Doprecyzowano pierwszeństwo odpowiedniej pozycji szczegółowej przed ogólną |
| ADR-B-0368 | Obowiązki pakującego | Oddzielono zgodność wspólnego pakowania od masy towaru i zgody odbiorcy |
| ADR-B-0377 | Obowiązki odbiorcy | Wyjaśniono, czemu podpisanie dokumentu nie kończy obowiązków po rozładunku |
| ADR-B-0426 | Zapis „4.1 + 1” w tabeli | Wyjaśniono, że chodzi o dwie nalepki na jednej sztuce, nie o dwie palety/ładunki |
| ADR-B-0487 | Ograniczenie tunelowe D/E | Doprecyzowano zakres zakazu dla sztuk przesyłek i znaczenie pozostałych ograniczeń |
| ADR-B-0502 | Zabezpieczenie baterii z ogniwami równoległymi | Rozróżniono ochronę elektryczną od opakowania i poziomu naładowania |
| ADR-B-0542 | Rozpoznanie klasy 3 | Wyjaśniono różnicę między cieczami zapalnymi, gazami palnymi i materiałami stałymi zapalnymi |
| ADR-B-0594 | Informacje przekazywane służbom | Podkreślono przekazywanie faktów, unikanie zgadywania i nieopóźnianie wezwania pomocy |

## Kontrole

- Po zmianie należy sprawdzić spójność snapshotów w `review/sequential/` i `review/legal-clauses/`, kluczy egzaminów 001–005 oraz bieżących manifestów pakietu recenzyjnego.
- Wymagany pełny Quality Gate i CI na dokładnym head PR; w szczególności JSONL, 651 unikalnych ID, statusy, minimum 300 znaków, balans odpowiedzi, egzaminy i integralność audytów.
- Wyjaśnienia i wskazane przepisy nie zostały niezależnie zatwierdzone prawnie. Wszystkie rekordy pozostają `needs_review`.
