# Etap 4x20 — wyrównanie długości odpowiedzi B-01/B-04 i poprawa explanation

- Punkt wyjścia: `main` `a1adec658d068ab00fbd4fa6410f69666c37a819`.
- Zakres: wyłącznie kurs podstawowy; żadna poprawna litera ani ID pytania nie zostały zmienione.

## 1. Wyrównanie długości odpowiedzi

| Dział | Przed | Po | Wynik |
|---|---:|---:|---|
| ADR-B-01 | 7/45 = 15,56% | 6/45 = 13.33% | PASS ≤14% |
| ADR-B-04 | 7/46 = 15,22% | 6/46 = 13.04% | PASS ≤14% |

- ADR-B-0149: dystraktor B przeredagowano z „według ładowności pojazdu” na realistyczny błąd polegający na liczeniu całej ilości w pojeździe zamiast limitu dla opakowania wewnętrznego. Poprawna litera C i podstawa ADR 3.2 tabela A / dział 3.4 bez zmian.
- ADR-B-0102: poprawną odpowiedź A skrócono do jasnego polecenia unikania źródeł zapłonu, bez palenia i włączania urządzeń elektrycznych. Sens odpowiedzi oraz litera A pozostają bez zmian; B/C pozostają niepoprawne i dłuższe.

## 2. Explanation przepisane

- **ADR-B-0196** — proste wyjaśnienie, że zakaz z 8.3.1 obejmuje pasażera spoza załogi, a telefoniczna zgoda nadawcy ani brak pracy przy ładunku nie tworzą wyjątku.
- **ADR-B-0398** — wyjaśniono, że dokument IMDG/ICAO można wykorzystać tylko w określonych warunkach; telefon i kolor kontenera nie zastępują dokumentacji drogowej.
- **ADR-B-0440** — wyjaśniono, że dodatkowe wymagania dla odcinka niedrogowego mogą wynikać z uzgodnienia stron na warunkach przepisu; ustne życzenie kierowcy nie wystarcza.

Każde explanation ma 2–4 zdania i kończy się krótką podstawą ADR. Wszystkie trzy pytania nadal mają status `needs_review`; nie zatwierdzano ich prawnie.

## 3. Metryki banku po zmianie

| Dział | Ściśle najdłuższa poprawna | Odsetek |
|---|---:|---:|
| B-01 | 6/45 | 13.33% |
| B-02 | 8/56 | 14.29% |
| B-03 | 7/49 | 14.29% |
| B-04 | 6/46 | 13.04% |
| B-05 | 6/43 | 13.95% |
| B-06 | 5/45 | 11.11% |
| B-07 | 6/48 | 12.5% |
| B-08 | 5/42 | 11.9% |
| B-09 | 4/46 | 8.7% |
| B-10 | 4/55 | 7.27% |
| B-11 | 6/43 | 13.95% |
| B-12 | 6/44 | 13.64% |
| B-13 | 4/47 | 8.51% |

- Liczba rekordów: 609; unikalne ID: 609.
- Explanation minimum: 300 znaków; poniżej 200 znaków: 0. Explanation ADR-B-0196, ADR-B-0398 i ADR-B-0440 mają odpowiednio 373, 355 i 409 znaków.
- Wszystkie pytania pozostają `needs_review`; `verified`: 0.
- Dodano regresyjny warunek w `tests/test_stage4u_module_metrics.py`: B-01 i B-04 muszą pozostać ≤14%; dotychczasowy limit pozostałych modułów 18% zachowano.

## Ograniczenia

Zaktualizowano też warianty egzaminów próbnych 001–005 i klucze: wszystkie 10 plików wskazuje nowy blob banku, a explanation w kluczach zsynchronizowano z bankiem. Dla pytań 0149 i 0102, jeśli występują w arkuszach, zaktualizowano odpowiednią opcję z zachowaniem jej litery w arkuszu.

Zmiany dotyczyły wyłącznie długości dystraktorów i czytelności wyjaśnień, bez zmiany poprawnej litery. Testy wykonane przez Quality Gate CI w PR; w tym środowisku nie uruchomiono lokalnego checkoutu repozytorium. Wszelkie rozstrzygnięcia prawne pozostają do specjalistycznej recenzji.
