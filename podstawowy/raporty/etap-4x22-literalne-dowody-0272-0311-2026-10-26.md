# Etap 4x22 — partia 0272–0311: próby źródłowe i kontrola cytatu

- Data: 2026-10-26.
- Świeży punkt wyjścia `main`: `07b79ea6c693aa4bd4057093390e0d6ba7c6f78c`.
- Zakres: 40 rekordów ADR-B-0272–ADR-B-0311, wyłącznie kurs podstawowy.
- Źródło wiążące: [Dz.U. 2025 poz. 642 — ELI](https://eli.gov.pl/eli/DU/2025/642/ogl) i [Dziennik Ustaw](https://dziennikustaw.gov.pl/DU/2025/642).

## Wynik

- Rekordy sprawdzone: **40**.
- Rekordy z wcześniejszym wynikiem porównania: **30**.
- Rekordy bez wyniku urzędowego porównania: **10**.
- Otwarty rekord z cytatem pomocniczym MI: **2** (ADR-B-0278 i ADR-B-0300); pozostałe **8** bez cytatu.
- Strony PDF Dz.U. rzeczywiście potwierdzone: **0**.
- Potwierdzone sprzeczności z tekstem wiążącym / zmiany pytań i kluczy: **0**; nie jest to potwierdzenie poprawności, bo strona Dz.U. nadal nie została odczytana.
- Status: wszystkie pytania `needs_review`, `verified`: 0.

## Próby źródłowe i następne kroki

| ID | Punkt ADR | Stan | Następny krok |
|---|---|---|---|
| ADR-B-0275 | 1.10.2.3 | Nie uzyskano strony urzędowej dla szkolenia ochronnego przy zatrudnieniu i szkoleniu okresowym. | Odczytać dział 1.10 w skanie Dz.U. i zanotować stronę. |
| ADR-B-0278 | 5.4.2; IMDG 5.4.2.4 | Poprzednie pole `short_quote` było parafrazą. Zastąpiono je dokładnym brzmieniem znalezionym w pomocniczym tekście MI. Strona Dz.U. nadal nieznana. | Porównać 5.4.2.4 z urzędowym skanem i ustalić, czy opcja egzaminacyjna powinna używać angielskiej czy polskiej formuły. |
| ADR-B-0286 | 7.5.1.5 | Brak strony urzędowej dla strzałek kierunkowych. | Odczytać 7.5.1.5 wraz z uwagą o cieczach i ciałach stałych. |
| ADR-B-0290 | 1.4.3.2 | Brak literalnego tekstu urzędowego o obowiązkach pakującego. | Odczytać 1.4.3.2 ze skanu Dz.U. 2025. |
| ADR-B-0292 | 7.3.1.1; tabela A kol. 10 i 17 | Brak strony urzędowej dla warunków przewozu luzem. | Odczytać punkt 7.3.1.1 i właściwe kolumny tabeli A. |
| ADR-B-0300 | 1.10.1.4 | Cytat MI o dokumencie tożsamości ze zdjęciem bez potwierdzonej strony Dz.U. | Odczytać 1.10.1.4 ze skanu urzędowego i zapisać stronę. |
| ADR-B-0301 | 8.2.1.1 | Brak strony urzędowej dla wymogu kursu i egzaminu kierowcy. | Odczytać 8.2.1.1 z części 8.2 Dz.U. 2025. |
| ADR-B-0304 | 1.10.3.2.2(a) | Brak literalnego tekstu o podziale odpowiedzialności w planie ochrony. | Odczytać 1.10.3.2.2(a) i zanotować stronę Dz.U. |
| ADR-B-0305 | 1.10.3.3 | Brak strony urzędowej dla wymogu zabezpieczeń przed kradzieżą. | Odczytać 1.10.3.3; nie używać tekstu RID jako zamiennika. |
| ADR-B-0310 | 8.4.1; tabela A kol. 19 | Brak pełnej kolejności miejsc postoju i warunków nadzoru ze źródła wiążącego. | Odczytać 8.4.1 oraz właściwy wpis kolumny 19 tabeli A. |

## Korekta cytatu pomocniczego — ADR-B-0278

W ledgerze wcześniejsze `short_quote` było ogólną parafrazą, która nie odzwierciedlała szczegółowej sytuacji pytania o elektroniczny certyfikat i późniejszy dokument papierowy. Zastąpiono je literalnym tekstem znalezionym w pomocniczym PDF MI:

> Jeżeli informacje dotyczące towarów niebezpiecznych przekazywane są przewoźnikowi przy użyciu technik elektronicznego przetwarzania danych (EDP) lub elektronicznej wymiany danych (EDI), a następnie towary niebezpieczne dostarczane są przewoźnikowi, który wymaga dokumentu przewozowego w formie papierowej, to przewoźnik ten powinien zapewnić, aby dokument w formie papierowej zawierał zapis „Oryginał otrzymano drogą elektroniczną” i nazwisko osoby upoważnionej pisane wielkimi literami.

Źródło pomocnicze: [MI, ADR 2025, fragment 5.4.2.4](https://www.gov.pl/attachment/b4638c72-30e3-4bff-afd1-1b9ba4100e70). Numeru strony nie wpisano, ponieważ nie został bezpośrednio potwierdzony w tym pobraniu. **Nie zmieniono pytania ani klucza**: wymaga ono literalnego porównania z tekstem ogłoszonym i niezależnego odbioru specjalisty, zwłaszcza w zakresie formuły językowej.

## Status ogólny

W całym ledgerze nadal **318** rekordów nie ma wyniku literalnego porównania z urzędowym tekstem. W tej partii zapisano ślad dla 10 otwartych rekordów, lecz nie odnaleziono strony Dz.U., więc licznik urzędowo porównanych rekordów nie rośnie. Bank i klucze pozostały bez zmian; statusy `needs_review`. Nie przypisano stron na podstawie paginacji MI.
