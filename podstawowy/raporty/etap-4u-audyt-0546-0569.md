# ETAP 4u — audyt nowych pytań 0546–0569

- Baza: `main` `4bd276694c31200315e6ade84f46deff5501a9fc`.
- Sprawdzono **24 pytania** dodane po 0545: treść, trzy odpowiedzi A/B/C, kolejność wyjaśnienia, liczbę zdań, długość, podstawę ADR i długość opcji. Weryfikacja redakcyjna nie jest kontrolą dosłownego polskiego przepisu ani zatwierdzeniem prawnym.
- W 23/24 wyjaśnienia kończyły się odniesieniem prawnym; w **ADR-B-0565** po podstawie pojawiało się dodatkowe zdanie. Uporządkowano to wyjaśnienie, zachowując sens i klucz. Utrzymano wpisy audytu sekwencyjnego oraz A/B/C z niezmienionym statusem recenzji.
- Obecnie **24/24** wyjaśnienia mają 2–5 zdań, a podstawa znajduje się na końcu (dla 0565 po poprawce). Rozróżnienie błędnych wariantów jest opisane zbiorczo lub oddzielnie, bez nadawania statusu zatwierdzenia.
- Dla wszystkich 24 pytań poprawna odpowiedź **nie jest ściśle najdłuższa**.
- Legalność: przypisano źródła ADR 2025 (oraz Kodeks cywilny 415/471 przy 0567–0569), lecz **nie potwierdzono dosłownie wszystkich przywołanych przepisów** względem polskiego tekstu i sprostowania. Status każdego pytania pozostaje `needs_review`; niezależny specjalista musi zweryfikować przesłanki i wyjątki.

| Pytanie | Dział | Zdania | Znaki | Klucz | Klucz ściśle najdłuższy | Wynik redakcyjny |
|---|---|---:|---:|---|---|---|
| ADR-B-0546 | ADR-B-06 | 4 | 337 | B | nie | PASS redakcyjny |
| ADR-B-0547 | ADR-B-06 | 4 | 352 | A | nie | PASS redakcyjny |
| ADR-B-0548 | ADR-B-06 | 4 | 348 | C | nie | PASS redakcyjny |
| ADR-B-0549 | ADR-B-06 | 4 | 315 | B | nie | PASS redakcyjny |
| ADR-B-0550 | ADR-B-06 | 4 | 325 | A | nie | PASS redakcyjny |
| ADR-B-0551 | ADR-B-08 | 4 | 352 | C | nie | PASS redakcyjny |
| ADR-B-0552 | ADR-B-08 | 4 | 310 | B | nie | PASS redakcyjny |
| ADR-B-0553 | ADR-B-08 | 4 | 327 | C | nie | PASS redakcyjny |
| ADR-B-0554 | ADR-B-09 | 4 | 321 | A | nie | PASS redakcyjny |
| ADR-B-0555 | ADR-B-09 | 4 | 314 | B | nie | PASS redakcyjny |
| ADR-B-0556 | ADR-B-09 | 4 | 337 | C | nie | PASS redakcyjny |
| ADR-B-0557 | ADR-B-09 | 4 | 337 | A | nie | PASS redakcyjny |
| ADR-B-0558 | ADR-B-09 | 4 | 395 | B | nie | PASS redakcyjny |
| ADR-B-0559 | ADR-B-09 | 4 | 338 | C | nie | PASS redakcyjny |
| ADR-B-0560 | ADR-B-09 | 4 | 369 | B | nie | PASS redakcyjny |
| ADR-B-0561 | ADR-B-06 | 4 | 351 | A | nie | PASS redakcyjny |
| ADR-B-0562 | ADR-B-06 | 4 | 319 | B | nie | PASS redakcyjny |
| ADR-B-0563 | ADR-B-06 | 4 | 308 | C | nie | PASS redakcyjny |
| ADR-B-0564 | ADR-B-06 | 4 | 368 | C | nie | PASS redakcyjny |
| ADR-B-0565 | ADR-B-06 | 4 | 336 | A | nie | PASS redakcyjny |
| ADR-B-0566 | ADR-B-08 | 4 | 344 | B | nie | PASS redakcyjny |
| ADR-B-0567 | ADR-B-07 | 4 | 366 | A | nie | PASS redakcyjny |
| ADR-B-0568 | ADR-B-07 | 3 | 335 | B | nie | PASS redakcyjny |
| ADR-B-0569 | ADR-B-07 | 4 | 371 | C | nie | PASS redakcyjny |

## Wymagane dalsze działania

- Niezależna kontrola ADR 2025 oraz właściwych aktów krajowych, szczególnie odpowiedzialności cywilnej (0567–0569) i oznakowania po rozładunku (0548, 0563, 0565).
- Nie zmieniać `verification_status` ani kluczy bez potwierdzonego błędu.
- Bramka CI musi osiągnąć PASS przed scaleniem.
