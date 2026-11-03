# Etap 4x325 — nalepka zasłonięta przez wyposażenie opakowania

2026-11-03. Bazowy main `92c9b6515c80884fc741998be0312c22ebf5c1a9`; gałąź `stage4x325-package-danger-labels`.

- Dodano ADR-B-0751 do `ADR-B-06-K02`: rozmieszczenie nalepek ostrzegawczych i ochrona przed zasłonięciem.
- Kompetencja wzrosła z 5 do 6 pytań; kompetencje teorii z mniej niż 6 pytaniami: **29** (3 praktyczne pominięte).
- Bank: 751 pytań (ADR-B-0001–0751), 751 `needs_review`, 0 `verified`; SHA `fed909b6dec8fbaece0f391f4f2b78df55cb68f5`.
- Moduł ADR-B-06: 61 pytań.
- Rozkład kluczy A/B/C: 252/270/229.
- „Poprawna odpowiedź jest jedyną najdłuższą”: **81/751 = 10,79%**; maksimum działu **14,61%**. Długości opcji ADR-B-0751: A=108, B=123, C=127; poprawna B nie jest najdłuższa.
- Explanation: 354 znaki, 4 zdania. Wyjaśnia, że nalepka nie może być zasłonięta przez wyposażenie, a wymagane nalepki powinny być blisko siebie; dokument nie zastępuje oznakowania.
- Podstawa: ADR 2025, 5.2.2.1.6(b)–(c). Status `needs_review`; pełne literalne porównanie i niezależna recenzja pozostają otwarte.
- Odświeżono klucze i warianty egzaminów 001–005, snapshoty sequential/legal 751, ledger, manifesty, kolejki prawne, rejestr specjalisty, coverage, lekcję B-06, README i testy liczebności.

## Pytanie ADR-B-0751

Na opakowaniu są dwie wymagane nalepki ostrzegawcze. Pas mocujący przebiega przez jedną z nich i zasłania część symbolu. Co należy zrobić przed przewozem?

A. Można pozostawić pas w tym miejscu, jeśli większość nalepki pozostaje widoczna, a jej wzór da się rozpoznać.

B. Zmienić położenie pasa lub nalepki, aby wyposażenie nie zasłaniało żadnej nalepki; wymagane nalepki umieścić blisko siebie.

C. Pozostawić widoczną nalepkę główną, a informację o zasłoniętej nalepce dodatkowej przekazać wyłącznie w dokumencie przewozowym.

Nalepka ma być widoczna w całości, a nie tylko na tyle, by dało się odgadnąć jej wzór. Pas, uchwyt ani inna część wyposażenia opakowania nie mogą jej zasłaniać. Jeśli wymagane są dwie nalepki, umieść je blisko siebie, ale tak, by żadna nie zakrywała drugiej. Wpis w dokumencie nie zastępuje prawidłowego oznakowania. Podstawa: ADR 2025, 5.2.2.1.6(b)–(c).

## Audyt A/B/C i źródła

- A — błędna: ADR nie dopuszcza częściowego zasłonięcia nalepki; nie wystarcza, że większość symbolu jest widoczna.
- B — poprawna: wyposażenie nie może zasłaniać nalepki, a wymagane nalepki umieszcza się blisko siebie.
- C — błędna: dokument przewozowy nie zastępuje nalepki wymaganej na sztuce przesyłki.
- Źródło: ADR 2025, 5.2.2.1.6(b)–(c), Dz.U. 2025 poz. 642 — https://eli.gov.pl/api/acts/DU/2025/642. Tekst pomocniczy Ministerstwa Infrastruktury: https://www.gov.pl/attachment/b4638c72-30e3-4bff-afd1-1b9ba4100e70.
- Nie oznaczono żadnego pytania jako `verified`.
