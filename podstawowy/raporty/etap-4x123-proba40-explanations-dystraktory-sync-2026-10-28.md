# Etap 4x123 — próbka 40, dystraktory, explanation i synchronizacja

- Data: 2026-10-28.
- Świeży punkt wejścia: `main` `945e07e9b32cf5194a734009968f3de5fa69e87a`; bank przed zmianami blob SHA `5d3bb481e372a45c89b30812841e76e9d91d542f`.
- Zakres: wyłącznie kurs podstawowy ADR.
- Próba deterministyczna: seed `41232026`; 544 ID wyłączone na podstawie skumulowanego manifestu 4x122 i zapisanych edycji/follow-upów; pula 65; próbka 40.

## Przegląd próbki

Każde pytanie przeczytano z opcjami A/B/C, poprawną literą, explanation, podstawą ADR i odpowiednim kontekstem lekcji. W 36 pytaniach nie potwierdzono potrzeby zmiany. W czterech pytaniach poprawiono wiarygodność błędnych wariantów i dopasowano explanation.

| ID | Dział | Wynik |
|---|---|---|
| ADR-B-0150 | ADR-B-02 | PASS redakcyjny; bez potwierdzonej potrzeby zmiany |
| ADR-B-0542 | ADR-B-02 | PASS redakcyjny; bez potwierdzonej potrzeby zmiany |
| ADR-B-0249 | ADR-B-12 | PASS redakcyjny; bez potwierdzonej potrzeby zmiany |
| ADR-B-0385 | ADR-B-10 | Poprawiono dystraktory i explanation |
| ADR-B-0360 | ADR-B-04 | PASS redakcyjny; bez potwierdzonej potrzeby zmiany |
| ADR-B-0215 | ADR-B-13 | PASS redakcyjny; bez potwierdzonej potrzeby zmiany |
| ADR-B-0387 | ADR-B-10 | Poprawiono dystraktory i explanation |
| ADR-B-0484 | ADR-B-08 | PASS redakcyjny; bez potwierdzonej potrzeby zmiany |
| ADR-B-0308 | ADR-B-11 | PASS redakcyjny; bez potwierdzonej potrzeby zmiany |
| ADR-B-0520 | ADR-B-01 | PASS redakcyjny; bez potwierdzonej potrzeby zmiany |
| ADR-B-0166 | ADR-B-05 | Poprawiono dystraktory i explanation |
| ADR-B-0366 | ADR-B-07 | PASS redakcyjny; bez potwierdzonej potrzeby zmiany |
| ADR-B-0515 | ADR-B-04 | PASS redakcyjny; bez potwierdzonej potrzeby zmiany |
| ADR-B-0590 | ADR-B-13 | PASS redakcyjny; bez potwierdzonej potrzeby zmiany |
| ADR-B-0162 | ADR-B-02 | PASS redakcyjny; bez potwierdzonej potrzeby zmiany |
| ADR-B-0427 | ADR-B-09 | PASS redakcyjny; bez potwierdzonej potrzeby zmiany |
| ADR-B-0327 | ADR-B-03 | PASS redakcyjny; bez potwierdzonej potrzeby zmiany |
| ADR-B-0117 | ADR-B-07 | PASS redakcyjny; bez potwierdzonej potrzeby zmiany |
| ADR-B-0268 | ADR-B-02 | PASS redakcyjny; bez potwierdzonej potrzeby zmiany |
| ADR-B-0153 | ADR-B-02 | PASS redakcyjny; bez potwierdzonej potrzeby zmiany |
| ADR-B-0021 | ADR-B-07 | PASS redakcyjny; bez potwierdzonej potrzeby zmiany |
| ADR-B-0007 | ADR-B-03 | PASS redakcyjny; bez potwierdzonej potrzeby zmiany |
| ADR-B-0472 | ADR-B-04 | PASS redakcyjny; bez potwierdzonej potrzeby zmiany |
| ADR-B-0152 | ADR-B-02 | PASS redakcyjny; bez potwierdzonej potrzeby zmiany |
| ADR-B-0539 | ADR-B-11 | PASS redakcyjny; bez potwierdzonej potrzeby zmiany |
| ADR-B-0450 | ADR-B-10 | PASS redakcyjny; bez potwierdzonej potrzeby zmiany |
| ADR-B-0136 | ADR-B-07 | PASS redakcyjny; bez potwierdzonej potrzeby zmiany |
| ADR-B-0519 | ADR-B-12 | PASS redakcyjny; bez potwierdzonej potrzeby zmiany |
| ADR-B-0383 | ADR-B-10 | PASS redakcyjny; bez potwierdzonej potrzeby zmiany |
| ADR-B-0380 | ADR-B-07 | PASS redakcyjny; bez potwierdzonej potrzeby zmiany |
| ADR-B-0393 | ADR-B-10 | PASS redakcyjny; bez potwierdzonej potrzeby zmiany |
| ADR-B-0259 | ADR-B-01 | PASS redakcyjny; bez potwierdzonej potrzeby zmiany |
| ADR-B-0024 | ADR-B-08 | Poprawiono dystraktory i explanation |
| ADR-B-0026 | ADR-B-09 | PASS redakcyjny; bez potwierdzonej potrzeby zmiany |
| ADR-B-0001 | ADR-B-01 | PASS redakcyjny; bez potwierdzonej potrzeby zmiany |
| ADR-B-0541 | ADR-B-02 | PASS redakcyjny; bez potwierdzonej potrzeby zmiany |
| ADR-B-0568 | ADR-B-07 | PASS redakcyjny; bez potwierdzonej potrzeby zmiany |
| ADR-B-0100 | ADR-B-03 | PASS redakcyjny; bez potwierdzonej potrzeby zmiany |
| ADR-B-0074 | ADR-B-08 | PASS redakcyjny; bez potwierdzonej potrzeby zmiany |
| ADR-B-0449 | ADR-B-10 | PASS redakcyjny; bez potwierdzonej potrzeby zmiany |

## Zmiany w próbce

1. **ADR-B-0024 — wyposażenie osobiste, ADR 8.1.5.2.** Zastąpiono absurdalne odpowiedzi o gaśnicy 12 kg na osobę i sprzęcie nurkowym wiarygodniejszymi pomyłkami: utożsamieniem wyposażenia pojazdu z osobistym oraz uznaniem, że ochrona oczu zastępuje rękawice. Wyjaśnienie tłumaczy różne funkcje wyposażenia.
2. **ADR-B-0166 — pożar przestrzeni ładunkowej, ADR 5.4.3.4.** Zastąpiono skrajne warianty o wejściu do ładowni i otwieraniu przesyłek scenariuszami, które mogą wydawać się rozsądne początkującemu: próbą użycia gaśnicy przy pozornie niewielkim ogniu oraz otwarciem drzwi, by ocenić sytuację. Explanation wyjaśnia, dlaczego oba działania zwiększają ryzyko.
3. **ADR-B-0385 — kontener-cysterna po transporcie morskim, ADR 1.1.4.2.1(c).** Zastąpiono arbitralny próg „10 km od portu” błędnym założeniem, że wymóg kończy się po zakończeniu odcinka morskiego. Explanation wyjaśnia, że sama odległość ani wyładunek ze statku nie rozstrzygają o stosowaniu reguły.
4. **ADR-B-0387 — wyjątek oznakowania w łańcuchu morskim, ADR 1.1.4.2.2 i 5.3.2.** Zastąpiono absurdalne warianty o braku dokumentów i reklamowej tablicy wariantami dotyczącymi pomylenia nalepek IMDG z tablicami pomarańczowymi ADR oraz nadmiernego rozszerzenia wyjątku na każdą trasę.

## Dwa jawne follow-upy poza próbką

Po zamknięciu bez scalania PR #585 przeniesiono do świeżej gałęzi dwie poprawki, które nie były częścią poprawnej, rozłącznej próby 4x122:
- **ADR-B-0326** — dopracowano dwa zbyt oczywiste dystraktory dotyczące wyłączenia procedury dla klasy 4.3 (ADR 2.1.3.5.5).
- **ADR-B-0361** — zastąpiono warianty z zapalniczką i wszystkimi odbiornikami bardziej realistycznymi pomyłkami dotyczącymi wentylatora i włączania urządzeń przy palnych oparach (ADR 5.4.3.4).

Te dwa rekordy są oznaczone jako follow-upy, a nie jako część próbki 40. We wszystkich sześciu pytaniach zachowano ID, poprawną literę i podstawę prawną. Łącznie poprawiono **11 dystraktorów** i przepisano **6 explanation**. Nie dodano nowych pytań i nie zmieniono statusów prawnych.

## Synchronizacja audytów i egzaminów

- Zsynchronizowano migaweczki `review/legal-clauses/` oraz `review/sequential/` dla ID 0024, 0166, 0326, 0361, 0385 i 0387. Zachowano `needs_review` i status oczekujący na pełne porównanie urzędowego tekstu polskiego.
- Warianty i klucze egzaminu próbnego 001–005 wskazują aktualny blob banku `dd247b2a1fe219c6b0a4643755c7cc820b842eeb`. Żaden ze zmienionych ID nie występuje w tych arkuszach, więc ich skład i rozkład liter nie wymagały zmian.

## Metryki po zmianach

- Bank: 609 pytań, bez duplikatów ID.
- „Poprawna = jedyna najdłuższa”: **69/609 = 11,33%**.
- Maksimum działu: **13,95%**.
- Explanation minimum: **300 znaków**; poniżej 200: **0**.
- Statusy: 609 `needs_review`, 0 `verified`.
- Aktualny blob SHA banku: `dd247b2a1fe219c6b0a4643755c7cc820b842eeb`.

## Ograniczenia

To przegląd dydaktyczny i redakcyjny, nie niezależna opinia prawna. Nie nadano statusu `verified`; nie rozpoczęto kursu cystern ani innego kursu.
