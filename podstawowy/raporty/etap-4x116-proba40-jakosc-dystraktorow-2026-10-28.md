# Etap 4x116 — próbka 40, czytelność dystraktorów i synchronizacja

- Data: 2026-10-28.
- Punkt wyjścia: `main` `47c886aae77cfa5dfba39ad33ec706ef5db11d96` po scaleniu PR #574 (4x115).
- Zakres: wyłącznie kurs podstawowy ADR.
- Bank przed zmianami: 609 pytań, blob SHA `aa6c4184014808849f154ab07bf6acc99cbe4701`.
- Bank po zmianach: 609 pytań, blob SHA `ed7e1842d6f15d1ecde54ea3319d9efe3ef7a728`.
- Statusy: 609 `needs_review`, 0 `verified`; nie zmieniano poprawnych liter ani podstaw prawnych.

## 1. Próba i ograniczenia

Seed: `41162026`; LCG + Fisher–Yates. Zbiór wykluczeń ma 543 unikalne ID z manifestów 4x107–4x115; pula wyniosła 66 pytań, z której wylosowano 40.

ID próbki: ADR-B-0390, ADR-B-0435, ADR-B-0161, ADR-B-0536, ADR-B-0544, ADR-B-0180, ADR-B-0422, ADR-B-0201, ADR-B-0554, ADR-B-0243, ADR-B-0530, ADR-B-0455, ADR-B-0510, ADR-B-0283, ADR-B-0263, ADR-B-0235, ADR-B-0346, ADR-B-0547, ADR-B-0131, ADR-B-0474, ADR-B-0538, ADR-B-0607, ADR-B-0135, ADR-B-0157, ADR-B-0526, ADR-B-0239, ADR-B-0408, ADR-B-0477, ADR-B-0585, ADR-B-0509, ADR-B-0288, ADR-B-0501, ADR-B-0154, ADR-B-0138, ADR-B-0238, ADR-B-0295, ADR-B-0599, ADR-B-0517, ADR-B-0004, ADR-B-0193

Pełny seed, lista próbki i wykluczenia znajdują się w [manifeście próby](etap-4x116-wykluczenia-proby.json). Ograniczenie dowodowe: wcześniejsze manifesty nie dowodzą pełnej rozłączności względem ewentualnych nieujawnionych ID ze starszych artefaktów 4x103–4x106; nie przedstawiam tej próbki jako dowodu obejmującego nieudokumentowane próbki.

## 2. Wynik przeglądu

- **33 pytania** pozostawiono bez zmian: explanation były zrozumiałe, miały 2–5 zdań i wyjaśniały sens poprawnej odpowiedzi oraz główną pomyłkę.
- **7 pytań** miało potwierdzone słabości dystraktorów; poprawiono łącznie **14 błędnych opcji** i dopasowano explanation do nowych odpowiedzi.
- Przy walidacji klucza 001 sprawdzono też `ADR-B-0489`: wyjaśnienie zawiera odwołanie do litery odpowiedzi, które w arkuszu jest celowo mapowane na inną literę niż w banku. Zachowano właściwe brzmienie dla kolejności opcji w wariancie.
- Nie dodano nowych pytań. Nie zmieniono ID, poprawnych odpowiedzi ani podstaw prawnych. Zmiany są redakcyjne i nie stanowią niezależnej weryfikacji prawnej.

| ID | Podstawa | Potwierdzony problem | Zmiana |
|---|---|---|---|
| ADR-B-0243 | ADR 8.3.3 | Jeden dystraktor opierał się na zgodzie telefonicznej spedytora, co zbyt łatwo zdradzało błąd. | Zastąpiono go realistyczną pomyłką: otwarcie przesyłki w celu sprawdzenia oznakowania. |
| ADR-B-0283 | ADR 8.1.4.4 | „Nakleić dowolną datę” było oczywistym dystraktorem. | Wprowadzono pomyłki oparte na sprawności gaśnicy, plombie i przepisywaniu daty bez kontroli. |
| ADR-B-0390 | ADR 5.4.2 | Zezwolenie parkingowe i faktura VAT były niepowiązane z certyfikatem pakowania. | Wprowadzono pomylenie certyfikatu z instrukcją pisemną lub dokumentem przewozowym ADR. |
| ADR-B-0435 | ADR 5.4.3.4 | Błędne opcje opisywały skrajne działania, bez realistycznego uzasadnienia kursanta. | Urealniono pokusę otwarcia ładowni i próbę gaszenia wodą przed oceną ładunku. |
| ADR-B-0455 | ADR 1.10.3.1.2 | Odwołanie do dowodu rejestracyjnego było zbyt łatwe do odrzucenia. | Zastąpiono je pomyłką polegającą na szukaniu progów dużego ryzyka w dokumentach pojazdu. |
| ADR-B-0510 | ADR 2.2.43.1.1 | Dystraktory myliły reakcję z wodą z odległymi zagrożeniami. | Wprowadzono pomyłkę klasyfikacyjną z klasą 8 oraz błędne przekonanie, że wodą można spłukać mokre opakowanie. |
| ADR-B-0530 | ADR 5.4.1.1.3 | Zastąpienie numeru UN kodem odpadu było opisane zbyt skrótowo. | Urealniono pomyłki: wpis w systemie wewnętrznym i zastąpienie nazwy przewozowej kodem odpadu. |

### Przykłady przed / po

1. **ADR-B-0390:** „Wyłącznie faktura VAT” → „Dokument przewozowy ADR, bez odrębnego potwierdzenia sposobu pakowania kontenera”. Nowy dystraktor sprawdza pomylenie dwóch rzeczywistych dokumentów.
2. **ADR-B-0283:** „Wystarczy nakleić dowolną datę” → „Samodzielnie dopisać termin z poprzedniej naklejki, bez sprawdzenia historii kontroli urządzenia”. Błąd nadal jest błędny, ale przypomina wiarygodną próbę obejścia kontroli.
3. **ADR-B-0510:** „Ryzyko promieniowania jonizującego” → „Kontakt z wodą oznacza, że towar należy traktować jak materiał żrący klasy 8, a nie klasę 4.3”. Dystraktor sprawdza mylenie klas zagrożenia, a nie wiedzę niezwiązaną z sytuacją.

Wszystkie siedem zmienionych explanation ma 2–5 zdań i 365–432 znaki. Najpierw wyjaśniają sens poprawnej odpowiedzi, następnie typową pomyłkę, a na końcu wskazują podstawę ADR.

## 3. Synchronizacja egzaminów i migawek

- Warianty i klucze egzaminów próbnych 001–005 wskazują nowy bank SHA `ed7e1842d6f15d1ecde54ea3319d9efe3ef7a728`.
- Wariant 004 zsynchronizowano z nowymi opcjami `ADR-B-0390`; wariant 005 — z nowymi opcjami `ADR-B-0510`. Klucze 004 i 005 otrzymały aktualne explanation dla tych pytań.
- Klucz 001 dla `ADR-B-0489` pozostawiono z wyjaśnieniem zmapowanym do liter w arkuszu; test sprawdza to mapowanie, a nie surowy tekst explanation z banku.
- Odświeżono migawki `review/legal-clauses/` i `review/sequential/` dla zakresów 241–246, 282–283, 381–398, 417–436, 455–460, 510–512 i 526–533. Wszystkie pozostają oznaczone jako wymagające niezależnej recenzji.
- Sprawdzono 13 lekcji i 39 scenariuszy pod kątem istnienia odwołań; nie zmieniano treści lekcji ani scenariuszy, ponieważ nie wykryto potwierdzonej sprzeczności wynikającej z tej partii.

## 4. Quality Gate — preflight

- Bank: 609 pytań; duplikaty ID: 0.
- Poprawna odpowiedź jest jedyną najdłuższą: **72/609 = 11,82%**; maksimum działu: **14,29%**.
- Najkrótsze explanation: **300 znaków**; poniżej 200 znaków: **0**.
- Wszystkie statusy: 609 `needs_review`, 0 `verified`.
- Warianty 001–005: po 30 pytań, brak powtórzeń w wariancie; preflight porównania tekstów opcji i kluczy nie wykazał dalszych rozbieżności po naprawie ADR-B-0489.
- Testy lokalne nie były dostępne w tym trybie pracy; przed scaleniem wymagany jest pełny PASS GitHub Actions.

## 5. Rozkład wskaźnika długości odpowiedzi po zmianach

| Dział | Pytania | Poprawna jedyną najdłuższą | Wskaźnik |
|---|---:|---:|---:|
| B-01 | 45 | 6 | 13,33% |
| B-02 | 56 | 8 | 14,29% |
| B-03 | 49 | 5 | 10,20% |
| B-04 | 46 | 6 | 13,04% |
| B-05 | 43 | 5 | 11,63% |
| B-06 | 45 | 6 | 13,33% |
| B-07 | 48 | 6 | 12,50% |
| B-08 | 42 | 4 | 9,52% |
| B-09 | 46 | 5 | 10,87% |
| B-10 | 55 | 4 | 7,27% |
| B-11 | 43 | 6 | 13,95% |
| B-12 | 44 | 6 | 13,64% |
| B-13 | 47 | 5 | 10,64% |

Nie rozpoczęto kursu cystern ani innego kursu. Bank pozostaje materiałem roboczym oczekującym na niezależną recenzję specjalisty ADR.
