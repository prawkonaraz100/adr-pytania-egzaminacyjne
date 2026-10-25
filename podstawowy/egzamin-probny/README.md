# Egzamin próbny ADR podstawowy — materiały robocze

- [Wariant 001 — arkusz pytań](wariant-001.json)
- [Wariant 001 — klucz i wyjaśnienia](klucz-001.json)
- [Wariant 002 — arkusz pytań](wariant-002.json)
- [Wariant 002 — klucz i wyjaśnienia](klucz-002.json)
- [Wariant 003 — arkusz pytań](wariant-003.json)
- [Wariant 003 — klucz i wyjaśnienia](klucz-003.json)

**Wyłącznie trening wewnętrzny.** Bank źródłowy ma 569 pytań `needs_review` i 0 `verified`. To nie jest oficjalny arkusz. Bramka verified-only pozostaje bez zmian.

## Generowanie kolejnego wariantu

```bash
python scripts/draft_mock_exam.py --seed 20261025 --variant 2 --source-head dac5ecc0ac3191c4db8afa5873e208a5f48bbeeb --exclude podstawowy/egzamin-probny/wariant-001.json --output podstawowy/egzamin-probny/wariant-002.json --key-output podstawowy/egzamin-probny/klucz-002.json
```

Wariant 002 wyklucza wszystkie ID z wariantu 001, gdy dostępna pula pozwala. Ten sam seed, bank i plik wykluczeń dają ten sam zestaw. Bez `--seed` losowany jest seed. Dobór jest proporcjonalny i obejmuje wszystkie 13 działów. Próg treningowy 20/30 (2/3), czas 60 minut.

Wariant 003: seed `2026102505`, 30 pytań, 20/30 do zaliczenia, 60 minut. Wykluczono wszystkie 60 ID z wariantów 001 i 002. Do odtworzenia użyj `scripts/draft_mock_exam.py` z połączoną listą wykluczeń lub przyjętym deterministycznym algorytmem wyboru. Arkusz jest wyłącznie roboczy — 0 pytań zatwierdzonych jako `verified`.
