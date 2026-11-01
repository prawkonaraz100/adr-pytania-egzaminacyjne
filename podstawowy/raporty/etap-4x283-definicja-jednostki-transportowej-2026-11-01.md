# Etap 4x283 — definicja jednostki transportowej w praktyce

Data: 01.11.2026  
Zakres: wyłącznie kurs podstawowy ADR  
Baza: main `bcc64b872bb21b4991a8e2ef64829c08dcabb8a0`  
Gałąź: `stage4x283-empty-packaging-inspection`  
Nowe ID: `ADR-B-0709`  
Kompetencja: `ADR-B-01-K01` — ramy prawne i definicje ADR

## Wybór luki

Kompetencja miała pięć pytań o ramy prawne i podstawowe pojęcia. Dodano praktyczne zastosowanie definicji „jednostki transportowej” do typowego zestawu samochód ciężarowy + przyczepa. Kursant ma rozpoznać, że w tym przypadku pojazd samochodowy i dołączona przyczepa tworzą jedną jednostkę, a nie dwa odrębne elementy liczone osobno.

## Dodane pytanie

- `ADR-B-0709`: kierowca zestawu z przyczepą ma wyjaśnić, co w ADR oznacza „jednostka transportowa”.
- Klucz: **B** — pojazd samochodowy wraz z dołączoną do niego przyczepą.
- Explanation: **305 znaków**, 4 zdania; najpierw praktyczne uzasadnienie, potem wyjaśnienie mylących odpowiedzi i krótka podstawa ADR.
- Długości A/B/C: **108/102/101** znaków; odpowiedzi są zbliżone długością, poprawna B nie jest najdłuższa.
- Audyt A/B/C: A — błędnie wyłącza przyczepę z jednostki; B — odpowiada definicji ADR 1.2.1; C — błędnie traktuje samą przyczepę jako jednostkę.
- Status: `needs_review`; nic nie oznaczono jako `verified`.

## Migawka banku i synchronizacja #646

- Blob SHA `podstawowy/questions.jsonl`: `ca182bd6c5e40d3ab1384d9eb91e3b1dd7035b0a`.
- Bank: 709 rekordów, wszystkie `needs_review`, 0 `verified`.
- Klucze i warianty egzaminów próbnych 001–005, snapshoty sequential/legal 709-709 i manifest `PAKIET-0709-MANIFEST.json` wskazują ten sam SHA.

## Podstawa prawna

- ADR 2025, 1.2.1 — „jednostka transportowa” oznacza pojazd samochodowy bez przyczepy lub zespół pojazdów składający się z pojazdu samochodowego i dołączonej do niego przyczepy.
- Dz.U. 2025 poz. 642, ADR 2025: https://eli.gov.pl/api/acts/DU/2025/642/text.pdf
- Ministerstwo Infrastruktury — oficjalne polskie teksty ADR 2025: https://www.gov.pl/web/infrastruktura/towary-niebezpieczne
- UNECE ADR 2025: https://unece.org/adr-2025-files

Definicja została sprawdzona w polskim tekście ADR; pełne literalne porównanie oraz niezależna recenzja specjalisty pozostają wymagane.

## Synchronizacja #646

- Bank: 709 pytań ADR-B-0001–0709; wszystkie `needs_review`, 0 `verified`.
- Blob SHA banku: `733efd0b63dc4b0048a03e53635faacd542ad6d2`.
- Warianty i klucze egzaminów próbnych 001–005 wskazują ten SHA.
- Snapshoty sequential/legal 709-709, rejestr źródeł, manifesty, indeksy i metryki odświeżane w tej gałęzi.
- Rozkład prawidłowych opcji A/B/C: 238/252/219.
- „Poprawna = jedyna najdłuższa”: 75/709 = 10,58%; maksimum modułu: 13,95%.
