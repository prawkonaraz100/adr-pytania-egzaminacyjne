# Etap 4x120 — próbka 40, dystraktory i synchronizacja

- Data: 2026-10-28.
- Punkt wejścia: świeży `main` po PR #580, commit `109dfac0134ce81adc527751aa0bd359cc17da4a`.
- Bank po poprawkach: 609 pytań; blob SHA `04ace7f478868d0901bbc45fb26af3d866e18538`; wszystkie `needs_review`, 0 `verified`.
- Próbka: 40 ID, seed `411202026`, kandydaci po wykluczeniu 450 unikalnych ID: 159.
- Explanation w próbce: 40/40 przeczytano; 4 wymagały dopasowania po zmianie dystraktorów, bo każde wyjaśnienie ma 2–5 zdań, co najmniej 300 znaków, najpierw wyjaśnia sens odpowiedzi, omawia mylące warianty i kończy podstawą.
- Dystraktory: 4 pytania z bieżącej próbki poprawiono; dodatkowo 5 celowanych follow-upów poza próbą, gdyż w tych pytaniach znaleziono oczywiste lub słabo dydaktyczne błędne opcje.

## Zmiany w dystraktorach

| ID | Zmiana | Dlaczego |
|---|---|---|
| ADR-B-0163 | Opcja A zmieniona z testowania wycieku gołą ręką na podejście z bliska w celu oceny sytuacji. | Błąd pozostaje wiarygodny dla początkującego, ale nie jest absurdalny; poprawna odpowiedź nadal podkreśla bezpieczeństwo. |
| ADR-B-0305 | Opcje B/C zastąpiono niedostatecznymi środkami ochrony i ograniczeniem zabezpieczeń tylko do jazdy. | Sprawdzają typowe błędy: uznanie zamknięcia pojazdu za wystarczające oraz pomijanie postoju. |
| ADR-B-0532 | Opcję C zmieniono na wpis „pusty” bez informacji o ostatniej zawartości. | To bardziej realistyczne pominięcie dokumentacyjne niż przypadkowy kod magazynowy. |
| ADR-B-0373 | Opcje B/C zmieniono na „ustalenie oddzielenia po załadunku” i założenie, że szczelne opakowanie znosi zasady wspólnego załadunku. | Dystraktory testują mylenie kolejności kontroli i nadmierne poleganie na szczelności. |
| ADR-B-0003 | Dopracowano opcję B dotyczącą zastępowania prawa jazdy zaświadczeniem ADR. | Celuje w częste mylenie dwóch różnych dokumentów. |
| ADR-B-0073 | Dopracowano opcję C o rzekomym zniesieniu obowiązku gaśnicy przez wyłączenie 1.1.3.6. | Sprawdza błędne uogólnienie zakresu wyłączenia. |
| ADR-B-0147 | Dopracowano opcję C dotyczącą traktowania zestawu jako jednostki tylko z pustą naczepą. | Sprawdza błędne ograniczenie definicji jednostki transportowej. |
| ADR-B-0192 | Dopracowano opcję C o rzekomym zwolnieniu z ADR przy powtórzonej cyfrze. | Sprawdza mylenie oznaczenia nasilenia zagrożenia z wyłączeniem. |
| ADR-B-0418 | Dopracowano opcję C o zastępowaniu gaśnicy szkoleniem. | Sprawdza mylenie kompetencji człowieka z wymaganym wyposażeniem. |

ID, poprawne litery, podstawy prawne i statusy weryfikacji pozostały bez zmian. Dla wszystkich dziewięciu pytań zsynchronizowano migawki audytu `review/legal-clauses` i `review/sequential`; warianty i klucze 001–005 wskazują aktualny SHA banku.

## Wynik próbki

- Przejrzano 40 pytań z 13 działów; 36 pozostawiono bez zmian, a 4 pytania w próbie otrzymały poprawione dystraktory.
- Dodatkowe 5 follow-upów nie wlicza się do próbki 40.
- Explanation przepisane/dopasowane: 4; minimum explanation w całym banku: 300 znaków; poniżej 200: 0.
- Bank: 609 rekordów, 0 zduplikowanych ID, 609 `needs_review`, 0 `verified`.

## Wskaźnik długości odpowiedzi

„Poprawna = jedyna najdłuższa”: 70/609 = 11.49%; maksimum działu 14.29%.

| Dział | Pytania | Poprawna jedyną najdłuższą | Odsetek |
|---|---:|---:|---:|
| ADR-B-01 | 45 | 6 | 13.33% |
| ADR-B-02 | 56 | 8 | 14.29% |
| ADR-B-03 | 49 | 5 | 10.20% |
| ADR-B-04 | 46 | 6 | 13.04% |
| ADR-B-05 | 43 | 5 | 11.63% |
| ADR-B-06 | 45 | 6 | 13.33% |
| ADR-B-07 | 48 | 7 | 14.58% |
| ADR-B-08 | 42 | 3 | 7.14% |
| ADR-B-09 | 46 | 5 | 10.87% |
| ADR-B-10 | 55 | 4 | 7.27% |
| ADR-B-11 | 43 | 6 | 13.95% |
| ADR-B-12 | 44 | 5 | 11.36% |
| ADR-B-13 | 47 | 6 | 12.77% |

## Spójność lekcji, scenariuszy i egzaminów

- 13 lekcji i 39 scenariuszy pozostają bez zmian merytorycznych; pytania nie zmieniły ID ani poprawnej litery.
- Warianty i klucze 001–005 zachowują zestawy 30 ID, kolejność ID w wariancie i kluczu jest zgodna, a klucze nie wymagają remapowania liter.
- Odświeżono `source_bank_head` w każdym wariancie i kluczu do SHA `04ace7f478868d0901bbc45fb26af3d866e18538`.
- Zmienione migawki audytu zachowują `needs_review`; żadne pytanie nie zostało oznaczone jako `verified`.

## Ograniczenia próbkowania

Manifest wyklucza wszystkie ID zapisane w dostępnych manifestach 4x107–4x119 oraz zapisane dodatkowe follow-upy. Dla 4x103–4x106 nie znaleziono oddzielnych manifestów z kompletną listą ID, więc nie deklaruję potwierdzonej rozłączności z ewentualnymi nieujętymi rekordami z tych etapów. Szczegóły seed, puli i listy ID są w `etap-4x120-wykluczenia-proby.json`.

## Testy

Lokalne testy nie mogły zostać uruchomione, ponieważ środowisko nie rozwiązuje `github.com` podczas klonowania. Dlatego wymagany jest pełny Quality Gate CI przed scaleniem.
