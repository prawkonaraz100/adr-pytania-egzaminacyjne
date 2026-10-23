# Etap 3 — instrukcja odbioru i bezpieczny egzamin próbny

Data: 23.10.2026. **Stan: projekt do zatwierdzenia.** Liczba szkiców: 324; status `needs_review`, 0 `verified`.

## Kolejność pracy specjalisty ADR

1. Otworzyć `review/REJESTR-RECENZJI-ETAP3.md` i po kolei każdą pozycję `podstawowy/questions.jsonl`.
2. Dla każdej pozycji porównać wszystkie warianty A/B/C, klucz, zakres wyłączeń, liczby, kod tunelowy, rodzaj dokumentacji oraz odpowiedni przepis z Dz.U. 2025 poz. 642, sprostowaniem poz. 1575 i mającymi zastosowanie odstępstwami.
3. Zwłaszcza dla ADR-B-01 (1.1.3.6), 05 (awarie), 06 (oznakowanie), 08 (wyposażenie), 09 (wspólny załadunek), 10 (multimodalność), 11 (tunele), 13 (dokumenty) ocenić rozwiązywanie sytuacji, nie tylko pamięć definicji.
4. Dla P1–P3 dokonać **oddzielnego** odbioru merytorycznego scenariuszy przez instruktora; ich przeprowadzenie i zaliczenie wymaga rzeczywistych zajęć, a nie testu tekstowego.
5. Udokumentować realny wynik w `review/reports/<ID>.md`; po zaakceptowaniu treści dołączyć wymagane pola, zgodne SHA i kwalifikowaną akceptację według `review/README.md`. Nie zatwierdzać automatycznie.

## Egzamin próbny — specyfikacja, bez publikacji pytań niezatwierdzonych

- Format projektowy zgodny z opublikowanymi zasadami egzaminu podstawowego: **30 pytań, 60 minut, próg 20 poprawnych**; potwierdzić szczegóły przed wdrożeniem według obowiązującego rozporządzenia egzaminacyjnego oraz zmian ADR 2025.
- Generator produkcyjny pobiera **wyłącznie** zatwierdzone i niezmienione rekordy z `scripts/release_gate.py` po aktualnej kontroli — gdy liczba zatwierdzonych jest za mała lub nie ma reprezentacji 13 działów, egzamin pozostaje `BLOCKED`.
- Projektowany rozkład do weryfikacji: działy 01–13: `[3,4,2,2,3,2,2,3,3,1,2,1,2]` = 30. **To autorska propozycja dydaktyczna, nie urzędowe proporcje.** Losowanie bez powtórzeń identyfikatorów, jedna prawidłowa odpowiedź, odłożone wyjaśnienie po zakończeniu testu. Potrzebna wersja awaryjna, gdy pula działu jest za mała — nigdy nie uzupełniać jej `needs_review`.
- Testy developerskie można przeprowadzać wyłącznie na syntetycznych danych testowych; nie mieszać ich z prawdziwym bankiem i nie wypuszczać niezatwierdzonych pytań publicznie.

## Końcowy przegląd spójności — otwarte bramki

| Obszar | Stan | Kryterium zamknięcia |
|---|---|---|
| Schemat danych, CI, audyty | 8/8 PASS dla PR #73 | Potwierdzenie na finalnym HEAD po wszystkich zmianach |
| Minimalna liczba na kompetencję teorii | 103/103 ma co najmniej 3 szkice | Indywidualna ocena zróżnicowania i poprawności prawnej |
| Lekcje | 13 szkiców po PR #72 | Recenzja treści i przykładów przez eksperta |
| P1–P3 | Scenariusze istnieją | Odbiór instruktorski i faktyczne wykonanie zajęć |
| Recenzja 324 pytań | 0 verified | 324 rozstrzygnięcia z zapisanymi dowodami, poprawki ponownie kontrolowane |
| Egzamin produkcyjny | BLOCKED | 30+ zatwierdzonych pytań ze wszystkich 13 działów i ważna bramka wydania |
| Pozostałe kursy | Nierozpoczęte | Po zakończeniu kursu podstawowego |

Żadnego statusu `verified` nie przypisywano w tym dokumencie. To pakiet przekazania do rzeczywistej recenzji, a nie deklaracja ukończenia kursu.
