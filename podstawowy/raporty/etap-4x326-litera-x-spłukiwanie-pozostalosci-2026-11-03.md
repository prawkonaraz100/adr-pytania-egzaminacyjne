# Etap 4x326 — litera X: reakcja z wodą i spłukiwanie pozostałości

2026-11-03. Bazowy main `cdeda8ac384515464f096b819e60bcc108a13ac5`; gałąź `stage4x326-x-before-hazard-number`.

- Dodano ADR-B-0752 do `ADR-B-06-K04`: zastosowanie ostrzeżenia X przy próbie spłukiwania pozostałości po wycieku.
- Kompetencja wzrosła z 5 do 6 pytań; kompetencje teorii z mniej niż 6 pytaniami: **28** (3 praktyczne pominięte).
- Bank: 752 pytania (ADR-B-0001–0752), 752 `needs_review`, 0 `verified`; SHA `3ddd949081089a48396e9a2e257a57fa5eb7aea4`.
- Moduł ADR-B-06: 62 pytania.
- Rozkład kluczy A/B/C: 253/270/229.
- „Poprawna odpowiedź jest jedyną najdłuższą”: **81/752 = 10,77%**; maksimum działu **14,61%**. Długości opcji ADR-B-0752: A=115, B=114, C=128; poprawna A nie jest najdłuższa.
- Explanation: 398 znaków, 4 zdania. Wyjaśnia, że ostrzeżenie X obejmuje także spłukiwanie i mycie pozostałości; woda wymaga zgody specjalistów.
- Podstawa: ADR 2025, 5.3.2.3.1. Status `needs_review`; pełne literalne porównanie i niezależna recenzja pozostają otwarte.
- Odświeżono klucze i warianty egzaminów 001–005, snapshoty sequential/legal 752, ledger, manifesty, kolejki prawne, rejestr specjalisty, coverage, lekcję B-06, README i testy liczebności.

## Pytanie ADR-B-0752

Po awarii niewielka ilość materiału wyciekła na podłogę skrzyni. Na tablicy pomarańczowej numer rozpoznawczy poprzedza litera X. Pracownik proponuje spłukać pozostałość wodą. Co kierowca powinien przekazać i zrobić?

A. Wstrzymać spłukiwanie i przekazać, że X oznacza niebezpieczną reakcję z wodą; jej użycie wymaga zgody specjalistów.

B. Można spłukać mały ślad, bo ostrzeżenie X dotyczy tylko gaszenia pożaru i nie obejmuje zwykłego mycia powierzchni.

C. Wystarczy rozcieńczyć pozostałość wodą z detergentem, jeżeli pracownik ma rękawice; zgoda specjalistów nie jest wtedy potrzebna.

Litera X przed numerem rozpoznawczym ostrzega, że materiał może niebezpiecznie reagować z wodą. Dlatego nie wolno samodzielnie spłukiwać nawet niewielkiej pozostałości ani zakładać, że mycie jest bezpieczniejsze niż gaszenie. Woda może być użyta tylko za zgodą specjalistów; pozostałe odpowiedzi błędnie ograniczają ostrzeżenie do pożaru albo pomijają wymaganą zgodę. Podstawa: ADR 2025, 5.3.2.3.1.

## Audyt A/B/C i źródła

- A — poprawna: X oznacza niebezpieczną reakcję z wodą, a jej użycie wymaga zgody specjalistów.
- B — błędna: ograniczenie nie dotyczy wyłącznie gaszenia pożaru; obejmuje także mycie i spłukiwanie.
- C — błędna: detergent i rękawice nie zastępują zgody specjalistów.
- Źródło: ADR 2025, 5.3.2.3.1, Dz.U. 2025 poz. 642 — https://eli.gov.pl/api/acts/DU/2025/642. Tekst pomocniczy Ministerstwa Infrastruktury: https://www.gov.pl/attachment/b4638c72-30e3-4bff-afd1-1b9ba4100e70.
- Nie oznaczono żadnego pytania jako `verified`.
