# Etap 4x95 — próbka 60 explanation, spójność wartości ADR i mapa wpływu 2027

- Data: 27.10.2026.
- Punkt wejścia: świeży `main`, `7e0eb51e2394977b6d0c6dc590c20d0292052582`.
- Gałąź robocza: `stage4x95-audit-20261027b`.
- Zakres: wyłącznie kurs podstawowy ADR.
- Metoda losowania: seed `2026102795`, LCG (`state = 1664525 × state + 1013904223 mod 2^32`) i Fisher–Yates.
- Z puli wykluczono wszystkie ID występujące w dostępnych raportach 4x84–4x92. Raport 4x86 sam wskazuje, że nie publikuje pełnej listy swojej próbki; dlatego wykluczenie wszystkich historycznych ID z nieujawnionej części 4x86 pozostaje nieudowodnione. Pula po wykluczeniu jawnie dostępnych ID: 174 pytania.

## 1. Stan bazowy i Quality Gate

Na wejściowym `main` ostatni workflow Quality Gate zakończył się PASS: [run #40546162112](https://github.com/prawkonaraz100/adr-pytania-egzaminacyjne/actions/runs/40546162112).

- Bank: 609 pytań, 609 unikalnych ID (`ADR-B-0001`–`ADR-B-0609`).
- Status: 609 `needs_review`, 0 `verified`.
- Najkrótsze explanation: 300 znaków; poniżej 200 znaków: 0.
- „Poprawna = jedyna najdłuższa” po zmianach: 74/609 = **12,15%**.
- Maksimum w pojedynczym dziale: B-02 = 8/56 i B-03 = 7/49 = **14,29%**; każdy dział pozostaje poniżej 18%.
- Scenariusze: 39; brak nieistniejących `question_ids` i brak ID z niewłaściwego modułu.
- Warianty 001–005: każdy ma 30 pytań i 30 unikalnych ID. Wszystkie pięć pól `source_bank_head` zsynchronizowano z aktualnym blobem banku `7a2f4615e652f69d4079bf622098c8dd586c1ae1`.

## 2. Próbka 60 — wynik ręcznej oceny

Wszystkie 60 wyjaśnień sprawdzono w kontekście pytania, opcji A/B/C, poprawnej litery i wskazanej podstawy. Zakres długości: 303–457 znaków; 0 poniżej 200, 0 jednozdaniowych; kontrola interpunkcji wykazała 3–5 zdań. Osiem pozycji wymagało korekty dydaktycznej; pozostałe 52 pozostawiono bez zmian, ponieważ explanation wyjaśniały sens poprawnej odpowiedzi, najbardziej kuszące błędne odpowiedzi i wskazywały podstawę.

### Zmienione pytania

| ID | Potwierdzony problem | Działanie | Podstawa ADR |
|---|---|---|---|
| ADR-B-0290 | Opcje pakującego mieszały obowiązki innych uczestników, a explanation powtarzało tę samą myśl | Urealniono dwie błędne odpowiedzi i skrócono powtórzenie w explanation | 1.4.3.2 |
| ADR-B-0304 | Dwa dystraktory były zbyt absurdalne, nie sprawdzały rozumienia planu ochrony | Zastąpiono je wiarygodnymi, lecz niepełnymi elementami planu | 1.10.3.2.2(a) |
| ADR-B-0364 | Odpowiedź „zgłosić problem i dojechać do postoju” mogła wyglądać na częściowo poprawną | Doprecyzowano dystraktor jako kontynuowanie jazdy mimo zagrożenia | 1.4.2.2.4 |
| ADR-B-0428 | „Bagaż podręczny” był absurdalnym dystraktorem | Zastąpiono go typową pomyłką: sprawdzeniem samej klasy bez grup zgodności | 7.5.2.2 |
| ADR-B-0249 | Odpowiedzi błędne nie odzwierciedlały wystarczająco realistycznego pominięcia kontroli tożsamości | Urealniono dystraktory: sam numer zlecenia albo telefoniczne zapewnienie bez weryfikacji | 1.10.1.2 |
| ADR-B-0403 | Dystraktory myliły procedurę ochrony z reklamacją i rozliczeniem szkody w sposób mało praktyczny | Zastąpiono je wiarygodnymi, ale niewystarczającymi działaniami | 1.10.3.2.2(e) |
| ADR-B-0366 | Explanation nie odpowiadało dokładnie dystraktorowi o obowiązku pakującego | Przepisano wyjaśnienie, rozdzielając obowiązek firmy zlecającej, pakującego i kierowcy | 1.4.2.1.3 |
| ADR-B-0512 | Wyjaśnienie nie odróżniało ograniczenia tunelowego dla jednostki oznakowanej LQ od kodu tunelowego z kolumny 15 | Doprecyzowano pytanie, poprawną treść i explanation; wyjaśniono zastosowanie ograniczenia kategorii E | 8.6.4, 3.4.13–3.4.14 |

W żadnym pytaniu nie zmieniono ID ani poprawnej litery. Dodatkowo skrócono treść poprawnej opcji w ADR-B-0512, by usunąć niezamierzony sygnał długości odpowiedzi; poprawna litera C pozostała bez zmian. Nie zmieniano klucza merytorycznego. Osiem rekordów nadal ma `needs_review`.

### Pozostałe 52 ID — fałszywy alarm, bez zmiany

`ADR-B-0182, ADR-B-0581, ADR-B-0068, ADR-B-0580, ADR-B-0531, ADR-B-0321, ADR-B-0587, ADR-B-0286, ADR-B-0534, ADR-B-0042, ADR-B-0586, ADR-B-0052, ADR-B-0582, ADR-B-0594, ADR-B-0460, ADR-B-0361, ADR-B-0024, ADR-B-0504, ADR-B-0045, ADR-B-0521, ADR-B-0332, ADR-B-0485, ADR-B-0333, ADR-B-0318, ADR-B-0019, ADR-B-0213, ADR-B-0499, ADR-B-0330, ADR-B-0498, ADR-B-0392, ADR-B-0406, ADR-B-0065, ADR-B-0034, ADR-B-0175, ADR-B-0427, ADR-B-0569, ADR-B-0235, ADR-B-0141, ADR-B-0195, ADR-B-0525, ADR-B-0102, ADR-B-0440, ADR-B-0578, ADR-B-0245, ADR-B-0125, ADR-B-0431, ADR-B-0079, ADR-B-0251, ADR-B-0108, ADR-B-0495, ADR-B-0598, ADR-B-0100`

W każdej z tych pozycji wyjaśnienie zachowano po sprawdzeniu kontekstu: nie znaleziono potwierdzonej sprzeczności między poprawną odpowiedzią, błędnymi odpowiedziami i podstawą ADR. Pytania wymagające odczytu konkretnego punktu lub tabeli pozostają materiałem do recenzji specjalisty, a nie są oznaczane jako zweryfikowane.

## 3. Kontrola wartości wrażliwych na zmianę ADR 2027

### Baterie — adnotacja do obowiązkowej kontroli specjalisty

Mapa 4x94 wymienia siedem pytań z B-02, których treść wymaga porównania z pakietem zmian ADR 2027:

- `ADR-B-0099` — nalepki wzoru 9 i 9A;
- `ADR-B-0162` — nalepka 9A i UN 3551/3552;
- `ADR-B-0315` — bateria sodowo-jonowa UN 3551;
- `ADR-B-0499` — bateria przewożona oddzielnie a bateria w urządzeniu;
- `ADR-B-0500` — badania typu baterii;
- `ADR-B-0501` — ochrona ogniwa przed zwarciem zewnętrznym;
- `ADR-B-0502` — ochrona przy równoległym połączeniu ogniw.

**Adnotacja:** przed wydaniem następnej edycji kursu specjalista ma porównać te rekordy z właściwymi punktami ECE/TRANS/WP.15/274 wraz z corrigenda i addenda, następnie sprawdzić odpowiadającą im lekcję B-02 i scenariusze tego działu. To są kandydaci do sprawdzenia, nie potwierdzone błędy. Nie zmieniono treści tylko dlatego, że dany temat występuje na liście wpływu.

Źródła: [UNECE — wykaz ADR 2025 i zmian przewidzianych na 1.01.2027](https://unece.org/adr-2025-files), [UNECE — podsumowanie obszarów zmian](https://unece.org/transport/dangerous-goods), [UN Treaty Collection — C.N.395.2026.TREATIES-XI.B.14 z 9.10.2026](https://treaties.un.org/Pages/ViewDetails.aspx?chapter=11&clang=_en&mtdsg_no=XI-B-14&src=IND). UN Treaty Collection odnotowuje wejście zmian w życie; strona informacyjna UNECE nadal opisuje pakiet jako zmiany przewidziane do wejścia w życie. Z tego powodu rejestr rozróżnia status formalny od szczegółowej weryfikacji każdego punktu. Nie potwierdzono w tym etapie skonsolidowanego polskiego tekstu ADR 2027, więc nie zmieniano merytoryki na podstawie streszczenia.

### M369 i inne wartości

- W mapie 4x94 M369 ma termin ważności do **31.12.2026**. Przeszukanie banku nie wykazało pytań o M369, UN 1202, EN 590, EN 15940 ani olej napędowy/parafinowy; nie ma więc pytania do poprawienia z tego powodu.
- M369 i M364 to odrębne umowy. Nie zakładać przedłużenia żadnej z nich bez urzędowego potwierdzenia.
- W zakresie siedmiu jawnie wskazanych rekordów bateryjnych nie wprowadzono nowych liczb, terminów ani wymagań. Pozostałe wartości pozostają w rejestrze 4x93 oraz raportach 4x91–4x94 do kontroli przy oficjalnym porównaniu tekstu.
- Nie deklaruje się, że każda liczba w całym banku została niezależnie zatwierdzona prawnie. To pozostaje zadaniem specjalisty; `needs_review` pozostaje bez zmian.

## 4. Lekcje, scenariusze i egzaminy

- Odczytano lekcje B-01–B-05 oczami kursanta, korzystając także z wyników wcześniejszego odbioru B-01–B-05 w raporcie 4x91. W tym przeglądzie nie znaleziono nowej, potwierdzonej sprzeczności wymagającej zmiany ich merytoryki.
- Strukturalna kontrola wszystkich 39 scenariuszy: każdy `question_id` istnieje i należy do tego samego działu co scenariusz.
- Żadne z ośmiu zmienionych pytań nie występuje w wariantach 001–005, więc treści arkuszy nie wymagały zmiany. Ich `source_bank_head` zaktualizowano po zmianie banku.
- Kontrola kluczy wykazała jeden stary opis opcji w `klucz-001.json` dla ADR-B-0489: po przetasowaniu odpowiedzi wyjaśnienie odwoływało się do dawnych liter. Zaktualizowano opis, aby wskazywał litery z aktualnego wariantu. W kontroli względem treści opcji w arkuszach nie wykryto rozbieżności poprawnej odpowiedzi.
- Nie dodano pytań: w tej próbce nie potwierdzono luki programu wymagającej nowego rekordu.

## 5. Metryki i status

- Explanation po zmianach: minimum 300 znaków, 0 poniżej 200.
- Wskaźnik „poprawna = jedyna najdłuższa”: 12,15% globalnie; maksimum działu 14,29% (B-02 i B-03).
- Bank: 609 unikalnych pytań, 609 `needs_review`, 0 `verified`.
- Nowe pytania: 0; poprawione explanation: 8; pytania z poprawionymi dystraktorami: 6; naprawiony opis odpowiedzi w kluczu egzaminu: 1.
- Wynik Quality Gate dla tej partii zostanie odnotowany po uruchomieniu CI na PR. Nie uruchamiano lokalnych testów w repozytorium; wykonano statyczny preflight na pobranych plikach przez GitHub, a testy automatyczne mają być potwierdzone przez CI.
