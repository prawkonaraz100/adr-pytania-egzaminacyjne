# Etap 4l — aktualizacja pakietu specjalisty i egzaminu próbnego

Data: 23.10.2026. Świeży `main` przed pracą: **542 pytania, ADR-B-0001–0542, 542 `needs_review`, 0 `verified`, brak otwartych PR**. Działy ADR-B-01 i ADR-B-13 mają po 35 pozycji. Wszystkie 103 kompetencje teoretyczne mają powiązane pytania; trzy cele praktyczne są osobnymi ćwiczeniami. Nowe 23 pytania 0520–0542 zachowano bez ingerencji w treść lub klucze.

## Co zaktualizowano

1. Nowy bieżący indeks `review/specialist/REJESTR-AKTUALNY-0001-0542.md` dokumentuje każde ID, moduł, kompetencje, pytanie, roboczy klucz, referencję ADR, `image` i wynik kontroli literalnej. Stare zakresowe i indeks 0519 pozostawiono jako migawki historyczne.
2. `review/specialist/PAKIET-0542-MANIFEST.json` obejmuje rozkład 13 działów, odniesienia do autorskich SVG, rejestr blokad prawnych i wymogi przekazania specjaliście. Zaktualizowano `INSTRUKCJA-RECENZJI.md` oraz `PRZEKAZANIE-ETAP4.md`, zaznaczając priorytet P1 dla wszystkich 23 nowych pytań i kontrolę grafiki niezależną od kontroli pytania.
3. `scripts/mock_exam.py` udostępnia SVG wyłącznie dla *prawidłowo zatwierdzonych* wybranych pytań; blokuje nieistniejące albo niebezpieczne ścieżki, przekazuje hash źródłowego banku, nadal korzysta z istniejącej `release_gate.eligible()` i z danymi produkcyjnymi **nie może** utworzyć egzaminu.
4. Testy syntetyczne sprawdzają dostępność klucza, fingerprint i odmowę eksportu przy brakującym SVG. `scripts/course_consistency.py` sprawdza bieżący indeks względem prawdziwych ID, kluczy i ścieżek obrazów, a nie tylko historyczne pliki zakresowe.
5. `docs/EGZAMIN-PROBNY.md` ostrzega o niedostępności i braku publicznej zgody.

## Blokady prawne i gotowość

- Rejestr `review/legal-polish/stage4k-literal-verification-ledger-0001-0542.json` obejmuje **542/542** pozycje z nierozstrzygniętą literalną kontrolą urzędowego polskiego PDF Dz.U. 2025 poz. 642 i sprostowania poz. 1575. Dostępne pomocnicze teksty angielskie nie stanowią równoważnej weryfikacji.
- Nie ma prawdziwych podpisów recenzenta, wpisów w `approvals.jsonl` ani żadnego `verified`. Dane nie nadają się do publicznej publikacji ani urzędowego egzaminu. Grafiki SVG są szkicami edukacyjnymi, nie oznakowaniem transportowym.
- Sformułowanie „techniczny PASS CI” nie oznacza prawnej zgodności materiałów. Priorytet po scaleniu: osobny raport gotowości 4l i kontrola wykrytych strukturalnych luk bez podejmowania kursów specjalistycznych.
