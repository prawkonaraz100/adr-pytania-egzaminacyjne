# Etap 4x118 — pozostała próbka, jakość dystraktorów i synchronizacja

- Data: 2026-10-28.
- Punkt wyjścia: świeży `main` `b8464030c2d9cf31bd67666673789d58ce9b6a79` po scaleniu PR #577 (4x117).
- Zakres: wyłącznie kurs podstawowy ADR.
- Bank po zmianach: 609 pytań; 609 `needs_review`, 0 `verified`.

## 1. Próba i jawne wykluczenia

Seed `41182026`, LCG + Fisher–Yates. Wykluczono 584 ID: wcześniejsze wykluczenia i próbę 4x116 oraz 40 ID z próby 4x117. Pozostała pula to 25 ID; przejrzano całą pulę, zamiast deklarować próbkę 40 z mniejszego zbioru.

**Nowa, rozłączna próbka 25 ID:** ADR-B-0197, ADR-B-0513, ADR-B-0054, ADR-B-0273, ADR-B-0481, ADR-B-0603, ADR-B-0443, ADR-B-0456, ADR-B-0168, ADR-B-0413, ADR-B-0499, ADR-B-0230, ADR-B-0221, ADR-B-0543, ADR-B-0028, ADR-B-0108, ADR-B-0505, ADR-B-0354, ADR-B-0492, ADR-B-0013, ADR-B-0523, ADR-B-0458, ADR-B-0086, ADR-B-0414, ADR-B-0419.

Dodatkowo wykonano celowany follow-up dla **ADR-B-0535**, które wystąpiło w próbie 4x117, ale jego opcje nie zostały w tamtym PR zmienione. To nakładanie jest jawnie opisane i nie liczy się do nowych 25 ID.

## 2. Wynik przeglądu

- W 25 nowych ID sprawdzono stem, opcje A/B/C, poprawną literę, explanation i wskazaną podstawę ADR. Wyjaśnienia w tej puli mają 2–5 zdań i co najmniej 300 znaków; nie wykryto wyjaśnień jednozdaniowych ani czysto „przepisowych”.
- W pięciu pytaniach urealniono 10 błędnych opcji i dopasowano explanation. Cztery z tych pytań należą do nowej próbki; ADR-B-0535 jest jawnie oznaczonym follow-upem po próbie 4x117. Zachowano ID, poprawne litery i podstawy ADR.

| ID | Potwierdzona słabość | Poprawka | Podstawa ADR |
|---|---|---|---|
| ADR-B-0028 | Dystraktory o regulaminie magazynu i parkowaniu były zbyt odległe od pomyłek w transporcie drogowym/morskim. | Wprowadzono błędne założenia, że IMDG obejmuje całą trasę albo że ADR reguluje także odcinek morski. | 1.1.4.2 |
| ADR-B-0054 | „Tak, bez ograniczeń” i zwykła taśma były zbyt łatwe do odrzucenia. | Wprowadzono pomyłki o czytelnym oznakowaniu/małym wycieku oraz doraźnym zaklejeniu. Poprawną opcję wydłużono, aby nie była wyraźnie najkrótsza. | 1.4.3.1.1(b) |
| ADR-B-0354 | Próbowanie substancji po smaku lub zapachu było absurdalne. | Wprowadzono wiarygodne, ale błędne założenia o zwykłych rękawicach i wyborze strony zawietrznej. | 5.4.3.4 |
| ADR-B-0492 | Rozdzielenie dokumentów i telefon do nadawcy nie opisywały realistycznej pomyłki. | Wprowadzono „rozdzielenie tylko na papierze” i traktowanie ustnej zgody jako wyjątku. | 7.5.2.1, uwaga 1; 5.4.1.4.2 |
| ADR-B-0535 | Liczba pojazdów i grafik kierowców nie dotyczyły wymaganej informacji o LQ. | Wprowadzono pomylenie liczby opakowań z masą brutto oraz masy netto z brutto. | 3.4.12 |

### Przykłady przed / po

1. **ADR-B-0028 B:** „Regulamin magazynu dotyczący przechowywania towarów” → „Stosować wyłącznie IMDG, ponieważ odcinek morski podlega temu kodeksowi, a on obejmuje całą trasę.”
2. **ADR-B-0354 C:** „Spróbować substancji, aby rozpoznać ją po smaku lub zapachu” → „Pozostać po stronie zawietrznej, jeśli z tej strony etykieta jest lepiej widoczna, i nie dotykać cieczy.”
3. **ADR-B-0535 C:** „Podać wyłącznie szczegółowy harmonogram zmian kierowców oraz plan przerw na trasie” → „Przekazać wyłącznie masę netto zawartości LQ, ponieważ opakowania nie są częścią towaru.”

## 3. Synchronizacja scenariuszy, egzaminów i audytów

- Scenariusze: 39; brak nieistniejących ID, odwołań między działami lub brakujących wymaganych pól: 0.
- Zmienione ID nie występują w wariantach 001–005; zsynchronizowano `source_bank_head` we wszystkich 5 wariantach i kluczach do blobu `28d809ccbf973fc8101f456eb9ab0144165110f1`.
- Odświeżono migawki A/B/C i sekwencyjne dla ADR-B-0028, 0054, 0354, 0492 i 0535.
- Pełne testy lokalne nie były dostępne przez sam interfejs GitHub; wymagany jest PASS GitHub Actions przed scaleniem.

## 4. Quality Gate — preflight

- Bank: 609 pytań, 609 unikalnych ID; wszystkie `needs_review`, 0 `verified`.
- „Poprawna = jedyna najdłuższa”: 72/609 = 11.82%; maksimum działu 14,29%.
- Najkrótsze explanation: 300 znaków; poniżej 200: 0.
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

Status prawny pozostaje otwarty; żadnego pytania nie oznaczono jako `verified`. Nie rozpoczęto kursu cystern ani innego kursu.
