# Etap 4t — audyt scenariuszy praktycznych dla 13 działów

- Data: 25.10.2026.
- Bazowy `main`: 2e5c2b52b64053cf51e82758d860e78ffe10e0e9.
- Zakres: wyłącznie kurs ADR podstawowy.

## Wynik kontroli przed zmianą

Plik `podstawowy/praktyka/SCENARIUSZE.md` zawierał trzy podstawowe scenariusze P1–P3 (gaśnica, pierwsza pomoc, awaria/wypadek), ale nie miał jednej, maszynowo sprawdzanej listy sytuacji drogowych przypisanej do każdego z 13 działów. Sam fakt, że każda lekcja ma przykład, nie gwarantował jednolitej procedury krok po kroku ani sprawdzalnych odwołań do pytań.

## Uzupełnienie

Dodano `podstawowy/praktyka/scenariusze-13-dzialow.json` i indeks w `SCENARIUSZE.md`. Zestaw zawiera po jednym scenariuszu dla ADR-B-01–13, każdy z sytuacją, czterema krokami, kryteriami oceny i ID pytań istniejącymi w tym samym dziale.

| Dział | Scenariusz | Pytania | Status |
|---|---|---|---|
| ADR-B-01 | Kontrola drogowa: czy przewóz korzysta ze zwolnienia? | ADR-B-0002, ADR-B-0259, ADR-B-0526 | uzupełniono |
| ADR-B-02 | Rozładunek: mokre opakowanie z nalepką 4.3 | ADR-B-0006, ADR-B-0510 | uzupełniono |
| ADR-B-03 | Wyciek przy kratce kanalizacyjnej | ADR-B-0009, ADR-B-0514 | uzupełniono |
| ADR-B-04 | Załadunek: e-papieros i pracujący silnik | ADR-B-0010, ADR-B-0012 | uzupełniono |
| ADR-B-05 | Wypadek i zagrożenie przy przesyłce | ADR-B-0013, ADR-B-0015, ADR-B-0169 | uzupełniono |
| ADR-B-06 | Kontrola oznakowania kontenera | ADR-B-0507, ADR-B-0546, ADR-B-0562 | uzupełniono |
| ADR-B-07 | Uszkodzone opakowanie mimo poprawnych dokumentów | ADR-B-0020, ADR-B-0517, ADR-B-0567, ADR-B-0568, ADR-B-0569 | uzupełniono |
| ADR-B-08 | Kontrola wyposażenia i świadectwa pojazdu | ADR-B-0418, ADR-B-0551, ADR-B-0566 | uzupełniono |
| ADR-B-09 | Kontrola przed załadunkiem i mocowania | ADR-B-0518, ADR-B-0554, ADR-B-0558 | uzupełniono |
| ADR-B-10 | Kontener po rejsie morskim — dalszy odcinek drogowy | ADR-B-0396, ADR-B-0511 | uzupełniono |
| ADR-B-11 | Wybór trasy przez tunel z ograniczeniami | ADR-B-0487, ADR-B-0539, ADR-B-0540 | uzupełniono |
| ADR-B-12 | Nieznana osoba chce odebrać ładunek | ADR-B-0304, ADR-B-0305, ADR-B-0519 | uzupełniono |
| ADR-B-13 | Kontrola dokumentów przed wyjazdem | ADR-B-0508, ADR-B-0525, ADR-B-0530 | uzupełniono |

## Bezpieczeństwo i granice

Scenariusze są symulacjami: fikcyjne dokumenty, mapy i puste makiety. Nie wymagają ani nie dopuszczają używania prawdziwych towarów niebezpiecznych, generowania wycieków lub pożarów. P1–P3 nadal wymagają rzeczywistego prowadzenia i oceny instruktora.

Dodano testy Quality Gate sprawdzające 13 unikalnych działów, co najmniej trzy kroki na scenariusz, istnienie wszystkich ID i zgodność działu pytania z działem scenariusza. Test strukturalny nie potwierdza prawnej poprawności pytań ani wykonania ćwiczeń.
