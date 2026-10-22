# ADR podstawowy — aktualne pokrycie kursu

**Stan roboczy: 22.10.2026.** Ramowy polski program to **13 tematów**, 18 godzin lekcyjnych teorii oraz wymagane ćwiczenia praktyczne (Dz.U. 2021 poz. 2150, załącznik nr 1). Nasza mapa 106 kompetencji to **wewnętrzny podział redakcyjny**, a nie urzędowy dokument z listą 106 wymagań.

## Co naprawdę zostało ukończone?

- **146 autorskich pytań** z A/B/C, własnym wyjaśnieniem i referencją do przepisu; **146 needs_review / 0 verified**.
- **103/103 kompetencji teoretycznych** ma co najmniej jedno pytanie w wersji roboczej. **0/103** ma pytanie zatwierdzone przez niezależnego eksperta.
- **3/3 cele praktyczne** mają scenariusz w `podstawowy/praktyka/SCENARIUSZE.md`. To program ćwiczeń, **nie dowód odbycia zajęć**.
- **13/13 lekcji ma szkic dydaktyczny** w `podstawowy/lekcje/`. Żadna nie ma jeszcze potwierdzonego odbioru eksperta.
- Rozkład prawidłowych opcji: A=48, B=49, C=49.
- Wciąż **brakuje gotowych ilustracji** wszystkich wymaganych nalepek i tablic, przykładowych poprawnie wypełnionych dokumentów oraz raportu kontroli tekstu prawnego i wszystkich błędnych wariantów odpowiedzi.

**Ważne:** 100% pokrycia *tematycznego pytaniami roboczymi* **nie oznacza gotowego kursu ani certyfikatu ADR**. Dla wybranych kompetencji jedno pytanie nie wystarczy do skutecznej nauki; kolejnym zadaniem jest zwiększenie głębokości pokrycia i niezależna kontrola.

## Matryca gotowości

| Dział | Zakres | Pytaniami roboczymi / teoria | Cele praktyczne | Liczba pytań | Zweryfikowane | Materiał do nauki |
|---|---|---:|---:|---:|---:|---|
| ADR-B-01 | Podstawy i wyłączenia | 7/7 | 0 | 11 | 0 | Szkic lekcji |
| ADR-B-02 | Klasyfikacja i zagrożenia | 14/14 | 0 | 15 | 0 | Szkic lekcji |
| ADR-B-03 | Środowisko i odpady | 6/6 | 0 | 8 | 0 | Szkic lekcji |
| ADR-B-04 | Zapobieganie zagrożeniom | 6/6 | 0 | 9 | 0 | Szkic lekcji |
| ADR-B-05 | Awaria, pierwsza pomoc | 12/12 | 3 | 15 | 0 | Szkic lekcji |
| ADR-B-06 | Oznakowanie | 9/9 | 0 | 10 | 0 | Szkic lekcji |
| ADR-B-07 | Obowiązki uczestników | 6/6 | 0 | 11 | 0 | Szkic lekcji |
| ADR-B-08 | Wyposażenie | 8/8 | 0 | 13 | 0 | Szkic lekcji |
| ADR-B-09 | Załadunek i mocowanie | 9/9 | 0 | 13 | 0 | Szkic lekcji |
| ADR-B-10 | Przewóz kombinowany | 5/5 | 0 | 9 | 0 | Szkic lekcji |
| ADR-B-11 | Tunele | 7/7 | 0 | 11 | 0 | Szkic lekcji |
| ADR-B-12 | Ochrona (security) | 6/6 | 0 | 9 | 0 | Szkic lekcji |
| ADR-B-13 | Dokumentacja | 8/8 | 0 | 12 | 0 | Szkic lekcji |
| **Razem** | | **103/103** | **3** | **146** | **0** | **13 szkiców** |

## Co musi być zrobione przed publikacją

1. **Kontrola jakości prawa:** dla wszystkich rekordów sprawdzić dokładne brzmienie aktu ADR 2025 w Dz.U. poz. 642 ze sprostowaniem poz. 1575, szczegółowe wyjątki oraz każdą prawidłową i błędną odpowiedź. Potwierdzenie przez rzeczywistego specjalistę ADR, z datą i identyfikatorem recenzenta.
2. **Dopracowanie materiału:** poprawić nadmiernie podobne pytania, dopisać scenariusze trudniejszych sytuacji, sprawdzić czy każda kompetencja ma **wystarczającą** liczbę pytań, a nie tylko jedno.
3. **Grafiki i dokumenty:** własne lub legalnie pozyskane wzory nalepek i tablic; materiały do rozpoznawania klas, opakowań, kodów i ograniczeń; wzorcowe opisy UN i dokumenty przewozowe.
4. **Praktyka:** zatwierdzenie 3 scenariuszy przez instruktora, rzeczywista realizacja ćwiczeń i odrębne potwierdzenie obecności i umiejętności. Quiz nie zalicza praktyki.
5. **Tryb egzaminu:** generator 30 pytań / 60 minut / próg 20 prawidłowych — wyłącznie ze zweryfikowanych rekordów, po sprawdzeniu jakości losowania, dostępności i powtórek.
6. **Odbiór końcowy:** ponowna weryfikacja każdej z 13 lekcji z aktualnymi źródłami i korektami legislacyjnymi oraz potwierdzony PASS wymaganego CI.

## Narzędzia kontroli

- `python scripts/validate.py` — format rekordów JSONL, unikalne ID, odpowiedzi A/B/C, metadane, rozkład kluczy.
- `python scripts/coverage.py` — powiązanie pytań z kompetencjami, 13 działów i obecność 13 plików lekcji, z rozdzieleniem `draft` i `verified`.
- `python -m unittest discover -s tests -v` — testy automatyczne.
- `docs/AUDYT-PARTIA-005.md` — przegląd 24 nowych pytań i ich punktów do szczegółowej kontroli.

## Status szkolenia praktycznego

Scenariusze: [SCENARIUSZE.md](../podstawowy/praktyka/SCENARIUSZE.md). Trzy wymagane obszary: gaśnica, pierwsza pomoc i działania po awarii/wypadku. Przygotowany materiał jest wyłącznie pomocą dla instruktora. Nie wystawia zaświadczenia ani nie zastępuje zorganizowanych zajęć.

## Dokumenty nadrzędne

- [Program kursu (Dz.U. 2021 poz. 2150)](https://eli.gov.pl/api/acts/DU/2021/2150/text.pdf)
- [Egzaminy ADR (Dz.U. 2024 poz. 964)](https://eli.gov.pl/api/acts/DU/2024/964/text.html)
- [ADR 2025 ogłoszone w Dz.U. poz. 642](https://dziennikustaw.gov.pl/DU/2025/642)
- [Sprostowanie Dz.U. 2025 poz. 1575](https://eli.gov.pl/eli/DU/2025/1575/ogl/pol/pdf)
