# Etap 4x14 — aktualizacja pakietu recenzyjnego i kontrola integralności

- Punkt wyjścia: świeży `main`, commit `385e4386bb91f026dd795acc3c1e1f04df54f1e1`.
- Zakres: kurs podstawowy ADR; bez cystern i innych specjalizacji.

## Potwierdzone rozbieżności i poprawki

1. `review/specialist/PRZEKAZANIE-ETAP4.md` opisywał w części bieżącej 542 pytania i stary indeks kończący się na 0542. Zaktualizowano nagłówek i dodano aktualny snapshot 609 pytań, 13 lekcji, 13 materiałów instruktora, 39 scenariuszy, pięciu wariantów i pięciu kluczy. Starsze sekcje oznaczono jako historyczne, zamiast usuwać historię decyzji.
2. `review/README.md` nie miało zwięzłego bieżącego stanu całego pakietu. Dodano informację o 609 pytaniach, 0 zatwierdzeniach, aktualnym indeksie i granicach historycznych audytów.
3. `review/specialist/PAKIET-0609-MANIFEST.json` wskazywał etap 4x6 mimo aktualnych artefaktów. Zmieniono etykietę etapu i dodano liczniki artefaktów: 13 lekcji, 13 materiałów instruktora, 39 scenariuszy, 5 wariantów, 5 kluczy i 90 haseł słowniczka.
4. Dodano blokujący test `tests/test_review_packet_integrity.py`, aby te rozjazdy nie wracały.

## Wynik kontroli danych

- Bank: 609 rekordów i 609 unikalnych ID; ostatnie ID `ADR-B-0609`.
- Statusy: 609 `needs_review`, 0 `verified`, 0 formalnych zatwierdzeń.
- Liczba pytań per moduł w manifeście zgadza się z bankiem dla wszystkich 13 działów.
- Indeks aktualny zawiera wszystkie 609 ID.
- Scenariusze: 39, po 3 dla każdego działu.
- Egzaminy próbne: warianty 001–005 i klucze 001–005 istnieją; test sprawdza po 30 pytań, unikalność ID w wariancie, zgodność kolejności ID z kluczem i istnienie ID w banku. Dodatkowy istniejący test wariantów sprawdza synchronizację odpowiedzi i rozkład A/B/C.
- Explanation: minimum 300 znaków; 0 poniżej 200.
- „Poprawna = jedyna najdłuższa” per dział:

| Dział | Pytania | Wskaźnik |
|---|---:|---:|
| B-01 | 45 | 15,56% |
| B-02 | 56 | 14,29% |
| B-03 | 49 | 14,29% |
| B-04 | 46 | 15,22% |
| B-05 | 43 | 13,95% |
| B-06 | 45 | 11,11% |
| B-07 | 48 | 12,50% |
| B-08 | 42 | 14,29% |
| B-09 | 46 | 8,70% |
| B-10 | 55 | 7,27% |
| B-11 | 43 | 13,95% |
| B-12 | 44 | 15,91% |
| B-13 | 47 | 8,51% |

Wszystkie działy pozostają poniżej 16%; bank nie był zmieniany w tym etapie.

## Nowy test CI

`tests/test_review_packet_integrity.py` blokuje PR, jeśli:
- liczba i statusy pytań nie zgadzają się z manifestem;
- rozkład pytań w modułach różni się od manifestu;
- aktualny indeks specjalisty nie obejmuje dokładnie wszystkich ID z banku;
- nie ma 39 scenariuszy po 3 na dział;
- brakuje jednej z 13 lekcji lub 13 kart instruktora;
- manifest nie odzwierciedla 90 haseł słowniczka;
- brakuje wariantu/klucza 001–005, wariant nie ma 30 unikalnych pytań albo kolejność ID nie zgadza się z kluczem.

Test potwierdza integralność plików i liczników, nie poprawność merytoryczną ani prawną. Nie zatwierdza pytań i nie zmienia statusów.

## Co nadal pozostaje otwarte dla specjalisty

Manifest wykazuje 599 nierozstrzygniętych porównań literalnych. Specjalista musi sprawdzić urzędowy polski tekst ADR 2025 (Dz.U. 2025 poz. 642 i sprostowanie poz. 1575), wszystkie warianty A/B/C, wyjątki, grafiki, explanation i zakres kursu. Żadna automatyczna kontrola ani PASS CI nie zastępuje podpisanej recenzji. Nie dodano fikcyjnych recenzentów, dat ani zatwierdzeń.
