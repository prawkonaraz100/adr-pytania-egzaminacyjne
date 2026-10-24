# Etap 4n — partia 1: wyjaśnienia dla kursanta, ADR-B-0001–0006

Data: 24.10.2026. Fresh main po PR #168: 545 pytań (0001–0545), 0 otwartych PR, 545 needs_review, 0 verified. Długość poprawnej opcji: 340/545 (62,4%) globalnie; B-10: 37/55 (67,3%). Identyfikatory nowych pytań od ADR-B-0546, ale w tej partii nie dodawano pytań.

## Zmiana

Zredagowano pole `explanation` wyłącznie w sześciu pytaniach: 0001, 0002, 0003 (ADR-B-01) i 0004, 0005, 0006 (ADR-B-02). Każda nowa treść ma 300–352 znaki, od 3 do 4 zdań, wyjaśnia praktyczny powód poprawnej odpowiedzi, dlaczego błędne opcje są mylące i podaje podstawę ADR na końcu.

Przed zmianą część wyjaśnień ograniczała się do jednego zdania lub do odesłania. Zmieniono tylko `explanation`, bez naruszania `options`, `correct_option`, `stem`, `sources`, `image` i `verification_status`. W `review/sequential/001-030.json` oraz `review/legal-clauses/001-030.json` zsynchronizowano wyłącznie dokładne kopie tych sześciu wyjaśnień. Pozostałe rekordy audytu bez zmian.

## Kryteria i granice

Język kursanta, mechanizm poprawnej odpowiedzi, wyjaśnienie dwóch mylących wyborów i podstawa prawna. Status każdego pytania nadal `needs_review`; brak `verified`. Bez niezależnej recenzji nie zatwierdzać publikacji. Pełne dosłowne porównanie polskiego Dz.U. 2025 poz. 642 i sprostowania poz. 1575 pozostaje do wykonania. Metryka długości A/B/C bez zmian, więc CI `--strict` jeszcze nieaktywne.

Kolejne kroki: dalsza redakcja wyjaśnień moduł po module, równoległe małe partie normalizacji długości B-10, potem B-12/B-05/B-04. W tej partii nie zmieniono żadnych innych kursów.
