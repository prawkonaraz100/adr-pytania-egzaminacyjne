# Pokrycie pełnego programu ADR podstawowego — audyt kompetencji

**Data:** 22 października 2026. Status: **mapa robocza**, bez niezależnej akceptacji instruktora ADR.  
**Podstawa prawna programu:** Dz.U. 2021 poz. 2150, załącznik nr 1, część 1 (13 zagadnień a–m, 18 godzin lekcyjnych) i część 3 (zajęcia praktyczne).  
**Sposób liczenia:** `python scripts/coverage.py`; źródło maszynowe `podstawowy/kompetencje.json`. Kompetencje rozbite wewnętrznie na bardziej szczegółowe podtematy, **nie jest to urzędowa lista 106 kompetencji**.

## Aktualne liczby i ich znaczenie

- **122 autorskie pytania** z A/B/C i wyjaśnieniem; 122 `needs_review`, **0 `verified`**.
- **106 roboczych kompetencji**: **103 teoretyczne** i **3 praktyczne**.
- **84/103 kompetencji teoretycznych** ma przynajmniej jedno przygotowane pytanie. To wyłącznie pokrycie redakcyjne, nie prawne.
- **19/103** nie ma jeszcze żadnego pytania i wymaga opracowania.
- **3 praktyczne cele** (gaśnica, pierwsza pomoc, scenariusz wypadku/awarii) nie mogą być zaliczone automatycznie przez test.
- Wszystkie 122 pytania są powiązane z mapą; brak nieprzypisanych rekordów.
- Rozkład poprawnych wariantów w całym banku: **A=40 / B=41 / C=41**. Testy jedynie sygnalizują poważne odchylenia; równy rozkład nie dowodzi jakości pytań.

## Pokrycie według działów

| Moduł | Temat | Teoria: pokryte / wszystkie | Praktyka | Liczba pytań | Zatwierdzone |
|---|---|---:|---:|---:|---:|
| ADR-B-01 | Prawo, definicje, wyłączenia | 5/7 | 0 | 8 | 0 |
| ADR-B-02 | Klasyfikacja i zagrożenia | 12/14 | 0 | 12 | 0 |
| ADR-B-03 | Środowisko i odpady | 5/6 | 0 | 7 | 0 |
| ADR-B-04 | Zapobieganie | 4/6 | 0 | 7 | 0 |
| ADR-B-05 | Wypadek i pierwsza pomoc | 12/12 | 3 | 15 | 0 |
| ADR-B-06 | Oznakowanie | 8/9 | 0 | 8 | 0 |
| ADR-B-07 | Obowiązki | 4/6 | 0 | 8 | 0 |
| ADR-B-08 | Wyposażenie | 7/8 | 0 | 12 | 0 |
| ADR-B-09 | Załadunek i mocowanie | 7/9 | 0 | 11 | 0 |
| ADR-B-10 | Transport kombinowany | 2/5 | 0 | 6 | 0 |
| ADR-B-11 | Tunele | 6/7 | 0 | 10 | 0 |
| ADR-B-12 | Ochrona | 5/6 | 0 | 8 | 0 |
| ADR-B-13 | Dokumentacja | 7/8 | 0 | 10 | 0 |
| **Razem** | | **84/103** | **3** | **122** | **0** |

## Dlaczego nie uznajemy samej liczby 400 za „kompletność”?

400 pytań to wyłącznie roboczy limit banku. Można napisać 400 pytań z gaśnic i tuneli, a nie nauczyć kierowcy ochrony środowiska, procedur awaryjnych ani dokumentacji. Miarą jakości są:

1. Pokrycie **każdego wymaganego działu i podtematu**.
2. Obecność czytelnej lekcji z przykładem zastosowania.
3. Prawdziwość **wszystkich trzech odpowiedzi** i sprawdzone warunki/wyjątki przepisu.
4. Rzeczywista recenzja eksperta ADR, data kontroli, wersja prawa i możliwość wycofania błędnego pytania.
5. Praktyczne ćwiczenia z udziałem instruktora i ich odrębna ewidencja.
6. Symulator 30 pytań / 60 minut / próg 20, ale **wyłącznie z zatwierdzonego banku**. Rozkład podtematów w symulatorze to wewnętrzny projekt, nie ujawniony rozkład państwowych losowań.

## Najważniejsze luki wykryte w tej wersji matrycy

- **ADR-B-01:** definicje, struktura aktu, decyzja o dopuszczalności towaru.
- **ADR-B-02:** zagrożenia klasy 1 oraz grupy pakowania/zagrożenia dodatkowe/tabela A.
- **ADR-B-03:** klasyfikowanie odpadów niebezpiecznych i warunki szczególne.
- **ADR-B-04:** bezpieczeństwo postoju i inne środki zapobiegawcze.
- **ADR-B-06:** nalepki dużego formatu na pojazdach/kontenerach i dokładne warunki oznakowania.
- **ADR-B-07:** obowiązki pakującego/napełniającego/rozładowcy i kierowcy jako członka załogi.
- **ADR-B-08:** rozróżnienie konstrukcji pojazdu i wymagań dla poszczególnych rodzajów przewozu.
- **ADR-B-09:** kontrole przed załadunkiem, podstawy przewozu luzem.
- **ADR-B-10:** certyfikat pakowania kontenera, ADR/RID/IMDG, wyjątki dla gałęzi transportu.
- **ADR-B-11:** szczególne zachowanie w tunelu przy pożarze.
- **ADR-B-12:** nadzór nad postojem i zabezpieczenie przed kradzieżą pojazdu.
- **ADR-B-13:** dodatkowe dokumenty zależne od towaru i rodzaju przewozu.

## Stan materiałów do nauki

- [Lekcja ADR-B-01: przepisy i wyłączenia](../podstawowy/lekcje/ADR-B-01.md) — wersja robocza.
- [Lekcja ADR-B-05: wypadek i pierwsza pomoc](../podstawowy/lekcje/ADR-B-05.md) — wersja robocza, z obowiązkową częścią praktyczną.
- [Lekcja ADR-B-12: ochrona](../podstawowy/lekcje/ADR-B-12.md) — wersja robocza.
- Pozostałe **10 działów**: brak gotowych lekcji; wymagają opracowania i recenzji.

## Co jeszcze trzeba wdrożyć jako profesjonalny produkt

**Treść:** 13 pełnych lekcji, ćwiczenia i scenariusze; definicje z przykładami; tablice klas/numerów UN i samodzielnie wykonane lub legalnie pozyskane grafiki nalepek/tablic; przykładowy dokument przewozowy; fiszki i pytania sytuacyjne.

**Silnik nauki:** tryb tematyczny, powtórki błędnych odpowiedzi, tłumaczenia prostym językiem, próbny egzamin 30/60, raport z działów, dostępność na telefonie, brak ujawniania odpowiedzi przed zakończeniem próby.

**QA:** weryfikacja każdej tezy wraz z ustępem, szczególna kontrola wyłączeń/ilości/tuneli/klas, monitoring zmian przepisów i recenzja osoby fachowej. Rozdzielenie `reviewed_by_author` od `verified` w praktyce operacyjnej.

**Prowadzenie kursu:** rzeczywisty kurs ADR i jego część praktyczna są prowadzone na zasadach przepisów krajowych. Sama platforma z testami jest **materiałem przygotowawczym**, nie może poświadczać udziału w ćwiczeniach ani wydawać państwowego zaświadczenia ADR.

## Kryterium zakończenia tego etapu

Dopuszczamy do testów produkcyjnych tylko pytania, których klucz i wszystkie trzy możliwości zostały sprawdzone na aktualnym tekście przepisów i zaakceptowane przez niezależnego recenzenta. Dla lekcji wymagany jest dodatkowy odbiór merytoryczny. Bramki techniczne i prawne są odrębne.

## Źródła oficjalne

- [Dz.U. 2021 poz. 2150 — załącznik nr 1](https://eli.gov.pl/api/acts/DU/2021/2150/text.pdf)
- [Dz.U. 2024 poz. 964 — egzamin](https://eli.gov.pl/api/acts/DU/2024/964/text.html)
- [Dz.U. 2025 poz. 642 — ADR](https://dziennikustaw.gov.pl/DU/2025/642)
- [Sprostowanie do ADR 2025, Dz.U. 2025 poz. 1575](https://eli.gov.pl/eli/DU/2025/1575/ogl/pol/pdf)
