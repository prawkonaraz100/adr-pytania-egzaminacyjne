# Etap 4x308 — klasa 9: wyposażenie ochrony kanalizacji

2026-11-02. Bazowy main `ea4b4010affe38863bb7e21562d769d75d388ee6`; gałąź `stage4x308-class9-drain-protection-equipment`.

- Dodano ADR-B-0734 do `ADR-B-03-K04`: ochrona kanalizacji i wód podczas wypadku.
- Kompetencja wzrosła z 5 do 6 pytań; kompetencje teorii z mniej niż 6 pytaniami: **46** (3 praktyczne pominięte).
- Bank: 734 pytania (ADR-B-0001–0734), 734 `needs_review`, 0 `verified`; SHA `27ff86cdb1ea2d4df14008965f54d9d0b8b435ee`.
- Moduł ADR-B-03: 59 pytań.
- Rozkład kluczy A/B/C: 245/264/225.
- „Poprawna odpowiedź jest jedyną najdłuższą”: **81/734 = 11,04%**; maksimum działu **14,61%**. Długości opcji ADR-B-0734: A=106, B=83, C=151; poprawna A nie jest najdłuższa.
- Explanation: 316 znaków, 4 zdania. ADR 8.1.5.2 obejmuje towary z nalepką 9 i wymaga łopaty, osłony kanalizacyjnej oraz pojemnika do zebrania pozostałości.
- Podstawa: ADR 2025, 8.1.5.2. Status `needs_review`; pełne literalne porównanie i niezależna recenzja pozostają otwarte.
- Odświeżono klucze i warianty 001–005, snapshoty sequential/legal 734, ledger, pakiety, kolejki, rejestr specjalisty, coverage, lekcję B-03, README i testy regresji.

## Pytanie ADR-B-0734

Jednostka przewozi UN 3082, materiał zagrażający środowisku, ciekły I.N.O., oznakowany nalepką 9. Kierowca sprawdza wyposażenie dodatkowe przed wyjazdem. Który zestaw musi znajdować się w pojeździe?

A. Łopata, osłona kanalizacyjna i pojemnik do zebrania pozostałości; wymóg obejmuje także towary z nalepką 9.

B. Tylko osłona kanalizacyjna; łopata i pojemnik są wymagane wyłącznie przy nalepce 8.

C. Wyposażenie dodatkowe nie jest wymagane przy klasie 9, ponieważ zagrożenie środowiska oznacza wyłącznie obowiązek odpowiedniego oznakowania opakowania.

Przepis 8.1.5.2 obejmuje towary z nalepką 9 tak samo jak wskazane tam klasy i wymaga łopaty, osłony kanalizacyjnej oraz pojemnika do zebrania pozostałości. Nie jest to wyposażenie zarezerwowane wyłącznie dla klasy 8. Odpowiedź B pomija dwa wymagane elementy, a C błędnie wyłącza klasę 9. Podstawa: ADR 2025, 8.1.5.2.

## Audyt A/B/C i źródła

- A — poprawna: nalepka 9 znajduje się w wykazie 8.1.5.2; wymagany zestaw obejmuje łopatę, osłonę kanalizacyjną i pojemnik.
- B — błędna: pomija łopatę i pojemnik.
- C — błędna: klasa 9 jest wprost objęta wymogiem.
- Źródło: Dz.U. 2025 poz. 642, ADR 2025, 8.1.5.2 — https://eli.gov.pl/api/acts/DU/2025/642/text.pdf.
- Nie oznaczono żadnego pytania jako `verified`.
