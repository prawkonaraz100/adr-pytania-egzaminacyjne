# Etap 4x6 — raport końcowy: ścieżka kursanta, spójność i pakiet recenzyjny

Data: 25.10.2026. Zakres: wyłącznie kurs podstawowy ADR.
Punkt wyjścia: świeży `main` `5d9594c8c4b76c3168104c0862d1152eb1d1097c`.

## 1. Materiały instruktora

Materiały instruktora B-01–B-13 uzupełniono w trzech partiach:
- [B-01–B-04](etap-4x6-instruktor-01-04-2026-10-25.md), PR #323;
- [B-05–B-08](etap-4x6-instruktor-05-08-2026-10-25.md), PR #324;
- [B-09–B-13](etap-4x6-instruktor-09-13-2026-10-25.md), PR #325.

Każdy plik instruktora zawiera trzy scenariusze działu, opis prowadzenia, kroki, kryteria obserwacji, typowe błędy i proste wyjaśnienia, granice bezpieczeństwa, question_ids oraz pytania kontrolne. ID kompetencji i odniesienia z mapy zestawiono z `podstawowy/kompetencje.json` i odsyłaczami do lekcji. Nie zmieniano pytań ani podstaw prawnych bez potwierdzonej rozbieżności.

Repo nie rejestruje wyników rzeczywistych kursantów. Pytania wskazane do dodatkowego omówienia są kandydatami tematycznymi, nie rankingiem empirycznej trudności.

## 2. Ścieżka kursanta

W `podstawowy/README.md` opisano stałą kolejność:
1. lekcja działu;
2. pytania działu i ich explanation;
3. trzy scenariusze właściwego działu;
4. egzaminy próbne 001–005 z odpowiednim kluczem;
5. powrót do lekcji i tematów, w których kursant popełnił błąd.

Wyjaśniono, jak czytać explanation po błędnej odpowiedzi: ustalić powód poprawności, porównać go z wybraną odpowiedzią, rozpoznać błąd dystraktora i sprawdzić wskazaną podstawę ADR. Dodano bezpośrednie linki do wszystkich pięciu arkuszy i kluczy.

Każda lekcja B-01–B-13 zawiera teraz jawne ID wszystkich trzech scenariuszy oraz link do `scenariusze-13-dzialow.json`. Zaktualizowano także `podstawowy/praktyka/SCENARIUSZE.md`, z indeksem 39 scenariuszy i opisem kolejności nauki.

## 3. Nowa kontrola Quality Gate

Dodano `validate_learning_material_links` do `scripts/course_consistency.py` i test integracyjny w `tests/test_course_consistency.py`. Bramka sprawdza dla każdego z 13 działów:
- istnienie lekcji i pliku instruktora;
- link do mapy scenariuszy oraz obecność wszystkich trzech ID scenariuszy tego działu;
- czy każde ID pytania w lekcji i materiale instruktora istnieje w `questions.jsonl`;
- czy każde z tych pytań należy do właściwego modułu.

Test jest uruchamiany przez istniejący krok `python -m unittest discover -s tests -v` w Quality Gate CI.

## 4. Pakiet recenzyjny

Zaktualizowano:
- `review/specialist/PAKIET-0609-MANIFEST.json` — 609 pytań, 39 scenariuszy (3 na dział), pliki pięciu wariantów i pięciu kluczy, materiały lekcji/instruktora i dodatkowe kryteria odbioru;
- `review/specialist/PRZEKAZANIE-ETAP4.md` — aktualny aneks przekazania specjaliście;
- `review/specialist/INSTRUKCJA-RECENZJI.md` — aktualny zakres, indeks 0001–0609 i lista kontroli.

Specjalista ma osobno sprawdzić treść pytania, A/B/C, explanation, dokładną podstawę w polskim ADR 2025 wraz ze sprostowaniem, zgodność scenariuszy z pytaniami, oraz synchronizację pięciu wariantów i kluczy. Wskazane pliki:
- `podstawowy/questions.jsonl`;
- `review/specialist/REJESTR-AKTUALNY-0001-0609.md`;
- `review/specialist/PAKIET-0609-MANIFEST.json`;
- `review/legal-polish/stage4w4-literal-verification-ledger-0001-0609.json`;
- `podstawowy/lekcje/ADR-B-01.md` … `ADR-B-13.md`;
- `podstawowy/instruktor/ADR-B-01.md` … `ADR-B-13.md`;
- `podstawowy/praktyka/scenariusze-13-dzialow.json` i `SCENARIUSZE.md`;
- `podstawowy/egzamin-probny/wariant-001.json` … `wariant-005.json`;
- `podstawowy/egzamin-probny/klucz-001.json` … `klucz-005.json`.

## 5. Stan i ograniczenia

- Bank: 609 pytań, 609 `needs_review`, 0 `verified`.
- Praktyka: 39 scenariuszy, dokładnie 3 w każdym dziale; dodatkowe ćwiczenia P1–P3 pozostają osobnym wymaganiem praktycznym.
- Egzamin: 5 wariantów i 5 kluczy, materiały treningowe, nie oficjalne arkusze; `publication_authorized: false`.
- Wskaźnik „poprawna = jedyna najdłuższa” w stanie bazowym: 83/609 = 13,63% (próg CI 18%).
- Testy lokalne nie zostały uruchomione, ponieważ nie ma lokalnego checkoutu repo w tym środowisku. Przed scaleniem wymagany jest pełny PASS Quality Gate CI, w tym nowe testy integracyjne.
- Test strukturalny nie jest recenzją prawną. Nie ustawiono żadnego statusu `verified`; pełna kontrola specjalisty pozostaje wymagana.
- Nie rozpoczęto kursu cystern ani żadnej innej specjalizacji.
