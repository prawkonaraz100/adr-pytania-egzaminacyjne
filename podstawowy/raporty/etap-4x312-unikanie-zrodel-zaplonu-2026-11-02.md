# Etap 4x312 — unikanie źródeł zapłonu przy awarii

2026-11-02. Bazowy main `043f577d28cb5b3286d677d743bea074b11491de`; gałąź `stage4x312-ignition-sources-emergency`.

- Dodano ADR-B-0738 do `ADR-B-04-K04`: unikanie źródeł zapłonu przy awarii.
- Kompetencja wzrosła z 5 do 6 pytań; kompetencje teorii z mniej niż 6 pytaniami: **42** (3 praktyczne pominięte).
- Bank: 738 pytań (ADR-B-0001–0738), 738 `needs_review`, 0 `verified`; SHA `c11732a07bf6b418107b2bf6010a184f3cf112df`.
- Moduł ADR-B-04: 50 pytań.
- Rozkład kluczy A/B/C: 248/264/226.
- „Poprawna odpowiedź jest jedyną najdłuższą”: **81/738 = 10,98%**; maksimum działu **14,61%**. Długości opcji ADR-B-0738: A=95, B=106, C=102; poprawna C nie jest najdłuższa.
- Explanation: 371 znaków, 4 zdania. Najpierw wyjaśnia ryzyko iskry przy włączaniu urządzenia; następnie obala pomysły użycia lampy i wentylatora; kończy podstawą ADR.
- Podstawa: ADR 2025, 5.4.3.4 — instrukcje pisemne, unikanie źródeł zapłonu. Status `needs_review`; pełne literalne porównanie i niezależna recenzja pozostają otwarte.
- Odświeżono klucze i warianty 001–005, snapshoty sequential/legal 738, ledger, pakiety, kolejki prawne, rejestr specjalisty, coverage, lekcję B-04, README i testy liczebności.

## Pytanie ADR-B-0738

Po awarii cysterny kierowca czuje zapach palnych oparów. W kabinie jest ciemno i chce włączyć lampę roboczą, aby obejrzeć miejsce wycieku. Co powinien zrobić zgodnie z instrukcjami pisemnymi ADR?

A. Włączyć lampę na chwilę, aby obejrzeć wyciek, a potem wyłączyć ją przed podejściem do cysterny.

B. Uruchomić wentylator kabiny i oświetlenie, bo brak widocznego płomienia oznacza, że nie ma źródła zapłonu.

C. Nie włączać urządzeń elektrycznych ani nie palić; oddalić się i postępować zgodnie z instrukcjami ADR.

Przy możliwych palnych oparach nawet krótkie włączenie lampy może wywołać iskrę, dlatego kierowca nie powinien uruchamiać urządzeń elektrycznych. Lampa robocza i wentylator nie są bezpiecznym sposobem sprawdzenia sytuacji, nawet gdy nie widać płomienia. Należy unikać źródeł zapłonu, oddalić się i postępować zgodnie z instrukcjami pisemnymi. Podstawa: ADR 2025, 5.4.3.4.

## Audyt A/B/C i źródła

- A — błędna: włączenie lampy roboczej jest użyciem urządzenia elektrycznego w sytuacji, w której instrukcje nakazują unikać źródeł zapłonu.
- B — błędna: uruchomienie wentylatora i oświetlenia oznacza włączenie urządzeń elektrycznych; brak widocznego płomienia nie usuwa ryzyka.
- C — poprawna: instrukcje pisemne nakazują unikać źródeł zapłonu, w tym nie włączać urządzeń elektrycznych, oddalić się od zagrożenia i stosować do instrukcji.
- Źródło: Dz.U. 2025 poz. 642, ADR 2025, 5.4.3.4 — https://eli.gov.pl/api/acts/DU/2025/642/text.pdf.
- Nie oznaczono żadnego pytania jako `verified`.
