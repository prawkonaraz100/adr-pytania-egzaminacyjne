# Etap 4x13 — kontrola naprawcza objaśnień inline B-05–08

## Punkt wyjścia
- Świeży `main`: `0c24a95b80fbd482bab3b3acd4878f95cd2a413d`, po scaleniu PR #366.
- Zakres: czytelność pierwszego użycia terminów fachowych; bank i klucze bez zmian.

## Zmiany
- **B-05:** uproszczono fragment o przekazywaniu danych służbom. Numer UN został wyjaśniony wprost, bez zagnieżdżonego linku do tabeli A; wyraźnie rozdzielono wezwanie pomocy, przekazanie danych i granicę bezpieczeństwa przy dokumentach. CI wykryło brak kotwicy ADR przy tym pierwszym użyciu; dodano ją.
- **B-06:** uproszczono wprowadzenie do oznakowania. Krótkie objaśnienia numeru UN, tablicy pomarańczowej i ADR stoją bezpośrednio przy pierwszym użyciu. Test wskazał też pierwsze wystąpienie „tabela A” w sekcji podstawy prawnej; dodano tam odsyłacz do kotwicy.
- **B-07:** przejrzano wstęp i pierwsze użycia. Nie znaleziono potwierdzonej usterki wymagającej zmiany, więc nie zmieniano treści.
- **B-08:** dodano przy pierwszym użyciu definicję „świadectwa dopuszczenia pojazdu” oraz odsyłacze do kotwic słowniczka dla tego pojęcia i skrótu ADR.

## Przykłady przed → po
1. **B-05**
   - Przed: „…w tym numer UN (czterocyfrowy identyfikator, po którym odnajdujesz towar w tabeli A ([słowniczek]…); [słowniczek]…)…”
   - Po: „…przekaż służbom numer UN — czterocyfrowy identyfikator towaru ([słowniczek](../SLOWNICZEK.md#numer-un)) — oraz dane z dokumentów przewozowych.”
2. **B-06**
   - Przed: „Nieczytelna nalepka, błędny numer UN (…) albo rozbieżność na tablicy pomarańczowej (…) może utrudnić prawidłową reakcję.”
   - Po: „Numer UN to czterocyfrowy identyfikator towaru; tablica pomarańczowa jest oznaczeniem pojazdu stosowanym w określonych przewozach. Jeśli oznakowanie nie pasuje do dokumentów, wyjaśnij rozbieżność przed wyjazdem.”
3. **B-08**
   - Przed: „…pojazd może wymagać dodatkowego świadectwa dopuszczenia.”
   - Po: „…pojazd może wymagać świadectwa dopuszczenia pojazdu — dokumentu potwierdzającego, że dany typ pojazdu spełnia specjalne wymagania ADR, gdy mają one zastosowanie ([słowniczek](../SLOWNICZEK.md#swiadectwo-dopuszczenia-pojazdu)).”

## Kontrola
- 3 akapity uproszczone lub poprawione (B-05, B-06, B-08); dodano 1 bezpośrednie objaśnienie wraz z kotwicą w B-08.
- Bank: bez zmian; ID, poprawne litery i statusy bez zmian.
- Testy lokalne nie uruchamiano w osobnym checkout; pełny test w CI wykrył trzy brakujące odsyłacze w pierwszym użyciu (ADR w B-05, tabela A w B-06, ADR w B-08). Poprawiono je na tej samej gałęzi; końcowy wynik Quality Gate musi być PASS przed scaleniem.

## Ograniczenia
Zmiany są redakcyjne i nie stanowią niezależnej recenzji prawnej. Nie dodano nowych twierdzeń prawnych ani nie zmieniano statusów `needs_review`.
