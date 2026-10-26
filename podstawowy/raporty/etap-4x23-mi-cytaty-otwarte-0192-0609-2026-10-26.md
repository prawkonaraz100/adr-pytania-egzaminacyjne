# Etap 4x23 — porównanie rekordów z istniejącym cytatem MI

- Data: 26.10.2026.
- Świeży `main`: `b095799701d34714dbaa4b192c4a2f04dbd6cdf2`.
- Podstawa porównania: `MI ADR 2025 PL (pomocniczy), strona Dz.U. do potwierdzenia przez specjalistę`.
- Nie wpisano żadnej strony Dz.U. i nie ponawiano pobierania PDF Dz.U.

## Wynik partii

- W dostępnych plikach partii 4x22 znaleziono **43 otwarte rekordy z cytatem MI**.
- **37** wyników: zgodne w zakresie przytoczonego cytatu.
- **6** cytatów: niewystarczające do potwierdzenia całego zakresu pytania; opisano ograniczenie w rejestrze.
- Potwierdzone sprzeczności: **0**.
- Poprawki pytań lub kluczy: **0**.
- Statusy `verified`: **0**; wszystkie wpisy pozostają `needs_review`.
- W opisie zadania podano 51 rekordów z cytatem MI. Pozostałych 8 nie udało się zidentyfikować w dostępnych plikach partii. Nie przypisano ich arbitralnie do ID; pozostają do odnalezienia w dużym ledgerze.

## Cytaty wymagające pełniejszego fragmentu

| ID | Dlaczego cytat nie wystarcza |
|---|---|
| ADR-B-0352 | Cytat wspiera wymóg klina, ale nie obejmuje szczególnego warunku 8.3.7 dotyczącego przyczepy bez własnego układu hamulcowego. |
| ADR-B-0430 | Cytat wskazuje położenie kodu tunelowego, lecz nie wyjaśnia znaczenia kategorii tunelu A. |
| ADR-B-0483 | Cytat nie zawiera przypisu o wyjątku dotyczącym płynu do płukania oczu dla nalepki 2.3. |
| ADR-B-0484 | Cytat dotyczy masek ucieczkowych, a pytanie dotyczy łopaty, osłony odpływu i pojemnika. |
| ADR-B-0486 | Cytat dotyczy masek ucieczkowych, a nie wyposażenia do ograniczenia rozlewu. |
| ADR-B-0609 | Cytat potwierdza wymiary oznakowania LQ, ale nie sam obowiązek pozostawienia go w opisanej sytuacji. |

## Zakres i ograniczenia

Rejestr `review/batches/stage4x23-mi-cited-open-records-0192-0609.json` zawiera ID, dział, punkt ADR, cytat MI, podstawę porównania i literal_comparison_result dla każdego z 43 znalezionych rekordów. Wynik „zgodne” dotyczy wyłącznie zakresu cytatu, nie jest formalną weryfikacją prawną. Brak wystarczającego cytatu nie jest traktowany jako sprzeczność. Pole `official_gazette_comparison` pozostaje `pending`; nie wpisano stron Dz.U. ani nie zmieniono banku pytań.
