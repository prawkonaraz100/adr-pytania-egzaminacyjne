# Etap 4x321 — kamizelka ostrzegawcza i znaki ostrzegawcze

2026-11-03. Bazowy main `9779770c671f3681d1774685ece25f3aacafe8a2`; gałąź `stage4x321-high-visibility-vest-warning-signs`.

- Dodano ADR-B-0747 do `ADR-B-05-K10`: wyposażenie jednostki transportowej w dwa stojące znaki ostrzegawcze oraz kamizelkę dla każdego członka załogi.
- Kompetencja wzrosła z 5 do 6 pytań; kompetencje teorii z mniej niż 6 pytaniami: **33** (3 praktyczne pominięte).
- Bank: 747 pytań (ADR-B-0001–0747), 747 `needs_review`, 0 `verified`; SHA `b287b7df4227de90a2d33199a005dde465c69c8a`.
- Moduł ADR-B-05: 85 pytań.
- Rozkład kluczy A/B/C: 251/268/228.
- „Poprawna odpowiedź jest jedyną najdłuższą”: **81/747 = 10,84%**; maksimum działu **14,61%**. Długości opcji ADR-B-0747: A=100, B=101, C=91; poprawna A nie jest najdłuższa.
- Explanation: 328 znaków, 4 zdania. Wyjaśnia różnicę między wyposażeniem jednostki (dwa znaki) a wyposażeniem indywidualnym (kamizelka dla każdego członka załogi). B zmniejsza liczbę wymaganych znaków, C pomija kamizelkę dla drugiej osoby.
- Podstawa: ADR 2025, 8.1.5.2. Status `needs_review`; pełne literalne porównanie i niezależna recenzja pozostają otwarte.
- Odświeżono klucze i warianty 001–005, snapshoty sequential/legal 747, ledger, manifesty, kolejki, rejestr specjalisty (747 unikalnych ID), coverage, lekcję B-05, README i testy regresji.

## Pytanie ADR-B-0747

Przed wyjazdem na przewóz ADR kierowca sprawdza wyposażenie jednostki transportowej, w której jadą dwie osoby. Który zestaw dotyczący znaków ostrzegawczych i kamizelek jest wymagany?

A. Dwa stojące znaki ostrzegawcze dla jednostki oraz kamizelka ostrzegawcza dla każdego członka załogi.

B. Jeden stojący znak ostrzegawczy dla jednostki oraz kamizelka ostrzegawcza dla każdego członka załogi.

C. Dwa stojące znaki ostrzegawcze dla jednostki oraz jedna wspólna kamizelka dla całej załogi.

Jednostka transportowa ma mieć dwa stojące znaki ostrzegawcze, a kamizelkę ostrzegawczą trzeba zapewnić każdemu członkowi załogi. Przy dwóch osobach oznacza to dwa znaki i dwie kamizelki, nie jeden wspólny zestaw. Odpowiedź B zmniejsza wymaganą liczbę znaków, a C pomija kamizelkę dla drugiej osoby. Podstawa: ADR 2025, 8.1.5.2.

## Audyt A/B/C i źródła

- A — poprawna: ADR wymaga dwóch stojących znaków ostrzegawczych dla jednostki transportowej i kamizelki ostrzegawczej dla każdego członka załogi.
- B — błędna: liczba znaków jest zaniżona; wymagane są dwa.
- C — błędna: kamizelka jest wymagana dla każdego członka załogi, a nie jedna wspólna.
- Źródło: Dz.U. 2025 poz. 642, ADR 2025, 8.1.5.2 — https://eli.gov.pl/api/acts/DU/2025/642/text.pdf.
- Nie oznaczono żadnego pytania jako `verified`.
