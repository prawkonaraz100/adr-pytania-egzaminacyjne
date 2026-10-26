# Etap 4x20 — ręczny audyt explanation ADR-B-0251–0300

- Punkt wyjścia: świeży `main`, commit `b5bbee485a8d1d187a6a84b37e618e4461ff659a`.
- Zakres: wszystkie 50 pytań o ID ADR-B-0251–ADR-B-0300, niezależnie od przypisanego działu.
- Metoda: skryptowa kontrola długości, liczby zdań, otwierających odwołań prawnych i skrótów, a następnie ręczna ocena, czy wyjaśnienie jest zrozumiałe dla początkującego kierowcy.

## Wynik

Ręcznie sprawdzono 50/50 wyjaśnień. Poprawiono 3, aby rozwinąć żargon bez zmiany poprawnej litery, treści odpowiedzi ani statusu weryfikacji:

| ID | Problem | Poprawka |
|---|---|---|
| ADR-B-0278 | Skrót EDI nie był wyjaśniony, mimo że wyjaśnienie dotyczyło elektronicznego otrzymania dokumentu. | Dodano „EDI, czyli elektroniczną wymianę danych”; pozostawiono wymagany angielski zapis dokumentu i podstawę ADR/IMDG. |
| ADR-B-0281 | „UN” było opisane jako litery, ale nie wyjaśniono, co identyfikuje numer. | Doprecyzowano, że numer UN jest czterocyfrowym identyfikatorem towaru niebezpiecznego. |
| ADR-B-0292 | Kody BK i VC pojawiały się bez wyjaśnienia, do czego służą. | Wyjaśniono, że wskazują dopuszczone typy kontenerów i szczególne warunki przewozu luzem; wskazano kolumny tabeli A. |

Pozostałe 47 wyjaśnień pozostawiono bez zmian: zawierają wystarczające objaśnienie sensu odpowiedzi i mylących wariantów albo skróty są już rozwinięte w kontekście. Nie zmieniono treści pytań, opcji, poprawnych liter ani przypisania modułów. Wszystkie statusy pozostają `needs_review`; nie oznaczono żadnego pytania jako `verified`.

## Lista sprawdzonych ID

ADR-B-0251, ADR-B-0252, ADR-B-0253, ADR-B-0254, ADR-B-0255
, ADR-B-0256, ADR-B-0257, ADR-B-0258, ADR-B-0259, ADR-B-0260
, ADR-B-0261, ADR-B-0262, ADR-B-0263, ADR-B-0264, ADR-B-0265
, ADR-B-0266, ADR-B-0267, ADR-B-0268, ADR-B-0269, ADR-B-0270
, ADR-B-0271, ADR-B-0272, ADR-B-0273, ADR-B-0274, ADR-B-0275
, ADR-B-0276, ADR-B-0277, ADR-B-0278, ADR-B-0279, ADR-B-0280
, ADR-B-0281, ADR-B-0282, ADR-B-0283, ADR-B-0284, ADR-B-0285
, ADR-B-0286, ADR-B-0287, ADR-B-0288, ADR-B-0289, ADR-B-0290
, ADR-B-0291, ADR-B-0292, ADR-B-0293, ADR-B-0294, ADR-B-0295
, ADR-B-0296, ADR-B-0297, ADR-B-0298, ADR-B-0299, ADR-B-0300


## Kontrola wskaźników po zmianach

- Bank: 609 pytań; duplikaty ID: 0.
- Explanation poniżej 200 znaków: 0; najkrótsze: 300 znaków.
- Wszystkie 3 zmienione explanation mają 200–500 znaków i 2–5 zdań.
- Poprawna odpowiedź jako jedyna najdłuższa w całym banku: 73/609 = 11.99%.
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
- B-01: 13.33%; B-04: 13.04%. Oba działy już przed tą partią mieściły się w limicie 14%; ich odpowiedzi nie zmieniano.
- Explanation ADR-B-0196, ADR-B-0398 i ADR-B-0440 na świeżym main nie zaczynały się już od numeru przepisu; wszystkie zaczynają od wyjaśnienia sensu i zostały zachowane.

## Ograniczenia

To przegląd językowy, nie niezależna recenzja prawna. Zmiany dotyczą wyłącznie objaśnienia terminów; nie zmieniono żadnego stanowiska prawnego bez potrzeby. Pełny Quality Gate CI jest wymagany przed scaleniem.
