# Etap 4x226 — audyt pokrycia po drugim przeglądzie explanation

Data: 31.10.2026. Zakres: wyłącznie kurs początkowy ADR podstawowy. Audyt wykonano na świeżym `main` `ad287ebcdec8cc7f9fe79b0252a6379d4165aa44`.
Bank: 651 rekordów `ADR-B-0001`–`ADR-B-0651`, wszystkie `needs_review`, zero `verified`. Blob SHA `questions.jsonl`: `803cae392630b0fe441c6dd1819269045526e52e`.

## 1. Metoda i zakres danych

Porównano:
- `podstawowy/kompetencje.json`: 107 roboczych kompetencji (104 teoretyczne, 3 praktyczne);
- wszystkie 651 rekordów `podstawowy/questions.jsonl`, ich `module_id`, treści, odpowiedzi, wyjaśnienia i podstawy;
- 13 lekcji `podstawowy/lekcje/ADR-B-01.md`–`ADR-B-13.md`;
- program kursu w `docs/PROGRAM-PODSTAWOWY.md`, matrycę `docs/POKRYCIE-KURSU.md`, walidator `scripts/coverage.py` i test głębokości kompetencji;
- podobieństwo treści pytań przez algorytm z `scripts/similarity.py`: tokenizacja bez polskich znaków, stoplista, Jaccard na treści pytania, próg 0,45, porównanie tylko w obrębie tego samego działu.

Mapa 107 kompetencji jest wewnętrznym podziałem redakcyjnym, nie urzędowym wykazem 107 wymagań. Cele praktyczne wymagają realnych ćwiczeń pod nadzorem; pytania nie zastępują zajęć praktycznych.

## 2. Głębokość pokrycia kompetencji

- 107/107 kompetencji ma prawidłowe przypisania do istniejących rekordów banku.
- 104/104 kompetencji teoretycznych ma co najmniej dwa pytania robocze; 0 ma 0–2 pytania.
- Najmniej pytań ma `ADR-B-07-K07` — „Podstawowe rozróżnienie odpowiedzialności cywilnej za szkodę i za niewykonanie zobowiązania”: **3 pytania** (`ADR-B-0567`, `0568`, `0569`). To minimum w mapie, ale nie jest potwierdzoną luką: trzy pytania obejmują odpowiedzialność deliktową (art. 415 KC), kontraktową (art. 471 KC) i brak automatyzmu przypisania kierowcy całej szkody. Lekcja B-07 ma osobną sekcję „Odpowiedzialność cywilna” i wyjaśnia, że nie jest tożsama z podziałem obowiązków ADR.
- Pozostałe 103 kompetencje teoretyczne mają po 4–23 pytania. Rozkład: 3 pytania — 1 kompetencja; 4 — 55; 5 — 14; 6 — 8; 7 — 9; 8 — 2; 9 — 3; 10 — 2; 11 — 4; 12 — 1; 13 — 2; 14 — 1; 15 — 1; 16 — 1; 17 — 1; 19 — 1; 23 — 1.
- 3 kompetencje praktyczne mają po 4 pytania/scenariusze wspierające: gaśnica, pierwsza pomoc, postępowanie przy wypadku/awarii. To nie stanowi dowodu przeprowadzenia ćwiczeń.

### Kompetencja o najniższym pokryciu

| Kompetencja | Liczba | ID | Ocena |
|---|---:|---|---|
| ADR-B-07-K07 — odpowiedzialność cywilna | 3 | 0567, 0568, 0569 | Minimum w mapie; obecne trzy odrębne aspekty i omówienie w lekcji. Brak potwierdzonej luki do dopisania pytania. |

Nie dopisano pytania ADR-B-0652: obecna analiza nie wykazała potwierdzonego braku treści, a zwiększanie liczby pytań wyłącznie dla podniesienia licznika nie poprawiałoby jakości. Kolejny wolny identyfikator pozostaje ADR-B-0652.

## 3. Pokrycie 13 działów i lekcji

Wszystkie 13 plików lekcji istnieje i odpowiada działom ADR-B-01–13. Każdy dział ma pytania przypisane w banku i kompetencjach. Liczby pytań w banku według `module_id` (bez podwójnego liczenia kompetencji, gdy jedno pytanie wspiera więcej niż jeden cel):

| Dział / lekcja | Pytania | Cel roboczy programu | Różnica |
|---|---:|---:|---:|
| ADR-B-01 — Wymagania ogólne | 47 | 30 | +17 |
| ADR-B-02 — Klasyfikacja i zagrożenia | 63 | 40 | +23 |
| ADR-B-03 — Środowisko i odpady | 52 | 20 | +32 |
| ADR-B-04 — Zapobieganie zagrożeniom | 46 | 25 | +21 |
| ADR-B-05 — Wypadek, pierwsza pomoc, sprzęt | 61 | 35 | +26 |
| ADR-B-06 — Nalepki, znaki i tablice | 52 | 45 | +7 |
| ADR-B-07 — Obowiązki uczestników | 48 | 35 | +13 |
| ADR-B-08 — Wyposażenie pojazdu | 42 | 40 | +2 |
| ADR-B-09 — Załadunek i mocowanie | 50 | 45 | +5 |
| ADR-B-10 — Transport kombinowany | 55 | 15 | +40 |
| ADR-B-11 — Przejazd przez tunele | 43 | 25 | +18 |
| ADR-B-12 — Ochrona przewozu | 44 | 20 | +24 |
| ADR-B-13 — Dokumentacja ADR | 48 | 25 | +23 |
| **Razem** | **651** | **400** | **+251** |

Cele ilościowe są wewnętrznymi celami redakcyjnymi, nie prawnymi minimami ani oficjalną proporcją egzaminacyjną. Wszystkie działy osiągają swoje założone liczby. B-08 jest najbliżej celu (+2), następnie B-09 (+5), B-06 (+7), ale nie stwierdzono braku tematu w tych działach. Nie należy dodawać pytań wyłącznie w celu zwiększenia licznika.

## 4. Podobieństwo pytań — kandydaci do przeglądu redakcyjnego

Skrypt `scripts/similarity.py` zwrócił 12 par o Jaccard ≥ 0,45 w obrębie tego samego działu. Wynik wskazuje podobieństwo sformułowania, a nie duplikat merytoryczny ani błąd prawny.

| Wynik | Pary | Temat | Ocena po ręcznym porównaniu |
|---:|---|---|---|
| 0,909 | 0071 / 0072 | Minimalna pojemność gaśnic dla DMC 3,5 t i 6 t | Najsilniejsza zbieżność szablonu. Różne przedziały DMC i różne prawidłowe minima (4 kg / 8 kg); nie są duplikatami, ale warto rozróżnić scenariusze przy przyszłej redakcji. |
| 0,636 | 0330 / 0337 | Procedura klasyfikacji odpadu 2.1.3.5.5 | Ta sama reguła sprawdzana dla dwóch różnych klas (5.2 i 6.2); celowo bada granice wyłączenia, lecz sformułowania są bliskie. Zachować rozróżnienie klas. |
| 0,538 | 0505 / 0545 | Cyfry 9 i 7 w numerze rozpoznawczym zagrożenia | Różne cyfry i różne rodzaje zagrożenia. |
| 0,500 | 0017 / 0052 | Litera X i kolor tablicy pomarańczowej | Różne elementy tablicy i różne przepisy. |
| 0,500 | 0022 / 0419 | Gaśnice: DMC powyżej 7,5 t i dokładnie 7,5 t | Ważna granica przedziału; nie duplikaty, ale pytania są bardzo podobnie zbudowane. |
| 0,500 | 0042 / 0096 | Klasy 2 i 5.2 | Pytania rozpoznawcze o różne klasy. |
| 0,500 | 0051 / 0194 | Powtórzenie cyfry w numerze zagrożenia i konkretny numer 88 | Drugi rekord jest zastosowaniem reguły do konkretnego numeru; częściowe powtórzenie. |
| 0,500 | 0153 / 0159 | Rozróżnienie klas 4.1/4.3 i 6.2/6.1 | Różne pary klas i inne zagrożenia. |
| 0,500 | 0194 / 0503 | Cyfra 8 powtórzona i cyfra 3 w numerze zagrożenia | Inne znaczenie cyfry; różne reguły odczytu. |
| 0,500 | 0223 / 0493 | Bezpieczna decyzja o użyciu gaśnicy przy małym pożarze | Różne części pojazdu (opona / hamulce); podobna zasada bezpieczeństwa. |
| 0,462 | 0304 / 0400 | Elementy planu ochrony towarów dużego ryzyka | Różne elementy planu (odpowiedzialność / zakres towarów). |
| 0,455 | 0245 / 0584 | Uszkodzona sztuka przesyłki przed załadunkiem | Jedno pytanie dotyczy wycieku, drugie widocznego uszkodzenia; bliski kontekst, ale inne okoliczności. |

**Wniosek:** dwie pary (0071/0072 i 0330/0337) są najsilniejszymi kandydatami do redakcyjnego odróżnienia stemów. Po ręcznym porównaniu nie potwierdzono identycznych pytań ani równoważnych odpowiedzi. Pozostałe pary sprawdzają różne wartości, klasy, progi lub elementy przepisu. Nie usuwano ani nie przepisywano pytań bez potwierdzonej wady. Ranking ma ograniczenia opisane w samym skrypcie: nie rozpoznaje wszystkich parafraz, nie bada semantycznej równoważności i nie potwierdza zgodności prawnej.

## 5. Decyzja o nowych pytaniach

**W tej partii nie dopisano nowych pytań.** Mapa nie zawiera kompetencji teoretycznej z 0–2 pytaniami, wszystkie 13 działów przekracza robocze cele ilościowe, a ręczna kontrola 12 par podobieństwa nie potwierdziła duplikatu ani merytorycznej luki wymagającej nowego rekordu. Nie ma zatem podstaw do tworzenia ADR-B-0652 tylko dla zwiększenia liczby.

Bank pozostał bez zmian: 651 rekordów, wszystkie `needs_review`, zero `verified`. Nie zmieniano treści pytań, kluczy ani źródeł. Nie zmieniano egzaminów próbnych, snapshotów ani SHA banku, ponieważ `questions.jsonl` nie został zmieniony.

## 6. Ograniczenia i dalsze prace

- Obecność pytań nie oznacza ich niezależnego zatwierdzenia prawnego. 651/651 pozostaje `needs_review`.
- Trzy kompetencje praktyczne wymagają rzeczywistych ćwiczeń i odbioru instruktora; pytania i scenariusze są tylko materiałem wspierającym.
- Podobieństwo językowe jest heurystyką. Dalsza redakcja par o wysokim wyniku powinna zachować różnice progów i warunków, nie zmieniając prawidłowych odpowiedzi.
- Następny przegląd może skoncentrować się na dwóch parach o najwyższym podobieństwie i na kontroli, czy lekcje wyjaśniają granice między tymi przypadkami.

## Źródła

- ADR 2025, Dz.U. 2025 poz. 642: https://dziennikustaw.gov.pl/DU/2025/642
- Oficjalna strona UNECE — ADR 2025, wersja obowiązująca od 1.01.2025: https://unece.org/adr-2025-files
- Program kursu początkowego podstawowego, Dz.U. 2021 poz. 2150, załącznik nr 1: https://eli.gov.pl/api/acts/DU/2021/2150/text.pdf
- ADR 2025, 8.2.2.3.2(k): minimum programu szkolenia obejmuje ogólne informacje o odpowiedzialności cywilnej.
- Kodeks cywilny, art. 415 i 471: odrębne podstawy odpowiedzialności deliktowej i kontraktowej, wskazane w mapie kompetencji ADR-B-07-K07.
