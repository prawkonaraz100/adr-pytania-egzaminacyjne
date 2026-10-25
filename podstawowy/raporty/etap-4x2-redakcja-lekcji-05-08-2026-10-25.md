# Etap 4x2 — redakcja podręcznikowa lekcji ADR-B-05–08

- Data: 25.10.2026.
- Punkt wyjścia: `main` po PR #305, commit `9b77ed3f855b15529964f345fc01123666017260`.
- Zakres: wyłącznie kurs podstawowy ADR.

## Co zredagowano

- **B-05 — Wypadek, awaria i pierwsza pomoc:** połączono bezpieczną kolejność działań, alarmowanie, instrukcje pisemne, ograniczenia gaszenia pożaru, reakcję na wyciek, pierwszą pomoc i kontrolę dostępności gaśnicy.
- **B-06 — Numery UN, nalepki i tablice:** zebrano rozróżnienie numeru UN i numeru zagrożenia, nalepki na sztuce przesyłki i nalepki dużego formatu, tablic pomarańczowych oraz kontrolę widoczności i zgodności oznakowania.
- **B-07 — Obowiązki uczestników:** połączono role nadawcy, przewoźnika, pakującego, załadowcy, odbiorcy i kierowcy; ujęto uszkodzone opakowanie, instrukcje pisemne, przewóz pasażerów i odrębność odpowiedzialności cywilnej.
- **B-08 — Wyposażenie, gaśnice i świadectwo pojazdu:** zebrano wymagania zależne od pojazdu i przewozu, sprawność/mocowanie/dostępność gaśnic, wyposażenie osobiste każdego członka załogi oraz potrzebę sprawdzenia świadectwa dopuszczenia.

We wszystkich czterech lekcjach usunięto nagłówki dat, numery etapów, etykiety „szkic”/„wersja robocza” oraz powtarzane noty redakcyjne. Przykłady i karty kursanta połączono z odpowiednimi rozdziałami i scenariuszami.

## Materiały instruktorskie

Plany zajęć, zadania instruktorskie, kryteria obserwacji i informację zwrotną przeniesiono do:
- `podstawowy/instruktor/ADR-B-05.md`
- `podstawowy/instruktor/ADR-B-06.md`
- `podstawowy/instruktor/ADR-B-07.md`
- `podstawowy/instruktor/ADR-B-08.md`

Nie dodano fikcyjnych ocen, dat ani podpisów; materiały nie stanowią potwierdzenia realizacji zajęć praktycznych.

## Zachowanie treści i referencji

Zachowano tematy pytań i przykłady dotyczące: dostępności i mocowania gaśnic; języka instrukcji pisemnych; nieczytelnych nalepek i tablic pomarańczowych; odpowiedzialności pakującego i załadowcy; przewozu pasażerów; gaśnic i wyposażenia zależnego od DMC; wyposażenia osobistego; wymaganego świadectwa pojazdu. Pytania w banku i ich klucze nie zostały zmienione.

W starym B-05 pojawiały się referencje ADR-B-0308, ADR-B-0362 i ADR-B-0435 z innych działów. W nowym tekście wykazano wyłącznie pytania przypisane do B-05. Nie usunięto pytań z banku; skorygowano jedynie nieprawidłowe powiązania redakcyjne.

## Preflight Quality Gate

- Bank: 609 pytań; duplikaty ID: 0.
- Poprawna odpowiedź jest jedyną najdłuższą: 86/609 = 14.12% (limit 18%).
- Najkrótsze explanation: 300 znaków; wyjaśnienia poniżej 200 znaków: 0.
- Status banku: 609 `needs_review`, 0 `verified`.
- Referencje:
  - B-05: 43 unikalnych ID, brakujące 0, inne działy 0.
  - B-06: 45 unikalnych ID, brakujące 0, inne działy 0.
  - B-07: 48 unikalnych ID, brakujące 0, inne działy 0.
  - B-08: 42 unikalnych ID, brakujące 0, inne działy 0.

## Ograniczenia

Nie stwierdzono potwierdzonego błędu prawnego wymagającego zmiany klucza lub odpowiedzi. Redakcja nie jest niezależną recenzją polskiego tekstu ADR; wszystkie pytania zachowują `needs_review`. Nie rozpoczęto pracy nad cysternami ani innym kursem.
