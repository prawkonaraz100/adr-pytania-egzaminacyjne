# Etap 4x230 — praktyczne łączne odczytanie tabeli A

Data: 31.10.2026. Zakres: wyłącznie kurs podstawowy ADR. Punkt wyjścia: świeży `main` `f300e9b199722095d11351e6de2bc71a11302f96`, bank 654 pytań, blob SHA `6d2b0fd39173fef829b70a5e42049104688c1604`.

## 1. Audyt luki

Bank zawierał 654 rekordy, wszystkie `needs_review`, bez `verified`. ID były ciągłe i unikalne ADR-B-0001–0654; kolejne wolne ID: ADR-B-0655. Mapa obejmuje 107 kompetencji (104 teoretyczne, 3 praktyczne). Najmniej liczebnie pokryta kompetencja to ADR-B-07-K07 (3 pytania), jednak jej zakres był już opisany w trzech odrębnych kontekstach.

Wybrałem ADR-B-02-K14 — „Grupy pakowania, zagrożenia dodatkowe, tabela A” (4 pytania przed zmianą). Dotychczasowe rekordy sprawdzały osobno kolejność grup pakowania, lokalizację klasy w tabeli A, ogólne znaczenie dwóch nalepek i kolumnę nalepek. Brakowało zadania łączącego odczyt trzech pól w jednym wpisie: klasy w kolumnie 3a, grupy pakowania w kolumnie 4 oraz nalepek w kolumnie 5. To uzupełnienie sprawdza zastosowanie, a nie tylko zapamiętanie numeru kolumny.

## 2. Nowe pytanie ADR-B-0655

Dodano ADR-B-0655 do ADR-B-02-K14. Scenariusz posługuje się fikcyjnym wpisem tabeli A i nie przypisuje tych wartości do konkretnego numeru UN.

**Pytanie:** Kierowca sprawdza wpis towaru w tabeli A. W kolumnie 3a widzi klasę 3, w kolumnie 4 grupę II, a w kolumnie 5 numery nalepek 3 i 6.1. Jak powinien odczytać te dane?

| Opcja | Długość | Ocena |
|---|---:|---|
| A | 142 | Błędna — zamienia znaczenie klasy i grupy pakowania oraz twierdzi, że nalepka dodatkowa zastępuje podstawową. |
| B | 130 | Błędna — dwie nalepki nie oznaczają automatycznie dwóch oddzielnych towarów. |
| C | 116 | **Poprawna** — klasa wskazuje rodzaj zagrożenia, grupa pakowania jego stopień, a nalepki wskazują zagrożenie główne i dodatkowe. |

Poprawna odpowiedź C nie jest najdłuższa. Explanation ma 399 znaków i 4 zdania; najpierw wyjaśnia praktyczne znaczenie pól, następnie rolę obu nalepek i odróżnienie jednego towaru od dwóch, a na końcu wskazuje podstawę ADR. Status pozostaje `needs_review`.

## 3. Źródła i zakres prawny

- ADR 2025, 2.1.1.3 — kryteria grup pakowania.
- ADR 2025, 3.2.1, tabela A, kolumny (3a)–(5) — klasa, grupa pakowania i numery nalepek.
- ADR 2025, 5.2.2.1.1 — stosowanie nalepek dla zagrożenia głównego i dodatkowego.
- Oficjalne ogłoszenie: Dz.U. 2025 poz. 642, https://dziennikustaw.gov.pl/DU/2025/642
- Polska wersja pomocnicza ADR 2025 opublikowana przez Ministerstwo Infrastruktury: https://www.gov.pl/web/infrastruktura/towary-niebezpieczne (strona wyraźnie wskazuje, że źródłem prawa jest tekst ogłoszony w Dzienniku Ustaw).

Nie przypisano przykładowej kombinacji do rzeczywistego UN. Pełne porównanie każdego zdania z urzędowym tekstem polskim i sprostowaniem Dz.U. 2025 poz. 1575 oraz niezależna recenzja specjalisty pozostają otwarte. Wpis ledgeru 0655 ma status `not_retrieved_not_literally_compared`; nie jest dowodem weryfikacji prawnej.

## 4. Materiały i synchronizacja

- Mapa: ADR-B-0655 przypisano do ADR-B-02-K14 (5 pytań w kompetencji).
- Lekcja i materiał instruktora ADR-B-02: dodano wyjaśnienie zintegrowanego odczytu i ćwiczenie na fikcyjnym wpisie tabeli A.
- Bank: 655 rekordów ADR-B-0001–0655, ID ciągłe i unikalne; wszystkie `needs_review`, 0 `verified`.
- Blob SHA banku: `ca07d9e94b63ba6b9f832838e645500bd2964939`.
- Rozkład prawidłowych odpowiedzi: A=223, B=220, C=212.
- Wskaźnik „poprawna jest jedyną najdłuższą”: 72/655 = 10,99%; maksimum działu 13,95%.
- Warianty i klucze egzaminów próbnych 001–005 wskazują nowy blob SHA banku.
- Snapshoty dodano jako `review/sequential/655-655.json` i `review/legal-clauses/655-655.json`; pełny zakres audytów pokrywa 655 pytań.
- Ledger źródeł rozszerzono do `review/legal-polish/stage4w4-literal-verification-ledger-0610-0655.json`; manifesty pakietów 0628 i 0638 wskazują nowy SHA, 655 rekordów i 0 zatwierdzeń.

## 5. Walidacja i ograniczenia wykonania

Kontrola w tej sesji potwierdziła ręcznie: 655 poprawnych rekordów JSONL, ciągłość ID 0001–0655, brak duplikatów, status `needs_review` dla wszystkich rekordów, 107 kompetencji i zgodność przypisania nowego ID do działu B-02. Sprawdzono długości A/B/C i explanation oraz zaktualizowano klucze, snapshoty i manifesty.

Lokalne uruchomienie skryptów Quality Gate nie było dostępne w tej sesji: połączenie GitHub umożliwiało odczyt i zapis repozytorium, ale nie udostępniało lokalnego checkoutu ani terminala repo. Nie deklaruję zatem lokalnego PASS. PR musi przejść pełny CI/Quality Gate przed scaleniem; w razie błędu należy poprawić ten sam PR.

Nie zmieniono statusów prawnych, nie oznaczono żadnego rekordu `verified`. Zakres wyłącznie kurs podstawowy ADR; bez kursu cystern.
