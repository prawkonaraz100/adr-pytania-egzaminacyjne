# Etap 4x86 — próbka 60, spójność kursu i synchronizacja pakietu

- Data: 27.10.2026.
- Gałąź: `stage4x86-audit60-consistency-20261027`.
- Zakres: wyłącznie kurs podstawowy ADR.
- Aktualny blob SHA `podstawowy/questions.jsonl` po poprawce końcowej: `a8650eb0fa9c24112f2d640d5a9dca04d10ccd2a`.
- Bank: 609 pytań ADR-B-0001–ADR-B-0609; wszystkie `needs_review`, 0 `verified`, 0 formalnych zatwierdzeń.

## 1. Próbka redakcyjna i spójność banku

Przejrzano deterministyczną próbkę 60 wyjaśnień spoza ID wymienionych w dostępnych raportach 4x84 i 4x85. W czterech pytaniach poprawiono treść/dystraktory i explanation; w dwóch dodatkowych ujednolicono terminologię. Poprawna litera nie została zmieniona.

| ID | Potwierdzony problem | Korekta | Podstawa zapisana w rekordzie |
|---|---|---|---|
| ADR-B-0021 | Błędne odpowiedzi były absurdalne („obsługa parkingu”, „przypadkowy kierowca”) i nie sprawdzały rozumienia ról | Zastąpiono je wiarygodnymi pomyłkami: zakres obowiązków przewoźnika i załadowcy; klucz B bez zmian | ADR 1.4.2.1.1(a) |
| ADR-B-0208 | Jedna błędna odpowiedź opisywała kod tunelowy poprawnie, co tworzyło ryzyko drugiej odpowiedzi poprawnej | Zmieniono A na mylenie kodu tunelowego z grupą pakowania; klucz C bez zmian | ADR 3.2 tabela A, kolumna 15; 8.6.3.1 i 8.6.4 |
| ADR-B-0341 | Pytanie i dystraktory były nieprecyzyjne; explanation miało 289 znaków i nie wyjaśniało wprost obu kuszących błędów | Urealniono sytuację klasyfikacji odpadu i dopisano, dlaczego podobna nazwa oraz opakowanie nie wystarczają; klucz C bez zmian | ADR 2.1.3.5.5 |
| ADR-B-0372 | Niespójny termin „nalepki wielkiego formatu” | Ujednolicono na „nalepki dużego formatu”; klucz A bez zmian | ADR 1.4.3.7.1(e) |
| ADR-B-0387 | Niespójny termin „nalepki wielkiego formatu” i skrótowe odwołanie do ADR | Ujednolicono termin oraz zapis przepisu w treści pytania; klucz A bez zmian | ADR 1.1.4.2.2 i 5.3.2 |
| ADR-B-0501 | Dystraktory o tablicy rejestracyjnej i długości pojazdu były absurdalne | Zastąpiono je pomyłkami dotyczącymi ochrony przed uszkodzeniem mechanicznym i różnicy między ogniwami litowymi a sodowo-jonowymi; klucz A bez zmian | ADR 2.2.9.1.7.2(c) |

Pozostałe 54 pozycje próbki nie wymagały potwierdzonej korekty redakcyjnej. To nie jest formalna recenzja prawna; pełne porównanie wszystkich 609 rekordów z urzędowym tekstem ADR nadal pozostaje wymagane.

## 2. Scenariusze praktyczne

Sprawdzono strukturę bieżącego pliku scenariuszy: 39 rekordów, po 3 dla każdego z 13 działów. W poprzednim odbiorze 4x85 potwierdzono dla 39/39 sytuację, cztery kroki kierowcy, typowe błędy z wyjaśnieniem, podstawę ADR, kryteria oceny i pytania z właściwego działu. W tej partii nie znaleziono potwierdzonej luki wymagającej zmiany scenariusza.

## 3. Egzaminy próbne i pakiet recenzyjny

Po zmianach banku zsynchronizowano pole `source_bank_head` w wariantach i kluczach 001–005. Zmieniono je na bieżący blob banku po końcowej poprawce explanation. Warianty pozostają treningowe, a nie oficjalne.

- 5 wariantów × 30 pytań; wszystkie 13 działów w każdym wariancie.
- Rozkład odpowiedzi A/B/C w każdym wariancie: 10/10/10; maksymalna seria tej samej litery: 3.
- 150 różnych ID pomiędzy wariantami; brak powtórzeń wewnątrz wariantów.
- Manifest, indeks specjalisty, kolejki priorytetowe oraz trzy przewodniki recenzyjne zaktualizowano do bieżącego SHA.
- Nie zmieniono żadnego statusu na `verified`.

## 4. Quality Gate — kontrole obliczone na aktualnym banku

| Kontrola | Wynik |
|---|---:|
| Liczba rekordów | 609 |
| Duplikaty ID | 0 |
| `needs_review` / `verified` | 609 / 0 |
| Najkrótsze explanation | 300 znaków |
| Explanation poniżej 300 znaków | 0 |
| Poprawna odpowiedź jest jedyną najdłuższą | 73/609 = 11,99% |
| Najwyższy wynik działu | B-02 i B-03: 14,29% |
| B-01 | 6/45 = 13,33% |
| B-04 | 6/46 = 13,04% |

Wszystkie 13 działów mieści się poniżej 18%; B-01 i B-04 pozostają poniżej 14%. Wyniki są obliczeniami redakcyjnymi, nie dowodem prawnej poprawności.

## 5. Naprawa CI i testy

Pierwszy Quality Gate na commit `f2f3ed2` wykazał cztery niepowodzenia:
1. trzy kontrole integralności pakietu recenzyjnego nie znajdowały nowego SHA banku w `review/specialist/INSTRUKCJA-RECENZJI.md`, `review/specialist/PRZEKAZANIE-ETAP4.md` i `review/README.md`;
2. explanation ADR-B-0341 miało 289 znaków, podczas gdy test wymaga minimum 300.

Naprawiono wszystkie cztery przyczyny: uaktualniono migawki w przewodnikach i rozszerzono explanation ADR-B-0341 do 412 znaków. Po zmianie bank ma SHA `a8650eb0fa9c24112f2d640d5a9dca04d10ccd2a); ten SHA przeniesiono także do manifestu, indeksu, kolejek i wszystkich wariantów/kluczy egzaminu.

Próba uruchomienia pełnych testów lokalnie nie powiodła się, ponieważ środowisko nie mogło rozwiązać hosta `github.com` podczas `git clone` (błąd DNS). Nie deklaruję lokalnego PASS. Wymagany jest końcowy, zielony CI Quality Gate dla tego PR przed scaleniem.

## Ograniczenia i status

- Zakres obejmuje tylko kurs podstawowy ADR.
- Nie dodano nowych pytań i nie zmieniono poprawnych liter.
- Wszystkie pytania pozostają `needs_review`; 0 `verified`.
- Automatyczne testy, kontrola redakcyjna i scenariusze nie zastępują niezależnej recenzji specjalisty na podstawie polskiego tekstu ADR 2025 (Dz.U. 2025 poz. 642) oraz sprostowania Dz.U. 2025 poz. 1575.
