# Etap 4x5 — raport końcowy: scenariusze praktyczne i egzaminy próbne

Data: 25.10.2026. Zakres: wyłącznie kurs podstawowy ADR.

## 1. Scenariusze praktyczne

- Rozbudowano `podstawowy/praktyka/scenariusze-13-dzialow.json` z 13 do 39 scenariuszy.
- Każdy z 13 działów ma dokładnie 3 scenariusze; bramka CI wymaga minimum 3 na dział.
- Scenariusze zawierają sytuację, kroki kierowcy, typowe błędy z wyjaśnieniem, podstawę ADR, ID pytań, kryteria oceny i granice bezpieczeństwa.
- Dokumentacja `SCENARIUSZE.md` została uzupełniona w trzech partiach.
- Raporty partii: [B-01–04](etap-4x5-scenariusze-01-04-2026-10-25.md), [B-05–08](etap-4x5-scenariusze-05-08-2026-10-25.md), [B-09–13](etap-4x5-scenariusze-09-13-2026-10-25.md).
- Kontrola ID: wszystkie odwołania w scenariuszach prowadzą do istniejących pytań z właściwego modułu. Wszystkie scenariusze pozostają symulacjami; nie stanowią dowodu wykonania praktyki.

## 2. Audyt wariantów 001–003 i kluczy

Wszystkie trzy istniejące warianty porównano z aktualnym `podstawowy/questions.jsonl`. Dla każdego pytania sprawdzono: ID, moduł, treść, opcje, poprawną odpowiedź i explanation. Klucz porównano po ID i kolejności z arkuszem. Nie wykryto rozjazdu w stanie `main` użytym do tej kontroli. Warianty 001–003 nie mają powtórzeń wewnętrznych ani nakładania się ID między wariantami.

## 3. Warianty 004–005

- Wariant 004: seed `2026102504`; rozkład klucza A/B/C: {"A":9,"B":10,"C":11}.
- Wariant 005: seed `2026102506`; rozkład klucza A/B/C: {"A":10,"B":10,"C":10}.
- Każdy wariant zawiera 30 pytań, obejmuje wszystkie 13 działów, ma proporcjonalne kwoty działowe, brak duplikatów i nie powtarza pytań z wariantów 001–004.
- Oba warianty i klucze zostały sprawdzone względem bieżącego banku. Wszystkie klucze zgadzają się z odpowiedzią i explanation źródłową.
- `publication_authorized: false`; materiały pozostają egzaminem treningowym, nie oficjalnym arkuszem.

## 4. Testy i Quality Gate

- Zaktualizowano test regresyjny tak, aby sprawdzał wszystkie pięć wariantów i kluczy względem banku: ID, kolejność, moduł, treść, opcje, odpowiedź, explanation i podstawę prawną.
- Test wymaga braku powtórzeń ID między wariantami i rozkładu A/B/C w nowych wariantach 004–005 z różnicą najwyżej 3.
- Bank: 609 pytań; statusy `needs_review`: 609; `verified`: 0; minimalna długość explanation: 300.
- Scenariusze na dział: {"ADR-B-01":3,"ADR-B-02":3,"ADR-B-03":3,"ADR-B-04":3,"ADR-B-05":3,"ADR-B-06":3,"ADR-B-07":3,"ADR-B-08":3,"ADR-B-09":3,"ADR-B-10":3,"ADR-B-11":3,"ADR-B-12":3,"ADR-B-13":3}.
- Wyniki preflight API: wszystkie pięć wariantów zsynchronizowane, brak duplikatów i nakładania się ID; wszystkie 13 działów objęte scenariuszami. PASS CI wymagany przed scaleniem tej partii.

## 5. Ograniczenia

Nie zmieniano odpowiedzi w banku ani statusów weryfikacji. Nie oznaczono niczego jako `verified`. Redakcja scenariuszy i techniczna synchronizacja egzaminów nie są niezależną recenzją prawną ADR.
