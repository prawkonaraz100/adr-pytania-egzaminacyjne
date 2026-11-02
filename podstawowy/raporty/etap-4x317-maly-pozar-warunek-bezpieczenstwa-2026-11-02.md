# Etap 4x317 — mały pożar i warunek bezpieczeństwa

2026-11-02. Bazowy main `c4c944d4ae7375d98da192cc164d2b5dcb5b2263`; gałąź `stage4x317-small-fire-smoke-safety`.

- Dodano ADR-B-0743 do `ADR-B-05-K06`: warunek bezpiecznego użycia gaśnicy przy małym pożarze komory silnika.
- Kompetencja wzrosła z 5 do 6 pytań; kompetencje teorii z mniej niż 6 pytaniami: **37** (3 praktyczne pominięte).
- Bank: 743 pytania (ADR-B-0001–0743), 743 `needs_review`, 0 `verified`; SHA `1834185447c88b46f712cba439b615f5a7e210a9`.
- Moduł ADR-B-05: 81 pytań.
- Rozkład kluczy A/B/C: 248/267/228.
- „Poprawna odpowiedź jest jedyną najdłuższą”: **81/743 = 10,90%**; maksimum działu **14,61%**. Długości opcji ADR-B-0743: A=100, B=68, C=93; poprawna B jest najkrótsza.
- Explanation: 329 znaków, 4 zdania. Wyjaśnia, że mały pożar silnika można gasić tylko wtedy, gdy jest to właściwe i bezpieczne; wejście w gęsty dym wyklucza bezpieczną próbę gaszenia.
- Podstawa: ADR 2025, 5.4.3.4 — użycie gaśnic do małych/początkowych pożarów opon, hamulców i komory silnika wyłącznie, gdy jest to właściwe i bezpieczne; unikanie wdychania dymu przez pozostawanie po stronie nawietrznej. Status `needs_review`; pełne literalne porównanie i niezależna recenzja pozostają otwarte.
- Odświeżono klucze i warianty 001–005, snapshoty sequential/legal 743, ledger, manifesty, kolejki prawne, rejestr specjalisty (743 unikalne ID), coverage, lekcję B-05, README, instrukcje recenzji i testy liczebności.

## Pytanie ADR-B-0743

Na postoju kierowca zauważa mały pożar w komorze silnika. Aby dosięgnąć gaśnicy i podejść do ognia, musiałby wejść w gęsty dym. Co powinien zrobić?

A. Spróbować gasić, bo pożar jest jeszcze mały, a warunek bezpieczeństwa dotyczy tylko ognia w ładowni.

B. Nie narażać się na dym; oddalić się, ostrzec innych i wezwać służby.

C. Otworzyć szeroko komorę silnika, aby szybciej zlokalizować płomienie i skrócić czas gaszenia.

Mały pożar silnika można gasić gaśnicą tylko wtedy, gdy jest to właściwe i bezpieczne. Jeżeli dojście wymaga wejścia w gęsty dym, warunek bezpieczeństwa nie jest spełniony: nie podejmuj próby, oddal się, ostrzeż innych i wezwij służby. Nie ryzykuj wdychania dymu ani nie otwieraj komory bez potrzeby. Podstawa: ADR 2025, 5.4.3.4.

## Audyt A/B/C i źródła

- A — błędna: warunek bezpieczeństwa dotyczy każdej próby użycia gaśnicy, nie tylko pożaru ładowni.
- B — poprawna: instrukcje dopuszczają gaszenie małego/początkowego pożaru komory silnika wyłącznie, gdy jest to właściwe i bezpieczne; wejście w gęsty dym nie spełnia tego warunku.
- C — błędna: otwarcie komory nie usuwa zagrożenia dymem i może narazić kierowcę na dodatkowe niebezpieczeństwo.
- Źródło prawa: Dz.U. 2025 poz. 642, ADR 2025, 5.4.3.4 — https://eli.gov.pl/api/acts/DU/2025/642/text.pdf.
- Nie oznaczono żadnego pytania jako `verified`.
