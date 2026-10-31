# Etap 4x246 — klasa 2: ochrona zaworu butli gazowej

Data: 31.10.2026. Zakres: wyłącznie kurs podstawowy ADR. Punkt wyjścia: main po scaleniu 4x245, commit `054c8a73e526ca2b81a14f099789a4cb400e1a39`, bank 670 pytań; kolejne wolne ID ADR-B-0671.

## 1. Luka pokrycia

Kompetencja ADR-B-02-K02 (klasa 2: gazy) obejmowała rozpoznawanie klasy i nalepek, w tym gazu palnego 2.1, ale nie zawierała sytuacyjnego sprawdzenia ochrony zaworu butli podczas przewozu. To ważne, ponieważ brak osobnego kapturka nie przesądza sam w sobie o niezgodności — ADR dopuszcza kilka metod zabezpieczenia.

## 2. Nowe pytanie ADR-B-0671

Kierowca widzi butlę bez osobnego kapturka na zaworze, przewożoną w ramie ochronnej. Ma sprawdzić, czy rama rzeczywiście chroni zawór przed uszkodzeniem i przypadkowym uwolnieniem gazu, zamiast automatycznie odrzucać butlę lub uznawać, że zamknięty zawór wystarczy.

| Opcja | Długość | Ocena |
|---|---:|---|
| A | 143 | Błędna — ADR nie wymaga wyłącznie metalowego kapturka; dopuszcza także inne metody ochrony. |
| B | 133 | **Poprawna** — należy ocenić, czy rama chroni zawór; przewóz w ramie jest jedną z metod wskazanych w ADR. |
| C | 129 | Błędna — zamknięcie zaworu nie zastępuje ochrony przed uderzeniem i uszkodzeniem w czasie przewozu. |

Explanation: 331 znaków, 4 zdania. Wyjaśnia, że wymagana jest ochrona zaworu, ale nie zawsze w postaci osobnego kapturka. Poprawna B nie jest najdłuższą odpowiedzią.

## 3. Podstawa prawna i ograniczenia

ADR 2025, 4.1.6.8. Zawory i elementy pozostające przy zaworze podczas przewozu muszą być odporne na uszkodzenie bez uwolnienia zawartości albo chronione przed uszkodzeniem, które mogłoby spowodować niezamierzone uwolnienie gazu. Przepis wymienia kilka rozwiązań, w tym kapturek lub osłonę, stałe zabezpieczenie, przewóz w ramie albo skrzyni ochronnej. Odniesienie do tekstu ogłoszonego: Dz.U. 2025 poz. 642; sprostowanie Dz.U. 2025 poz. 1575 pozostaje częścią zestawu źródeł kontrolnych.

Pytanie nie zakłada, że każda rama automatycznie spełnia wymagania — kierowca ma sprawdzić rzeczywistą ochronę. Literalne porównanie z wiążącym tekstem Dz.U. oraz niezależna recenzja specjalisty pozostają otwarte. Pytanie ma status `needs_review`; nie oznaczono go jako `verified`.

## 4. Kontrola banku

- Liczba pytań: 671; ID ADR-B-0001–ADR-B-0671 ciągłe i unikalne.
- Status: 671 `needs_review`, 0 `verified`.
- Blob SHA `questions.jsonl`: `8012802240554ba203baa2272adfced09b837471`.
- Rozkład poprawnych opcji: A=231, B=227, C=213.
- „Poprawna odpowiedź jest jedyną najdłuższą”: 72/671 = 10,73% (licznik bez zmian; nowa poprawna odpowiedź nie jest najdłuższa).
- Kompetencja ADR-B-02-K02 została uzupełniona o ADR-B-0671; dział ADR-B-02 ma 75 pytań.

## 5. Synchronizacja

- Warianty i klucze egzaminów próbnych 001–005 wskazują SHA aktualnego banku.
- Dodano snapshoty `review/sequential/671-671.json` i `review/legal-clauses/671-671.json`.
- Zaktualizowano ledger, manifesty pakietu recenzyjnego, kolejki priorytetowe, rejestr specjalisty, README, mapę pokrycia i testy.
- Uzupełniono lekcję ADR-B-02 i materiały instruktora o ćwiczenie z butlą w ramie ochronnej.

## 6. Wynik i bramki

Zmiana przygotowana na gałęzi `stage4x246-class2-cylinder-valve-protection`, od świeżego main. Lokalny checkout i uruchomienie testów lokalnie nie są dostępne w tym środowisku; wymagany jest PASS pełnego CI na PR przed scaleniem. Wszystkie pytania pozostają `needs_review`.
