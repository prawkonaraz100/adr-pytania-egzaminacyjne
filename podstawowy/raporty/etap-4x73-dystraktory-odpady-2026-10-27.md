# Etap 4x73 — dalsza korekta oczywistego dystraktora w temacie odpadów

Data: 27.10.2026. Punkt wyjścia: świeży `main` po PR #530, commit `85cb08165522dec83a5bbc6f79e91fac77294211`. Zakres: wyłącznie kurs podstawowy ADR.

## Potwierdzony problem

`ADR-B-0336` pyta, czyja wiedza może stanowić podstawę klasyfikacji odpadu o nieznanym dokładnie składzie. Dotychczasowe błędne opcje „Dowolny świadek załadunku” i „Wyłącznie kierowca pojazdu mijającego transport” były zbyt oczywiste, by stanowić uczciwy test znajomości obowiązków uczestników przewozu.

| Opcja | Nowa treść | Dlaczego jest błędna |
|---|---|---|
| A | Załadowca, ponieważ widzi stan opakowania odpadu podczas załadunku | Kontrola stanu opakowania nie zastępuje wiedzy nadawcy o odpadzie, o której mówi 2.1.3.5.5 |
| B (poprawna, bez zmiany) | Nadawca | Właściwy podmiot wskazany w 2.1.3.5.5 |
| C | Przewoźnik, ponieważ kontroluje dokumenty odpadu przed wyruszeniem | Sprawdzenie dokumentu nie oznacza posiadania wiedzy o składzie odpadu wymaganej w tym szczególnym przepisie |

Wyjaśnienie napisano w języku początkującego kursanta: dlaczego B, dlaczego A i C mylą obowiązki oraz jaka jest podstawa prawna. Zachowano ID, poprawną literę i status `needs_review`. **Podstawa:** ADR 2025 2.1.3.5.5, Dz.U. 2025 poz. 642 i sprostowanie poz. 1575; kontrola pomocnicza z tomem I ADR 2025. Nie jest to formalna weryfikacja specjalisty.

## Synchronizacja

Pytanie nie występuje w wariantach egzaminów 001–005, dlatego nie trzeba było zmieniać pytań arkuszy ani kluczy odpowiedzi. Zaktualizowano `source_bank_head` w każdym wariancie i kluczu oraz bieżący identyfikator banku w manifeście, instrukcjach recenzji i kolejkach specjalisty. Zaktualizowano także audyt sekwencyjny i A/B/C dla ADR-B-0336.

## Metryki przed Quality Gate CI

- 609 pytań; `needs_review`: 609, `verified`: 0.
- Poprawna odpowiedź jako jedyna najdłuższa: 73/609 = 11.99% (limit 18%).
- Najkrótsze explanation: 300 znaków (minimum Quality Gate: 200).
- Działy: ADR-B-01 13.33%; ADR-B-02 14.29%; ADR-B-03 14.29%; ADR-B-04 13.04%; ADR-B-05 11.63%; ADR-B-06 11.11%; ADR-B-07 12.50%; ADR-B-08 11.90%; ADR-B-09 8.70%; ADR-B-10 7.27%; ADR-B-11 13.95%; ADR-B-12 13.64%; ADR-B-13 10.64%.
- Nie dodawano nowego pytania ani nie zmieniano numeracji; nie rozpoczynano innych kursów.

## Następny krok

Przejrzeć kolejne potencjalnie zbyt łatwe dystraktory w priorytetowej kolejce, ale nie zmieniać ich bez potwierdzenia właściwej podstawy ADR oraz sprawdzenia, czy nowa błędna odpowiedź nie stanie się częściowo prawdziwa. Wszystkie dane w pakiecie pozostają przeznaczone do recenzji.
