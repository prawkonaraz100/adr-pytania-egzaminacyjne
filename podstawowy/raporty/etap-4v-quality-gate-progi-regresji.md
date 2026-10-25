# Etap 4v — blokujący Quality Gate dla heurystyk zgadywania

**Świeży main:** `34cc3d653517f9533d85f5eaee59ff7a9bdd7c5d`, po scaleniu PR #292. Metryki działowe etapu 4v są osiągnięte i opisane w [raporcie końcowym](etap-4v-finalne-progi-13-dzialow.md).

## Zmiana

Dodano test regresyjny `tests/test_stage4v_leakage_gate.py`, uruchamiany przez istniejącą komendę CI `python -m unittest discover -s tests -v`. Test importuje dokładnie tę samą implementację liczącą metryki, której używa skrypt doradczy `scripts/answer_leakage_metrics.py`, więc nie powiela innej definicji „najkrótszej” ani słów absolutnych.

Blokujące progi **osobno dla każdego z 13 działów**:
- poprawna odpowiedź ściśle najkrótsza (bez remisów): **≤38%**;
- słowo absolutne w błędnej odpowiedzi: **≤38% dystraktorów**;
- poprawna odpowiedź ściśle najdłuższa (bez remisów): **≤18%** (istniejący test również to egzekwuje).

Test sprawdza 13 działów, po dwa dystraktory na pytanie, oraz syntetyczny przypadek, w którym poprawna odpowiedź jest najkrótsza i słowo absolutne występuje w odpowiedzi błędnej. Porównanie progów jest całkowitoliczbowe, więc granice nie zależą od zaokrąglenia wyświetlanego procentu.

## Ograniczenia

Metryki nie sprawdzają, czy treść opcji jest prawnie prawdziwa, i nie wykrywają wszystkich wskazówek językowych. Nie zmieniono żadnego pytania, klucza ani `verification_status`: 569 `needs_review`, 0 `verified`. To Quality Gate redakcyjny, a nie recenzja specjalisty ADR.

PR wymaga PASS wszystkich kontroli CI przed scaleniem; po scaleniu wynik odnotować w Issue #10. Następna luka: pogłębienie dydaktyki 13 lekcji i scenariuszy praktycznych bez kursu cystern.
