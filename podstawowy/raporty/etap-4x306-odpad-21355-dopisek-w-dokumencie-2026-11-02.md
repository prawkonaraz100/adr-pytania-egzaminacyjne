# Etap 4x306 — odpad sklasyfikowany według 2.1.3.5.5: dopisek w dokumencie

2026-11-02. Bazowy main `117d12fff090960f72de5bb6e43a61c92dfe08d2`; gałąź `stage4x306-waste-transport-document`.

- Dodano ADR-B-0732 do `ADR-B-03-K02`: odpady niebezpieczne w dokumencie przewozowym.
- Kompetencja wzrosła z 5 do 6 pytań; kompetencje teorii z mniej niż 6 pytaniami: **48** (3 praktyczne pominięte).
- Bank: 732 pytania (ADR-B-0001–0732), 732 `needs_review`, 0 `verified`; SHA `2896a94357e8cd8b745602efc7f425960e89ca6a`.
- Moduł ADR-B-03: 57 pytań.
- Rozkład kluczy A/B/C: 244/263/225.
- „Poprawna odpowiedź jest jedyną najdłuższą”: **81/732 = 11,07%**; maksimum działu **14,61%**. Długości opcji ADR-B-0732: A=115, B=115, C=88; poprawna B nie jest jedyną najdłuższą.
- Explanation: 355 znaków, 4 zdania. A pomija szczególny dopisek wymagany przy klasyfikacji według 2.1.3.5.5; B podaje wymagane sformułowanie; C błędnie zastępuje wymóg ADR kodem odpadu.
- Podstawa: ADR 2025, 5.4.1.1.3.1 i 2.1.3.5.5. Status `needs_review`; pełne literalne porównanie i niezależna recenzja pozostają otwarte.
- Odświeżono klucze i warianty 001–005, snapshoty sequential/legal 732, ledger, pakiety, kolejki, rejestr specjalisty, coverage, lekcję B-03, README i testy regresji.

## Pytanie ADR-B-0732

Zakład wysyła odpad, którego klasyfikację przeprowadzono zgodnie z ADR 2.1.3.5.5. W dokumencie wpisano już numer UN, prawidłową nazwę przewozową, klasę, grupę pakowania i kod tunelowy. Jakiego dodatkowego zapisu wymaga ADR?

A. Wystarczy poprzedzić nazwę przewozową słowem „ODPAD”; nie trzeba wskazywać zastosowanej metody klasyfikacji odpadu.

B. Dodać do opisu towaru zapis „ODPAD ZGODNY Z 2.1.3.5.5”, ponieważ zastosowano szczególną metodę klasyfikacji odpadu.

C. Dodać wyłącznie kod odpadu z katalogu odpadów, a wymagany opis ADR pozostawić bez zmian.

Jeżeli klasyfikację odpadu przeprowadzono na podstawie 2.1.3.5.5, samo zwykłe poprzedzenie nazwy słowem „ODPAD” nie wystarcza. W opisie wymaganym przez ADR trzeba dodać dokładny zapis „ODPAD ZGODNY Z 2.1.3.5.5”. Odpowiedź A pomija ten szczególny dopisek, a C myli kod z katalogu odpadów z wymaganym opisem ADR. Podstawa: ADR 2025, 5.4.1.1.3.1 i 2.1.3.5.5.

## Audyt A/B/C i źródła

- A — błędna: opisuje tylko ogólną regułę poprzedzenia nazwy słowem „ODPAD”, nie wymóg szczególny przy 2.1.3.5.5.
- B — poprawna: ADR wymaga dodania wyrazów „ODPAD ZGODNY Z 2.1.3.5.5”.
- C — błędna: kod z katalogu odpadów nie zastępuje wymaganego dopisku w dokumencie ADR.
- Źródło: Dz.U. 2025 poz. 642, ADR 2025, 5.4.1.1.3.1 i 2.1.3.5.5 — https://eli.gov.pl/api/acts/DU/2025/642/text.pdf. Tekst pomocniczy MI: https://www.gov.pl/attachment/b7292c03-ac9d-4f80-9a29-c22f53d847b8.
- Nie oznaczono żadnego pytania jako `verified`.
