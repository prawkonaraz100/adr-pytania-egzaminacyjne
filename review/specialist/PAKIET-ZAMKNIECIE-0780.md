# Pakiet końcowy do recenzji specjalisty — ADR kurs podstawowy

**Bank zamknięty, gotowy do przeglądu specjalisty — 03.11.2026 (etap 4x355).**

## Stan i zasady

Bank: **780** pytań (ADR-B-0001–0780), wszystkie **`needs_review`**, 0 `verified`, 0 zatwierdzeń specjalisty, publikacja nieautoryzowana. **104 kompetencje teorii mają minimum 6 pytań**. Licznik kompetencji teorii z <6 pytań = **0**; 3 kompetencje praktyczne nie są objęte progiem. Nie dopisujemy pytań ponad REGUŁĘ KOŃCA.

Nie zmieniono treści pytań ani odpowiedzi w PR zamknięcia. Ostatni blob banku: `db5b90f4305fd75c1bb2f73a8b5c8b7a6bb42d63`; `main` po 4x354: `40d877c7909ca9274140281768ebe126b211ee70`. Rozkład A/B/C: 258/291/231; „poprawna jedyna najdłuższa”: 84/780 = 10,77%, maksimum działu 15,22%.

## Kolejność niezależnego przeglądu

1. Porównaj źródła `sources[].reference` każdego pytania z oficjalnym ADR 2025 (Dz.U. 2025 poz. 642, sprostowania i aktualne modyfikacje w zakresie obowiązywania). Rejestr źródeł w `review/legal-polish/` obejmuje pozycje podstawowe i suplementarne; brak literalnego porównania nie stanowi potwierdzenia.
2. Dla każdego pytania osobno oceń poprawny klucz A/B/C oraz każdy dystraktor. Sprawdź wyjątki, kontekst zawodowy kierowcy i jasność wyjaśnienia. Snapshoty w `review/sequential/` i `review/legal-clauses/` chronią przed rozbieżnością treści pytania i recenzji.
3. Sprawdź zgodność pytań zależnych od rysunków z zatwierdzonymi SVG. Zapisuj wynik recenzji i dowody w przeznaczonych do tego plikach; status `verified` może nadać dopiero upoważniony specjalista.
4. Dopiero po rzeczywistych zatwierdzeniach rozważ zastosowanie bramki publikacji; samo CI i gotowy pakiet nie uprawniają do eksportu jako zweryfikowanego banku.

## Zestaw plików wejściowych

- Bank: `podstawowy/questions.jsonl`; mapa kompetencji: `podstawowy/kompetencje.json`.
- Manifest: `review/specialist/PAKIET-0780-MANIFEST.json`; rejestr 780 unikalnych pozycji: `review/specialist/REJESTR-AKTUALNY-0001-0780.md`.
- Instrukcja: `review/specialist/INSTRUKCJA-RECENZJI.md`; przegląd etapów: `review/specialist/PRZEKAZANIE-ETAP4.md`.
- Ledger: `review/legal-polish/stage4w4-literal-verification-ledger-0001-0609.json` i `review/legal-polish/stage4w4-literal-verification-ledger-0610-0678.json`.
- Ostatnie snapshoty: `review/sequential/780-780.json`, `review/legal-clauses/780-780.json`.
- Egzaminy próbne: 5 × wariant i 5 × klucz w `podstawowy/egzamin-probny/`. Dziesięć artefaktów odnosi się do SHA `db5b90f4305fd75c1bb2f73a8b5c8b7a6bb42d63` i pozostaje nieautoryzowanych do publikacji.
- Raport końcowy: `docs/STAN-KONCOWY-BANKU-ADR-PODSTAWOWY-2026-11-03.md`.

**Otwarte dowody:** 753 rekordy bez dosłownie pobranego polskiego fragmentu prawnego; 27 z celowanym sprawdzeniem źródła i bez zakończonego pełnego porównania. Wszystkie 780 wymagają niezależnej recenzji. Nie wpisano pozornych zatwierdzeń.
