# Etap 4x248 — bateria litowo-jonowa zapakowana razem z urządzeniem (UN 3481)

Data: 31.10.2026. Zakres: wyłącznie kurs podstawowy ADR. Punkt wyjścia: świeży main po scaleniu PR #716, commit `8d61832307e5ba9220bd8191c34f21d52ee3be3c`, bank 672 pytań. Kolejne wolne ID: ADR-B-0673.

## 1. Luka pokrycia

Kompetencja ADR-B-02-K13 (klasa 9 i 9A) miała siedem pytań. Większość dotyczyła baterii sodowo-jonowych UN 3551/3552, badań 38.3 i ogólnego rozpoznania nalepki 9A. Pytanie o baterie litowe wspominało je tylko łącznie z sodowo-jonowymi. Brakowało praktycznego rozróżnienia numerów UN dla baterii litowo-jonowej przewożonej samodzielnie i zapakowanej z urządzeniem, które zasila.

Przegląd dziennika Issue #10 dla etapów 4x227–4x247 nie wykazał wcześniejszego etapu poświęconego temu konkretnemu rozróżnieniu. Wybór dotyczy więc wąskiego, niepokrytego przypadku, a nie ponownego opracowania ogólnej klasy 9.

## 2. Nowe pytanie ADR-B-0673

Scenariusz: w opakowaniu z wiertarką znajduje się zapasowa bateria litowo-jonowa przeznaczona do zasilania tego urządzenia. Kursant ma wybrać właściwy numer UN.

| Opcja | Długość | Ocena |
|---|---:|---|
| A | 136 | Błędna — UN 3480 dotyczy baterii litowo-jonowej przewożonej bez urządzenia; bateria zapakowana z urządzeniem, które zasila, nie jest w tej sytuacji przewożona samodzielnie. |
| B | 134 | **Poprawna** — UN 3481 obejmuje baterię litowo-jonową zawartą w urządzeniu lub zapakowaną z urządzeniem, które zasila. |
| C | 109 | Błędna — UN 3091 dotyczy baterii z litem metalicznym z urządzeniem, a nie baterii litowo-jonowej. |

Explanation: 423 znaki, 4 zdania. Najpierw wyjaśnia wybór UN 3481, potem rozróżnia UN 3480 i UN 3091, wskazuje praktyczną kontrolę dokumentów i kończy podstawą ADR. Poprawna B nie jest najdłuższą odpowiedzią.

## 3. Podstawa prawna i zakres pytania

- ADR 2025, 2.2.9.1.7.1 — przepisy dotyczące baterii litowych.
- Dział 3.2, tabela A — odrębne pozycje UN 3480 (baterie litowo-jonowe przewożone samodzielnie) i UN 3481 (baterie litowo-jonowe zawarte w urządzeniu lub zapakowane z urządzeniem); UN 3090/3091 odnoszą się do litu metalicznego.
- ADR 5.2.1.9.2 — oznakowanie baterii litowych i wskazanie właściwego numeru UN, w tym dla baterii zawartych w urządzeniu lub zapakowanych z nim.

Odniesienie do źródła prawa: Dz.U. 2025 poz. 642. Sprawdzono odpowiednie brzmienie w polskim ADR 2025 udostępnionym przez Ministerstwo Infrastruktury: 2.2.9.1.7.1 oraz 5.2.1.9.2. Ministerstwo wyraźnie zastrzega, że udostępnione pliki mają charakter pomocniczy, a źródłem prawa jest ADR ogłoszony w Dzienniku Ustaw. Dlatego literalne porównanie wszystkich zdań i opcji z wiążącym tekstem Dz.U. pozostaje otwarte. W pytaniu przyjęto, że bateria jest litowo-jonowa i jest zapakowana razem z urządzeniem, które zasila; nie rozstrzyga ono, czy spełnione są wszystkie warunki wyłączenia SP 188, kompletności opakowania lub pozostałe wymagania przewozowe. Te kwestie wymagają odrębnego sprawdzenia właściwego wpisu, przepisu szczególnego i instrukcji pakowania.

Literalne porównanie każdego zdania i opcji z właściwymi stronami wiążącego tekstu Dz.U. oraz niezależna recenzja specjalisty pozostają otwarte. Pytanie ma status `needs_review`; nie oznaczono go jako `verified`.

## 4. Kontrola banku

- Liczba pytań: 673; ID ADR-B-0001–ADR-B-0673 ciągłe i unikalne.
- Status: 673 `needs_review`, 0 `verified`.
- Blob SHA `questions.jsonl`: `0ff923d6a491bf134d36a9efe9a4f9bea82eb431`.
- Rozkład poprawnych opcji: A=231, B=229, C=213.
- „Poprawna odpowiedź jest jedyną najdłuższą”: 72/673 = 10,70%; maksimum działu 13,95%.
- Kompetencja ADR-B-02-K13 została uzupełniona o ADR-B-0673; dział ADR-B-02 ma 76 pytań.

## 5. Synchronizacja i kontrole

- Warianty i klucze egzaminów próbnych 001–005 wskazują SHA aktualnego banku.
- Dodano snapshoty `review/sequential/673-673.json` i `review/legal-clauses/673-673.json`.
- Dodano ADR-B-0673 do ledgeru literalnej weryfikacji i rejestru specjalisty.
- Zaktualizowano manifesty pakietu recenzyjnego, kolejki, README, mapę pokrycia, lekcję, materiały instruktora i testy regresyjne.
- Zachowano wszystkie pytania jako `needs_review`; brak zgody na oznaczenie `verified`.

Zmiana jest przygotowana na gałęzi `stage4x248-lithium-battery-un3481-equipment`, utworzonej od świeżego main. Lokalny checkout nie był dostępny, więc testy zostaną potwierdzone przez pełny Quality Gate w GitHub Actions na PR. Nie scalaj bez PASS.
