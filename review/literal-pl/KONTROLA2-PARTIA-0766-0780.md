# Kontrola druga — partia 52 (ADR-B-0766–0780)

**Wynik:** 0 OK / 15 POPRAW / 0 BLOKUJ. Wdrożono wszystkie 15 rekordów z `POPRAWKI-KONTROLA2-0766-0780.jsonl`. Bank ma 780 rekordów; blob SHA: `e2fba7594e5334356a1e5f3192987e538d58ee2c`.

## Zakres zmian

- **6 nowych elementów w tej samej kompetencji:** 0768, 0769, 0770, 0771, 0772, 0773.
- **9 przeredagowań z zachowaniem tematu:** 0766, 0767, 0774, 0775, 0776, 0777, 0778, 0779, 0780.
- Bez kursu cystern. Litery kluczy, moduły, kompetencje i liczba pytań pozostają bez zmian.
- Wszystkie rekordy zachowują `needs_review`; nic nie oznaczono jako `verified`, `checked_at` ani `reviewer`.

## Wyniki i uzasadnienia

| ID | Kompetencja | Klucz | Decyzja po kontroli 2 |
|---|---|---:|---|
| ADR-B-0766 | ADR-B-09-K04 | B | PRZEREDAGOWANIE |
| ADR-B-0767 | ADR-B-09-K05 | B | PRZEREDAGOWANIE |
| ADR-B-0768 | ADR-B-09-K06 | B | NOWY ELEMENT |
| ADR-B-0769 | ADR-B-09-K07 | B | NOWY ELEMENT |
| ADR-B-0770 | ADR-B-10-K02 | B | NOWY ELEMENT |
| ADR-B-0771 | ADR-B-11-K04 | B | NOWY ELEMENT |
| ADR-B-0772 | ADR-B-11-K06 | B | NOWY ELEMENT |
| ADR-B-0773 | ADR-B-11-K07 | C | NOWY ELEMENT |
| ADR-B-0774 | ADR-B-12-K01 | A | PRZEREDAGOWANIE |
| ADR-B-0775 | ADR-B-12-K02 | B | PRZEREDAGOWANIE |
| ADR-B-0776 | ADR-B-12-K04 | C | PRZEREDAGOWANIE |
| ADR-B-0777 | ADR-B-13-K03 | B | PRZEREDAGOWANIE |
| ADR-B-0778 | ADR-B-13-K05 | B | PRZEREDAGOWANIE |
| ADR-B-0779 | ADR-B-13-K06 | B | PRZEREDAGOWANIE |
| ADR-B-0780 | ADR-B-13-K07 | B | PRZEREDAGOWANIE |

### Korekty merytoryczne i redakcyjne

- 0766 — strzałki kierunkowe na dwóch przeciwległych pionowych bokach; butelki 750 ml poza wyjątkami 5.2.1.10.2 (b) i (f)
- 0767 — wzajemna zgodność piętrzenia różnych typów konstrukcji
- 0768 — elastyczny kontener 1,5 m wymaga sztywnych ścian bocznych i czołowych o wysokości co najmniej 1 m (2/3 wysokości)
- 0769 — po przewozie luzem innego towaru tej samej klasy pojazd wymaga czyszczenia; wyjątek dotyczy tych samych towarów
- 0770 — przewóz ciężarówki promem morskim na warunkach 1.1.4.2.1; wymagany wpis „PRZEWÓZ ZGODNY Z 1.1.4.2.1”
- 0771 — kod C z przyczepy wyznacza ograniczenie dla całej jednostki transportowej (samochód z przyczepą)
- 0772 — jednostka oznakowana LQ bez tablic pomarańczowych podlega ograniczeniom tunelowym kategorii E
- 0773 — przy pożarze przedziału ładunkowego zahamować i wyłączyć silnik, jeżeli możliwe i bezpieczne
- 0774 — wymagany jest dokument z fotografią potwierdzający tożsamość; ADR nie wskazuje wyłącznie dowodu osobistego
- 0775 — miejsce czasowego przechowywania ma być odpowiednio chronione i dobrze oświetlone; warunek „o ile jest to możliwe i wskazane” dotyczy dostępu osób postronnych
- 0776 — wstrzymać wydanie do ustalenia tożsamości przewoźnika przy rozbieżności Alfa/Beta
- 0777 — polski zapis „Sprzedaż obwoźna” i zgoda właściwych władz
- 0778 — dokumenty ze zdjęciem wszystkich członków załogi w kabinie kierowcy i przy sobie
- 0779 — zapis wymagany w dokumencie EDI, nie tylko papierowym
- 0780 — instrukcje pisemne przenieść do kabiny ciągnika zastępczego; podstawa obejmuje 8.1.2.1 (b), 8.1.2.3 i 5.4.3.1

## Wskaźniki

- „Poprawna = jedyna najdłuższa”: 9/780 (1,15%) → 8/780 (1,03%); maksimum działu 4,35% → 3,77%.
- „Poprawna = jedyna najkrótsza”: 62/780 → 53/780.
- Wyjaśnienia nowych rekordów: 351–466 znaków; wszystkie odpowiedzi ≤ 80 znaków, bez końcowych kropek i średników oraz bez słów absolutnych; klucz nie jest jedyną najkrótszą ani jedyną najdłuższą odpowiedzią.
- Porównanie podobieństwa: brak kandydatów przy progach CI 0,60 (near duplicates) i 0,80 (cross-module); ręczna analiza 5 par o podobieństwie 0,25–0,45 odnotowana w pakiecie kontroli.

## Synchronizacja

- Bank `podstawowy/questions.jsonl`: 780 linii, SHA `e2fba7594e5334356a1e5f3192987e538d58ee2c`.
- Snapshoty `review/sequential/766-766.json`–`780-780.json` i `review/legal-clauses/766-766.json`–`780-780.json`.
- Ledger źródeł zaktualizowany dla 0766–0780; statusy pozostają `needs_review`, akceptacja specjalisty pending.
- Rejestry specjalisty, manifest pakietu, pięć lekcji ADR-B-09–13, dokumentacja kursu, README, egzaminy próbne i testy SHA zsynchronizowane z nowym bankiem.
- Egzaminy próbne 001–005 nie zawierają nowych pytań; zmienia się wyłącznie `source_bank_head` / SHA.
- `tools/apply_poprawki.py` rejestruje nowy plik korekt.
- Pełny Quality Gate i testy jednostkowe pozostają warunkiem scalenia; ten raport nie stanowi zgody na publikację.

## Do niezależnej recenzji specjalisty

0766 — wyjątki strzałek dla butelek 750 ml; 0768 — zakres kompetencji 09-K06 względem 7.5.7.6; 0769 — bliskość wyjątku 7.5.8.2 do 0201; 0770 — interpretacja rejsu promem w łańcuchu 1.1.4.2.1 i relacja do 1.1.4.2.2; 0771 — kod tunelowy zespołu pojazdów; 0772 — relacja 8.6.3.3 i 8.6.4; 0773 — nasycenie 11-K07 oraz legal_refs kompetencji; 0774 — dokument tożsamości bez ograniczania do dowodu osobistego; 0776 — bliskość 0413/0414; 0778 — rozdział miejsca przewożenia od rodzaju dokumentu; 0779 — EDI i wymagany zapis. Żadne z tych pytań nie uzyskało statusu `verified`.

