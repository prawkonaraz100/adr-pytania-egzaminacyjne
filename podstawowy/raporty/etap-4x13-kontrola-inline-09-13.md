# Etap 4x13 — kontrola naprawcza objaśnień inline B-09–13

## Punkt wyjścia
- Świeży `main`: `7c57f2dcf60e171274f561524d668a9cb3d3f156`, po scaleniu PR #367.
- Zakres: kontrola czytelności i poprawności wstawek objaśniających w B-09–B-13.

## Wynik przeglądu
- **B-09:** przejrzano definicję przewozu luzem, tabelę A, wspólny załadunek i wskazanie CV28. Nie wykryto potwierdzonej usterki składniowej wymagającej zmiany.
- **B-10:** przejrzano objaśnienia ADR/RID/IMDG oraz dokumentację transportu kombinowanego. Nie wykryto potwierdzonej usterki w sprawdzonym zakresie.
- **B-11:** przejrzano kod tunelowy, kategorie A–E i odsyłacze do tabeli A. Nie wykryto potwierdzonej usterki w sprawdzonym zakresie.
- **B-12:** wykryto uszkodzenie tekstu „…tabela-a))DR 1.10.3.1.2”. Zostało ono naprawione; akapit o towarach dużego ryzyka przepisano prostszym językiem, zachowując rozróżnienie klasy 7, sprawdzanie wpisu tabeli A, sposób przewozu i podstawę ADR 1.10.3.1.2.
- **B-13:** przejrzano odwołania do dokumentu przewozowego, numeru UN, grupy pakowania i zagrożenia dodatkowego. Nie wykryto potwierdzonej usterki składniowej w badanym zakresie.

## Przykłady przed → po
1. **B-12 — uszkodzony zapis przepisu**
   - Przed: „…warunki przewozu; [słowniczek](../SLOWNICZEK.md#tabela-a))DR 1.10.3.1.2…”
   - Po: „…sprawdź właściwy wpis w tabeli A, czyli wykazie ADR, który łączy numer UN z warunkami przewozu ([słowniczek](../SLOWNICZEK.md#tabela-a); [słowniczek](../SLOWNICZEK.md#numer-un)), oraz próg z ADR 1.10.3.1.2.”
2. **B-12 — sens wymagania**
   - Przed: „Dla towarów innych niż klasa 7 wykaz i progi sprawdza się w tabeli A…”
   - Po: „Dla towarów innych niż klasa 7 sprawdź właściwy wpis w tabeli A… oraz próg z ADR 1.10.3.1.2.”
3. **B-12 — wyjaśnienie pułapki**
   - Przed: „Próg 3000 l dla cystern nie przenosi się automatycznie na sztuki przesyłek…”
   - Po: „Próg może zależeć od sposobu przewozu: wartości dla cystern nie stosuj automatycznie do sztuk przesyłek.”

## Kontrola
- Potwierdzona usterka składniowa: 1, poprawiona w B-12.
- Uproszczony akapit: 1 (B-12).
- Bank i klucze: bez zmian; żadne pytanie nie otrzymało statusu `verified`.
- Test `tests/test_learner_glossary.py` oraz cały Quality Gate muszą przejść w CI PR. Nie uruchamiano osobnego lokalnego checkout; weryfikacja treści i kotwic była prowadzona na plikach pobranych z GitHub.

## Ograniczenia
To naprawa redakcyjna, a nie niezależna recenzja prawna. Nie zmieniano progów ani interpretacji ADR bez potwierdzenia w tekście urzędowym.
