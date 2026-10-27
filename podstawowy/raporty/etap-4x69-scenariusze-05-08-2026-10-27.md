# Etap 4x69 — scenariusze i spójność B-05–08

- Punkt bazowy: świeży `main` `c7ea9dce7f85662134739a5818e6d8f9208356b4`.
- Zakres: ADR podstawowy, działy B-05–08.
- Bank: 609 pytań, bez zmian w treści pytań i kluczach.

## Potwierdzony problem i poprawka

`SC-ADR-B-07` i `SC-ADR-B-07-02` miały identyczny zestaw pytań: `ADR-B-0020`, `ADR-B-0517`, `ADR-B-0584`, mimo że ćwiczyły różne aspekty sytuacji. W `SC-ADR-B-07-02` zachowano pytanie o uszkodzone opakowanie (`ADR-B-0020`), a dwa powtarzające się zastąpiono pytaniami o obowiązki nadawcy oraz zakres obowiązków uczestników: `ADR-B-0365` i `ADR-B-0479`. Wszystkie trzy ID istnieją i należą do B-07.

## Zabezpieczenie Quality Gate

Rozszerzono `validate_practical_scenario_map`, aby zgłaszał identyczne zestawy `question_ids` w scenariuszach tego samego modułu. Dodano test jednostkowy z celowo powtórzonymi zestawami, który potwierdza, że walidator wykrywa regresję. To kontrola dydaktycznej różnorodności, nie potwierdzenie poprawności prawnej odpowiedzi.

## Powiązania B-05–08

| Scenariusz | Pytania | Kontrola |
|---|---|---|
| `SC-ADR-B-05` — Awaria: bezpieczne zgłoszenie i dostępność sprzętu | `ADR-B-0169`, `ADR-B-0585`, `ADR-B-0594` | PASS — wszystkie ID istnieją i należą do działu |
| `SC-ADR-B-06` — Kontrola oznakowania kontenera | `ADR-B-0507`, `ADR-B-0546`, `ADR-B-0562` | PASS — wszystkie ID istnieją i należą do działu |
| `SC-ADR-B-07` — Niezgodne opakowanie i uszkodzona sztuka przesyłki | `ADR-B-0020`, `ADR-B-0517`, `ADR-B-0584` | PASS — wszystkie ID istnieją i należą do działu |
| `SC-ADR-B-08` — Kontrola wyposażenia pojazdu i każdego członka załogi | `ADR-B-0596`, `ADR-B-0597`, `ADR-B-0423` | PASS — wszystkie ID istnieją i należą do działu |
| `SC-ADR-B-05-02` — Awaria na poboczu: pierwsze decyzje kierowcy | `ADR-B-0106`, `ADR-B-0220`, `ADR-B-0594` | PASS — wszystkie ID istnieją i należą do działu |
| `SC-ADR-B-05-03` — Pożar przy przestrzeni ładunkowej | `ADR-B-0107`, `ADR-B-0222`, `ADR-B-0223` | PASS — wszystkie ID istnieją i należą do działu |
| `SC-ADR-B-06-02` — Rozbieżność numeru na tablicy i w dokumentach | `ADR-B-0016`, `ADR-B-0507`, `ADR-B-0217` | PASS — wszystkie ID istnieją i należą do działu |
| `SC-ADR-B-06-03` — Nalepka zasłonięta podczas załadunku | `ADR-B-0133`, `ADR-B-0546`, `ADR-B-0550` | PASS — wszystkie ID istnieją i należą do działu |
| `SC-ADR-B-07-02` — Niejasny podział obowiązków przy uszkodzonym opakowaniu | `ADR-B-0020`, `ADR-B-0365`, `ADR-B-0479` | PASS — wszystkie ID istnieją i należą do działu |
| `SC-ADR-B-07-03` — Przekazanie instrukcji pisemnych nowemu członkowi załogi | `ADR-B-0019` | PASS — wszystkie ID istnieją i należą do działu |
| `SC-ADR-B-08-02` — Kontrola gaśnicy przed wyjazdem | `ADR-B-0074`, `ADR-B-0423`, `ADR-B-0283` | PASS — wszystkie ID istnieją i należą do działu |
| `SC-ADR-B-08-03` — Wyposażenie osobiste dla całej załogi | `ADR-B-0596`, `ADR-B-0597`, `ADR-B-0076` | PASS — wszystkie ID istnieją i należą do działu |

Dla B-05, B-06, B-07 i B-08 sprawdzono również kompletność powiązań pytań w lekcjach: wszystkie ID występują w banku i należą do właściwego modułu. Każdy z czterech działów ma trzy scenariusze; każdy ma co najmniej trzy kroki, kryteria oceny i granicę bezpieczeństwa.

## Metryki banku

- 609 pytań, 609 `needs_review`, 0 `verified`.
- Poprawna odpowiedź jest jedyną najdłuższą w 72/609 = 11,82% globalnie.
- B-05: 5/43 = 11,63%; B-06: 5/45 = 11,11%; B-07: 6/48 = 12,50%; B-08: 5/42 = 11,90%.
- Explanation minimum 300 znaków; 0 poniżej 200.
- Nie zmieniano poprawnych liter ani źródeł ADR.

## Ograniczenia

Nie stwierdzono potwierdzonego błędu prawnego w tej kontroli mapowania. Materiały pozostają do niezależnej recenzji specjalisty; niczego nie oznaczono jako `verified`.
