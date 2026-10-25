# Egzamin próbny ADR podstawowy — materiały robocze

- [Wariant 001 — arkusz pytań](wariant-001.json)
- [Wariant 001 — klucz i wyjaśnienia](klucz-001.json)
- [Wariant 002 — arkusz pytań](wariant-002.json)
- [Wariant 002 — klucz i wyjaśnienia](klucz-002.json)
- [Wariant 003 — arkusz pytań](wariant-003.json)
- [Wariant 003 — klucz i wyjaśnienia](klucz-003.json)
- [Wariant 004 — arkusz pytań](wariant-004.json)
- [Wariant 004 — klucz i wyjaśnienia](klucz-004.json)
- [Wariant 005 — arkusz pytań](wariant-005.json)
- [Wariant 005 — klucz i wyjaśnienia](klucz-005.json)

**Wyłącznie trening wewnętrzny.** Bank źródłowy ma 609 pytań `needs_review` i 0 `verified`. To nie jest oficjalny arkusz. Bramka verified-only pozostaje bez zmian.

## Wynik końcowej kontroli 4x1 (25.10.2026)

- Warianty 001–003: po 30 pytań, wszystkie 13 działów, brak duplikatów i brak wspólnych ID między wariantami.
- Każdy klucz ma kolejność zgodną z arkuszem; klucze, wyjaśnienia, odpowiedzi i treści pytań zgodne z bankiem na źródłowym SHA `e1eb80d9db9bb5f475bb655fc08b47b7a866bb64`.
- Wszystkie warianty mają `publication_authorized: false`; pozostają treningiem roboczym, nie zatwierdzonym egzaminem.
- Raport: [końcowa kontrola egzaminu i pakietu recenzyjnego](../raporty/etap-4x1-kontrola-egzaminu-i-pakietu-2026-10-25.md).

## Generowanie kolejnego wariantu

```bash
python scripts/draft_mock_exam.py --seed 20261025 --variant 2 --source-head e1eb80d9db9bb5f475bb655fc08b47b7a866bb64 --exclude podstawowy/egzamin-probny/wariant-001.json --output podstawowy/egzamin-probny/wariant-002.json --key-output podstawowy/egzamin-probny/klucz-002.json
```

Wariant 002 wyklucza wszystkie ID z wariantu 001, gdy dostępna pula pozwala. Ten sam seed, bank i plik wykluczeń dają ten sam zestaw. Bez `--seed` losowany jest seed. Dobór jest proporcjonalny i obejmuje wszystkie 13 działów. Próg treningowy 20/30 (2/3), czas 60 minut.

Wariant 003: seed `2026102505`, 30 pytań, 20/30 do zaliczenia, 60 minut. Wykluczono wszystkie 60 ID z wariantów 001 i 002; arkusz i klucz są regenerowane z bieżącego banku. Do odtworzenia użyj `scripts/draft_mock_exam.py` z połączoną listą wykluczeń lub przyjętym deterministycznym algorytmem wyboru. Arkusz jest wyłącznie roboczy — 0 pytań zatwierdzonych jako `verified`.


## Etap 4x5 — warianty 004–005 i synchronizacja

- Warianty 001–005 zawierają po 30 pytań; nie ma powtórzeń ID wewnątrz wariantu ani między wariantami.
- Każdy wariant i klucz sprawdzany jest względem aktualnego banku: ID, dział, treść pytania, opcje, poprawna odpowiedź i explanation.
- Warianty 004–005 są deterministyczne, mają proporcjonalny rozkład 13 działów i dobrane seedy `2026102504` i `2026102506`, z rozkładem poprawnych opcji A/B/C odpowiednio {"A":9,"B":10,"C":11} oraz {"A":10,"B":10,"C":10}.
- Bank ma 609 pytań `needs_review`, 0 `verified`; warianty pozostają materiałem treningowym, `publication_authorized: false`.
