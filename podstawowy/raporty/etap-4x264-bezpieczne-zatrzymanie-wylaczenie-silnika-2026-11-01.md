# Etap 4x264 — bezpieczne zatrzymanie i odłączenie akumulatora

Data: 01.11.2026  
Zakres: wyłącznie kurs podstawowy ADR  
Baza: main `d88c323f103a25fddd6f0cd08201bf0d03464141`  
Gałąź: `stage4x264-engine-shutdown-scenario`  
Nowe ID: `ADR-B-0690`  
Kompetencja: `ADR-B-05-K02` — bezpieczne zatrzymanie i wyłączenie silnika

## Wybór luki

Kompetencja miała cztery pytania. Wcześniejsze pozycje w znacznej części sprawdzały odtworzenie pojedynczych czynności z instrukcji pisemnych. Nowe pytanie sprawdza decyzję kierowcy w konkretnej sytuacji: pojazd stoi już bezpiecznie, silnik nadal pracuje, a wyłącznik główny akumulatora jest dostępny. To rozróżnia wyłączenie silnika od dodatkowego odłączenia akumulatora.

## Dodane pytanie

- `ADR-B-0690`: awaria, bezpieczne zatrzymanie pojazdu, dostępny wyłącznik główny akumulatora.
- Klucz: **C** — zastosować hamulec, wyłączyć silnik i użyć wyłącznika głównego akumulatora, jeśli jest dostępny.
- Explanation: **424 znaki, 4 zdania**; najpierw praktyczny sens prawidłowej czynności, następnie wyjaśnienie błędnych wariantów i podstawa ADR.
- Długości A/B/C: **103/77/96** znaków; poprawna C nie jest ani najdłuższa, ani najkrótsza.
- Audyt odpowiedzi: A — błędna (pozostawienie pracującego silnika i uruchamianie odbiorników); B — błędna (pomija dostępny wyłącznik główny); C — poprawna (odpowiada modelowi instrukcji pisemnych).
- Status: `needs_review`; nic nie oznaczono jako `verified`.

## Podstawa prawna

- **ADR 2025, 5.4.3.4** — model instrukcji pisemnych: w razie wypadku lub awarii, gdy jest to bezpieczne i wykonalne, załoga stosuje hamulec, wyłącza silnik i odłącza akumulator przez uruchomienie wyłącznika głównego, jeśli jest dostępny.
- Dz.U. 2025 poz. 642: https://dziennikustaw.gov.pl/DU/2025/642
- Oficjalny polski tekst ADR 2025, tom II, Ministerstwo Infrastruktury: https://www.gov.pl/attachment/b7292c03-ac9d-4f80-9a29-c22f53d847b8
- UNECE ADR 2025: https://unece.org/adr-2025-files

Zakres pytania ogranicza się do standardowego modelu instrukcji pisemnych. Sformułowanie „jeśli jest dostępny” oraz warunek bezpieczeństwa i wykonalności są zachowane. Nie sugeruje się ręcznego odłączania przewodów akumulatora. Pełne literalne porównanie z właściwym tekstem Dz.U. oraz niezależna recenzja specjalisty pozostają pending.

## Synchronizacja #646

- Bank po dodaniu: **690** pytań, ADR-B-0001–0690; SHA `66a862742a9c134f92bf467574865101faa0c884`; rozkład kluczy A/B/C: **236/236/218**; poprawna = jedyna najdłuższa: **72/690 = 10,43%**; wszystkie mają pozostać `needs_review`, 0 `verified`.
- Kompetencja `ADR-B-05-K02` otrzymała piąte pytanie.
- Klucze i warianty egzaminów próbnych 001–005 wymagają odświeżenia do nowego SHA banku.
- Dodano snapshoty `review/sequential/690-690.json` i `review/legal-clauses/690-690.json`.
- Rozkład długości odpowiedzi dla nowego pytania: A=103/B=77/C=96.
- Quality Gate i pełne CI pozostają do potwierdzenia na PR; lokalnego Quality Gate nie uruchamiano.

## Audyt A/B/C

| Opcja | Ocena | Uzasadnienie |
|---|---|---|
| A | Błędna | Pozostawienie pracującego silnika i uruchamianie dodatkowych odbiorników nie odpowiada instrukcji i może wprowadzać źródła zapłonu. |
| B | Błędna | Samo wyłączenie silnika pomija odłączenie akumulatora wyłącznikiem głównym, gdy jest dostępny. |
| C | Poprawna | Odtwarza pierwszą czynność z modelu: hamulec, wyłączenie silnika i wyłącznik główny akumulatora. |

Raport nie stanowi niezależnej akceptacji prawnej ani zatwierdzenia pytania.
