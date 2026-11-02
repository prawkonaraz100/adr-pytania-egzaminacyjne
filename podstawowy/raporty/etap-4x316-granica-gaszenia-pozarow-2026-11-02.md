# Etap 4x316 — granica gaszenia pożaru komory silnika i ładowni

2026-11-02. Bazowy main `7dc12e62e40ea0a7a2b816866bc0abab46e72334`; gałąź `stage4x316-cargo-fire-boundary`.

- Dodano ADR-B-0742 do `ADR-B-05-K05`: granica między małym/początkowym pożarem komory silnika a pożarem przedziału ładunkowego.
- Kompetencja wzrosła z 5 do 6 pytań; kompetencje teorii z mniej niż 6 pytaniami: **38** (3 praktyczne pominięte).
- Bank: 742 pytania (ADR-B-0001–0742), 742 `needs_review`, 0 `verified`; SHA `23499db89b3fcf011fac9ff33ca4319841281a0d`.
- Moduł ADR-B-05: 80 pytań.
- Rozkład kluczy A/B/C: 248/266/228.
- „Poprawna odpowiedź jest jedyną najdłuższą”: **81/742 = 10,92%**; maksimum działu **14,61%**. Długości opcji ADR-B-0742: A=89, B=62, C=79; poprawna B jest najkrótsza.
- Explanation: 359 znaków, 4 zdania. Wyjaśnia, że możliwość użycia gaśnicy przy małym pożarze komory silnika nie oznacza zgody na gaszenie przedziału ładunkowego; pożaru ładowni załoga nie powinna gasić.
- Podstawa: ADR 2025, 5.4.3.4 — małe/początkowe pożary opon, hamulców i komory silnika można gasić, jeżeli jest to właściwe i bezpieczne; pożarów przedziałów ładunkowych członkowie załogi nie powinni gasić. Status `needs_review`; pełne literalne porównanie i niezależna recenzja pozostają otwarte.
- Odświeżono klucze i warianty 001–005, snapshoty sequential/legal 742, ledger, manifesty, kolejki prawne, rejestr specjalisty (742 unikalne ID), coverage, lekcję B-05, README, instrukcje recenzji i testy liczebności.

## Pytanie ADR-B-0742

Podczas awarii mały pożar w komorze silnika rozprzestrzenia się na przedział ładunkowy z towarami niebezpiecznymi. Co powinien zrobić członek załogi?

A. Kontynuować gaszenie, bo pożar rozpoczął się w komorze silnika, a gaśnica była już użyta.

B. Przerwać gaszenie pożaru ładowni, oddalić się i wezwać służby.

C. Otworzyć przedział ładunkowy, aby sprawdzić, czy ogień nie zajął już przesyłek.

Mały pożar komory silnika można próbować gasić tylko wtedy, gdy jest to właściwe i bezpieczne. Gdy ogień obejmie przedział ładunkowy, ten wyjątek już nie obowiązuje: załoga nie powinna podejmować gaszenia, nawet jeśli ogień nadal wygląda na niewielki. Otwieranie ładowni może dodatkowo narazić ludzi na dym i substancje z ładunku. Podstawa: ADR 2025, 5.4.3.4.

## Audyt A/B/C i źródła

- A — błędna: warunkowe dopuszczenie gaszenia małego pożaru komory silnika nie rozciąga się na przedział ładunkowy.
- B — poprawna: instrukcje pisemne wskazują, że członkowie załogi nie powinni podejmować gaszenia pożarów w przedziałach ładunkowych.
- C — błędna: otwarcie ładowni może narazić załogę na ogień, dym i towary niebezpieczne; nie jest działaniem przewidzianym w instrukcji.
- Źródło prawa: Dz.U. 2025 poz. 642, ADR 2025, 5.4.3.4 — https://eli.gov.pl/api/acts/DU/2025/642/text.pdf.
- Tekst ADR 2025 i instrukcje pisemne: UNECE — https://unece.org/adr-2025-files.
- Nie oznaczono żadnego pytania jako `verified`.
