# Etap 4x203 — drugi przegląd explanation (partia 44)

Data: 2026-10-30. Bazowy main: `ed6ee1d4878856d5a803d7ff57156a8549475b77`. Bank: 651 pytań kursu podstawowego.

## Dobór pytań

ADR-B-0101, ADR-B-0185, ADR-B-0197, ADR-B-0229, ADR-B-0232, ADR-B-0235, ADR-B-0283, ADR-B-0294, ADR-B-0313, ADR-B-0320. Wybrano rekordy z wyjaśnieniami wymagającymi bardziej bezpośrednich wskazówek i omówienia dystraktorów, z wyłączeniem pytań ujętych w poprzednich partiach 4x156–4x202.

## Zakres zmian

Przeredagowano wyłącznie pole `explanation` w powyższych 10 rekordach. Nowe wyjaśnienia mają 354–404 znaków i 4–5 zdań: praktyczna przyczyna poprawnej odpowiedzi, dlaczego pozostałe są błędne, na końcu krótka podstawa ADR. Nie zmieniono pytań, odpowiedzi A/B/C, kluczy, źródeł ani statusów; brak potwierdzonego błędu uzasadniającego ingerencję w pozostałe pola.

## Synchronizacja

- `review/sequential` i `review/legal-clauses` uaktualniono dla 10 ID w zakresach 091–120, 181–210, 229–234, 235–240, 282–283, 294–297, 312–313, 320–322.
- Warianty i klucze egzaminów próbnych 001–005 wskazują blob `9dcd8d5681424fd604a585c33e4ee18ad918556f`. Żadne z 10 ID nie wymagało zastąpienia explanation w obecnych kluczach.
- Odświeżono manifest próbkowy, referencje SHA w dokumentacji audytu i pakietu specjalisty.

## Zastrzeżenie

Bank: 651 pytań ze statusem `needs_review`; zero `verified`. Redakcja dydaktyczna i techniczne testy spójności **nie są niezależną recenzją prawną**. Wyłącznie kurs podstawowy; nie rozpoczęto kursu cystern. Scalenie wymaga pełnego PASS CI.
