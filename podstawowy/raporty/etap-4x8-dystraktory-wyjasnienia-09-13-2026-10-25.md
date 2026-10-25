# Etap 4x8 — jakość dystraktorów i wyjaśnień, B-09–13

## Zakres
- Punkt wyjścia: świeży `main` `35398b072119cc2bbdc6daeeca67928d9b38a0bb`.
- Sprawdzono wszystkie 235 pytań w działach B-09–B-13: B-09 46, B-10 55, B-11 43, B-12 44, B-13 47.
- Kontrola skryptowa nie znalazła explanation poniżej 200 znaków ani zdań dłuższych niż 35 słów w tej partii. Ręczny przegląd kandydatów wykrył kilka dystraktorów, które były zbyt łatwe do odrzucenia ze względu na kolor opakowania/pojazdu, logo lub zastąpienie dokumentu telefonem.

## Potwierdzone poprawki
- **ADR-B-0291** — zastąpiono dystraktor o podobnym kolorze opakowań błędem polegającym na uznaniu wspólnego odbiorcy i dokumentu za podstawę dopuszczalności wspólnego załadunku. Wyjaśnienie wskazuje, że decyduje ADR 7.5.2.1.
- **ADR-B-0324** — zastąpiono „kolor kartonów” błędnym założeniem, że zgodność opakowania UN zastępuje kontrolę tabeli wspólnego załadunku. Podstawa: ADR 7.5.2.1.
- **ADR-B-0388** — zastąpiono „kolorowe logo armatora” niepełnym sprawdzeniem wyłącznie numeru UN. Explanation wyjaśnia, że dokument musi zawierać dodatkowe dane wymagane na drodze. Podstawa: ADR 1.1.4.2.3.
- **ADR-B-0413** — zastąpiono „kolor i oznakowanie pojazdu” błędem polegającym na uznaniu numeru rejestracyjnego za wystarczający dowód upoważnienia kierowcy. Podstawa: ADR 1.10.1.2.
- **ADR-B-0586** — zastąpiono zastąpienie instrukcji telefonem dyspozytora wiarygodnym błędem: użyciem skróconej instrukcji firmowej. Podstawa: ADR 5.4.3.

Zachowano wszystkie ID i poprawne litery. Wyjaśnienia tych pięciu pytań przeredagowano na 2–5 zdań dla kursanta; długości wynoszą ADR-B-0291: 325, ADR-B-0324: 338, ADR-B-0388: 382, ADR-B-0413: 369, ADR-B-0586: 381 znaków.

## Audyt i klucze
Zaktualizowano migawki w plikach `review/sequential/` i `review/legal-clauses/` dla pięciu zmienionych pytań. Nie zmieniono poprawnych liter ani ID, dlatego klucze egzaminów 001–005 pozostają bez zmian.

## Uzupełnienia lekcji
Dodano sekcję „Najczęstsze błędy kursantów” do B-09–B-13:
- B-09: wspólny załadunek, wymagania opakowań, mocowanie i pozostałości.
- B-10: dokumenty transportu kombinowanego i wymagane dodatkowe wpisy.
- B-11: kody tunelowe, kategorie tuneli i planowanie trasy.
- B-12: weryfikacja przewoźnika, ochrona przewozu i kontrola dostępu.
- B-13: wzór instrukcji pisemnych, dokumenty dostępne w pojeździe i wymagane wpisy.
Każda sekcja wskazuje podstawę ADR i link do słowniczka.

## Lista sprawdzonych pytań
Wszystkie ID, których `module_id` to ADR-B-09, ADR-B-10, ADR-B-11, ADR-B-12 lub ADR-B-13 (235 rekordów).

## Preflight Quality Gate
- Bank: 609 pytań; duplikaty ID: 0.
- „Poprawna odpowiedź jest jedyną najdłuższą”: 81/609 = 13.30% (limit globalny 18%).
- Najkrótsze explanation: 300 znaków; poniżej 200: 0.
- Statusy: 609 `needs_review`, 0 `verified`.
- Wskaźnik modułowy:
  - B-10: 4/55 = 7.27% (limit 18%).
  - B-11: 7/43 = 16.28% (limit 18%).
  - B-12: 7/44 = 15.91% (limit 18%).
  - B-13: 4/47 = 8.51% (limit 18%).
  - B-09: 4/46 = 8.70% (limit 18%).
- Nie oznaczono żadnego pytania jako `verified`.

## Ograniczenia
Poprawki są redakcyjne i dydaktyczne; nie są zatwierdzeniem prawnym. Status wszystkich pytań pozostaje `needs_review` do niezależnej recenzji specjalisty ADR.