# Etap 4x315 — unikanie pyłu i pozostawanie po stronie nawietrznej

2026-11-02. Bazowy main `3617ff0c03fab9350c479d06486d14492d0e6d7b`; gałąź `stage4x315-windward-side-vapours`.

- Dodano ADR-B-0741 do `ADR-B-05-K04`: unikanie wdychania pyłu i wybór strony nawietrznej.
- Kompetencja wzrosła z 5 do 6 pytań; kompetencje teorii z mniej niż 6 pytaniami: **39** (3 praktyczne pominięte).
- Bank: 741 pytań (ADR-B-0001–0741), 741 `needs_review`, 0 `verified`; SHA `02fb3c3056749458ebcee9661ffa7895768b56e0`.
- Moduł ADR-B-05: 79 pytań.
- Rozkład kluczy A/B/C: 248/265/228.
- „Poprawna odpowiedź jest jedyną najdłuższą”: **81/741 = 10,93%**; maksimum działu **14,61%**. Długości opcji ADR-B-0741: A=128, B=118, C=84; poprawna C nie jest najdłuższa.
- Explanation: 408 znaków, 4 zdania. Wyjaśnia, że pył również może dostać się do dróg oddechowych, a strona nawietrzna to miejsce, z którego wiatr niesie zanieczyszczenie od kierowcy. Odrzuca pozostawanie po stronie zawietrznej i przechodzenie przez chmurę.
- Podstawa: ADR 2025, 5.4.3.4 — instrukcje pisemne nakazują unikać wdychania dymu, pyłu, oparów i par przez pozostawanie po stronie nawietrznej. Status `needs_review`; pełne literalne porównanie i niezależna recenzja pozostają otwarte.
- Odświeżono klucze i warianty 001–005, snapshoty sequential/legal 741, ledger, manifesty, kolejki prawne, rejestr specjalisty (741 unikalnych wierszy), coverage, lekcję B-05, README, instrukcje recenzji i testy liczebności.

## Pytanie ADR-B-0741

Po awarii z uszkodzonej przesyłki wydobywa się drobny pył. Wiatr niesie go w stronę kierowcy stojącego przy poboczu. Które działanie jest zgodne z instrukcjami pisemnymi ADR?

A. Pozostać po stronie zawietrznej w większej odległości, bo pył po rozproszeniu nie powinien już stanowić zagrożenia dla kierowcy.

B. Przejść przez chmurę pyłu na drugą stronę, a potem poczekać, aż opadnie, zanim kierowca wróci do pojazdu po dokumenty.

C. Odejść od pyłu i pozostać po stronie nawietrznej, tak by wiatr niósł go od kierowcy.

Pył z uszkodzonej przesyłki może dostać się do dróg oddechowych, dlatego kierowca powinien oddalić się i pozostać po stronie nawietrznej. Oznacza to miejsce, z którego wiatr wieje w stronę chmury, a nie takie, na które ją niesie. Nie zakładaj, że rozproszony pył jest bezpieczny, ani nie przechodź przez chmurę. Podstawa: ADR 2025, 5.4.3.4 — unikanie wdychania pyłu przez pozostawanie po stronie nawietrznej.

## Audyt A/B/C i źródła

- A — błędna: strona zawietrzna może znajdować się na drodze przemieszczania się pyłu; sam większy odstęp nie zastępuje ustawienia się po stronie nawietrznej.
- B — błędna: przejście przez chmurę naraża na wdychanie pyłu, a oczekiwanie aż opadnie nie jest instrukcją ADR.
- C — poprawna: instrukcje pisemne nakazują unikać wdychania pyłu przez pozostawanie po stronie nawietrznej.
- Źródło prawa: Dz.U. 2025 poz. 642, ADR 2025, 5.4.3.4 — https://eli.gov.pl/api/acts/DU/2025/642/text.pdf.
- Potwierdzenie tekstu ADR 2025 i wzoru instrukcji pisemnych: UNECE, ADR 2025 — https://unece.org/adr-2025-files; wersje językowe instrukcji — https://unece.org/transport/road-transport/linguistic-versions-adr-instructions-writing.
- Nie oznaczono żadnego pytania jako `verified`.
