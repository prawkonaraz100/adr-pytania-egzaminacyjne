# Etap 4x136 — pogłębienie kompetencji ADR-B-0629–0638

**Data:** 29.10.2026. **Zakres:** wyłącznie kurs podstawowy ADR.

## Uzasadnienie wyboru
Przegląd świeżego `podstawowy/kompetencje.json` wykazał 11 celów teoretycznych z najniższą liczebnością — po trzy pytania. Ta partia dodaje scenariusze dotyczące dokumentu odpadu, przekazania informacji ratownikom, skażonej odzieży, ostrzegania osób postronnych, kamizelki ostrzegawczej, tablic pomarańczowych i wspólnego przewozu żywności/paszy.

## Nowe rekordy i podstawy do niezależnej kontroli

| ID | Kompetencja | Podstawa ADR |
|---|---|---|
| ADR-B-0629 | ADR-B-03-K02 | ADR 2025, 5.4.1.1.3.1 |
| ADR-B-0630 | ADR-B-05-K07 | ADR 2025, 5.4.3.4 |
| ADR-B-0631 | ADR-B-05-K08 | ADR 2025, 5.4.3.4 |
| ADR-B-0632 | ADR-B-05-K09 | ADR 2025, 5.4.3.4 |
| ADR-B-0633 | ADR-B-05-K10 | ADR 2025, 8.1.5.2; 5.4.3.4 |
| ADR-B-0634 | ADR-B-06-K05 | ADR 2025, 5.3.2.2.1 |
| ADR-B-0635 | ADR-B-06-K06 | ADR 2025, 5.3.2.3.1 |
| ADR-B-0636 | ADR-B-06-K07 | ADR 2025, 5.3.2.2.2 |
| ADR-B-0637 | ADR-B-06-K08 | ADR 2025, 5.3.2.3.1 |
| ADR-B-0638 | ADR-B-09-K03 | ADR 2025, 7.5.4 |

Wszystkie rekordy zachowują `needs_review`. Podstawy prawne wskazują miejsca do kontroli, nie formalną akceptację specjalisty.

## Metryki wstępne
- Bank: 628 → 638 pytań.
- Rozkład kluczy A/B/C: A=212/B=213/C=203 → A=214/B=218/C=206.
- Wskaźnik „poprawna = jedyna najdłuższa”: 70/638 = 10.97%; maksimum działu: 13.95%.
- Wyjaśnienia: 322–380 znaków; 0 poniżej 300 i 0 powyżej 500. Wskaźnik i rozkład przeliczono z rzeczywistego pliku banku.
- **Ograniczenie:** lokalny checkout/testy nie były dostępne w tym środowisku; nie deklaruję lokalnego PASS. Wymagany jest PASS wszystkich kontroli CI przed scaleniem.

## Kontrola merytoryczna
Przed publikacją specjalista powinien literalnie porównać każde pytanie i wszystkie warianty z polskim ADR 2025 (Dz.U. 2025 poz. 642) oraz sprostowaniem (Dz.U. 2025 poz. 1575). Szczególnej kontroli wymagają zakres ADR 7.5.4, instrukcje pisemne i wyposażenie. Pytania są materiałem roboczym.
