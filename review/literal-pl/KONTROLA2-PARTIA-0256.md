# Druga kontrola ADR-B-0256

**Werdykt: POPRAW.** Pierwotny klucz A był zgodny z ADR. Pytanie dublowało ADR-B-0017 i częściowo ADR-B-0170. Opcja B błędnie zalecała użycie wody, a C myliła literę X z oznaczeniem LQ. Wyjaśnienie pomijało warunek zgody specjalistów. Porównanie z pierwszą kontrolą w PR #863 potwierdziło duplikat.

Pytanie zastąpiono porównaniem pełnych kodów 80 i X80. W pozostałych 779 pytaniach nie znaleziono takiego zestawienia. A opisuje wspólne działanie żrące oraz dodatkowe ostrzeżenie w X80. B błędnie przypisuje obu kodom ostrzeżenie przed wodą i traktuje X jako wskaźnik silniejszego działania żrącego. C przypisuje ostrzeżenie kodowi 80 zamiast X80. Ilustracja przedstawia X80 i pasuje do treści. Pytanie pozostaje w kompetencji ADR-B-06-K04 ze statusem `needs_review`.

Zweryfikowano obraz urzędowego PDF-u. [ADR 5.3.2.3.1, s. 956 Dz.U.](https://eli.gov.pl/api/acts/DU/2025/642/text/I/D20250642-20.pdf#page=6) określa znaczenie X i warunek stosowania wody. [ADR 5.3.2.3.2, s. 959 Dz.U.](https://eli.gov.pl/api/acts/DU/2025/642/text/I/D20250642-20.pdf#page=9) zawiera obie pozycje. Sprostowanie Dz.U. 2025 poz. 1575 ich nie zmienia.
