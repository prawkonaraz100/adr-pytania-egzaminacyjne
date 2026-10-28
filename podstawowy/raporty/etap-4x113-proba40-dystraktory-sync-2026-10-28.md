# Etap 4x113 — próbka 40, dystraktory i synchronizacja kursu

- Data: 2026-10-28.
- Punkt wyjścia: świeży `main` po PR #571, commit `51d3d1c86da9661db047752373402c6c22b2a1b6`.
- Zakres: wyłącznie kurs podstawowy ADR.
- Bank po zmianach: 609 pytań, blob `2675c0636a421bf3b4347ad0117087d6ec633321`; 609 `needs_review`, 0 `verified`.
- Próbka: seed `41132026`; 423 ID wykluczone z zapisanych list 4x107–4x112; pula 186, wybrano 40 unikalnych ID. Explanation w próbce: 303–413 znaków, 0 poniżej 200. Pełny manifest: [seed, próbka i wykluczenia](etap-4x113-wykluczenia-proby.json).

## 1. Wynik przeglądu explanation i dystraktorów

Ręcznie przeczytano 40 wyjaśnień. 34 pozostawiono bez zmian, ponieważ już prostym językiem tłumaczyły sens poprawnej odpowiedzi i najważniejszą pomyłkę. W sześciu pytaniach potwierdzono, że błędne odpowiedzi były zbyt skrajne, nieprecyzyjne albo mało diagnostyczne; zastąpiono je realistycznymi błędami początkującego i dopasowano explanation. Zachowano 2–5 zdań, sens praktyczny i krótką podstawę ADR.

| ID | Problem przed zmianą | Co zmieniono | Klucz / podstawa |
|---|---|---|---|
| ADR-B-0035 | Publiczny dostęp dla każdego lub brak jakichkolwiek wymagań ochrony były zbyt skrajne. | Zastąpiono je pomyłkami: ochrona tylko podczas przeładunku oraz poleganie na znakach bez ograniczenia dostępu. | Klucz C bez zmian; ADR 1.10.1.3. |
| ADR-B-0143 | Otwieranie przesyłek i bierne obserwowanie pożaru bez alarmowania były zbyt skrajne. | Dodano realistyczne błędy: próba gaszenia ładowni przy małym ogniu oraz zbliżenie się do rozpoznania źródła przed alarmem. | Klucz C bez zmian; ADR 5.4.3.4. |
| ADR-B-0516 | Odkładanie lektury do postoju i ograniczenie się do numeru UN słabo różnicowały poziom przygotowania. | Zastosowano pomyłki: lektura dopiero na krótkiej trasie oraz poleganie na ustnym streszczeniu dyspozytora. | Klucz A bez zmian; ADR 5.4.3.3. |
| ADR-B-0292 | „Wszystkie towary luzem, jeśli są przykryte” i sama zgoda kierowcy były zbyt oczywiste. | Zastąpiono je błędami: uznaniem szczelnego kontenera za wystarczające dopuszczenie oraz zgodą nadawcy za podstawę prawną. | Klucz A bez zmian; ADR 3.2.1 tabela A, kolumny 10 i 17, oraz 7.3.1.1. |
| ADR-B-0199 | Miejsce dostawy i podobne wymiary opakowań były słabo związane z decyzją o wspólnym załadunku. | Opcje sprawdzają teraz błędne poleganie na osobnych dokumentach oraz samej szczelności; poprawna opcja mówi o tabeli 7.5.2 i wyjątkach. | Klucz C bez zmian; ADR 7.5.2.1–7.5.2.2. |
| ADR-B-0345 | „Zawsze parking publiczny” i pobocze były zbyt skrajne. | Wprowadzono wiarygodne, lecz błędne priorytety: wygodę parkingu publicznego i najkrótszy postój na poboczu zamiast dostępnego terenu chronionego. | Klucz A bez zmian; ADR 8.4.1. |

Nie zmieniono ID, poprawnych liter ani wskazanych podstaw prawnych. Wszystkie sześć zmienionych explanation ma 310–382 znaki.

## 2. Synchronizacja banku, audytów i egzaminów

- Zaktualizowano migawki audytu redakcyjnego i klauzul prawnych dla ADR-B-0035, 0143, 0516, 0292, 0199 i 0345; statusy pozostają `needs_review`, a niezależna akceptacja prawna — pending.
- ADR-B-0035 występuje w wariancie 005. Zaktualizowano jego teksty odpowiedzi zgodnie z mapowaniem liter oraz explanation w kluczu 005. Pozostałe warianty nie zawierały zmienionych pytań.
- Zsynchronizowano `source_bank_head` we wszystkich wariantach i kluczach 001–005 do aktualnego blobu `2675c0636a421bf3b4347ad0117087d6ec633321`.
- Sprawdzono referencje scenariuszy: 39 scenariuszy, 0 nieistniejących ID i 0 odwołań do innego działu. Pytania pozostały przypisane do dotychczasowych modułów.
- Nie dodano pytań, ponieważ w tej próbce nie potwierdzono nowej luki programowej.

## 3. Metryki Quality Gate

- 609 pytań, 609 unikalnych ID; 609 `needs_review`, 0 `verified`.
- Explanation: minimum 300 znaków, 0 poniżej 200.
- Poprawna odpowiedź jest jedyną najdłuższą w 74/609 = **12,15%**; wszystkie działy mieszczą się w progu 16%.
- Przed zmianą było 71/609 = 11,66%; sześć poprawionych zestawów nie zwiększyło wskaźnika ponad limit.

| Dział | Pytania | Poprawna jedyną najdłuższą | Wskaźnik |
|---|---:|---:|---:|
| B-01 | 45 | 6 | 13,33% |
| B-02 | 56 | 8 | 14,29% |
| B-03 | 49 | 6 | 12,24% |
| B-04 | 46 | 6 | 13,04% |
| B-05 | 43 | 5 | 11,63% |
| B-06 | 45 | 6 | 13,33% |
| B-07 | 48 | 6 | 12,50% |
| B-08 | 42 | 5 | 11,90% |
| B-09 | 46 | 5 | 10,87% |
| B-10 | 55 | 4 | 7,27% |
| B-11 | 43 | 6 | 13,95% |
| B-12 | 44 | 6 | 13,64% |
| B-13 | 47 | 5 | 10,64% |

## 4. Pełna lista 40 sprawdzonych ID

ADR-B-0429, ADR-B-0035, ADR-B-0301, ADR-B-0020, ADR-B-0143, ADR-B-0582, ADR-B-0107, ADR-B-0480, ADR-B-0333, ADR-B-0199, ADR-B-0085, ADR-B-0606, ADR-B-0058, ADR-B-0468, ADR-B-0122, ADR-B-0192, ADR-B-0127, ADR-B-0149, ADR-B-0563, ADR-B-0104, ADR-B-0516, ADR-B-0251, ADR-B-0212, ADR-B-0359, ADR-B-0267, ADR-B-0196, ADR-B-0276, ADR-B-0545, ADR-B-0043, ADR-B-0245, ADR-B-0292, ADR-B-0465, ADR-B-0497, ADR-B-0006, ADR-B-0345, ADR-B-0220, ADR-B-0187, ADR-B-0375, ADR-B-0586, ADR-B-0503.

## 5. Ograniczenia i testy

Lista wykluczeń jest odtwarzalna względem zachowanych manifestów 4x107–4x112. Dla 4x103–4x106 wcześniejsze raporty nie zachowały pełnego manifestu każdego losowania; dlatego wykluczenie jest konserwatywne, ale nie dowodzi rozłączności z nieudokumentowanymi ID z tamtych prób.

Nie uruchomiono testów lokalnych, ponieważ połączenie dostępne w tej sesji pozwala edytować pliki przez GitHub, lecz nie udostępnia lokalnego checkoutu. Nie deklaruję lokalnego PASS; przed scaleniem wymagany jest zielony Quality Gate CI. Nie nadano statusu `verified`; recenzja prawna specjalisty pozostaje otwarta.
