# Etap 4x37 — rozdzielenie powtórzeń dotyczących kodu tunelowego (-)

- Data: 26.10.2026.
- Punkt wyjścia: świeży `main` po PR #479, commit `3978fc38022f3aecdc993e4f5fc388b267ad7e3e`.
- Zakres: kurs podstawowy ADR, dział B-11.

## Potwierdzone powtórzenie

ADR-B-0065 i ADR-B-0431 pytały praktycznie o to samo: co oznacza kod tunelowy `(-)). W obu poprawna odpowiedź mówiła, że dla towaru nie przypisano ograniczenia tunelowego ADR. Samo podobieństwo nie było tylko leksykalne — sprawdzany fakt i zastosowany punkt ADR (8.6.3.1) były takie same.

Przeredagowano **ADR-B-0431**, zachowując ID, dział i poprawną literę C. Nowa sytuacja sprawdza osobny aspekt: kierowca widzi znak drogowy ograniczający wjazd, mimo że towar ma kod `(-)). Poprawna decyzja to stosowanie znaku drogowego, ponieważ kod oznacza brak ograniczenia tunelowego przypisanego temu towarowi przez ADR, a nie uchylenie lokalnych znaków lub innych przepisów.

### Przed / po

- **Przed:** „Towar ma kod ograniczenia tunelowego (-) w kolumnie (15) tabeli A. Jak interpretować ten znak?”
- **Po:** „Kod tunelowy (-) znajduje się w kolumnie 15 tabeli A. Na trasie jest jednak znak drogowy ograniczający wjazd do tunelu. Co ma zrobić kierowca?”

Wyjaśnienie ma 318 znaków, proste zdania i podstawę ADR 8.6.3.1. Wszystkie odpowiedzi pozostają wiarygodnymi błędami interpretacji, a poprawna odpowiedź nie jest jedyną najdłuższą.

## Synchronizacja i metryki

- Zaktualizowano snapshoty sekwencyjne i klauzulowe dla ADR-B-0431 oraz migawkę banku w pakiecie recenzyjnym.
- Zaktualizowano `source_bank_head` w wariantach i kluczach egzaminów próbnych 001–005. ADR-B-0431 nie występuje w arkuszach, więc nie zmieniano ich pytań.
- Bank: 609 pytań, 0 zduplikowanych ID; wszystkie `needs_review`, 0 `verified`.
- Explanation poniżej 300 znaków: 0.
- „Poprawna odpowiedź jest jedyną najdłuższą”: 72/609 = 11,82% globalnie; dział B-11 pozostaje poniżej progu 18%.

## Ograniczenia

Podstawa ADR wskazuje temat do kontroli, ale zmiana nie jest formalnym zatwierdzeniem prawnym. Pytanie pozostaje `needs_review` do niezależnej recenzji specjalisty. Nie rozpoczęto kursu cystern ani innej specjalizacji.
