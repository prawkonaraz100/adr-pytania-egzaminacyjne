# Przekazanie specjaliście ADR — pakiet aktualny na 519 pytań (etap 4g)

## Co obejmuje pakiet

- **Bank:** `podstawowy/questions.jsonl`, 519 pytań; każdy rekord ma własną odpowiedź A/B/C, wyjaśnienie, konkretne odwołania ADR i status `needs_review`.
- **Indeks aktualny:** `review/specialist/REJESTR-AKTUALNY-0001-0519.md` — 519 wierszy z ID, działem, kluczem i źródłem; poprzednie rejestry `REJESTR-0001-0506.md`, `REJESTR-0507-0509.md`, `REJESTR-0510-0512.md`, `REJESTR-0513-0519.md` pozostają jako **historyczne migawki**.
- **Instrukcja i formularz:** `review/specialist/INSTRUKCJA-RECENZJI.md` i `FORMULARZ-UWAG.md`, bez wstawionych fikcyjnych recenzentów.
- **Wstępne audyty:** `review/sequential/` i `review/legal-clauses/`, podsumowania w `review/batches/`, w tym `stage4a-quality-001-506.md` (sygnały jakości), `stage4d-coverage-and-0507-0509.md` oraz dwa raporty nowych scenariuszy, `stage4e-polish-clause-0507-0519.md` (ograniczone źródłowo porównanie z polskim tekstem pomocniczym).
- **Kurs podstawowy:** 13 plików `podstawowy/lekcje/ADR-B-01.md` ... `ADR-B-13.md`, 3 rzeczywiste cele P1–P3 w `podstawowy/praktyka/SCENARIUSZE.md`, karty `docs/POWTORKI-13-DZIALOW.md` i `docs/SLOWNIK-TERMINOLOGII-ADR.md`.
- **Bramka publikacji:** `scripts/release_gate.py`; `scripts/mock_exam.py` nie wytworzy arkusza z pytań needs_review.

## Kolejność recenzji

1. Specjalista uzgadnia z redaktorem **wersję/commit SHA** banku, zanim rozpocznie osobne sprawdzanie A/B/C. Aktualny spis może stać się nieaktualny po przyszłych PR-ach.
2. Weryfikacja literalna **z odpowiednimi oficjalnymi plikami Dz.U. 2025 poz. 642** i sprostowaniem 1575, a nie wyłącznie z pomocniczymi publikacjami.
3. Osobny werdykt dla stem, wariantu A, B, C, explanation, obowiązujących wyjątków, prawidłowej podstawy, w szczególności zakresu kursu podstawowego. Uwaga: przesiew 4a sygnalizuje wiele słabych dystraktorów.
4. Rejestrowanie *realnych* ustaleń w formularzu, z podpisem/wiarygodnym potwierdzeniem recenzenta. Nierozstrzygnięty temat = blokada; nie zmieniać w ciemno correct_option.
5. Potwierdzone poprawki w osobnych PR-ach **z odświeżeniem dwóch audytów i pełnym PASS CI**. Nie wolno nadpisywać historycznego dziennika Issue #10.
6. Dopiero po niezależnym, pozytywnym odbiorze i kontroli release gate można rozważyć wydanie wewnętrzne; publikacja publiczna i realne prowadzenie zajęć wymagają odrębnego odbioru.

## Zakres gotowości

| Obszar | Ocena | Dlaczego |
|---|---|---|
| Struktura 13 działów i 106 wewnętrznych celów | Gotowa do recenzji | 103/103 cele teorii mają pytania; 3 cele praktyki bez sztucznych quizów |
| Materiał pytań | W przygotowaniu / niezakończony odbiór | 519/519 needs_review, 0 verified |
| Dystraktory i jakość języka | Otwarte uwagi | Etap 4a oznaczył liczne kandydatury do indywidualnej oceny |
| Scenariusze w każdym dziale | Wersja robocza | 13 nowych pytań 0507–0519, audyty 39 wariantów A/B/C |
| Dosłowna zgodność z urzędowym Dz.U. 642 i sprostowaniem 1575 | **Nieukończona** | 4e wykorzystało także materiał pomocniczy MI; potrzeba urzędowego PDF i eksperta |
| Grafiki | Szkice i specyfikacje | Prawa własne, ale jeszcze kontrola symboli i legalnej zgodności |
| Egzamin próbny | Technicznie zablokowany | Brak zaakceptowanych pytań; fail-closed |
| Praktyka P1–P3 | Projekty scenariuszy | Trzeba rzeczywiście przeprowadzić, ocenić i bezpiecznie udokumentować |
| Gotowość do publikacji | **NIE** | Brak realnych potwierdzeń prawnych i odbioru |

**Zasada niezmienna:** żadnego `verified`, żadnego kursu cystern ani innego kursu specjalistycznego.
