# Etap 4x32 — raport końcowy: jakość dystraktorów i wyjaśnień

- Data: 26.10.2026.
- Świeży `main` po partiach: `dad8bc228dbf9526bf257ce4ca32d3d474ef7099`.
- Bank: 609 pytań, ID ADR-B-0001–ADR-B-0609.
- Zakres: wyłącznie kurs podstawowy.

## Podsumowanie partii

| Partia | PR | Pytania przeredagowane | Zakres |
|---|---|---:|---|
| B-01–04 | [#472](../../pull/472) | 5 | ADR-B-0313, 0266, 0317, 0318, 0353 |
| B-05–08 | [#473](../../pull/473) | 6 | ADR-B-0184, 0223, 0379, 0479, 0552, 0565 |
| B-09–13 | [#474](../../pull/474) | 6 | ADR-B-0079, 0213, 0228, 0248, 0398, 0531 |
| **Razem** | 3 partie | **17** | 17 pytań; bez zmian ID, działu i poprawnej litery |

Poprawiono potwierdzone przypadki dystraktorów absurdalnych, żartobliwych albo łatwych do odrzucenia bez znajomości tematu. Zastąpiono je realistycznymi pomyłkami: myleniem wymagań, nadmiernym poleganiem na dokumentach lub oznakowaniu, pominięciem warunków bezpieczeństwa oraz błędnym przenoszeniem zasad z jednej sytuacji na inną.

## Explanation i statusy

- Przepisano wyjaśnienia dla 17 pytań.
- Każde wyjaśnienie ma 2–5 zdań i co najmniej 300 znaków; najpierw wyjaśnia sens poprawnej odpowiedzi, potem błąd w dystraktorach, a na końcu podaje podstawę ADR.
- Bank nadal zawiera 609 `needs_review`, 0 `verified`.
- Nie zmieniano poprawnych liter ani numeracji. Nie wprowadzano zmian prawnych bez potwierdzenia.

## Spójność materiałów po edycjach

Po każdej partii zsynchronizowano:
- arkusze i klucze egzaminów próbnych 001–005 z aktualnym blobem banku;
- kopie opcji i explanation w wariantach/kluczach, gdy dany zmieniony ID był w egzaminie;
- `current_bank_blob_sha` i pole migawki 4x31 w `review/specialist/PAKIET-0609-MANIFEST.json`;
- nagłówek bank SHA w indeksie `review/specialist/REJESTR-AKTUALNY-0001-0609.md`;
- snapshoty audytów `review/sequential/` i `review/legal-clauses/` dla zmienionych pytań.

Końcowy bank blob SHA: `84a7df797344eef50dc47f7a460b92d8cfa89b09`. Manifest i snapshot 4x31 wskazują ten sam SHA.

## Lekcje i scenariusze

Kontrola struktury wszystkich 13 lekcji wykazała:
- 13/13 ma sekcję „Co musisz zapamiętać”;
- 13/13 ma scenariusze praktyczne;
- 13/13 ma odwołania do pytań w banku;
- 0 brakujących ID pytań i 0 odwołań do pytań z niewłaściwego działu.
- Mapa praktyki zawiera 39 scenariuszy, po 3 na dział.

## Wskaźnik „poprawna = jedyna najdłuższa” po wszystkich partiach

| Dział | Pytań | Liczba | Udział | Najkrótsze explanation | Klucz A/B/C |
|---|---:|---:|---:|---:|---|
| ADR-B-01 | 45 | 6 | 13.33% | 300 znaków | 17/17/11 |
| ADR-B-02 | 56 | 7 | 12.50% | 300 znaków | 21/19/16 |
| ADR-B-03 | 49 | 7 | 14.29% | 300 znaków | 16/21/12 |
| ADR-B-04 | 46 | 6 | 13.04% | 301 znaków | 15/18/13 |
| ADR-B-05 | 43 | 5 | 11.63% | 300 znaków | 18/14/11 |
| ADR-B-06 | 45 | 5 | 11.11% | 301 znaków | 16/14/15 |
| ADR-B-07 | 48 | 6 | 12.50% | 304 znaków | 18/18/12 |
| ADR-B-08 | 42 | 5 | 11.90% | 303 znaków | 12/12/18 |
| ADR-B-09 | 46 | 3 | 6.52% | 301 znaków | 13/15/18 |
| ADR-B-10 | 55 | 4 | 7.27% | 308 znaków | 19/18/18 |
| ADR-B-11 | 43 | 6 | 13.95% | 300 znaków | 12/13/18 |
| ADR-B-12 | 44 | 6 | 13.64% | 303 znaków | 14/13/17 |
| ADR-B-13 | 47 | 4 | 8.51% | 308 znaków | 15/15/17 |
- Globalnie: **70/609 = 11,49%**; limit CI wynosi 16%, a wszystkie działy są poniżej 18%.
- Wyjaśnienia poniżej 200 znaków: 0.
- Zduplikowane ID: 0.

## Quality Gate i ograniczenia

- PR #472: PASS, [run #40298674055](../../actions/runs/40298674055).
- PR #473: PASS, [run #40299269748](../../actions/runs/40299269748).
- PR #474: PASS, [run #40299789345](../../actions/runs/40299789345).
- W pierwszych przebiegach CI ujawniły się nieaktualne snapshoty po edycji pytań; poprawiono je w tych samych gałęziach. Końcowe przebiegi przeszły.
- Wyniki są kontrolą jakości redakcyjnej i integralności plików, a nie zatwierdzeniem prawnym. Wszystkie pytania pozostają `needs_review`; pełna niezależna weryfikacja względem polskiego tekstu urzędowego i sprostowania nadal jest wymagana.
