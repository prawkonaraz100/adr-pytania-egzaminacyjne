# Etap 4x117 — pozostała pula explanation, dystraktory i synchronizacja

- Data: 2026-10-28.
- Punkt wyjścia: świeży `main` `cf78398aeca638cdd14f0d8e724cd8523f25af91` (PR #575 / 4x116).
- Zakres: wyłącznie kurs podstawowy ADR.
- Bank po redakcji: 609 pytań, 609 `needs_review`, 0 `verified`.

## Próba i metoda

Zastosowano seed `41172026`, LCG + Fisher–Yates. Wykluczono identyfikatory z manifestu 4x116: `543` ID z list wykluczeń i prób poprzednich etapów. Pozostała pula ma 26 pytań; przejrzano całą pulę zamiast deklarować próbkę 40, gdy kandydatów jest mniej.

ID przeglądu: ADR-B-0523, ADR-B-0054, ADR-B-0230, ADR-B-0419, ADR-B-0492, ADR-B-0481, ADR-B-0354, ADR-B-0456, ADR-B-0197, ADR-B-0513, ADR-B-0443, ADR-B-0221, ADR-B-0028, ADR-B-0168, ADR-B-0414, ADR-B-0535, ADR-B-0108, ADR-B-0603, ADR-B-0458, ADR-B-0505, ADR-B-0086, ADR-B-0413, ADR-B-0013, ADR-B-0499, ADR-B-0543, ADR-B-0273.

Ograniczenie: wcześniejsze raporty 4x103–4x106 nie zawsze odróżniają ID wylosowane od omawianych przy innych kontrolach. Poprzednie etapy stosowały konserwatywne wykluczenia, a ta próba obejmuje pozostałą pulę wynikającą z manifestu 4x116. Nie twierdzę, że nieudokumentowane starsze próbki są możliwe do odtworzenia z samych raportów.

## Wynik

- Przejrzano 26 wyjaśnień. Długość explanation w puli: 300–425 znaków; wszystkie mają 2–5 zdań i wyjaśniają sens poprawnej odpowiedzi oraz główną pomyłkę. Nie było potrzeby przepisywania samych explanation.
- Potwierdzono 5 zestawów dystraktorów, w których błędne opcje były zbyt odległe od sytuacji lub łatwe do odrzucenia. Zmieniono 10 błędnych opcji i dopasowano explanation, nie zmieniając ID, poprawnej litery ani podstawy prawnej.

| ID | Potwierdzony problem | Poprawka |
|---|---|---|
| ADR-B-0028 | Dystraktory o regulaminie magazynu i parkowaniu były zbyt odległe od pomyłek w transporcie drogowym/morskim. | Zastąpiono je błędnym założeniem, że IMDG obejmuje całą trasę albo ADR także odcinek morski. Podstawa: ADR 1.1.4.2. |
| ADR-B-0054 | „Tak, bez ograniczeń” i zwykła taśma były zbyt łatwe do odrzucenia. | Wprowadzono pomyłki o czytelnym oznakowaniu/małym wycieku i doraźnym zaklejeniu. Podstawa: ADR 1.4.3.1.1(b). |
| ADR-B-0354 | Próbowanie substancji po smaku lub zapachu było absurdalne. | Wprowadzono typowe błędy: zaufanie zwykłym rękawicom oraz wybór strony zawietrznej, by odczytać etykietę. Podstawa: ADR 5.4.3.4. |
| ADR-B-0492 | Rozdzielenie dokumentów i kontakt telefoniczny nie opisywały wiarygodnie błędnego rozumowania. | Zmieniono je na „rozdzielenie tylko na papierze” i traktowanie ustnej zgody nadawcy jako wyjątku. Podstawa: ADR 7.5.2.1, uwaga 1, oraz 5.4.1.4.2. |
| ADR-B-0535 | Liczba pojazdów i harmonogram zmian nie dotyczyły informacji o LQ. | Wprowadzono pomylenie liczby opakowań z masą brutto oraz masy netto z brutto. Podstawa: ADR 3.4.12. |

### Przykłady przed / po

1. ADR-B-0028 B: „Regulamin magazynu dotyczący przechowywania towarów” → „Stosować wyłącznie IMDG, ponieważ odcinek morski podlega temu kodeksowi, a on obejmuje całą trasę.”
2. ADR-B-0354 C: „Spróbować substancji, aby rozpoznać ją po smaku lub zapachu” → „Pozostać po stronie zawietrznej, jeśli z tej strony etykieta jest lepiej widoczna, i nie dotykać cieczy.”
3. ADR-B-0535 C: „Podać wyłącznie szczegółowy harmonogram zmian kierowców oraz plan przerw na trasie” → „Przekazać wyłącznie masę netto zawartości LQ, ponieważ opakowania nie są częścią towaru.”

## Scenariusze i egzaminy

- Scenariusze: 39; brakujące wymagane pola lub niezgodne/nieistniejące question ID: 0.
- Zmienione ID nie występują w arkuszach 001–005, więc nie zmieniano tekstu pytań ani kluczy w arkuszach. Zaktualizowano `source_bank_head` we wszystkich 5 wariantach i 5 kluczach do nowego blobu banku `30b9212b2feff4232440416c9ab4052e93cc1f4a`.
- Zaktualizowano migawki prawne A/B/C oraz migawki sekwencyjne dla pięciu zmienionych ID. Ich status nadal wynosi `needs_review`; specjalista musi niezależnie potwierdzić treść prawną.

## Quality Gate — preflight

- Bank: 609 pytań, 609 unikalnych ID.
- Poprawna odpowiedź jest jedyną najdłuższą: 72/609 = 11.82%.
- Najkrótsze explanation: 300 znaków; poniżej 200 znaków: 0.
- Wskaźniki działowe:
  - ADR-B-01: 6/45 = 13.33%; minimum explanation 300 znaków
  - ADR-B-02: 8/56 = 14.29%; minimum explanation 300 znaków
  - ADR-B-03: 5/49 = 10.20%; minimum explanation 300 znaków
  - ADR-B-04: 6/46 = 13.04%; minimum explanation 301 znaków
  - ADR-B-05: 5/43 = 11.63%; minimum explanation 300 znaków
  - ADR-B-06: 6/45 = 13.33%; minimum explanation 301 znaków
  - ADR-B-07: 6/48 = 12.50%; minimum explanation 304 znaków
  - ADR-B-08: 4/42 = 9.52%; minimum explanation 303 znaków
  - ADR-B-09: 5/46 = 10.87%; minimum explanation 301 znaków
  - ADR-B-10: 4/55 = 7.27%; minimum explanation 308 znaków
  - ADR-B-11: 6/43 = 13.95%; minimum explanation 300 znaków
  - ADR-B-12: 6/44 = 13.64%; minimum explanation 303 znaków
  - ADR-B-13: 5/47 = 10.64%; minimum explanation 308 znaków
- Statusy: 609 `needs_review`, 0 `verified`.

Pełne testy lokalne nie były dostępne przez samo API GitHub w tej sesji; wymagany jest PASS GitHub Actions przed scaleniem. Nie rozpoczęto kursu cystern ani innego kursu.
