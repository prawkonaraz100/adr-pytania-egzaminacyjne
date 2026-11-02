# Etap 4x310 — zakaz palenia podczas przeładunku

2026-11-02. Bazowy main `d340a44a16781fd6e4a3df6d9955ab0a54fc8679`; gałąź `stage4x310-smoking-ban-loading-area`.

- Dodano ADR-B-0736 do `ADR-B-04-K01`: zakaz palenia w pobliżu pojazdu podczas czynności ładunkowych obejmuje także pracownika magazynu.
- Kompetencja wzrosła z 5 do 6 pytań; kompetencje teorii z mniej niż 6 pytaniami: **44** (3 praktyczne pominięte).
- Bank: 736 pytań (ADR-B-0001–0736), 736 `needs_review`, 0 `verified`; SHA `1c1ee10536eceecdc7cc34cdb2675f8605036c30`.
- Moduł ADR-B-04: 48 pytań.
- Rozkład kluczy A/B/C: 247/264/225.
- „Poprawna odpowiedź jest jedyną najdłuższą”: **81/736 = 11,01%**; maksimum działu **14,61%**. Długości opcji ADR-B-0736: A=140, B=135, C=144; poprawna A nie jest najdłuższa.
- Explanation: 377 znaków, 4 zdania. A wskazuje, że zakaz obejmuje przeładunek w pobliżu pojazdu i osobę spoza załogi; B błędnie ogranicza zakaz do kierowcy i pomocnika; C błędnie ogranicza go do wnętrza pojazdu i tradycyjnego palenia.
- Podstawa: ADR 2025, 8.3.5 — zakaz palenia podczas czynności ładunkowych w pobliżu pojazdów i wewnątrz nich, także e-papierosów i podobnych urządzeń. Status `needs_review`; pełne literalne porównanie i niezależna recenzja pozostają otwarte.
- Odświeżono klucze i warianty 001–005, snapshoty sequential/legal 736, ledger, manifesty, kolejki prawne, rejestr specjalisty, coverage, lekcję B-04, README i testy regresji.

## Pytanie ADR-B-0736

Podczas przeładunku towarów niebezpiecznych pracownik magazynu staje obok pojazdu i zapala papierosa. Tłumaczy, że zakaz z ADR dotyczy tylko kierowcy i wnętrza kabiny. Jak należy ocenić tę sytuację?

A. Przerwać czynność i zażądać zaprzestania palenia; zakaz obejmuje obsługę ładunku w pobliżu pojazdu, również gdy pali pracownik spoza załogi.

B. Pozwolić dokończyć papierosa, bo przepis z 8.3.5 dotyczy tylko kierowcy i pomocnika, a pracownik magazynu nie należy do załogi pojazdu.

C. Pozwolić palić na zewnątrz, jeśli osoba stoi poza kabiną; zakaz dotyczy tylko wnętrza pojazdu i tradycyjnych papierosów, nie samego przeładunku.

Zakaz z ADR 8.3.5 obowiązuje podczas czynności ładunkowych w pobliżu pojazdów oraz wewnątrz nich, a nie tylko w kabinie. Przepis obejmuje też e-papierosy i podobne urządzenia; nie ogranicza zakazu do kierowcy, bo dotyczy miejsca i czasu wykonywania operacji. Dlatego pracownik magazynu nie może palić przy pojeździe podczas przeładunku. Podstawa: ADR 2025, 8.3.5.

## Audyt A/B/C i źródła

- A — poprawna: zakaz odnosi się do czynności ładunkowych w pobliżu pojazdu oraz wewnątrz niego; nie ogranicza się do członków załogi.
- B — błędna: 8.3.5 nie zawęża zakazu do kierowcy i pomocnika.
- C — błędna: zakaz dotyczy również okolicy pojazdu i obejmuje e-papierosy oraz podobne urządzenia.
- Źródło: Dz.U. 2025 poz. 642, ADR 2025, 8.3.5 — https://dziennikustaw.gov.pl/DU/2025/642; tekst ADR 2025, tom II, ECE/TRANS/352 — https://unece.org/adr-2025-files.
- Nie oznaczono żadnego pytania jako `verified`.
