# Etap 4x22 — audyt sprostowania Dz.U. 2025 poz. 1575

## Zakres i źródła

Przeanalizowano całe obwieszczenie o sprostowaniu błędów opublikowane w Dz.U. 2025 poz. 1575 oraz przeskanowano wszystkie 609 rekordów banku `podstawowy/questions.jsonl` i 609 rekordów ledgeru `review/legal-polish/stage4w4-literal-verification-ledger-0001-0609.json`. Sprawdzono pola podstawy prawnej, treść pytania, odpowiedzi i explanation dla bezpośrednich trafień.

- **Źródło prawnie wiążące dla sprostowania:** [Dz.U. 2025 poz. 1575 — oficjalny PDF](https://eli.gov.pl/api/acts/DU/2025/1575/text.pdf), 3 strony.
- **ADR bazowy:** [Dz.U. 2025 poz. 642](https://dziennikustaw.gov.pl/DU/2025/642).
- **Kopia robocza MI:** [ADR 2025 tom I PL](https://www.gov.pl/attachment/8856b22a-bfd8-4567-8386-b9709bba8da7). Ministerstwo zastrzega, że kopie mają charakter pomocniczy; nie zastępują tekstu ogłoszonego w Dzienniku Ustaw.

## Pełna lista korekt z poz. 1575

| Punkt ADR | Treść sprostowania |
|---|---|
| Załącznik A, 1.8.5.3 lit. (b) | „leczenia szpitalnego” → „pobytu w szpitalu” |
| Załącznik A, 1.8.6.2.1 | Zastąpiono cały przepis o akredytacji jednostek inspekcyjnych; dla zadań ogólnych typ A, dla okresowych badań naczyń ciśnieniowych działu 6.2 typ A lub B; akredytacja obejmuje zatwierdzenie |
| Załącznik A, 2.2.9.3, pozycja UN 3508 | Nazwa: „KONDENSATOR ASYMETRYCZNY (o pojemności magazynowanej energii większej niż 0,3 Wh)” |
| Załącznik A, 3.2.1, tabela A, objaśnienie kolumny 12 | „dopuszczenia” → „zatwierdzenia” w akapicie szóstym |
| Załącznik A, 3.2.1, tabela A, dodane po UN 0514 | Dodano pozycje UN 1001 ACETYLEN ROZPUSZCZONY i UN 1002 POWIETRZE SPRĘŻONE |
| Załącznik A, 3.2.1, tabela A, UN 1010 | Nazwa angielska: próg „more than 40% butadienes” → „more than 20% butadienes” |
| Załącznik A, 3.2.1, tabela A, UN 1835 (pierwszy wiersz) | Nazwa doprecyzowana: roztwór wodny w zakresie powyżej 2,5% i poniżej 25% |
| Załącznik A, 3.2.1, tabela A, UN 1835 (drugi wiersz) | Nazwa doprecyzowana: roztwór wodny o stężeniu nie większym niż 2,5% |
| Załącznik A, 3.2.1, tabela A, UN 3550 | „DIWODREK” → „DIWODROTLENEK” |
| Załącznik A, 3.2.1, tabela A, UN 3551 | „organicz” → „organiczny” |
| Załącznik A, 3.2.1, tabela A, UN 3554 | „GAL ZAWARTY W PRZEDMIOTACH” → „GAL ZAWARTY W PRZEDMIOTACH PRZEMYSŁOWYCH” |
| Załącznik A, 3.4.1 lit. (d) | „to” → „do” |
| Załącznik A, 6.8.2.1.20 lit. (b) pkt 1 | Doprecyzowano, że chodzi o „elementy wzmacniające obejmujące przegrody, falochrony, pierścienie zewnętrzne lub wewnętrzne” |
| Załącznik A, 7.3.3.2.7, AP11 | Terminologia kadzi: „okładzina” → „wykładzina”; „kontrole” → „badania”; „kontrole i badania” → „badania i próby”; „kontrola wstępna/okresowa” → „badanie odbiorcze/okresowe”; „szczelność” → „integralność”; zmiany oznakowania i ustawienia otworów do opróżniania |
| Załącznik A, 7.4.1 | Odwołanie „9.7.2” → „9.7” |
| Załącznik A, 7.5.11, CV24 | „układania” → „układaniu” |
| Załącznik B, 8.2.2.7.2.3 | „10 pytań” → „15 pytań” |

Źródło listy: Dz.U. 2025 poz. 1575, strony 1–3 (PDF strony 1–3). Lista obejmuje wszystkie punkty wskazane w obwieszczeniu, także korekty terminologiczne i odwołania, które nie zmieniają merytorycznej odpowiedzi kursanta.

## Wynik porównania z bankiem i ledgerem

- Rekordy banku przejrzane skryptem: **609/609**.
- Rekordy ledgeru przejrzane skryptem: **609/609**.
- Bezpośrednie pytania odnoszące się do poprawionej pozycji UN 3551 lub wymieniające ją w podstawie: **4** — ADR-B-0162, ADR-B-0315, ADR-B-0499 i ADR-B-0501.
- Potwierdzone sprzeczności wymagające zmiany pytania/odpowiedzi/explanation: **0**.
- Poprawki w banku: **0**.
- Statusy: pozostają `needs_review`; **nie ustawiono żadnego `verified`**.

### Pytania związane z UN 3551

| ID | Zakres | Wynik porównania ze sprostowaniem |
|---|---|---|
| ADR-B-0162 | UN 3551/3552 w podstawie; pytanie o nalepkę 9A | Brak sprzeczności widocznej w pytaniu, odpowiedziach ani explanation. Sprostowanie poprawia brzmienie nazwy pozycji UN 3551, nie zmienia wskazanej w pytaniu klasy/nalepki. |
| ADR-B-0315 | Tabela A, UN 3551 | Brak sprzeczności: pytanie mówi o bateriach sodowo-jonowych z elektrolitem organicznym, a sprostowanie poprawia zapis „organiczny” w nazwie pozycji. Klasa 9 nie jest zmieniana w sprostowaniu. |
| ADR-B-0499 | Tabela A, UN 3551/3552 | Brak sprzeczności widocznej: rozróżnienie UN 3551/3552 w pytaniu dotyczy sposobu przewozu; sprostowanie koryguje nazwę pozycji, nie tę regułę. Wymaga nadal niezależnej recenzji specjalisty. |
| ADR-B-0501 | 2.2.9.1.7.2(c), wzmianka UN 3551 | Brak bezpośredniego związku z korektą nazwy w tabeli A; warunek ochrony przed zwarciem wynika z 2.2.9.1.7.2(c). Nie stwierdzono sprzeczności z samym sprostowaniem. |

Pytania o ogólną strukturę tabeli A (np. kolumny 1, 3a, 7a, 15) nie odnoszą się do wierszy zmienionych sprostowaniem i nie zostały uznane za objęte korektą wyłącznie dlatego, że cytują ogólnie 3.2.1. W wyszukiwaniu pól podstawy nie znaleziono pytań odnoszących się bezpośrednio do 1.8.5.3, 1.8.6.2.1, UN 3508, UN 1001/1002, UN 1010, UN 1835, UN 3550, UN 3554, 3.4.1 lit. (d), 6.8.2.1.20, 7.3.3.2.7 AP11, 7.4.1, 7.5.11 CV24 ani 8.2.2.7.2.3.

## Ważne rozróżnienie

Brak wykrytej sprzeczności z treścią sprostowania **nie jest równoznaczny z pełną weryfikacją prawną pytania**. Nadal wymagane jest literalne porównanie z konkretnym plikiem i stroną Dz.U. 2025 poz. 642 oraz niezależny przegląd specjalisty, w tym audyt wszystkich opcji A/B/C. Obecny ledger pokazuje, że dla znacznej części rekordów dokładny fragment prawnie wiążącego PDF nie został jeszcze zapisany. Nie uzupełniano cytatów na podstawie domysłu.

## Ograniczenia i dalsze działanie

Sprostowanie identyfikuje zmiany w polskim tekście ADR; część z nich dotyczy nomenklatury technicznej kadzi lub jednostek inspekcyjnych i nie stanowi bezpośredniego pytania w obecnym banku kursu podstawowego. Powyższy przegląd zamyka punkt 1 w zakresie wykrywania zastosowania sprostowania do pytań. Następny krok etapu 4x22 to literalne dowody dla rekordów bez cytatu, zaczynając od wartości liczbowych, terminów i progów.
