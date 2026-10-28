# Etap 4x110 — próbka 40 explanation i kontrola dystraktorów

- Data: 2026-10-28.
- Punkt wejścia: świeży `main` po PR #568, commit `0380b90701759ad8434757450ee47d6d174e1185`.
- Zakres: wyłącznie kurs podstawowy ADR.
- Bank po zmianach: 609 pytań, blob `47b9c144b6b59c88338bad92fc7897e620d14a0c`; wszystkie `needs_review`, 0 `verified`.
- Seed `41092027`; [manifest próbki i jawne wykluczenia](etap-4x110-wykluczenia-proby.json).

## 1. Próba i przegląd

Przeprowadzono deterministyczne losowanie 40 pytań z puli 306 po wykluczeniu 303 ID jawnie zapisanych w rejestrze 4x109. Wszystkie 40 przeczytano wraz z pytaniem, odpowiedziami A/B/C, poprawną literą i podstawą ADR.

- Wyjaśnienia pozostawione bez zmian: 37.
- Pytania z potwierdzonym problemem redakcyjnym/dydaktycznym i korektą: 3.
- Explanation po zmianach: 2–5 zdań; minimum w banku 300 znaków, 0 poniżej 200.
- Rozłączność potwierdzona wobec ID jawnie zapisanych w etapach 4x103–4x109. Nie twierdzę, że próbka jest rozłączna z 4x84–4x102, ponieważ raport 4x86 nie publikuje pełnej listy 60 ID.

## 2. Potwierdzone korekty

| ID | Problem | Zmiana | Podstawa |
|---|---|---|---|
| ADR-B-0194 | Pytanie o powtórzoną cyfrę 8 powielało aspekt sprawdzany w ADR-B-0217 i nie różnicowało kompetencji. | Zmieniono je na praktyczne odczytanie obu pól tablicy i przekazanie ratownikowi właściwego numeru zagrożenia (88) oraz numeru UN (1831). Poprawna litera C pozostała bez zmian. | ADR 5.3.2.2.1; 5.3.2.3.1 |
| ADR-B-0217 | Dystraktor „druga ósemka to numer paczki” był przypadkowy i łatwy do odrzucenia. | Zastąpiono go wiarygodniejszą pomyłką: uznaniem powtórzenia cyfr za dwa odrębne zagrożenia. Explanation wyjaśnia też, czemu B błędnie wyklucza inne zagrożenia. Poprawna litera A bez zmian. | ADR 5.3.2.3.1 |
| ADR-B-0324 | Explanation zawierało niepowiązane zdanie o kolorze kartonów; poprawna opcja była wyraźnie dłuższa od dystraktorów. | Usunięto zdanie niezwiązane z pytaniem, skrócono poprawną opcję i wydłużono dwa dystraktory do wiarygodnych błędów: automatyczny zakaz przez nalepkę klasy 1 oraz uznanie, że oznaczenie UN zastępuje kontrolę wspólnego załadunku. Poprawna litera A bez zmian. | ADR 7.5.2.1 |

Migawki audytu zaktualizowano dla ADR-B-0194 i ADR-B-0217 (sekwencyjne i prawne) oraz ADR-B-0324 (prawna). Statusy pozostały `needs_review`.

## 3. Scenariusze i egzaminy

Ponownie sprawdzono strukturę wszystkich 39 scenariuszy: komplet wymaganych pól, co najmniej 3 kroki, istniejące `question_ids` z właściwego modułu. Nie wykryto potwierdzonego braku wymagającego zmiany scenariusza.

Warianty i klucze 001–005 wskazują nowy blob banku. Żadne ze zmienionych ID nie występuje w wariantach; nie było potrzeby zmiany treści arkuszy ani kluczy, jedynie synchronizacji `source_bank_head`.

## 4. Metryki po zmianach

- Bank: 609 rekordów, 609 unikalnych ID, 0 duplikatów ID; 609 `needs_review`, 0 `verified`.
- Explanation: minimum 300 znaków, 0 poniżej 200; wszystkie wyjaśnienia mają 2–5 zdań, bez zdań dłuższych niż 35 słów.
- „Poprawna = jedyna najdłuższa”: 70/609 = 11,49%; maksimum działu 14,29%.
- Wszystkie 13 działów pozostają poniżej 18%.

## 5. Testy i ograniczenia

Próba lokalnego `git clone` nie powiodła się z powodu błędu DNS (`github.com` nie został rozwiązany). Nie deklaruję lokalnego PASS. W PR wymagany jest pełny PASS GitHub Actions Quality Gate, w tym testy audytu sekwencyjnego, audytu prawnego, banku, metryk i synchronizacji egzaminów.

Niezależna recenzja prawna nadal wymaga specjalisty. Nie rozpoczęto kursu cystern ani żadnego innego kursu.
