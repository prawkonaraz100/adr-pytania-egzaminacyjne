# Etap 4x112 — próbka 40, dystraktory, spójność banku i egzaminów

- Data: 2026-10-28.
- Punkt wyjścia: świeży `main` po PR #570, commit `41b3780093e0ff7e7b9706669a90353267fdf44d`.
- Zakres: wyłącznie kurs podstawowy ADR.
- Bank źródłowy po zmianach: 609 pytań, blob `4f6deeca86fea1b746039ab74db7c48f43abbfd0`; wszystkie `needs_review`, zero `verified`.
- Próbka deterministyczna: seed `41122026`; 383 ID wykluczono konserwatywnie na podstawie identyfikatorów wymienionych w raportach 4x103–4x106 oraz manifestach 4x107–4x111. Pula: 226 pytań; sprawdzono 40 bez powtórzeń. Pełny rejestr: [manifest próby i wykluczeń](etap-4x112-wykluczenia-proby.json).

## 1. Przegląd 40 wyjaśnień

Wszystkie 40 explanation przeczytano jako kursant. Długość w próbce: 301–430 znaków; zero poniżej 200 znaków. Większość już w prosty sposób tłumaczyła sens odpowiedzi i najważniejszą pomyłkę, więc nie zmieniano tekstu tylko po to, by wykazać edycję. Sześć wyjaśnień dopasowano do urealnionych dystraktorów; zachowano 2–5 zdań, krótką podstawę ADR i język dla początkującego.

## 2. Potwierdzone poprawki dystraktorów

| ID | Potwierdzona słabość | Poprawka |
|---|---|---|
| ADR-B-0498 | Jedna z błędnych odpowiedzi przypisywała podklasę 1.6 do klasy 8 bez dydaktycznie użytecznego powodu. | Zamieniono ją na wiarygodną pomyłkę dotyczącą wrażliwości/rodzaju zagrożenia; wyjaśnienie rozróżnia podklasę 1.6 od klas 5.1 i 8. Podstawa: ADR 2.2.1.1.5. |
| ADR-B-0525 | Opcja o numerze rejestracyjnym za każdym oznaczeniem klasy była oczywiście nie na temat. | Zastąpiono ją typową pomyłką: wpisaniem kategorii tunelu bez kodu towaru. Wyjaśnienie wskazuje wymóg kodu w nawiasach. Podstawa: ADR 5.4.1.1.1(k). |
| ADR-B-0224 | Dwa błędne warianty były zbyt skrajne i słabo sprawdzały ocenę bezpiecznej odległości. | Zastąpiono je pomyłkami: pozostawieniem ludzi zbyt blisko zdarzenia oraz wysłaniem świadka do odczytania oznakowania. Podstawa: ADR 5.4.3.4. |
| ADR-B-0110 | Odpowiedzi o pozostawieniu skażonej odzieży były powtarzalne i mało diagnostyczne. | Zastąpiono je typowymi błędami: otrzepaniem ubrania i kontynuacją pracy oraz odłożeniem zmiany odzieży do powrotu do bazy. Podstawa: instrukcje pisemne ADR 5.4.3.4. |
| ADR-B-0174 | Jedna opcja błędna sugerowała, że kod (-) znosi znak drogowy; druga nadmiernie zawężała jego znaczenie. | Urealniono obie pomyłki, zachowując rozróżnienie między kodem ADR a pozostałymi ograniczeniami drogowymi. Podstawa: ADR 8.6.3.1. |
| ADR-B-0207 | Błędna odpowiedź ograniczała kategorie tuneli do wymiarów pojazdu, co było zbyt oczywistym dystraktorem. | Zastąpiono ją typową pomyłką dotyczącą związku kategorii tunelu z ograniczeniami dla ładunku. Podstawa: ADR 1.9.5.2.2 i 8.6.4. |

Nie zmieniano ID pytań, poprawnych liter ani podstaw prawnych. Po wyrównaniu opcji poprawna odpowiedź nie stała się jedyną najdłuższą w żadnym z sześciu zmienionych pytań.

## 3. Spójność z lekcjami i scenariuszami

- Powiązane lekcje sprawdzone dla zmienionych pytań: B-02 (podklasa 1.6), B-05 (awaria i skażona odzież), B-11 (kody i kategorie tuneli), B-13 (wpis w dokumencie przewozowym).
- Scenariusze: 39; wszystkie `question_ids` istnieją w banku i należą do właściwego działu (0 błędnych referencji).
- Zmienione pytania nie są użyte w wariantach egzaminu 001–005, więc ich treść i kolejność opcji w arkuszach nie wymagały regeneracji.
- Migawki audytu redakcyjnego i klauzul prawnych zaktualizowano dla wszystkich sześciu zmienionych ID; statusy pozostają `needs_review` / oczekujące na niezależną recenzję.

## 4. Egzaminy próbne 001–005

Wszystkie pięć wariantów i pięć kluczy wskazuje aktualny blob banku `4f6deeca86fea1b746039ab74db7c48f43abbfd0`. Każdy wariant zawiera 30 unikalnych pytań. Kontrola mapowania liter wykazała, że explanation ADR-B-0489 w kluczu 001 musi używać litery po przestawieniu opcji: bankowa opcja A odpowiada opcji C w wariancie, więc odniesienie do C jest prawidłowe. Przywrócono wyjaśnienie z zachowaniem tego mapowania. Ponowna kontrola pięciu kluczy: brak rozbieżności tekstu poprawnej odpowiedzi lub explanation po mapowaniu.

## 5. Metryki Quality Gate po zmianach

- Liczba pytań: 609; unikalne ID: 609.
- `needs_review`: 609; `verified`: 0.
- Najkrótsze explanation w banku: 300 znaków; poniżej 200 znaków: 0.
- Poprawna odpowiedź jest jedyną najdłuższą w 71/609 = **11,66%** (próg 16%).
- Maksymalny wskaźnik działowy: **14,29%** w B-02; wszystkie działy mieszczą się w progu 16%.

| Dział | Pytania | Poprawna jedyną najdłuższą | Wskaźnik |
|---|---:|---:|---:|
| B-01 | 45 | 6 | 13,33% |
| B-02 | 56 | 8 | 14,29% |
| B-03 | 49 | 6 | 12,24% |
| B-04 | 46 | 5 | 10,87% |
| B-05 | 43 | 4 | 9,30% |
| B-06 | 45 | 6 | 13,33% |
| B-07 | 48 | 6 | 12,50% |
| B-08 | 42 | 5 | 11,90% |
| B-09 | 46 | 4 | 8,70% |
| B-10 | 55 | 4 | 7,27% |
| B-11 | 43 | 6 | 13,95% |
| B-12 | 44 | 6 | 13,64% |
| B-13 | 47 | 5 | 10,64% |

## 6. Zakres próby

ADR-B-0207, ADR-B-0087, ADR-B-0578, ADR-B-0055, ADR-B-0050, ADR-B-0094, ADR-B-0224, ADR-B-0110, ADR-B-0525, ADR-B-0174, ADR-B-0498, ADR-B-0464, ADR-B-0596, ADR-B-0557, ADR-B-0604, ADR-B-0141, ADR-B-0008, ADR-B-0099, ADR-B-0126, ADR-B-0218, ADR-B-0447, ADR-B-0113, ADR-B-0370, ADR-B-0337, ADR-B-0165, ADR-B-0363, ADR-B-0559, ADR-B-0269, ADR-B-0593, ADR-B-0106, ADR-B-0411, ADR-B-0169, ADR-B-0315, ADR-B-0527, ADR-B-0062, ADR-B-0426, ADR-B-0317, ADR-B-0172, ADR-B-0114, ADR-B-0186.

## 7. Ograniczenia i testy

Nie dodano nowych pytań, ponieważ w tej próbce nie potwierdzono konkretnej luki programowej. Nie wykonano testów lokalnych: dostępne połączenie pozwala zmieniać pliki przez GitHub, ale nie udostępnia lokalnego checkoutu do uruchomienia `python -m unittest`. Nie deklaruję więc lokalnego PASS; przed scaleniem wymagany jest zielony Quality Gate CI. Nie nadano statusu `verified` i nie rozpoczęto kursu cystern.
