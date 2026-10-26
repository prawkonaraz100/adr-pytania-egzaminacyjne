# Etap 4x20 — audyt czytelności explanation ADR-B-0051–0100

- Punkt wyjścia: świeży `main` `a7bae14f6f98b95de0bdf49ea40dc351ff3b98e8`.
- Zakres: 50 pytań ADR-B-0051–0100.
- Metoda: skryptowe wyłapanie skrótów i odniesień przepisowych, potem ręczny odczyt explanation jako początkujący kursant. Flagi heurystyki były tylko wskazówką, nie automatycznym rozstrzygnięciem.

## Wynik przeglądu

- Ręcznie przejrzano 50/50 wyjaśnień: ADR-B-0051–ADR-B-0100.
- Przepisano 7 explanation: ADR-B-0061, 0062, 0069, 0073, 0082, 0089 i 0093.
- Pozostałe 43 zostawiono bez zmian; 5 z 12 kandydatów heurystycznych uznano po lekturze za fałszywe alarmy:
  - **ADR-B-0067** — wyjaśnienie jasno odróżnia dokument ze zdjęciem od karty zakładowej i listu przewozowego.
  - **ADR-B-0076** — wskazuje funkcję ochrony oczu i konkretnie porównuje ją z okularami przeciwsłonecznymi oraz kaskiem.
  - **ADR-B-0081** — podaje próg 0,8 m, cel oddzielenia i informuje, że istnieją inne dopuszczone metody.
  - **ADR-B-0084** — wyjaśnia skutek kodu D/E dla sztuk przesyłek i odróżnia go od pozostałych ograniczeń.
  - **ADR-B-0086** — wprost wskazuje regułę najsurowszego kodu oraz wyklucza wybór według kolejności lub masy.
- Pozostałe 38 wyjaśnień w tej partii nie wzbudziło istotnych zastrzeżeń językowych podczas ręcznej lektury.

## Przykłady przed/po

1. **ADR-B-0061 — punkt 1.1.3.6**
   - Przed: „...a nie do odrębnych punktów 1.1.3.6 czy 5.4.3.1.”
   - Po: wyjaśniono, że 1.1.3.6 to wyłączenie ilościowe dla określonych ilości na jednostkę transportową, a 5.4.3.1 dotyczy instrukcji pisemnych. Kursant widzi, dlaczego te punkty nie zastępują zapisu o przewozie kombinowanym.
   - Podstawa: ADR 5.4.1.1.7 i 1.1.4.2.1.

2. **ADR-B-0062 — IMDG**
   - Przed: „...znaki IMDG nie zawsze są identyczne ze znakami ADR.”
   - Po: dodano rozwinięcie IMDG jako kodeksu przewozu towarów niebezpiecznych drogą morską oraz praktyczną wskazówkę, by nie usuwać oznakowania bez sprawdzenia wymagań dla odcinka drogowego.
   - Podstawa: ADR 1.1.4.2.

3. **ADR-B-0082 — UN i CV28**
   - Przed: „...sprawdzić właściwy numer UN...” oraz odwołanie do CV28 bez wyjaśnienia.
   - Po: dopowiedziano, że numer UN to czterocyfrowy identyfikator towaru, a CV28 to szczególny warunek dotyczący oddzielenia od żywności, pasz i towarów konsumpcyjnych.
   - Podstawa: ADR 7.5.4 i 7.5.11, CV28.

## Wszystkie poprawione rekordy

- ADR-B-0061 — wyłączenie ilościowe 1.1.3.6 i instrukcje pisemne 5.4.3.1.
- ADR-B-0062 — skrót IMDG i oznakowanie w łańcuchu morsko-drogowym.
- ADR-B-0069 — wyjaśnienie numeru UN i jego różnicy względem liczby sztuk przesyłek.
- ADR-B-0073 — prosty sens wyłączenia ilościowego oraz minimalna gaśnica.
- ADR-B-0082 — numer UN, kod CV28 i oddzielenie od żywności.
- ADR-B-0089 — rozróżnienie 1.1.3.6, 5.4.3.2 i wpisu dla przewozu kombinowanego.
- ADR-B-0093 — różnica między ilościami ograniczonymi LQ a wyłączeniem ilościowym 1.1.3.6.

## Integralność i metryki

- Bank: 609 rekordów, 609 unikalnych ID, 0 duplikatów.
- Explanation minimum: 300 znaków; 0 poniżej 300.
- Wszystkie pytania nadal `needs_review`; `verified`: 0.
- Zmieniono wyłącznie explanation, więc wskaźnik „poprawna = jedyna najdłuższa” pozostaje bez zmian:
  - B-01: 6/45 = 13,33%
  - B-02: 8/56 = 14,29%
  - B-03: 7/49 = 14,29%
  - B-04: 6/46 = 13,04%
  - B-05: 6/43 = 13,95%
  - B-06: 5/45 = 11,11%
  - B-07: 6/48 = 12,50%
  - B-08: 5/42 = 11,90%
  - B-09: 4/46 = 8,70%
  - B-10: 4/55 = 7,27%
  - B-11: 6/43 = 13,95%
  - B-12: 6/44 = 13,64%
  - B-13: 4/47 = 8,51%
- Synchronizowano warianty 001–005, klucze 001–005 i migawki audytów `review/sequential/` oraz `review/legal-clauses/` dla wszystkich siedmiu zmienionych pytań.
- Wszystkie zmiany pozostają redakcyjne; nie oznaczono żadnego pytania jako `verified`.

## Ograniczenia

Kontrola wyjaśnień nie stanowi niezależnej recenzji prawnej. Wymagany jest PASS Quality Gate CI; lokalny checkout nie był dostępny w tym środowisku.
