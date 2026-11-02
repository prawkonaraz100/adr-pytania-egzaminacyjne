# Etap 4x311 — zakaz otwierania sztuki przesyłki mimo zgody odbiorcy

2026-11-02. Bazowy main `a7ffda35ab35a4cb74ceb5aa18c563218fcd568e`; gałąź `stage4x311-package-opening-consignee-request`.

- Dodano ADR-B-0737 do `ADR-B-04-K02`: pisemna zgoda odbiorcy nie uchyla zakazu otwierania sztuki przesyłki przez kierowcę lub pomocnika.
- Kompetencja wzrosła z 5 do 6 pytań; kompetencje teorii z mniej niż 6 pytaniami: **43** (3 praktyczne pominięte).
- Bank: 737 pytań (ADR-B-0001–0737), 737 `needs_review`, 0 `verified`; SHA `fd06cfd4d0d67d5285afa71981e1b2e448d71143`.
- Moduł ADR-B-04: 50 pytań.
- Rozkład kluczy A/B/C: 248/264/225.
- „Poprawna odpowiedź jest jedyną najdłuższą”: **81/737 = 10,99%**; maksimum działu **14,61%**. Długości opcji ADR-B-0737: A=95, B=120, C=104; poprawna A nie jest najdłuższa.
- Explanation: 370 znaków, 4 zdania. A wyjaśnia, że zgoda odbiorcy nie tworzy wyjątku; B błędnie uznaje, że odbiorca może uchylić zakaz; C błędnie próbuje przenieść czynność na pomocnika.
- Podstawa: ADR 2025, 8.3.3. Status `needs_review`; pełne literalne porównanie i niezależna recenzja pozostają otwarte.
- Odświeżono klucze i warianty 001–005, snapshoty sequential/legal 737, ledger, manifesty, kolejki prawne, rejestr specjalisty, coverage, lekcję B-04, README i testy regresji.

## Pytanie ADR-B-0737

Po przyjeździe do odbiorcy magazynier prosi kierowcę o otwarcie sztuki przesyłki ADR, by porównać zawartość z zamówieniem. Odbiorca pisemnie zgadza się na otwarcie. Co może zrobić kierowca?

A. Odmówić otwarcia; zgoda odbiorcy nie znosi zakazu z ADR 8.3.3 dotyczącego kierowcy i pomocnika.

B. Otworzyć opakowanie w obecności magazyniera, bo odbiorca przejmuje odpowiedzialność za przesyłkę po przyjeździe pojazdu.

C. Poprosić pomocnika o otwarcie, ponieważ zakaz dotyczy tylko kierowcy, który samodzielnie otwiera paczkę.

ADR 8.3.3 zabrania kierowcy i pomocnikowi otwierania sztuk przesyłek zawierających towary niebezpieczne. Zgoda odbiorcy ani jego obecność nie tworzą wyjątku od tego zakazu. Kierowca nie może też przerzucić tej czynności na pomocnika; w razie wątpliwości dotyczących zawartości powinien wyjaśnić je z nadawcą lub odbiorcą bez otwierania paczki. Podstawa: ADR 2025, 8.3.3.

## Audyt A/B/C i źródła

- A — poprawna: ADR 8.3.3 obejmuje kierowcę i pomocnika; zgoda odbiorcy nie uchyla zakazu.
- B — błędna: odbiorca nie może udzielić wyjątku od wymogu ADR.
- C — błędna: pomocnik kierowcy również nie może otwierać sztuk przesyłek z towarami niebezpiecznymi.
- Źródło: Dz.U. 2025 poz. 642, ADR 2025, 8.3.3 — https://dziennikustaw.gov.pl/DU/2025/642; tekst ADR 2025, tom II, ECE/TRANS/352 — https://unece.org/adr-2025-files.
- Nie oznaczono żadnego pytania jako `verified`.
