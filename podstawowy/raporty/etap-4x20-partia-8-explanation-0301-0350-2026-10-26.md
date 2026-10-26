# Etap 4x20 — ręczny audyt explanation ADR-B-0301–0350

- Punkt wyjścia: świeży `main` po PR #386, commit `600604382aee3253764e492dcd8aa8c81543d48c`.
- Zakres: wszystkie 50 pytań ADR-B-0301–ADR-B-0350.
- Metoda: skryptowe wskazanie krótkich/żargonowych wyjaśnień i akronimów, a następnie ręczna ocena sensu odpowiedzi dla początkującego kursanta.

## Wynik

Ręcznie sprawdzono 50/50 wyjaśnień. Przepisano 10 wyjaśnień, aby rozwinąć terminy lub wyjaśnić ich znaczenie praktyczne:

| ID | Co doprecyzowano |
|---|---|
| ADR-B-0314 | Numer UN jako czterocyfrowy identyfikator i rola kolumny 2 tabeli A. |
| ADR-B-0318 | Numer UN oraz klasyfikacja odpadu na podstawie dostępnych danych. |
| ADR-B-0319 | Kategorie pojazdów EX/II, EX/III, FL i AT w prostym języku. |
| ADR-B-0320 | IMDG jako kodeks morski oraz ICAO jako wymagania dla przewozu lotniczego. |
| ADR-B-0321 | IMDG jako dokumentacja dla przewozu morskiego. |
| ADR-B-0324 | Znaczenie oznaczenia opakowania UN i odrębność dopuszczenia opakowania od wspólnego załadunku. |
| ADR-B-0325 | Numer UN i procedura dla odpadu o nieznanym składzie. |
| ADR-B-0327 | Znaczenie pozycji UN 3077/3082 i warunek wyłącznego zagrożenia środowiskowego. |
| ADR-B-0329 | Numer UN oraz brak automatycznego zwolnienia dla odpadu. |
| ADR-B-0334 | Skrót i.n.o. oraz znaczenie pozycji UN 3082. |

Pozostałe 40 wyjaśnień pozostawiono bez zmian: skróty były już objaśnione w kontekście albo zdania wystarczająco jasno wyjaśniały, dlaczego pozostałe odpowiedzi nie pasują. Przykładowe fałszywe alarmy: ADR-B-0315 (wyjaśnia, że numer UN wskazuje konkretną pozycję wykazu), ADR-B-0322 (LQ jest rozwinięte jako ilości ograniczone), ADR-B-0341 i ADR-B-0343 (numer UN jest już objaśniony wprost).

Nie zmieniono pytań, opcji, poprawnych liter, modułów ani statusów. Wszystkie rekordy pozostają `needs_review`; żaden nie został oznaczony jako `verified`.

## Lista wszystkich sprawdzonych ID

ADR-B-0301, ADR-B-0302, ADR-B-0303, ADR-B-0304, ADR-B-0305, ADR-B-0306, ADR-B-0307, ADR-B-0308, ADR-B-0309, ADR-B-0310, ADR-B-0311, ADR-B-0312, ADR-B-0313, ADR-B-0314, ADR-B-0315, ADR-B-0316, ADR-B-0317, ADR-B-0318, ADR-B-0319, ADR-B-0320, ADR-B-0321, ADR-B-0322, ADR-B-0323, ADR-B-0324, ADR-B-0325, ADR-B-0326, ADR-B-0327, ADR-B-0328, ADR-B-0329, ADR-B-0330, ADR-B-0331, ADR-B-0332, ADR-B-0333, ADR-B-0334, ADR-B-0335, ADR-B-0336, ADR-B-0337, ADR-B-0338, ADR-B-0339, ADR-B-0340, ADR-B-0341, ADR-B-0342, ADR-B-0343, ADR-B-0344, ADR-B-0345, ADR-B-0346, ADR-B-0347, ADR-B-0348, ADR-B-0349, ADR-B-0350

## Kontrola wskaźników

- Bank: 609 pytań; duplikaty ID: 0.
- Explanation poniżej 200 znaków: 0; najkrótsze: 300 znaków.
- Wszystkie zmienione explanation mają 200–500 znaków.
- Poprawna odpowiedź jako jedyna najdłuższa: 73/609 = 11.99%.
- Wskaźnik per dział:
  - ADR-B-01: 6/45 = 13.33%
  - ADR-B-02: 8/56 = 14.29%
  - ADR-B-03: 7/49 = 14.29%
  - ADR-B-04: 6/46 = 13.04%
  - ADR-B-05: 6/43 = 13.95%
  - ADR-B-06: 5/45 = 11.11%
  - ADR-B-07: 6/48 = 12.5%
  - ADR-B-08: 5/42 = 11.9%
  - ADR-B-09: 4/46 = 8.7%
  - ADR-B-10: 4/55 = 7.27%
  - ADR-B-11: 6/43 = 13.95%
  - ADR-B-12: 6/44 = 13.64%
  - ADR-B-13: 4/47 = 8.51%

## Synchronizacja śladów audytu i egzaminów

Po zmianie wyjaśnień zsynchronizowano dokładne snapshoty w `review/sequential` i `review/legal-clauses` dla wszystkich zmienionych rekordów. Zaktualizowano `source_bank_head` w wariantach i kluczach egzaminu próbnego 001–005. Poprawne litery i kolejność pytań egzaminacyjnych pozostały bez zmian.

## Ograniczenia

Jest to przegląd redakcyjny i językowy, nie formalna akceptacja prawna. Podstawy prawne pozostały niezmienione; pytania nadal wymagają niezależnej recenzji specjalisty.
