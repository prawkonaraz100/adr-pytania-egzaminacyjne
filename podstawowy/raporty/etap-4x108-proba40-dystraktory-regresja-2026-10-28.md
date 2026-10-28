# Etap 4x108 — próbka 40 explanation, dystraktory i regresja kursu

- Data: 2026-10-28.
- Punkt wejścia: świeży `main` po PR #566, commit `1a25c4289b4e24bd29abaad9358bacf3c072b5db`.
- Zakres: wyłącznie kurs podstawowy ADR.
- Bank końcowy tej partii: blob `685a14690ed68e7c4fff7ff741d48dffa526eb3f`, 609 pytań, wszystkie `needs_review`, 0 `verified`.
- Seed `41082026`; pełna lista próbki i wykluczeń: [JSON 4x108](etap-4x108-wykluczenia-proby.json).

## 1. Próbka 40 wyjaśnień

Próbkę wylosowano z puli 386 pytań po wykluczeniu 183 ID z raportów 4x103–4x106 oraz 40 ID próbki 4x107 (łącznie 223 wykluczone ID). Lista ma 40 unikalnych ID i jest rozłączna z tym zbiorem. Nie twierdzę, że jest w pełni rozłączna z etapami 4x84–4x102: raport 4x86 nie zachował kompletnej listy wszystkich 60 wylosowanych ID.

| Kontrola przed zmianą | Wynik |
|---|---:|
| Wyjaśnienia przeczytane w kontekście pytania, A/B/C i podstawy ADR | 40/40 |
| Długość explanation | 303–490 znaków |
| Liczba zdań | 4–6 |
| Najdłuższe zdanie | 29 słów |
| Explanation poniżej 200 znaków | 0 |
| Explanation wymagające poprawy struktury | 1 |
| Dystraktory wymagające urealnienia | 6 |

## 2. Potwierdzone poprawki

| ID | Problem i korekta | Podstawa ADR |
|---|---|---|
| ADR-B-0389 | Błędne odpowiedzi o „zniknięciu” wszystkich zasad drogowych i o samym logo armatora były zbyt łatwe do odrzucenia. Zastąpiono je wiarygodnymi, lecz nieprawidłowymi założeniami o zakresie dokumentu IMDG i wyjątku dla przewozu morskiego. | 1.1.4.2.1 |
| ADR-B-0437 | Jeden dystraktor ograniczał się do przepisów o czasie pracy kierowcy. Zastąpiono go częstszą pomyłką: stosowaniem reguł kolejowych, ale pomijaniem wymagań dla towarów niebezpiecznych. Uporządkowano też długości wszystkich opcji. | 1.1.4.5.1 |
| ADR-B-0323 | Odpowiedź „każdy przewóz mieszany automatycznie nie podlega ADR” była zbyt absurdalna. Zastąpiono ją błędem polegającym na sumowaniu ilości bez współczynników. | 1.1.3.6.4 |
| ADR-B-0342 | Dystraktor „klasa 7 nie występuje w ADR” był niewiarygodny. Zastąpiono go pomyłką w kolejności klasyfikacji; drugi dystraktor dotyczy mylenia pierwszeństwa z udziałem masowym. | 2.1.3.5.3(a) |
| ADR-B-0233 | Dane konta bankowego kierowcy i numer rejestracyjny były zbyt oczywistymi błędami. Zastąpiono je realistycznymi pomyłkami: użyciem danych nadawcy lub samego adresu rozładunku zamiast danych odbiorcy. | 5.4.1.1.1(h) |
| ADR-B-0280 | „Palenie zawsze dozwolone po wyłączeniu zapłonu” było zbyt kategoryczne. Zastąpiono to warunkową, ale błędną interpretacją przerwy w załadunku; drugi dystraktor błędnie ogranicza zakaz do tuneli E. | 8.3.5 |
| ADR-B-0319 | Explanation miało 6 zdań. Skrócono je do 4 zdań, zachowując rozróżnienie typów EX/II, EX/III, FL i AT oraz wyjaśnienie, dlaczego nie są zamienne. | 9.1.1.2 |

Wszystkie poprawne litery i podstawy ADR pozostały bez zmian. Odświeżono migawki sekwencyjne i audyty A/B/C. Nie oznaczono żadnego pytania jako `verified`.

## 3. Spójność lekcji, scenariuszy i egzaminów

- Lekcje: **13/13** — wszystkie odwołania do pytań istnieją i należą do właściwego modułu; każde pytanie banku jest wymienione w lekcji swojego działu.
- Scenariusze: **39/39** — brak brakujących ID i odwołań do innego działu; każdy scenariusz zawiera kroki kierowcy, kryteria oceny i podstawę.
- Egzaminy 001–005: każdy ma 30 unikalnych pytań, obejmuje 13 działów, rozkład klucza A/B/C 10/10/10 i maksymalną serię 3. Zmienione pytania nie występują w wariantach, więc aktualizacja ograniczyła się do metadanych `source_bank_head`. Pełne porównanie arkuszy i kluczy uruchamia CI.
- W tej partii nie wykryto potwierdzonej luki programu wymagającej nowego pytania.

## 4. Metryki po zmianach

- Bank: 609 unikalnych ID; 609 `needs_review`, 0 `verified`.
- Explanation minimum: 300 znaków; poniżej 200: 0.
- Rozkład poprawnych liter: A=206, B=207, C=196.
- Poprawna odpowiedź jest jedyną najdłuższą: **71/609 = 11,66%**.
- Maksimum w dziale: **14,29%**; wszystkie działy poniżej 18%.
- Najwyższy wskaźnik poprawnej odpowiedzi jako najkrótszej: **18/48 = 37,50%** w B-07, poniżej limitu 38%.

## 5. Testy i ograniczenia

Lokalny `git clone` nie zadziałał z powodu niedostępności sieci w środowisku lokalnym. Wykonano preflight na plikach pobranych z GitHub: metryki odpowiedzi, długość i strukturę explanation, odwołania lekcji/scenariuszy oraz synchronizację wariantów. PR wymaga PASS pełnego Quality Gate CI przed scaleniem. Pełna recenzja polskiego tekstu urzędowego i niezależna kontrola specjalisty nadal pozostają wymagane.

Nie rozpoczęto kursu cystern ani innego kursu.
