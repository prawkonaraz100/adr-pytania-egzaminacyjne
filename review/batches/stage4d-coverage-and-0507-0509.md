# Etap 4d — inwentaryzacja scenariuszy i pierwsza partia 0507–0509

Data: 23.10.2026. Świeży main na wejściu: **506 pytań, ADR-B-0001–0506, 506 needs_review, zero verified**, bez otwartych PR-ów. 

## Metoda liczenia

Sygnał scenariusza = jednoczesna obecność w **treści pytania**: (1) uczestnika/pojazdu albo miejsca transportu, (2) sformułowania decyzji lub obowiązku oraz (3) konkretnego kontekstu czasowego/warunku/zdarzenia. To **automatyczny przesiew o niskiej czułości**, nie ocena wyczerpującej jakości: stwierdzenie „0” oznacza brak trafienia w heurystyce, NIE dowodzi braku wszystkich scenariuszy semantycznych.

## Wyniki w 13 działach przed dopisaniem

| Dział | Wszystkie pytania | Ścisłe scenariusze | Udział | Priorytet |
|---|---:|---:|---:|---|
| ADR-B-01 | 25 | 1 | 4.0% | wysoki |
| ADR-B-02 | 53 | 1 | 1.9% | wysoki |
| ADR-B-03 | 48 | 2 | 4.2% | średni |
| ADR-B-04 | 43 | 4 | 9.3% | kontrola różnorodności |
| ADR-B-05 | 39 | 5 | 12.8% | kontrola różnorodności |
| ADR-B-06 | 31 | 0 | 0.0% | wysoki |
| ADR-B-07 | 42 | 8 | 19.0% | kontrola różnorodności |
| ADR-B-08 | 35 | 1 | 2.9% | wysoki |
| ADR-B-09 | 38 | 6 | 15.8% | kontrola różnorodności |
| ADR-B-10 | 54 | 1 | 1.9% | wysoki |
| ADR-B-11 | 32 | 1 | 3.1% | wysoki |
| ADR-B-12 | 42 | 2 | 4.8% | średni |
| ADR-B-13 | 24 | 0 | 0.0% | wysoki |

**Suma ścisłych trafień:** 32 / 506. W szczególności działy 06 i 13 mają **0 trafień**, a 02, 08, 10, 11 i 01 tylko po 1 — są priorytetem rozbudowy. To licznik heurystyczny, nie ostateczna klasyfikacja pytania.

## Partia wykonana: nowe pytania i kompetencje

| ID | Dział | Decyzja w realnej sytuacji | Przepis ADR 2025 | Przypisanie |
|---|---|---|---|---|
| ADR-B-0507 | 06 | Kierowca przed odjazdem widzi numery tablicy zamienione miejscami | 5.3.2.2.2 | ADR-B-06-K03 |
| ADR-B-0508 | 13 | Kierowca zgłasza brak „UN” przed numerem towaru w dokumencie | 5.4.1.1.1(a) | ADR-B-13-K01 |
| ADR-B-0509 | 08 | Kierowca zestawu ciężarówka + przyczepa sprawdza liczbę klinów | 8.1.5.2 | ADR-B-08-K04 |

Każde pytanie ma odrębny audyt **A/B/C** z uzasadnieniem poprawności/błędu wszystkich opcji (9 ocen), konkretne źródło prawne, status `needs_review` i brak danych recenzenta. Dystraktory opisują realne, ale błędne interpretacje, a nie ewidentne żarty czy oczywiste skrajności. Żadne stare pytanie nie zostało zmienione.

## Kontrola podstaw prawnych i ograniczenia

- Wersja ADR 2025 na stronie UNECE: https://unece.org/adr-2025-files (punktowa kontrola EN). Materiał w Dz.U. 2025 poz. 642: https://eli.gov.pl/eli/DU/2025/642/ogl; sprostowanie: https://eli.gov.pl/eli/DU/2025/1575/ogl.
- **Dosłowne porównanie pełnej polskiej publikacji na poziomie 3 nowych pytań i ocena wpływu sprostowania nie zostały wykonane.** Z tego powodu w raportach `official_polish_full_text_comparison=pending`, `needs_review`, nie `verified`. CI jest kontrolą techniczną, a nie dowodem materialnej zgodności prawnej.
- Pytania są przeznaczone dla kursu **podstawowego**, bez obsługi cystern i bez nowych kursów. Następne partie powinny objąć szczególnie ADR-B-02, ADR-B-10, ADR-B-11, ADR-B-01 i ADR-B-12, a docelowo wszystkie 13 działów.
- Równolegle z nowymi pytaniami trzeba aktualizować indeks `review/specialist/REJESTR-0001-0506.md` i tester spójności, który dotychczas oczekuje dokładnie 506 rekordów. Nie wolno fałszować migawki historycznej: rejestr 0001–0506 zachować, a następne pytania indeksować w osobnym dodatku.
