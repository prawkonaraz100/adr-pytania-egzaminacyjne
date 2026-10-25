# Etap 4x16 — partia 5: 48 pytań, w tym pozycje wymagające specjalisty

- Data: 25.10.2026.
- Punkt wyjścia: świeży `main`, commit `a760666c7a141b00814b334a276bada46ab42dbc`.
- Zakres: LQ i oznakowanie, dokumenty, zakaz palenia, klasy zagrożenia, klasyfikacja odpadów, wspólny załadunek i wybrane nowe pozycje ADR 2025.
- Bank: 609 pytań; bez zmian w pytaniach i kluczach; wszystkie pozostają `needs_review`, 0 `verified`.

## Źródła

- [Dz.U. 2025 poz. 642 — ADR 2025](https://dziennikustaw.gov.pl/DU/2025/642).
- [Polski tekst ADR 2025, tom I — kopia MI](https://www.gov.pl/attachment/8856b22a-bfd8-4567-8386-b9709bba8da7).
- [Polski tekst ADR 2025, tom II — kopia MI](https://www.gov.pl/attachment/b7292c03-ac9d-4f80-9a29-c22f53d847b8).
- [Sprostowanie Dz.U. 2025 poz. 1575](https://eli.gov.pl/api/acts/DU/2025/1575/text.pdf).

## Wynik

- Przejrzano: **48** pytań.
- Zgodne w zakresie sprawdzonego punktu: **32**.
- Potwierdzone sprzeczności wymagające poprawki: **0**.
- Nie dało się potwierdzić bez dalszego odczytu punktu/wyjątku: **16**.
- Zmiany w banku, kluczach lub explanation: **0**.
- Licznik nierozstrzygniętych porównań: **408 → 375** (odjęto wyłącznie 32 pozycje zakończone).
- Statusy: wszystkie nadal `needs_review`; 0 `verified`.

## Rejestr pytanie → podstawa → wynik

| ID | Podstawa ADR | Wynik | Ustalenie |
|---|---|---|---|
| ADR-B-0010 | ADR 2025, 8.3.5 | Zgodne w zakresie sprawdzonego punktu | 8.3.5 zakazuje palenia podczas manipulowania towarami niebezpiecznymi i w ich pobliżu; e-papieros także może być źródłem zapłonu. |
| ADR-B-0103 | ADR 2025, 8.3.5 | Zgodne w zakresie sprawdzonego punktu | 8.3.5 obejmuje zakaz palenia w trakcie czynności ładunkowych i w pobliżu pojazdu, gdy ma zastosowanie. |
| ADR-B-0273 | ADR 2025, 3.4.7.1 | Zgodne w zakresie sprawdzonego punktu | 3.4.7.1 określa znak dla ilości ograniczonych LQ; nie jest to nalepka klasy zagrożenia. |
| ADR-B-0276 | ADR 2025, 5.2.1.8.3 | Zgodne w zakresie sprawdzonego punktu | 5.2.1.8.3: symbol ryby i drzewa oznacza zagrożenie dla środowiska. |
| ADR-B-0277 | ADR 2025, 5.4.1.1.7 | Zgodne w zakresie sprawdzonego punktu | 5.4.1.1.7 wymaga wpisu „PRZEWÓZ ZGODNY Z 1.1.4.2.1”, gdy przewóz rzeczywiście odbywa się na tych warunkach. |
| ADR-B-0279 | ADR 2025, 8.3.5 | Zgodne w zakresie sprawdzonego punktu | 8.3.5: zakaz palenia dotyczy również papierosa elektronicznego podczas załadunku. |
| ADR-B-0280 | ADR 2025, 8.3.5 | Zgodne w zakresie sprawdzonego punktu | 8.3.5 zabrania palenia podczas czynności ładunkowych i w pobliżu pojazdu; nie ma wyjątku tylko dlatego, że ktoś jest w kabinie. |
| ADR-B-0281 | ADR 2025, 5.2.1.1 | Zgodne w zakresie sprawdzonego punktu | 5.2.1.1 wymaga liter UN przed czterocyfrowym numerem na sztuce przesyłki, gdy oznakowanie numerem UN jest wymagane. |
| ADR-B-0283 | ADR 2025, 8.1.4.4 | Zgodne w zakresie sprawdzonego punktu | 8.1.4.4 wymaga oznaczenia terminu następnej kontroli lub maksymalnego okresu użytkowania; brak oznaczenia trzeba wyjaśnić przed wyjazdem. |
| ADR-B-0284 | ADR 2025, 5.2.2.2.2 | Zgodne w zakresie sprawdzonego punktu | Wzór nalepki 2.2 w 5.2.2.2.2 oznacza gaz niepalny i nietrujący. |
| ADR-B-0285 | ADR 2025, 1.4.2.2.1(b) | Zgodne w zakresie sprawdzonego punktu | 1.4.2.2.1(b): przewoźnik powinien mieć dane potrzebne do sprawdzenia zgodności przewozu; gdy ich brakuje, nie może ich zgadywać. |
| ADR-B-0287 | ADR 2025, 5.4.1.1.7 | Zgodne w zakresie sprawdzonego punktu | 5.4.1.1.7 wymaga dodatkowego zapisu dla przewozu zgodnego z 1.1.4.2.1. |
| ADR-B-0288 | ADR 2025, 5.2.2.2.2 | Zgodne w zakresie sprawdzonego punktu | Wzór nalepki 3 w 5.2.2.2.2 oznacza materiały ciekłe zapalne. |
| ADR-B-0289 | ADR 2025, 5.2.2.2.2 | Zgodne w zakresie sprawdzonego punktu | Wzór 6.1 w 5.2.2.2.2 ostrzega przed materiałem trującym. |
| ADR-B-0291 | ADR 2025, 7.5.2.1 | Zgodne w zakresie sprawdzonego punktu | 7.5.2.1 wymaga sprawdzenia tabeli zakazów wspólnego załadunku; same nalepki nie oznaczają automatycznie zakazu lub zgody bez zastosowania tabeli. |
| ADR-B-0294 | ADR 2025, 5.4.1.1.3.1 | Zgodne w zakresie sprawdzonego punktu | 5.4.1.1.3.1: słowo ODPAD dodaje się do prawidłowej nazwy przewozowej w opisanych przypadkach; nie zastępuje ono identyfikacji towaru. |
| ADR-B-0295 | ADR 2025, 5.4.3.4 | Zgodne w zakresie sprawdzonego punktu | 5.4.3.4: nieprzeszkolony członek załogi powinien przede wszystkim zadbać o własne bezpieczeństwo, ostrzec innych i wezwać pomoc. |
| ADR-B-0296 | ADR 2025, 5.4.3.4 | Zgodne w zakresie sprawdzonego punktu | Przy możliwych palnych oparach nie należy uruchamiać źródeł zapłonu ani przełączać urządzeń, jeśli mogłoby to wywołać iskrę. |
| ADR-B-0297 | ADR 2025, 5.4.3.4 | Zgodne w zakresie sprawdzonego punktu | Ostrzeżenie osób postronnych i utrzymywanie bezpiecznej odległości jest właściwe, jeśli można to zrobić bez narażenia się na opary. |
| ADR-B-0298 | ADR 2025, 5.3.2.3.2 | Zgodne w zakresie sprawdzonego punktu | 5.3.2.3.2: numer 80 oznacza materiał żrący bez wskazania dodatkowego zagrożenia przez inne cyfry. |
| ADR-B-0299 | ADR 2025, 5.3.1.2 | Zgodne w zakresie sprawdzonego punktu | 5.3.1.2: duże nalepki na kontenerze co do zasady umieszcza się na obu bokach i obu końcach. |
| ADR-B-0302 | ADR 2025, 2.2.42.1.1 | Zgodne w zakresie sprawdzonego punktu | 2.2.42.1.1: klasa 4.2 obejmuje materiały podatne na samozapalenie lub samonagrzewanie. |
| ADR-B-0303 | ADR 2025, 5.2.2.1.1 | Zgodne w zakresie sprawdzonego punktu | 5.2.2.1.1 wymaga wszystkich nalepek głównego i dodatkowego zagrożenia wskazanych dla przesyłki. |
| ADR-B-0306 | ADR 2025, 8.1.2.1–8.1.2.2 | Zgodne w zakresie sprawdzonego punktu | 8.1.2.1–8.1.2.2 określają, które dokumenty muszą znajdować się w kabinie: m.in. dokumenty przewozowe, instrukcje pisemne, dokumenty identyfikacyjne i wymagane świadectwa. |
| ADR-B-0307 | ADR 2025, 2.2.52.1.2, 2.2.52.1.4 | Zgodne w zakresie sprawdzonego punktu | 2.2.52 wskazuje, że nadtlenki organiczne mogą rozkładać się niebezpiecznie; niekontrolowane ogrzewanie zwiększa ryzyko reakcji. |
| ADR-B-0308 | ADR 2025, 5.4.3.4 | Zgodne w zakresie sprawdzonego punktu | 5.4.3.4: pożar przedziału ładunkowego wymaga oddalenia się i alarmowania, nie podejmowania gaszenia ładunku przez załogę. |
| ADR-B-0309 | ADR 2025, 2.2.62.1.1 | Zgodne w zakresie sprawdzonego punktu | 2.2.62.1.1: klasa 6.2 obejmuje materiały zakaźne mogące powodować choroby u ludzi lub zwierząt. |
| ADR-B-0311 | ADR 2025, 2.2.62.1.2 | Zgodne w zakresie sprawdzonego punktu | 2.2.62.1.2 rozróżnia kategorie materiałów zakaźnych według zagrożenia dla ludzi i zwierząt. |
| ADR-B-0313 | ADR 2025, 1.1.3.1(a)(i) | Zgodne w zakresie sprawdzonego punktu | 1.1.3.1(a)(i) przewiduje wyłączenie dla określonych przewozów prywatnych na własny użytek, jeśli spełnione są warunki opakowania i ilości. |
| ADR-B-0314 | ADR 2025, 3.2.1, objaśnienie kolumny (2) | Zgodne w zakresie sprawdzonego punktu | 3.2.1 tabela A, kolumna (2), podaje nazwę i opis odpowiadające pozycji UN; nie należy dobierać nazwy wyłącznie z nazwy handlowej. |
| ADR-B-0315 | ADR 2025, 2.2.9.1.7.2; tabela A UN 3551 | Nie da się potwierdzić | Nie da się potwierdzić w tej partii: nowa pozycja UN 3551 i jej klasyfikacja wymagają bezpośredniego porównania tabeli A z pełnym brzmieniem sprostowania poz. 1575. Pozostaje otwarte. |
| ADR-B-0316 | ADR 2025, 2.2.1.1.5 (podklasa 1.1) | Zgodne w zakresie sprawdzonego punktu | 2.2.1.1.5: podklasa 1.1 oznacza zagrożenie wybuchem masowym. |
| ADR-B-0317 | ADR 2025, 2.2.7.1.1 oraz 2.2.7.2.2.1–2.2.7.2.2.6 | Nie da się potwierdzić | Nie da się potwierdzić bez dokładnego sprawdzenia kryteriów klasy 7 i tabel wartości z 2.2.7.2.2; pozostaje do decyzji specjalisty. |
| ADR-B-0318 | ADR 2025, 2.1.3.5.5 | Nie da się potwierdzić | Nie da się potwierdzić bez pełnego odczytania 2.1.3.5.5 oraz powiązanych wyjątków dla odpadów; nie zmieniono statusu. |
| ADR-B-0322 | ADR 2025, 8.6.3.3 i 8.6.4 w związku z 3.4.13–3.4.14 | Zgodne w zakresie sprawdzonego punktu | 8.6.4: jednostka oznakowana zgodnie z 3.4.13 podlega ograniczeniu tuneli kategorii E, z uwzględnieniem 3.4.14. |
| ADR-B-0324 | ADR 2025, 7.5.2.1 (tabela: 5.2 + 1 z 5.2) | Nie da się potwierdzić | Nie da się potwierdzić bez bezpośredniego sprawdzenia konkretnego wiersza tabeli zakazów ładowania razem 7.5.2.1 dla kombinacji 5.2 + 1. Pozostaje otwarte. |
| ADR-B-0325 | ADR 2025, 2.1.3.5.5 | Nie da się potwierdzić | Nie da się potwierdzić bez pełnego odczytania 2.1.3.5.5 i wszystkich wyjątków klasyfikacyjnych dla odpadów. |
| ADR-B-0326 | ADR 2025, 2.1.3.5.5 | Nie da się potwierdzić | Nie da się potwierdzić bez sprawdzenia, czy obecność klasy 4.3 wyklucza zastosowanie procedury uproszczonej w danym przypadku. |
| ADR-B-0327 | ADR 2025, 2.1.3.5.5 | Nie da się potwierdzić | Nie da się potwierdzić bez pełnego brzmienia warunków 2.1.3.5.5 dla UN 3077/3082 i grupy pakowania III. |
| ADR-B-0328 | ADR 2025, 2.1.3.5.5 | Nie da się potwierdzić | Nie da się potwierdzić bez pełnego brzmienia warunku wykluczającego grupę I i reguły domyślnej w 2.1.3.5.5. |
| ADR-B-0329 | ADR 2025, 2.1.3.5.5 | Nie da się potwierdzić | Nie da się potwierdzić bez pełnego sprawdzenia wyłączeń dla materiałów zakazanych w 2.1.3.5.5. |
| ADR-B-0330 | ADR 2025, 2.1.3.5.3; 2.1.3.5.5 | Nie da się potwierdzić | Nie da się potwierdzić bez pełnego sprawdzenia wyjątków 2.1.3.5.3/5.5 dla klasy 5.2. |
| ADR-B-0331 | ADR 2025, 2.1.3.5.2 | Nie da się potwierdzić | Nie da się potwierdzić bez pełnego odczytania 2.1.3.5.2 i warunków zastosowania klasyfikacji mieszanin. |
| ADR-B-0332 | ADR 2025, 2.1.3.5.3 | Nie da się potwierdzić | Nie da się potwierdzić bez pełnego odczytania tabeli pierwszeństwa zagrożeń w 2.1.3.5.3. |
| ADR-B-0333 | ADR 2025, 2.1.3.5.4 | Nie da się potwierdzić | Nie da się potwierdzić bez pełnego odczytania 2.1.3.5.4 i tabeli pierwszeństwa zagrożeń. |
| ADR-B-0335 | ADR 2025, 2.1.3.5.5 | Nie da się potwierdzić | Nie da się potwierdzić bez pełnego brzmienia 2.1.3.5.5 o wykorzystaniu danych technicznych i wiedzy nadawcy. |
| ADR-B-0336 | ADR 2025, 2.1.3.5.5 | Nie da się potwierdzić | Nie da się potwierdzić bez pełnego brzmienia 2.1.3.5.5 dotyczącego wiedzy nadawcy odpadu. |
| ADR-B-0337 | ADR 2025, 2.1.3.5.3; 2.1.3.5.5 | Nie da się potwierdzić | Nie da się potwierdzić bez sprawdzenia wyjątków dla klasy 6.2 w 2.1.3.5.3 i 2.1.3.5.5. |

## Pozycje pozostawione do decyzji specjalisty

- **ADR-B-0315:** UN 3551 i sprostowanie 2025 poz. 1575 — wymagane bezpośrednie porównanie tabeli A i przepisów dotyczących baterii sodowo-jonowych.
- **ADR-B-0317:** kryteria klasy 7 i wartości z 2.2.7.2.2 wymagają dokładnego odczytu.
- **ADR-B-0318, ADR-B-0325–ADR-B-0333, ADR-B-0335–ADR-B-0337:** wymagają pełnego porównania szczegółowych reguł i wyjątków 2.1.3.5.2–2.1.3.5.5 dla odpadów i mieszanin; nie oznaczono ich jako zgodnych na podstawie samego ogólnego streszczenia.
- **ADR-B-0324:** wymaga sprawdzenia konkretnego wiersza tabeli zakazów ładowania razem 7.5.2.1 dla kombinacji nalepek 5.2 + 1.

## Kolejny krok

Kontynuować kolejną partią 40–50 otwartych pozycji. Nie stwierdzono potwierdzonego błędu wymagającego zmiany banku w tej partii. Niczego nie oznaczono jako `verified`.
