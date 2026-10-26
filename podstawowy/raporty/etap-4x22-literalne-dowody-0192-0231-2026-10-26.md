# Etap 4x22 — partia 0192–0231: ponowne próby źródłowe

- Data: 2026-10-26.
- Świeży punkt wyjścia `main`: `502a39482a2545d4d03ffb8146e51c49f8bed754`.
- Zakres: wyłącznie kurs podstawowy ADR; kontrola 40 rekordów ADR-B-0192–ADR-B-0231.
- Źródło wiążące: [Dz.U. 2025 poz. 642 — ELI](https://eli.gov.pl/eli/DU/2025/642/ogl) oraz [Dziennik Ustaw](https://dziennikustaw.gov.pl/DU/2025/642). Ministerialne PDF-y są wyłącznie pomocą, zgodnie z informacją MI.

## Wynik partii

- Rekordy objęte kontrolą: **40**.
- Rekordy, które już miały `literal_comparison_result`: **31**; nie nadpisywano ich wcześniejszych wyników.
- Rekordy bez wyniku urzędowego porównania na wejściu: **9**.
- Rekordy z wcześniejszym cytatem z pomocniczego PDF MI spośród otwartych: **3** (ADR-B-0201, ADR-B-0204, ADR-B-0208).
- Rekordy bez cytatu, dla których zapisano konkretną przyczynę blokady i następny krok: **6** (ADR-B-0195, ADR-B-0200, ADR-B-0202, ADR-B-0205, ADR-B-0211, ADR-B-0213).
- Strony PDF Dz.U. rzeczywiście znalezione dla tej partii: **0**.
- Potwierdzone sprzeczności z prawnie wiążącym PDF, poprawki pytań/kluczy: **0**.
- Status wszystkich pytań pozostaje `needs_review`; niczego nie oznaczono `verified`.

## Próby dostępu do Dz.U.

Bezpośrednie otwarcie [PDF ELI `text.pdf`](https://eli.gov.pl/api/acts/DU/2025/642/text.pdf) zakończyło się limitem długości treści (ponad 10 MiB). Próby otwarcia plików skanowych ELI obejmowały `D20250642-02.pdf` (timeout), `D20250642-15.pdf` (limit treści 24 MB) i `D20250642-41.pdf` (limit ponad 10 MiB). Nie ustalono, który z tych plików zawiera strony potrzebne do sprawdzanych ustępów. Nie przypisano numerów stron z pamięci ani z paginacji MI.

To jest udokumentowana blokada dostępu, a nie potwierdzenie treści przepisu. Następny krok dla każdego rekordu: ustalić zakres stron właściwego skanu Dz.U., odczytać stronę lub jej OCR i zapisać rzeczywisty numer strony PDF Dz.U.

## Rekordy otwarte — wynik i następny krok

| ID | Punkt ADR | Wynik bieżącej kontroli | Następny krok |
|---|---|---|---|
| ADR-B-0195 | 1.4.2.3.2 | Brak strony Dz.U. i brak literalnego cytatu z aktualnego tekstu urzędowego. | Odnaleźć skan części 1.4, zapisać literalny tekst i stronę Dz.U. |
| ADR-B-0200 | 7.5.7.1 | Dostępne wyszukiwanie wskazywało materiały pomocnicze/starsze; nie wystarcza to do potwierdzenia tekstu ADR 2025. | Odnaleźć skan części 7.5 i potwierdzić dokładne brzmienie reguły mocowania. |
| ADR-B-0201 | 7.5.8.2 | Cytat MI mówi o wyjątku przy ponownym załadunku tym samym materiałem; pytanie i explanation są zgodne z tym fragmentem, ale kontekst oraz strona Dz.U. pozostają niepotwierdzone. | Odczytać ustęp wraz z poprzedzającym go kontekstem na skanie Dz.U. |
| ADR-B-0202 | 7.5.1.2 | Nie uzyskano urzędowej strony z pełnym warunkiem kontroli przed załadunkiem. | Odnaleźć skan części 7.5 i sprawdzić dokumenty, oględziny oraz warunek wstrzymania załadunku. |
| ADR-B-0204 | 5.4.2 | Poprzednie pole `short_quote` było parafrazą, nie cytatem literalnym. Zastąpiono je dokładnym brzmieniem znalezionym w pomocniczym tekście MI; Dz.U. nadal niepotwierdzone. | Porównać z urzędowym skanem Dz.U. i zanotować rzeczywistą stronę. |
| ADR-B-0205 | 1.1.4.2; 1.1.4.3 | Nie znaleziono właściwej strony urzędowego PDF dla warunków przewozu łączonego. Nie użyto tekstu RID jako zamiennika ADR. | Ustalić plik i stronę dla działu 1.1, odczytać warunki ADR 2025. |
| ADR-B-0208 | 8.6.3.1; 8.6.4 | Cytat MI wskazuje kolumnę 15 tabeli A jako miejsce kodu tunelowego; zgodność pytania w tym zakresie nie jest urzędowym porównaniem. | Odnaleźć skan Dz.U. dla części 8.6 i zapisać stronę PDF. |
| ADR-B-0211 | 1.10.1.2 | Wyniki wyszukiwania zwracały również starsze teksty; nie użyto ich jako dowodu dla edycji 2025. | Odczytać dział 1.10 w skanie Dz.U. 2025 poz. 642. |
| ADR-B-0213 | 1.10.3.3 | Znalezione fragmenty obejmowały RID lub wcześniejsze edycje; brak urzędowego potwierdzenia ADR 2025. | Odczytać punkt 1.10.3.3 ze skanu Dz.U. 2025 poz. 642. |

## Korekta cytatu pomocniczego — ADR-B-0204

W ledgerze zapisano wcześniej skróconą treść jako `short_quote`. Zastąpiono ją tekstem znalezionym w pomocniczym PDF MI (nie źródle wiążącym):

> Jeżeli przewóz towarów niebezpiecznych znajdujących się w kontenerze dokonywany jest bezpośrednio przed przewozem morskim, certyfikat pakowania kontenera/pojazdu zgodny z przepisami rozdziału 5.4.2 Kodeksu IMDG,⁵,⁹ powinien być dostarczony przewoźnikowi morskiemu przez odpowiedzialnych za pakowanie kontenera.

Źródło pomocnicze: [MI, ADR 2025, fragment 5.4.2](https://www.gov.pl/attachment/b4638c72-30e3-4bff-afd1-1b9ba4100e70). Nie zapisano numeru strony, ponieważ nie został bezpośrednio potwierdzony w tym pobraniu. Pytanie ADR-B-0204 nie zostało zmienione: odpowiedź B jest zgodna z przytoczonym fragmentem w zakresie odpowiedzialności osób pakujących, ale pełna kontrola warunków i tekstu Dz.U. nadal jest otwarta.

## Status zakresu i dalsza praca

Pełny zakres 0192–0609 obejmuje 276 rekordów bez wyniku urzędowego porównania; ta partia zapisuje nowe próby dla pierwszych 9 otwartych rekordów w przedziale 0192–0231. Nie zmniejsza to liczby rekordów wymagających rzeczywistego porównania z Dz.U. Następna partia ma objąć kolejne ID i kontynuować próby, bez deklarowania sukcesu na podstawie samych materiałów MI.

Nie zmieniono pytań, odpowiedzi, explanation ani kluczy egzaminu. Wskaźniki banku nie zmieniają się; statusy pozostają `needs_review`.
