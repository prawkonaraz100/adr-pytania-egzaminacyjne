# Etap 4x268 — widoczność i położenie tylnej tablicy pomarańczowej

Data: 01.11.2026  
Zakres: wyłącznie kurs podstawowy ADR  
Baza: main `aa9e3d38499901a516df620ce3292cd5cd0c997c`  
Gałąź: `stage4x268-orange-plate-rear-visibility`  
Nowe ID: `ADR-B-0694`  
Kompetencja: `ADR-B-06-K05` — wymiary i rozmieszczenie tablic pomarańczowych

## Wybór luki

Kompetencja miała cztery pytania, z których większość dotyczyła wymiarów tablic i wyjątku dla pojazdu, w którym brakuje miejsca. Brakowało praktycznego sprawdzenia ogólnej zasady z ADR 5.3.2.1.1: tablica z tyłu musi być dobrze widoczna, tak samo jak tablica z przodu, a obie muszą być ustawione prostopadle do osi podłużnej jednostki transportowej. Nowe pytanie sprawdza reakcję na zasłoniętą tylną tablicę przed rozpoczęciem przewozu.

## Dodane pytanie

- `ADR-B-0694`: przednia tablica jest widoczna, ale tylną zasłania koło zapasowe.
- Klucz: **B** — odsłonić tylną tablicę i zamocować ją tak, by była dobrze widoczna oraz prostopadła do osi pojazdu.
- Explanation: **404 znaki, 4 zdania**; prosty opis praktycznego znaczenia dwóch tablic, mylących odpowiedzi i podstawy ADR.
- Długości A/B/C: **130/99/74** znaki; poprawna B nie jest ani najdłuższa, ani najkrótsza.
- Audyt A/B/C: A — błędna, bo przednia tablica nie zastępuje tylnej; B — poprawna, bo przywraca widoczność i prawidłowe położenie; C — błędna, bo ustawia tablicę równolegle, a wymagana jest pozycja prostopadła.
- Status: `needs_review`; nic nie oznaczono jako `verified`.

## Podstawa prawna — źródło oficjalne sprawdzone

- **ADR 2025, 5.3.2.1.1**, tom II, s. 248: jednostka transportowa ma mieć dwie prostokątne tablice pomarańczowe — jedną z przodu, drugą z tyłu; obie prostopadle do osi podłużnej i dobrze widoczne.
- Oficjalny polski tekst ADR 2025, Ministerstwo Infrastruktury: https://www.gov.pl/attachment/b7292c03-ac9d-4f80-9a29-c22f53d847b8
- Dz.U. 2025 poz. 642: https://dziennikustaw.gov.pl/DU/2025/642
- UNECE ADR 2025: https://unece.org/adr-2025-files

Właściwy fragment punktu został sprawdzony bezpośrednio w oficjalnym polskim PDF. Pytanie dotyczy wyłącznie ogólnych tablic z 5.3.2.1.1, nie dodatkowego oznakowania bocznego w szczególnych konfiguracjach. Pełne porównanie wszystkich elementów pytania z tekstem Dz.U. oraz niezależna recenzja specjalisty pozostają pending.

## Synchronizacja #646

- Bank po dodaniu: **694** pytań, ADR-B-0001–0694; SHA banku zostanie wpisany po zatwierdzeniu commitu.
- Kompetencja `ADR-B-06-K05` otrzymała piąte pytanie; moduł ADR-B-06 ma 58 pytań.
- Klucze i warianty egzaminów próbnych 001–005 wymagają odświeżenia do nowego SHA banku.
- Snapshoty: `review/sequential/694-694.json`, `review/legal-clauses/694-694.json`; ledger, indeks specjalisty i manifest pakietu dołączone.
- Rozkład prawidłowych odpowiedzi po dodaniu: A=236/B=240/C=218.
- Globalny wskaźnik „poprawna = jedyna najdłuższa”: **72/694 = 10,37%**; maksimum działu pozostaje 13,95%.
- Quality Gate i pełne CI pozostają do potwierdzenia na PR. Lokalnego Quality Gate nie uruchamiano.

## Audyt A/B/C

| Opcja | Ocena | Uzasadnienie |
|---|---|---|
| A | Błędna | Tablice muszą być widoczne zarówno z przodu, jak i z tyłu jednostki. |
| B | Poprawna | Odsłania tylną tablicę i zachowuje wymagane położenie prostopadłe do osi. |
| C | Błędna | Ustawienie równoległe nie spełnia ogólnej zasady z 5.3.2.1.1. |

Raport nie stanowi niezależnej akceptacji prawnej ani zatwierdzenia pytania.
