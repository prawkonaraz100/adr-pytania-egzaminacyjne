# Etap 4m — wyrównanie długości odpowiedzi ADR-B-0166–0180

24.10.2026. Punkt wyjścia sprawdzono na świeżym `main` po PR #220, commit `7751edf66379e2bd2b8e1b482614b3422a3901f5`. Wyrównano warianty w 14 pytaniach: ADR-B-0166 i 0168–0180. Klucze odpowiedzi zachowano.

- Nie zmieniano wyjaśnień, źródeł, podstaw prawnych ani `verification_status=needs_review`.
- Migawki audytowe w `review/sequential/151-180.json` i `review/legal-clauses/151-180.json` odświeżono.
- W partii poprawna odpowiedź nie jest najdłuższa w **15/15** pytań. Rozpiętość długości wariantów to 1–16 znaków.
- Wskaźnik globalny „poprawna odpowiedź jest najdłuższa” spadł z **291/545 (53,4%)** do **280/545 (51,4%)**. Cel globalny ≤40% nadal nie został osiągnięty.
- Żadne pytanie nie zostało oznaczone jako `verified`; wszystkie 545 pozostają `needs_review`.

Wyłącznie kurs podstawowy ADR; niezależna recenzja prawna pozostaje wymagana.
