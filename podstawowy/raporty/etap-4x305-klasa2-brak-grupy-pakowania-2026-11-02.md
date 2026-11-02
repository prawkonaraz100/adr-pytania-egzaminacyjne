# Etap 4x305 — klasa 2: brak grupy pakowania przy gazach

2026-11-02. Bazowy main `a7797e10`; gałąź `stage4x305-class2-no-packing-group`.

- Dodano ADR-B-0731 do `ADR-B-02-K14`: grupy pakowania, zagrożenia dodatkowe i tabela A.
- Kompetencja wzrosła z 5 do 6 pytań; kompetencje teorii z mniej niż 6 pytaniami: **49** (3 praktyczne pominięte).
- Bank: 731 pytań (ADR-B-0001–0731), 731 `needs_review`, 0 `verified`; SHA `7323023ff6f3fcb361caf625e781cd5cb1303d58`.
- Moduł ADR-B-02: 89 pytań.
- Rozkład kluczy A/B/C: 244/262/225.
- „Poprawna odpowiedź jest jedyną najdłuższą”: **81/731 = 11,08%**; maksimum działu **14,61%**. Długości opcji ADR-B-0731: A=67, B=109, C=100; poprawna A nie jest najdłuższa.
- Explanation: 346 znaków, 4 zdania. A prawidłowo opisuje wyłączenie klasy 2 z grup pakowania; B błędnie uznaje brak grupy za błąd; C przypisuje kierowcy nieistniejące uprawnienie do samodzielnego wyznaczania grupy.
- Podstawa: ADR 2025, 2.1.1.3 oraz 3.2.1, tabela A, kolumna (4). Status `needs_review`; pełne literalne porównanie i niezależna recenzja pozostają otwarte.
- Odświeżono klucze 001–005 i warianty 001–005, snapshoty sequential/legal 731, manifesty, ledger, kolejki prawne, rejestr specjalisty i coverage.

## Pytanie ADR-B-0731

Kierowca porównuje dokument z tabelą A ADR dla przewożonego gazu klasy 2. W kolumnie 4 nie ma grupy pakowania. Co powinien z tego wywnioskować?

A. To normalne: klasa 2 nie jest objęta systemem grup pakowania I–III.

B. Brak grupy oznacza błąd w dokumentach; przed rozpoczęciem przewozu nadawca musi dopisać grupę I, II albo III.

C. Kierowca powinien sam przypisać grupę II na podstawie tego, czy gaz jest palny, trujący lub duszący.

Brak grupy pakowania przy gazie klasy 2 nie oznacza błędu w tabeli ani dokumentach. ADR wyłącza klasę 2 z systemu grup I–III, dlatego kierowca nie powinien dopisywać grupy ani samodzielnie jej ustalać. Zamiast tego odczytuje pozostałe dane wpisu, w tym klasyfikację gazu i wymagane warunki przewozu. Podstawa: ADR 2025, 2.1.1.3 i 3.2.1, tabela A.

## Audyt A/B/C i źródła

- A — poprawna: klasa 2 jest wyłączona z systemu grup pakowania I–III.
- B — błędna: brak grupy nie jest błędem dla klasy 2.
- C — błędna: kierowca nie przypisuje samodzielnie grupy pakowania na podstawie cech gazu.
- Źródło: Dz.U. 2025 poz. 642, ADR 2025, 2.1.1.3 i 3.2.1 tabela A — https://eli.gov.pl/api/acts/DU/2025/642/text.pdf.
- Nie oznaczono żadnego pytania jako `verified`.
