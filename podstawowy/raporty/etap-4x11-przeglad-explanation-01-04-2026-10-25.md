# Etap 4x11 — ręczny przegląd ostrzeżeń explanation, partia B-01–04

- Data: 25.10.2026.
- Świeży punkt startowy: `main` `2ac484095d84fb4fbf732d8633ec8262eaf63b35`.
- Zakres: 28 z 86 ID ostrzeżeń heurystycznych z sekcji 3 raportu 4x10. Moduł określono na podstawie pola `module_id`, a nie numeru ID.
- Bank bez zmian merytorycznych w tej partii: wszystkie 609 pytań nadal `needs_review`; 0 `verified`.

## Wynik ręcznego przeglądu

| Dział | Przejrzane ostrzeżenia | Przepisane | Fałszywe alarmy |
|---|---:|---:|---:|
| B-01 | 12 | 0 | 12 |
| B-02 | 4 | 0 | 4 |
| B-03 | 4 | 0 | 4 |
| B-04 | 8 | 0 | 8 |
| **Razem** | **28** | **0** | **28** |

W każdym z 28 wyjaśnień sprawdzono, czy odpowiedź poprawna jest uzasadniona, czy odrzucono kuszące odpowiedzi błędne konkretnym powodem, czy użyte skróty są objaśnione lub zrozumiałe z kontekstu oraz czy na końcu podano punkt ADR. Nie znaleziono w tej próbce potwierdzonego braku dydaktycznego wymagającego przepisania. Przepisanie dobrych wyjaśnień tylko po to, by dodać określone słowo, pogorszyłoby stabilność treści bez korzyści dla kursanta.

## Lista sprawdzonych ID

- **B-01 (12):** ADR-B-0001, ADR-B-0124, ADR-B-0147, ADR-B-0271, ADR-B-0312, ADR-B-0527, ADR-B-0529, ADR-B-0534, ADR-B-0535, ADR-B-0571, ADR-B-0573, ADR-B-0595.
- **B-02 (4):** ADR-B-0094, ADR-B-0128, ADR-B-0309, ADR-B-0499.
- **B-03 (4):** ADR-B-0046, ADR-B-0178, ADR-B-0325, ADR-B-0327.
- **B-04 (8):** ADR-B-0280, ADR-B-0297, ADR-B-0346, ADR-B-0349, ADR-B-0357, ADR-B-0362, ADR-B-0471, ADR-B-0580.

## Dlaczego to fałszywe alarmy

Wszystkie 28 wyjaśnień podają powód poprawnej odpowiedzi, odrzucają błędne warianty przez wskazanie konkretnej pomyłki (np. pomylenie mnożnika kategorii, dokumentu, klasy, obowiązku lub warunku wyłączenia) i kończą się podstawą ADR. Brak konkretnego słowa-sygnału nie oznacza braku rozumowania dydaktycznego. Nie zmieniano poprawnych liter, dystraktorów, numeracji ani statusów.

## Heurystyka — rozszerzenie sygnałów

W repozytorium nie było osobnego, uruchamianego walidatora odpowiadającego opisowi ostrzeżeń w raporcie 4x10. Dodano jawny, doradczy skrypt `scripts/check_explanation_heuristics.py` z listą kandydatów utrwaloną w `review/stage4x11-heuristic-candidates.json`, testy i krok Quality Gate. Rozszerzono słownictwo o m.in. „więc”, „czyli”, „oznacza to”, „z tego powodu”, „w rezultacie”, „dzięki temu”, „nie zastępuje” i „nie wystarczy”. Skrypt nie wymusza konkretnego słowa i nie uznaje braku sygnału za błąd.

- Przed: **86** ostrzeżeń w raporcie 4x10.
- Po rozszerzeniu sygnałów: **12** kandydatów nadal bez żadnego z rozszerzonych sygnałów (86 → 12; spadek o 74).
- Te 12 przypadków jest kolejką do ręcznego czytania, nie werdyktem. Nie rozszerzamy słownictwa dalej tylko po to, by sprowadzić wynik do zera.

## Wskaźniki banku

- Liczba pytań: 609; duplikaty ID: 0.
- Wskaźnik „poprawna = jedyna najdłuższa” według raportu 4x10: 77/609 = 12,64% globalnie; każdy dział ≤16%.
- Minimalna długość explanation: 300 znaków; poniżej 200: 0.
- Statusy: 609 `needs_review`, 0 `verified`.

## Ograniczenia

To przegląd dydaktyczny wyjaśnień z listy heurystycznej, a nie niezależna weryfikacja prawna. Nie zmieniano treści prawnej, ponieważ nie wykryto potwierdzonej wady w tych 28 rekordach. Kolejne partie przejrzą pozostałe 58 ostrzeżeń.
