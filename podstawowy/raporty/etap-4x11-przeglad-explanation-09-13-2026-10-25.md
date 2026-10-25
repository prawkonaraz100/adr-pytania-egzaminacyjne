# Etap 4x11 — ręczny przegląd ostrzeżeń explanation, partia B-09–13

- Data: 25.10.2026.
- Świeży punkt startowy: `main` `2277c1b7c73bed5cb85dfbbf06445902f305cd91`.
- Zakres: 33 ostrzeżenia z listy 4x10 przypisane do działów B-09–B-13.
- Zakres projektu pozostaje wyłącznie kursem podstawowym ADR.

## Wynik ręcznego przeglądu

| Dział | Przejrzane | Przepisane | Fałszywe alarmy |
|---|---:|---:|---:|
| B-09 | 4 | 0 | 4 |
| B-10 | 6 | 0 | 6 |
| B-11 | 5 | 1 | 4 |
| B-12 | 12 | 2 | 10 |
| B-13 | 6 | 0 | 6 |
| **Razem** | **33** | **3** | **30** |

## Lista sprawdzonych ID

- **B-09 (4):** ADR-B-0081, ADR-B-0173, ADR-B-0240, ADR-B-0291.
- **B-10 (6):** ADR-B-0391, ADR-B-0395, ADR-B-0438, ADR-B-0441, ADR-B-0448, ADR-B-0453.
- **B-11 (5):** ADR-B-0085, ADR-B-0086, ADR-B-0248, ADR-B-0490, ADR-B-0576.
- **B-12 (12):** ADR-B-0036, ADR-B-0067, ADR-B-0120, ADR-B-0122, ADR-B-0211, ADR-B-0300, ADR-B-0304, ADR-B-0402, ADR-B-0403, ADR-B-0404, ADR-B-0415, ADR-B-0582.
- **B-13 (6):** ADR-B-0037, ADR-B-0039, ADR-B-0068, ADR-B-0228, ADR-B-0250, ADR-B-0306.

## Potwierdzone poprawki

- **ADR-B-0085:** poprawiono zgodę gramatyczną w zdaniu o wyłączeniach i ograniczeniach tunelowych; dodano prostą wskazówkę, by najpierw sprawdzić warunki wyłączenia. Zachowano sens i podstawę: ADR 8.6.3.3.
- **ADR-B-0402:** usunięto powtórzenie o godzinie obiadu i modelu pojazdu; wyjaśnienie wskazuje, że plan ma określać środki ograniczające konkretne zagrożenia. Podstawa: ADR 1.10.3.2.2(d).
- **ADR-B-0403:** usunięto powtórzenie o reklamacjach i harmonogramie przerw; wyjaśnienie koncentruje się na zgłaszaniu naruszeń i reakcji na incydent. Podstawa: ADR 1.10.3.2.2(e).

Nie zmieniano ID, opcji, poprawnej litery ani źródeł. Zaktualizowano snapshoty w `review/sequential/` i `review/legal-clauses/`. Wszystkie trzy zmienione explanation przekraczają 300 znaków. Statusy pytań pozostały `needs_review`.

## Fałszywe alarmy

Pozostałe 30 wyjaśnień uznano za wystarczające dydaktycznie: wyjaśniają sens poprawnej odpowiedzi, konkretnie odrzucają mylące odpowiedzi i wskazują podstawę ADR. Brak jednego słowa-sygnału nie był powodem do redakcji. Wśród sprawdzonych tematów znalazły się czyszczenie po przewozie luzem, wspólny załadunek, dokumentacja transportu kombinowanego, kod tunelowy, dokument tożsamości załogi, plan ochrony, instrukcje pisemne i dane odbiorcy.

## Heurystyka po wszystkich partiach

- Lista bazowa z raportu 4x10: **86** ostrzeżeń.
- Po rozszerzeniu sygnałów: **11** kandydatów nadal bez sygnału; aktualny wynik sprawdzono w CI.
- Heurystyka jest doradcza: brak sygnału nie stanowi automatycznie błędu, a pozytywny sygnał nie zastępuje czytania wyjaśnienia przez człowieka.

## Wskaźniki banku

- 609 pytań, 0 zduplikowanych ID.
- Wskaźnik „poprawna = jedyna najdłuższa”: **77/609 = 12,64%** globalnie; każdy dział ≤16%. Zmieniono tylko explanation, nie długości opcji.
- Minimum explanation po poprawkach: **300 znaków**; wszystkie spełniają Quality Gate.
- Statusy: **609 `needs_review`, 0 `verified`**.
- Egzaminy próbne 001–005 nie wymagają aktualizacji: nie zmieniono opcji ani kluczy.

## Ograniczenia

To ręczny przegląd dydaktyczny wybranych ostrzeżeń, nie formalna akceptacja prawna. Nie potwierdzano zmian w ADR 2027. Nie rozpoczęto kursu cystern ani innego kursu.
