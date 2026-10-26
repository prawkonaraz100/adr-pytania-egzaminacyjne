# Etap 4x42 — scenariusze kursanta i spójność kluczy egzaminów

- Data: 2026-10-26.
- Bazowy `main`: `dd73baf47d60b2e4f7e7d07a83682fec3f71c9f3`.
- Zakres: wyłącznie kurs podstawowy ADR. Bank pytań i poprawne litery nie zostały zmienione.

## 1. Przegląd scenariuszy

W `podstawowy/praktyka/scenariusze-13-dzialow.json` jest 39 scenariuszy: po 3 na każdy z 13 działów. Każdy z 39 rekordów zawiera wymagane pola: sytuację, kroki, typowe błędy, podstawę ADR, powiązane ID pytań, kryteria oceny i wniosek dla kursanta. Automatyczna kontrola referencji nie wykazała brakujących ID ani pytań przypisanych do niewłaściwego działu.

W każdej lekcji jest również własna sekcja „Scenariusze praktyczne”; w przejrzanych plikach znalazłem 4–5 scenariuszy inline na lekcję. Treść uczy kolejności działania, wyjaśnia dlaczego należy zatrzymać czynność, sprawdzić dokumenty albo wezwać pomoc i oznacza ćwiczenia jako symulacje, nie jako dowód zaliczenia praktyki.

| Lekcja | Scenariusze w JSON | Scenariusze w tekście lekcji | Wniosek |
|---|---:|---:|---|
| ADR-B-01 | 3 | 5 | Brak potwierdzonej luki wymagającej dopisywania kolejnych scenariuszy |
| ADR-B-02 | 3 | 4 | Brak potwierdzonej luki wymagającej dopisywania kolejnych scenariuszy |
| ADR-B-03 | 3 | 4 | Brak potwierdzonej luki wymagającej dopisywania kolejnych scenariuszy |
| ADR-B-04 | 3 | 5 | Brak potwierdzonej luki wymagającej dopisywania kolejnych scenariuszy |
| ADR-B-05 | 3 | 5 | Brak potwierdzonej luki wymagającej dopisywania kolejnych scenariuszy |
| ADR-B-06 | 3 | 4 | Brak potwierdzonej luki wymagającej dopisywania kolejnych scenariuszy |
| ADR-B-07 | 3 | 4 | Brak potwierdzonej luki wymagającej dopisywania kolejnych scenariuszy |
| ADR-B-08 | 3 | 5 | Brak potwierdzonej luki wymagającej dopisywania kolejnych scenariuszy |
| ADR-B-09 | 3 | 4 | Brak potwierdzonej luki wymagającej dopisywania kolejnych scenariuszy |
| ADR-B-10 | 3 | 4 | Brak potwierdzonej luki wymagającej dopisywania kolejnych scenariuszy |
| ADR-B-11 | 3 | 4 | Brak potwierdzonej luki wymagającej dopisywania kolejnych scenariuszy |
| ADR-B-12 | 3 | 4 | Brak potwierdzonej luki wymagającej dopisywania kolejnych scenariuszy |
| ADR-B-13 | 3 | 4 | Brak potwierdzonej luki wymagającej dopisywania kolejnych scenariuszy |

Przykłady sprawdzonych sytuacji obejmują: weryfikację wyłączenia ilościowego przed wyjazdem; przesyłkę klasy 4.3 i kontakt z wodą; wyciek przy kanalizacji; silnik i e-papieros przy załadunku; gaśnicę niedostępną; nieczytelną nalepkę; wadliwe opakowanie; mocowanie ładunku; dokument morski dla dalszego odcinka drogowego; ograniczenie tunelowe; nieuprawnionego odbiorcę i niekompletny dokument przewozowy.

## 2. Egzaminy próbne 001–005

Każdy wariant ma 30 pytań i odpowiadający mu klucz. Przed zmianą klucze zawierały poprawną odpowiedź, explanation i podstawę prawną, ale nie miały bezpośredniego odnośnika do lekcji działu. Dodano do wszystkich 150 odpowiedzi pole `lesson_path`, np. `../lekcje/ADR-B-07.md`.

- Warianty: 5.
- Odpowiedzi w kluczach: 150.
- ID nieobecne w banku: 0.
- Explanation krótsze niż 200 znaków: 0.
- Odpowiedzi z linkiem do istniejącej lekcji właściwego modułu: 150/150.
- Bank, pytania, poprawne litery i explanation nie zmieniły się.

Po błędzie kursant może przeczytać explanation, otworzyć bezpośrednio lekcję z tego samego działu, wrócić do trzech scenariuszy i dopiero potem powtórzyć egzamin. Nie trzeba zgadywać, która lekcja omawia dane pytanie.

## 3. Quality Gate i testy

Zaktualizowano `scripts/check_mock_exam_variants.py`, aby sprawdzał, czy każdy wpis klucza ma `lesson_path` zgodny z `module_id` banku i czy docelowy plik lekcji istnieje. Dodano też test regresyjny w `tests/test_learning_traceability.py` dla wszystkich 150 odpowiedzi.

### Metryki banku

| Dział | Pytań | Poprawna = jedyna najdłuższa | Najkrótsze explanation |
|---|---:|---:|---:|
| ADR-B-01 | 45 | 13.33% (6/45) | 300 znaków |
| ADR-B-02 | 56 | 12.50% (7/56) | 300 znaków |
| ADR-B-03 | 49 | 14.29% (7/49) | 300 znaków |
| ADR-B-04 | 46 | 13.04% (6/46) | 301 znaków |
| ADR-B-05 | 43 | 11.63% (5/43) | 300 znaków |
| ADR-B-06 | 45 | 11.11% (5/45) | 301 znaków |
| ADR-B-07 | 48 | 12.50% (6/48) | 304 znaków |
| ADR-B-08 | 42 | 11.90% (5/42) | 303 znaków |
| ADR-B-09 | 46 | 8.70% (4/46) | 301 znaków |
| ADR-B-10 | 55 | 7.27% (4/55) | 308 znaków |
| ADR-B-11 | 43 | 13.95% (6/43) | 300 znaków |
| ADR-B-12 | 44 | 13.64% (6/44) | 303 znaków |
| ADR-B-13 | 47 | 10.64% (5/47) | 308 znaków |
| **Razem** | **609** | **11,82%** | **300 znaków** |

- Duplikaty ID: 0.
- Explanation poniżej 200 znaków: 0.
- Status pytań: 609 `needs_review`, 0 `verified`.
- Najwyższy wskaźnik działu: 14,29% (B-03), poniżej limitu 18%.

## 4. Pytania nowe i kwestie prawne

Nie dodano pytań: przegląd struktury scenariuszy i referencji nie ujawnił konkretnej luki w programie, którą można bezpiecznie uzupełnić na podstawie potwierdzonego przepisu. Nie zmieniano treści ani statusu pytań na podstawie samego przeglądu dydaktycznego. Potwierdzenie poprawności prawnej nadal należy do specjalisty ADR.

## 5. Ograniczenie wykonania

Zmiany wykonano przez GitHub. Lokalnego środowiska repozytorium nie udostępnia ten kanał pracy, dlatego nie deklaruję lokalnego PASS. Rozstrzygające są wymagane testy i pełny Quality Gate CI uruchomione na PR; raport należy uzupełnić po ich wyniku.
