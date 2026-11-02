# Etap 4x307 — czyszczenie po przewozie luzem: wyjątek tylko dla tego samego towaru

2026-11-02. Bazowy main `7bb1d16bf950757b01e72c840d96baccc793d67b`; gałąź `stage4x307-bulk-load-same-dangerous-goods`.

- Dodano ADR-B-0733 do `ADR-B-03-K03`: oczyszczanie pojazdu po wycieku i po przewozie luzem.
- Kompetencja wzrosła z 5 do 6 pytań; kompetencje teorii z mniej niż 6 pytaniami: **47** (3 praktyczne pominięte).
- Bank: 733 pytania (ADR-B-0001–0733), 733 `needs_review`, 0 `verified`; SHA `0ca9332689073fc3750b9e0bd5d7a4a93e9a1d0b`.
- Moduł ADR-B-03: 58 pytań.
- Rozkład kluczy A/B/C: 244/264/225.
- „Poprawna odpowiedź jest jedyną najdłuższą”: **81/733 = 11,05%**; maksimum działu **14,61%**. Długości opcji ADR-B-0733: A=129, B=106, C=113; poprawna B nie jest najdłuższa.
- Explanation: 378 znaków, 4 zdania. Wyjątek z 7.5.8.2 dotyczy tylko ponownego załadunku tych samych towarów niebezpiecznych; sama zgodność klasy zagrożenia nie wystarcza.
- Podstawa: ADR 2025, 7.5.8.2. Status `needs_review`; pełne literalne porównanie i niezależna recenzja pozostają otwarte.
- Odświeżono klucze i warianty 001–005, snapshoty sequential/legal 733, ledger, pakiety, kolejki, rejestr specjalisty, coverage, lekcję B-03, README i testy regresji.

## Pytanie ADR-B-0733

Po rozładunku luzem UN 1993 firma chce załadować luzem UN 1203. Oba towary należą do klasy 3. Czy można zastosować wyjątek od czyszczenia pojazdu przewidziany w ADR 7.5.8.2?

A. Tak. Oba towary należą do klasy 3 i mają takie samo główne zagrożenie, więc wyjątek obejmuje je tak samo jak identyczny materiał.

B. Nie. To różne towary niebezpieczne; wyjątek dotyczy tylko tego samego towaru, więc pojazd trzeba oczyścić.

C. Tak, jeśli pojazd jest pusty i nie ma widocznych pozostałości, nawet gdy zmienia się numer UN i nazwa przewozowa.

Wyjątek z 7.5.8.2 dotyczy tylko ponownego załadunku tych samych towarów niebezpiecznych, a nie dowolnych materiałów z tej samej klasy. UN 1993 i UN 1203 to różne pozycje, choć oba należą do klasy 3, więc przed kolejnym załadunkiem trzeba oczyścić pojazd lub kontener. Odpowiedź A myli klasę z identycznością towaru, a C pomija obowiązek czyszczenia. Podstawa: ADR 2025, 7.5.8.2.

## Audyt A/B/C i źródła

- A — błędna: przynależność do tej samej klasy nie oznacza, że są to te same towary niebezpieczne.
- B — poprawna: UN 1993 i UN 1203 to różne towary; wyjątek dotyczy tylko ponownego załadunku tych samych towarów niebezpiecznych.
- C — błędna: brak widocznych pozostałości nie znosi obowiązku czyszczenia, gdy wyjątek nie ma zastosowania.
- Źródło: Dz.U. 2025 poz. 642, ADR 2025, 7.5.8.2 — https://eli.gov.pl/api/acts/DU/2025/642/text.pdf.
- Nie oznaczono żadnego pytania jako `verified`.
