# Etap 4x20 — audyt czytelności explanation ADR-B-0151–0200

- Punkt wyjścia: świeży `main` `1a8e4c0f095fb6d9814cfffed39d7f92af964296`.
- Zakres: 50 pytań ADR-B-0151–0200.
- Metoda: skryptowa lista kandydatów i ręczny odczyt explanation z perspektywy początkującego kierowcy.

## Wynik

- Ręcznie przejrzano 50/50 explanation: ADR-B-0151–ADR-B-0200.
- Przepisano 4 explanation: ADR-B-0165, 0189, 0197 i 0198.
- Pozostałe 46 pozostawiono bez zmian. Dwa trafienia heurystyczne uznano za fałszywe alarmy:
  - **ADR-B-0163** — wyjaśnia, że osłonięcie odpływu jest dopuszczalne tylko wtedy, gdy jest bezpieczne, i stawia bezpieczeństwo ludzi na pierwszym miejscu.
  - **ADR-B-0186** — prosto wyjaśnia ryzyko dla obserwatorów i dlaczego należy ich ostrzec zamiast angażować do przenoszenia przesyłek.
- Pozostałe 44 wyjaśnienia nie wzbudziły istotnych zastrzeżeń językowych.

## Przykłady przed/po

1. **ADR-B-0165 — numer UN**
   - Przed: „...na przykład numeru UN z dokumentu.”
   - Po: dodano definicję, że numer UN to czterocyfrowy identyfikator towaru niebezpiecznego, oraz wyjaśniono, dlaczego przypadkowy numer może wprowadzić ratowników w błąd.
   - Podstawa: ADR 5.4.3.4.

2. **ADR-B-0197 — wyłączenie ilościowe**
   - Przed: „Przy przewozie korzystającym z wyłączenia ilościowego 1.1.3.6...”
   - Po: dopowiedziano, że ADR 1.1.3.6 pozwala w określonych warunkach stosować część uproszczeń, ale nie znosi minimalnego wymogu dotyczącego gaśnicy.
   - Podstawa: ADR 8.1.4.2.

3. **ADR-B-0198 — kategoria FL**
   - Przed: „...świadectwo dopuszczenia dla pojazdu FL...”
   - Po: wyjaśniono, że FL to kategoria pojazdu używanego przy określonych przewozach cieczy lub gazów palnych w cysternach, a następnie wskazano, gdzie musi znajdować się wymagane świadectwo.
   - Podstawa: ADR 8.1.2.2(a) i 9.1.3.

## Wszystkie poprawione rekordy

- ADR-B-0165 — numer UN i informacje dla służb ratunkowych.
- ADR-B-0189 — numer UN, nalepka główna i dodatkowa.
- ADR-B-0197 — wyłączenie ilościowe 1.1.3.6 i minimalna skuteczność gaśnicy.
- ADR-B-0198 — kategoria FL i świadectwo dopuszczenia pojazdu.

## Integralność i metryki

- Bank: 609 rekordów, 609 unikalnych ID, 0 duplikatów.
- Explanation minimum: 300 znaków; 0 poniżej 300.
- Wszystkie pytania pozostają `needs_review`; `verified`: 0.
- Zmieniono tylko explanation, więc wskaźnik „poprawna = jedyna najdłuższa” pozostaje bez zmian:
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
- Zsynchronizowano warianty i klucze egzaminów 001–005 oraz snapshoty audytów `review/sequential/` i `review/legal-clauses/` dla czterech zmienionych rekordów.
- Nie zmieniono opcji, poprawnych liter ani statusów prawnych.

## Ograniczenia

Kontrola językowa nie zastępuje niezależnej recenzji prawnej. Wymagany jest PASS Quality Gate CI; lokalny checkout nie był dostępny w tym środowisku.
