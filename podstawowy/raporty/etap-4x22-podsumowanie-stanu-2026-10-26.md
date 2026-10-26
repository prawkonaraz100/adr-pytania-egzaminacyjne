# Etap 4x22 — podsumowanie stanu dowodów literalnych

- Data: 2026-10-26.
- Punkt wyjścia: `main` commit `00aad2916cf20a45883b63dd2cd804c19753b2ac`.
- Zakres wyłącznie: kurs podstawowy ADR; brak prac nad cysternami lub innymi kursami.

## 1. Sprostowanie Dz.U. 2025 poz. 1575

Raport `podstawowy/raporty/etap-4x22-sprostowanie-1575-2026-10-26.md` zawiera listę 17 korekt/punktów z oficjalnego sprostowania oraz porównanie z bankiem i ledgerem. Przejrzano 609 rekordów. Cztery pytania bezpośrednio powiązane z wpisem UN 3551 to ADR-B-0162, ADR-B-0315, ADR-B-0499 i ADR-B-0501. Nie wykryto potwierdzonej sprzeczności wymagającej zmiany pytania, odpowiedzi lub explanation.

Źródła:
- [Dz.U. 2025 poz. 1575 — oficjalny tekst sprostowania](https://eli.gov.pl/api/acts/DU/2025/1575/text.pdf)
- [Dz.U. 2025 poz. 642 — tekst ADR](https://dziennikustaw.gov.pl/DU/2025/642)
- [MI ADR 2025 tom I PL — kopia pomocnicza](https://www.gov.pl/attachment/8856b22a-bfd8-4567-8386-b9709bba8da7)
- [MI ADR 2025 tom II PL — kopia pomocnicza](https://www.gov.pl/attachment/b7292c03-ac9d-4f80-9a29-c22f53d847b8)

## 2. Liczniki ledgeru po partiach

| Miara | Stan |
|---|---:|
| Rekordy banku / ledgeru | 609 |
| Rekordy z polem `literal_evidence` | 187 |
| Rekordy z `literal_comparison_result` | 291 |
| Rekordy bez `literal_comparison_result` | 318 |
| Wśród 318 otwartych: mają cytat MI, ale nadal oczekują porównania | 51 |
| Wśród 318 otwartych: nadal bez literalnego cytatu | 267 |
| Spośród 267 bez cytatu: konkretna blokada pobrania zapisana | 72 |
| Spośród 267 bez cytatu: jeszcze bez indywidualnej próby pobrania zapisanej w ledgerze | 195 |
| Rekordy z dokładną stroną PDF Dz.U. 2025 poz. 642 potwierdzoną w ledgerze | 0 |
| Rekordy oznaczone `verified` | 0 |
| Potwierdzone zmiany pytań/kluczy w etapie 4x22 | 0 |

## 3. Partie zrealizowane i CI

- **PR #407 — sprostowanie poz. 1575:** lista korekt, audyt 609 rekordów, aktualizacja ledgeru; PASS CI.
- **PR #408 — partia 0001–0040:** 40 wpisów z cytatami z kopii MI; PASS CI.
- **PR #409 — partia 0041–0071:** 31 wpisów z cytatami z kopii MI; PASS CI.
- **PR #410 — partia 0072–0111:** 40 wpisów z cytatami z kopii MI; PASS CI.
- **PR #411 — partia 0112–0151:** 8 cytatów i 32 szczegółowe blokady pobrania; PASS CI.
- **PR #412 — partia 0152–0191:** 40 szczegółowych blokad pobrania; PASS CI.

Łącznie w etapie 4x22 dodano **119 nowych wpisów z literalnymi fragmentami MI**. Dodatkowo zapisano 72 rekordy z konkretnymi przyczynami braku pobranego cytatu w dwóch ostatnich partiach. Nie dopisywano cytatów z pamięci i nie zgadywano numerów stron.

## 4. Co pozostaje otwarte

Etap 4x22 **nie jest zakończony**. Z 318 rekordów bez wyniku porównania 267 nadal nie ma literalnego cytatu, a 51 ma fragment z kopii MI, ale nie ma potwierdzonego mapowania do strony prawnie wiążącego Dz.U. 2025 poz. 642. Dla żadnego cytatu nie zapisano potwierdzonej strony pliku Dz.U.; paginacji kopii MI nie przenoszono na Dziennik Ustaw.

Z 267 rekordów bez cytatu, dla 72 zapisano konkretną blokadę i następny krok; dla pozostałych 195 ledger nadal wymaga indywidualnej próby pobrania oraz albo cytatu, albo konkretnego powodu niepowodzenia. Nie należy traktować ich jako sprawdzonych.

Dalsze partie muszą najpierw odzyskać właściwe strony źródłowe dla progów liczbowych i wyjątków, w szczególności:
- ADR 5.2.1.8.1 i 5.3.6.2 — progi i wymiary oznakowania środowiskowego;
- ADR 1.10.3.1.2 — tabela towarów dużego ryzyka i przypisy;
- ADR 2.1.3.5.3–2.1.3.5.5 — wyjątki i warunki klasyfikacji odpadów;
- ADR 5.4.2 — certyfikat pakowania kontenera/pojazdu;
- pozostałe rekordy, których exact text/page jest wskazany w `stage4x22_source_attempt`.

Nie należy deklarować sukcesu całego etapu ani zatwierdzać pytań, dopóki te dowody nie zostaną uzyskane i porównane z urzędowym tekstem. Wszystkie pytania pozostają `needs_review`; niezależna akceptacja specjalisty nadal jest wymagana.


## Aktualizacja po partii 0192–0231

- Świeży `main` na wejściu: `502a39482a2545d4d03ffb8146e51c49f8bed754`.
- Sprawdzono 40 rekordów. 31 miało już wynik porównania; 9 nadal nie ma wyniku urzędowego porównania.
- Dla 9 otwartych rekordów zapisano konkretną próbę źródłową i następny krok. W 3 przypadkach zachowano cytat z MI jako materiał pomocniczy; w ADR-B-0204 skorygowano parafrazę do brzmienia znalezionego w pomocniczym tekście MI.
- Bezpośredni PDF ELI oraz wybrane podzielone skany nie dały się odczytać przez limit treści/timeout. **Nie odnaleziono żadnej strony PDF Dz.U.**; nie przenoszono paginacji MI na Dz.U.
- Nie stwierdzono potwierdzonej rozbieżności z tekstem wiążącym, bo porównanie z tym tekstem pozostaje zablokowane. Brak zmian pytań/kluczy; 0 `verified`.
- Szczegóły: `podstawowy/raporty/etap-4x22-literalne-dowody-0192-0231-2026-10-26.md` oraz `review/batches/stage4x22-literal-0192-0231.json`.


## Aktualizacja po partii 0232–0271

- Świeży `main` na wejściu: `463c94d720d7fca71540895612bb8b9f396095c1`.
- Przejrzano 40 rekordów; 29 miało już wynik, 11 nadal oczekuje na urzędowe porównanie.
- Dla wszystkich 11 otwartych rekordów zapisano indywidualną przyczynę i następny krok. Trzy mają cytat z pomocniczego tekstu MI, ale bez strony Dz.U.; osiem nie ma cytatu.
- Strony PDF Dz.U. znalezione: 0; nie przypisywano stron z paginacji MI. Brak potwierdzonych poprawek pytań/kluczy; statusy pozostają `needs_review`.
- Raport: `podstawowy/raporty/etap-4x22-literalne-dowody-0232-0271-2026-10-26.md`; rejestr: `review/batches/stage4x22-literal-0232-0271.json`.
