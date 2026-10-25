# Etap 4x16 — partia 3: porównanie literalne kolejnych 48 pytań

- Data: 25.10.2026.
- Punkt wyjścia: świeży `main`, commit `378dcd6c12025ef560bd03ff29d9a06962f5a523`.
- Zakres: 48 kolejnych otwartych pytań z klasyfikacji, oznakowania, dokumentów, wyposażenia, ograniczeń tunelowych i ochrony.
- Bank: 609 pytań; bez zmian w banku i kluczach; wszystkie nadal `needs_review`, 0 `verified`.

## Źródła

- [Dz.U. 2025 poz. 642 — ADR 2025](https://dziennikustaw.gov.pl/DU/2025/642).
- [Polski tekst ADR 2025, tom I — kopia MI](https://www.gov.pl/attachment/8856b22a-bfd8-4567-8386-b9709bba8da7).
- [Polski tekst ADR 2025, tom II — kopia MI](https://www.gov.pl/attachment/b7292c03-ac9d-4f80-9a29-c22f53d847b8).
- [Sprostowanie Dz.U. 2025 poz. 1575](https://eli.gov.pl/api/acts/DU/2025/1575/text.pdf).

## Wynik

- Przejrzano: **48** pytań.
- Zgodne w zakresie sprawdzonego punktu: **47**.
- Potwierdzone sprzeczności wymagające poprawki: **0**.
- Nie dało się potwierdzić w tej partii: **1** (`ADR-B-0162`).
- Zmiany w banku, kluczach lub explanation: **0**.
- Licznik nierozstrzygniętych porównań: **503 → 456**. W liczniku odjęto wyłącznie 47 pozycji, których tekstowe porównanie zakończono; ADR-B-0162 pozostaje otwarte.
- Wszystkie pytania nadal wymagają niezależnej oceny specjalisty.

## Rejestr pytanie → podstawa → wynik

| ID | Podstawa ADR | Wynik | Ustalenie |
|---|---|---|---|
| ADR-B-0159 | ADR 2025, 2.2.62.1.1; 2.2.61.1.1 | Zgodne w zakresie sprawdzonego punktu | ADR 2.2.62 i 2.2.61 odróżniają materiały zakaźne klasy 6.2 od materiałów trujących klasy 6.1. |
| ADR-B-0160 | ADR 2025, 8.2.1.4; 8.5 przepis szczególny S12 | Zgodne w zakresie sprawdzonego punktu | 8.2.1.4 i przepis szczególny S12 określają dodatkowe warunki szkolenia dla niektórych przewozów klasy 7; kurs podstawowy nie daje automatycznie uprawnień do każdego takiego przewozu. |
| ADR-B-0161 | ADR 2025, 2.2.8.1.1; 5.2.2.2.2 wzór nr 8 | Zgodne w zakresie sprawdzonego punktu | 2.2.8 i wzór nalepki 8 opisują zagrożenie żrące, które może powodować uszkodzenia skóry, oczu lub materiałów. |
| ADR-B-0162 | ADR 2025, 5.2.2.2.2 (model nr 9A); 3.2 tabela A: UN 3551, UN 3552; 2.2.9.1.7.2 | Nie da się potwierdzić | Nie da się zamknąć literalnego porównania w tej partii: pytanie wskazuje konkretne UN 3551/3552 i model 9A, więc trzeba osobno sprawdzić wpływ sprostowania Dz.U. 2025 poz. 1575 na te pozycje i ich oznakowanie. Pozostaje nierozstrzygnięte. |
| ADR-B-0165 | ADR 2025, 5.4.3.4 | Zgodne w zakresie sprawdzonego punktu | 5.4.3.4 wskazuje, by załoga korzystała z instrukcji pisemnych; przy zgłoszeniu zdarzenia przekazuje się sprawdzone informacje o ładunku. |
| ADR-B-0168 | ADR 2025, 5.4.3.4; 8.1.5.2 | Zgodne w zakresie sprawdzonego punktu | 8.1.5.2 przewiduje stojące znaki ostrzegawcze; ostrzeganie należy prowadzić bez wchodzenia w strefę oparów. |
| ADR-B-0169 | ADR 2025, 8.1.4.5 | Zgodne w zakresie sprawdzonego punktu | 8.1.4.5 wymaga łatwej dostępności gaśnic i ochrony przed warunkami atmosferycznymi. |
| ADR-B-0170 | ADR 2025, 5.3.2.3.1 | Zgodne w zakresie sprawdzonego punktu | 5.3.2.3.1: X przed numerem zagrożenia oznacza niebezpieczną reakcję z wodą. |
| ADR-B-0171 | ADR 2025, 8.1.5.3 | Zgodne w zakresie sprawdzonego punktu | 8.1.5.3 wymaga maski ucieczkowej dla każdego członka załogi przy nalepkach 2.3 lub 6.1. |
| ADR-B-0175 | ADR 2025, 1.10.1.4; 8.1.2.1 (d) | Zgodne w zakresie sprawdzonego punktu | 1.10.1.4 i 8.1.2.1(d) wymagają indywidualnych dokumentów identyfikacyjnych ze zdjęciem dla członków załogi, gdy przepisy mają zastosowanie. |
| ADR-B-0176 | ADR 2025, 8.1.4.4 | Zgodne w zakresie sprawdzonego punktu | 8.1.4.4 wymaga plomby i oznaczenia daty następnej kontroli lub maksymalnego okresu użytkowania; sama plomba nie wystarcza. |
| ADR-B-0179 | ADR 2025, 5.4.1.1.1; 5.4.1.1.3.1 | Zgodne w zakresie sprawdzonego punktu | 5.4.1.1.1 i 5.4.1.1.3.1 wymagają identyfikacji towaru oraz odpowiedniego oznaczenia odpadu; samo słowo ODPAD nie zastępuje danych towaru. |
| ADR-B-0182 | ADR 2025, 5.4.3.4 | Zgodne w zakresie sprawdzonego punktu | 5.4.3.4 zawiera instrukcje postępowania po zdarzeniu, w tym działania dotyczące wyłączenia akumulatora, o ile można je wykonać bezpiecznie. |
| ADR-B-0185 | ADR 2025, 5.4.3.4 | Zgodne w zakresie sprawdzonego punktu | 5.4.3.4 przewiduje przekazanie ratownikom informacji o przewożonym towarze i dostęp do instrukcji oraz dokumentów, gdy jest to bezpieczne. |
| ADR-B-0188 | ADR 2025, 5.2.1.1 | Zgodne w zakresie sprawdzonego punktu | 5.2.1.1 wymaga właściwego oznakowania numerem UN, poprzedzonym literami UN, gdy takie oznakowanie jest wymagane. |
| ADR-B-0189 | ADR 2025, 3.2 tabela A kol. (5); 5.2.2.1 | Zgodne w zakresie sprawdzonego punktu | 3.2 tabela A kolumna 5 i 5.2.2.1 określają nalepki główne i dodatkowe; trzeba umieścić wszystkie wymagane nalepki. |
| ADR-B-0190 | ADR 2025, 5.3.2.2.2 | Zgodne w zakresie sprawdzonego punktu | 5.3.2.2.2: górne pole numerowanej tablicy pomarańczowej zawiera numer rozpoznawczy zagrożenia. |
| ADR-B-0191 | ADR 2025, 5.3.2.2.1 | Zgodne w zakresie sprawdzonego punktu | 5.3.2.2.1 podaje standardowe wymiary 400 × 300 mm oraz ograniczone możliwości zmniejszenia rozmiaru, gdy nie ma miejsca. |
| ADR-B-0192 | ADR 2025, 5.3.2.3.1 | Zgodne w zakresie sprawdzonego punktu | 5.3.2.3.1: powtórzona cyfra zwykle wzmacnia odpowiadające jej zagrożenie. |
| ADR-B-0193 | ADR 2025, 5.3.2.2.2 | Zgodne w zakresie sprawdzonego punktu | 5.3.2.2 wymaga czytelnych i właściwych tablic; zabrudzone, nieczytelne oznakowanie trzeba doprowadzić do zgodności przed przewozem. |
| ADR-B-0194 | ADR 2025, 5.3.2.3.1 | Zgodne w zakresie sprawdzonego punktu | 5.3.2.3.1: cyfra 8 oznacza zagrożenie żrące. |
| ADR-B-0198 | ADR 2025, 8.1.2.2(a); 9.1.3; Umowa wielostronna M364, pkt 1 (warunkowy wyjątek dla naczepy do 31.12.2026) | Zgodne w zakresie sprawdzonego punktu | 8.1.2.2(a) wymaga świadectwa dopuszczenia w kabinie, jeśli jest wymagane. Warunki M364 są osobną umową i trzeba je sprawdzić oddzielnie. |
| ADR-B-0199 | ADR 2025, 7.5.2.1; 7.5.2.2 | Zgodne w zakresie sprawdzonego punktu | 7.5.2.1–7.5.2.2 wymagają sprawdzenia zakazów wspólnego załadunku; szczelność opakowań sama nie rozstrzyga zgodności. |
| ADR-B-0203 | ADR 2025, 5.4.1.1.7 | Zgodne w zakresie sprawdzonego punktu | 5.4.1.1.7 wymaga dodatkowego wpisu tylko wtedy, gdy przewóz jest wykonywany zgodnie z 1.1.4.2.1, a nie tylko dlatego, że jedzie do portu. |
| ADR-B-0206 | ADR 2025, 1.1.4.2.1 | Zgodne w zakresie sprawdzonego punktu | 1.1.4.2.1 przewiduje warunkowe uznanie części wymagań IMDG; sprawdza się, czy konkretny przewóz spełnia te warunki. |
| ADR-B-0207 | ADR 2025, 1.9.5.2.2; 8.6.4 | Zgodne w zakresie sprawdzonego punktu | 1.9.5.2.2 i 8.6.4 opisują ograniczenia kategorii tuneli; kategorię należy porównać z kodem przypisanym do towaru. |
| ADR-B-0212 | ADR 2025, 1.10.3.2.2 | Zgodne w zakresie sprawdzonego punktu | 1.10.3.2.2 dotyczy planu ochrony dla towarów dużego ryzyka; sama lista telefonów alarmowych nie obejmuje wszystkich środków ochrony. |
| ADR-B-0214 | ADR 2025, 5.4.1.1.1(g),(h) | Zgodne w zakresie sprawdzonego punktu | 5.4.1.1.1(g) wymaga danych nadawcy, a (h) danych odbiorcy; brak wymaganych danych należy uzupełnić przed przewozem. |
| ADR-B-0215 | ADR 2025, 5.4.1.1.7; 5.4.1.1.1 | Zgodne w zakresie sprawdzonego punktu | 5.4.1.1.7 dodaje zapis dla określonego łańcucha transportowego, ale nie zastępuje podstawowego opisu towaru z 5.4.1.1.1. |
| ADR-B-0216 | ADR 2025, 8.1.2.1(b); 8.1.2.3 | Zgodne w zakresie sprawdzonego punktu | 8.1.2.3 wymaga, aby instrukcje pisemne były łatwo dostępne; samo posiadanie ich w pojeździe nie wystarcza. |
| ADR-B-0217 | ADR 2025, 5.3.2.3.1 | Zgodne w zakresie sprawdzonego punktu | 5.3.2.3.1: podwójna cyfra 8 wskazuje nasilone zagrożenie żrące. |
| ADR-B-0218 | ADR 2025, 5.2.2.1.1; 3.2.1 tabela A kolumna (5) | Zgodne w zakresie sprawdzonego punktu | 5.2.2.1.1 i tabela A kolumna 5 wymagają nalepek odpowiadających zagrożeniu głównemu i dodatkowemu. |
| ADR-B-0219 | ADR 2025, 5.4.3.4 | Zgodne w zakresie sprawdzonego punktu | 5.4.3.4 instruuje kierowcę, by po awarii zatrzymał się w bezpiecznym miejscu, ostrzegł innych i postępował według instrukcji. |
| ADR-B-0220 | ADR 2025, 5.4.3.4 | Zgodne w zakresie sprawdzonego punktu | 5.4.3.4 wskazuje, że służbom należy przekazać dane o zdarzeniu i towarze, w tym informacje dostępne z dokumentów. |
| ADR-B-0225 | ADR 2025, 5.4.3.4 | Zgodne w zakresie sprawdzonego punktu | 5.4.3.4 wymaga, by nie podejmować działań w strefie zagrożenia bez oceny bezpieczeństwa; przy nieznanym wycieku pierwszeństwo ma własne bezpieczeństwo. |
| ADR-B-0226 | ADR 2025, 5.4.1.1.1(a) | Zgodne w zakresie sprawdzonego punktu | 5.4.1.1.1(a) wymaga liter UN przed numerem UN w dokumencie przewozowym. |
| ADR-B-0227 | ADR 2025, 5.4.1.1.1(e) | Zgodne w zakresie sprawdzonego punktu | 5.4.1.1.1(e) wymaga liczby i opisu sztuk przesyłek, gdy mają zastosowanie. |
| ADR-B-0228 | ADR 2025, 5.4.3.1; 8.1.2.3 | Zgodne w zakresie sprawdzonego punktu | 5.4.3.1 i 8.1.2.3 wymagają przechowywania instrukcji pisemnych w miejscu łatwo dostępnym dla załogi. |
| ADR-B-0231 | ADR 2025, 5.4.3.4; 8.1.5.2 | Zgodne w zakresie sprawdzonego punktu | 5.4.3.4 i 8.1.5.2: ostrzeganie innych nie może narażać załogi na opary; używa się właściwego wyposażenia i zachowuje bezpieczną odległość. |
| ADR-B-0232 | ADR 2025, 8.1.4.5 | Zgodne w zakresie sprawdzonego punktu | 8.1.4.5 wymaga gaśnicy łatwo dostępnej i właściwie zamocowanej. |
| ADR-B-0233 | ADR 2025, 5.4.1.1.1(h) | Zgodne w zakresie sprawdzonego punktu | 5.4.1.1.1(h) wymaga nazwy i adresu odbiorcy w typowym dokumencie przewozowym, z uwzględnieniem właściwych wyjątków. |
| ADR-B-0241 | ADR 2025, 5.4.1.1.6.3(b); 7.5.8.1 | Zgodne w zakresie sprawdzonego punktu | 5.4.1.1.6.3(b) wymaga dodatkowego zapisu „PRZEWÓZ ZGODNY Z 7.5.8.1” w opisanej sytuacji pustego, nieoczyszczonego pojazdu/kontenera. |
| ADR-B-0244 | ADR 2025, 8.3.6 | Zgodne w zakresie sprawdzonego punktu | 8.3.6 wymaga wyłączenia silnika podczas załadunku, jeżeli nie napędza urządzeń potrzebnych do tej czynności. |
| ADR-B-0248 | ADR 2025, 3.2.1 tabela A kolumna (15); 8.6.3.1 | Zgodne w zakresie sprawdzonego punktu | 3.2 tabela A kolumna 15 wskazuje kod ograniczeń tunelowych; 8.6.3.1 wyjaśnia, jak go odczytać. |
| ADR-B-0250 | ADR 2025, 1.10.1.4; 8.1.2.1 | Zgodne w zakresie sprawdzonego punktu | 1.10.1.4 i 8.1.2.1 wymagają dokumentu ze zdjęciem dla identyfikacji członków załogi, gdy przepisy ochrony mają zastosowanie. |
| ADR-B-0251 | ADR 2025, 8.1.5.2 | Zgodne w zakresie sprawdzonego punktu | 8.1.5.2 wymaga klina dla każdego pojazdu; liczba zależy od liczby pojazdów, nie osi. |
| ADR-B-0252 | ADR 2025, 8.1.5.2 | Zgodne w zakresie sprawdzonego punktu | 8.1.5.2 wymaga kamizelki ostrzegawczej dla każdego członka załogi. |
| ADR-B-0253 | ADR 2025, 8.1.5.2 | Zgodne w zakresie sprawdzonego punktu | 8.1.5.2 wymaga ochrony oczu dla każdego członka załogi, gdy stosuje się ten wykaz. |

## Pozycja pozostawiona otwarta

**ADR-B-0162** dotyczy nalepki 9A i konkretnych pozycji UN 3551/3552. Ponieważ wymaga to dokładnego powiązania wpisu tabeli A, wzoru nalepki i sprostowania z poz. 1575, nie zamykam jej na podstawie samego ogólnego opisu klasy 9. Pytanie pozostaje `needs_review`, a rozstrzygnięcie przekazano do bezpośredniego sprawdzenia przez specjalistę.

## Następny krok

Kontynuować kolejną partią 40–50 pozycji otwartych. Nie stwierdzono potwierdzonego błędu wymagającego zmiany treści w tej partii. Niczego nie oznaczono jako `verified`.
