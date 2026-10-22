# Plan projektu — ADR podstawowy (Polska)

Data rozpoczęcia: 22.10.2026. Priorytet: rzetelność prawnomerytoryczna i łatwa nauka, nie maksymalna liczba rekordów.

## Cel produktu

Samodzielne testy szkoleniowe i egzamin próbny dla kierowcy przygotowującego się do **kursu ADR początkowego podstawowego**. Po zamknięciu jakościowym podstawowego uruchomimy osobny zakres „cysterny”. Etap podstawowy obejmuje zarówno autorskie pytania, jak i materiały dydaktyczne oraz program wymaganych ćwiczeń praktycznych; platforma nie zastępuje formalnego szkolenia. Nie łączymy pytań egzaminu podstawowego ze specjalistycznymi.

## Twarde wymagania

- Zakres treści zgodny z urzędowym programem kursu (13 tematów, załącznik nr 1, Dz.U. 2021 poz. 2150) oraz ADR 2025 i właściwym prawem krajowym.
- Egzamin próbny: 30 pytań jednokrotnego wyboru, 3 możliwości, 60 minut, zdane od 20 poprawnych odpowiedzi (Dz.U. 2024 poz. 964, § 9–11).
- Tylko autorskie pytania z jednoznaczną odpowiedzią i prostym wyjaśnieniem; pytania graficzne dla nalepek i oznakowania.
- Pełna identyfikowalność: źródło, punkt przepisu, data ostatniej weryfikacji, recenzent, wersja ADR.
- Wyraźne oznaczenie: „autorskie materiały szkoleniowe”, nigdy „oficjalna baza pytań”, dopóki brak podstaw prawnych.
- Status zweryfikowany nie może zostać nadany automatycznie tylko dlatego, że rekord przechodzi walidację strukturalną.
- Eksport produkcyjny wykonuje osobna **bramka udokumentowanego zatwierdzenia**: zgodny zapis `verified`, dokładny skrót treści, prawdziwy recenzent/data i istniejący protokół recenzji. Baza główna może zawierać pytania robocze, ale nigdy nie mogą one trafić do eksportu.
- Dodatkowo do aktualnego ADR trzeba sprawdzać mające zastosowanie, czasowo ograniczone **umowy wielostronne** (ADR 1.5.1), [rejestr 2026](ODSTEPSTWA-ADR-2026.md).

## Etapy

| Etap | Praca | Wynik / kryterium PASS |
|---|---|---|
| 0. Fundament | Repo, dokumentacja, schemat JSONL, walidator, CI | Pliki i testy dostępne, CI PASS |
| 1. Mapa wiedzy | 13 tematów, podtematy, dokładne punkty ADR i prawa PL | Każdy temat ma mapę źródeł, brak niesprawdzonych reguł |
| 2. Prototyp | 30–50 autorskich pytań z różnych tematów, ilustracje gdy konieczne | 100% pytań ma źródła i recenzję; format bez błędów |
| 3. Produkcja | Partie 25–50 pytań; cel roboczy 400 (kwoty orientacyjne) | Dla każdej partii: audyt, brak otwartych błędów, CI PASS |
| 4. Pokrycie | Analiza luk programowych, trudności, podchwytliwych sformułowań | Każdy z 13 tematów pokryty, brak nadużywania pamięciówki |
| 5. Tryb egzaminu | Generator 30/60, rozkład pytań, wynik i objaśnienia po zakończeniu | Testy jednostkowe i scenariusze E2E PASS |
| 6. Publikacja | Eksport do platformy, weryfikacja prawna i UX | Wydanie z datą, wersją źródeł i protokołem QA |
| 7. Specjalizacja | Dopiero potem: ADR cysterny — osobny program, bank i egzaminy | Nowy zakres bez naruszania zatwierdzonej podstawy |

## Proponowany proces pojedynczej partii

1. Wybrać temat i podtemat z mapy programu.
2. Sprawdzić brzmienie ADR 2025 oraz ewentualne przepisy polskie/wyjątki.
3. Zapisać w mapie wiedzy dokładny punkt i wniosek, którego będziemy uczyć.
4. Napisać własne pytanie A/B/C, jedną prawidłową odpowiedź i dwa merytorycznie sensowne, ale błędne warianty.
5. Dodać proste wyjaśnienie i przykład z pracy kierowcy.
6. Wykonać przegląd merytoryczny: weryfikacja faktu, jednoznaczności, zakresu i wersji prawa.
7. Sprawdzić gramatykę oraz jednoznaczność; oznaczyć verified dopiero po dowodzie przeglądu.
8. Uruchomić walidator, testy, CI; odnotować commit i wyniki.
9. Każdą zmianę prawa odnieść do wszystkich zależnych pytań.

## Pokrycie kompetencji (nowe wymaganie jakościowe)

- Rejestr 106 roboczych kompetencji: `podstawowy/kompetencje.json`, z powiązaniami `question_ids`.
- `python scripts/coverage.py` sprawdza istnienie zagadnień, poprawne powiązania i liczbę pytań `verified`. Nie nadaje statusu zweryfikowanego.
- `docs/POKRYCIE-KURSU.md` śledzi 103 cele teoretyczne i 3 praktyczne (ćwiczenia nie są zaliczane przez quiz).
- Stan redakcyjny: 103/103 celów teorii mają co najmniej dwa pytania robocze, 0 ma mniej niż dwa; 13/13 lekcji ma szkic, istnieje wstępny dokument 3 scenariuszy praktycznych. **Do ukończenia pozostaje** zwiększenie głębokości pytań, niezależna recenzja całości, zatwierdzenie ćwiczeń, materiały wizualne, testy symulatora oraz weryfikacja aktualnych przepisów. Samo pokrycie tematu jednym pytaniem nie zalicza etapu.

## Strategia rozkładu pytań

Cel roboczy: około 400 pytań, **nie uznajemy jednak samej liczby za miernik kompletności**. Liczba może się zmienić po audycie. Podział w docs/PROGRAM-PODSTAWOWY.md to **wewnętrzne kwoty planowania**, nie oficjalna liczba ani skład egzaminu państwowego.

## Ryzyka i zabezpieczenia

- Nie ma potwierdzonego publicznego kompletnego katalogu pytań państwowych → nie obiecujemy identycznych z egzaminem pytań.
- Przykładowe testy ośrodków bywają nieaktualne → nie używamy ich jako podstawy prawnej.
- Pytanie bywa prawdziwe tylko przy warunkach granicznych (np. ilości, rodzaju pakowania, klasie, wyłączeniach) → warunki doprecyzować w pytaniu.
- Ilustracje oznakowania i nalepek → tworzyć własne materiały lub mieć potwierdzoną zgodę/licencję.
- Rozdział „ADR podstawowy” nie zastępuje rzeczywistego kursu, ćwiczeń praktycznych i egzaminu państwowego.

## Definicja ukończenia (Definition of Done)

- Komplet 13 tematów i pokrycie treści z programu; wszystkie zweryfikowane pytania mają dokładne odniesienie do obowiązującego przepisu.
- Zero rekordów o statusie draft / needs_review / blocked w eksporcie produkcyjnym.
- Zero błędów walidatora, testów i CI.
- Przegląd eksperta ADR oraz kontrola zmian legislacyjnych przed publikacją.
- Raport końcowy zawiera liczby pytań i wyniki kontroli, bez deklaracji niepotwierdzonych kodem.
