# Etap 4x304 — klasa 8: żrące pary i mgły przy wilgoci powietrza

2026-11-02. Bazowy main `5c19985f`; gałąź `stage4x304-class8-corrosives`.

- Dodano ADR-B-0730 do ADR-B-02-K12; kompetencja uzupełniona z 5 do 6 pytań.
- **Kompetencje teorii <6 pytań: 50** (poprzednio 51; trzy praktyczne pomijane).
- Bank 730 pytań, 730 `needs_review`, 0 `verified`; SHA `1c9843ec48321d6a46dbc75f9f104d034dc26dba`.
- Rozkład kluczy A/B/C: 243/262/225.
- „Poprawna odpowiedź jest jedyną najdłuższą”: **81/730 = 11,10%**; pytanie 0730 ma długości A/B/C 98/125/116, więc poprawna A nie jest najdłuższa i wskaźnik nie wzrasta.
- Explanation: 375 znaków, 4 zdania; klucz A; odpowiedzi A/B/C poddane audytowi — A opisuje wprost wyjątek wilgotności z 2.2.8.1.1, B pomija go, C myli żrące działanie z toksycznością.
- Podstawa: ADR 2025, 2.2.8.1.1. Pełne literalne porównanie tekstu polskiego i niezależna recenzja specjalisty pozostają wymagane.
- Odświeżono klucze egzaminów próbnych 001–005 (source_bank_head), snapshoty sequential/legal 730, manifest pakietu, rejestr specjalisty i bieżące metryki coverage.

## Pytanie

Karta towaru wskazuje, że substancja w stanie suchym nie działa żrąco, ale w kontakcie z naturalną wilgocią powietrza tworzy żrącą mgłę. Jak należy rozumieć jej klasyfikację ADR?

A. Tak. Klasa 8 obejmuje też substancje tworzące żrące pary lub mgły pod wpływem wilgoci z powietrza.

B. Nie. Materiał musi być żrący już w stanie suchym, bez kontaktu z wilgocią z otoczenia, inaczej nie spełnia definicji klasy 8.

C. Nie. Każda mgła lub para oznacza wyłącznie zagrożenie zatruciem klasy 6.1, a nie działanie żrące opisane w klasie 8.

Taka substancja może należeć do klasy 8, mimo że w stanie suchym nie powoduje korozji: wilgoć z powietrza może uruchomić powstawanie żrącej mgły lub pary. Kierowca nie powinien więc uznawać jej za bezpieczną tylko dlatego, że nie widać cieczy ani wycieku. Odpowiedź B pomija ten przypadek, a C myli działanie żrące z samym zagrożeniem trującym. Podstawa: ADR 2025, 2.2.8.1.1.

## Audyt A/B/C i źródła

- A — poprawna: 2.2.8.1.1 obejmuje substancje tworzące żrące pary lub mgły w obecności naturalnej wilgoci powietrza.
- B — błędna: zawęża definicję do substancji żrących już w stanie suchym.
- C — błędna: postać mgły/pary sama w sobie nie przesądza o klasie 6.1; decyduje opisane działanie żrące.
- Źródło do kontroli tekstu polskiego: Dz.U. 2025 poz. 642, ADR 2025, 2.2.8.1.1 — https://eli.gov.pl/api/acts/DU/2025/642/text.pdf.
- Status pozostaje `needs_review`; bez oznaczenia `verified`.
