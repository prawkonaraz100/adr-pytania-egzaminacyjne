# Etap 4x118 — próbka 40 explanation, wiarygodność dystraktorów i spójność materiałów

- Data: 2026-10-28.
- Świeży `main` na wejściu: `b8464030c2d9cf31bd67666673789d58ce9b6a79` (PR #577 / 4x117).
- Bank wejściowy: 609 pytań; blob SHA `b763f639efe11f972d4c3047dc8238334f9ff9f2`.
- Bank po poprawkach: 609 pytań; blob SHA `c7690500784676272a886d28ec0831a1975704c5`.
- Seed próby: `41182026`; [manifest i wykluczenia](etap-4x118-wykluczenia-proby.json).

## 1. Próba 40 pytań

Każde pytanie oceniono wraz z A/B/C, poprawną literą, explanation i wskazaną podstawą ADR. W próbie było 25 ID nieobecnych w zapisanych listach poprzednich prób oraz 15 wcześniej przeczytanych, ale pozostawionych bez zmian. Wszystkie 40 explanation nie były przepisywane w etapach 4x103–4x117.

| Wynik | Liczba |
|---|---:|
| Pytania przeczytane w kontekście treści i A/B/C | 40 |
| Explanation przepisane | 8 |
| Pytania z urealnionym dystraktorem | 6 |
| Pytania bez zmian | 32 |
| Poprawne litery zmienione | 0 |
| Explanation poniżej 200 znaków w banku po zmianach | 0 |

### Poprawki potwierdzone w przeglądzie

| ID | Co było słabe | Co poprawiono | Podstawa ADR |
|---|---|---|---|
| ADR-B-0193 | „Dokument UN” był nieprecyzyjnym określeniem i sugerował, że dokument zastępuje oznakowanie pojazdu. | Dystraktor A zmieniono na wiarygodny błąd polegający na poleganiu na danych z dokumentu; explanation podkreśla konieczność czytelnej tablicy na pojeździe. | 5.3.2.2.2 |
| ADR-B-0197 | Wyjaśnienie używało technicznego zwrotu o równoważnej skuteczności bez wyjaśnienia klas pożarów. | Dopisano proste objaśnienie pożarów A/B/C jako pożarów ciał stałych, cieczy i gazów; nie zmieniono wymagań. | 8.1.4.2; 1.1.3.6 |
| ADR-B-0223 | Odpowiedź o otwieraniu przesyłki przed oceną pożaru była zbyt absurdalna. | Zastąpiono ją częstszym błędem: zbliżeniem się do przesyłki, by odczytać nalepkę mimo zagrożenia. Explanation wskazuje bezpieczną drogę odwrotu. | 5.4.3.4 |
| ADR-B-0354 | Próbowanie substancji po smaku lub zapachu było oczywiście absurdalne. | Zastąpiono je realistycznym, lecz niebezpiecznym podejściem od strony, z której wiatr niesie opary. | 5.4.3.4 |
| ADR-B-0458 | Dystraktor o nalepce z literą „A” nie pasował do znaczenia przypisu w tabeli. | Zastąpiono go pomyłką w odczycie tabeli: przenoszeniem wartości z sąsiedniej kolumny; doprecyzowano wyjaśnienie przypisu „a”. | 1.10.3.1.2, przypis (a) |
| ADR-B-0496 | Odpowiedź o zagrożeniu żrącym była oczywiście nie na temat klasy 1. | Zastąpiono ją błędnym, ale wiarygodnym stwierdzeniem, że pożar nie niesie ryzyka wybuchu ani rozrzutu. | 2.2.1.1.5, podklasa 1.3 |
| ADR-B-0505 | Explanation nie objaśniało, gdzie znajduje się numer rozpoznawczy zagrożenia. | Dodano krótkie wyjaśnienie, że chodzi o numer w górnym polu tablicy pomarańczowej. | 5.3.2.3.1 |
| ADR-B-0577 | „Liczba pojazdów” i „kod magazynowy” były zbyt łatwe do odrzucenia. | Zastąpiono je realistycznymi pomyłkami: pominięciem liter „UN” oraz użyciem nazwy handlowej zamiast numeru. | 5.4.1.1.1(a) |

Każde zmienione explanation ma 4 zdania, 319–396 znaków, zaczyna od sensu poprawnej odpowiedzi, wyjaśnia mylące warianty i kończy podstawą ADR. ID, poprawne litery i statusy prawne pozostają bez zmian.

## 2. Wszystkie ID w próbce

- `ADR-B-0002` (ADR-B-01): bez zmiany — explanation i dystraktory wystarczająco czytelne.
- `ADR-B-0013` (ADR-B-05): bez zmiany — explanation i dystraktory wystarczająco czytelne.
- `ADR-B-0028` (ADR-B-10): bez zmiany — explanation i dystraktory wystarczająco czytelne.
- `ADR-B-0042` (ADR-B-02): bez zmiany — explanation i dystraktory wystarczająco czytelne.
- `ADR-B-0046` (ADR-B-03): bez zmiany — explanation i dystraktory wystarczająco czytelne.
- `ADR-B-0052` (ADR-B-06): bez zmiany — explanation i dystraktory wystarczająco czytelne.
- `ADR-B-0054` (ADR-B-07): bez zmiany — explanation i dystraktory wystarczająco czytelne.
- `ADR-B-0068` (ADR-B-13): bez zmiany — explanation i dystraktory wystarczająco czytelne.
- `ADR-B-0086` (ADR-B-11): bez zmiany — explanation i dystraktory wystarczająco czytelne.
- `ADR-B-0097` (ADR-B-02): bez zmiany — explanation i dystraktory wystarczająco czytelne.
- `ADR-B-0108` (ADR-B-05): bez zmiany — explanation i dystraktory wystarczająco czytelne.
- `ADR-B-0168` (ADR-B-05): bez zmiany — explanation i dystraktory wystarczająco czytelne.
- `ADR-B-0193` (ADR-B-06): poprawiono explanation; poprawiono dystraktor.
- `ADR-B-0197` (ADR-B-08): poprawiono explanation.
- `ADR-B-0221` (ADR-B-05): bez zmiany — explanation i dystraktory wystarczająco czytelne.
- `ADR-B-0223` (ADR-B-05): poprawiono explanation; poprawiono dystraktor.
- `ADR-B-0230` (ADR-B-05): bez zmiany — explanation i dystraktory wystarczająco czytelne.
- `ADR-B-0273` (ADR-B-01): bez zmiany — explanation i dystraktory wystarczająco czytelne.
- `ADR-B-0285` (ADR-B-07): bez zmiany — explanation i dystraktory wystarczająco czytelne.
- `ADR-B-0286` (ADR-B-09): bez zmiany — explanation i dystraktory wystarczająco czytelne.
- `ADR-B-0289` (ADR-B-02): bez zmiany — explanation i dystraktory wystarczająco czytelne.
- `ADR-B-0354` (ADR-B-04): poprawiono explanation; poprawiono dystraktor.
- `ADR-B-0413` (ADR-B-12): bez zmiany — explanation i dystraktory wystarczająco czytelne.
- `ADR-B-0414` (ADR-B-12): bez zmiany — explanation i dystraktory wystarczająco czytelne.
- `ADR-B-0419` (ADR-B-08): bez zmiany — explanation i dystraktory wystarczająco czytelne.
- `ADR-B-0443` (ADR-B-10): bez zmiany — explanation i dystraktory wystarczająco czytelne.
- `ADR-B-0456` (ADR-B-12): bez zmiany — explanation i dystraktory wystarczająco czytelne.
- `ADR-B-0458` (ADR-B-12): poprawiono explanation; poprawiono dystraktor.
- `ADR-B-0481` (ADR-B-07): bez zmiany — explanation i dystraktory wystarczająco czytelne.
- `ADR-B-0492` (ADR-B-09): bez zmiany — explanation i dystraktory wystarczająco czytelne.
- `ADR-B-0496` (ADR-B-02): poprawiono explanation; poprawiono dystraktor.
- `ADR-B-0499` (ADR-B-02): bez zmiany — explanation i dystraktory wystarczająco czytelne.
- `ADR-B-0505` (ADR-B-06): poprawiono explanation.
- `ADR-B-0513` (ADR-B-01): bez zmiany — explanation i dystraktory wystarczająco czytelne.
- `ADR-B-0523` (ADR-B-13): bez zmiany — explanation i dystraktory wystarczająco czytelne.
- `ADR-B-0543` (ADR-B-06): bez zmiany — explanation i dystraktory wystarczająco czytelne.
- `ADR-B-0556` (ADR-B-09): bez zmiany — explanation i dystraktory wystarczająco czytelne.
- `ADR-B-0577` (ADR-B-13): poprawiono explanation; poprawiono dystraktor.
- `ADR-B-0579` (ADR-B-13): bez zmiany — explanation i dystraktory wystarczająco czytelne.
- `ADR-B-0603` (ADR-B-11): bez zmiany — explanation i dystraktory wystarczająco czytelne.

## 3. Spójność lekcji, scenariuszy i egzaminów

- Lekcje B-01–B-13: 13/13; odwołania do pytań istnieją i należą do właściwego działu.
- Scenariusze: 39/39; wszystkie `question_ids` istnieją i odpowiadają modułowi scenariusza.
- Warianty egzaminu 001–005: po 30 unikalnych pytań; poprawione ID nie występują w arkuszach, więc nie trzeba było zmieniać ich zawartości ani mapowania liter. Zaktualizowano `source_bank_head` we wszystkich pięciu wariantach i kluczach.
- Migawki `review/legal-clauses/` i `review/sequential/` zsynchronizowano dla ośmiu zmienionych ID. Zaktualizowano bieżący manifest pakietu recenzyjnego i kolejki recenzji.

## 4. Preflight Quality Gate

- Bank: 609 pytań, unikalne ID: 609, duplikaty: 0.
- Status: 609 `needs_review`, 0 `verified`.
- Najkrótsze explanation: 300 znaków; poniżej 200: 0.
- „Poprawna odpowiedź = jedyna najdłuższa”: 72/609 = 11.82%; najwyższy wynik działu: 14.29%.

| Dział | Pytania | Poprawna = jedyna najdłuższa | Wskaźnik |
|---|---:|---:|---:|
| ADR-B-01 | 45 | 6 | 13.33% |
| ADR-B-02 | 56 | 8 | 14.29% |
| ADR-B-03 | 49 | 5 | 10.20% |
| ADR-B-04 | 46 | 6 | 13.04% |
| ADR-B-05 | 43 | 5 | 11.63% |
| ADR-B-06 | 45 | 6 | 13.33% |
| ADR-B-07 | 48 | 6 | 12.50% |
| ADR-B-08 | 42 | 4 | 9.52% |
| ADR-B-09 | 46 | 5 | 10.87% |
| ADR-B-10 | 55 | 4 | 7.27% |
| ADR-B-11 | 43 | 6 | 13.95% |
| ADR-B-12 | 44 | 6 | 13.64% |
| ADR-B-13 | 47 | 5 | 10.64% |
| **Razem** | **609** | **72** | **11.82%** |

## 5. Testy i zastrzeżenia

Lokalne klonowanie repo nadal jest niedostępne w tym środowisku z powodu błędu DNS dla `github.com`; nie deklaruję lokalnego PASS. Wykonano preflight na danych pobranych z GitHub: długości explanation, unikalność ID, rozkład długości odpowiedzi, odwołania lekcji/scenariuszy i synchronizację SHA egzaminów. Pełny test jednostkowy oraz Quality Gate GitHub Actions są wymagane przed scaleniem.

Nie stwierdzono potwierdzonego błędu prawnego wymagającego zmiany poprawnej odpowiedzi. Wszystkie pytania nadal `needs_review`; recenzja specjalisty i formalne porównanie z polskim tekstem ADR 2025 pozostają wymagane. Nie rozpoczęto kursu cystern ani innego kursu.
