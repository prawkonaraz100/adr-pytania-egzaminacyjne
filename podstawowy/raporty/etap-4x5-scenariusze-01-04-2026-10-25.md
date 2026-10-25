# Etap 4x5 — scenariusze praktyczne ADR-B-01–04

- Zakres: wyłącznie kurs podstawowy.
- Punkt wyjścia: świeży `main` `70da095d050e54c1819e7c5532c02cc6ac94284a`.
- Źródła robocze: `podstawowy/praktyka/scenariusze-13-dzialow.json`, `SCENARIUSZE.md`, `podstawowy/questions.jsonl`.

## Zmiany

Dodano osiem scenariuszy, po dwa do każdego z działów B-01–B-04. Każdy zawiera sytuację, kroki kierowcy, co najmniej dwa typowe błędy z wyjaśnieniem, podstawę ADR, ID pytań, kryteria oceny i granice bezpieczeństwa.

| ID | Dział | Temat | Powiązane pytania |
|---|---|---|---|
| `SC-ADR-B-01-02` | B-01 | Ocena zwolnienia przed wyjazdem | `ADR-B-0001`, `ADR-B-0002`, `ADR-B-0003`, `ADR-B-0259`, `ADR-B-0570` |
| `SC-ADR-B-01-03` | B-01 | Niepełne dokumenty i polecenie dyspozytora | `ADR-B-0001`, `ADR-B-0002`, `ADR-B-0003` |
| `SC-ADR-B-02-02` | B-02 | Nieznana substancja na mokrym opakowaniu | `ADR-B-0004`, `ADR-B-0005`, `ADR-B-0006`, `ADR-B-0510` |
| `SC-ADR-B-02-03` | B-02 | Rozbieżność klasyfikacji i oznakowania | `ADR-B-0004`, `ADR-B-0005`, `ADR-B-0006` |
| `SC-ADR-B-03-02` | B-03 | Nieznany wyciek na parkingu | `ADR-B-0007`, `ADR-B-0008`, `ADR-B-0009`, `ADR-B-0514` |
| `SC-ADR-B-03-03` | B-03 | Pozostałości po rozładunku | `ADR-B-0007`, `ADR-B-0008`, `ADR-B-0009` |
| `SC-ADR-B-04-02` | B-04 | E-papieros i pracujący silnik przy załadunku | `ADR-B-0010`, `ADR-B-0011`, `ADR-B-0012`, `ADR-B-0580`, `ADR-B-0581` |
| `SC-ADR-B-04-03` | B-04 | Postój, który może nie spełniać wymagań | `ADR-B-0010`, `ADR-B-0011`, `ADR-B-0012`, `ADR-B-0310`, `ADR-B-0347` |

## Kontrola referencji i bezpieczeństwa

- JSON parsuje się poprawnie, a wszystkie nowe identyfikatory scenariuszy są unikalne.
- 8/8 scenariuszy ma co najmniej 3 kroki, 2 typowe błędy, podstawę ADR, kryteria oceny i granice bezpieczeństwa.
- Wszystkie 35 wskazań pytaniowych (z uwzględnieniem powtórzeń między scenariuszami) prowadzą do istniejących pytań przypisanych do właściwego działu.
- Liczba scenariuszy wzrosła z 13 do 21; B-01–B-04 mają po trzy scenariusze.
- Zaktualizowano `SCENARIUSZE.md`.

## Zasady

Wszystkie scenariusze są symulacjami na fikcyjnych dokumentach, mapach lub makietach. Nie należy używać rzeczywistych towarów niebezpiecznych, tworzyć wycieków ani traktować quizu jako dowodu odbycia zajęć. Nie zmieniano banku pytań, kluczy ani statusów weryfikacji; nie dodano statusu `verified`.

## Testy

Wykonano przed PR kontrolę struktury JSON i kontrolę referencji w treści zmian. Formalny Quality Gate CI jest wymagany przed scaleniem.
