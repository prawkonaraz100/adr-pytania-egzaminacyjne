# Etap 4x329 — odblaskowość tablicy pomarańczowej

Data: 03.11.2026. Gałąź: `stage4x329-orange-plate-colour-construction`. Bazowy main: `e5c4e6eac536fbbfdbf4035187664631f97d15f8`.

## Zakres i wynik

Dodano ADR-B-0755 do kompetencji `ADR-B-06-K07` — kolor i budowa tablicy. Pytanie sprawdza, czy kierowca rozumie wymóg odblaskowości tablicy na pojeździe drogowym i nie przenosi wyjątku dotyczącego wagonów na samochód. Podstawa: ADR 2025, 5.3.2.2.1.

- Bank: **755** pytań (ADR-B-0001–0755), 755 `needs_review`, 0 `verified`.
- SHA `9b6cf3e78af2fd49a2fcbe99b1fb10a8021904e1`.
- Moduł ADR-B-06: **65** pytań; K07: 5→6.
- Kompetencje teorii z mniej niż 6 pytaniami: **25** (3 praktyczne pominięte).
- Rozkład kluczy A/B/C: **253/273/229**.
- „Poprawna odpowiedź jest jedyną najdłuższą”: **81/755 = 10,73%**; maksimum działu **14,61%**.
- Długości opcji A/B/C: **120/102/98**; poprawna B nie jest najdłuższa.
- Explanation: **367 znaków, 4 zdania**.

## Pytanie ADR-B-0755

Przed wyjazdem zauważasz, że pomarańczowa tablica na samochodzie jest matowa i nie odbija światła reflektorów. Pozostałe wymiary i oznaczenia są prawidłowe. Co wynika z ADR?

A. Sam pomarańczowy kolor wystarcza; odblaskowość jest tylko zaleceniem, a nie warunkiem dla tablic na pojazdach drogowych.

B. Tablica na samochodzie musi być odblaskowa; wyjątek dopuszczający nieodblaskowy kolor dotyczy wagonów.

C. Wystarczy, że numery są czytelne w dzień; odblaskowość jest wymagana wyłącznie podczas jazdy nocą.

Na pojeździe drogowym tablica pomarańczowa musi być odblaskowa, żeby była lepiej widoczna przy słabym oświetleniu. Matowa tablica bez właściwości odblaskowych nie spełnia tego warunku, nawet jeśli ma właściwy kolor i czytelne numery. Odpowiedzi A i C pomijają obowiązek odblaskowości; wyjątek dla nieodblaskowego koloru dotyczy wagonów. Podstawa: ADR 2025, 5.3.2.2.1.

## Audyt A/B/C i źródła

- A — błędna: pomarańczowa barwa nie zastępuje wymogu odblaskowości.
- B — poprawna: tablice na pojazdach drogowych mają być odblaskowe; wyjątek dotyczy wagonów.
- C — błędna: obowiązek nie jest ograniczony do jazdy nocą ani do samej czytelności cyfr.
- Podstawa prawna: Dz.U. 2025 poz. 642, ADR 2025, 5.3.2.2.1 — https://eli.gov.pl/api/acts/DU/2025/642/text.pdf.
- Dodatkowe porównanie ADR 2025, 5.3.2.2.1 — https://digitallibrary.un.org/record/4092124/files/E_ECE_TRANS_351-EN.pdf.
- Pytanie pozostaje `needs_review`; pełne literalne porównanie polskiego tekstu i niezależna recenzja specjalisty są nadal wymagane. Nie oznaczono żadnego pytania jako `verified`.

## Synchronizacja artefaktów

Klucze i warianty egzaminów próbnych 001–005 wskazują SHA bieżącego banku. Snapshoty `review/sequential/755-755.json` i `review/legal-clauses/755-755.json` zawierają ADR-B-0755. Ledger prawny, manifesty pakietu i kolejki specjalisty mają zaktualizowane SHA oraz stan 755 pytań. Zaktualizowano coverage, README kursanta i specjalisty, lekcję B-06, rejestr specjalisty oraz testy liczebności.
