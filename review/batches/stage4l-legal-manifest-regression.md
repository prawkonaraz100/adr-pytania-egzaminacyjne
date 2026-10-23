# Uzupełniająca partia 4l — wykrywanie przestarzałych odniesień ADR i manifestu recenzyjnego

23.10.2026. Stan świeżego `main` na początku: **542 pytania ADR-B-0001–0542**, 542 `needs_review`, 0 `verified`, brak otwartych PR-ów. Ta partia nie zmienia treści pytań ani ustawień egzaminu próbnego. Dotyczy tylko spójności przekazania niezależnemu specjaliście.

## Potwierdzona luka

Wcześniejszy `scripts/course_consistency.py` sprawdzał numerację pytań i klucze w indeksie recenzenta, ale **nie porównywał** referencji prawnych w rejestrze `review/legal-polish/stage4k-literal-verification-ledger-0001-0542.json` z rzeczywistym `questions.jsonl` ani liczby nierozstrzygniętych porównań i listy SVG w `review/specialist/PAKIET-0542-MANIFEST.json`. Zmiana konkretnego punktu ADR w pytaniu mogłaby pozostawić stary punkt w pakiecie, mimo pozytywnego audytu technicznego.

## Zastosowana kontrola

Dodano `validate_reviewer_manifest()` do `scripts/course_consistency.py`, która sprawdza: (1) liczbę pytań i ostatnie ID; (2) dokładnie 542 unikatowe ID rejestru wobec banku; (3) identyczność modułu, referencji źródłowych i statusu dla każdego ID; (4) statusy i liczbę nierozstrzygniętych odczytów oficjalnego PDF; (5) identyczność mapy ID→plik SVG bez braków i duplikatów. Syntetyczne testy regresji odrzucają przestarzały punkt ADR oraz błędnie zadeklarowaną liczbę otwartych przypadków. Nie rozszerzono zakresu o cysterny ani inne kursy.

## Ocena stanu

Zmiany mają wyłącznie charakter mechanizmu *fail-closed* i nie wykonują przeglądu prawa. Rzeczywisty specjalista nadal musi porównać dosłownie polski Dz.U. 2025 poz. 642 i sprostowanie poz. 1575 dla wszystkich 542 pytań, sprawdzić każdy wariant A/B/C i podpisać autentyczny raport. Wszystkie wpisy pozostają `needs_review`, bez `verified`, bez nowych rekordów i bez akceptacji. Przed scaleniem wymagany jest pełny PASS Quality Gate i dopisanie wyniku do Issue #10.
