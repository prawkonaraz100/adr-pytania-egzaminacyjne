# ETAP 4a — pełny przesiew jakości 506 pytań (23.10.2026)

> Status: **przesiew całego banku, nie audyt merytoryczny ani decyzja specjalisty**. Dla każdego ID niżej podano wynik zestawu reguł i proponowaną poprawkę. Flagi oznaczają potrzebę manualnej kontroli, nie automatyczne potwierdzenie błędu prawnego. Analizowano `main` na wejściu: ADR-B-0001–0506, 506 needs_review, 0 verified, brak otwartych PR. Klucz odpowiedzi we wszystkich rekordach pozostaje niezmieniony.

## Metoda i wyniki

- **DWA-SKRAJNE:** oba błędne warianty zawierają sformułowania typu „zawsze”, „nigdy”, „wyłącznie” lub inny podejrzanie skrajny/niepoważny zwrot; wymaga interpretacji kontekstu, bo nie każde „wyłącznie” jest błędem.
- **DŁUGOŚĆ:** stosunek długości najdłuższego do najkrótszego wariantu > 2,25 (metryka znaków).
- **KLUCZ-DŁUŻSZY:** poprawna odpowiedź > 1,65 × dłuższa od każdego błędnego wariantu.
- **BRAK-PUNKTU-W-WYJAŚNIENIU:** nie wykryto konkretnego numeru przepisu w samym wyjaśnieniu. **Nie oznacza to braku źródła!** Każdy rekord ma osobne pole `sources`; sprawdzenie ich trafności należy do specjalisty.
- **OGÓLNE:** pytanie krótsze niż 65 znaków; to sygnał możliwej zbyt prostej konstrukcji, nie wada sama w sobie.
- **SPRAWDŹ-WARUNEK:** pytanie zawiera bezwzględny lub szeroki kwantyfikator, którego znaczenie trzeba sprawdzić z warunkami ADR.

**Wyniki surowych reguł (przed korektami):** 472/506 z co najmniej jedną flagą, 73 z dwiema skrajnymi alternatywami, 162 z dysproporcją długości, 147 z najdłuższym poprawnym wariantem, 434 bez numeru punktu w wyjaśnieniu, 23 z krótkim pytaniem, 31 ze sformułowaniem wymagającym kontroli warunków. Flagi mogą się nakładać.

**Nie dokonano masowej automatycznej redakcji**: bez przejrzenia dokładnego prawa takie działanie mogłoby zmienić znaczenie prawidłowych dystraktorów lub warunków. Potwierdzone i poprawione redakcyjnie tylko dwa przypadki ADR-B-0503 oraz 0505; cała reszta w kolejce eksperckiej. Wszelkie zatwierdzenia 0; statusy pozostają `needs_review`.

## Rozkład na działy

| Dział | Wszystkie | Co najmniej jedna flaga |
|---|---:|---:|
| ADR-B-01 | 25 | 23 |
| ADR-B-02 | 53 | 52 |
| ADR-B-03 | 48 | 45 |
| ADR-B-04 | 43 | 42 |
| ADR-B-05 | 39 | 39 |
| ADR-B-06 | 31 | 31 |
| ADR-B-07 | 42 | 41 |
| ADR-B-08 | 35 | 31 |
| ADR-B-09 | 38 | 31 |
| ADR-B-10 | 54 | 48 |
| ADR-B-11 | 32 | 28 |
| ADR-B-12 | 42 | 41 |
| ADR-B-13 | 24 | 20 |

## Zweryfikowane poprawki w tej partii

- **ADR-B-0503,** ADR 2025, 5.3.2.3.1: oba wcześniejsze dystraktory były oczywiście błędne i naprowadzały „wyłącznie”; zastąpiono je opisami realnych kategorii zagrożeń mylonych z cyfrą 3. Zapisano konkretny ustęp w wyjaśnieniu, zachowano literę **A**, zakres i status.
- **ADR-B-0505,** ADR 2025, 5.3.2.3.1: zastąpiono niepoważny dystraktor o ciężarze opakowania opisem właściwości utleniającej, a „wyłącznie radioaktywność” opisem promieniowania. Zapisano ustęp w wyjaśnieniu, zachowano literę **C**, zakres i status.
- Odświeżono `review/sequential/503-506.json` i `review/legal-clauses/503-506.json`. **Nie wpisano zatwierdzenia eksperta ani pełnego porównania urzędowego polskiego tekstu.** Zewnętrzna podstawa prawna: [Dz.U. 2025 poz. 642](https://dziennikustaw.gov.pl/DU/2025/642) i [sprostowanie poz. 1575](https://dziennikustaw.gov.pl/DU/2025/1575).

## Lista wszystkich rekordów: ID → sygnał → sugerowana poprawka

| ID | Dział | Sygnały jakościowe | Długość max/min | Proponowane działanie | Stan |
|---|---|---|---:|---|---|
| ADR-B-0001 | ADR-B-01 | DWA-SKRAJNE, BRAK-PUNKTU-W-WYJAŚNIENIU | 1.96 | zastąpić skrajne dystraktory realistycznymi błędnymi interpretacjami przepisu; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 1.3.2 | DO-RECENZJI |
| ADR-B-0002 | ADR-B-01 | BRAK-PUNKTU-W-WYJAŚNIENIU, SPRAWDŹ-WARUNEK | 1.53 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 1.1.3; sprawdzić konieczność doprecyzowania sytuacji i wyjątku | DO-RECENZJI |
| ADR-B-0003 | ADR-B-01 | DŁUGOŚĆ, BRAK-PUNKTU-W-WYJAŚNIENIU, OGÓLNE | 3.86 | wyrównać długości i szczegółowość wariantów bez zmiany klucza; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 8.2.1; sprawdzić konieczność doprecyzowania sytuacji i wyjątku | DO-RECENZJI |
| ADR-B-0004 | ADR-B-02 | BRAK-PUNKTU-W-WYJAŚNIENIU | 1.29 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 2.2.3.1.1 | DO-RECENZJI |
| ADR-B-0005 | ADR-B-02 | BRAK-PUNKTU-W-WYJAŚNIENIU, OGÓLNE | 1.80 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 2.2.8.1.1; sprawdzić konieczność doprecyzowania sytuacji i wyjątku | DO-RECENZJI |
| ADR-B-0006 | ADR-B-02 | DWA-SKRAJNE, BRAK-PUNKTU-W-WYJAŚNIENIU, OGÓLNE | 1.38 | zastąpić skrajne dystraktory realistycznymi błędnymi interpretacjami przepisu; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 2.2.43.1.1; sprawdzić konieczność doprecyzowania sytuacji i wyjątku | DO-RECENZJI |
| ADR-B-0007 | ADR-B-03 | BRAK-PUNKTU-W-WYJAŚNIENIU | 1.32 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 5.2.1.8 | DO-RECENZJI |
| ADR-B-0008 | ADR-B-03 | brak flag | 1.77 | nie wykryto sygnału w przesiewie; pozostawić do oceny eksperckiej | DO-RECENZJI |
| ADR-B-0009 | ADR-B-03 | BRAK-PUNKTU-W-WYJAŚNIENIU | 1.56 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 7.5.8.1 | DO-RECENZJI |
| ADR-B-0010 | ADR-B-04 | DŁUGOŚĆ, KLUCZ-DŁUŻSZY, BRAK-PUNKTU-W-WYJAŚNIENIU | 2.61 | wyrównać długości i szczegółowość wariantów bez zmiany klucza; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 8.3.5 | DO-RECENZJI |
| ADR-B-0011 | ADR-B-04 | BRAK-PUNKTU-W-WYJAŚNIENIU | 1.41 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 8.3.3 | DO-RECENZJI |
| ADR-B-0012 | ADR-B-04 | DŁUGOŚĆ, KLUCZ-DŁUŻSZY, BRAK-PUNKTU-W-WYJAŚNIENIU, SPRAWDŹ-WARUNEK | 2.75 | wyrównać długości i szczegółowość wariantów bez zmiany klucza; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 8.3.6; sprawdzić konieczność doprecyzowania sytuacji i wyjątku | DO-RECENZJI |
| ADR-B-0013 | ADR-B-05 | BRAK-PUNKTU-W-WYJAŚNIENIU | 1.65 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 5.4.3.1 | DO-RECENZJI |
| ADR-B-0014 | ADR-B-05 | DŁUGOŚĆ, KLUCZ-DŁUŻSZY, BRAK-PUNKTU-W-WYJAŚNIENIU | 2.48 | wyrównać długości i szczegółowość wariantów bez zmiany klucza; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 5.4.3.3 | DO-RECENZJI |
| ADR-B-0015 | ADR-B-05 | BRAK-PUNKTU-W-WYJAŚNIENIU, OGÓLNE | 1.10 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 8.1.4.5; sprawdzić konieczność doprecyzowania sytuacji i wyjątku | DO-RECENZJI |
| ADR-B-0016 | ADR-B-06 | BRAK-PUNKTU-W-WYJAŚNIENIU | 1.21 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 5.3.2.2.2 | DO-RECENZJI |
| ADR-B-0017 | ADR-B-06 | DŁUGOŚĆ, BRAK-PUNKTU-W-WYJAŚNIENIU | 3.00 | wyrównać długości i szczegółowość wariantów bez zmiany klucza; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 5.3.2.3.1 | DO-RECENZJI |
| ADR-B-0018 | ADR-B-06 | BRAK-PUNKTU-W-WYJAŚNIENIU, OGÓLNE | 1.00 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 5.3.2.2.1; sprawdzić konieczność doprecyzowania sytuacji i wyjątku | DO-RECENZJI |
| ADR-B-0019 | ADR-B-07 | BRAK-PUNKTU-W-WYJAŚNIENIU | 2.00 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 1.4.2.2.6; 5.4.3.2 | DO-RECENZJI |
| ADR-B-0020 | ADR-B-07 | BRAK-PUNKTU-W-WYJAŚNIENIU | 1.41 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 1.4.3.1.1 (b) | DO-RECENZJI |
| ADR-B-0021 | ADR-B-07 | DŁUGOŚĆ, BRAK-PUNKTU-W-WYJAŚNIENIU | 6.00 | wyrównać długości i szczegółowość wariantów bez zmiany klucza; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 1.4.2.1.1 (a) | DO-RECENZJI |
| ADR-B-0022 | ADR-B-08 | BRAK-PUNKTU-W-WYJAŚNIENIU | 1.25 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 8.1.4.1 | DO-RECENZJI |
| ADR-B-0023 | ADR-B-08 | DŁUGOŚĆ, BRAK-PUNKTU-W-WYJAŚNIENIU | 3.11 | wyrównać długości i szczegółowość wariantów bez zmiany klucza; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 8.1.5.2 | DO-RECENZJI |
| ADR-B-0024 | ADR-B-08 | BRAK-PUNKTU-W-WYJAŚNIENIU | 2.06 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 8.1.5.2 | DO-RECENZJI |
| ADR-B-0025 | ADR-B-09 | brak flag | 1.66 | nie wykryto sygnału w przesiewie; pozostawić do oceny eksperckiej | DO-RECENZJI |
| ADR-B-0026 | ADR-B-09 | BRAK-PUNKTU-W-WYJAŚNIENIU, OGÓLNE | 1.88 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 7.5.7.1; sprawdzić konieczność doprecyzowania sytuacji i wyjątku | DO-RECENZJI |
| ADR-B-0027 | ADR-B-09 | brak flag | 1.12 | nie wykryto sygnału w przesiewie; pozostawić do oceny eksperckiej | DO-RECENZJI |
| ADR-B-0028 | ADR-B-10 | DWA-SKRAJNE, BRAK-PUNKTU-W-WYJAŚNIENIU | 1.90 | zastąpić skrajne dystraktory realistycznymi błędnymi interpretacjami przepisu; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 1.1.4.2 | DO-RECENZJI |
| ADR-B-0029 | ADR-B-10 | DŁUGOŚĆ | 7.70 | wyrównać długości i szczegółowość wariantów bez zmiany klucza | DO-RECENZJI |
| ADR-B-0030 | ADR-B-10 | BRAK-PUNKTU-W-WYJAŚNIENIU | 1.85 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 1.1.4.2 | DO-RECENZJI |
| ADR-B-0031 | ADR-B-11 | KLUCZ-DŁUŻSZY, BRAK-PUNKTU-W-WYJAŚNIENIU, OGÓLNE | 2.07 | wyrównać długości i szczegółowość wariantów bez zmiany klucza; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 1.9.5.2.2; 8.6; sprawdzić konieczność doprecyzowania sytuacji i wyjątku | DO-RECENZJI |
| ADR-B-0032 | ADR-B-11 | brak flag | 1.20 | nie wykryto sygnału w przesiewie; pozostawić do oceny eksperckiej | DO-RECENZJI |
| ADR-B-0033 | ADR-B-11 | BRAK-PUNKTU-W-WYJAŚNIENIU | 1.72 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 8.6.4 | DO-RECENZJI |
| ADR-B-0034 | ADR-B-12 | BRAK-PUNKTU-W-WYJAŚNIENIU | 1.57 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 1.10.1.4 | DO-RECENZJI |
| ADR-B-0035 | ADR-B-12 | KLUCZ-DŁUŻSZY, BRAK-PUNKTU-W-WYJAŚNIENIU | 1.70 | wyrównać długości i szczegółowość wariantów bez zmiany klucza; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 1.10.1.3 | DO-RECENZJI |
| ADR-B-0036 | ADR-B-12 | DWA-SKRAJNE, BRAK-PUNKTU-W-WYJAŚNIENIU | 1.15 | zastąpić skrajne dystraktory realistycznymi błędnymi interpretacjami przepisu; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 1.10.2.2 | DO-RECENZJI |
| ADR-B-0037 | ADR-B-13 | BRAK-PUNKTU-W-WYJAŚNIENIU | 1.31 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 5.4.1.1.1 (a) | DO-RECENZJI |
| ADR-B-0038 | ADR-B-13 | BRAK-PUNKTU-W-WYJAŚNIENIU | 1.04 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 5.4.1.1.1 (b) | DO-RECENZJI |
| ADR-B-0039 | ADR-B-13 | BRAK-PUNKTU-W-WYJAŚNIENIU, OGÓLNE | 1.60 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 5.4.3.4; sprawdzić konieczność doprecyzowania sytuacji i wyjątku | DO-RECENZJI |
| ADR-B-0040 | ADR-B-01 | BRAK-PUNKTU-W-WYJAŚNIENIU | 1.29 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 1.3.1 | DO-RECENZJI |
| ADR-B-0041 | ADR-B-01 | BRAK-PUNKTU-W-WYJAŚNIENIU | 1.60 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 1.3.2.4 | DO-RECENZJI |
| ADR-B-0042 | ADR-B-02 | BRAK-PUNKTU-W-WYJAŚNIENIU, OGÓLNE | 1.00 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 2.2.2.1.1; sprawdzić konieczność doprecyzowania sytuacji i wyjątku | DO-RECENZJI |
| ADR-B-0043 | ADR-B-02 | DŁUGOŚĆ, BRAK-PUNKTU-W-WYJAŚNIENIU, OGÓLNE | 3.22 | wyrównać długości i szczegółowość wariantów bez zmiany klucza; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 2.2.62.1.1; sprawdzić konieczność doprecyzowania sytuacji i wyjątku | DO-RECENZJI |
| ADR-B-0044 | ADR-B-02 | DŁUGOŚĆ, KLUCZ-DŁUŻSZY, BRAK-PUNKTU-W-WYJAŚNIENIU, OGÓLNE | 3.21 | wyrównać długości i szczegółowość wariantów bez zmiany klucza; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 2.2.51.1.1; sprawdzić konieczność doprecyzowania sytuacji i wyjątku | DO-RECENZJI |
| ADR-B-0045 | ADR-B-03 | BRAK-PUNKTU-W-WYJAŚNIENIU | 1.42 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 5.2.1.8 | DO-RECENZJI |
| ADR-B-0046 | ADR-B-03 | DŁUGOŚĆ, BRAK-PUNKTU-W-WYJAŚNIENIU | 7.36 | wyrównać długości i szczegółowość wariantów bez zmiany klucza; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 5.4.1.1.1 (a); 5.4.1.1.3.1 | DO-RECENZJI |
| ADR-B-0047 | ADR-B-04 | BRAK-PUNKTU-W-WYJAŚNIENIU | 1.55 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 8.3.6 | DO-RECENZJI |
| ADR-B-0048 | ADR-B-04 | brak flag | 1.33 | nie wykryto sygnału w przesiewie; pozostawić do oceny eksperckiej | DO-RECENZJI |
| ADR-B-0049 | ADR-B-05 | BRAK-PUNKTU-W-WYJAŚNIENIU | 1.15 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 5.4.3.3 | DO-RECENZJI |
| ADR-B-0050 | ADR-B-05 | DWA-SKRAJNE, DŁUGOŚĆ, BRAK-PUNKTU-W-WYJAŚNIENIU | 3.41 | zastąpić skrajne dystraktory realistycznymi błędnymi interpretacjami przepisu; wyrównać długości i szczegółowość wariantów bez zmiany klucza; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 5.4.3.2 | DO-RECENZJI |
| ADR-B-0051 | ADR-B-06 | BRAK-PUNKTU-W-WYJAŚNIENIU | 1.52 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 5.3.2.3.1 | DO-RECENZJI |
| ADR-B-0052 | ADR-B-06 | BRAK-PUNKTU-W-WYJAŚNIENIU | 1.44 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 5.3.2.2.2 | DO-RECENZJI |
| ADR-B-0053 | ADR-B-06 | BRAK-PUNKTU-W-WYJAŚNIENIU | 1.69 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 5.3.2.3.1 | DO-RECENZJI |
| ADR-B-0054 | ADR-B-07 | DŁUGOŚĆ, BRAK-PUNKTU-W-WYJAŚNIENIU | 3.47 | wyrównać długości i szczegółowość wariantów bez zmiany klucza; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 1.4.3.1.1 (b) | DO-RECENZJI |
| ADR-B-0055 | ADR-B-07 | DŁUGOŚĆ, BRAK-PUNKTU-W-WYJAŚNIENIU | 8.57 | wyrównać długości i szczegółowość wariantów bez zmiany klucza; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 1.4.2.1.1 | DO-RECENZJI |
| ADR-B-0056 | ADR-B-08 | DŁUGOŚĆ, BRAK-PUNKTU-W-WYJAŚNIENIU | 3.77 | wyrównać długości i szczegółowość wariantów bez zmiany klucza; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 8.1.5.2 | DO-RECENZJI |
| ADR-B-0057 | ADR-B-08 | DŁUGOŚĆ, BRAK-PUNKTU-W-WYJAŚNIENIU | 2.48 | wyrównać długości i szczegółowość wariantów bez zmiany klucza; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 8.1.5.2 | DO-RECENZJI |
| ADR-B-0058 | ADR-B-09 | DŁUGOŚĆ, BRAK-PUNKTU-W-WYJAŚNIENIU | 2.90 | wyrównać długości i szczegółowość wariantów bez zmiany klucza; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 7.5.1.5 | DO-RECENZJI |
| ADR-B-0059 | ADR-B-09 | DŁUGOŚĆ, BRAK-PUNKTU-W-WYJAŚNIENIU | 20.00 | wyrównać długości i szczegółowość wariantów bez zmiany klucza; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 7.5.7.2 | DO-RECENZJI |
| ADR-B-0060 | ADR-B-09 | BRAK-PUNKTU-W-WYJAŚNIENIU | 1.83 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 7.5.7.1 | DO-RECENZJI |
| ADR-B-0061 | ADR-B-10 | BRAK-PUNKTU-W-WYJAŚNIENIU | 1.08 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 5.4.1.1.7 | DO-RECENZJI |
| ADR-B-0062 | ADR-B-10 | DWA-SKRAJNE, BRAK-PUNKTU-W-WYJAŚNIENIU, SPRAWDŹ-WARUNEK | 1.47 | zastąpić skrajne dystraktory realistycznymi błędnymi interpretacjami przepisu; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 1.1.4.2; sprawdzić konieczność doprecyzowania sytuacji i wyjątku | DO-RECENZJI |
| ADR-B-0063 | ADR-B-11 | BRAK-PUNKTU-W-WYJAŚNIENIU | 1.00 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 8.6.3.1 | DO-RECENZJI |
| ADR-B-0064 | ADR-B-11 | brak flag | 1.96 | nie wykryto sygnału w przesiewie; pozostawić do oceny eksperckiej | DO-RECENZJI |
| ADR-B-0065 | ADR-B-11 | DŁUGOŚĆ, BRAK-PUNKTU-W-WYJAŚNIENIU | 2.50 | wyrównać długości i szczegółowość wariantów bez zmiany klucza; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 8.6.3.1 | DO-RECENZJI |
| ADR-B-0066 | ADR-B-12 | BRAK-PUNKTU-W-WYJAŚNIENIU | 1.41 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 1.10.1.3 | DO-RECENZJI |
| ADR-B-0067 | ADR-B-12 | BRAK-PUNKTU-W-WYJAŚNIENIU, SPRAWDŹ-WARUNEK | 1.22 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 1.10.1.4; sprawdzić konieczność doprecyzowania sytuacji i wyjątku | DO-RECENZJI |
| ADR-B-0068 | ADR-B-13 | DŁUGOŚĆ, BRAK-PUNKTU-W-WYJAŚNIENIU, SPRAWDŹ-WARUNEK | 2.27 | wyrównać długości i szczegółowość wariantów bez zmiany klucza; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 5.4.1.1.1 (h); sprawdzić konieczność doprecyzowania sytuacji i wyjątku | DO-RECENZJI |
| ADR-B-0069 | ADR-B-13 | BRAK-PUNKTU-W-WYJAŚNIENIU | 1.23 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 5.4.1.1.1 (e) | DO-RECENZJI |
| ADR-B-0070 | ADR-B-13 | BRAK-PUNKTU-W-WYJAŚNIENIU | 1.24 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 5.4.1.1.1 (f) | DO-RECENZJI |
| ADR-B-0071 | ADR-B-08 | brak flag | 1.02 | nie wykryto sygnału w przesiewie; pozostawić do oceny eksperckiej | DO-RECENZJI |
| ADR-B-0072 | ADR-B-08 | BRAK-PUNKTU-W-WYJAŚNIENIU | 1.03 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 8.1.4.1 | DO-RECENZJI |
| ADR-B-0073 | ADR-B-08 | brak flag | 1.62 | nie wykryto sygnału w przesiewie; pozostawić do oceny eksperckiej | DO-RECENZJI |
| ADR-B-0074 | ADR-B-08 | BRAK-PUNKTU-W-WYJAŚNIENIU | 1.02 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 8.1.4.4; 8.1.4.5 | DO-RECENZJI |
| ADR-B-0075 | ADR-B-08 | BRAK-PUNKTU-W-WYJAŚNIENIU | 1.38 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 8.1.5.2 | DO-RECENZJI |
| ADR-B-0076 | ADR-B-08 | DWA-SKRAJNE, BRAK-PUNKTU-W-WYJAŚNIENIU | 1.41 | zastąpić skrajne dystraktory realistycznymi błędnymi interpretacjami przepisu; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 8.1.5.2 | DO-RECENZJI |
| ADR-B-0077 | ADR-B-08 | BRAK-PUNKTU-W-WYJAŚNIENIU | 1.09 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 8.1.5.3 | DO-RECENZJI |
| ADR-B-0078 | ADR-B-09 | BRAK-PUNKTU-W-WYJAŚNIENIU | 1.25 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 7.5.7.2 | DO-RECENZJI |
| ADR-B-0079 | ADR-B-09 | BRAK-PUNKTU-W-WYJAŚNIENIU | 1.22 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 7.5.7.1 | DO-RECENZJI |
| ADR-B-0080 | ADR-B-09 | BRAK-PUNKTU-W-WYJAŚNIENIU | 1.21 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 7.5.8.1 | DO-RECENZJI |
| ADR-B-0081 | ADR-B-09 | brak flag | 1.13 | nie wykryto sygnału w przesiewie; pozostawić do oceny eksperckiej | DO-RECENZJI |
| ADR-B-0082 | ADR-B-09 | DŁUGOŚĆ, KLUCZ-DŁUŻSZY | 3.03 | wyrównać długości i szczegółowość wariantów bez zmiany klucza | DO-RECENZJI |
| ADR-B-0083 | ADR-B-11 | BRAK-PUNKTU-W-WYJAŚNIENIU | 1.45 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 8.6.4 | DO-RECENZJI |
| ADR-B-0084 | ADR-B-11 | BRAK-PUNKTU-W-WYJAŚNIENIU | 1.71 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 8.6.4 | DO-RECENZJI |
| ADR-B-0085 | ADR-B-11 | brak flag | 2.11 | nie wykryto sygnału w przesiewie; pozostawić do oceny eksperckiej | DO-RECENZJI |
| ADR-B-0086 | ADR-B-11 | brak flag | 1.74 | nie wykryto sygnału w przesiewie; pozostawić do oceny eksperckiej | DO-RECENZJI |
| ADR-B-0087 | ADR-B-13 | brak flag | 1.57 | nie wykryto sygnału w przesiewie; pozostawić do oceny eksperckiej | DO-RECENZJI |
| ADR-B-0088 | ADR-B-13 | BRAK-PUNKTU-W-WYJAŚNIENIU, SPRAWDŹ-WARUNEK | 1.71 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 5.4.3.4; sprawdzić konieczność doprecyzowania sytuacji i wyjątku | DO-RECENZJI |
| ADR-B-0089 | ADR-B-13 | brak flag | 1.08 | nie wykryto sygnału w przesiewie; pozostawić do oceny eksperckiej | DO-RECENZJI |
| ADR-B-0090 | ADR-B-13 | DWA-SKRAJNE, DŁUGOŚĆ, BRAK-PUNKTU-W-WYJAŚNIENIU | 2.75 | zastąpić skrajne dystraktory realistycznymi błędnymi interpretacjami przepisu; wyrównać długości i szczegółowość wariantów bez zmiany klucza; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 5.4.3.1; 8.1.2.3 | DO-RECENZJI |
| ADR-B-0091 | ADR-B-01 | DŁUGOŚĆ, KLUCZ-DŁUŻSZY, BRAK-PUNKTU-W-WYJAŚNIENIU, SPRAWDŹ-WARUNEK | 4.67 | wyrównać długości i szczegółowość wariantów bez zmiany klucza; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 1.1.3.1 (a); sprawdzić konieczność doprecyzowania sytuacji i wyjątku | DO-RECENZJI |
| ADR-B-0092 | ADR-B-01 | BRAK-PUNKTU-W-WYJAŚNIENIU | 1.61 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 1.3.1 | DO-RECENZJI |
| ADR-B-0093 | ADR-B-01 | DŁUGOŚĆ, KLUCZ-DŁUŻSZY, SPRAWDŹ-WARUNEK | 4.17 | wyrównać długości i szczegółowość wariantów bez zmiany klucza; sprawdzić konieczność doprecyzowania sytuacji i wyjątku | DO-RECENZJI |
| ADR-B-0094 | ADR-B-02 | BRAK-PUNKTU-W-WYJAŚNIENIU, OGÓLNE | 1.00 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 2.2.41.1.1; sprawdzić konieczność doprecyzowania sytuacji i wyjątku | DO-RECENZJI |
| ADR-B-0095 | ADR-B-02 | BRAK-PUNKTU-W-WYJAŚNIENIU, OGÓLNE | 1.00 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 2.2.42.1.1; sprawdzić konieczność doprecyzowania sytuacji i wyjątku | DO-RECENZJI |
| ADR-B-0096 | ADR-B-02 | BRAK-PUNKTU-W-WYJAŚNIENIU, OGÓLNE | 1.00 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 2.2.52.1.1; sprawdzić konieczność doprecyzowania sytuacji i wyjątku | DO-RECENZJI |
| ADR-B-0097 | ADR-B-02 | DŁUGOŚĆ, BRAK-PUNKTU-W-WYJAŚNIENIU, OGÓLNE | 3.00 | wyrównać długości i szczegółowość wariantów bez zmiany klucza; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 2.2.61.1.1; sprawdzić konieczność doprecyzowania sytuacji i wyjątku | DO-RECENZJI |
| ADR-B-0098 | ADR-B-02 | BRAK-PUNKTU-W-WYJAŚNIENIU, OGÓLNE | 1.29 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 2.2.7.1; sprawdzić konieczność doprecyzowania sytuacji i wyjątku | DO-RECENZJI |
| ADR-B-0099 | ADR-B-02 | brak flag | 1.49 | nie wykryto sygnału w przesiewie; pozostawić do oceny eksperckiej | DO-RECENZJI |
| ADR-B-0100 | ADR-B-03 | DWA-SKRAJNE, DŁUGOŚĆ, BRAK-PUNKTU-W-WYJAŚNIENIU | 2.55 | zastąpić skrajne dystraktory realistycznymi błędnymi interpretacjami przepisu; wyrównać długości i szczegółowość wariantów bez zmiany klucza; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 5.4.3.4 | DO-RECENZJI |
| ADR-B-0101 | ADR-B-03 | BRAK-PUNKTU-W-WYJAŚNIENIU | 1.88 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 5.4.3.4 | DO-RECENZJI |
| ADR-B-0102 | ADR-B-04 | KLUCZ-DŁUŻSZY, BRAK-PUNKTU-W-WYJAŚNIENIU | 2.00 | wyrównać długości i szczegółowość wariantów bez zmiany klucza; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 5.4.3.4 | DO-RECENZJI |
| ADR-B-0103 | ADR-B-04 | KLUCZ-DŁUŻSZY | 2.09 | wyrównać długości i szczegółowość wariantów bez zmiany klucza | DO-RECENZJI |
| ADR-B-0104 | ADR-B-05 | KLUCZ-DŁUŻSZY, BRAK-PUNKTU-W-WYJAŚNIENIU | 1.80 | wyrównać długości i szczegółowość wariantów bez zmiany klucza; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 5.4.3.4 | DO-RECENZJI |
| ADR-B-0105 | ADR-B-05 | DWA-SKRAJNE, KLUCZ-DŁUŻSZY, BRAK-PUNKTU-W-WYJAŚNIENIU | 1.91 | zastąpić skrajne dystraktory realistycznymi błędnymi interpretacjami przepisu; wyrównać długości i szczegółowość wariantów bez zmiany klucza; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 5.4.3.4 | DO-RECENZJI |
| ADR-B-0106 | ADR-B-05 | BRAK-PUNKTU-W-WYJAŚNIENIU | 1.07 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 5.4.3.4 | DO-RECENZJI |
| ADR-B-0107 | ADR-B-05 | KLUCZ-DŁUŻSZY, BRAK-PUNKTU-W-WYJAŚNIENIU | 1.96 | wyrównać długości i szczegółowość wariantów bez zmiany klucza; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 5.4.3.4 | DO-RECENZJI |
| ADR-B-0108 | ADR-B-05 | KLUCZ-DŁUŻSZY, BRAK-PUNKTU-W-WYJAŚNIENIU | 2.10 | wyrównać długości i szczegółowość wariantów bez zmiany klucza; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 5.4.3.4 | DO-RECENZJI |
| ADR-B-0109 | ADR-B-05 | BRAK-PUNKTU-W-WYJAŚNIENIU | 1.60 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 5.4.3.4 | DO-RECENZJI |
| ADR-B-0110 | ADR-B-05 | BRAK-PUNKTU-W-WYJAŚNIENIU | 1.70 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 5.4.3.4 | DO-RECENZJI |
| ADR-B-0111 | ADR-B-05 | DŁUGOŚĆ, BRAK-PUNKTU-W-WYJAŚNIENIU | 2.27 | wyrównać długości i szczegółowość wariantów bez zmiany klucza; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 5.4.3.4 | DO-RECENZJI |
| ADR-B-0112 | ADR-B-05 | BRAK-PUNKTU-W-WYJAŚNIENIU | 1.39 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 5.4.3.4 | DO-RECENZJI |
| ADR-B-0113 | ADR-B-05 | DŁUGOŚĆ, KLUCZ-DŁUŻSZY, BRAK-PUNKTU-W-WYJAŚNIENIU, SPRAWDŹ-WARUNEK | 2.94 | wyrównać długości i szczegółowość wariantów bez zmiany klucza; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 5.4.3.4; program praktyczny zał. 1 (Dz.U. 2021 poz. 2150); sprawdzić konieczność doprecyzowania sytuacji i wyjątku | DO-RECENZJI |
| ADR-B-0114 | ADR-B-06 | DWA-SKRAJNE, BRAK-PUNKTU-W-WYJAŚNIENIU | 1.62 | zastąpić skrajne dystraktory realistycznymi błędnymi interpretacjami przepisu; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 5.2.1.1 | DO-RECENZJI |
| ADR-B-0115 | ADR-B-06 | BRAK-PUNKTU-W-WYJAŚNIENIU | 1.14 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 5.2.2.1.1 | DO-RECENZJI |
| ADR-B-0116 | ADR-B-07 | KLUCZ-DŁUŻSZY, BRAK-PUNKTU-W-WYJAŚNIENIU | 1.98 | wyrównać długości i szczegółowość wariantów bez zmiany klucza; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 1.4.2.2.1(c); 1.4.2.2.3–1.4.2.2.4 | DO-RECENZJI |
| ADR-B-0117 | ADR-B-07 | DŁUGOŚĆ, BRAK-PUNKTU-W-WYJAŚNIENIU | 5.57 | wyrównać długości i szczegółowość wariantów bez zmiany klucza; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 1.4.2.1.1 | DO-RECENZJI |
| ADR-B-0118 | ADR-B-07 | DŁUGOŚĆ, KLUCZ-DŁUŻSZY, BRAK-PUNKTU-W-WYJAŚNIENIU | 3.08 | wyrównać długości i szczegółowość wariantów bez zmiany klucza; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 1.4.2.3.1 | DO-RECENZJI |
| ADR-B-0119 | ADR-B-10 | DWA-SKRAJNE, DŁUGOŚĆ | 2.64 | zastąpić skrajne dystraktory realistycznymi błędnymi interpretacjami przepisu; wyrównać długości i szczegółowość wariantów bez zmiany klucza | DO-RECENZJI |
| ADR-B-0120 | ADR-B-12 | BRAK-PUNKTU-W-WYJAŚNIENIU | 1.85 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 1.10.1.2 | DO-RECENZJI |
| ADR-B-0121 | ADR-B-12 | BRAK-PUNKTU-W-WYJAŚNIENIU | 1.21 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 1.10.2.2 | DO-RECENZJI |
| ADR-B-0122 | ADR-B-12 | BRAK-PUNKTU-W-WYJAŚNIENIU | 1.57 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 1.10.3.2.1 | DO-RECENZJI |
| ADR-B-0123 | ADR-B-01 | DŁUGOŚĆ, KLUCZ-DŁUŻSZY, BRAK-PUNKTU-W-WYJAŚNIENIU, OGÓLNE | 4.92 | wyrównać długości i szczegółowość wariantów bez zmiany klucza; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, Umowa ADR, art. 1(b); sprawdzić konieczność doprecyzowania sytuacji i wyjątku | DO-RECENZJI |
| ADR-B-0124 | ADR-B-01 | DŁUGOŚĆ, KLUCZ-DŁUŻSZY, BRAK-PUNKTU-W-WYJAŚNIENIU | 3.07 | wyrównać długości i szczegółowość wariantów bez zmiany klucza; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 2.1.1; 3.2 tabela A | DO-RECENZJI |
| ADR-B-0125 | ADR-B-01 | DŁUGOŚĆ, BRAK-PUNKTU-W-WYJAŚNIENIU, OGÓLNE | 3.33 | wyrównać długości i szczegółowość wariantów bez zmiany klucza; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 3.2.1, tabela A kol. (1); sprawdzić konieczność doprecyzowania sytuacji i wyjątku | DO-RECENZJI |
| ADR-B-0126 | ADR-B-02 | BRAK-PUNKTU-W-WYJAŚNIENIU, OGÓLNE | 1.72 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 2.2.1.1.5; sprawdzić konieczność doprecyzowania sytuacji i wyjątku | DO-RECENZJI |
| ADR-B-0127 | ADR-B-02 | DŁUGOŚĆ, BRAK-PUNKTU-W-WYJAŚNIENIU | 5.86 | wyrównać długości i szczegółowość wariantów bez zmiany klucza; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 2.1.1.3 | DO-RECENZJI |
| ADR-B-0128 | ADR-B-02 | DŁUGOŚĆ, BRAK-PUNKTU-W-WYJAŚNIENIU | 2.31 | wyrównać długości i szczegółowość wariantów bez zmiany klucza; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 3.2.1 tabela A kol. (3a) | DO-RECENZJI |
| ADR-B-0129 | ADR-B-03 | DŁUGOŚĆ, KLUCZ-DŁUŻSZY, SPRAWDŹ-WARUNEK | 3.00 | wyrównać długości i szczegółowość wariantów bez zmiany klucza; sprawdzić konieczność doprecyzowania sytuacji i wyjątku | DO-RECENZJI |
| ADR-B-0130 | ADR-B-04 | KLUCZ-DŁUŻSZY, BRAK-PUNKTU-W-WYJAŚNIENIU | 1.74 | wyrównać długości i szczegółowość wariantów bez zmiany klucza; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 5.4.3.4 | DO-RECENZJI |
| ADR-B-0131 | ADR-B-04 | DWA-SKRAJNE, DŁUGOŚĆ, KLUCZ-DŁUŻSZY, BRAK-PUNKTU-W-WYJAŚNIENIU | 2.42 | zastąpić skrajne dystraktory realistycznymi błędnymi interpretacjami przepisu; wyrównać długości i szczegółowość wariantów bez zmiany klucza; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 8.4.1; 8.5; 3.2 tabela A kol. (19) | DO-RECENZJI |
| ADR-B-0132 | ADR-B-06 | DWA-SKRAJNE, SPRAWDŹ-WARUNEK | 2.06 | zastąpić skrajne dystraktory realistycznymi błędnymi interpretacjami przepisu; sprawdzić konieczność doprecyzowania sytuacji i wyjątku | DO-RECENZJI |
| ADR-B-0133 | ADR-B-06 | BRAK-PUNKTU-W-WYJAŚNIENIU | 1.85 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 5.3.1.3 | DO-RECENZJI |
| ADR-B-0134 | ADR-B-07 | DWA-SKRAJNE, DŁUGOŚĆ, BRAK-PUNKTU-W-WYJAŚNIENIU | 4.25 | zastąpić skrajne dystraktory realistycznymi błędnymi interpretacjami przepisu; wyrównać długości i szczegółowość wariantów bez zmiany klucza; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 1.4.3.2 | DO-RECENZJI |
| ADR-B-0135 | ADR-B-07 | DŁUGOŚĆ, KLUCZ-DŁUŻSZY, BRAK-PUNKTU-W-WYJAŚNIENIU | 2.36 | wyrównać długości i szczegółowość wariantów bez zmiany klucza; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 1.4.3.7.1(b) | DO-RECENZJI |
| ADR-B-0136 | ADR-B-07 | BRAK-PUNKTU-W-WYJAŚNIENIU | 1.12 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 8.3.1 | DO-RECENZJI |
| ADR-B-0137 | ADR-B-08 | BRAK-PUNKTU-W-WYJAŚNIENIU | 1.14 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 9.1.2.1; 9.1.3 | DO-RECENZJI |
| ADR-B-0138 | ADR-B-09 | BRAK-PUNKTU-W-WYJAŚNIENIU | 1.57 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 7.5.1.2 | DO-RECENZJI |
| ADR-B-0139 | ADR-B-09 | KLUCZ-DŁUŻSZY | 2.07 | wyrównać długości i szczegółowość wariantów bez zmiany klucza | DO-RECENZJI |
| ADR-B-0140 | ADR-B-10 | brak flag | 1.11 | nie wykryto sygnału w przesiewie; pozostawić do oceny eksperckiej | DO-RECENZJI |
| ADR-B-0141 | ADR-B-10 | BRAK-PUNKTU-W-WYJAŚNIENIU | 1.34 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 1.1.4.2; 1.1.4.3 | DO-RECENZJI |
| ADR-B-0142 | ADR-B-10 | BRAK-PUNKTU-W-WYJAŚNIENIU | 1.93 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 1.1.4.2.1 | DO-RECENZJI |
| ADR-B-0143 | ADR-B-11 | DŁUGOŚĆ, KLUCZ-DŁUŻSZY, BRAK-PUNKTU-W-WYJAŚNIENIU | 2.44 | wyrównać długości i szczegółowość wariantów bez zmiany klucza; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 5.4.3.4; program kursu lit. k | DO-RECENZJI |
| ADR-B-0144 | ADR-B-12 | brak flag | 2.21 | nie wykryto sygnału w przesiewie; pozostawić do oceny eksperckiej | DO-RECENZJI |
| ADR-B-0145 | ADR-B-13 | DŁUGOŚĆ, KLUCZ-DŁUŻSZY | 3.25 | wyrównać długości i szczegółowość wariantów bez zmiany klucza | DO-RECENZJI |
| ADR-B-0146 | ADR-B-13 | BRAK-PUNKTU-W-WYJAŚNIENIU | 1.56 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 8.1.2.2(b); 8.2.1 | DO-RECENZJI |
| ADR-B-0147 | ADR-B-01 | DWA-SKRAJNE, BRAK-PUNKTU-W-WYJAŚNIENIU | 1.25 | zastąpić skrajne dystraktory realistycznymi błędnymi interpretacjami przepisu; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 1.2.1, definicja transport unit | DO-RECENZJI |
| ADR-B-0148 | ADR-B-01 | BRAK-PUNKTU-W-WYJAŚNIENIU | 1.75 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 8.2.1; prawo krajowe o uprawnieniach do kierowania | DO-RECENZJI |
| ADR-B-0149 | ADR-B-01 | BRAK-PUNKTU-W-WYJAŚNIENIU | 1.34 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 3.2 tabela A kol. (7a); 3.4.1 | DO-RECENZJI |
| ADR-B-0150 | ADR-B-02 | DŁUGOŚĆ, KLUCZ-DŁUŻSZY, BRAK-PUNKTU-W-WYJAŚNIENIU | 2.51 | wyrównać długości i szczegółowość wariantów bez zmiany klucza; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 2.2.1.1.5 | DO-RECENZJI |
| ADR-B-0151 | ADR-B-02 | DWA-SKRAJNE, BRAK-PUNKTU-W-WYJAŚNIENIU | 2.17 | zastąpić skrajne dystraktory realistycznymi błędnymi interpretacjami przepisu; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 5.2.2.2.2, wzór nr 2.3; 2.2.2 | DO-RECENZJI |
| ADR-B-0152 | ADR-B-02 | BRAK-PUNKTU-W-WYJAŚNIENIU | 1.22 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 2.2.3; 8.3.5 | DO-RECENZJI |
| ADR-B-0153 | ADR-B-02 | DWA-SKRAJNE, KLUCZ-DŁUŻSZY, BRAK-PUNKTU-W-WYJAŚNIENIU, OGÓLNE | 2.25 | zastąpić skrajne dystraktory realistycznymi błędnymi interpretacjami przepisu; wyrównać długości i szczegółowość wariantów bez zmiany klucza; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 2.2.41.1.1; 2.2.43.1.1; sprawdzić konieczność doprecyzowania sytuacji i wyjątku | DO-RECENZJI |
| ADR-B-0154 | ADR-B-02 | KLUCZ-DŁUŻSZY, BRAK-PUNKTU-W-WYJAŚNIENIU | 1.83 | wyrównać długości i szczegółowość wariantów bez zmiany klucza; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 2.2.42.1.1 | DO-RECENZJI |
| ADR-B-0155 | ADR-B-02 | BRAK-PUNKTU-W-WYJAŚNIENIU | 1.51 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 2.2.43.1.1; 5.4.3.4 | DO-RECENZJI |
| ADR-B-0156 | ADR-B-02 | BRAK-PUNKTU-W-WYJAŚNIENIU | 1.15 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 2.2.51.1.1 | DO-RECENZJI |
| ADR-B-0157 | ADR-B-02 | BRAK-PUNKTU-W-WYJAŚNIENIU, OGÓLNE | 1.41 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 2.2.51; 2.2.52; sprawdzić konieczność doprecyzowania sytuacji i wyjątku | DO-RECENZJI |
| ADR-B-0158 | ADR-B-02 | DWA-SKRAJNE, BRAK-PUNKTU-W-WYJAŚNIENIU, OGÓLNE | 1.24 | zastąpić skrajne dystraktory realistycznymi błędnymi interpretacjami przepisu; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 5.2.2.2.2 wzór nr 6.1; 2.2.61.1.1; sprawdzić konieczność doprecyzowania sytuacji i wyjątku | DO-RECENZJI |
| ADR-B-0159 | ADR-B-02 | BRAK-PUNKTU-W-WYJAŚNIENIU, OGÓLNE | 1.50 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 2.2.62.1.1; 2.2.61.1.1; sprawdzić konieczność doprecyzowania sytuacji i wyjątku | DO-RECENZJI |
| ADR-B-0160 | ADR-B-02 | SPRAWDŹ-WARUNEK | 1.67 | sprawdzić konieczność doprecyzowania sytuacji i wyjątku | DO-RECENZJI |
| ADR-B-0161 | ADR-B-02 | DWA-SKRAJNE, BRAK-PUNKTU-W-WYJAŚNIENIU | 1.62 | zastąpić skrajne dystraktory realistycznymi błędnymi interpretacjami przepisu; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 2.2.8.1.1; 5.2.2.2.2 wzór nr 8 | DO-RECENZJI |
| ADR-B-0162 | ADR-B-02 | DWA-SKRAJNE | 1.32 | zastąpić skrajne dystraktory realistycznymi błędnymi interpretacjami przepisu | DO-RECENZJI |
| ADR-B-0163 | ADR-B-03 | BRAK-PUNKTU-W-WYJAŚNIENIU | 1.49 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 5.4.3.4 | DO-RECENZJI |
| ADR-B-0164 | ADR-B-04 | BRAK-PUNKTU-W-WYJAŚNIENIU | 1.39 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 5.4.3.4 | DO-RECENZJI |
| ADR-B-0165 | ADR-B-05 | DWA-SKRAJNE, BRAK-PUNKTU-W-WYJAŚNIENIU | 1.50 | zastąpić skrajne dystraktory realistycznymi błędnymi interpretacjami przepisu; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 5.4.3.4 | DO-RECENZJI |
| ADR-B-0166 | ADR-B-05 | BRAK-PUNKTU-W-WYJAŚNIENIU | 1.75 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 5.4.3.4 | DO-RECENZJI |
| ADR-B-0167 | ADR-B-05 | BRAK-PUNKTU-W-WYJAŚNIENIU | 1.09 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 5.4.3.4 | DO-RECENZJI |
| ADR-B-0168 | ADR-B-05 | BRAK-PUNKTU-W-WYJAŚNIENIU | 1.52 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 5.4.3.4; 8.1.5.2 | DO-RECENZJI |
| ADR-B-0169 | ADR-B-05 | BRAK-PUNKTU-W-WYJAŚNIENIU | 1.27 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 8.1.4.5 | DO-RECENZJI |
| ADR-B-0170 | ADR-B-06 | BRAK-PUNKTU-W-WYJAŚNIENIU | 1.44 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 5.3.2.3.1 | DO-RECENZJI |
| ADR-B-0171 | ADR-B-08 | BRAK-PUNKTU-W-WYJAŚNIENIU | 2.03 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 8.1.5.3 | DO-RECENZJI |
| ADR-B-0172 | ADR-B-09 | BRAK-PUNKTU-W-WYJAŚNIENIU | 1.60 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 7.5.1.5 | DO-RECENZJI |
| ADR-B-0173 | ADR-B-09 | brak flag | 1.75 | nie wykryto sygnału w przesiewie; pozostawić do oceny eksperckiej | DO-RECENZJI |
| ADR-B-0174 | ADR-B-11 | KLUCZ-DŁUŻSZY, BRAK-PUNKTU-W-WYJAŚNIENIU | 1.75 | wyrównać długości i szczegółowość wariantów bez zmiany klucza; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 8.6.3.1 | DO-RECENZJI |
| ADR-B-0175 | ADR-B-13 | BRAK-PUNKTU-W-WYJAŚNIENIU, SPRAWDŹ-WARUNEK | 1.36 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 1.10.1.4; 8.1.2.1 (d); sprawdzić konieczność doprecyzowania sytuacji i wyjątku | DO-RECENZJI |
| ADR-B-0176 | ADR-B-08 | brak flag | 1.67 | nie wykryto sygnału w przesiewie; pozostawić do oceny eksperckiej | DO-RECENZJI |
| ADR-B-0177 | ADR-B-03 | BRAK-PUNKTU-W-WYJAŚNIENIU | 1.96 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 7.5.8.1 | DO-RECENZJI |
| ADR-B-0178 | ADR-B-03 | BRAK-PUNKTU-W-WYJAŚNIENIU | 1.30 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 5.4.3.4 | DO-RECENZJI |
| ADR-B-0179 | ADR-B-03 | KLUCZ-DŁUŻSZY | 2.17 | wyrównać długości i szczegółowość wariantów bez zmiany klucza | DO-RECENZJI |
| ADR-B-0180 | ADR-B-04 | BRAK-PUNKTU-W-WYJAŚNIENIU | 1.68 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 5.4.3.4 | DO-RECENZJI |
| ADR-B-0181 | ADR-B-04 | BRAK-PUNKTU-W-WYJAŚNIENIU | 1.91 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 8.4.1 | DO-RECENZJI |
| ADR-B-0182 | ADR-B-05 | BRAK-PUNKTU-W-WYJAŚNIENIU | 1.52 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 5.4.3.4 | DO-RECENZJI |
| ADR-B-0183 | ADR-B-05 | BRAK-PUNKTU-W-WYJAŚNIENIU | 1.49 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 5.4.3.4 | DO-RECENZJI |
| ADR-B-0184 | ADR-B-05 | KLUCZ-DŁUŻSZY, BRAK-PUNKTU-W-WYJAŚNIENIU | 1.72 | wyrównać długości i szczegółowość wariantów bez zmiany klucza; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 5.4.3.4 | DO-RECENZJI |
| ADR-B-0185 | ADR-B-05 | BRAK-PUNKTU-W-WYJAŚNIENIU | 1.32 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 5.4.3.4 | DO-RECENZJI |
| ADR-B-0186 | ADR-B-05 | BRAK-PUNKTU-W-WYJAŚNIENIU | 1.68 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 5.4.3.4 | DO-RECENZJI |
| ADR-B-0187 | ADR-B-05 | KLUCZ-DŁUŻSZY, BRAK-PUNKTU-W-WYJAŚNIENIU | 2.18 | wyrównać długości i szczegółowość wariantów bez zmiany klucza; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 5.4.3.4; program szkolenia praktycznego | DO-RECENZJI |
| ADR-B-0188 | ADR-B-06 | BRAK-PUNKTU-W-WYJAŚNIENIU | 1.28 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 5.2.1.1 | DO-RECENZJI |
| ADR-B-0189 | ADR-B-06 | BRAK-PUNKTU-W-WYJAŚNIENIU | 1.22 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 3.2 tabela A kol. (5); 5.2.2.1 | DO-RECENZJI |
| ADR-B-0190 | ADR-B-06 | BRAK-PUNKTU-W-WYJAŚNIENIU | 1.34 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 5.3.2.2.2 | DO-RECENZJI |
| ADR-B-0191 | ADR-B-06 | BRAK-PUNKTU-W-WYJAŚNIENIU | 1.91 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 5.3.2.2.1 | DO-RECENZJI |
| ADR-B-0192 | ADR-B-06 | BRAK-PUNKTU-W-WYJAŚNIENIU | 1.74 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 5.3.2.3.1 | DO-RECENZJI |
| ADR-B-0193 | ADR-B-06 | BRAK-PUNKTU-W-WYJAŚNIENIU | 1.17 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 5.3.2.2.2 | DO-RECENZJI |
| ADR-B-0194 | ADR-B-06 | BRAK-PUNKTU-W-WYJAŚNIENIU | 1.88 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 5.3.2.3.1 | DO-RECENZJI |
| ADR-B-0195 | ADR-B-07 | BRAK-PUNKTU-W-WYJAŚNIENIU | 1.27 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 1.4.2.3.2 | DO-RECENZJI |
| ADR-B-0196 | ADR-B-07 | brak flag | 1.71 | nie wykryto sygnału w przesiewie; pozostawić do oceny eksperckiej | DO-RECENZJI |
| ADR-B-0197 | ADR-B-08 | BRAK-PUNKTU-W-WYJAŚNIENIU | 1.53 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 8.1.4.2 | DO-RECENZJI |
| ADR-B-0198 | ADR-B-08 | brak flag | 1.92 | nie wykryto sygnału w przesiewie; pozostawić do oceny eksperckiej | DO-RECENZJI |
| ADR-B-0199 | ADR-B-09 | BRAK-PUNKTU-W-WYJAŚNIENIU | 1.54 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 7.5.2.1; 7.5.2.2 | DO-RECENZJI |
| ADR-B-0200 | ADR-B-09 | BRAK-PUNKTU-W-WYJAŚNIENIU | 1.31 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 7.5.7.1 | DO-RECENZJI |
| ADR-B-0201 | ADR-B-09 | DWA-SKRAJNE, SPRAWDŹ-WARUNEK | 1.69 | zastąpić skrajne dystraktory realistycznymi błędnymi interpretacjami przepisu; sprawdzić konieczność doprecyzowania sytuacji i wyjątku | DO-RECENZJI |
| ADR-B-0202 | ADR-B-09 | BRAK-PUNKTU-W-WYJAŚNIENIU | 1.56 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 7.5.1.2 | DO-RECENZJI |
| ADR-B-0203 | ADR-B-10 | brak flag | 1.61 | nie wykryto sygnału w przesiewie; pozostawić do oceny eksperckiej | DO-RECENZJI |
| ADR-B-0204 | ADR-B-10 | DWA-SKRAJNE, BRAK-PUNKTU-W-WYJAŚNIENIU | 1.54 | zastąpić skrajne dystraktory realistycznymi błędnymi interpretacjami przepisu; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 5.4.2 | DO-RECENZJI |
| ADR-B-0205 | ADR-B-10 | DWA-SKRAJNE, BRAK-PUNKTU-W-WYJAŚNIENIU | 2.09 | zastąpić skrajne dystraktory realistycznymi błędnymi interpretacjami przepisu; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 1.1.4.2; 1.1.4.3 | DO-RECENZJI |
| ADR-B-0206 | ADR-B-10 | BRAK-PUNKTU-W-WYJAŚNIENIU | 1.60 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 1.1.4.2.1 | DO-RECENZJI |
| ADR-B-0207 | ADR-B-11 | DWA-SKRAJNE, BRAK-PUNKTU-W-WYJAŚNIENIU | 1.12 | zastąpić skrajne dystraktory realistycznymi błędnymi interpretacjami przepisu; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 1.9.5.2.2; 8.6.4 | DO-RECENZJI |
| ADR-B-0208 | ADR-B-11 | DŁUGOŚĆ, KLUCZ-DŁUŻSZY, BRAK-PUNKTU-W-WYJAŚNIENIU | 3.54 | wyrównać długości i szczegółowość wariantów bez zmiany klucza; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 8.6.3.1; 8.6.4 | DO-RECENZJI |
| ADR-B-0209 | ADR-B-11 | DWA-SKRAJNE, DŁUGOŚĆ | 11.00 | zastąpić skrajne dystraktory realistycznymi błędnymi interpretacjami przepisu; wyrównać długości i szczegółowość wariantów bez zmiany klucza | DO-RECENZJI |
| ADR-B-0210 | ADR-B-11 | KLUCZ-DŁUŻSZY, BRAK-PUNKTU-W-WYJAŚNIENIU | 1.77 | wyrównać długości i szczegółowość wariantów bez zmiany klucza; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 5.4.3.4; 1.9.5 | DO-RECENZJI |
| ADR-B-0211 | ADR-B-12 | BRAK-PUNKTU-W-WYJAŚNIENIU | 1.64 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 1.10.1.2 | DO-RECENZJI |
| ADR-B-0212 | ADR-B-12 | DŁUGOŚĆ, KLUCZ-DŁUŻSZY, BRAK-PUNKTU-W-WYJAŚNIENIU | 2.40 | wyrównać długości i szczegółowość wariantów bez zmiany klucza; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 1.10.3.2.2 | DO-RECENZJI |
| ADR-B-0213 | ADR-B-12 | DWA-SKRAJNE, KLUCZ-DŁUŻSZY, BRAK-PUNKTU-W-WYJAŚNIENIU | 1.82 | zastąpić skrajne dystraktory realistycznymi błędnymi interpretacjami przepisu; wyrównać długości i szczegółowość wariantów bez zmiany klucza; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 1.10.3.3 | DO-RECENZJI |
| ADR-B-0214 | ADR-B-13 | BRAK-PUNKTU-W-WYJAŚNIENIU | 1.29 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 5.4.1.1.1(g),(h) | DO-RECENZJI |
| ADR-B-0215 | ADR-B-13 | brak flag | 1.41 | nie wykryto sygnału w przesiewie; pozostawić do oceny eksperckiej | DO-RECENZJI |
| ADR-B-0216 | ADR-B-13 | BRAK-PUNKTU-W-WYJAŚNIENIU | 1.19 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 8.1.2.1(b); 8.1.2.3 | DO-RECENZJI |
| ADR-B-0217 | ADR-B-06 | DŁUGOŚĆ, BRAK-PUNKTU-W-WYJAŚNIENIU | 2.40 | wyrównać długości i szczegółowość wariantów bez zmiany klucza; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 5.3.2.3.1 | DO-RECENZJI |
| ADR-B-0218 | ADR-B-02 | BRAK-PUNKTU-W-WYJAŚNIENIU | 1.47 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 5.2.2.1.1; 3.2.1 tabela A kolumna (5) | DO-RECENZJI |
| ADR-B-0219 | ADR-B-05 | BRAK-PUNKTU-W-WYJAŚNIENIU | 1.31 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 5.4.3.4 | DO-RECENZJI |
| ADR-B-0220 | ADR-B-05 | DŁUGOŚĆ, KLUCZ-DŁUŻSZY, BRAK-PUNKTU-W-WYJAŚNIENIU | 2.87 | wyrównać długości i szczegółowość wariantów bez zmiany klucza; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 5.4.3.4 | DO-RECENZJI |
| ADR-B-0221 | ADR-B-05 | BRAK-PUNKTU-W-WYJAŚNIENIU | 1.37 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 5.4.3.4 | DO-RECENZJI |
| ADR-B-0222 | ADR-B-05 | BRAK-PUNKTU-W-WYJAŚNIENIU | 1.52 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 5.4.3.4 | DO-RECENZJI |
| ADR-B-0223 | ADR-B-05 | DŁUGOŚĆ, KLUCZ-DŁUŻSZY, BRAK-PUNKTU-W-WYJAŚNIENIU | 3.06 | wyrównać długości i szczegółowość wariantów bez zmiany klucza; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 5.4.3.4 | DO-RECENZJI |
| ADR-B-0224 | ADR-B-05 | BRAK-PUNKTU-W-WYJAŚNIENIU | 1.64 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 5.4.3.4 | DO-RECENZJI |
| ADR-B-0225 | ADR-B-05 | BRAK-PUNKTU-W-WYJAŚNIENIU | 1.44 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 5.4.3.4 | DO-RECENZJI |
| ADR-B-0226 | ADR-B-13 | DŁUGOŚĆ, KLUCZ-DŁUŻSZY, BRAK-PUNKTU-W-WYJAŚNIENIU | 2.47 | wyrównać długości i szczegółowość wariantów bez zmiany klucza; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 5.4.1.1.1(a) | DO-RECENZJI |
| ADR-B-0227 | ADR-B-13 | BRAK-PUNKTU-W-WYJAŚNIENIU | 1.50 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 5.4.1.1.1(e) | DO-RECENZJI |
| ADR-B-0228 | ADR-B-13 | BRAK-PUNKTU-W-WYJAŚNIENIU | 1.74 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 5.4.3.1; 8.1.2.3 | DO-RECENZJI |
| ADR-B-0229 | ADR-B-05 | DŁUGOŚĆ, BRAK-PUNKTU-W-WYJAŚNIENIU | 2.45 | wyrównać długości i szczegółowość wariantów bez zmiany klucza; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 5.4.3.4 | DO-RECENZJI |
| ADR-B-0230 | ADR-B-05 | BRAK-PUNKTU-W-WYJAŚNIENIU | 1.74 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 5.4.3.4 | DO-RECENZJI |
| ADR-B-0231 | ADR-B-05 | DŁUGOŚĆ, KLUCZ-DŁUŻSZY, BRAK-PUNKTU-W-WYJAŚNIENIU | 2.57 | wyrównać długości i szczegółowość wariantów bez zmiany klucza; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 5.4.3.4; 8.1.5.2 | DO-RECENZJI |
| ADR-B-0232 | ADR-B-05 | BRAK-PUNKTU-W-WYJAŚNIENIU | 1.63 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 8.1.4.5 | DO-RECENZJI |
| ADR-B-0233 | ADR-B-13 | BRAK-PUNKTU-W-WYJAŚNIENIU | 1.76 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 5.4.1.1.1(h) | DO-RECENZJI |
| ADR-B-0234 | ADR-B-13 | BRAK-PUNKTU-W-WYJAŚNIENIU | 1.60 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 5.4.3.2; 5.4.3.4 | DO-RECENZJI |
| ADR-B-0235 | ADR-B-09 | DŁUGOŚĆ, KLUCZ-DŁUŻSZY, BRAK-PUNKTU-W-WYJAŚNIENIU | 3.00 | wyrównać długości i szczegółowość wariantów bez zmiany klucza; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 7.5.7.1 | DO-RECENZJI |
| ADR-B-0236 | ADR-B-09 | BRAK-PUNKTU-W-WYJAŚNIENIU | 2.11 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 7.5.7.1 | DO-RECENZJI |
| ADR-B-0237 | ADR-B-09 | DŁUGOŚĆ, KLUCZ-DŁUŻSZY, BRAK-PUNKTU-W-WYJAŚNIENIU | 2.82 | wyrównać długości i szczegółowość wariantów bez zmiany klucza; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 7.5.7.2 | DO-RECENZJI |
| ADR-B-0238 | ADR-B-09 | KLUCZ-DŁUŻSZY, BRAK-PUNKTU-W-WYJAŚNIENIU | 1.89 | wyrównać długości i szczegółowość wariantów bez zmiany klucza; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 7.5.8.1 | DO-RECENZJI |
| ADR-B-0239 | ADR-B-09 | BRAK-PUNKTU-W-WYJAŚNIENIU | 2.05 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 7.5.1.2 | DO-RECENZJI |
| ADR-B-0240 | ADR-B-09 | DŁUGOŚĆ, KLUCZ-DŁUŻSZY, BRAK-PUNKTU-W-WYJAŚNIENIU | 4.45 | wyrównać długości i szczegółowość wariantów bez zmiany klucza; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 7.5.8.2 | DO-RECENZJI |
| ADR-B-0241 | ADR-B-03 | brak flag | 1.30 | nie wykryto sygnału w przesiewie; pozostawić do oceny eksperckiej | DO-RECENZJI |
| ADR-B-0242 | ADR-B-03 | BRAK-PUNKTU-W-WYJAŚNIENIU | 1.20 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 5.4.3.4 | DO-RECENZJI |
| ADR-B-0243 | ADR-B-04 | DŁUGOŚĆ, BRAK-PUNKTU-W-WYJAŚNIENIU | 2.95 | wyrównać długości i szczegółowość wariantów bez zmiany klucza; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 8.3.3 | DO-RECENZJI |
| ADR-B-0244 | ADR-B-04 | DŁUGOŚĆ, BRAK-PUNKTU-W-WYJAŚNIENIU | 2.27 | wyrównać długości i szczegółowość wariantów bez zmiany klucza; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 8.3.6 | DO-RECENZJI |
| ADR-B-0245 | ADR-B-07 | BRAK-PUNKTU-W-WYJAŚNIENIU | 1.20 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 1.4.3.1 | DO-RECENZJI |
| ADR-B-0246 | ADR-B-07 | KLUCZ-DŁUŻSZY, BRAK-PUNKTU-W-WYJAŚNIENIU | 2.04 | wyrównać długości i szczegółowość wariantów bez zmiany klucza; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 1.4.2.3.1 | DO-RECENZJI |
| ADR-B-0247 | ADR-B-10 | DŁUGOŚĆ, KLUCZ-DŁUŻSZY, BRAK-PUNKTU-W-WYJAŚNIENIU, SPRAWDŹ-WARUNEK | 5.29 | wyrównać długości i szczegółowość wariantów bez zmiany klucza; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 1.1.4.2.1; sprawdzić konieczność doprecyzowania sytuacji i wyjątku | DO-RECENZJI |
| ADR-B-0248 | ADR-B-11 | DWA-SKRAJNE, BRAK-PUNKTU-W-WYJAŚNIENIU | 2.00 | zastąpić skrajne dystraktory realistycznymi błędnymi interpretacjami przepisu; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 3.2.1 tabela A kolumna (15); 8.6.3.1 | DO-RECENZJI |
| ADR-B-0249 | ADR-B-12 | BRAK-PUNKTU-W-WYJAŚNIENIU | 1.79 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 1.10.1.2 | DO-RECENZJI |
| ADR-B-0250 | ADR-B-13 | DWA-SKRAJNE, BRAK-PUNKTU-W-WYJAŚNIENIU | 1.45 | zastąpić skrajne dystraktory realistycznymi błędnymi interpretacjami przepisu; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 1.10.1.4; 8.1.2.1 | DO-RECENZJI |
| ADR-B-0251 | ADR-B-08 | BRAK-PUNKTU-W-WYJAŚNIENIU | 1.51 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 8.1.5.2 | DO-RECENZJI |
| ADR-B-0252 | ADR-B-08 | BRAK-PUNKTU-W-WYJAŚNIENIU, SPRAWDŹ-WARUNEK | 1.25 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 8.1.5.2; sprawdzić konieczność doprecyzowania sytuacji i wyjątku | DO-RECENZJI |
| ADR-B-0253 | ADR-B-08 | BRAK-PUNKTU-W-WYJAŚNIENIU | 1.42 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 8.1.5.2 | DO-RECENZJI |
| ADR-B-0254 | ADR-B-08 | DWA-SKRAJNE, BRAK-PUNKTU-W-WYJAŚNIENIU | 1.64 | zastąpić skrajne dystraktory realistycznymi błędnymi interpretacjami przepisu; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 8.1.5.3 | DO-RECENZJI |
| ADR-B-0255 | ADR-B-06 | BRAK-PUNKTU-W-WYJAŚNIENIU | 1.20 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 5.3.2.2.2 | DO-RECENZJI |
| ADR-B-0256 | ADR-B-06 | BRAK-PUNKTU-W-WYJAŚNIENIU | 1.03 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 5.3.2.3.1 | DO-RECENZJI |
| ADR-B-0257 | ADR-B-06 | BRAK-PUNKTU-W-WYJAŚNIENIU | 1.91 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 5.3.2.2.2 | DO-RECENZJI |
| ADR-B-0258 | ADR-B-06 | BRAK-PUNKTU-W-WYJAŚNIENIU | 1.00 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 5.3.2.2.1 | DO-RECENZJI |
| ADR-B-0259 | ADR-B-01 | BRAK-PUNKTU-W-WYJAŚNIENIU, SPRAWDŹ-WARUNEK | 1.22 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 1.1.3.6.3; sprawdzić konieczność doprecyzowania sytuacji i wyjątku | DO-RECENZJI |
| ADR-B-0260 | ADR-B-01 | BRAK-PUNKTU-W-WYJAŚNIENIU | 1.23 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 3.5.1.2 | DO-RECENZJI |
| ADR-B-0261 | ADR-B-01 | SPRAWDŹ-WARUNEK | 1.54 | sprawdzić konieczność doprecyzowania sytuacji i wyjątku | DO-RECENZJI |
| ADR-B-0262 | ADR-B-11 | KLUCZ-DŁUŻSZY, BRAK-PUNKTU-W-WYJAŚNIENIU | 1.76 | wyrównać długości i szczegółowość wariantów bez zmiany klucza; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 1.9.5.3.6; 8.6.4 | DO-RECENZJI |
| ADR-B-0263 | ADR-B-11 | BRAK-PUNKTU-W-WYJAŚNIENIU | 1.25 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 8.6.3.2 | DO-RECENZJI |
| ADR-B-0264 | ADR-B-11 | DŁUGOŚĆ, KLUCZ-DŁUŻSZY, BRAK-PUNKTU-W-WYJAŚNIENIU | 2.43 | wyrównać długości i szczegółowość wariantów bez zmiany klucza; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 8.6.3.1 | DO-RECENZJI |
| ADR-B-0265 | ADR-B-02 | KLUCZ-DŁUŻSZY, BRAK-PUNKTU-W-WYJAŚNIENIU | 1.93 | wyrównać długości i szczegółowość wariantów bez zmiany klucza; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 2.2.43.1.1 | DO-RECENZJI |
| ADR-B-0266 | ADR-B-02 | DWA-SKRAJNE, BRAK-PUNKTU-W-WYJAŚNIENIU | 1.79 | zastąpić skrajne dystraktory realistycznymi błędnymi interpretacjami przepisu; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 2.2.51.1.1 | DO-RECENZJI |
| ADR-B-0267 | ADR-B-02 | DWA-SKRAJNE, DŁUGOŚĆ, KLUCZ-DŁUŻSZY, BRAK-PUNKTU-W-WYJAŚNIENIU | 2.62 | zastąpić skrajne dystraktory realistycznymi błędnymi interpretacjami przepisu; wyrównać długości i szczegółowość wariantów bez zmiany klucza; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 2.2.8.1.1 | DO-RECENZJI |
| ADR-B-0268 | ADR-B-02 | BRAK-PUNKTU-W-WYJAŚNIENIU | 2.15 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 5.2.2.2.2 | DO-RECENZJI |
| ADR-B-0269 | ADR-B-02 | BRAK-PUNKTU-W-WYJAŚNIENIU | 2.07 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 5.2.2.2.2 | DO-RECENZJI |
| ADR-B-0270 | ADR-B-02 | BRAK-PUNKTU-W-WYJAŚNIENIU | 1.39 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 5.2.2.2.2 | DO-RECENZJI |
| ADR-B-0271 | ADR-B-01 | brak flag | 1.67 | nie wykryto sygnału w przesiewie; pozostawić do oceny eksperckiej | DO-RECENZJI |
| ADR-B-0272 | ADR-B-01 | BRAK-PUNKTU-W-WYJAŚNIENIU | 1.38 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 1.1.3.6.4 | DO-RECENZJI |
| ADR-B-0273 | ADR-B-01 | BRAK-PUNKTU-W-WYJAŚNIENIU | 2.12 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 3.4.7.1 | DO-RECENZJI |
| ADR-B-0274 | ADR-B-12 | DŁUGOŚĆ, KLUCZ-DŁUŻSZY, BRAK-PUNKTU-W-WYJAŚNIENIU | 3.21 | wyrównać długości i szczegółowość wariantów bez zmiany klucza; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 1.10.1.3 | DO-RECENZJI |
| ADR-B-0275 | ADR-B-12 | DŁUGOŚĆ, KLUCZ-DŁUŻSZY, BRAK-PUNKTU-W-WYJAŚNIENIU | 2.58 | wyrównać długości i szczegółowość wariantów bez zmiany klucza; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 1.10.2.3 | DO-RECENZJI |
| ADR-B-0276 | ADR-B-03 | DWA-SKRAJNE, BRAK-PUNKTU-W-WYJAŚNIENIU | 1.65 | zastąpić skrajne dystraktory realistycznymi błędnymi interpretacjami przepisu; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 5.2.1.8.3 | DO-RECENZJI |
| ADR-B-0277 | ADR-B-10 | DWA-SKRAJNE | 1.97 | zastąpić skrajne dystraktory realistycznymi błędnymi interpretacjami przepisu | DO-RECENZJI |
| ADR-B-0278 | ADR-B-10 | KLUCZ-DŁUŻSZY | 2.00 | wyrównać długości i szczegółowość wariantów bez zmiany klucza | DO-RECENZJI |
| ADR-B-0279 | ADR-B-04 | BRAK-PUNKTU-W-WYJAŚNIENIU | 2.16 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 8.3.5 | DO-RECENZJI |
| ADR-B-0280 | ADR-B-04 | DŁUGOŚĆ, KLUCZ-DŁUŻSZY, BRAK-PUNKTU-W-WYJAŚNIENIU | 2.35 | wyrównać długości i szczegółowość wariantów bez zmiany klucza; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 8.3.5 | DO-RECENZJI |
| ADR-B-0281 | ADR-B-06 | BRAK-PUNKTU-W-WYJAŚNIENIU | 1.22 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 5.2.1.1 | DO-RECENZJI |
| ADR-B-0282 | ADR-B-08 | DŁUGOŚĆ, KLUCZ-DŁUŻSZY | 3.91 | wyrównać długości i szczegółowość wariantów bez zmiany klucza | DO-RECENZJI |
| ADR-B-0283 | ADR-B-08 | BRAK-PUNKTU-W-WYJAŚNIENIU | 1.61 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 8.1.4.4 | DO-RECENZJI |
| ADR-B-0284 | ADR-B-02 | BRAK-PUNKTU-W-WYJAŚNIENIU | 1.76 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 5.2.2.2.2 | DO-RECENZJI |
| ADR-B-0285 | ADR-B-07 | KLUCZ-DŁUŻSZY, BRAK-PUNKTU-W-WYJAŚNIENIU | 1.82 | wyrównać długości i szczegółowość wariantów bez zmiany klucza; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 1.4.2.2.1(b) | DO-RECENZJI |
| ADR-B-0286 | ADR-B-09 | BRAK-PUNKTU-W-WYJAŚNIENIU, SPRAWDŹ-WARUNEK | 1.34 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 7.5.1.5; sprawdzić konieczność doprecyzowania sytuacji i wyjątku | DO-RECENZJI |
| ADR-B-0287 | ADR-B-13 | brak flag | 1.90 | nie wykryto sygnału w przesiewie; pozostawić do oceny eksperckiej | DO-RECENZJI |
| ADR-B-0288 | ADR-B-02 | BRAK-PUNKTU-W-WYJAŚNIENIU | 2.00 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 5.2.2.2.2 | DO-RECENZJI |
| ADR-B-0289 | ADR-B-02 | BRAK-PUNKTU-W-WYJAŚNIENIU | 1.17 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 5.2.2.2.2 | DO-RECENZJI |
| ADR-B-0290 | ADR-B-07 | DŁUGOŚĆ, KLUCZ-DŁUŻSZY, BRAK-PUNKTU-W-WYJAŚNIENIU | 3.03 | wyrównać długości i szczegółowość wariantów bez zmiany klucza; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 1.4.3.2 | DO-RECENZJI |
| ADR-B-0291 | ADR-B-09 | DŁUGOŚĆ | 2.33 | wyrównać długości i szczegółowość wariantów bez zmiany klucza | DO-RECENZJI |
| ADR-B-0292 | ADR-B-09 | DŁUGOŚĆ, KLUCZ-DŁUŻSZY, BRAK-PUNKTU-W-WYJAŚNIENIU | 2.44 | wyrównać długości i szczegółowość wariantów bez zmiany klucza; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 7.3.1.1 | DO-RECENZJI |
| ADR-B-0293 | ADR-B-07 | BRAK-PUNKTU-W-WYJAŚNIENIU | 1.55 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 8.3.1 | DO-RECENZJI |
| ADR-B-0294 | ADR-B-03 | BRAK-PUNKTU-W-WYJAŚNIENIU | 1.61 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 5.4.1.1.3.1 | DO-RECENZJI |
| ADR-B-0295 | ADR-B-03 | KLUCZ-DŁUŻSZY, BRAK-PUNKTU-W-WYJAŚNIENIU | 2.25 | wyrównać długości i szczegółowość wariantów bez zmiany klucza; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 5.4.3.4 | DO-RECENZJI |
| ADR-B-0296 | ADR-B-04 | BRAK-PUNKTU-W-WYJAŚNIENIU | 1.90 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 5.4.3.4 | DO-RECENZJI |
| ADR-B-0297 | ADR-B-04 | BRAK-PUNKTU-W-WYJAŚNIENIU | 1.75 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 5.4.3.4 | DO-RECENZJI |
| ADR-B-0298 | ADR-B-06 | DŁUGOŚĆ, KLUCZ-DŁUŻSZY, BRAK-PUNKTU-W-WYJAŚNIENIU | 3.56 | wyrównać długości i szczegółowość wariantów bez zmiany klucza; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 5.3.2.3.2 | DO-RECENZJI |
| ADR-B-0299 | ADR-B-06 | BRAK-PUNKTU-W-WYJAŚNIENIU | 1.48 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 5.3.1.2 | DO-RECENZJI |
| ADR-B-0300 | ADR-B-12 | DŁUGOŚĆ, KLUCZ-DŁUŻSZY, BRAK-PUNKTU-W-WYJAŚNIENIU | 2.57 | wyrównać długości i szczegółowość wariantów bez zmiany klucza; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 1.10.1.4 | DO-RECENZJI |
| ADR-B-0301 | ADR-B-01 | BRAK-PUNKTU-W-WYJAŚNIENIU | 1.67 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 8.2.1.1 | DO-RECENZJI |
| ADR-B-0302 | ADR-B-02 | DWA-SKRAJNE, BRAK-PUNKTU-W-WYJAŚNIENIU | 2.00 | zastąpić skrajne dystraktory realistycznymi błędnymi interpretacjami przepisu; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 2.2.42.1.1 | DO-RECENZJI |
| ADR-B-0303 | ADR-B-06 | BRAK-PUNKTU-W-WYJAŚNIENIU | 1.60 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 5.2.2.1.1 | DO-RECENZJI |
| ADR-B-0304 | ADR-B-12 | DWA-SKRAJNE, DŁUGOŚĆ, KLUCZ-DŁUŻSZY, BRAK-PUNKTU-W-WYJAŚNIENIU | 2.64 | zastąpić skrajne dystraktory realistycznymi błędnymi interpretacjami przepisu; wyrównać długości i szczegółowość wariantów bez zmiany klucza; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 1.10.3.2.2(a) | DO-RECENZJI |
| ADR-B-0305 | ADR-B-12 | BRAK-PUNKTU-W-WYJAŚNIENIU | 1.58 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 1.10.3.3 | DO-RECENZJI |
| ADR-B-0306 | ADR-B-13 | DWA-SKRAJNE, DŁUGOŚĆ, KLUCZ-DŁUŻSZY | 4.42 | zastąpić skrajne dystraktory realistycznymi błędnymi interpretacjami przepisu; wyrównać długości i szczegółowość wariantów bez zmiany klucza | DO-RECENZJI |
| ADR-B-0307 | ADR-B-02 | BRAK-PUNKTU-W-WYJAŚNIENIU | 1.61 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 2.2.52.1.2, 2.2.52.1.4 | DO-RECENZJI |
| ADR-B-0308 | ADR-B-11 | DŁUGOŚĆ, BRAK-PUNKTU-W-WYJAŚNIENIU | 2.27 | wyrównać długości i szczegółowość wariantów bez zmiany klucza; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 5.4.3.4 | DO-RECENZJI |
| ADR-B-0309 | ADR-B-02 | BRAK-PUNKTU-W-WYJAŚNIENIU | 1.42 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 2.2.62.1.1 | DO-RECENZJI |
| ADR-B-0310 | ADR-B-04 | DWA-SKRAJNE, KLUCZ-DŁUŻSZY | 2.18 | zastąpić skrajne dystraktory realistycznymi błędnymi interpretacjami przepisu; wyrównać długości i szczegółowość wariantów bez zmiany klucza | DO-RECENZJI |
| ADR-B-0311 | ADR-B-02 | KLUCZ-DŁUŻSZY, BRAK-PUNKTU-W-WYJAŚNIENIU, SPRAWDŹ-WARUNEK | 1.96 | wyrównać długości i szczegółowość wariantów bez zmiany klucza; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 2.2.62.1.2; sprawdzić konieczność doprecyzowania sytuacji i wyjątku | DO-RECENZJI |
| ADR-B-0312 | ADR-B-01 | DWA-SKRAJNE, DŁUGOŚĆ, KLUCZ-DŁUŻSZY, BRAK-PUNKTU-W-WYJAŚNIENIU | 5.38 | zastąpić skrajne dystraktory realistycznymi błędnymi interpretacjami przepisu; wyrównać długości i szczegółowość wariantów bez zmiany klucza; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 1.2.1 | DO-RECENZJI |
| ADR-B-0313 | ADR-B-01 | DŁUGOŚĆ, KLUCZ-DŁUŻSZY, BRAK-PUNKTU-W-WYJAŚNIENIU | 2.51 | wyrównać długości i szczegółowość wariantów bez zmiany klucza; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 1.1.3.1(a)(i) | DO-RECENZJI |
| ADR-B-0314 | ADR-B-01 | BRAK-PUNKTU-W-WYJAŚNIENIU | 1.59 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 3.2.1, objaśnienie kolumny (2) | DO-RECENZJI |
| ADR-B-0315 | ADR-B-02 | DŁUGOŚĆ, KLUCZ-DŁUŻSZY, BRAK-PUNKTU-W-WYJAŚNIENIU | 7.43 | wyrównać długości i szczegółowość wariantów bez zmiany klucza; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 2.2.9.1.7.2; tabela A UN 3551 | DO-RECENZJI |
| ADR-B-0316 | ADR-B-02 | DWA-SKRAJNE, BRAK-PUNKTU-W-WYJAŚNIENIU | 1.68 | zastąpić skrajne dystraktory realistycznymi błędnymi interpretacjami przepisu; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 2.2.1.1.5 (podklasa 1.1) | DO-RECENZJI |
| ADR-B-0317 | ADR-B-02 | DŁUGOŚĆ, KLUCZ-DŁUŻSZY, BRAK-PUNKTU-W-WYJAŚNIENIU | 3.17 | wyrównać długości i szczegółowość wariantów bez zmiany klucza; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 2.2.7.1.1 oraz 2.2.7.2.2.1–2.2.7.2.2.6 | DO-RECENZJI |
| ADR-B-0318 | ADR-B-03 | DŁUGOŚĆ, KLUCZ-DŁUŻSZY, BRAK-PUNKTU-W-WYJAŚNIENIU | 3.20 | wyrównać długości i szczegółowość wariantów bez zmiany klucza; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 2.1.3.5.5 | DO-RECENZJI |
| ADR-B-0319 | ADR-B-08 | DWA-SKRAJNE, BRAK-PUNKTU-W-WYJAŚNIENIU | 1.42 | zastąpić skrajne dystraktory realistycznymi błędnymi interpretacjami przepisu; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 9.1.1.2 (definicje pojazdów EX/II i EX/III) | DO-RECENZJI |
| ADR-B-0320 | ADR-B-10 | DŁUGOŚĆ, BRAK-PUNKTU-W-WYJAŚNIENIU | 3.16 | wyrównać długości i szczegółowość wariantów bez zmiany klucza; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 1.1.4.2.1 | DO-RECENZJI |
| ADR-B-0321 | ADR-B-10 | BRAK-PUNKTU-W-WYJAŚNIENIU | 1.15 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 1.1.4.2.3 | DO-RECENZJI |
| ADR-B-0322 | ADR-B-11 | DWA-SKRAJNE, DŁUGOŚĆ | 2.67 | zastąpić skrajne dystraktory realistycznymi błędnymi interpretacjami przepisu; wyrównać długości i szczegółowość wariantów bez zmiany klucza | DO-RECENZJI |
| ADR-B-0323 | ADR-B-01 | brak flag | 1.63 | nie wykryto sygnału w przesiewie; pozostawić do oceny eksperckiej | DO-RECENZJI |
| ADR-B-0324 | ADR-B-09 | brak flag | 1.86 | nie wykryto sygnału w przesiewie; pozostawić do oceny eksperckiej | DO-RECENZJI |
| ADR-B-0325 | ADR-B-03 | BRAK-PUNKTU-W-WYJAŚNIENIU | 1.76 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 2.1.3.5.5 | DO-RECENZJI |
| ADR-B-0326 | ADR-B-03 | BRAK-PUNKTU-W-WYJAŚNIENIU | 1.96 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 2.1.3.5.5 | DO-RECENZJI |
| ADR-B-0327 | ADR-B-03 | DŁUGOŚĆ, KLUCZ-DŁUŻSZY, BRAK-PUNKTU-W-WYJAŚNIENIU | 2.48 | wyrównać długości i szczegółowość wariantów bez zmiany klucza; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 2.1.3.5.5 | DO-RECENZJI |
| ADR-B-0328 | ADR-B-03 | BRAK-PUNKTU-W-WYJAŚNIENIU | 1.30 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 2.1.3.5.5 | DO-RECENZJI |
| ADR-B-0329 | ADR-B-03 | DŁUGOŚĆ, KLUCZ-DŁUŻSZY, BRAK-PUNKTU-W-WYJAŚNIENIU, SPRAWDŹ-WARUNEK | 2.64 | wyrównać długości i szczegółowość wariantów bez zmiany klucza; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 2.1.3.5.5; sprawdzić konieczność doprecyzowania sytuacji i wyjątku | DO-RECENZJI |
| ADR-B-0330 | ADR-B-03 | DŁUGOŚĆ, KLUCZ-DŁUŻSZY | 3.08 | wyrównać długości i szczegółowość wariantów bez zmiany klucza | DO-RECENZJI |
| ADR-B-0331 | ADR-B-03 | DŁUGOŚĆ, BRAK-PUNKTU-W-WYJAŚNIENIU | 4.64 | wyrównać długości i szczegółowość wariantów bez zmiany klucza; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 2.1.3.5.2 | DO-RECENZJI |
| ADR-B-0332 | ADR-B-03 | BRAK-PUNKTU-W-WYJAŚNIENIU | 1.18 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 2.1.3.5.3 | DO-RECENZJI |
| ADR-B-0333 | ADR-B-03 | brak flag | 1.15 | nie wykryto sygnału w przesiewie; pozostawić do oceny eksperckiej | DO-RECENZJI |
| ADR-B-0334 | ADR-B-03 | KLUCZ-DŁUŻSZY, BRAK-PUNKTU-W-WYJAŚNIENIU | 2.24 | wyrównać długości i szczegółowość wariantów bez zmiany klucza; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 2.1.3.6 | DO-RECENZJI |
| ADR-B-0335 | ADR-B-03 | DŁUGOŚĆ, KLUCZ-DŁUŻSZY, BRAK-PUNKTU-W-WYJAŚNIENIU | 2.78 | wyrównać długości i szczegółowość wariantów bez zmiany klucza; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 2.1.3.5.5 | DO-RECENZJI |
| ADR-B-0336 | ADR-B-03 | DWA-SKRAJNE, DŁUGOŚĆ, BRAK-PUNKTU-W-WYJAŚNIENIU | 6.71 | zastąpić skrajne dystraktory realistycznymi błędnymi interpretacjami przepisu; wyrównać długości i szczegółowość wariantów bez zmiany klucza; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 2.1.3.5.5 | DO-RECENZJI |
| ADR-B-0337 | ADR-B-03 | DŁUGOŚĆ | 2.68 | wyrównać długości i szczegółowość wariantów bez zmiany klucza | DO-RECENZJI |
| ADR-B-0338 | ADR-B-03 | DŁUGOŚĆ, KLUCZ-DŁUŻSZY | 2.64 | wyrównać długości i szczegółowość wariantów bez zmiany klucza | DO-RECENZJI |
| ADR-B-0339 | ADR-B-03 | DŁUGOŚĆ, KLUCZ-DŁUŻSZY | 3.33 | wyrównać długości i szczegółowość wariantów bez zmiany klucza | DO-RECENZJI |
| ADR-B-0340 | ADR-B-03 | DŁUGOŚĆ, KLUCZ-DŁUŻSZY, BRAK-PUNKTU-W-WYJAŚNIENIU | 2.67 | wyrównać długości i szczegółowość wariantów bez zmiany klucza; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 2.1.3.5.3 | DO-RECENZJI |
| ADR-B-0341 | ADR-B-03 | DŁUGOŚĆ | 4.21 | wyrównać długości i szczegółowość wariantów bez zmiany klucza | DO-RECENZJI |
| ADR-B-0342 | ADR-B-03 | DŁUGOŚĆ | 2.74 | wyrównać długości i szczegółowość wariantów bez zmiany klucza | DO-RECENZJI |
| ADR-B-0343 | ADR-B-03 | DŁUGOŚĆ, KLUCZ-DŁUŻSZY, BRAK-PUNKTU-W-WYJAŚNIENIU | 3.04 | wyrównać długości i szczegółowość wariantów bez zmiany klucza; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 2.1.3.5.5 | DO-RECENZJI |
| ADR-B-0344 | ADR-B-03 | DŁUGOŚĆ, KLUCZ-DŁUŻSZY, BRAK-PUNKTU-W-WYJAŚNIENIU | 3.61 | wyrównać długości i szczegółowość wariantów bez zmiany klucza; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 2.1.3.6 | DO-RECENZJI |
| ADR-B-0345 | ADR-B-04 | BRAK-PUNKTU-W-WYJAŚNIENIU | 1.75 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 8.4.1 | DO-RECENZJI |
| ADR-B-0346 | ADR-B-04 | DŁUGOŚĆ, KLUCZ-DŁUŻSZY, BRAK-PUNKTU-W-WYJAŚNIENIU | 2.48 | wyrównać długości i szczegółowość wariantów bez zmiany klucza; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 8.4.1(a) | DO-RECENZJI |
| ADR-B-0347 | ADR-B-04 | DŁUGOŚĆ, KLUCZ-DŁUŻSZY, BRAK-PUNKTU-W-WYJAŚNIENIU | 2.58 | wyrównać długości i szczegółowość wariantów bez zmiany klucza; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 8.4.1(a)–(b) | DO-RECENZJI |
| ADR-B-0348 | ADR-B-04 | DŁUGOŚĆ, BRAK-PUNKTU-W-WYJAŚNIENIU | 3.25 | wyrównać długości i szczegółowość wariantów bez zmiany klucza; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 8.4.1(c) | DO-RECENZJI |
| ADR-B-0349 | ADR-B-04 | DŁUGOŚĆ, KLUCZ-DŁUŻSZY, BRAK-PUNKTU-W-WYJAŚNIENIU | 3.52 | wyrównać długości i szczegółowość wariantów bez zmiany klucza; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 8.4.1(c) | DO-RECENZJI |
| ADR-B-0350 | ADR-B-04 | BRAK-PUNKTU-W-WYJAŚNIENIU | 1.91 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 8.4.1; 3.2 tabela A kol. (19) | DO-RECENZJI |
| ADR-B-0351 | ADR-B-04 | BRAK-PUNKTU-W-WYJAŚNIENIU | 1.32 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 8.3.7 | DO-RECENZJI |
| ADR-B-0352 | ADR-B-04 | BRAK-PUNKTU-W-WYJAŚNIENIU | 1.44 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 8.3.7; 8.1.5.2 | DO-RECENZJI |
| ADR-B-0353 | ADR-B-04 | DŁUGOŚĆ, KLUCZ-DŁUŻSZY, BRAK-PUNKTU-W-WYJAŚNIENIU | 2.85 | wyrównać długości i szczegółowość wariantów bez zmiany klucza; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 8.3.4 | DO-RECENZJI |
| ADR-B-0354 | ADR-B-04 | BRAK-PUNKTU-W-WYJAŚNIENIU | 1.97 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 5.4.3.4 | DO-RECENZJI |
| ADR-B-0355 | ADR-B-04 | DŁUGOŚĆ, BRAK-PUNKTU-W-WYJAŚNIENIU | 2.58 | wyrównać długości i szczegółowość wariantów bez zmiany klucza; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 5.4.3.4 | DO-RECENZJI |
| ADR-B-0356 | ADR-B-04 | KLUCZ-DŁUŻSZY, BRAK-PUNKTU-W-WYJAŚNIENIU | 1.90 | wyrównać długości i szczegółowość wariantów bez zmiany klucza; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 5.4.3.4 | DO-RECENZJI |
| ADR-B-0357 | ADR-B-04 | BRAK-PUNKTU-W-WYJAŚNIENIU | 1.43 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 8.3.3 | DO-RECENZJI |
| ADR-B-0358 | ADR-B-04 | DWA-SKRAJNE, KLUCZ-DŁUŻSZY, BRAK-PUNKTU-W-WYJAŚNIENIU | 2.23 | zastąpić skrajne dystraktory realistycznymi błędnymi interpretacjami przepisu; wyrównać długości i szczegółowość wariantów bez zmiany klucza; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 8.3.6 | DO-RECENZJI |
| ADR-B-0359 | ADR-B-04 | BRAK-PUNKTU-W-WYJAŚNIENIU, SPRAWDŹ-WARUNEK | 1.48 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 8.3.6; sprawdzić konieczność doprecyzowania sytuacji i wyjątku | DO-RECENZJI |
| ADR-B-0360 | ADR-B-04 | DŁUGOŚĆ, KLUCZ-DŁUŻSZY, BRAK-PUNKTU-W-WYJAŚNIENIU | 3.33 | wyrównać długości i szczegółowość wariantów bez zmiany klucza; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 8.3.5 | DO-RECENZJI |
| ADR-B-0361 | ADR-B-04 | BRAK-PUNKTU-W-WYJAŚNIENIU | 1.93 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 5.4.3.4 | DO-RECENZJI |
| ADR-B-0362 | ADR-B-04 | BRAK-PUNKTU-W-WYJAŚNIENIU | 1.39 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 5.4.3.4 | DO-RECENZJI |
| ADR-B-0363 | ADR-B-07 | BRAK-PUNKTU-W-WYJAŚNIENIU | 1.72 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 1.4.2.2.3 | DO-RECENZJI |
| ADR-B-0364 | ADR-B-07 | DŁUGOŚĆ, KLUCZ-DŁUŻSZY, BRAK-PUNKTU-W-WYJAŚNIENIU | 3.35 | wyrównać długości i szczegółowość wariantów bez zmiany klucza; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 1.4.2.2.4 | DO-RECENZJI |
| ADR-B-0365 | ADR-B-07 | DŁUGOŚĆ, KLUCZ-DŁUŻSZY, BRAK-PUNKTU-W-WYJAŚNIENIU, SPRAWDŹ-WARUNEK | 6.42 | wyrównać długości i szczegółowość wariantów bez zmiany klucza; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 1.4.2.1.2; sprawdzić konieczność doprecyzowania sytuacji i wyjątku | DO-RECENZJI |
| ADR-B-0366 | ADR-B-07 | BRAK-PUNKTU-W-WYJAŚNIENIU | 2.05 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 1.4.2.1.3 | DO-RECENZJI |
| ADR-B-0367 | ADR-B-07 | DŁUGOŚĆ, KLUCZ-DŁUŻSZY, BRAK-PUNKTU-W-WYJAŚNIENIU | 2.91 | wyrównać długości i szczegółowość wariantów bez zmiany klucza; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 1.4.3.2(b) | DO-RECENZJI |
| ADR-B-0368 | ADR-B-07 | DWA-SKRAJNE, BRAK-PUNKTU-W-WYJAŚNIENIU | 1.74 | zastąpić skrajne dystraktory realistycznymi błędnymi interpretacjami przepisu; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 1.4.3.2(a) | DO-RECENZJI |
| ADR-B-0369 | ADR-B-07 | DŁUGOŚĆ, KLUCZ-DŁUŻSZY, BRAK-PUNKTU-W-WYJAŚNIENIU | 2.95 | wyrównać długości i szczegółowość wariantów bez zmiany klucza; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 1.4.3.7.1(a) | DO-RECENZJI |
| ADR-B-0370 | ADR-B-07 | DŁUGOŚĆ, KLUCZ-DŁUŻSZY, BRAK-PUNKTU-W-WYJAŚNIENIU | 7.23 | wyrównać długości i szczegółowość wariantów bez zmiany klucza; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 1.4.3.7.1(b) | DO-RECENZJI |
| ADR-B-0371 | ADR-B-07 | DŁUGOŚĆ, BRAK-PUNKTU-W-WYJAŚNIENIU | 3.50 | wyrównać długości i szczegółowość wariantów bez zmiany klucza; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 1.4.3.7.1(d) | DO-RECENZJI |
| ADR-B-0372 | ADR-B-07 | BRAK-PUNKTU-W-WYJAŚNIENIU | 1.96 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 1.4.3.7.1(e) | DO-RECENZJI |
| ADR-B-0373 | ADR-B-07 | DŁUGOŚĆ, KLUCZ-DŁUŻSZY, BRAK-PUNKTU-W-WYJAŚNIENIU | 3.50 | wyrównać długości i szczegółowość wariantów bez zmiany klucza; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 1.4.3.1.1(e) | DO-RECENZJI |
| ADR-B-0374 | ADR-B-07 | KLUCZ-DŁUŻSZY, BRAK-PUNKTU-W-WYJAŚNIENIU | 1.86 | wyrównać długości i szczegółowość wariantów bez zmiany klucza; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 1.4.2.2.1(f) | DO-RECENZJI |
| ADR-B-0375 | ADR-B-07 | KLUCZ-DŁUŻSZY, BRAK-PUNKTU-W-WYJAŚNIENIU | 1.93 | wyrównać długości i szczegółowość wariantów bez zmiany klucza; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 1.4.2.2.2 | DO-RECENZJI |
| ADR-B-0376 | ADR-B-07 | DŁUGOŚĆ, BRAK-PUNKTU-W-WYJAŚNIENIU | 2.33 | wyrównać długości i szczegółowość wariantów bez zmiany klucza; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 8.3.2 | DO-RECENZJI |
| ADR-B-0377 | ADR-B-07 | DŁUGOŚĆ, KLUCZ-DŁUŻSZY, BRAK-PUNKTU-W-WYJAŚNIENIU | 3.43 | wyrównać długości i szczegółowość wariantów bez zmiany klucza; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 1.4.2.3.1–1.4.2.3.2 | DO-RECENZJI |
| ADR-B-0378 | ADR-B-07 | DWA-SKRAJNE, BRAK-PUNKTU-W-WYJAŚNIENIU | 1.68 | zastąpić skrajne dystraktory realistycznymi błędnymi interpretacjami przepisu; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 1.4.3.1.1(c) | DO-RECENZJI |
| ADR-B-0379 | ADR-B-07 | DŁUGOŚĆ, BRAK-PUNKTU-W-WYJAŚNIENIU | 2.62 | wyrównać długości i szczegółowość wariantów bez zmiany klucza; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 1.4.2.2.1(e) | DO-RECENZJI |
| ADR-B-0380 | ADR-B-07 | BRAK-PUNKTU-W-WYJAŚNIENIU | 1.36 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 1.4.2.1.2 | DO-RECENZJI |
| ADR-B-0381 | ADR-B-10 | DŁUGOŚĆ, KLUCZ-DŁUŻSZY, BRAK-PUNKTU-W-WYJAŚNIENIU | 2.62 | wyrównać długości i szczegółowość wariantów bez zmiany klucza; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 1.1.4.2.1(a) | DO-RECENZJI |
| ADR-B-0382 | ADR-B-10 | DWA-SKRAJNE, BRAK-PUNKTU-W-WYJAŚNIENIU | 1.83 | zastąpić skrajne dystraktory realistycznymi błędnymi interpretacjami przepisu; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 1.1.4.2.1(b) | DO-RECENZJI |
| ADR-B-0383 | ADR-B-10 | DŁUGOŚĆ, KLUCZ-DŁUŻSZY, BRAK-PUNKTU-W-WYJAŚNIENIU | 2.96 | wyrównać długości i szczegółowość wariantów bez zmiany klucza; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 1.1.4.2.1(c) | DO-RECENZJI |
| ADR-B-0384 | ADR-B-10 | KLUCZ-DŁUŻSZY, BRAK-PUNKTU-W-WYJAŚNIENIU | 2.00 | wyrównać długości i szczegółowość wariantów bez zmiany klucza; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 1.1.4.2.1(c); 5.3.2.1.1 | DO-RECENZJI |
| ADR-B-0385 | ADR-B-10 | BRAK-PUNKTU-W-WYJAŚNIENIU | 1.54 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 1.1.4.2.1(c) | DO-RECENZJI |
| ADR-B-0386 | ADR-B-10 | DŁUGOŚĆ, BRAK-PUNKTU-W-WYJAŚNIENIU, SPRAWDŹ-WARUNEK | 5.00 | wyrównać długości i szczegółowość wariantów bez zmiany klucza; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 1.1.4.2.1 akapit końcowy; sprawdzić konieczność doprecyzowania sytuacji i wyjątku | DO-RECENZJI |
| ADR-B-0387 | ADR-B-10 | DWA-SKRAJNE, DŁUGOŚĆ, KLUCZ-DŁUŻSZY, BRAK-PUNKTU-W-WYJAŚNIENIU | 2.44 | zastąpić skrajne dystraktory realistycznymi błędnymi interpretacjami przepisu; wyrównać długości i szczegółowość wariantów bez zmiany klucza; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 1.1.4.2.2 | DO-RECENZJI |
| ADR-B-0388 | ADR-B-10 | DŁUGOŚĆ, KLUCZ-DŁUŻSZY, BRAK-PUNKTU-W-WYJAŚNIENIU | 3.35 | wyrównać długości i szczegółowość wariantów bez zmiany klucza; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 1.1.4.2.3 | DO-RECENZJI |
| ADR-B-0389 | ADR-B-10 | BRAK-PUNKTU-W-WYJAŚNIENIU | 1.68 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 1.1.4.2.1 | DO-RECENZJI |
| ADR-B-0390 | ADR-B-10 | DWA-SKRAJNE, DŁUGOŚĆ, KLUCZ-DŁUŻSZY, BRAK-PUNKTU-W-WYJAŚNIENIU | 3.48 | zastąpić skrajne dystraktory realistycznymi błędnymi interpretacjami przepisu; wyrównać długości i szczegółowość wariantów bez zmiany klucza; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 5.4.2 | DO-RECENZJI |
| ADR-B-0391 | ADR-B-10 | DŁUGOŚĆ, BRAK-PUNKTU-W-WYJAŚNIENIU | 2.53 | wyrównać długości i szczegółowość wariantów bez zmiany klucza; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 5.4.2 | DO-RECENZJI |
| ADR-B-0392 | ADR-B-10 | DŁUGOŚĆ, KLUCZ-DŁUŻSZY, BRAK-PUNKTU-W-WYJAŚNIENIU | 2.60 | wyrównać długości i szczegółowość wariantów bez zmiany klucza; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 5.4.2 | DO-RECENZJI |
| ADR-B-0393 | ADR-B-10 | BRAK-PUNKTU-W-WYJAŚNIENIU | 1.42 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 5.4.2 | DO-RECENZJI |
| ADR-B-0394 | ADR-B-10 | KLUCZ-DŁUŻSZY, BRAK-PUNKTU-W-WYJAŚNIENIU | 2.00 | wyrównać długości i szczegółowość wariantów bez zmiany klucza; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 5.4.2 | DO-RECENZJI |
| ADR-B-0395 | ADR-B-10 | brak flag | 1.45 | nie wykryto sygnału w przesiewie; pozostawić do oceny eksperckiej | DO-RECENZJI |
| ADR-B-0396 | ADR-B-10 | DŁUGOŚĆ, BRAK-PUNKTU-W-WYJAŚNIENIU | 6.00 | wyrównać długości i szczegółowość wariantów bez zmiany klucza; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 1.1.4.2 | DO-RECENZJI |
| ADR-B-0397 | ADR-B-10 | BRAK-PUNKTU-W-WYJAŚNIENIU | 1.61 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 1.1.4.2.1(a) | DO-RECENZJI |
| ADR-B-0398 | ADR-B-10 | DŁUGOŚĆ, KLUCZ-DŁUŻSZY, BRAK-PUNKTU-W-WYJAŚNIENIU | 3.54 | wyrównać długości i szczegółowość wariantów bez zmiany klucza; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 1.1.4.2.3 | DO-RECENZJI |
| ADR-B-0399 | ADR-B-12 | DŁUGOŚĆ, KLUCZ-DŁUŻSZY, BRAK-PUNKTU-W-WYJAŚNIENIU | 2.70 | wyrównać długości i szczegółowość wariantów bez zmiany klucza; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 1.10.3.2.2(a) | DO-RECENZJI |
| ADR-B-0400 | ADR-B-12 | DŁUGOŚĆ, KLUCZ-DŁUŻSZY, BRAK-PUNKTU-W-WYJAŚNIENIU | 2.72 | wyrównać długości i szczegółowość wariantów bez zmiany klucza; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 1.10.3.2.2(b) | DO-RECENZJI |
| ADR-B-0401 | ADR-B-12 | DŁUGOŚĆ, KLUCZ-DŁUŻSZY, BRAK-PUNKTU-W-WYJAŚNIENIU, SPRAWDŹ-WARUNEK | 2.82 | wyrównać długości i szczegółowość wariantów bez zmiany klucza; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 1.10.3.2.2(c); sprawdzić konieczność doprecyzowania sytuacji i wyjątku | DO-RECENZJI |
| ADR-B-0402 | ADR-B-12 | KLUCZ-DŁUŻSZY, BRAK-PUNKTU-W-WYJAŚNIENIU | 1.73 | wyrównać długości i szczegółowość wariantów bez zmiany klucza; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 1.10.3.2.2(d) | DO-RECENZJI |
| ADR-B-0403 | ADR-B-12 | DŁUGOŚĆ, KLUCZ-DŁUŻSZY, BRAK-PUNKTU-W-WYJAŚNIENIU | 2.52 | wyrównać długości i szczegółowość wariantów bez zmiany klucza; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 1.10.3.2.2(e) | DO-RECENZJI |
| ADR-B-0404 | ADR-B-12 | KLUCZ-DŁUŻSZY, BRAK-PUNKTU-W-WYJAŚNIENIU | 2.14 | wyrównać długości i szczegółowość wariantów bez zmiany klucza; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 1.10.3.2.2(f) | DO-RECENZJI |
| ADR-B-0405 | ADR-B-12 | BRAK-PUNKTU-W-WYJAŚNIENIU | 2.00 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 1.10.3.2.2(g) | DO-RECENZJI |
| ADR-B-0406 | ADR-B-12 | DŁUGOŚĆ, KLUCZ-DŁUŻSZY, BRAK-PUNKTU-W-WYJAŚNIENIU | 4.63 | wyrównać długości i szczegółowość wariantów bez zmiany klucza; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 1.10.3.2.2(h) | DO-RECENZJI |
| ADR-B-0407 | ADR-B-12 | BRAK-PUNKTU-W-WYJAŚNIENIU | 1.80 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 1.10.3.3 | DO-RECENZJI |
| ADR-B-0408 | ADR-B-12 | BRAK-PUNKTU-W-WYJAŚNIENIU | 1.86 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 1.10.3.3 | DO-RECENZJI |
| ADR-B-0409 | ADR-B-12 | KLUCZ-DŁUŻSZY, BRAK-PUNKTU-W-WYJAŚNIENIU | 1.71 | wyrównać długości i szczegółowość wariantów bez zmiany klucza; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 1.10.2.2 | DO-RECENZJI |
| ADR-B-0410 | ADR-B-12 | DŁUGOŚĆ, BRAK-PUNKTU-W-WYJAŚNIENIU | 3.04 | wyrównać długości i szczegółowość wariantów bez zmiany klucza; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 1.10.2.2 | DO-RECENZJI |
| ADR-B-0411 | ADR-B-12 | DŁUGOŚĆ, KLUCZ-DŁUŻSZY, BRAK-PUNKTU-W-WYJAŚNIENIU | 4.50 | wyrównać długości i szczegółowość wariantów bez zmiany klucza; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 1.10.2.3 | DO-RECENZJI |
| ADR-B-0412 | ADR-B-12 | BRAK-PUNKTU-W-WYJAŚNIENIU | 1.51 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 1.10.2.4 | DO-RECENZJI |
| ADR-B-0413 | ADR-B-12 | BRAK-PUNKTU-W-WYJAŚNIENIU | 1.74 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 1.10.1.2 | DO-RECENZJI |
| ADR-B-0414 | ADR-B-12 | BRAK-PUNKTU-W-WYJAŚNIENIU | 1.68 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 1.10.1.2 | DO-RECENZJI |
| ADR-B-0415 | ADR-B-12 | DŁUGOŚĆ, KLUCZ-DŁUŻSZY, BRAK-PUNKTU-W-WYJAŚNIENIU | 2.66 | wyrównać długości i szczegółowość wariantów bez zmiany klucza; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 1.10.1.3 | DO-RECENZJI |
| ADR-B-0416 | ADR-B-12 | BRAK-PUNKTU-W-WYJAŚNIENIU | 1.52 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 1.10.1.4 | DO-RECENZJI |
| ADR-B-0417 | ADR-B-08 | DŁUGOŚĆ, BRAK-PUNKTU-W-WYJAŚNIENIU | 3.91 | wyrównać długości i szczegółowość wariantów bez zmiany klucza; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 8.1.4.1 | DO-RECENZJI |
| ADR-B-0418 | ADR-B-08 | BRAK-PUNKTU-W-WYJAŚNIENIU | 1.53 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 8.1.4.1 | DO-RECENZJI |
| ADR-B-0419 | ADR-B-08 | BRAK-PUNKTU-W-WYJAŚNIENIU | 1.25 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 8.1.4.1 | DO-RECENZJI |
| ADR-B-0420 | ADR-B-08 | KLUCZ-DŁUŻSZY, BRAK-PUNKTU-W-WYJAŚNIENIU | 1.86 | wyrównać długości i szczegółowość wariantów bez zmiany klucza; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 8.1.4.1 | DO-RECENZJI |
| ADR-B-0421 | ADR-B-08 | BRAK-PUNKTU-W-WYJAŚNIENIU | 1.21 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 8.1.4.2 | DO-RECENZJI |
| ADR-B-0422 | ADR-B-08 | BRAK-PUNKTU-W-WYJAŚNIENIU | 1.57 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 8.1.4.4–8.1.4.5 | DO-RECENZJI |
| ADR-B-0423 | ADR-B-08 | DWA-SKRAJNE, BRAK-PUNKTU-W-WYJAŚNIENIU | 1.94 | zastąpić skrajne dystraktory realistycznymi błędnymi interpretacjami przepisu; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 8.1.4.5 | DO-RECENZJI |
| ADR-B-0424 | ADR-B-09 | brak flag | 1.57 | nie wykryto sygnału w przesiewie; pozostawić do oceny eksperckiej | DO-RECENZJI |
| ADR-B-0425 | ADR-B-09 | BRAK-PUNKTU-W-WYJAŚNIENIU | 1.76 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 7.5.2.1, uwaga (a) | DO-RECENZJI |
| ADR-B-0426 | ADR-B-09 | DŁUGOŚĆ, KLUCZ-DŁUŻSZY, BRAK-PUNKTU-W-WYJAŚNIENIU | 6.55 | wyrównać długości i szczegółowość wariantów bez zmiany klucza; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 7.5.2.1 tabela | DO-RECENZJI |
| ADR-B-0427 | ADR-B-09 | BRAK-PUNKTU-W-WYJAŚNIENIU, SPRAWDŹ-WARUNEK | 1.24 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 7.5.2.1, uwaga (d); sprawdzić konieczność doprecyzowania sytuacji i wyjątku | DO-RECENZJI |
| ADR-B-0428 | ADR-B-09 | brak flag | 1.46 | nie wykryto sygnału w przesiewie; pozostawić do oceny eksperckiej | DO-RECENZJI |
| ADR-B-0429 | ADR-B-09 | DŁUGOŚĆ, KLUCZ-DŁUŻSZY, BRAK-PUNKTU-W-WYJAŚNIENIU | 2.52 | wyrównać długości i szczegółowość wariantów bez zmiany klucza; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 7.5.2.1 | DO-RECENZJI |
| ADR-B-0430 | ADR-B-11 | BRAK-PUNKTU-W-WYJAŚNIENIU | 1.54 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 8.6.3.1; 8.6.4 | DO-RECENZJI |
| ADR-B-0431 | ADR-B-11 | BRAK-PUNKTU-W-WYJAŚNIENIU | 1.74 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 8.6.3.1 | DO-RECENZJI |
| ADR-B-0432 | ADR-B-11 | DWA-SKRAJNE, BRAK-PUNKTU-W-WYJAŚNIENIU | 1.82 | zastąpić skrajne dystraktory realistycznymi błędnymi interpretacjami przepisu; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 8.6.3.2 | DO-RECENZJI |
| ADR-B-0433 | ADR-B-11 | DŁUGOŚĆ, KLUCZ-DŁUŻSZY, BRAK-PUNKTU-W-WYJAŚNIENIU | 4.80 | wyrównać długości i szczegółowość wariantów bez zmiany klucza; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 1.9.5.3.5 | DO-RECENZJI |
| ADR-B-0434 | ADR-B-11 | DŁUGOŚĆ, KLUCZ-DŁUŻSZY, BRAK-PUNKTU-W-WYJAŚNIENIU | 2.35 | wyrównać długości i szczegółowość wariantów bez zmiany klucza; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 8.6.3.1; 3.2 tabela A kol. (15) | DO-RECENZJI |
| ADR-B-0435 | ADR-B-11 | BRAK-PUNKTU-W-WYJAŚNIENIU | 1.89 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 5.4.3.4 | DO-RECENZJI |
| ADR-B-0436 | ADR-B-09 | BRAK-PUNKTU-W-WYJAŚNIENIU | 1.70 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 7.5.1.2; 1.4.3.1.1(b) | DO-RECENZJI |
| ADR-B-0437 | ADR-B-10 | DWA-SKRAJNE, DŁUGOŚĆ, KLUCZ-DŁUŻSZY, BRAK-PUNKTU-W-WYJAŚNIENIU | 2.79 | zastąpić skrajne dystraktory realistycznymi błędnymi interpretacjami przepisu; wyrównać długości i szczegółowość wariantów bez zmiany klucza; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 1.1.4.5.1 | DO-RECENZJI |
| ADR-B-0438 | ADR-B-10 | BRAK-PUNKTU-W-WYJAŚNIENIU | 2.00 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 1.1.4.5.1 | DO-RECENZJI |
| ADR-B-0439 | ADR-B-10 | BRAK-PUNKTU-W-WYJAŚNIENIU | 1.92 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 1.1.4.5.2 | DO-RECENZJI |
| ADR-B-0440 | ADR-B-10 | BRAK-PUNKTU-W-WYJAŚNIENIU | 1.85 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 1.1.4.5.2 | DO-RECENZJI |
| ADR-B-0441 | ADR-B-10 | BRAK-PUNKTU-W-WYJAŚNIENIU | 1.73 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 1.1.4.5.2 | DO-RECENZJI |
| ADR-B-0442 | ADR-B-10 | DŁUGOŚĆ, KLUCZ-DŁUŻSZY, BRAK-PUNKTU-W-WYJAŚNIENIU | 3.02 | wyrównać długości i szczegółowość wariantów bez zmiany klucza; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 1.1.4.5.3 | DO-RECENZJI |
| ADR-B-0443 | ADR-B-10 | DWA-SKRAJNE, BRAK-PUNKTU-W-WYJAŚNIENIU | 1.36 | zastąpić skrajne dystraktory realistycznymi błędnymi interpretacjami przepisu; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 1.1.4.5.3 | DO-RECENZJI |
| ADR-B-0444 | ADR-B-10 | DŁUGOŚĆ, KLUCZ-DŁUŻSZY, BRAK-PUNKTU-W-WYJAŚNIENIU | 4.28 | wyrównać długości i szczegółowość wariantów bez zmiany klucza; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 1.1.4.3 | DO-RECENZJI |
| ADR-B-0445 | ADR-B-10 | DŁUGOŚĆ, KLUCZ-DŁUŻSZY, BRAK-PUNKTU-W-WYJAŚNIENIU | 3.50 | wyrównać długości i szczegółowość wariantów bez zmiany klucza; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 1.1.4.3 | DO-RECENZJI |
| ADR-B-0446 | ADR-B-10 | BRAK-PUNKTU-W-WYJAŚNIENIU, SPRAWDŹ-WARUNEK | 1.65 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 1.1.4.3; sprawdzić konieczność doprecyzowania sytuacji i wyjątku | DO-RECENZJI |
| ADR-B-0447 | ADR-B-10 | brak flag | 1.90 | nie wykryto sygnału w przesiewie; pozostawić do oceny eksperckiej | DO-RECENZJI |
| ADR-B-0448 | ADR-B-10 | DWA-SKRAJNE, KLUCZ-DŁUŻSZY, BRAK-PUNKTU-W-WYJAŚNIENIU | 1.85 | zastąpić skrajne dystraktory realistycznymi błędnymi interpretacjami przepisu; wyrównać długości i szczegółowość wariantów bez zmiany klucza; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 1.1.4.7.2 | DO-RECENZJI |
| ADR-B-0449 | ADR-B-10 | BRAK-PUNKTU-W-WYJAŚNIENIU | 2.03 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 1.1.4.7.2(a) | DO-RECENZJI |
| ADR-B-0450 | ADR-B-10 | DWA-SKRAJNE, DŁUGOŚĆ, BRAK-PUNKTU-W-WYJAŚNIENIU | 2.31 | zastąpić skrajne dystraktory realistycznymi błędnymi interpretacjami przepisu; wyrównać długości i szczegółowość wariantów bez zmiany klucza; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 1.1.4.7.2(b) | DO-RECENZJI |
| ADR-B-0451 | ADR-B-10 | KLUCZ-DŁUŻSZY, BRAK-PUNKTU-W-WYJAŚNIENIU | 2.20 | wyrównać długości i szczegółowość wariantów bez zmiany klucza; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 1.1.4.7.2(c) | DO-RECENZJI |
| ADR-B-0452 | ADR-B-10 | DŁUGOŚĆ, KLUCZ-DŁUŻSZY, BRAK-PUNKTU-W-WYJAŚNIENIU | 2.44 | wyrównać długości i szczegółowość wariantów bez zmiany klucza; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 1.1.4.7.2(c) | DO-RECENZJI |
| ADR-B-0453 | ADR-B-10 | brak flag | 1.64 | nie wykryto sygnału w przesiewie; pozostawić do oceny eksperckiej | DO-RECENZJI |
| ADR-B-0454 | ADR-B-10 | brak flag | 1.30 | nie wykryto sygnału w przesiewie; pozostawić do oceny eksperckiej | DO-RECENZJI |
| ADR-B-0455 | ADR-B-12 | DWA-SKRAJNE, DŁUGOŚĆ | 2.32 | zastąpić skrajne dystraktory realistycznymi błędnymi interpretacjami przepisu; wyrównać długości i szczegółowość wariantów bez zmiany klucza | DO-RECENZJI |
| ADR-B-0456 | ADR-B-12 | DŁUGOŚĆ, BRAK-PUNKTU-W-WYJAŚNIENIU, SPRAWDŹ-WARUNEK | 2.43 | wyrównać długości i szczegółowość wariantów bez zmiany klucza; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 1.10.3.1.2 (tabela i przypis c); sprawdzić konieczność doprecyzowania sytuacji i wyjątku | DO-RECENZJI |
| ADR-B-0457 | ADR-B-12 | DŁUGOŚĆ, KLUCZ-DŁUŻSZY | 3.68 | wyrównać długości i szczegółowość wariantów bez zmiany klucza | DO-RECENZJI |
| ADR-B-0458 | ADR-B-12 | DŁUGOŚĆ, KLUCZ-DŁUŻSZY, BRAK-PUNKTU-W-WYJAŚNIENIU | 2.55 | wyrównać długości i szczegółowość wariantów bez zmiany klucza; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 1.10.3.1.2 przypis a | DO-RECENZJI |
| ADR-B-0459 | ADR-B-12 | BRAK-PUNKTU-W-WYJAŚNIENIU | 1.46 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 1.10.3.1.2 | DO-RECENZJI |
| ADR-B-0460 | ADR-B-12 | KLUCZ-DŁUŻSZY, SPRAWDŹ-WARUNEK | 2.16 | wyrównać długości i szczegółowość wariantów bez zmiany klucza; sprawdzić konieczność doprecyzowania sytuacji i wyjątku | DO-RECENZJI |
| ADR-B-0461 | ADR-B-03 | DWA-SKRAJNE, BRAK-PUNKTU-W-WYJAŚNIENIU | 1.61 | zastąpić skrajne dystraktory realistycznymi błędnymi interpretacjami przepisu; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 5.2.1.8.1 | DO-RECENZJI |
| ADR-B-0462 | ADR-B-03 | KLUCZ-DŁUŻSZY, BRAK-PUNKTU-W-WYJAŚNIENIU | 2.11 | wyrównać długości i szczegółowość wariantów bez zmiany klucza; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 5.2.1.8.1 | DO-RECENZJI |
| ADR-B-0463 | ADR-B-03 | DŁUGOŚĆ, BRAK-PUNKTU-W-WYJAŚNIENIU | 2.36 | wyrównać długości i szczegółowość wariantów bez zmiany klucza; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 5.2.1.8.1 | DO-RECENZJI |
| ADR-B-0464 | ADR-B-03 | DWA-SKRAJNE | 1.47 | zastąpić skrajne dystraktory realistycznymi błędnymi interpretacjami przepisu | DO-RECENZJI |
| ADR-B-0465 | ADR-B-03 | KLUCZ-DŁUŻSZY, SPRAWDŹ-WARUNEK | 2.03 | wyrównać długości i szczegółowość wariantów bez zmiany klucza; sprawdzić konieczność doprecyzowania sytuacji i wyjątku | DO-RECENZJI |
| ADR-B-0466 | ADR-B-03 | DŁUGOŚĆ | 2.90 | wyrównać długości i szczegółowość wariantów bez zmiany klucza | DO-RECENZJI |
| ADR-B-0467 | ADR-B-03 | BRAK-PUNKTU-W-WYJAŚNIENIU | 1.93 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 5.4.1.1.18 | DO-RECENZJI |
| ADR-B-0468 | ADR-B-03 | DWA-SKRAJNE, BRAK-PUNKTU-W-WYJAŚNIENIU | 1.17 | zastąpić skrajne dystraktory realistycznymi błędnymi interpretacjami przepisu; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 5.3.6.1 | DO-RECENZJI |
| ADR-B-0469 | ADR-B-03 | BRAK-PUNKTU-W-WYJAŚNIENIU | 1.20 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 5.3.6.2 | DO-RECENZJI |
| ADR-B-0470 | ADR-B-03 | DŁUGOŚĆ, BRAK-PUNKTU-W-WYJAŚNIENIU | 2.45 | wyrównać długości i szczegółowość wariantów bez zmiany klucza; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 5.3.6.2 | DO-RECENZJI |
| ADR-B-0471 | ADR-B-04 | DŁUGOŚĆ, KLUCZ-DŁUŻSZY | 2.87 | wyrównać długości i szczegółowość wariantów bez zmiany klucza | DO-RECENZJI |
| ADR-B-0472 | ADR-B-04 | DWA-SKRAJNE, BRAK-PUNKTU-W-WYJAŚNIENIU | 1.57 | zastąpić skrajne dystraktory realistycznymi błędnymi interpretacjami przepisu; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 8.3.2 | DO-RECENZJI |
| ADR-B-0473 | ADR-B-04 | KLUCZ-DŁUŻSZY | 1.72 | wyrównać długości i szczegółowość wariantów bez zmiany klucza | DO-RECENZJI |
| ADR-B-0474 | ADR-B-04 | DŁUGOŚĆ, KLUCZ-DŁUŻSZY, BRAK-PUNKTU-W-WYJAŚNIENIU | 2.41 | wyrównać długości i szczegółowość wariantów bez zmiany klucza; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 7.5.1.2 | DO-RECENZJI |
| ADR-B-0475 | ADR-B-04 | DŁUGOŚĆ, KLUCZ-DŁUŻSZY, BRAK-PUNKTU-W-WYJAŚNIENIU | 2.45 | wyrównać długości i szczegółowość wariantów bez zmiany klucza; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 7.5.1.2 | DO-RECENZJI |
| ADR-B-0476 | ADR-B-04 | DWA-SKRAJNE, DŁUGOŚĆ, KLUCZ-DŁUŻSZY, BRAK-PUNKTU-W-WYJAŚNIENIU | 2.34 | zastąpić skrajne dystraktory realistycznymi błędnymi interpretacjami przepisu; wyrównać długości i szczegółowość wariantów bez zmiany klucza; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 7.5.1.3 | DO-RECENZJI |
| ADR-B-0477 | ADR-B-07 | BRAK-PUNKTU-W-WYJAŚNIENIU | 2.10 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 1.4.2.3.3 | DO-RECENZJI |
| ADR-B-0478 | ADR-B-07 | DŁUGOŚĆ, KLUCZ-DŁUŻSZY, BRAK-PUNKTU-W-WYJAŚNIENIU | 3.79 | wyrównać długości i szczegółowość wariantów bez zmiany klucza; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 1.4.3.7.2 | DO-RECENZJI |
| ADR-B-0479 | ADR-B-07 | BRAK-PUNKTU-W-WYJAŚNIENIU | 1.47 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 1.4.3.1.2 | DO-RECENZJI |
| ADR-B-0480 | ADR-B-07 | DŁUGOŚĆ, BRAK-PUNKTU-W-WYJAŚNIENIU | 2.28 | wyrównać długości i szczegółowość wariantów bez zmiany klucza; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 1.4.3.7.1(d)(i) | DO-RECENZJI |
| ADR-B-0481 | ADR-B-07 | BRAK-PUNKTU-W-WYJAŚNIENIU | 1.53 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 1.4.3.7.1(d)(ii) | DO-RECENZJI |
| ADR-B-0482 | ADR-B-07 | DWA-SKRAJNE, DŁUGOŚĆ, BRAK-PUNKTU-W-WYJAŚNIENIU | 2.82 | zastąpić skrajne dystraktory realistycznymi błędnymi interpretacjami przepisu; wyrównać długości i szczegółowość wariantów bez zmiany klucza; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 1.4.3.1.2; 1.4.3.1.1(d) | DO-RECENZJI |
| ADR-B-0483 | ADR-B-08 | DŁUGOŚĆ, BRAK-PUNKTU-W-WYJAŚNIENIU | 3.35 | wyrównać długości i szczegółowość wariantów bez zmiany klucza; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 8.1.5.2, przypis 2 | DO-RECENZJI |
| ADR-B-0484 | ADR-B-08 | DWA-SKRAJNE, BRAK-PUNKTU-W-WYJAŚNIENIU | 1.27 | zastąpić skrajne dystraktory realistycznymi błędnymi interpretacjami przepisu; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 8.1.5.3, przypis 4 | DO-RECENZJI |
| ADR-B-0485 | ADR-B-08 | BRAK-PUNKTU-W-WYJAŚNIENIU | 1.75 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 8.1.5.3 | DO-RECENZJI |
| ADR-B-0486 | ADR-B-08 | DŁUGOŚĆ, KLUCZ-DŁUŻSZY, BRAK-PUNKTU-W-WYJAŚNIENIU | 3.70 | wyrównać długości i szczegółowość wariantów bez zmiany klucza; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 8.1.5.3, przypis 4 | DO-RECENZJI |
| ADR-B-0487 | ADR-B-11 | BRAK-PUNKTU-W-WYJAŚNIENIU | 1.33 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 8.6.4, kod D/E | DO-RECENZJI |
| ADR-B-0488 | ADR-B-11 | DWA-SKRAJNE, BRAK-PUNKTU-W-WYJAŚNIENIU | 1.36 | zastąpić skrajne dystraktory realistycznymi błędnymi interpretacjami przepisu; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 8.6.4, kod D/E | DO-RECENZJI |
| ADR-B-0489 | ADR-B-11 | BRAK-PUNKTU-W-WYJAŚNIENIU | 1.91 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 8.6.4, kod B/D | DO-RECENZJI |
| ADR-B-0490 | ADR-B-11 | DŁUGOŚĆ, KLUCZ-DŁUŻSZY, BRAK-PUNKTU-W-WYJAŚNIENIU | 2.73 | wyrównać długości i szczegółowość wariantów bez zmiany klucza; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 8.6.4, kod B1000C | DO-RECENZJI |
| ADR-B-0491 | ADR-B-09 | DWA-SKRAJNE | 1.50 | zastąpić skrajne dystraktory realistycznymi błędnymi interpretacjami przepisu | DO-RECENZJI |
| ADR-B-0492 | ADR-B-09 | DŁUGOŚĆ, KLUCZ-DŁUŻSZY, BRAK-PUNKTU-W-WYJAŚNIENIU | 6.18 | wyrównać długości i szczegółowość wariantów bez zmiany klucza; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 7.5.2.1 uwaga 1; 5.4.1.4.2 | DO-RECENZJI |
| ADR-B-0493 | ADR-B-05 | BRAK-PUNKTU-W-WYJAŚNIENIU | 2.05 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 5.4.3.4 (instrukcje pisemne) | DO-RECENZJI |
| ADR-B-0494 | ADR-B-05 | DŁUGOŚĆ, KLUCZ-DŁUŻSZY, BRAK-PUNKTU-W-WYJAŚNIENIU | 7.47 | wyrównać długości i szczegółowość wariantów bez zmiany klucza; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 5.4.3.4 (instrukcje pisemne) | DO-RECENZJI |
| ADR-B-0495 | ADR-B-02 | BRAK-PUNKTU-W-WYJAŚNIENIU | 1.56 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 2.2.1.1.5, podklasa 1.2 | DO-RECENZJI |
| ADR-B-0496 | ADR-B-02 | DWA-SKRAJNE, BRAK-PUNKTU-W-WYJAŚNIENIU | 2.11 | zastąpić skrajne dystraktory realistycznymi błędnymi interpretacjami przepisu; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 2.2.1.1.5, podklasa 1.3 | DO-RECENZJI |
| ADR-B-0497 | ADR-B-02 | DŁUGOŚĆ, KLUCZ-DŁUŻSZY, BRAK-PUNKTU-W-WYJAŚNIENIU | 2.49 | wyrównać długości i szczegółowość wariantów bez zmiany klucza; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 2.2.1.1.5, podklasa 1.5 | DO-RECENZJI |
| ADR-B-0498 | ADR-B-02 | BRAK-PUNKTU-W-WYJAŚNIENIU | 1.44 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 2.2.1.1.5, podklasa 1.6 | DO-RECENZJI |
| ADR-B-0499 | ADR-B-02 | DWA-SKRAJNE, DŁUGOŚĆ, KLUCZ-DŁUŻSZY | 5.58 | zastąpić skrajne dystraktory realistycznymi błędnymi interpretacjami przepisu; wyrównać długości i szczegółowość wariantów bez zmiany klucza | DO-RECENZJI |
| ADR-B-0500 | ADR-B-02 | DWA-SKRAJNE, BRAK-PUNKTU-W-WYJAŚNIENIU | 1.79 | zastąpić skrajne dystraktory realistycznymi błędnymi interpretacjami przepisu; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 2.2.9.1.7.2(a) i uwaga | DO-RECENZJI |
| ADR-B-0501 | ADR-B-02 | DWA-SKRAJNE, BRAK-PUNKTU-W-WYJAŚNIENIU | 1.70 | zastąpić skrajne dystraktory realistycznymi błędnymi interpretacjami przepisu; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 2.2.9.1.7.2(c) | DO-RECENZJI |
| ADR-B-0502 | ADR-B-02 | DŁUGOŚĆ, KLUCZ-DŁUŻSZY, BRAK-PUNKTU-W-WYJAŚNIENIU | 2.87 | wyrównać długości i szczegółowość wariantów bez zmiany klucza; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 2.2.9.1.7.2(d) | DO-RECENZJI |
| ADR-B-0503 | ADR-B-06 | DWA-SKRAJNE, DŁUGOŚĆ, BRAK-PUNKTU-W-WYJAŚNIENIU | 2.44 | POPRAWIONO: bardziej wiarygodne warianty, wyrównanie długości, konkretny punkt 5.3.2.3.1 w wyjaśnieniu; zaktualizowano obie migawki audytu | ZMIENIONE |
| ADR-B-0504 | ADR-B-06 | BRAK-PUNKTU-W-WYJAŚNIENIU, SPRAWDŹ-WARUNEK | 1.56 | po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 5.3.2.3.1; sprawdzić konieczność doprecyzowania sytuacji i wyjątku | DO-RECENZJI |
| ADR-B-0505 | ADR-B-06 | DWA-SKRAJNE, BRAK-PUNKTU-W-WYJAŚNIENIU | 2.17 | POPRAWIONO: bardziej wiarygodne warianty, wyrównanie długości, konkretny punkt 5.3.2.3.1 w wyjaśnieniu; zaktualizowano obie migawki audytu | ZMIENIONE |
| ADR-B-0506 | ADR-B-06 | DWA-SKRAJNE, BRAK-PUNKTU-W-WYJAŚNIENIU | 1.47 | zastąpić skrajne dystraktory realistycznymi błędnymi interpretacjami przepisu; po kontroli źródła dodać do wyjaśnienia dokładny punkt ADR 2025, 5.3.2.3.1 | DO-RECENZJI |

## Decyzja redakcyjna i kolejność następnych działań

1. Najpierw manualnie przejrzeć rekordy z dwoma skrajnymi dystraktorami i nierównowagą długości odpowiedzi, z priorytetem dla przypadków, gdzie poprawna odpowiedź jest jednocześnie najdłuższa. Każdą ingerencję połączyć z kontrolą dokładnego przepisu i zapisów A/B/C.
2. Dopełnić odniesienia do jednostki redakcyjnej w wyjaśnieniach **dopiero po** sprawdzeniu pełnego polskiego przepisu; samo `sources` pozostaje wskazaniem roboczym.
3. Nie przepisywać automatycznie kluczy w ramach etapu 4b. Zmiana kolejności wariantów pociąga za sobą synchronizację migawek oraz audytów A/B/C i historię decyzji.
4. Przy kolejnych poprawkach semantyki lub dystraktorów aktualizować właściwe istniejące `review/sequential/*.json` i `review/legal-clauses/*.json`. Przed publikacją cały bank wymaga rzeczywistej niezależnej recenzji.

**Granice:** pomiar jest powtarzalnym filtrem językowo-statystycznym, nie pełnym badaniem semantycznym ani dosłowną prawną weryfikacją 506 pozycji. Nie deklarować zakończenia recenzji merytorycznej.
