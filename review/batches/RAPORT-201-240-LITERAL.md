# ADR-B-0201–0240 — kontrola A/B/C i potwierdzone błędy kluczy

Data 23.10.2026. Przejrzano warianty A/B/C oraz uzasadnienia 40 rekordów i porównano z podanymi ustępami ADR 2025, szczegółowo z polską wersją MI: [tom II](https://www.gov.pl/attachment/b7292c03-ac9d-4f80-9a29-c22f53d847b8). Źródłem prawa pozostaje [Dz.U. 2025 poz. 642](https://dziennikustaw.gov.pl/DU/2025/642) z [sprostowaniem poz. 1575](https://eli.gov.pl/eli/DU/2025/1575/ogl). **6 błędów klucza potwierdzono w bezpośrednio odczytanych punktach**; dla pozostałych 34 nie zakończono literalnego porównania wszystkich warunków i odesłań urzędowego Dz.U., więc wynik końcowy to wymaga specjalisty. Sprostowanie sprawdzono co do zakresu wskazanych poprawek; nie dotyczy ono bezpośrednio sześciu przepisów będących podstawą korekty.

## Błędy naprawione

| ID | Stary klucz | Poprawiony | Potwierdzający ustęp |
|---|---|---|---|
| 0220 | B | A | 5.4.3.4: informacje dla ratowników |
| 0221 | C | B | 5.4.3.4: strona nawietrzna |
| 0223 | B | A | 5.4.3.4: mały pożar tylko gdy bezpiecznie |
| 0224 | C | B | 5.4.3.4: oddalenie osób postronnych |
| 0226 | B | A | 5.4.1.1.1(a): litery UN |
| 0228 | A | C | 5.4.3.1: instrukcje łatwo dostępne w kabinie |

## Cała partia i ocena wariantów

Pełne brzmienie opcji A, B, C, osobne uzasadnienie, wyjaśnienie i uwagi o wyjątkach: `review/batches/201-240-comparisons.json`.

| ID | Ustęp | Decyzja |
|---|---|---|
| ADR-B-0201 | ADR 2025, 7.5.8.2 | wymaga specjalisty do ostatecznego literalnego potwierdzenia |
| ADR-B-0202 | ADR 2025, 7.5.1.2 | wymaga specjalisty do ostatecznego literalnego potwierdzenia |
| ADR-B-0203 | ADR 2025, 5.4.1.1.7 | wymaga specjalisty do ostatecznego literalnego potwierdzenia |
| ADR-B-0204 | ADR 2025, 5.4.2 | wymaga specjalisty do ostatecznego literalnego potwierdzenia |
| ADR-B-0205 | ADR 2025, 1.1.4.2; 1.1.4.3 | wymaga specjalisty do ostatecznego literalnego potwierdzenia |
| ADR-B-0206 | ADR 2025, 1.1.4.2.1 | wymaga specjalisty do ostatecznego literalnego potwierdzenia |
| ADR-B-0207 | ADR 2025, 1.9.5.2.2; 8.6.4 | wymaga specjalisty do ostatecznego literalnego potwierdzenia |
| ADR-B-0208 | ADR 2025, 8.6.3.1; 8.6.4 | wymaga specjalisty do ostatecznego literalnego potwierdzenia |
| ADR-B-0209 | ADR 2025, 8.6.3.3; 8.6.4 | wymaga specjalisty do ostatecznego literalnego potwierdzenia |
| ADR-B-0210 | ADR 2025, 5.4.3.4; 1.9.5 | wymaga specjalisty do ostatecznego literalnego potwierdzenia |
| ADR-B-0211 | ADR 2025, 1.10.1.2 | wymaga specjalisty do ostatecznego literalnego potwierdzenia |
| ADR-B-0212 | ADR 2025, 1.10.3.2.2 | wymaga specjalisty do ostatecznego literalnego potwierdzenia |
| ADR-B-0213 | ADR 2025, 1.10.3.3 | wymaga specjalisty do ostatecznego literalnego potwierdzenia |
| ADR-B-0214 | ADR 2025, 5.4.1.1.1(g),(h) | wymaga specjalisty do ostatecznego literalnego potwierdzenia |
| ADR-B-0215 | ADR 2025, 5.4.1.1.7; 5.4.1.1.1 | wymaga specjalisty do ostatecznego literalnego potwierdzenia |
| ADR-B-0216 | ADR 2025, 8.1.2.1(b); 8.1.2.3 | wymaga specjalisty do ostatecznego literalnego potwierdzenia |
| ADR-B-0217 | ADR 2025, 5.3.2.3.1 | wymaga specjalisty do ostatecznego literalnego potwierdzenia |
| ADR-B-0218 | ADR 2025, 5.2.2.1.1; 3.2.1 tabela A kolumna (5) | wymaga specjalisty do ostatecznego literalnego potwierdzenia |
| ADR-B-0219 | ADR 2025, 5.4.3.4 | wymaga specjalisty do ostatecznego literalnego potwierdzenia |
| ADR-B-0220 | ADR 2025, 5.4.3.4 | błąd potwierdzony i poprawiony |
| ADR-B-0221 | ADR 2025, 5.4.3.4 | błąd potwierdzony i poprawiony |
| ADR-B-0222 | ADR 2025, 5.4.3.4 | wymaga specjalisty do ostatecznego literalnego potwierdzenia |
| ADR-B-0223 | ADR 2025, 5.4.3.4 | błąd potwierdzony i poprawiony |
| ADR-B-0224 | ADR 2025, 5.4.3.4 | błąd potwierdzony i poprawiony |
| ADR-B-0225 | ADR 2025, 5.4.3.4 | wymaga specjalisty do ostatecznego literalnego potwierdzenia |
| ADR-B-0226 | ADR 2025, 5.4.1.1.1(a) | błąd potwierdzony i poprawiony |
| ADR-B-0227 | ADR 2025, 5.4.1.1.1(e) | wymaga specjalisty do ostatecznego literalnego potwierdzenia |
| ADR-B-0228 | ADR 2025, 5.4.3.1; 8.1.2.3 | błąd potwierdzony i poprawiony |
| ADR-B-0229 | ADR 2025, 5.4.3.4 | wymaga specjalisty do ostatecznego literalnego potwierdzenia |
| ADR-B-0230 | ADR 2025, 5.4.3.4 | wymaga specjalisty do ostatecznego literalnego potwierdzenia |
| ADR-B-0231 | ADR 2025, 5.4.3.4; 8.1.5.2 | wymaga specjalisty do ostatecznego literalnego potwierdzenia |
| ADR-B-0232 | ADR 2025, 8.1.4.5 | wymaga specjalisty do ostatecznego literalnego potwierdzenia |
| ADR-B-0233 | ADR 2025, 5.4.1.1.1(h) | wymaga specjalisty do ostatecznego literalnego potwierdzenia |
| ADR-B-0234 | ADR 2025, 5.4.3.2; 5.4.3.4 | wymaga specjalisty do ostatecznego literalnego potwierdzenia |
| ADR-B-0235 | ADR 2025, 7.5.7.1 | wymaga specjalisty do ostatecznego literalnego potwierdzenia |
| ADR-B-0236 | ADR 2025, 7.5.7.1 | wymaga specjalisty do ostatecznego literalnego potwierdzenia |
| ADR-B-0237 | ADR 2025, 7.5.7.2 | wymaga specjalisty do ostatecznego literalnego potwierdzenia |
| ADR-B-0238 | ADR 2025, 7.5.8.1 | wymaga specjalisty do ostatecznego literalnego potwierdzenia |
| ADR-B-0239 | ADR 2025, 7.5.1.2 | wymaga specjalisty do ostatecznego literalnego potwierdzenia |
| ADR-B-0240 | ADR 2025, 7.5.8.2 | wymaga specjalisty do ostatecznego literalnego potwierdzenia |

## Integralność

Zmodyfikowano tylko 6 pól `correct_option` w pytaniach i zsynchronizowano `review/legal-clauses/219-228.json` (wszystkie trzy flagi oczekiwanej odpowiedzi, uzasadnienia, klucze, snapshoty) oraz `review/sequential/219-228.json` (snapshoty i ryzyka). Brak sztucznych podpisów, recenzentów, `verified`. **Nie twierdzimy, że CI bada zgodność prawa:** Quality Gate wykrywa wyłącznie spójność techniczną. Eksport BLOCKED. Bez cystern.
