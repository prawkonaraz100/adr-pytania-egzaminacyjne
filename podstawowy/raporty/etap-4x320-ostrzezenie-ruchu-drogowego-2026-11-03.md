# Etap 4x320 — ostrzeżenie ruchu drogowego po awarii ADR

2026-11-03. Bazowy main `712ef6833bf98823ae73a534a23d6479d75ad1a6`; gałąź `stage4x320-warning-bystanders-evacuation`.

- Dodano ADR-B-0746 do `ADR-B-05-K09`: ostrzeganie ruchu drogowego i utrzymanie osób oraz pojazdów z dala od miejsca zagrożenia.
- Kompetencja wzrosła z 5 do 6 pytań; kompetencje teorii z mniej niż 6 pytaniami: **34** (3 praktyczne pominięte).
- Bank: **746** pytań (ADR-B-0001–0746), 746 `needs_review`, 0 `verified`; SHA `74c197c3add4c0f537c84254e9115f2a86a22da2`.
- Moduł ADR-B-05: **84** pytania.
- Rozkład kluczy A/B/C: 250/268/228.
- „Poprawna odpowiedź jest jedyną najdłuższą”: **81/746 = 10,86%**; maksimum działu **14,61%**. Długości wariantów ADR-B-0746: A=84, B=100, C=108; poprawna A jest najkrótsza.
- Explanation: 391 znaków, 4 zdania. Wyjaśnia obowiązek ostrzeżenia także ruchu drogowego i utrzymania go z dala od zagrożenia. B błędnie zakłada, że samo zwolnienie wystarcza; C nakazuje kierowcy wejście w obszar rozlewu i samodzielne kierowanie pojazdami.
- Podstawa: ADR 2025, 5.4.3.4 — ostrzec inne osoby i ruch drogowy o zagrożeniu oraz trzymać je z dala od strefy zagrożenia. Status `needs_review`; pełne literalne porównanie i niezależna recenzja pozostają otwarte.
- Klucze i warianty egzaminów 001–005 zsynchronizowano z SHA banku; każdy ma 30 pozycji i aktualny `source_bank_head`.
- Dodano snapshoty sequential/legal dla ADR-B-0746; ledger i manifest pakietu zaktualizowane. Rejestr specjalisty: 746 unikalnych ID, bez duplikatów. Coverage i testy liczebności zaktualizowane.

## Pytanie ADR-B-0746

Po awarii ADR kierowca znajduje się w bezpiecznym miejscu, a za pojazdem zbliżają się kolejne samochody. Jak powinien postąpić zgodnie z instrukcjami pisemnymi?

A. Ostrzec ruch drogowy i osoby w pobliżu oraz utrzymać je z dala od strefy zagrożenia.

B. Pozwolić samochodom przejechać obok zdarzenia, jeśli kierowcy zmniejszą prędkość i zachowają odstęp.

C. Samemu zatrzymywać i kierować pojazdy przez miejsce zdarzenia, nawet gdy wymaga to wejścia w strefę rozlewu.

Po awarii ostrzeż nie tylko osoby stojące obok, ale też ruch drogowy, i trzymaj wszystkich z dala od strefy zagrożenia. Nie wystarczy poprosić kierowców, by tylko zwolnili, bo nadal mogą wjechać w obszar zagrożenia. Nie kieruj samodzielnie pojazdów przez rozlew ani nie wchodź w niebezpieczne miejsce; działaj z bezpiecznej pozycji i zgodnie z poleceniami służb. Podstawa: ADR 2025, 5.4.3.4.

## Audyt A/B/C i źródła

- A — poprawna: instrukcje pisemne wymagają ostrzeżenia innych osób i ruchu drogowego oraz trzymania ich z dala od strefy zagrożenia.
- B — błędna: samo ograniczenie prędkości nie zabezpiecza przed wjazdem w obszar zdarzenia.
- C — błędna: kierowca nie powinien wchodzić w obszar rozlewu ani kierować pojazdów przez miejsce zagrożenia.
- Źródło: Dz.U. 2025 poz. 642, ADR 2025, 5.4.3.4 — https://eli.gov.pl/api/acts/DU/2025/642/text.pdf.
- Nie oznaczono żadnego pytania jako `verified`.
