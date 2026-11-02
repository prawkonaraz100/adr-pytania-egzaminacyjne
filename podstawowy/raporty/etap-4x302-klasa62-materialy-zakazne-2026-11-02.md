# Etap 4x302 — klasa 6.2: materiały zakaźne

Data: 2026-11-02. Gałąź `stage4x302-class62-infectious-substances`; punkt wyjścia main `13cbac7f`.

- ADR-B-0728 do ADR-B-02-K10; kompetencja uzupełniona z 5 do 6 pytań.
- **Kompetencje teorii <6 pytań: 52** (poprzednio 53; 3 praktyczne pomijane).
- Bank: 728 pytań, 728 `needs_review`, 0 `verified`; SHA `eaeeceaf087c739347aa93e99a57f37567f5d344`.
- Rozkład A/B/C: 242/261/225. Poprawna jako jedyna najdłuższa: 81/728 = 11,13%; maksimum działu 15,12% (limit 18%).
- Klucz C; długości opcji A/B/C 97/107/99; explanation 326 znaków.
- Podstawa: ADR 2025, 2.2.62.1.1 (materiały zakaźne) i 8.3.3 (zakaz otwierania sztuk przesyłki przez kierowcę lub pomocnika). Oficjalny tekst jest źródłem wiążącym; niezależna recenzja specjalisty i literalne porównanie nadal wymagane.
- Odświeżono klucze/warianty 001–005, snapshoty sequential/legal 728, ledger i SHA, kolejki, manifest PAKIET-0728, rejestr specjalisty, README, coverage i testy regresji.

## Pytanie

Kierowca odbiera zamknięte opakowanie z materiałem zakaźnym klasy 6.2. Pracownik prosi, by otworzył je i sprawdził zawartość przed załadunkiem. Jak powinien postąpić kierowca?

A. Otworzyć opakowanie na świeżym powietrzu, bo w ten sposób można szybko potwierdzić rodzaj próbki.

B. Otworzyć opakowanie tylko na chwilę, jeśli przez rękawice nie widać uszkodzeń jego zewnętrznej powierzchni.

C. Nie otwierać przesyłki; sprawdzić jej stan zewnętrzny i zgłosić wątpliwości osobom odpowiedzialnym.

Materiał zakaźny może zawierać drobnoustroje zdolne wywołać chorobę, więc nie wolno narażać się przez otwieranie przesyłki. Kierowca ocenia jej stan z zewnątrz i w razie problemu zgłasza go właściwym osobom. Otwarcie na powietrzu ani krótkie zajrzenie do środka nie usuwa zagrożenia. Podstawa: ADR 2025, 2.2.62.1.1 oraz 8.3.3.
