# Etap 4x109 — próbka 40 explanation, dystraktory, scenariusze i egzaminy

- Data: 2026-10-28.
- Punkt wejścia: świeży `main` po scaleniu PR #567, commit `cffa51ee02a8c7f39709032f2595c13811c44a2d`.
- Zakres: wyłącznie kurs podstawowy ADR.
- Bank po zmianach: 609 pytań, blob `6fd194bfc51ff19c38e4dee598a9fae499e953a3`; wszystkie `needs_review`, 0 `verified`.
- Seed próbki: `41092026`; manifest i jawne wykluczenia: [JSON 4x109](etap-4x109-wykluczenia-proby.json).

## 1. Próba 40 explanation

Próbę wylosowano deterministycznie z puli po wykluczeniu 263 ID jawnie zapisanych w rejestrze 4x108 (zbiór obejmuje znane ID z etapów 4x103–4x108). Pula po wykluczeniu: 346; wylosowano 40 unikalnych ID. Pełna lista znajduje się w JSON.

- Przeczytano ręcznie w kontekście pytania, opcji A/B/C, poprawnej litery i podstawy ADR: **40/40**.
- Długość explanation w banku po korektach: minimum 300 znaków; poniżej 200: 0.
- Cztery pytania wymagały poprawy: w każdym urealniono dystraktory i dopasowano explanation. Pozostałe 36 wyjaśnień pozostawiono bez zmian, bo jasno tłumaczyły poprawną odpowiedź, główne błędne tropy i podstawę ADR.
- Ograniczenie doboru: rozłączność jest potwierdzona względem ID jawnie wymienionych w 4x103–4x108; nie można dowieść rozłączności względem 4x84–4x102, ponieważ raport 4x86 nie publikuje pełnej listy 60 ID.

## 2. Potwierdzone poprawki pytań

| ID | Problem | Zmiana | Podstawa ADR |
|---|---|---|---|
| ADR-B-0194 | Pytanie powtarzało praktycznie ADR-B-0053: obie pozycje pytały, co oznacza pojedyncza cyfra 8. | Przeredagowano je tak, aby sprawdzało odrębny aspekt: znaczenie powtórzenia cyfry w numerze 88. Dystraktory dotyczą błędnego rozumienia dwóch cyfr, a explanation wyjaśnia nasilenie zagrożenia żrącego. ID i poprawna litera C bez zmian. | ADR 5.3.2.3.1 |
| ADR-B-0575 | Dystraktory „numer rejestracyjny pojazdu” i „kod pocztowy odbiorcy” były mało wiarygodne i łatwe do odrzucenia bez znajomości tabeli A. | Zastąpiono je pomyłką kolumny 14 (kategoria transportowa) i kolumny 4 (grupa pakowania). Poprawna litera C bez zmian; explanation rozróżnia funkcję kolumn. | ADR 3.2.1, tabela A, kolumny 4, 14 i 15; 8.6.3.1 |
| ADR-B-0561 | Pytanie było niemal duplikatem ADR-B-0299: oba pytały ogólnie o rozmieszczenie nalepek na kontenerze. | Zmieniono je w scenariusz kontroli przed wyjazdem: brak nalepek na obu końcach mimo oznakowania boków. Poprawna litera A bez zmian; explanation wyjaśnia, że dokument nie zastępuje oznakowania fizycznego. | ADR 5.3.1.1.4 |
| ADR-B-0083 | „Dwa kartony” był przypadkowym dystraktorem w pytaniu o ograniczenie tunelowe. | Zastąpiono go częstą pomyłką, że kod E dotyczy tylko cystern; druga opcja sprawdza błędne założenie, że pora dnia znosi ograniczenie. Poprawna litera C bez zmian. | ADR 8.6.4 |

Nie zmieniano ID, kluczy w banku ani statusów recenzji. Odświeżono snapshoty sekwencyjne i audytu A/B/C dla wszystkich trzech rekordów. W banku explanation tych trzech pozycji mają odpowiednio 315, 388 i 311 znaków.

## 3. Kontrola scenariuszy praktycznych

Sprawdzono strukturę wszystkich 39 scenariuszy z `podstawowy/praktyka/scenariusze-13-dzialow.json`:
- wymagane pola sytuacji, kroków, typowych błędów, podstawy ADR, kryteriów oceny i wniosku dla kursanta: 39/39;
- co najmniej 3 kroki kierowcy: 39/39;
- istniejące `question_ids` należące do właściwego modułu: 39/39.
Nie wykryto brakujących odwołań ani potwierdzonego błędu wymagającego zmiany scenariusza.

## 4. Egzaminy próbne 001–005

Pierwszy preflight oparty na bezpośrednim porównaniu ciągów wskazał pozorną różnicę przy ADR-B-0489. Po zastosowaniu mapowania liter z arkusza (tak jak robi to `check_mock_exam_variants.py`) potwierdzono, że klucz był zgodny; nie zmieniano go merytorycznie. Po zmianie banku zsynchronizowano `source_bank_head` we wszystkich wariantach i kluczach 001–005. Wariant 005 zawiera ADR-B-0575, więc jego opcje i explanation klucza zaktualizowano zgodnie z nowym brzmieniem pytania i mapowaniem liter.

## 5. Metryki po zmianach

- Bank: 609 rekordów, 609 unikalnych ID, 0 duplikatów ID.
- Statusy: 609 `needs_review`, 0 `verified`.
- Explanation: minimum 300 znaków; poniżej 200 znaków: 0.
- „Poprawna = jedyna najdłuższa”: 72/609 = 11.82% globalnie.
- Wskaźniki per dział:
  - ADR-B-01: 6/45 = 13.33%.
  - ADR-B-02: 8/56 = 14.29%.
  - ADR-B-03: 6/49 = 12.24%.
  - ADR-B-04: 5/46 = 10.87%.
  - ADR-B-05: 5/43 = 11.63%.
  - ADR-B-06: 6/45 = 13.33%.
  - ADR-B-07: 6/48 = 12.50%.
  - ADR-B-08: 5/42 = 11.90%.
  - ADR-B-09: 4/46 = 8.70%.
  - ADR-B-10: 4/55 = 7.27%.
  - ADR-B-11: 6/43 = 13.95%.
  - ADR-B-12: 6/44 = 13.64%.
  - ADR-B-13: 5/47 = 10.64%.
- Wszystkie działy poniżej 18%; maksimum: 14.29%.

## 6. Testy i ograniczenia

Próba lokalnego `git clone` i uruchomienia testów nie powiodła się, ponieważ środowisko nie rozwiązuje hosta `github.com` (błąd DNS). Nie deklaruję lokalnego PASS. Przed scaleniem wymagany jest pełny PASS GitHub Actions Quality Gate, obejmujący testy banku, audytów, scenariuszy i synchronizacji egzaminów.

Nie oznaczono żadnego pytania jako `verified`; niezależna kontrola polskiego tekstu urzędowego i odbiór specjalisty ADR pozostają wymagane.
