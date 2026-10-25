# Etap 4x2 — redakcja podręcznikowa lekcji ADR-B-01–04

- Data: 25.10.2026.
- Świeży `main` przed zmianami: `339e29f36fa5a9af506d7951f2d4e486499432e7`.
- Zakres: tylko kurs podstawowy ADR; bez zmian w banku, kluczach odpowiedzi ani statusach weryfikacji.

## Co zrobiono

Przepisano ADR-B-01, ADR-B-02, ADR-B-03 i ADR-B-04 do wspólnego układu:
1. Po co to jest?
2. Czego się nauczysz
3. Ponumerowane rozdziały — od podstaw do decyzji w pracy kierowcy
4. Typowe błędy kursantów
5. Scenariusze praktyczne
6. Co musisz zapamiętać
7. Sprawdź się
8. Powiązane pytania w banku
9. Podstawa prawna

Usunięto z tekstu kursanta daty, numery etapów, etykiety „szkic”, „wersja robocza”, powtarzające się zastrzeżenia redakcyjne i osobne karty/mapy, które powielały te same zasady. Ich merytoryczne treści włączono do odpowiednich rozdziałów, scenariuszy, pytań kontrolnych lub wykazu powiązanych pytań.

## Przeniesienie materiału instruktorskiego

Utworzono osobne pliki:
- `podstawowy/instruktor/ADR-B-01.md`
- `podstawowy/instruktor/ADR-B-02.md`
- `podstawowy/instruktor/ADR-B-03.md`
- `podstawowy/instruktor/ADR-B-04.md`

Przeniesiono do nich istniejące plany zajęć, mapy kompetencji, zadania instruktorskie, kryteria obserwacji i informację zwrotną. Pliki nie poświadczają realizacji zajęć; nie dodano fikcyjnych dat, ocen ani podpisów.

## Zachowanie treści i odwołań

- Zebrano przykłady o wyłączeniach prywatnych, obliczeniach 1.1.3.6, LQ/EQ, klasyfikacji i nalepkach, nadtlenkach organicznych, klasie 6.2, bateriach sodowo-jonowych, zagrożeniu środowiskowym, odpadach, wyciekach, czyszczeniu pojazdu, zakazie palenia, pracy silnika i wymaganiach postoju.
- Każda lekcja zawiera pełny wykaz ID pytań przypisanych w banku do jej modułu; testy kontrolują, że identyfikatory istnieją i nie wskazują innego działu.
- Wykryto jeden błędny odsyłacz w starym pliku B-04: ADR-B-0241 należy do działu B-03, a nie B-04. Usunięto go z treści B-04; temat zakazu otwierania przesyłek i pracy silnika wskazano przez prawidłowe pytania B-04, ADR-B-0243–0244. Banku nie zmieniano.
- Nie wykryto potwierdzonego błędu prawnego wymagającego zmiany odpowiedzi lub klucza. Redakcja nie jest niezależną weryfikacją polskiego tekstu ADR.

## Preflight banku i referencji

- Bank: 609 pytań; duplikaty ID: 0.
- Poprawna odpowiedź jest jedyną najdłuższą: 86/609 = 14.12% (limit 18%).
- Najkrótsze explanation: 300 znaków; poniżej 200 znaków: 0.
- Statusy: 609 `needs_review`, 0 `verified`.
- Referencje w lekcjach:
  - B-01: 45 unikalnych ID; brakujące: 0; ID z innego działu: 0.
  - B-02: 56 unikalnych ID; brakujące: 0; ID z innego działu: 0.
  - B-03: 49 unikalnych ID; brakujące: 0; ID z innego działu: 0.
  - B-04: 46 unikalnych ID; brakujące: 0; ID z innego działu: 0.

## Ograniczenia

Treść jest redakcyjnie ujednolicona, ale pytania i lekcje nadal wymagają niezależnej recenzji prawnej i odbioru instruktorskiego. Wszystkie pytania zachowują `needs_review`; nie nadano `verified`. Nie rozpoczęto pracy nad cysternami ani innym kursem.
