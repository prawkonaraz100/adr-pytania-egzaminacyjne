# ADR podstawowy — partia 0399–0416: ochrona przewozu (ADR-B-12)

Data: 2026-10-23. Po odczycie main na 398 rekordów przygotowano 18 NOWYCH pytań o ochronie towarów niebezpiecznych, bez ingerencji w poprzednie rekordy. Zakres: 1.10.2.4, 1.10.3.2.2(a–h), uwaga po 1.10.3.2.2 oraz 1.10.3.3.

- 18 indywidualnych pytań, 54 warianty odpowiedzi; JSONL ADR-B-0399–0416.
- Uzasadnienia A/B/C i zachowane migawki: `review/legal-clauses/399-416.json`.
- Kontrola sekwencyjna: `review/sequential/399-416.json`.
- `verification_status=needs_review` dla każdej pozycji; 0 nowych `verified`.
- Kontrola treści przepisów na podstawie wydania ADR 2025 udostępnionego pomocniczo; link do aktu ogłoszonego: https://dziennikustaw.gov.pl/DU/2025/642 oraz sprostowanie https://eli.gov.pl/eli/DU/2025/1575/ogl.
- Źródło pomocnicze: https://www.gov.pl/web/infrastruktura/towary-niebezpieczne. **Nie poświadczono pełnego dosłownego porównania każdego wariantu z wszystkimi częściami urzędowego polskiego tekstu; nie ma podpisu eksperta.**
- Żadne z pytań nie zostało dopuszczone do eksportu produkcyjnego.

**Quality Gate:** oczekuje na wynik CI dla PR. Nie scalać bez potwierdzonego PASS wszystkich wymaganych kroków. Kolejne planowane pogłębienie: trudne wyjątki w pozostałych działach podstawowego ADR; cysterny poza zakresem.
