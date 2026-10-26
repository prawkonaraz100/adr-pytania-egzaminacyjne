# Etap 4x20 — ręczny audyt explanation ADR-B-0501–0550

- Punkt wyjścia: świeży `main` po PR #390, commit `5a429dfaadafc5175732073eb2cbbcca450d989e`.
- Zakres: wszystkie 50 pytań ADR-B-0501–ADR-B-0550.
- Metoda: automatyczne wskazanie skrótów i ryzyk językowych, następnie ręczna ocena wyjaśnień dla początkującego kursanta.

## Wynik

Ręcznie sprawdzono 50/50 wyjaśnień. Poprawiono 5, aby rozwinąć niewyjaśnione terminy:

| ID | Zmiana |
|---|---|
| ADR-B-0506 | Wyjaśniono znaczenie cyfry 6 w numerze rozpoznawczym zagrożenia oraz rolę numeru UN. |
| ADR-B-0511 | Rozwinięto IMDG jako kodeks przewozu towarów niebezpiecznych morzem. |
| ADR-B-0530 | Rozwinięto numer UN i wyjaśniono, że nie zastępuje nazwy przewozowej. |
| ADR-B-0545 | Rozróżniono numer rozpoznawczy zagrożenia od numeru UN. |
| ADR-B-0546 | Wyjaśniono, że numer UN jest identyfikatorem towaru, ale zwykła kartka nie zastępuje wymaganej nalepki. |

Pozostałe 45 wyjaśnień pozostawiono bez zmian. Przykładowe fałszywe alarmy: ADR-B-0507, 0508 i 0547 już wyjaśniają numer UN; ADR-B-0512, 0526–0528 oraz 0534–0535 rozwijają LQ/EQ w kontekście.

Nie zmieniono pytań, opcji, poprawnych liter, modułów ani statusów. Wszystkie rekordy pozostają `needs_review`.

## Lista sprawdzonych ID

ADR-B-0501, ADR-B-0502, ADR-B-0503, ADR-B-0504, ADR-B-0505, ADR-B-0506, ADR-B-0507, ADR-B-0508, ADR-B-0509, ADR-B-0510, ADR-B-0511, ADR-B-0512, ADR-B-0513, ADR-B-0514, ADR-B-0515, ADR-B-0516, ADR-B-0517, ADR-B-0518, ADR-B-0519, ADR-B-0520, ADR-B-0521, ADR-B-0522, ADR-B-0523, ADR-B-0524, ADR-B-0525, ADR-B-0526, ADR-B-0527, ADR-B-0528, ADR-B-0529, ADR-B-0530, ADR-B-0531, ADR-B-0532, ADR-B-0533, ADR-B-0534, ADR-B-0535, ADR-B-0536, ADR-B-0537, ADR-B-0538, ADR-B-0539, ADR-B-0540, ADR-B-0541, ADR-B-0542, ADR-B-0543, ADR-B-0544, ADR-B-0545, ADR-B-0546, ADR-B-0547, ADR-B-0548, ADR-B-0549, ADR-B-0550

## Kontrola wskaźników

- Bank: 609 pytań; duplikaty ID: 0.
- Explanation poniżej 200 znaków: 0; najkrótsze: 300 znaków.
- Zmienione explanation: 355–407 znaków, 3–4 zdania.
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

Zsynchronizowano snapshoty w `review/sequential` i `review/legal-clauses` dla wszystkich zmienionych rekordów. Odświeżono `source_bank_head` w wariantach i kluczach egzaminów 001–005 oraz wyjaśnienia w kluczach. Warianty zachowują 30 pytań, wszystkie 13 działów, A/B/C = 10/10/10 i maksymalną serię tej samej litery równą 1.

## Ograniczenia

To przegląd redakcyjny, nie formalna akceptacja prawna. Żadnego pytania nie oznaczono jako `verified`.
