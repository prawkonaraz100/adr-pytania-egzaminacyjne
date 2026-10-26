# Etap 4x29 — druga próbka wyjaśnień, egzamin próbny i aktualizacja pakietu recenzyjnego

- Data: 2026-10-26.
- Świeży `main` na starcie: `a98fc53093eb944133110386e412c31fb54d1826`.
- Bank blob SHA: `ed0dee6e93f21cbb758c3d088a4d02e0aaed9fc4`.
- Zakres: wyłącznie ADR podstawowy.

## 1. Weryfikacja stanu po 4x28

- Bank: 609 pytań, 609 `needs_review`, 0 `verified`.
- Słowniczek: 90 haseł; 90 unikalnych kotwic według kontroli 4x28.
- Przewodnik startowy istnieje w `podstawowy/README.md` i zawiera kolejność: lekcja → pytania działu i explanation → 3 scenariusze → egzaminy próbne 001–005.
- Raport 4x28 potwierdza brak nieistniejących i błędnie przypisanych ID w lekcjach, instruktorach i scenariuszach.
- Nie znaleziono brakującego elementu wymagającego dokończenia przed próbką 4x29.

## 2. Druga próbka 60 wyjaśnień

- Metoda: deterministyczne tasowanie wewnątrz modułu, ziarno `4292026`; ID wyłączone z próbki 4x28 (ziarno `4282026`).
- Rozkład: 5 pytań z B-01–B-08 i 4 pytania z B-09–B-13, łącznie 60.
- Ręczna ocena języka kursanta: wszystkie 60 wyjaśnień najpierw tłumaczą sens poprawnej odpowiedzi, następnie odnoszą się do mylących odpowiedzi i kończą podstawą ADR. Zakres długości: 301–454 znaków; 3–5 zdań na wyjaśnienie.
- Wyjaśnienia wymagające przepisania: **0**. Potwierdzone słabe przypadki: **0**. Nie zmieniono pytań ani statusów prawnych.
- Próbkowane ID:
  - **ADR-B-01:** ADR-B-0148, ADR-B-0041, ADR-B-0092, ADR-B-0301, ADR-B-0091
  - **ADR-B-02:** ADR-B-0097, ADR-B-0157, ADR-B-0099, ADR-B-0005, ADR-B-0317
  - **ADR-B-03:** ADR-B-0318, ADR-B-0335, ADR-B-0340, ADR-B-0276, ADR-B-0325
  - **ADR-B-04:** ADR-B-0581, ADR-B-0580, ADR-B-0474, ADR-B-0348, ADR-B-0010
  - **ADR-B-05:** ADR-B-0493, ADR-B-0230, ADR-B-0186, ADR-B-0185, ADR-B-0229
  - **ADR-B-06:** ADR-B-0051, ADR-B-0018, ADR-B-0257, ADR-B-0256, ADR-B-0132
  - **ADR-B-07:** ADR-B-0054, ADR-B-0372, ADR-B-0245, ADR-B-0477, ADR-B-0369
  - **ADR-B-08:** ADR-B-0197, ADR-B-0597, ADR-B-0485, ADR-B-0553, ADR-B-0071
  - **ADR-B-09:** ADR-B-0139, ADR-B-0292, ADR-B-0286, ADR-B-0428
  - **ADR-B-10:** ADR-B-0321, ADR-B-0388, ADR-B-0203, ADR-B-0441
  - **ADR-B-11:** ADR-B-0033, ADR-B-0490, ADR-B-0432, ADR-B-0602
  - **ADR-B-12:** ADR-B-0405, ADR-B-0213, ADR-B-0121, ADR-B-0404
  - **ADR-B-13:** ADR-B-0089, ADR-B-0601, ADR-B-0538, ADR-B-0175

## 3. Egzaminy próbne 001–005 i klucze

Arkusze i klucze porównano z aktualnym bankiem, z uwzględnieniem zmiany liter A/B/C, gdy kolejność opcji w arkuszu różni się od banku.

| Kontrola | Wynik |
|---|---:|
| Warianty sprawdzone | 5 |
| Pytań na wariant | 30 |
| Unikalne ID w zestawie 001–005 | 150 |
| Zgodność migawki banku | 5/5, blob `ed0dee6e93f21cbb758c3d088a4d02e0aaed9fc4` |
| Zgodność ID, treści, modułu i zestawu opcji | 5/5 wariantów |
| Poprawna odpowiedź po mapowaniu tekstu opcji | 5/5 wariantów |
| Explanation klucza po mapowaniu liter | 5/5 wariantów |
| Rozkład poprawnych liter | A/B/C = 10/10/10 w każdym |
| Maksymalna seria tej samej litery | 3 |
| Poprawna odpowiedź jako jedyna najdłuższa | 0/30 w każdym wariancie |

Pierwsze porównanie surowych explanation wywołało pozorny alarm dla ADR-B-0489, ponieważ litery opcji w arkuszu są przestawione. Po użyciu mapowania tekstu opcji wyjaśnienie klucza jest zgodne; nie było podstaw do zmiany klucza.

## 4. Wskaźniki banku

| Dział | Pytań | Poprawna jako jedyna najdłuższa | Wskaźnik |
|---|---:|---:|---:|
| ADR-B-01 | 45 | 6 | 13.33% |
| ADR-B-02 | 56 | 8 | 14.29% |
| ADR-B-03 | 49 | 7 | 14.29% |
| ADR-B-04 | 46 | 6 | 13.04% |
| ADR-B-05 | 43 | 6 | 13.95% |
| ADR-B-06 | 45 | 5 | 11.11% |
| ADR-B-07 | 48 | 6 | 12.50% |
| ADR-B-08 | 42 | 5 | 11.90% |
| ADR-B-09 | 46 | 4 | 8.70% |
| ADR-B-10 | 55 | 4 | 7.27% |
| ADR-B-11 | 43 | 6 | 13.95% |
| ADR-B-12 | 44 | 6 | 13.64% |
| ADR-B-13 | 47 | 4 | 8.51% |
| **Razem** | **609** | **73** | **11.99%** |

- Najkrótsze explanation w banku: 300 znaków.
- Explanation poniżej 200 znaków: 0.
- Statusy: 609 `needs_review`, 0 `verified`.
- Wskaźnik jest poniżej limitu 18% globalnie i w każdym dziale.

## 5. Pakiet recenzyjny dla specjalisty

Zaktualizowano manifest, instrukcję recenzji i przekazanie do aktualnej migawki. Stan materiałów:
- `podstawowy/questions.jsonl`: 609 pytań.
- 13 lekcji, 13 materiałów instruktorskich.
- 39 scenariuszy, po 3 na każdy dział.
- 90 haseł słowniczka.
- 5 wariantów egzaminu i 5 kluczy.
- Wszystkie pytania `needs_review`; nie nadano `verified`.

### Pozycje bez cytatu i otwarte porównania

- **121 rekordów bez zapisanego dosłownego fragmentu MI** — lista w `review/specialist/ETAP-4X24-POZYCJE-BEZ-CYTATU-MI.md`.
- **376 otwartych porównań z pełnym polskim tekstem urzędowym** — odrębna miara, nie tożsama z brakiem fragmentu MI.
- **10 rekordów** nadal wymaga dokończenia celowanego porównania.
- **609 pytań** wymaga formalnej recenzji specjalisty. Brak cytatu nie oznacza automatycznie błędu lub poprawności; nie zmieniono odpowiedzi bez potwierdzonego dowodu.

### Co sprawdzić

Specjalista powinien porównać pełne brzmienie pytania, A/B/C, klucz i explanation z ADR 2025 w Dz.U. 2025 poz. 642 oraz sprostowaniem poz. 1575, wskazując dokładny punkt, tabelę i kolumnę. Priorytetowo sprawdzić progi, wyjątki, dokumenty, warunki przewozu oraz pytania zależne od tabeli A. Wynik redakcji i PASS CI nie są zatwierdzeniem prawnym.

## 6. Interpretacja wyniku egzaminu

Do `podstawowy/egzamin-probny/README.md` dodano instrukcję: 20/30 to wyłącznie próg treningowy; po wyniku poniżej progu kursant wraca do działów z błędnymi odpowiedziami, czyta explanation, sprawdza podstawę ADR i ćwiczy trzy scenariusze przed kolejnym wariantem.

## Ograniczenia

Nie stwierdzono potwierdzonego błędu prawnego ani niezgodności klucza wymagającej zmiany. Żadne pytanie nie zostało oznaczone jako `verified`; nie rozpoczęto innego kursu.
