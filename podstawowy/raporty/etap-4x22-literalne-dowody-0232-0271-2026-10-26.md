# Etap 4x22 — partia 0232–0271: ponowne próby źródłowe

- Data: 2026-10-26.
- Świeży punkt wyjścia `main`: `463c94d720d7fca71540895612bb8b9f396095c1`.
- Zakres: 40 rekordów ADR-B-0232–ADR-B-0271, wyłącznie kurs podstawowy.
- Źródło wiążące: [Dz.U. 2025 poz. 642 — ELI](https://eli.gov.pl/eli/DU/2025/642/ogl) i [Dziennik Ustaw](https://dziennikustaw.gov.pl/DU/2025/642). Kopie MI są wyłącznie pomocnicze.

## Wynik

- Rekordy sprawdzone: **40**.
- Rekordy z wcześniejszym `literal_comparison_result`: **29**.
- Rekordy bez wyniku urzędowego porównania: **11**.
- Wśród otwartych: cytat pomocniczy MI istnieje dla **3** (ADR-B-0237, 0240, 0247); bez cytatu w ledgerze pozostaje **8**.
- Strony PDF Dz.U. znalezione i potwierdzone: **0**.
- Potwierdzone rozbieżności z tekstem wiążącym / zmiany pytań lub kluczy: **0**. Nie oznacza to zgodności prawnej — porównanie urzędowe pozostaje otwarte.
- Statusy: `needs_review`; `verified`: 0.

## Próba źródłowa i blokada

Ponowiono próbę dotarcia do oficjalnego tekstu. Pełny PDF ELI przekracza limit odczytu; pliki skanowe zwracają timeout lub limit treści. Wyszukiwanie klauzul zwracało także starsze wydania i teksty innych gałęzi transportu, które celowo nie zostały użyte jako dowód dla ADR 2025. Nie przypisano stron z paginacji MI.

| ID | Punkt ADR | Stan dowodu | Następny krok |
|---|---|---|---|
| ADR-B-0235 | 7.5.7.1 | Brak literalnego tekstu ze strony Dz.U.; dostępne wyniki były pomocnicze/starsze. | Odnaleźć urzędowy skan części 7.5 i zapisać stronę. |
| ADR-B-0236 | 7.5.7.1 | Brak literalnego tekstu ze źródła wiążącego; nie przenoszono cytatu z wcześniejszych edycji. | Odczytać 7.5.7.1 z Dz.U. 2025 i porównać z odpowiedzią oraz explanation. |
| ADR-B-0237 | 7.5.7.2 | Cytat MI istnieje, ale strona Dz.U. nieustalona. | Odnaleźć skan i potwierdzić warunek piętrzenia. |
| ADR-B-0239 | 7.5.1.2 | Brak strony Dz.U. z pełnym warunkiem kontroli przed załadunkiem. | Odczytać cały punkt 7.5.1.2 i zapisać stronę. |
| ADR-B-0240 | 7.5.8.2 | Cytat MI wskazuje wyjątek dla tego samego materiału, ale nie potwierdzono strony Dz.U. | Odczytać skan wraz z kontekstem przepisu. |
| ADR-B-0245 | 1.4.3.1.1(b) | Brak literalnego tekstu urzędowego dla obowiązku załadowcy przy uszkodzonym opakowaniu. | Odczytać dział 1.4, podpunkt 1.4.3.1.1(b). |
| ADR-B-0246 | 1.4.2.3.1 | Brak strony Dz.U.; starsze teksty nie potwierdzają edycji 2025. | Odczytać punkt 1.4.2.3.1 ze skanu Dz.U. |
| ADR-B-0247 | 1.1.4.2.1 | Cytat MI istnieje, lecz urzędowa strona i pełne warunki wyjątku pozostają niepotwierdzone. | Odczytać punkt 1.1.4.2.1 w skanie Dz.U. i zapisać stronę. |
| ADR-B-0249 | 1.10.1.2 | Brak strony Dz.U.; wyniki obejmowały starsze akty. | Odczytać dział 1.10 z edycji 2025. |
| ADR-B-0262 | 1.9.5.3.6; 8.6.4 | Brak strony urzędowej dla kategorii tunelu E. | Odczytać oba punkty ze skanów Dz.U. 2025 i sprawdzić wyjątki. |
| ADR-B-0263 | 8.6.3.2 | Znaleziono tylko tekst z wcześniejszej edycji, nieużyty jako dowód ADR 2025. | Odczytać punkt 8.6.3.2 ze skanu Dz.U. i zanotować stronę. |

## Zakres pozostały

Po tej partii nadal **318** rekordów w całym ledgerze nie ma literalnego wyniku porównania z urzędowym tekstem. Ta partia nie zmniejsza tej liczby, bo dla żadnego rekordu nie udało się potwierdzić strony PDF Dz.U. Dla kolejnych partii należy kontynuować identyfikację właściwych skanów, a jeśli pobranie nadal nie jest możliwe — zapisywać indywidualny powód i następny krok zamiast zgadywać cytat lub stronę.

Bank, odpowiedzi i klucze nie zostały zmienione. Wskaźniki banku pozostają: 609 pytań, 0 duplikatów ID, 0 `verified`; poprawna odpowiedź jest jedyną najdłuższą w 11,99% pytań globalnie, każdy dział ≤16%; 0 explanation poniżej 200 znaków.
