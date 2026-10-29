# Etap 4x153 — uzupełnienie najmniej pokrytej kompetencji teoretycznej

Data: 29.10.2026. Bazowy main: `abefaa0295903c7bed779f191cfa5fd68f0d51a2`.

## Zidentyfikowana luka

Audyt mapy `podstawowy/kompetencje.json` (107 kompetencji, 638 pytań) wykazał, że wśród kompetencji teoretycznych najmniejszą liczbę pytań miały po 3:
- `ADR-B-01-K01` — ramy prawne i definicje ADR (ADR 1.1, 1.2);
- `ADR-B-07-K07` — rozróżnienie odpowiedzialności cywilnej za szkodę i za niewykonanie zobowiązania.

Wybrano `ADR-B-01-K01`, ponieważ można ją uzupełnić bez rozszerzania kursu poza ADR i bez ponownego konstruowania pytania o odpowiedzialność na gruncie prawa krajowego. Pozostałe kompetencje teoretyczne miały co najmniej 4 przypisane pytania. Trzy kompetencje praktyczne z działu 05 mają zero przypisanych pytań testowych, ale są przeznaczone do ćwiczeń i scenariuszy praktycznych, więc nie potraktowano ich jako automatycznej luki w banku.

## Nowe pytanie

Dodano `ADR-B-0639` do działu `ADR-B-01` i przypisano je do kompetencji `ADR-B-01-K01`.

- **Temat:** jak znaleźć wymagania dotyczące załogi, wyposażenia, eksploatacji i dokumentów w strukturze ADR.
- **Podstawa prawna:** ADR 2025, 1.1.1 oraz układ załączników A i B, części 8–9. Oficjalne polskie ogłoszenie: [Dz.U. 2025 poz. 642](https://dziennikustaw.gov.pl/DU/2025/642). Spis treści urzędowego tekstu rozdziela część 8 (załoga, wyposażenie, eksploatacja i dokumentacja) i część 9 (konstrukcja i zatwierdzanie pojazdów).
- **Klucz:** A. W audycie A/B/C wskazano, że B myli część 2 załącznika A (klasyfikacja), a C myli część 5 załącznika A (procedury nadawcze) z częścią 8 załącznika B.
- **Explanation:** 367 znaków, 4 zdania; tłumaczy praktyczny sens, różnicę między poprawnym wskazaniem i dystraktorami oraz podaje podstawę ADR.
- **Status:** `needs_review`; to wstępny audyt redakcyjny, nie formalne zatwierdzenie prawne.

## Synchronizacja zależnych danych

- Bank: 639 pytań, ostatnie ID `ADR-B-0639`; blob `4171182f79c15fcb023541a68828945e82abbd16`.
- Mapa kompetencji: dodano ID do `ADR-B-01-K01` i odświeżono metadane audytu.
- Egzaminy próbne i klucze 001–005: zaktualizowano `source_bank_head` we wszystkich 10 plikach do nowego blobu.
- Audyt sekwencyjny: snapshot nowego pytania dodany do `review/sequential/629-639.json`.
- Przegląd klauzul prawnych: dodano snapshot i uzasadnienia A/B/C do `review/legal-clauses/629-639.json`. Statusy `official_polish_full_text_comparison` i `independent_specialist_approval` pozostają `pending`.
- Pakiety specjalisty: zaktualizowano bieżący blob, liczbę pytań i ostatnie ID w manifestach 0628 i 0638; odświeżono źródłowy blob obu kolejek priorytetowych.
- Raport wykluczeń egzaminu próbnego i dokumentację recenzji zaktualizowano do bieżącego snapshotu.

## Ograniczenia i odbiór

Nie oznaczono żadnego pytania jako `verified`. Zmiana nie jest niezależną opinią doradcy ADR; pełne porównanie literalne z polskim tekstem urzędowym i specjalistyczna akceptacja pozostają otwarte. Etap można uznać za zakończony dopiero po PASS wszystkich testów CI, w tym testów integralności snapshotów oraz egzaminów próbnych.
