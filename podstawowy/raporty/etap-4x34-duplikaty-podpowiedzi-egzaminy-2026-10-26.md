# Etap 4x34 — kontrola duplikatów, podpowiedzi i egzaminów próbnych

- Data: 26.10.2026.
- Świeży punkt wyjścia: `main` po PR #476, commit `461d4a37f6d3a2551fd40d526d509736c3ec2f95`.
- Zakres: wyłącznie bank ADR podstawowy, 609 pytań `ADR-B-0001…0609`.
- PR #476 / etap 4x33 potwierdzono jako scalony; jego Quality Gate zakończył się sukcesem, a wpis w Issue #10 już istnieje.

## 1. Wynik skanowania powtórzeń

Skryptowy przegląd całego banku porównał znormalizowane treści pytań, zestawy odpowiedzi oraz podobieństwo leksykalne w obrębie każdego działu. Wynik przed zmianami: **0 identycznych treści pytań, 0 identycznych zestawów trzech odpowiedzi**. Heurystyka podobieństwa wskazywała parę ADR-B-0071/0072; po ręcznym odczycie uznano ją za uzasadnioną — sprawdza różne progi minimalnej łącznej pojemności gaśnic dla różnych przedziałów DMC, a nie ten sam próg.

Ręczny przegląd wykrył jednak powtarzające się schematy dydaktyczne, których próg leksykalny nie wykrywał:
- **ADR-B-0059 / 0078 / 0237 — piętrzenie opakowań:** B-05? Nie — wszystkie trzy pytania należą do B-09. Pytanie 0078 przeredagowano tak, by sprawdzało osobny przypadek mokrego i zdeformowanego opakowania z oznaczeniem piętrzenia. Podstawa: ADR 7.5.1.3 i 7.5.7.2.
- **ADR-B-0009 / 0238 — oczyszczenie po wycieku:** 0009 sprawdza obowiązek oczyszczenia przed ponownym załadunkiem; 0238 przeredagowano, by sprawdzało pilność — oczyścić tak szybko, jak to możliwe, a nie czekać do planowanego załadunku za dwa dni. Podstawa: ADR 7.5.8.1.
- **ADR-B-0048 / 0243 — otwieranie sztuk przesyłek:** 0048 przeredagowano, by sprawdzało, kogo obejmuje zakaz (całą załogę, nie tylko kierowcę), a nie powtarzało ogólne pytanie „czy wolno otwierać”. Podstawa: ADR 8.3.3.

Nie usunięto żadnego ID i nie zmieniono przypisania do działu.

## 2. Podpowiedź w treści

- **ADR-B-0127:** poprzednia odpowiedź powtarzała wprost zwrot z pytania („wysoki stopień zagrożenia”), co mogło podpowiadać klucz. Przepisano pytanie i odpowiedzi, tak aby kursant musiał znać kolejność grup pakowania: I — wysoki, II — średni, III — niski. Zachowano poprawną literę B. Podstawa: ADR 2.1.1.3.
- **ADR-B-0125:** sprawdzono powtórzenie terminu „numer UN”; uznano je za naturalne i niewystarczające samo w sobie do ujawnienia klucza, ponieważ pytanie rozróżnia konkretne kolumny tabeli A. Bez zmiany.
- **ADR-B-0007 i ADR-B-0008:** powtórzenie pojęcia „symbol” / „ODPAD” jest potrzebne do identyfikacji badanego znaku lub wpisu, a błędne odpowiedzi pozostają merytorycznie odróżnialne. Bez zmiany.
- **ADR-B-0105 / 0165 / 0220:** mają wspólny temat alarmowania, ale różne sytuacje i zakres informacji (ogólne zgłoszenie, pytanie dyspozytora, informacja poza lokalizacją). Nie uznano ich za duplikaty; bez zmiany.

## 3. Zmienione pytania

| ID | Co zmieniono | Podstawa ADR | Explanation |
|---|---|---|---:|
| ADR-B-0048 | Zamiast ponownego pytania o sam zakaz: zakres zakazu wobec całej załogi | 8.3.3 | 346 znaków |
| ADR-B-0078 | Mokre/zdeformowane opakowanie mimo oznaczenia dopuszczającego piętrzenie | 7.5.1.3, 7.5.7.2 | 359 znaków |
| ADR-B-0127 | Usunięto powtórzenie frazy zdradzającej odpowiedź; uporządkowano I/II/III | 2.1.1.3 | 322 znaki |
| ADR-B-0238 | Pilność czyszczenia po wycieku, nie tylko termin przed następnym załadunkiem | 7.5.8.1 | 333 znaki |

Dla wszystkich czterech pytań zachowano ID, dział, poprawną literę i status `needs_review`. Explanation mają 2–5 zdań, prosty język, wyjaśnienie błędnych opcji oraz podstawę ADR. Nie oznaczono niczego jako `verified`.

## 4. Metryki po zmianach

- Bank: 609 pytań, 609 unikalnych ID; statusy: 609 `needs_review`, 0 `verified`.
- Identyczne treści pytań: 0.
- Identyczne zestawy odpowiedzi: 0.
- Nierozstrzygnięte pary ponad próg skryptu `check_near_duplicates.py --threshold 0.60`: 0 (para 0071/0072 pozostaje udokumentowanym wyjątkiem dla odmiennych przedziałów DMC).
- Explanation poniżej 300 znaków: 0; najkrótsze wyjaśnienia w działach mają 300–308 znaków.
- „Poprawna odpowiedź jest jedyną najdłuższą”: **71/609 = 11,66%** globalnie (limit 18%).

| Dział | Pytania | Poprawna = jedyna najdłuższa | Odsetek | Litery A/B/C |
|---|---:|---:|---:|---:|
| B-01 | 45 | 6 | 13,33% | 17/17/11 |
| B-02 | 56 | 7 | 12,50% | 21/19/16 |
| B-03 | 49 | 7 | 14,29% | 16/21/12 |
| B-04 | 46 | 6 | 13,04% | 15/18/13 |
| B-05 | 43 | 5 | 11,63% | 18/14/11 |
| B-06 | 45 | 5 | 11,11% | 16/14/15 |
| B-07 | 48 | 6 | 12,50% | 18/18/12 |
| B-08 | 42 | 5 | 11,90% | 12/12/18 |
| B-09 | 46 | 4 | 8,70% | 13/15/18 |
| B-10 | 55 | 4 | 7,27% | 19/18/18 |
| B-11 | 43 | 6 | 13,95% | 12/13/18 |
| B-12 | 44 | 6 | 13,64% | 14/13/17 |
| B-13 | 47 | 4 | 8,51% | 15/15/17 |

## 5. Egzaminy próbne 001–005

- Wszystkie pięć wariantów i kluczy wskazuje aktualny blob banku: `7c7573215da82caeabe9543eb47dfc9703ecf622`.
- Każdy wariant ma 30 pytań i 30 pozycji klucza; kolejność ID arkusza i klucza jest zgodna.
- Wariant 002 zawiera ADR-B-0078 — jego treść, kolejność odpowiedzi i explanation w kluczu zsynchronizowano. Pozostałe warianty zachowały wybór pytań; odświeżono metadane źródła.
- Każdy wariant nadal ma reprezentację wszystkich 13 działów i niepowtarzające się ID; szczegółowy balans liter/serii oraz synchronizację opcji ponownie sprawdzi Quality Gate.

## 6. Ograniczenia i dalsze kroki

Porównanie podobieństwa jest narzędziem redakcyjnym, nie dowodem zgodności prawnej. Podstawy prawne zmian wskazano przy każdym pytaniu, ale wszystkie rekordy pozostają `needs_review` do formalnego sprawdzenia przez specjalistę. Nie rozpoczęto pracy nad cysternami ani innym kursem.
