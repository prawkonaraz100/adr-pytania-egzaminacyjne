# Przekazanie specjaliście ADR — historia etapów 4g–4l i aktualny aneks 4m

## Co obejmuje pakiet

- **Bank:** `podstawowy/questions.jsonl`, 542 pytania; każdy rekord ma własną odpowiedź A/B/C, wyjaśnienie, konkretne odwołania ADR i status `needs_review`.
- **Indeks aktualny:** `review/specialist/REJESTR-AKTUALNY-0001-0542.md` — 519 wierszy z ID, działem, kluczem i źródłem; poprzednie rejestry `REJESTR-0001-0506.md`, `REJESTR-0507-0509.md`, `REJESTR-0510-0512.md`, `REJESTR-0513-0519.md` pozostają jako **historyczne migawki**.
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
| Materiał pytań | W przygotowaniu / niezakończony odbiór | 542/542 needs_review, 0 verified |
| Dystraktory i jakość języka | Otwarte uwagi | Etap 4a oznaczył liczne kandydatury do indywidualnej oceny |
| Scenariusze w każdym dziale | Wersja robocza | 13 nowych pytań 0507–0519, audyty 39 wariantów A/B/C |
| Dosłowna zgodność z urzędowym Dz.U. 642 i sprostowaniem 1575 | **Nieukończona** | 4e wykorzystało także materiał pomocniczy MI; potrzeba urzędowego PDF i eksperta |
| Grafiki | Szkice i specyfikacje | Prawa własne, ale jeszcze kontrola symboli i legalnej zgodności |
| Egzamin próbny | Technicznie zablokowany | Brak zaakceptowanych pytań; fail-closed |
| Praktyka P1–P3 | Projekty scenariuszy | Trzeba rzeczywiście przeprowadzić, ocenić i bezpiecznie udokumentować |
| Gotowość do publikacji | **NIE** | Brak realnych potwierdzeń prawnych i odbioru |

**Zasada niezmienna:** żadnego `verified`, żadnego kursu cystern ani innego kursu specjalistycznego.


## Aneks 4l — stan po nowych pytaniach i grafikach

Nowe archiwalne rejestry zakresowe: `REJESTR-0520-0525.md`, `REJESTR-0526-0533.md`, `REJESTR-0534-0538.md`, `REJESTR-0539-0540.md`, `REJESTR-0541-0542.md`. Obecnie **542 pytania**, z czego **23 nowe (0520–0542)**, 0 verified. Nie używać poprzedniej liczby 519 jako aktualnego stanu.

Dosłowna polska kontrola **0/542 nowych porównań** w poprzednim audycie 4k: `review/batches/stage4k-official-polish-source-blockers.md`. Priorytet P1 to nowe pytania, ze szczególną kontrolą wyników EQ/LQ, wpisów w dokumentacji, ograniczeń tunelowych i wzorów nalepek 2.2/3. Każdy wariant A/B/C wymaga odrębnej fachowej oceny. Egzamin pozostaje zamknięty. Ostatecznym dokumentem stanu jest `review/batches/stage4l-readiness-0542.md`.


## Aktualny aneks etapu 4m — 545 pytań (23.10.2026)

**Ten aneks jest nadrzędny wobec historycznych liczb 519/542 w powyższym dokumencie.** Przed rzeczywistą recenzją sprawdzić aktualny `main`, commit SHA i zawartość pytań.

- **Bank:** `podstawowy/questions.jsonl`, 545 kolejnych identyfikatorów ADR-B-0001–0545; wszystkie `needs_review`, 0 `verified`, 0 formalnych zatwierdzeń.
- **Aktualny indeks specjalisty:** `review/specialist/REJESTR-AKTUALNY-0001-0545.md` — 545 pozycji, ID, pytanie, klucz, podstawa prawna i ścieżka obrazu. Archiwalne indeksy i migawki zachować.
- **Manifest przekazania:** `review/specialist/PAKIET-0545-MANIFEST.json`. **Rejestr dosłownej kontroli PL:** `review/legal-polish/stage4m-literal-verification-ledger-0001-0545.json` — 545 pozycji z nierozstrzygniętym porównaniem urzędowego polskiego tekstu; nie nadawać `verified`.
- **Dział ADR-B-06:** 35 pytań po dodaniu 0543–0545, ogólne znaczenia cyfr 2, 4, 7 (ADR 2025 5.3.2.3.1); audyty `review/sequential/543-545.json` oraz `review/legal-clauses/543-545.json`.
- **Bramka dydaktyczna:** 13 lekcji + ćwiczenia P1–P3; test próbny pozostaje niedostępny przy 0 realnych zatwierdzeń.
- **Ryzyko wskazówki długości:** poprawna odpowiedź jest jednoznacznie najdłuższa w **370/545 (67,9%)**; próg docelowy ≤40% **nieosiągnięty**. Quality Gate raportuje wskaźnik globalnie i dla każdego modułu (`scripts/answer_length_bias.py`, `--strict` dostępne dopiero po redukcji w całym banku).
- Raporty 4m: `review/batches/stage4m-length-bias-batch1.md`, `review/batches/stage4m-adr-b-06-543-545.md`, `review/batches/stage4m-length-bias-batch3.md`, bieżący `review/batches/stage4m-readiness-0545.md`.

**Priorytety:** niezależna kontrola A/B/C po każdej zmianie redakcyjnej; dosłowne porównanie polskiego ADR 2025 Dz.U. 642 i sprostowania poz. 1575; dalsze poprawki długości i realistyczności dystraktorów, zwłaszcza w działach powyżej 40%; żadnego przedwczesnego egzaminu publicznego. Nie rozpoczęto kursu cystern ani innych specjalizacji.
