# Etap 4x245 — klasa 6.1: uszkodzone opakowanie i ryzyko narażenia na materiał trujący

Data: 31.10.2026. Zakres: wyłącznie kurs podstawowy ADR. Punkt wyjścia: main po scaleniu 4x244, commit `1dd049d8e9a38e9580b311c06aa03e8aa72c86d1`, bank 669 pytań; kolejne wolne ID ADR-B-0670.

## 1. Luka pokrycia

Kompetencja ADR-B-02-K09 (klasa 6.1: materiały trujące) miała cztery pytania: rozpoznanie klasy, nalepki i ogólnego zagrożenia. Brakowało scenariusza decyzji kierowcy podczas rozładunku, gdy uszkodzone opakowanie uwalnia materiał w postaci proszku, a pracownik chce go samodzielnie sprzątać.

## 2. Nowe pytanie ADR-B-0670

Kursant ma rozpoznać, że materiały klasy 6.1 mogą szkodzić przez wdychanie, kontakt ze skórą lub połknięcie. Przy rozsypaniu z uszkodzonego opakowania nie należy dotykać ani zamiatać substancji, lecz oddalić się, ostrzec innych i wykonać instrukcje pisemne oraz procedurę awaryjną.

| Opcja | Długość | Ocena |
|---|---:|---|
| A | 125 | Błędna — zamiatanie i przenoszenie rozsypanej substancji naraża na kontakt z pyłem; zwykłe rękawice nie wystarczają. |
| B | 130 | **Poprawna** — nie dotykać ani nie sprzątać wycieku, oddalić się, ostrzec innych i zastosować instrukcje pisemne. |
| C | 134 | Błędna — spłukiwanie do odpływu może rozprzestrzenić skażenie; rozcieńczanie nie jest decyzją kierowcy. |

Explanation: 382 znaki, 4 zdania. Wyjaśnia praktyczne zagrożenie, odrzuca niebezpieczne pomysły sprzątania i podaje podstawę ADR. Poprawna B nie jest najdłuższą odpowiedzią.

## 3. Podstawa prawna i ograniczenia

ADR 2025, 2.2.61.1.1 określa klasę 6.1 jako materiały, które mogą szkodzić zdrowiu lub powodować śmierć przez wdychanie, absorpcję przez skórę lub połknięcie. ADR 5.4.3.4 zawiera instrukcje pisemne dla załogi na wypadek awarii lub wypadku. Odniesienie do tekstu ogłoszonego: Dz.U. 2025 poz. 642; sprostowanie Dz.U. 2025 poz. 1575 pozostaje częścią zestawu źródeł kontrolnych.

Pytanie nie instruuje kierowcy do samodzielnego używania sprzętu ochronnego ani sprzątania wycieku. Pełne literalne porównanie z wiążącym polskim tekstem Dz.U. oraz niezależna recenzja specjalisty pozostają otwarte. Pytanie ma status `needs_review`; nie oznaczono go jako `verified`.

## 4. Kontrola banku

- Liczba pytań: 670; ID ADR-B-0001–ADR-B-0670 ciągłe i unikalne.
- Status: 670 `needs_review`, 0 `verified`.
- Blob SHA `questions.jsonl`: `d4e74d64dc557d9c93e59bde4772bc7a972a92ae`.
- Rozkład poprawnych opcji: A=231, B=226, C=213.
- „Poprawna odpowiedź jest jedyną najdłuższą”: 72/670 = 10,75% (licznik bez zmian; nowa poprawna odpowiedź nie jest najdłuższa).
- Kompetencja ADR-B-02-K09 została uzupełniona o ADR-B-0670; dział ADR-B-02 ma 74 pytania.

## 5. Synchronizacja

- Warianty i klucze egzaminów próbnych 001–005 wskazują SHA aktualnego banku.
- Dodano snapshoty `review/sequential/670-670.json` i `review/legal-clauses/670-670.json`.
- Zaktualizowano ledger, manifesty pakietu recenzyjnego, kolejki priorytetowe, rejestr specjalisty, README, mapę pokrycia i testy.
- Uzupełniono lekcję ADR-B-02 i materiały instruktora o ćwiczenie z uszkodzonym opakowaniem klasy 6.1.

## 6. Wynik i bramki

Zmiana przygotowana na gałęzi `stage4x245-class61-toxic-spill-safety`, od świeżego main. Lokalny checkout i uruchomienie testów lokalnie nie są dostępne w tym środowisku; wymagany jest PASS pełnego CI na PR przed scaleniem. Wszystkie pytania pozostają `needs_review`.
