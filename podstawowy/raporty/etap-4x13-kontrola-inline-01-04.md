# Etap 4x13 — kontrola naprawcza objaśnień inline B-01–04

## Zakres i punkt wyjścia
- Bazowy `main`: `7e96d410f3c1ad0e389df1a37a6ab65231acced9`.
- Kontrola dotyczy jakości wykonania wcześniejszego etapu 4x13; nie zmienia banku pytań ani kluczy.
- Nie stwierdzono potrzeby zmiany statusów pytań.

## Potwierdzone problemy i poprawki
- **B-01:** akapit wprowadzający powtarzał rozwinięcie ADR i zawierał zagnieżdżony odsyłacz do tabeli A w definicji numeru UN. Zastąpiono go krótszymi zdaniami: czym jest ADR, jak znaleźć numer UN i czym różnią się LQ, EQ oraz wyłączenie z ADR 1.1.3.6. Każdy termin ma odsyłacz bezpośrednio przy pierwszym użyciu.
- **B-02:** znaleziono uszkodzony ciąg „kod klasyfikacyjn…y”, powstały przy wstawianiu definicji. Przywrócono prawidłowe brzmienie „kod klasyfikacyjny” i uproszczono dwa punkty listy, żeby definicje nie były zagnieżdżone w kilku nawiasach.
- **B-03 i B-04:** w sprawdzonym zakresie nie wykryto analogicznego uszkodzenia składniowego wymagającego poprawki w tej partii. Nie zmieniano ich merytoryki.

## Przykłady przed → po
1. **B-01 — numer UN**
   - Przed: „Numer UN (czterocyfrowy identyfikator, po którym odnajdujesz towar w tabeli A ([słowniczek]…); [słowniczek]…) identyfikuje konkretną pozycję w wykazie.”
   - Po: „Numer UN to czterocyfrowy numer identyfikujący pozycję towaru w wykazie ADR ([słowniczek](../SLOWNICZEK.md#numer-un)); w tabeli A sprawdzisz powiązane warunki przewozu ([słowniczek](../SLOWNICZEK.md#tabela-a)).”
2. **B-01 — różne rodzaje uproszczeń**
   - Przed: „LQ (…) oznacza ilości ograniczone, EQ (…) — ilości wyłączone; to inne mechanizmy niż ADR 1.1.3.6 (…)”.
   - Po: „LQ oznacza ilości ograniczone, dla których niektóre małe opakowania mogą korzystać z uproszczeń po spełnieniu limitów. EQ to osobny system dla bardzo małych ilości. ADR 1.1.3.6 to z kolei wyłączenie ilościowe, które obejmuje część wymagań tylko po sprawdzeniu właściwych limitów i obliczeniu ilości.”
3. **B-02 — kod klasyfikacyjny**
   - Przed: „kod klasyfikacyjn (oznaczenie …)y”
   - Po: „kod klasyfikacyjny (oznaczenie doprecyzowujące rodzaj zagrożenia w obrębie klasy; [słowniczek](../SLOWNICZEK.md#kod-klasyfikacyjny))”.

## Kontrola przed PR
- Zmieniono 2 lekcje; 2 główne akapity i 3 elementy listy poprawiono lub uproszczono.
- Bank: bez zmian; ID i poprawne litery bez zmian; brak nowych statusów `verified`.
- Kontrola składni lokalna w ramach odczytanej treści: uszkodzony fragment w B-02 usunięty; odsyłacze B-01 kierują do kotwic słowniczka. Pełny test `tests/test_learner_glossary.py` i Quality Gate muszą potwierdzić CI przed scaleniem.
- W tej partii nie zmieniano explanation w banku, więc wskaźnik „poprawna = jedyna najdłuższa” i długość explanation pozostają bez zmian.

## Ograniczenia
To naprawa redakcyjna, nie niezależna opinia prawna. Wątpliwości co do zastosowania konkretnych wyłączeń należy rozstrzygać na podstawie właściwego wpisu ADR 2025 i urzędowego tekstu polskiego.
