# Etap 4x62 — audyt użyteczności 39 scenariuszy dla instruktora

Data: 2026-10-26. Świeży main `ca106bd9de9b318884398e157682aa2694ff58fe` (po PR #514).

## Kontrola strukturalna wszystkich 39 scenariuszy
- Dokładnie **3 scenariusze na każdy z 13 działów**.
- Wszystkie 39 zawierają czteroelementową listę kroków kierowcy (`steps`).
- Wszystkie 39 mają pytanie do kursanta (`learner_question`), minimum jeden powiązany `question_ids`, typowe błędy (`common_mistakes`), wytłumaczenie (`learner_takeaway`), podstawę (`legal_basis`) i co najmniej jedno kryterium oceny (`assessment_criteria`).
- Nie stwierdzono strukturalnych braków wymagających zmian w bazie pytań, mapie kompetencji albo wariantach egzaminów próbnych.

## Potwierdzony problem dydaktyczny
W indeksie `SCENARIUSZE.md` znajdowały się odsyłacze i podpowiedzi, lecz **brakowało jednej wspólnej, łatwej do zastosowania karty przebiegu symulacji i informacji zwrotnej**. W części scenariuszy `assessment_criteria` jest sformułowane ogólnie; nadal można je stosować, ale prowadzący potrzebuje prostego sposobu rozdzielenia bezpieczeństwa, kolejności decyzji, wyjaśnienia jej sensu i pytań powiązanych.

## Potwierdzona poprawka
Dodano `podstawowy/praktyka/KARTA-OCENY-SCENARIUSZY.md` z sześcioma krokami prowadzenia ćwiczenia i czterema obszarami informacji zwrotnej. Dodano link w indeksie `SCENARIUSZE.md`. Nie zmieniano treści scenariuszy, w szczególności oryginalnych indywidualnych `assessment_criteria`.

## Ograniczenia
To dodatkowy materiał instruktorski do bezpiecznej symulacji, **nie formalne zaliczenie zajęć praktycznych** ani zatwierdzenie przepisów. Bank 609 pytań pozostaje bez zmian: 609 `needs_review`, 0 `verified`; najnowszy potwierdzony wskaźnik 72/609 = 11,82%, min explanation 300 znaków. Nie regenerowano egzaminów ani pakietu recenzyjnego, ponieważ żaden rekord pytania nie został zmieniony.