# Etap 4x244 — klasa 7: przypisanie kategorii przesyłki na podstawie TI i poziomu promieniowania

Data: 31.10.2026. Zakres: wyłącznie kurs podstawowy ADR. Punkt wyjścia: świeży main `6a3f05ff2cee7c1e031ba9c9dedc787fa7f6c7c5`, 668 pytań; następne wolne ID ADR-B-0669.

## 1. Luka pokrycia

Kompetencja ADR-B-02-K11 dotyczy podstawowego rozpoznawania materiałów promieniotwórczych klasy 7. Dotychczasowe pytania obejmowały identyfikację klasy, podstawy kryteriów i ograniczenia uprawnień, ale brakowało sytuacyjnego zastosowania zasady, że kategorię przesyłki ustala się z uwzględnieniem zarówno wskaźnika transportowego (TI), jak i maksymalnego poziomu promieniowania na powierzchni opakowania.

## 2. Nowe pytanie ADR-B-0669

Podczas odbioru przesyłki klasy 7 dokument podaje TI 0,8, a maksymalny poziom promieniowania na powierzchni opakowania wynosi 0,7 mSv/h. Kursant ma odczytać oba kryteria z tabeli 5.1.5.3.4 i wybrać kategorię wyższą w przypadku rozbieżności.

| Opcja | Długość | Ocena |
|---|---:|---|
| A | 145 | Błędna — TI 0,8 mieści się w przedziale II-YELLOW, ale nie rozstrzyga samodzielnie o kategorii. |
| B | 130 | **Poprawna** — poziom 0,7 mSv/h odpowiada III-YELLOW; przy różnych wynikach przypisuje się kategorię wyższą. |
| C | 115 | Błędna — I-WHITE wymaga TI równego zero oraz poziomu na powierzchni nie większego niż 0,005 mSv/h. |

Explanation: 340 znaków, 4 zdania. Najpierw wyjaśnia praktyczny sens obu kryteriów, następnie pułapki dystraktorów, a na końcu podaje podstawę ADR. Poprawna B nie jest najdłuższą odpowiedzią.

## 3. Podstawa prawna i ograniczenia

ADR 2025, 5.1.5.3.4(a) i tabela 5.1.5.3.4. Przy TI 0,8 zakres wskazuje II-YELLOW; poziom promieniowania 0,7 mSv/h na powierzchni wskazuje III-YELLOW. Przepis wymaga uwzględnienia obu warunków i przypisania kategorii wyższej, jeżeli wskazują różne kategorie. Odniesienie do tekstu ogłoszonego: Dz.U. 2025 poz. 642. Sprostowanie Dz.U. 2025 poz. 1575 pozostaje częścią zestawu źródeł kontrolnych.

Wyszukiwalna kopia ADR 2025 i źródła pomocnicze nie zastępują literalnego porównania z wiążącym polskim tekstem Dz.U. oraz niezależnej recenzji specjalisty. Te kontrole pozostają otwarte. Pytanie ma status `needs_review`; nie oznaczono go jako `verified`.

## 4. Kontrola banku

- Liczba pytań: 669; ID ADR-B-0001–ADR-B-0669 ciągłe i unikalne.
- Status: 669 `needs_review`, 0 `verified`.
- Blob SHA `questions.jsonl`: `fa0d2c28445e6b8a9ca0cca533944766a41f8c43`.
- Rozkład poprawnych opcji: A=231, B=225, C=213.
- „Poprawna odpowiedź jest jedyną najdłuższą”: 72/669 = 10,76% (licznik bez zmian; nowa poprawna odpowiedź nie jest najdłuższa).
- Kompetencja ADR-B-02-K11 została uzupełniona o ADR-B-0669; dział ADR-B-02 ma 73 pytania.

## 5. Synchronizacja po pułapce #646

- Warianty i klucze egzaminów próbnych 001–005 wskazują SHA aktualnego banku.
- Dodano snapshoty `review/sequential/669-669.json` i `review/legal-clauses/669-669.json`.
- Zaktualizowano ledger literalnej kontroli, manifesty pakietu recenzyjnego, kolejki priorytetowe, rejestr specjalisty, README, mapę pokrycia i testy liczebności.
- Uzupełniono lekcję ADR-B-02 i materiały instruktora o ćwiczenie z dwoma kryteriami kategorii.

## 6. Wynik i dalsze bramki

Zmiana została przygotowana na gałęzi `stage4x244-class7-radioactive-transport-index`, nie na `main`. Lokalny checkout i uruchomienie Quality Gate lokalnie nie są dostępne w tym środowisku; wymagane jest potwierdzenie przez CI na PR. Nie należy uznawać etapu za zakończony ani scalać PR, dopóki wymagane kontrole CI nie zakończą się PASS.

Zakres pozostaje ograniczony do kursu podstawowego ADR. Wszystkie pytania zachowują status `needs_review`.
