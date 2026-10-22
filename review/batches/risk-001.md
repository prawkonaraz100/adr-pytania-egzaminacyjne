# ADR podstawowy — audyt ryzyka, partia 001 (30 pytań)

**Data:** 23.10.2026. **Zakres:** 30 pytań wybranych wg ryzyka błędnego zrozumienia ADR (zwolnienia, gaśnice, dokumenty, klasy 7, odpady, tunele, przewóz luzem, odstępstwa).  
**Status:** **WSTĘPNA KONTROLA REDAKCYJNO-ŹRÓDŁOWA, NIE ZATWIERDZENIE EKSPERCKIE.** Wszystkie 30 pytań nadal mają `needs_review`, żadne nie jest dopuszczone do publikacji.

## Potwierdzony rezultat i ograniczenia

- Przeczytano komplet treści, wszystkie trzy opcje odpowiedzi, klucze, wyjaśnienia i wskazane ustępy z istniejącej bazy.
- Porównano wskazane przepisy z udostępnionymi fragmentami **wydania ADR 2025** (UNECE / pomocnicze pełne tomy), źródłami organów i wybranymi krajowymi objaśnieniami. To kontrola wstępna, nie indywidualny protokół pełnego porównania każdego przepisu z polskim Dz.U.
- **19/30** — nie wykryto sprzeczności w sprawdzonym zakresie, ale trzeba przeprowadzić pełne porównanie prawne i fachową ocenę wszystkich opcji.
- **8/30** — wykryto potrzebę korekty treści/wyjaśnienia/podstawy, wykonano zmiany w JSONL, nadal do recenzji. Szczególnie `ADR-B-0073` miało **dwa dopuszczalne warianty** (gaśnica 2 kg i 6 kg). Doprecyzowano pytanie o *minimum*.
- **3/30** — wymagają odrębnego sprawdzenia dokładnej polskiej formuły (`0061`, `0209`) lub szczegółowego zastosowania wyjątku M364 (`0145`). To nie znaczy, że pozostałe 27 są „zatwierdzone”.
- **0/30** — faktycznie ocenione i podpisane przez niezależnego specjalistę ADR.

## Zestawienie dla redaktora i recenzenta

| Pytanie | Punkt prawa | Wstępny rezultat | Uzasadnienie / zaobserwowana kwestia | Następne sprawdzenie |
|---|---|---|---|---|
| [ADR-B-0002](../../podstawowy/questions.jsonl) | 1.1.3 | Wstępnie spójne | Różne wyłączenia mają różne warunki; mała ilość nie uchyla wszystkich wymagań | Zidentyfikować konkretną podstawę wyłączenia dla przykładowego przewozu |
| [ADR-B-0008](../../podstawowy/questions.jsonl) | 5.4.1.1.3.1 | Poprawiono | Wskazano w treści ograniczenie: odpad inny niż promieniotwórczy | Sprawdzić rzeczywistą polską formułę i zastrzeżenie 2.1.3.5.5 |
| [ADR-B-0009](../../podstawowy/questions.jsonl) | 7.5.8.1 | Wstępnie spójne | Czyszczenie po wycieku ze sztuki przesyłki przed kolejnym załadunkiem | Utrzymać rozróżnienie od wyjątku dla przewozu luzem 7.5.8.2 |
| [ADR-B-0010](../../podstawowy/questions.jsonl) | 8.3.5 i 7.5.9 | Wstępnie spójne | Zakaz palenia obejmuje e-papierosy w opisanych czynnościach | Sprawdzić brzmienie obu przepisów i zakres miejsca pracy |
| [ADR-B-0017](../../podstawowy/questions.jsonl) | 5.3.2.3.1 | Wstępnie spójne | X oznacza niebezpieczną reakcję z wodą; woda wyłącznie za zgodą specjalistów | Zachować zastrzeżenie ograniczonego uprawnienia do użycia wody |
| [ADR-B-0022](../../podstawowy/questions.jsonl) | 8.1.4.1 | Wstępnie spójne | DMC powyżej 7,5 t: co najmniej 12 kg łącznie oraz szczegółowe minima gaśnic | Nie mylić minimum łącznego z pojemnością każdej gaśnicy |
| [ADR-B-0023](../../podstawowy/questions.jsonl) | 8.1.5.2 | Wstępnie spójne | Klin pod koła na każdy pojazd jednostki transportowej, odpowiednio dobrany | Rozróżnić wyposażenie pojazdu i członka załogi |
| [ADR-B-0024](../../podstawowy/questions.jsonl) | 8.1.5.2 | Wstępnie spójne | Rękawice ochronne dla każdego członka załogi | Sprawdzić także ochronę oczu, kamizelkę i latarkę |
| [ADR-B-0032](../../podstawowy/questions.jsonl) | 8.6.4 | Wstępnie spójne | Kod E: zakaz tunelu kategorii E dla przewozu podlegającego ograniczeniom | Sprawdzić wyjątki i inne znaki drogowe |
| [ADR-B-0033](../../podstawowy/questions.jsonl) | 8.6.4 | Poprawiono | D/E w sztukach przesyłek: E; nie utożsamiać z cysterną lub luzem | Poprawiono odmianę 'sztuki przesyłek'; dodać przykład multimodalny w lekcji |
| [ADR-B-0037](../../podstawowy/questions.jsonl) | 5.4.1.1.1(a) | Wstępnie spójne | Numer czterocyfrowy z literami UN w dokumencie przewozowym | Zweryfikować wymagany porządek opisu ADR i wersję polską |
| [ADR-B-0061](../../podstawowy/questions.jsonl) | 5.4.1.1.7 | Sprawdzić polski tekst | Odpowiedni dodatkowy wpis obowiązuje tylko przy 1.1.4.2.1 | Sprawdzić dokładne brzmienie polskiej wymaganej wzmianki w urzędowym tekście |
| [ADR-B-0064](../../podstawowy/questions.jsonl) | 8.6.3.2 | Wstępnie spójne | Najbardziej restrykcyjny kod przy ładunku mieszanym | Odróżnić towary pomijane przy ustalaniu kodu zgodnie z 8.6.3.3 |
| [ADR-B-0071](../../podstawowy/questions.jsonl) | 8.1.4.1 | Wstępnie spójne | DMC 3,5 t: dwie gaśnice, minimum 4 kg łącznie | W odpowiedzi nie mylić pojemności jednej i sumarycznej |
| [ADR-B-0072](../../podstawowy/questions.jsonl) | 8.1.4.1 | Wstępnie spójne | DMC 6 t: minimum 8 kg łącznie, przynajmniej jedna 6 kg i jedna 2 kg | Warto nauczyć dodatkowego minimum indywidualnego |
| [ADR-B-0073](../../podstawowy/questions.jsonl) | 8.1.4.2 | Poprawiono | Były dwie dopuszczalne odpowiedzi (2 kg i 6 kg); poprawiono na wymagane minimum | Sprawdzić nową treść, trzy opcje i równoważną skuteczność innego środka |
| [ADR-B-0077](../../podstawowy/questions.jsonl) | 8.1.5.3 | Wstępnie spójne | Maska ucieczkowa dla 2.3 i 6.1 | Nie utożsamiać maski ucieczkowej ze sprzętem do pracy w skażonej strefie |
| [ADR-B-0085](../../podstawowy/questions.jsonl) | 8.6.3.3; 3.4.13-3.4.14 | Poprawiono | Warunkowe wyłączenie z ograniczeń tunelowych; wydobyto wyjątek LQ do treści | Prawnie skontrolować kombinacje 1.1.3/3.4 i oznakowanie całej jednostki |
| [ADR-B-0091](../../podstawowy/questions.jsonl) | 1.1.3.1(a) | Wstępnie spójne | Przewóz handlowy na odsprzedaż nie jest automatycznie wyłączeniem osób prywatnych | Dodać w lekcji warunek pakowania do sprzedaży detalicznej i celu prywatnego |
| [ADR-B-0093](../../podstawowy/questions.jsonl) | 1.1.3.6; 3.4 | Wstępnie spójne | Wyjątki transport-category i LQ to różne mechanizmy | Nie sugerować sumowania LQ według punktów 1.1.3.6 |
| [ADR-B-0129](../../podstawowy/questions.jsonl) | 2.1.3.5.5 | Poprawiono | Zbyt krótkie wyjaśnienie; dodano zasadę wysokiego zagrożenia i ściśle ograniczone PG II/III | Konieczna specjalistyczna recenzja odpadów i zakazanych wyjątków z ustępu |
| [ADR-B-0131](../../podstawowy/questions.jsonl) | 8.4.1; 8.5; tab. A kol. 19 | Wstępnie spójne | Obowiązek nadzoru wynika z konkretnych przepisów szczególnych i ilości | Ujęcie MEMU z 8.4.2 i zasady S1(6), S14–S24 jako odrębne przypadki |
| [ADR-B-0139](../../podstawowy/questions.jsonl) | 7.3.1.1; tabela A kol. 10 i 17 | Poprawiono | Był zbyt wąski wariant BK/VC; dodano alternatywne wyraźne odesłanie do przepisu | Sprawdzić obowiązujące warunki 7.3.2/7.3.3 i puste nieoczyszczone opakowania |
| [ADR-B-0140](../../podstawowy/questions.jsonl) | 5.4.2 | Poprawiono | Zbyt szerokie 'kontener ADR'; wyraźnie wyłączono kontener-cysternę ze scenariusza | Skontrolować wyjątki IMDG, MEGC i możliwość łączenia dokumentów |
| [ADR-B-0145](../../podstawowy/questions.jsonl) | 8.1.2.2(a); M364 | Sprawdzić wyjątek z ekspertem | Ogólna zasada kabiny dla pojazdu silnikowego; M364 ograniczony wyjątek dla naczepy | Sprawdzić ważność M364, państwa trasy, dokładne kryteria naczepy |
| [ADR-B-0160](../../podstawowy/questions.jsonl) | 8.2.1.4; 8.5 S12 | Poprawiono | Uzupełniono odniesienie do S12 dla określonych zwolnień klasy 7 | Sprawdzić szczegółowe kryteria S12 i polski tekst aktualny |
| [ADR-B-0171](../../podstawowy/questions.jsonl) | 8.1.5.3 | Wstępnie spójne | Maska ucieczkowa przy nalepce 6.1 (i 2.3) | Zwrócić uwagę na przeznaczenie sprzętu wyłącznie do ewakuacji |
| [ADR-B-0197](../../podstawowy/questions.jsonl) | 8.1.4.2 | Wstępnie spójne | Zgodność innego odpowiedniego środka przy równoważnej skuteczności do 2 kg proszku | Nie używać masy całej gaśnicy jako ekwiwalentu skuteczności |
| [ADR-B-0201](../../podstawowy/questions.jsonl) | 7.5.8.2 | Wstępnie spójne | Przewóz luzem — wyjątek czyszczenia przed ponownym załadunkiem tego samego towaru | Nie przenosić wyjątku na wycieki po sztukach przesyłek 7.5.8.1 |
| [ADR-B-0209](../../podstawowy/questions.jsonl) | 8.6.3.3; 8.6.4; 3.4.13-3.4.14 | Sprawdzić polski tekst | Wyraźnie warunkowe oznakowanie LQ powoduje ograniczenie E | Porównać wymagania znaku LQ, ilości i ograniczenie tunelowe z polskim ADR |

## Wykonane poprawki w banku

| ID | Zmiana | Powód |
|---|---|---|
| `ADR-B-0008` | Wskazano, że chodzi o odpad inny niż promieniotwórczy; dopisano wyjątek 2.1.3.5.5 | Słowo „ODPAD” w 5.4.1.1.3.1 ma ograniczony zakres |
| `ADR-B-0033` | Poprawiono nazwę sposobu przewozu na „sztuki przesyłek” | Usunięcie niepoprawnej formy językowej |
| `ADR-B-0073` | Zmieniono pytanie o „co najmniej 2 kg” na pytanie o **minimalną wymaganą pojemność** | Wcześniej 6 kg także spełniało warunek, więc obie odpowiedzi były prawdziwe |
| `ADR-B-0085` | Wprost określono warunek braku oznakowania LQ z 3.4.13 i 3.4.14 | Ograniczenia tunelowe z 8.6.3.3 są warunkowe |
| `ADR-B-0129` | Rozszerzono opis wyjątków przy odpadach i wątpliwościach klasyfikacyjnych | Nie wolno automatycznie przyjmować grupy pakowania III |
| `ADR-B-0139` | W opcji poprawnej uwzględniono również **wyraźne odesłanie do określonego punktu ADR** w kolumnie 10/17, nie tylko BK/VC | Wynika z 7.3.1.1 i ma znaczenie przy dopuszczalności przewozu luzem |
| `ADR-B-0140` | Zawężono do zwykłego kontenera z opakowanymi przesyłkami, wyłączając kontener-cysternę | 5.4.2 zawiera wyjątki w zakresie certyfikatu pakowania |
| `ADR-B-0160` | Dodano odniesienie do przepisów szczególnych S12, gdy stosowne | Kurs podstawowy nie zawsze wystarczy dla klasy 7, ale występują odstępstwa |

**Klucze poprawnych odpowiedzi pozostały bez zmian.** Nie nadano `verified` ani wpisów do `review/approvals.jsonl`.

## Dlaczego NIE oznaczamy tych pytań jako zweryfikowane?

1. Nie przeprowadzono pełnego porównania **każdego zdania i wariantu** z prawnie wiążącym tekstem polskim Dz.U. 2025 poz. 642 ze sprostowaniem poz. 1575.
2. Nie sprawdzono w całości wszystkich przepisów szczególnych i wyjątków dla transportu w wybranych sytuacjach (np. S12, M364, 7.3.1.1).
3. Nie ma rzeczywistej niezależnej recenzji zawodowego specjalisty ADR ani jego dokumentu potwierdzającego ocenę.
4. Pytania nadal mogą mieć dydaktyczne wady niezależne od zgodności formalnej: oczywiste dystraktory, powtórzenia znaczeniowe lub niewłaściwy poziom trudności.

## Przed następną partią

- Najpierw recenzja wysokiego ryzyka: `0073`, `0139`, `0140`, `0129`, `0209`, `0145`, `0160`, `0061`.
- Dla każdego pytania recenzent powinien odpowiedzieć **osobno**: czy A jest błędne/prawdziwe w danych warunkach, czy B jest błędne/prawdziwe i czy C jest błędne/prawdziwe, z podaniem dokładnego punktu ADR.
- Sprawdzić aktualne umowy wielostronne i sygnatariuszy na konkretnej trasie, w razie potrzeby opracować przykład odrębnie dla przewozu krajowego i międzynarodowego.
- Jeśli recenzent odrzuci pytanie, pozostawić `needs_review` albo zastosować istniejący status blokujący zgodnie ze schematem; **nie generować fikcyjnego protokołu pozytywnego**.

## Użyte źródła

- [UNECE: oficjalne wydanie ADR 2025](https://unece.org/adr-2025-files)
- [ADR 2025, tom I — tekst angielski](https://www.euraca.eu/media/ewof3ibp/adr-2025-vol-i.pdf)
- [ADR 2025, tom II — tekst angielski](https://www.euraca.eu/media/frmeo2lm/adr-2025-vol-ii.pdf)
- [Ministerstwo Infrastruktury — polskie tomy pomocnicze](https://www.gov.pl/web/infrastruktura/towary-niebezpieczne)
- [Dz.U. 2025 poz. 642 — oficjalny polski tekst](https://dziennikustaw.gov.pl/DU/2025/642)
- [Sprostowanie, Dz.U. 2025 poz. 1575](https://eli.gov.pl/eli/DU/2025/1575/ogl/pol/pdf)
- [UNECE: umowy wielostronne](https://unece.org/transport/road-transport/adr-multilateral-agreements)
- [Rejestr odstępstw projektu](../../docs/ODSTEPSTWA-ADR-2026.md)

`risk-001.json` obok tego dokumentu jest źródłem maszynowym, które można sprawdzić w CI. **Rozstrzygnięcie fachowca wymagane przed publikacją.**
