# Egzamin próbny ADR podstawowy — materiały robocze

- [Wariant 001 — arkusz pytań](wariant-001.json)
- [Wariant 001 — klucz i wyjaśnienia](klucz-001.json)

**Wyłącznie trening wewnętrzny.** Bank źródłowy ma 566 pytań `needs_review` i 0 `verified`. To nie jest oficjalny arkusz. Bramka verified-only pozostaje bez zmian.

## Generowanie kolejnego wariantu

```bash
python scripts/draft_mock_exam.py --seed 20261025 --output podstawowy/egzamin-probny/wariant-002.json --key-output podstawowy/egzamin-probny/klucz-002.json
```

Ten sam seed i bank dają ten sam zestaw. Bez `--seed` losowany jest seed. Dobór jest proporcjonalny i obejmuje wszystkie 13 działów. Próg treningowy 20/30 (2/3), czas 60 minut.
