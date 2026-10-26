# Etap 4x20 — ręczny audyt explanation ADR-B-0351–0400

- Punkt wyjścia: świeży `main` po PR #387, commit `4ee9994b26f67d069d59276056b8da4751ba7e5f`.
- Zakres: wszystkie 50 pytań ADR-B-0351–ADR-B-0400.
- Metoda: automatyczne wskazanie akronimów i ryzyk językowych, a następnie ręczna ocena dla początkującego kursanta.

## Wynik

Ręcznie sprawdzono 50/50 wyjaśnień. Przepisano 8, by rozwinąć niewyjaśnione terminy:

| ID | Zmiana |
|---|---|
| ADR-B-0367 | Numer UN jako identyfikator towaru niebezpiecznego i obowiązek prawidłowego oznakowania sztuki przesyłki. |
| ADR-B-0381 | IMDG i ICAO TI — przepisy/ instrukcje dla przewozu morskiego i lotniczego. |
| ADR-B-0382 | Rozwinięto ICAO TI, zachowując wyjaśnienie IMDG i warunków pakowania. |
| ADR-B-0383 | IMDG rozwinięto jako kodeks przewozu towarów niebezpiecznych morzem. |
| ADR-B-0386 | Rozwinięto IMDG i ICAO TI oraz ograniczenia wyjątku. |
| ADR-B-0387 | Wyjaśniono, że IMDG dotyczy oznakowania w transporcie morskim. |
| ADR-B-0388 | Rozwinięto IMDG, ICAO TI i numer UN. |
| ADR-B-0397 | ICAO TI rozwinięto jako instrukcje techniczne dla przewozu lotniczego. |

Pozostałe 42 wyjaśnienia pozostawiono bez zmian. Przykładowe fałszywe alarmy: ADR-B-0384 już wyjaśnia IMDG jako przepisy dla przewozu morskiego; ADR-B-0388 otrzymał rozwinięcia wszystkich istotnych skrótów; ADR-B-0398 wyjaśnia IMDG jako dokument dla morza i ICAO jako dokument dla lotnictwa. Nie zmieniono pytań, opcji, poprawnych liter, modułów ani statusów; wszystkie pozostają `needs_review`.

## Lista sprawdzonych ID

ADR-B-0351, ADR-B-0352, ADR-B-0353, ADR-B-0354, ADR-B-0355, ADR-B-0356, ADR-B-0357, ADR-B-0358, ADR-B-0359, ADR-B-0360, ADR-B-0361, ADR-B-0362, ADR-B-0363, ADR-B-0364, ADR-B-0365, ADR-B-0366, ADR-B-0367, ADR-B-0368, ADR-B-0369, ADR-B-0370, ADR-B-0371, ADR-B-0372, ADR-B-0373, ADR-B-0374, ADR-B-0375, ADR-B-0376, ADR-B-0377, ADR-B-0378, ADR-B-0379, ADR-B-0380, ADR-B-0381, ADR-B-0382, ADR-B-0383, ADR-B-0384, ADR-B-0385, ADR-B-0386, ADR-B-0387, ADR-B-0388, ADR-B-0389, ADR-B-0390, ADR-B-0391, ADR-B-0392, ADR-B-0393, ADR-B-0394, ADR-B-0395, ADR-B-0396, ADR-B-0397, ADR-B-0398, ADR-B-0399, ADR-B-0400

## Kontrola wskaźników

- Bank: 609 pytań; duplikaty ID: 0.
- Explanation poniżej 200 znaków: 0; najkrótsze: 300 znaków.
- Wszystkie zmienione explanation mają 200–500 znaków i 3–5 zdań.
- Poprawna odpowiedź jako jedyna najdłuższa: 73/609 = 11.99%.
- Wskaźnik per dział:
  - ADR-B-01: 6/45 = 13.33%
  - ADR-B-02: 8/56 = 14.29%
  - ADR-B-03: 7/49 = 14.29%
  - ADR-B-04: 6/46 = 13.04%
  - ADR-B-05: 6/43 = 13.95%
  - ADR-B-06: 5/45 = 11.11%
  - ADR-B-07: 6/48 = 12.5%
  - ADR-B-08: 5/42 = 11.9%
  - ADR-B-09: 4/46 = 8.7%
  - ADR-B-10: 4/55 = 7.27%
  - ADR-B-11: 6/43 = 13.95%
  - ADR-B-12: 6/44 = 13.64%
  - ADR-B-13: 4/47 = 8.51%

## Synchronizacja audytu i egzaminów

Zsynchronizowano snapshoty dla zmienionych rekordów w `review/sequential/363-380.json`, `review/sequential/381-398.json` oraz odpowiednich plikach `review/legal-clauses`. Odświeżono `source_bank_head` w wariantach i kluczach 001–005 oraz wyjaśnienia w kluczach. Warianty zachowują 30 pytań każdy, unikalność między wariantami, rozkład A/B/C = 10/10/10 i maksymalną serię tej samej litery 1.

## Ograniczenia

To przegląd językowy, nie formalna akceptacja prawna. Żadnego pytania nie oznaczono jako `verified`.
