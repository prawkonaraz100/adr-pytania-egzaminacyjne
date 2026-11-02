# Etap 4x313 — bezpieczne zatrzymanie i wyłączenie silnika

2026-11-02. Bazowy main `2761336780f399f0660d4974993c74c4c9e7fa80`; gałąź `stage4x313-safe-stop-engine-shutdown`.

- Dodano ADR-B-0739 do `ADR-B-05-K02`: bezpieczne zatrzymanie i wyłączenie silnika, z uwzględnieniem warunku bezpiecznego dostępu do wyłącznika głównego akumulatora.
- Kompetencja wzrosła z 5 do 6 pytań; kompetencje teorii z mniej niż 6 pytaniami: **41** (3 praktyczne pominięte).
- Bank: 739 pytań (ADR-B-0001–0739), 739 `needs_review`, 0 `verified`; SHA `84e83d8ee582633e06b86dfce0e35e664ead2bda`.
- Moduł ADR-B-05: 77 pytań.
- Rozkład kluczy A/B/C: 248/264/227.
- „Poprawna odpowiedź jest jedyną najdłuższą”: **81/739 = 10,96%**; maksimum działu **14,61%**. Długości opcji ADR-B-0739: A=121, B=101, C=98; poprawna C nie jest najdłuższa.
- Explanation: 422 znaki, 4 zdania. Wyjaśnia warunek „możliwe i bezpieczne”, odrzuca ryzykowne podejście do wyłącznika i ponowne uruchomienie silnika oraz wskazuje dalsze działania.
- Podstawa: ADR 2025, 5.4.3.4 — instrukcje pisemne, działania w razie wypadku lub awarii, o ile są możliwe i bezpieczne. Status `needs_review`; pełne literalne porównanie i niezależna recenzja pozostają otwarte.
- Odświeżono klucze i warianty 001–005, snapshoty sequential/legal 739, ledger, pakiety, kolejki prawne, rejestr specjalisty, coverage, lekcję B-05, README i testy liczebności.

## Pytanie ADR-B-0739

Po awarii kierowca zatrzymał pojazd w bezpiecznym miejscu i wyłączył silnik. Wyłącznik główny akumulatora znajduje się przy uszkodzonej części pojazdu, do której nie można bezpiecznie podejść. Co powinien zrobić?

A. Podejść do wyłącznika mimo ryzyka, ponieważ odłączenie akumulatora zawsze ma pierwszeństwo przed własnym bezpieczeństwem.

B. Uruchomić ponownie silnik i przestawić pojazd, zanim kierowca oceni miejsce awarii i ostrzeże innych.

C. Nie narażać się dla wyłącznika; oddalić się, ostrzec innych i wykonać dalsze bezpieczne czynności.

Instrukcje pisemne stosuje się tylko wtedy, gdy dane działanie jest możliwe i bezpieczne; nie wolno ryzykować wejścia w strefę zagrożenia dla obsługi wyłącznika. Podejście do uszkodzonej części może narazić kierowcę na wyciek lub opary, a ponowne uruchomienie silnika nie jest bezpiecznym sposobem rozwiązania sytuacji. Oddal się, ostrzeż innych i postępuj według kolejnych punktów instrukcji. Podstawa: ADR 2025, 5.4.3.4.

## Audyt A/B/C i źródła

- A — błędna: instrukcje nie wymagają narażania się dla użycia wyłącznika; działania podejmuje się tylko wtedy, gdy są możliwe i bezpieczne.
- B — błędna: ponowne uruchomienie silnika nie jest sposobem rozwiązania sytuacji awaryjnej i może zwiększyć zagrożenie.
- C — poprawna: jeżeli podejście do wyłącznika nie jest bezpieczne, kierowca nie podejmuje tego działania, oddala się, ostrzega innych i kontynuuje bezpieczne czynności z instrukcji.
- Źródło: Dz.U. 2025 poz. 642, ADR 2025, 5.4.3.4 — https://eli.gov.pl/api/acts/DU/2025/642/text.pdf.
- Nie oznaczono żadnego pytania jako `verified`.
