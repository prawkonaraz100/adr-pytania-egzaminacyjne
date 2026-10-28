# Etap 4x122 — próbka 40, explanation, dystraktory i synchronizacja

- Data: 2026-10-28.
- Punkt wejścia: świeży `main` `54bfc33446ad735be9ef86e721eac746c6c8da6d`; bank wejściowy blob SHA `f18b273e3451730a4efc28e10cd0ff16b03807f5`.
- Zakres: wyłącznie kurs podstawowy ADR. Próbka wybrana deterministycznie (seed `41222026`) z puli po wykluczeniu 302 unikalnych ID z próbek i jawnych poprawek/follow-upów etapów 4x114–4x121. Pula: 307; próbka: 40 unikalnych pytań.
- Wszystkie 40 pytań przeczytano wraz z opcjami A/B/C, kluczem, explanation i podstawą ADR. W 38 nie potwierdzono słabości wymagającej zmiany. Dwa pytania otrzymały poprawki dydaktyczne poniżej.

## Rejestr próbki

| ID | Dział | Wynik |
|---|---|---|
| ADR-B-0342 | ADR-B-03 | PASS redakcyjny; bez potwierdzonej potrzeby zmiany |
| ADR-B-0191 | ADR-B-06 | PASS redakcyjny; bez potwierdzonej potrzeby zmiany |
| ADR-B-0578 | ADR-B-13 | PASS redakcyjny; bez potwierdzonej potrzeby zmiany |
| ADR-B-0590 | ADR-B-13 | PASS redakcyjny; bez potwierdzonej potrzeby zmiany |
| ADR-B-0022 | ADR-B-08 | PASS redakcyjny; bez potwierdzonej potrzeby zmiany |
| ADR-B-0234 | ADR-B-13 | PASS redakcyjny; bez potwierdzonej potrzeby zmiany |
| ADR-B-0562 | ADR-B-06 | PASS redakcyjny; bez potwierdzonej potrzeby zmiany |
| ADR-B-0375 | ADR-B-07 | PASS redakcyjny; bez potwierdzonej potrzeby zmiany |
| ADR-B-0351 | ADR-B-04 | PASS redakcyjny; bez potwierdzonej potrzeby zmiany |
| ADR-B-0240 | ADR-B-09 | PASS redakcyjny; bez potwierdzonej potrzeby zmiany |
| ADR-B-0175 | ADR-B-13 | PASS redakcyjny; bez potwierdzonej potrzeby zmiany |
| ADR-B-0113 | ADR-B-05 | PASS redakcyjny; bez potwierdzonej potrzeby zmiany |
| ADR-B-0449 | ADR-B-10 | PASS redakcyjny; bez potwierdzonej potrzeby zmiany |
| ADR-B-0417 | ADR-B-08 | PASS redakcyjny; bez potwierdzonej potrzeby zmiany |
| ADR-B-0495 | ADR-B-02 | PASS redakcyjny; bez potwierdzonej potrzeby zmiany |
| ADR-B-0215 | ADR-B-13 | PASS redakcyjny; bez potwierdzonej potrzeby zmiany |
| ADR-B-0335 | ADR-B-03 | PASS redakcyjny; bez potwierdzonej potrzeby zmiany |
| ADR-B-0237 | ADR-B-09 | PASS redakcyjny; bez potwierdzonej potrzeby zmiany |
| ADR-B-0164 | ADR-B-04 | PASS redakcyjny; bez potwierdzonej potrzeby zmiany |
| ADR-B-0358 | ADR-B-04 | PASS redakcyjny; bez potwierdzonej potrzeby zmiany |
| ADR-B-0476 | ADR-B-04 | PASS redakcyjny; bez potwierdzonej potrzeby zmiany |
| ADR-B-0133 | ADR-B-06 | PASS redakcyjny; bez potwierdzonej potrzeby zmiany |
| ADR-B-0324 | ADR-B-09 | PASS redakcyjny; bez potwierdzonej potrzeby zmiany |
| ADR-B-0020 | ADR-B-07 | PASS redakcyjny; bez potwierdzonej potrzeby zmiany |
| ADR-B-0534 | ADR-B-01 | PASS redakcyjny; bez potwierdzonej potrzeby zmiany |
| ADR-B-0074 | ADR-B-08 | PASS redakcyjny; bez potwierdzonej potrzeby zmiany |
| ADR-B-0202 | ADR-B-09 | PASS redakcyjny; bez potwierdzonej potrzeby zmiany |
| ADR-B-0319 | ADR-B-08 | PASS redakcyjny; bez potwierdzonej potrzeby zmiany |
| ADR-B-0144 | ADR-B-12 | PASS redakcyjny; bez potwierdzonej potrzeby zmiany |
| ADR-B-0520 | ADR-B-01 | PASS redakcyjny; bez potwierdzonej potrzeby zmiany |
| ADR-B-0462 | ADR-B-03 | PASS redakcyjny; bez potwierdzonej potrzeby zmiany |
| ADR-B-0327 | ADR-B-03 | PASS redakcyjny; bez potwierdzonej potrzeby zmiany |
| ADR-B-0291 | ADR-B-09 | PASS redakcyjny; bez potwierdzonej potrzeby zmiany |
| ADR-B-0001 | ADR-B-01 | PASS redakcyjny; bez potwierdzonej potrzeby zmiany |
| ADR-B-0361 | ADR-B-04 | Poprawiono dystraktory i explanation |
| ADR-B-0027 | ADR-B-09 | PASS redakcyjny; bez potwierdzonej potrzeby zmiany |
| ADR-B-0312 | ADR-B-01 | PASS redakcyjny; bez potwierdzonej potrzeby zmiany |
| ADR-B-0320 | ADR-B-10 | PASS redakcyjny; bez potwierdzonej potrzeby zmiany |
| ADR-B-0298 | ADR-B-06 | PASS redakcyjny; bez potwierdzonej potrzeby zmiany |
| ADR-B-0497 | ADR-B-02 | PASS redakcyjny; bez potwierdzonej potrzeby zmiany |

## Potwierdzone poprawki

1. **ADR-B-0326 — klasyfikacja odpadu, ADR 2.1.3.5.5.** Dwa błędne warianty były zbyt łatwe do odrzucenia („tak, bez żadnych ograniczeń” oraz odwołanie do samej znajomości nazwy przez kierowcę). Zastąpiono je typowymi, lecz nadal błędnymi założeniami, że nazwa i ogólne dane albo kod katalogowy i karta przekazania znoszą wyłączenie dla klasy 4.3. Poprawna litera B i podstawa prawna pozostały bez zmian. Explanation wyjaśnia, dlaczego te informacje nie uchylają wyłączenia.
2. **ADR-B-0361 — palne opary i źródła zapłonu, ADR 5.4.3.4.** Dwa błędne warianty z zapalniczką i uruchamianiem wszystkich odbiorników były zbyt skrajne. Zastąpiono je pomysłami, które kursant może uznać za pomocne: włączeniem wentylatora i uruchomieniem oświetlenia/urządzeń, gdy nie widać płomienia. Poprawna litera A i podstawa ADR pozostały bez zmian. Explanation mówi, dlaczego oba działania nie gwarantują bezpieczeństwa.

Łącznie: **2 pytania zmienione, 4 dystraktory poprawione, 2 explanation dopasowane**. Nie znaleziono w tej próbce potwierdzonej podstawy do zmiany klucza, numeracji ani dopisania pytania. To nie jest potwierdzenie pełnego pokrycia programu ani niezależna opinia prawna.

## Synchronizacja

- Migawki `review/legal-clauses/325-344.json` i `345-362.json` odświeżono o nowe opcje, explanation i uzasadnienia A/B/C.
- Migawki `review/sequential/325-344.json` i `345-362.json` zsynchronizowano z aktualnym zapisem pytań; statusy prawne pozostają `needs_review`.
- Warianty egzaminu próbnego 001–005 wskazują nowy blob banku `bc5656006e7d5ced7065ef099dca814bb6fa9f15`. Żaden z dwóch zmienionych ID nie występuje w tych pięciu arkuszach, więc nie zmieniano składu wariantów ani liter kluczy.

## Metryki po zmianach

- Bank: 609 pytań, brak duplikatów ID.
- „Poprawna = jedyna najdłuższa”: 71/609 = **11,66%** (limit 18%).
- Maksimum działu: **14,29%**.
- Najkrótsze explanation: **300 znaków**; poniżej 200 znaków: **0**.
- Status: 609 `needs_review`, 0 `verified`.
- Nowy blob banku: `bc5656006e7d5ced7065ef099dca814bb6fa9f15`.

## Ograniczenia

Przegląd redakcyjny nie zastępuje porównania z pełnym polskim tekstem urzędowym ADR 2025 i niezależnej recenzji. Nie nadano statusu `verified`; nie rozpoczęto kursu cystern ani innego kursu.
