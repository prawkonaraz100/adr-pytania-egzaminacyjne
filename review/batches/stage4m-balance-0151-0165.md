# Etap 4m — wyrównanie długości odpowiedzi ADR-B-0151–0165

24.10.2026. Punkt wyjścia sprawdzono na świeżym `main` = `889e6584e74cf9f3efb3660e24db29d115012555`, po PR #216. Wyrównano warianty odpowiedzi w 9 pytaniach: ADR-B-0153–0155, 0157, 0159–0163, 0165, a także dopracowano długości opcji w 0151 i 0164 (łącznie 11 rekordów). Klucze odpowiedzi pozostały bez zmian.

- Nie zmieniano wyjaśnień, źródeł, podstaw prawnych ani `verification_status=needs_review`.
- Zaktualizowano migawki audytowe: `review/sequential/151-180.json` oraz `review/legal-clauses/151-180.json`.
- W tej partii poprawna odpowiedź nie jest najdłuższa w **15/15** pytaniach; rozpiętość długości wariantów wynosi 4–14 znaków.
- Wskaźnik globalny „poprawna odpowiedź jest najdłuższa” spadł z **300/545 (55,0%)** do **291/545 (53,4%)**. Cel globalny ≤40% pozostaje otwarty.
- Kontrole jakości nie zostały wyłączone. Wszystkie 545 pytań nadal mają status `needs_review`; żadnego nie oznaczono jako `verified`.

Wyłącznie kurs podstawowy ADR; niezależna recenzja prawna pozostaje wymagana.
