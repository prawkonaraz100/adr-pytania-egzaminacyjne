# Etap 4d — partia 3, siedem scenariuszy 0513–0519

Stan przed pracą: main miał 512 pytań, ID ADR-B-0512 ostatnie, zero otwartych PR. Po dwóch poprzednich partiach scenariusze dodano w 6 działach; teraz uzupełniono pozostałe 7. W ten sposób **każdy z 13 modułów** ma przynajmniej **jeden nowy opis konkretnej decyzji uczestnika przewozu**. To cel etapu 4d, nie dowód pełnego merytorycznego wyczerpania scenariuszy.

| ID | Moduł | Sytuacja | Przepis |
|---|---|---|---|
| 0513 | 01 | Nowy pracownik terminalu bez szkolenia działa pod nadzorem | 1.3.1 |
| 0514 | 03 | Wyciek w kontenerze: czyszczenie przed kolejnym załadunkiem | 7.5.8.1 |
| 0515 | 04 | Silnik podczas rozładunku służy wyłącznie ogrzaniu kabiny | 8.3.6 |
| 0516 | 05 | Załoga nie przeczytała instrukcji przed wyjazdem | 5.4.3.3 |
| 0517 | 07 | Załadowca dostaje uszkodzone, nieszczelne opakowanie | 1.4.3.1.1(b) |
| 0518 | 09 | Nadmiernie naprężony pas deformuje opakowanie | 7.5.7.1 |
| 0519 | 12 | Drugi członek załogi nie ma identyfikatora ze zdjęciem | 1.10.1.4 |

Wszystkie 7 pytań to trzy realnie konkurujące decyzje A/B/C, bez zmiany starej bazy; 21 odrębnych ocen prawnych wariantów, migawki `review/sequential/513-519.json` oraz `review/legal-clauses/513-519.json`, kompletna mapa kompetencji, osobny aneks rejestru specjalisty. Klucze: B/A/C/A/B/C/A. Każdy rekord `needs_review`, niczego nie oznaczono `verified`.

Źródło normatywne: ADR 2025 ogłoszony w Dz.U. 2025 poz. 642 wraz ze sprostowaniem 1575, dostępne w ELI. Ustępy sprawdzono punktowo względem wydania ADR 2025 EN na UNECE; **pełne dosłowne porównanie polskiego urzędowego tekstu i ocena wpływu sprostowania są nadal pending**, wymagają specjalisty; CI nie przesądza o poprawności prawnej. Nie dodano kursu cystern ani innych kursów. Raport podsumowuje jedynie pierwsze uzupełnienie sytuacyjne wszystkich działów; dalsza praca 4e–4g jest osobna.
