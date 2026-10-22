# Partia 006 — przegląd źródeł i jakości 30 pytań

**Data:** 22 października 2026. **Charakter:** dokumentacja redakcyjna nowej partii, a nie poświadczenie prawne lub eksperckie.

## Dlaczego powstała partia

Przed rozpoczęciem 70 z 103 roboczych celów teoretycznych było reprezentowanych przez **jedno pytanie**. Samo odtwarzanie klasy/numeru z pamięci nie sprawdza rozumienia postępowania przez kierowcę. Dodano 30 pytań sytuacyjnych `ADR-B-0147`–`ADR-B-0176`, przypisanych po jednym do 30 celów.

Po zmianach:
- bank: **176 pytań, 176 `needs_review`, 0 `verified`**;
- pokrycie tematyczne: 103/103 celów teoretycznych mają pytanie;
- głębokość: **40 z 103** nadal mają mniej niż 2 pytania; wcześniej 70;
- aktualny rozkład A/B/C należy odczytać z JSONL; nie utożsamiać go z poprawnością merytoryczną.

## Audyt do zatwierdzenia per rekord

| ID | Kompetencja | Podstawa do kontroli | Ryzyko/wyjątki do sprawdzenia | Status |
|---|---|---|---|---|
| ADR-B-0147 | ADR-B-01-K01 | `ADR 2025, 1.2.1, definicja transport unit` | Weryfikacja całego ustępu, wyjątków i odpowiedzi błędnych | needs_review |
| ADR-B-0148 | ADR-B-01-K03 | `ADR 2025, 8.2.1; prawo krajowe o uprawnieniach do kierowania` | Warunki stosowania, wyjątki ilościowe i zakres wyposażenia/uprawnień | needs_review |
| ADR-B-0149 | ADR-B-01-K05 | `ADR 2025, 3.2 tabela A kol. (7a); 3.4.1` | Warunki stosowania, wyjątki ilościowe i zakres wyposażenia/uprawnień | needs_review |
| ADR-B-0150 | ADR-B-02-K01 | `ADR 2025, 2.2.1.1.5` | Zakres danej klasy, zagrożenia dodatkowe, rozróżnienie nalepek | needs_review |
| ADR-B-0151 | ADR-B-02-K02 | `ADR 2025, 5.2.2.2.2, wzór nr 2.3; 2.2.2` | Zakres danej klasy, zagrożenia dodatkowe, rozróżnienie nalepek | needs_review |
| ADR-B-0152 | ADR-B-02-K03 | `ADR 2025, 2.2.3; 8.3.5` | Zakres danej klasy, zagrożenia dodatkowe, rozróżnienie nalepek | needs_review |
| ADR-B-0153 | ADR-B-02-K04 | `ADR 2025, 2.2.41.1.1; 2.2.43.1.1` | Zakres danej klasy, zagrożenia dodatkowe, rozróżnienie nalepek | needs_review |
| ADR-B-0154 | ADR-B-02-K05 | `ADR 2025, 2.2.42.1.1` | Zakres danej klasy, zagrożenia dodatkowe, rozróżnienie nalepek | needs_review |
| ADR-B-0155 | ADR-B-02-K06 | `ADR 2025, 2.2.43.1.1; 5.4.3.4` | Warunki stosowania, wyjątki ilościowe i zakres wyposażenia/uprawnień | needs_review |
| ADR-B-0156 | ADR-B-02-K07 | `ADR 2025, 2.2.51.1.1` | Zakres danej klasy, zagrożenia dodatkowe, rozróżnienie nalepek | needs_review |
| ADR-B-0157 | ADR-B-02-K08 | `ADR 2025, 2.2.51; 2.2.52` | Zakres danej klasy, zagrożenia dodatkowe, rozróżnienie nalepek | needs_review |
| ADR-B-0158 | ADR-B-02-K09 | `ADR 2025, 5.2.2.2.2 wzór nr 6.1; 2.2.61.1.1` | Zakres danej klasy, zagrożenia dodatkowe, rozróżnienie nalepek | needs_review |
| ADR-B-0159 | ADR-B-02-K10 | `ADR 2025, 2.2.62.1.1; 2.2.61.1.1` | Zakres danej klasy, zagrożenia dodatkowe, rozróżnienie nalepek | needs_review |
| ADR-B-0160 | ADR-B-02-K11 | `ADR 2025, 8.2.1.4; 8.2.1.5` | Warunki stosowania, wyjątki ilościowe i zakres wyposażenia/uprawnień | needs_review |
| ADR-B-0161 | ADR-B-02-K12 | `ADR 2025, 2.2.8.1.1; 5.2.2.2.2 wzór nr 8` | Zakres danej klasy, zagrożenia dodatkowe, rozróżnienie nalepek | needs_review |
| ADR-B-0162 | ADR-B-02-K13 | `ADR 2025, 5.2.2.2.2 wzór nr 9A; 3.2 tabela A` | Zakres danej klasy, zagrożenia dodatkowe, rozróżnienie nalepek | needs_review |
| ADR-B-0163 | ADR-B-03-K04 | `ADR 2025, 5.4.3.4` | Warunki stosowania, wyjątki ilościowe i zakres wyposażenia/uprawnień | needs_review |
| ADR-B-0164 | ADR-B-04-K04 | `ADR 2025, 5.4.3.4` | Warunki stosowania, wyjątki ilościowe i zakres wyposażenia/uprawnień | needs_review |
| ADR-B-0165 | ADR-B-05-K03 | `ADR 2025, 5.4.3.4` | Warunki stosowania, wyjątki ilościowe i zakres wyposażenia/uprawnień | needs_review |
| ADR-B-0166 | ADR-B-05-K05 | `ADR 2025, 5.4.3.4` | Warunki stosowania, wyjątki ilościowe i zakres wyposażenia/uprawnień | needs_review |
| ADR-B-0167 | ADR-B-05-K08 | `ADR 2025, 5.4.3.4` | Warunki stosowania, wyjątki ilościowe i zakres wyposażenia/uprawnień | needs_review |
| ADR-B-0168 | ADR-B-05-K10 | `ADR 2025, 5.4.3.4; 8.1.5.2` | Warunki stosowania, wyjątki ilościowe i zakres wyposażenia/uprawnień | needs_review |
| ADR-B-0169 | ADR-B-05-K12 | `ADR 2025, 8.1.4.5` | Warunki stosowania, wyjątki ilościowe i zakres wyposażenia/uprawnień | needs_review |
| ADR-B-0170 | ADR-B-06-K04 | `ADR 2025, 5.3.2.3.1` | Odczyt i interpretacja dokładnego oznaczenia | needs_review |
| ADR-B-0171 | ADR-B-08-K07 | `ADR 2025, 8.1.5.3` | Warunki stosowania, wyjątki ilościowe i zakres wyposażenia/uprawnień | needs_review |
| ADR-B-0172 | ADR-B-09-K04 | `ADR 2025, 7.5.1.5` | Dopuszczenie sposobu przewozu i szczególne wymagania | needs_review |
| ADR-B-0173 | ADR-B-09-K09 | `ADR 2025, 7.3.1.1; 3.2 tabela A kol. (10),(17)` | Dopuszczenie sposobu przewozu i szczególne wymagania | needs_review |
| ADR-B-0174 | ADR-B-11-K05 | `ADR 2025, 8.6.3.1` | Odczyt i interpretacja dokładnego oznaczenia | needs_review |
| ADR-B-0175 | ADR-B-13-K05 | `ADR 2025, 1.10.1.4; 8.1.2.1 (d)` | Weryfikacja całego ustępu, wyjątków i odpowiedzi błędnych | needs_review |
| ADR-B-0176 | ADR-B-08-K03 | `ADR 2025, 8.1.4.4` | Warunki stosowania, wyjątki ilościowe i zakres wyposażenia/uprawnień | needs_review |

## Źródła

- **Tekst ogłoszony, nadrzędny w Polsce:** [Dz.U. 2025 poz. 642](https://dziennikustaw.gov.pl/DU/2025/642) i [sprostowanie Dz.U. poz. 1575](https://eli.gov.pl/eli/DU/2025/1575/ogl/pol/pdf).
- [UNECE — wydanie ADR 2025](https://unece.org/adr-2025-files), szczególnie tom I (części 1–3) oraz tom II (części 4–9).
- [Ministerstwo Infrastruktury — ADR 2025, polskie tomy pomocnicze](https://www.gov.pl/web/infrastruktura/towary-niebezpieczne); **pliki pomocnicze nie są źródłem prawa**.
- [UNECE — oficjalny model czterostronicowych instrukcji pisemnych](https://unece.org/transport/road-transport/linguistic-versions-adr-instructions-writing).
- Przepisy programowe: [Dz.U. 2021 poz. 2150](https://eli.gov.pl/api/acts/DU/2021/2150/text.pdf).

## Co rzeczywiście sprawdzono

- Zestawiono tematy z punktami ADR 2025, zidentyfikowano wyjątki w szczególnie wrażliwych fragmentach (m.in. 1.1.3.6; 5.4.3.4; 8.1.4; 8.1.5).
- Przed zapisaniem każdemu rekordowi nadano identyfikator, jedną poprawną odpowiedź, dwa warianty błędne, krótkie wyjaśnienie i numer przepisu.
- Pytania o klasy zagrożeń i zdarzenia nie mogą być traktowane jako dowód spełnienia wymagań dotyczących szkolenia specjalistycznego klasy 1 lub 7, ani wykonania praktyki.
- **Nie przeprowadzono jeszcze ostatecznego porównania każdego wariantu odpowiedzi z pełnym urzędowym polskim tekstem oraz recenzji niezależnego specjalisty ADR.** Dlatego wszystkie 30 rekordów mają `needs_review`.

## Wymagane kontrole przed dopuszczeniem

- [ ] Każde pytanie i **wszystkie trzy warianty** porównać z dokładnym brzmieniem ustępu ADR 2025 i sprostowaniem.
- [ ] Upewnić się, że dwie błędne odpowiedzi są naprawdę nieprawidłowe w określonych warunkach, a nie tylko mało prawdopodobne.
- [ ] Szczególnie skontrolować klasę 1, 7, litery X, zakres LQ/EQ i zaświadczeń kierowców, wyposażenie 8.1.5 oraz postępowanie przy niebezpiecznej substancji.
- [ ] Zatwierdzić pytania osobno z rzeczywistą datą i recenzentem (bez fikcyjnych podpisów).
- [ ] Niezatwierdzone pozostawić `needs_review`, sporne `blocked`.
- [ ] Potwierdzić pełny Quality Gate dla finalnego commita PR.

**Uwaga:** liczba 30 nowych pytań nie zastępuje żadnej części obowiązkowego kursu ani ćwiczeń praktycznych.
