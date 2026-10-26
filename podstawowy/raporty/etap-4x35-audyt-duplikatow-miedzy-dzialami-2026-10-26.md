# Etap 4x35 — audyt powtórzeń między działami i nowa kontrola CI

- Data: 26.10.2026.
- Punkt wyjścia: świeży `main` po scaleniu PR #477, commit `f74dc906502d22a02400dbd7c6ec2758a8f0f5ca`.
- Zakres: wyłącznie kurs podstawowy ADR, wszystkie 609 pytań.

## Wynik skanowania między działami

Przeprowadzono porównanie par pytań przypisanych do różnych działów, z normalizacją wielkości liter i polskich znaków. Porównano identyczne treści, identyczne zestawy trzech odpowiedzi i podobieństwo słów w treści pytania.

- Identyczne treści pytań między działami: **0 par**.
- Identyczne zestawy odpowiedzi między działami: **0 par**.
- Pary między działami o podobieństwie leksykalnym co najmniej 0,60: **0 par**.
- Nie zmieniono żadnego pytania i nie zmieniono statusu żadnego rekordu.
- Wcześniejszy audyt 4x34 nadal ma wynik: 609 pytań, 0 duplikatów ID, globalny wskaźnik „poprawna = jedyna najdłuższa” 71/609 = 11,66%, wszystkie explanation co najmniej 300 znaków.

## Nowa kontrola Quality Gate

Dodano:
- `scripts/check_cross_module_duplicates.py` — blokuje identyczne treści, identyczne zestawy odpowiedzi lub niemal identyczne pytania między różnymi działami (próg podobieństwa 0,80).
- `tests/test_cross_module_duplicates.py` — testy dla identycznych treści, identycznych odpowiedzi, podobnych pytań, par w tym samym module i normalizacji polskich znaków.
- Krok w `.github/workflows/quality.yml`: `python scripts/check_cross_module_duplicates.py --threshold 0.80`.

Kontrola działa blokująco, ponieważ identyczne pytanie w dwóch działach może oznaczać błędne przypisanie kompetencji albo niepotrzebne powtórzenie. Samo podobieństwo tekstu nie dowodzi błędu merytorycznego; w razie alarmu para musi zostać oceniona ręcznie, a nie automatycznie usunięta.

## Ograniczenia

To test integralności redakcyjnej, nie ocena poprawności prawnej. Brak wykrytych duplikatów nie dowodzi pełnego pokrycia programu. Wszystkie 609 pytań pozostaje `needs_review`; 0 `verified`, bez formalnej akceptacji specjalisty. Nie rozpoczęto kursu cystern ani innego kursu.
