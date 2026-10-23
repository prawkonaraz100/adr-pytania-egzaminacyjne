# ETAP 4f — słownik i reguły redakcyjne ADR podstawowego

Celem jest **spójne nazewnictwo 13 lekcji i 519 rekordów banku**, bez masowego przepisywania sensu pytań lub snapshotów audytu. Każdą zmianę treści należy osobno recenzować. Karty powtórkowe: `docs/POWTORKI-13-DZIALOW.md`.

| Preferowany termin | Rozróżnienie i zasada użycia | Punkt ADR do kontroli |
|---|---|---|
| numer UN | Nie: numer rozpoznawczy zagrożenia; to identyfikator towaru UN, często w dolnym polu tablicy pomarańczowej | 5.3.2.2.2; 5.4.1.1.1(a) |
| numer rozpoznawczy zagrożenia | Nie: numer UN; na tablicy numerowanej u góry, wskazuje rodzaj zagrożenia | 5.3.2.2.2; 5.3.2.3.1 |
| sztuka przesyłki | Nie zawsze: pojedynczy produkt czy paleta; stosować zgodnie z definicją ADR | 1.2.1 |
| nalepka ostrzegawcza | Na sztuce przesyłki; nie mylić z nalepką wielkiego formatu na kontenerze | 5.2.2; 5.3.1 |
| nalepka wielkiego formatu | Stosowana dla określonych jednostek transportowych; osobne zasady rozmiarów i umiejscowienia | 5.3.1 |
| ilości ograniczone (LQ) | Nie: 1.1.3.6; osobny zestaw wymogów i oznakowanie | 3.4 |
| ilości wyłączone (EQ) | Nie: LQ; kod z kolumny 7b, E0 oznacza brak dostępności tej ścieżki | 3.5; 3.2 kol.7b |
| instrukcje pisemne | Informacje dla załogi przed podróżą, nie dokument przewozowy ani karta charakterystyki | 5.4.3 |
| towary niebezpieczne dużego ryzyka | Pojęcie ochrony security z osobnymi progami i przypadkami | 1.10.3 |
| kod ograniczenia tunelowego | Odnosi się do konkretnego towaru, sposobu przewozu i kategori tunelu, nie do całej klasy automatycznie | 8.6 |
| rozładowca / odbiorca | Nie zawsze jedna strona; obowiązki określone odrębnie | 1.4.2.3; 1.4.3.7 |
| gaśnica / sprzęt ochronny | Środki przeciwpożarowe i osobiste to osobne kategorie wyposażenia | 8.1.4; 8.1.5 |

## Reguły kontroli edytorskiej

1. Zachowuj dokładne nazwy w dokumentach i opisach towarów; używaj *numer UN* a nie *numer zagrożenia*, gdy mowa o identyfikatorze 4-cyfrowym towaru.
2. Nie nazywaj oznakowania LQ/EQ „nalepką klasy ADR”. Nie utożsamiaj wyjątku częściowego z całkowitym brakiem wymagań.
3. Nie łącz zadania ćwiczenia praktycznego P1/P2/P3 z zaliczeniem quizu.
4. Zamiast absolutnych słów („zawsze”, „nigdy”) podawaj warunki lub wskazuj właściwy wyjątek.
5. Różnicuj świadomie właściwy uczestnik (nadawca/załadowca/rozładowca/odbiorca/przewoźnik/kierowca).
6. Numeracja w rejestrach prawnych, pytaniach i 13 lekcjach musi odnosić się do tego samego wydania ADR 2025; zmienione rekordy wymagają odnowienia legal i sequential snapshots.
7. Niniejszy słownik jest wzorcem redakcyjnym, nie świadectwem wykonania pełnego audytu 519 pytań. Wszystko remains needs_review.
