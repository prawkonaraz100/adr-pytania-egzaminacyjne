# Etap 4x36 — kontrola podpowiedzi leksykalnych w treści pytań

- Data: 26.10.2026.
- Punkt wyjścia: świeży `main` po PR #478, commit `0fdf270066f2ef45fd9be67b38d665068855ac53`.
- Zakres: 609 pytań kursu podstawowego.

## Skan i ręczna ocena

Skan fraz dwuwyrazowych wykrył 41 kandydatów, w których fraza występuje jednocześnie w treści pytania i tylko w poprawnej odpowiedzi. To heurystyka — nie każdy wspólny termin zdradza odpowiedź. W wielu przypadkach termin jest niezbędny do opisania wymogu ADR, np. „dokument tożsamości”, „ograniczenie tunelowe” albo „ponowny załadunek”. Nie zmieniano takich pozycji automatycznie.

Dwa potwierdzone przypadki poprawiono:
- **ADR-B-0148:** usunięto z treści pytania powtórzenie frazy „prawo jazdy odpowiedniej kategorii”. Pytanie nadal sprawdza, że zaświadczenie ADR nie zastępuje uprawnień do prowadzenia właściwego zestawu.
- **ADR-B-0226:** treść pytania nie powtarza już wprost „litery UN przed czterocyfrowym numerem”; kursant musi rozpoznać, jak uzupełnić niekompletny identyfikator. Poprawna odpowiedź pozostała A.

Kandydat **ADR-B-0127** został już przeredagowany w etapie 4x34, więc w tej partii nie zmieniano go ponownie. Przykłady uznane za naturalne powtórzenie terminologii: ADR-B-0009 („przed ponownym załadunkiem”), ADR-B-0034 („dokument tożsamości”) i ADR-B-0065 („ograniczeń tunelowych”). Samo powtórzenie słów nie dowodzi podpowiedzi; ocena wymaga sprawdzenia, czy dystraktory są wiarygodne i czy pytanie nadal mierzy wiedzę.

## Zmiany i zachowane statusy

| ID | Zmiana | Poprawna litera | Explanation |
|---|---|---:|---:|
| ADR-B-0148 | Skrócono echo słów z treści pytania; sens pytania zachowany | B | 369 znaków |
| ADR-B-0226 | Usunięto bezpośrednie podanie słów, które należy uzupełnić | A | 336 znaków |

ID, dział i poprawna litera nie uległy zmianie. Nie dodano nowych pytań ani nie oznaczono niczego jako `verified`. Snapshoty sekwencyjne i klauzulowe oraz manifest pakietu recenzyjnego zaktualizowano.

## Metryki po zmianach

- Bank: 609 pytań, 0 zduplikowanych ID; 609 `needs_review`, 0 `verified`.
- Explanation poniżej 300 znaków: 0.
- „Poprawna odpowiedź jest jedyną najdłuższą”: **72/609 = 11,82%** globalnie; każdy dział pozostaje poniżej 18%.
- Egzaminy próbne 001–005 i klucze wskazują aktualny blob banku `c564077110cc812bb5f980a03c57363038d29967`. Żaden z dwóch zmienionych ID nie występuje w arkuszach; zaktualizowano źródłową migawkę banku we wszystkich wariantach i kluczach.

## Ograniczenia

Skan wykrywa tylko wybrane wzorce leksykalne; nie dowodzi, że pozostałe 39 kandydatów jest poprawnych dydaktycznie. Zostały zachowane bez zmian, ponieważ wspólne terminy były potrzebne do precyzyjnego opisania badanego wymogu, a automatyczna zmiana mogłaby zniekształcić sens prawny. Materiał nadal wymaga recenzji specjalisty. Nie rozpoczęto pracy nad cysternami ani innym kursem.
