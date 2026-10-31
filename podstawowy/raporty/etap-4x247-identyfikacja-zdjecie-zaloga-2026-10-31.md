# Etap 4x247 — dokument identyfikacyjny ze zdjęciem dla każdego członka załogi

Data: 31.10.2026. Zakres: wyłącznie kurs podstawowy ADR. Punkt wyjścia: main po scaleniu 4x246, commit `4f350c700361c5f529ea30e2998f88bd94af996f`, bank 671 pytań; kolejne wolne ID ADR-B-0672.

## 1. Luka pokrycia

Kompetencja ADR-B-13-K05 obejmowała cztery pytania o dokumenty i identyfikację członków załogi, ale brakowało scenariusza, w którym dokument drugiej osoby nie zawiera fotografii. To ważne, ponieważ wymóg dotyczy każdego członka załogi, a nie tylko kierowcy.

## 2. Nowe pytanie ADR-B-0672

Podczas kontroli przed wyjazdem kierowca sprawdza dokumenty załogi. Drugi członek załogi ma dokument tożsamości, ale bez fotografii. Pytanie sprawdza, czy kursant pamięta, że każdy członek załogi musi mieć przy sobie środek identyfikacji ze zdjęciem, a notatka kierowcy ani jego własny dokument nie zastępują dokumentu drugiej osoby.

| Opcja | Długość | Ocena |
|---|---:|---|
| A | 148 | Błędna — notatnik i zapisane dane nie zastępują środka identyfikacji zawierającego fotografię. |
| B | 128 | **Poprawna** — każdy członek załogi ma mieć przy sobie środek identyfikacji ze zdjęciem; brak należy uzupełnić przed przewozem. |
| C | 105 | Błędna — dokument kierowcy identyfikuje kierowcę, a nie pozostałych członków załogi. |

Explanation: 366 znaków, 4 zdania. Wyjaśnia, kogo dotyczy obowiązek, dlaczego dokument bez zdjęcia nie wystarcza i na końcu podaje podstawę ADR. Poprawna B nie jest najdłuższą odpowiedzią.

## 3. Podstawa prawna i ograniczenia

ADR 2025, 1.10.1.4 wymaga, aby każdy członek załogi pojazdu miał przy sobie podczas przewozu towarów niebezpiecznych środek identyfikacji zawierający fotografię. ADR 8.1.2.1(d) wymaga przewożenia dokumentów umożliwiających identyfikację wszystkich członków załogi, zawierających ich fotografie, w kabinie kierowcy. Odniesienie do tekstu ogłoszonego: Dz.U. 2025 poz. 642; sprostowanie Dz.U. 2025 poz. 1575 pozostaje częścią zestawu źródeł kontrolnych.

Pytanie nie rozstrzyga, jaki konkretny dokument krajowy ma zostać użyty — wymaga jedynie, by środek identyfikacji zawierał fotografię i dotyczył danej osoby. Literalne porównanie z wiążącym tekstem Dz.U. oraz niezależna recenzja specjalisty pozostają otwarte. Pytanie ma status `needs_review`; nie oznaczono go jako `verified`.

## 4. Kontrola banku

- Liczba pytań: 672; ID ADR-B-0001–ADR-B-0672 ciągłe i unikalne.
- Status: 672 `needs_review`, 0 `verified`.
- Blob SHA `questions.jsonl`: `dc499257cfae6fa8c5f5882248f676c15929c3a5`.
- Rozkład poprawnych opcji: A=231, B=228, C=213.
- „Poprawna odpowiedź jest jedyną najdłuższą”: 72/672 = 10,71% (licznik bez zmian; nowa poprawna odpowiedź nie jest najdłuższa).
- Kompetencja ADR-B-13-K05 została uzupełniona o ADR-B-0672; dział ADR-B-13 ma 49 pytań.

## 5. Synchronizacja

- Warianty i klucze egzaminów próbnych 001–005 wskazują SHA aktualnego banku.
- Dodano snapshoty `review/sequential/672-672.json` i `review/legal-clauses/672-672.json`.
- Zaktualizowano ledger, manifesty pakietu recenzyjnego, kolejki priorytetowe, rejestr specjalisty, README, mapę pokrycia i testy.
- Uzupełniono lekcję ADR-B-13 i materiały instruktora o ćwiczenie kontroli dokumentów całej załogi.

## 6. Wynik i bramki

Zmiana przygotowana na gałęzi `stage4x247-crew-photo-identification-documents`, od świeżego main. Lokalny checkout i uruchomienie testów lokalnie nie są dostępne w tym środowisku; wymagany jest PASS pełnego CI na PR przed scaleniem. Wszystkie pytania pozostają `needs_review`.
