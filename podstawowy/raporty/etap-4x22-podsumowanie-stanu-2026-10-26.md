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


## Aktualizacja po partii 0272–0311

- Świeży `main` na wejściu: `07b79ea6c693aa4bd4057093390e0d6ba7c6f78c`.
- Sprawdzono 40 rekordów; 30 miało już wynik, 10 nadal oczekuje na urzędowe porównanie.
- Dla 10 otwartych rekordów zapisano przyczynę i następny krok. Dwa mają cytaty pomocnicze MI; dla ADR-B-0278 poprawiono parafrazę do dokładnego tekstu MI. Strony Dz.U. nie potwierdzono.
- Nie znaleziono urzędowych stron PDF i nie zmieniono pytań/kluczy; 0 `verified`.
- Raport: `podstawowy/raporty/etap-4x22-literalne-dowody-0272-0311-2026-10-26.md`; rejestr: `review/batches/stage4x22-literal-0272-0311.json`.


## Aktualizacja po partii 0312–0351

- Świeży `main` na wejściu: `0d8b5560e76c7f22d837bca191cb4785bfd186c5`.
- Przejrzano 40 rekordów; 11 miało już wynik, 29 nadal oczekuje na urzędowe porównanie.
- Dla wszystkich 29 otwartych rekordów zapisano konkretny powód blokady i następny krok. Zakres obejmuje m.in. klasyfikację odpadów, UN 3551, klasę 7, pojazdy EX/II/EX/III, wspólny załadunek i nadzór postoju.
- Strony PDF Dz.U. znalezione: 0; nie zmieniono pytań/kluczy i nie nadano `verified`.
- Raport: `podstawowy/raporty/etap-4x22-literalne-dowody-0312-0351-2026-10-26.md`; rejestr: `review/batches/stage4x22-literal-0312-0351.json`.


## Aktualizacja po partii 0352–0391

- Świeży `main` na wejściu: `6d9ef1b5be1482407375caf41b3a4e2832c50dc1`.
- Sprawdzono 40 rekordów; 8 miało już wynik, 32 nadal oczekują na urzędowe porównanie.
- Wśród otwartych 7 ma cytaty z pomocniczego tekstu MI, ale 25 nie ma cytatu. Dla wszystkich 32 zapisano przyczynę i następny krok.
- Nie odnaleziono stron PDF Dz.U.; brak potwierdzonych zmian pytań/kluczy, 0 `verified`.
- Raport: `podstawowy/raporty/etap-4x22-literalne-dowody-0352-0391-2026-10-26.md`; rejestr: `review/batches/stage4x22-literal-0352-0391.json`.


## Aktualizacja po partii 0392–0431

- Świeży `main` na wejściu: `0559bed79d4f1f918208dc989350ab5e303d1a34`.
- Sprawdzono 40 rekordów; 4 miały już wynik, 36 nadal oczekuje na urzędowe porównanie.
- Wśród otwartych 9 ma cytaty pomocnicze MI, a 27 nie ma cytatu; dla wszystkich 36 zapisano przyczynę i następny krok.
- Strony PDF Dz.U. potwierdzone: 0; brak potwierdzonych zmian pytań/kluczy i 0 `verified`.
- Raport: `podstawowy/raporty/etap-4x22-literalne-dowody-0392-0431-2026-10-26.md`; rejestr: `review/batches/stage4x22-literal-0392-0431.json`.


## Aktualizacja po partii 0432–0471

- Świeży `main` na wejściu: `779dfa1b00a9025c9b4924067515b4ac260f17cd`.
- Sprawdzono 40 rekordów; 2 miały już wynik, 38 nadal oczekuje na urzędowe porównanie.
- Dla 38 otwartych zapisano przyczynę i następny krok. W szczególności progi tabeli 1.10.3.1.2, 5.2.1.8.1 oraz wymiary znaku z 5.3.6.2 pozostają niepotwierdzone w Dz.U. 2025.
- Wyszukiwanie zwracało teksty Dz.U. 2023/2019, odrzucone jako niewłaściwa edycja. Strony Dz.U. 2025 znalezione: 0; brak zmian pytań/kluczy i 0 `verified`.
- Raport: `podstawowy/raporty/etap-4x22-literalne-dowody-0432-0471-2026-10-26.md`; rejestr: `review/batches/stage4x22-literal-0432-0471.json`.


## Aktualizacja po partii 0472–0511

- Świeży `main` na wejściu: `38a5462270bde30837e294a7e890fa3ad99dbdc0`.
- Sprawdzono 40 rekordów; 1 miał już wynik, 39 nadal oczekuje na urzędowe porównanie.
- Wśród otwartych 11 ma cytaty pomocnicze MI, a 28 nie ma cytatu. Dla wszystkich 39 zapisano przyczynę i następny krok.
- Strony PDF Dz.U. potwierdzone: 0; brak potwierdzonych poprawek pytań/kluczy i 0 `verified`.
- Raport: `podstawowy/raporty/etap-4x22-literalne-dowody-0472-0511-2026-10-26.md`; rejestr: `review/batches/stage4x22-literal-0472-0511.json`.


## Aktualizacja po partii 0512–0551

- Świeży `main` na wejściu: `8b02eb4f5fed1cd7ba09dfd670afd3c652f64135`.
- Sprawdzono 40 rekordów; 10 miało już wynik, 30 nadal oczekuje na urzędowe porównanie.
- Wśród otwartych 2 mają cytaty pomocnicze MI, 28 nie ma cytatu. Dla wszystkich 30 zapisano przyczynę i następny krok.
- Strony PDF Dz.U. potwierdzone: 0; brak potwierdzonych zmian pytań/kluczy i 0 `verified`.
- Raport: `podstawowy/raporty/etap-4x22-literalne-dowody-0512-0551-2026-10-26.md`; rejestr: `review/batches/stage4x22-literal-0512-0551.json`.
