# Etap 4v — partia 1a, pierwsze 14 rekordów (2026-10-25)

**Punkt wyjścia:** świeży main `629f3534cc81cf402adee7ae4e5972d4e9155728`. Początkowy cel około 40 pytań podzielono na małe PR-y, żeby uniknąć automatycznego masowego usuwania słów zmieniającego sens; ta pierwsza zmiana obejmuje 14 wskazanych identyfikatorów.

Wybrane identyfikatory: ADR-B-0001, ADR-B-0002, ADR-B-0006, ADR-B-0010, ADR-B-0012, ADR-B-0013, ADR-B-0015, ADR-B-0019, ADR-B-0025, ADR-B-0026, ADR-B-0028, ADR-B-0029, ADR-B-0032, ADR-B-0033.

Zmiana: podmieniono dystraktory zawierające „zawsze”, „nigdy”, „wyłącznie”, „tylko” itd. na scenariusze z konkretnym, nadal błędnym rozumowaniem kierowcy. Nie zmieniono poprawnych odpowiedzi, kluczy, explanation ani `needs_review`, ponieważ istniejące wyjaśnienia nadal wyraźnie odrzucają te same merytoryczne pomyłki. Zsynchronizowano migawki obu audytów oraz wariant próbny 001, gdy zawierał zmienione pytanie. Audit A/B/C pozostaje weryfikacją redakcyjną, a nie eksperckim `verified`.

| Metryka | Przed | Po |
|---|---:|---:|
| Poprawna ściśle najkrótsza | 256/569 | 261/569 |
| Poprawna ściśle najdłuższa | 71/569 | 70/569 |
| Słowa absolutne w dystraktorach | 375/1138 | 355/1138 |
| Słowa absolutne w poprawnych | 26/569 | 26/569 |
| Luka udziału słów absolutnych | 28.38 p.p. | 26.63 p.p. |
| Pytania z absolutnym słowem wyłącznie w dystraktorach | 267 | 253 |

Próg 18% dla poprawnej najdłuższej zachowano. Nowe metryki pozostają raportowe. Nie wykonano niezależnej literalnej recenzji polskiego ADR 2025 i sprostowania; pytania pozostają `needs_review`.

**Quality Gate:** do potwierdzenia w CI przed scaleniem.
