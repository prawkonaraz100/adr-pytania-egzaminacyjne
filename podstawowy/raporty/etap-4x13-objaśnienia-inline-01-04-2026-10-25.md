# Etap 4x13 — objaśnienia inline w lekcjach ADR-B-01–04

- Punkt wyjścia: świeży `main` `2917d7f8ac097267858134e768e6711933559aab`.
- Zakres: kurs podstawowy, lekcje B-01–04 i kotwice słowniczka. Bank pytań i klucze egzaminów bez zmian.

## Zmiany
- Dodano objaśnienia przy pierwszym użyciu 22 terminów łącznie: B-01: 8; B-02: 7; B-03: 4; B-04: 3.
- Uproszczono po jednym zdaniu w każdej lekcji (4 łącznie), wyjaśniając sens wymogu i praktyczne działanie kierowcy.
- Dodano/ujednolicono kotwice HTML w tabeli słowniczka, żeby odsyłacze kierowały do konkretnego hasła.
- Poprawiono cel kotwicy dla „ADR 1.1.3.6 — wyłączenie ilościowe” po sprawdzeniu faktycznego identyfikatora w słowniczku.

## Przykłady przed → po
1. **B-01**
   - Przed: „W ujęciu ADR towary niebezpieczne to towary, których międzynarodowy przewóz drogowy jest zabroniony albo dopuszczony wyłącznie na warunkach określonych w załącznikach A i B.”
   - Po: „W ADR „towary niebezpieczne” to towary, których przewóz drogą jest zakazany albo dozwolony tylko po spełnieniu konkretnych warunków. Dlatego przed wyjazdem sprawdź wpis towaru i wymagania z załączników A i B.”
2. **B-02**
   - Przed: „Klasyfikacja wynika z właściwości towaru i przepisów ADR.”
   - Po: „O klasie decydują właściwości towaru oraz kryteria ADR, a nie kolor opakowania czy nazwa handlowa. Gdy etykieta i dokumenty się różnią, nie zgaduj — wyjaśnij rozbieżność przed przewozem.”
3. **B-03**
   - Przed: „Co do zasady ADR 5.2.1.8.1 przewiduje limit do 5 l dla cieczy i do 5 kg netto dla ciał stałych w odpowiednim opakowaniu pojedynczym lub wewnętrznym, pod warunkiem spełnienia pozostałych kryteriów.”
   - Po: „Dla niektórych opakowań ADR pozwala nie umieszczać znaku zagrożenia środowiskowego, jeśli ilość nie przekracza 5 l cieczy albo 5 kg netto ciała stałego i spełnione są pozostałe warunki. Sama mała ilość nie wystarcza — sprawdź też rodzaj opakowania i kryteria ADR 5.2.1.8.1.”
4. **B-04**
   - Przed: „ADR 8.3.5 zabrania palenia podczas czynności ładunkowych w pojazdach oraz w ich pobliżu; obejmuje to również e-papierosy i podobne urządzenia.”
   - Po: „Podczas załadunku i rozładunku nie pal w pojeździe ani w jego pobliżu. Zakaz obejmuje też e-papierosy i podobne urządzenia, bo mogą stanowić źródło zapłonu (ADR 8.3.5).”

## Kontrola odsyłaczy
- B-01: 8 odsyłaczy inline; brakujące kotwice: 0.
- B-02: 7 odsyłaczy inline; brakujące kotwice: 0.
- B-03: 4 odsyłaczy inline; brakujące kotwice: 0.
- B-04: 3 odsyłaczy inline; brakujące kotwice: 0.

## Bank — metryka bez zmian
- Liczba pytań: 609; nie zmieniano ID, odpowiedzi ani explanation.
- „Poprawna = jedyna najdłuższa” per dział:
  - ADR-B-01: 7/45 = 15.56%.
  - ADR-B-02: 8/56 = 14.29%.
  - ADR-B-03: 7/49 = 14.29%.
  - ADR-B-04: 7/46 = 15.22%.
- Wymagania explanation ≥200 znaków i statusy w banku nie były modyfikowane w tej partii.

## Testy
- Sprawdzono automatycznie, że każdy dodany odsyłacz inline z B-01–04 wskazuje istniejącą kotwicę w słowniczku.
- Pełny blokujący test „pierwsze wystąpienie w akapicie” zostanie włączony w partii B-09–13, po wprowadzeniu objaśnień we wszystkich lekcjach, aby nie blokować poprawnych PR-ów pośrednich.
- Dostęp do środowiska lokalnego nie jest dostępny w tej sesji; walidację repo wykonuje CI na PR. Nie oznaczono żadnego pytania jako `verified`.
