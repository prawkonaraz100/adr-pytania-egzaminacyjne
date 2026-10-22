# Audyt partii 007B — 20 pytań pogłębiających kurs podstawowy ADR

Data przeglądu redakcyjnego: **2026-10-22**. Opracowanie autorskie; **bez niezależnej akceptacji eksperta ADR**.

## Uzasadnienie

Na początku partii 20/103 kompetencji teoretycznych posiadało dokładnie jedno pytanie robocze. Zapisano 20 nowych pytań **ADR-B-0197–ADR-B-0216**, po jednym na każdy słabo pokryty cel. Cały bank zawiera **216** rekordów, z czego **216 needs_review i 0 verified**. Pokrycie robocze wynosi **103/103 celów z co najmniej dwoma pytaniami**; 7 celów ma trzy lub więcej.

**Wniosek redakcyjny:** zamknięcie luki ilościowej **nie** jest równoznaczne z osiągnięciem odpowiedniej różnorodności sytuacji ani z zatwierdzeniem prawidłowości prawnej.

## Lista zagadnień do zatwierdzenia per pytanie

| ID | Powiązany cel | Wskazany punkt ADR 2025 | Ryzyka do sprawdzenia | Status |
|---|---|---|---|---|
| ADR-B-0197 | ADR-B-08-K02 | `ADR 2025, 8.1.4.2` | Warunki 1.1.3.6, równoważny środek gaśniczy lub świadectwo określonego pojazdu | needs_review |
| ADR-B-0198 | ADR-B-08-K08 | `ADR 2025, 8.1.2.2(a); 9.1.3` | Warunki 1.1.3.6, równoważny środek gaśniczy lub świadectwo określonego pojazdu | needs_review |
| ADR-B-0199 | ADR-B-09-K01 | `ADR 2025, 7.5.2.1; 7.5.2.2` | Dopuszczalność mieszanego załadunku, mocowanie innych towarów, różnica 7.5.8.1 i 7.5.8.2 | needs_review |
| ADR-B-0200 | ADR-B-09-K06 | `ADR 2025, 7.5.7.1` | Dopuszczalność mieszanego załadunku, mocowanie innych towarów, różnica 7.5.8.1 i 7.5.8.2 | needs_review |
| ADR-B-0201 | ADR-B-09-K07 | `ADR 2025, 7.5.8.2` | Dopuszczalność mieszanego załadunku, mocowanie innych towarów, różnica 7.5.8.1 i 7.5.8.2 | needs_review |
| ADR-B-0202 | ADR-B-09-K08 | `ADR 2025, 7.5.1.2` | Dopuszczalność mieszanego załadunku, mocowanie innych towarów, różnica 7.5.8.1 i 7.5.8.2 | needs_review |
| ADR-B-0203 | ADR-B-10-K02 | `ADR 2025, 5.4.1.1.7` | Wyjątki 1.1.4.2.1 oraz certyfikat pakowania 5.4.2; źródło odpowiedzialności | needs_review |
| ADR-B-0204 | ADR-B-10-K03 | `ADR 2025, 5.4.2` | Wyjątki 1.1.4.2.1 oraz certyfikat pakowania 5.4.2; źródło odpowiedzialności | needs_review |
| ADR-B-0205 | ADR-B-10-K04 | `ADR 2025, 1.1.4.2; 1.1.4.3` | Wyjątki 1.1.4.2.1 oraz certyfikat pakowania 5.4.2; źródło odpowiedzialności | needs_review |
| ADR-B-0206 | ADR-B-10-K05 | `ADR 2025, 1.1.4.2.1` | Wyjątki 1.1.4.2.1 oraz certyfikat pakowania 5.4.2; źródło odpowiedzialności | needs_review |
| ADR-B-0207 | ADR-B-11-K01 | `ADR 2025, 1.9.5.2.2; 8.6.4` | Sposób przewozu, 3.4.13/3.4.14, kod w kolumnie 15 i lokalne znaki tunelowe | needs_review |
| ADR-B-0208 | ADR-B-11-K03 | `ADR 2025, 8.6.3.1; 8.6.4` | Sposób przewozu, 3.4.13/3.4.14, kod w kolumnie 15 i lokalne znaki tunelowe | needs_review |
| ADR-B-0209 | ADR-B-11-K06 | `ADR 2025, 8.6.3.3; 8.6.4` | Sposób przewozu, 3.4.13/3.4.14, kod w kolumnie 15 i lokalne znaki tunelowe | needs_review |
| ADR-B-0210 | ADR-B-11-K07 | `ADR 2025, 5.4.3.4; 1.9.5` | Sposób przewozu, 3.4.13/3.4.14, kod w kolumnie 15 i lokalne znaki tunelowe | needs_review |
| ADR-B-0211 | ADR-B-12-K04 | `ADR 2025, 1.10.1.2` | Warunki ochrony w 1.10.1, towary dużego ryzyka i zakres planu ochrony | needs_review |
| ADR-B-0212 | ADR-B-12-K05 | `ADR 2025, 1.10.3.2.2` | Warunki ochrony w 1.10.1, towary dużego ryzyka i zakres planu ochrony | needs_review |
| ADR-B-0213 | ADR-B-12-K06 | `ADR 2025, 1.10.3.3` | Warunki ochrony w 1.10.1, towary dużego ryzyka i zakres planu ochrony | needs_review |
| ADR-B-0214 | ADR-B-13-K03 | `ADR 2025, 5.4.1.1.1(g),(h)` | Wpis warunkowy i pełne dane 5.4.1, dostępność instrukcji w kabinie | needs_review |
| ADR-B-0215 | ADR-B-13-K06 | `ADR 2025, 5.4.1.1.7; 5.4.1.1.1` | Wpis warunkowy i pełne dane 5.4.1, dostępność instrukcji w kabinie | needs_review |
| ADR-B-0216 | ADR-B-13-K07 | `ADR 2025, 8.1.2.1(b); 8.1.2.3` | Wpis warunkowy i pełne dane 5.4.1, dostępność instrukcji w kabinie | needs_review |

## Konkretne rozróżnienia źródłowe

1. **Gaśnica przy 1.1.3.6 — 8.1.4.2:** co najmniej 2 kg proszku lub odpowiednia równoważna skuteczność innego środka, przy wymaganiach dla klas pożarów A/B/C. [ADR 2025 — źródło techniczne](https://www.dgg.bam.de/dgginfo/detailinfo/adr/ppwrmellsoja?lang=en).
2. **Wspólny załadunek — 7.5.2:** tabela zgodności nalepek i odrębne reguły klasy 1; sama szczelność opakowania nie rozstrzyga o zgodności. [ADR 2025, tom II](https://www.euraca.eu/media/frmeo2lm/adr-2025-vol-ii.pdf).
3. **Czyszczenie po rozładunku:** w 7.5.8.1 chodzi o zabrudzenie po uwolnieniu zawartości sztuki przesyłki; w 7.5.8.2 o przewóz luzem i odstępstwo przy tym samym następnym towarze. Dlatego zaktualizowano tytuł i podstawę kompetencji `ADR-B-09-K07` tak, by nie przypisywać wyjątku do niewłaściwej reguły.
4. **Certyfikat pakowania — 5.4.2:** osoby odpowiedzialne za pakowanie kontenera przekazują certyfikat przewoźnikowi morskiemu. Dokument może być w określonych warunkach połączony z dokumentem przewozowym. [ADR 2025, 5.4.2](https://www.mindop.sk/fileadmin/documents/doprava/nebezpecnetovary/cesta/ADR_2025_Vol._II._EN.pdf).
5. **Tunel kategorii E i LQ:** 8.6.3.3 oraz 8.6.4 przewidują wyjątek przy obowiązkowym oznakowaniu jednostki według 3.4.13 z zastrzeżeniem 3.4.14; nie wystarczy hasło „LQ nie podlega ADR”.
6. **Plan ochrony — 1.10.3.2:** plan dla odpowiednich towarów dużego ryzyka musi opisywać odpowiedzialności, analizę ryzyka i działania zabezpieczające; numer telefonu nie jest planem. Z kolei 1.10.3.3 reguluje środki przeciwdziałania kradzieży.
7. **Instrukcje pisemne — 8.1.2.1 i 8.1.2.3:** muszą być w kabinie i łatwo dostępne, a nie tylko formalnie znajdować się w samochodzie.

## Przegląd podobieństw językowych

Uruchomiono przegląd tokenów pytań w tych samych modułach (normalizacja polskich znaków, usunięcie wybranych słów wspólnych, miara Jaccarda, próg `0.45`). Narzędzie `scripts/similarity.py` ma charakter **informacyjny**, nie jest walidatorem poprawności lub automatycznym detektorem parafraz.

W aktualnym banku wychodzą **4 pary kandydujące do oceny redaktora**:

| Pytania | Uzasadnienie |
|---|---|
| `ADR-B-0071` / `ADR-B-0072` | Brzmienie niemal identyczne, ale **różne DMC i różne progi gaśnic** — podobieństwo może być celowym ćwiczeniem liczb |
| `ADR-B-0017` / `ADR-B-0052` | Podobna fraza o numerze zagrożenia i tablicy; **inny cel** (X vs kolor tablicy) |
| `ADR-B-0042` / `ADR-B-0096` | Ten sam format pytania o klasę, ale **różne towary** (gazy/nadtlenki) |
| `ADR-B-0153` / `ADR-B-0159` | Podobna forma pytania porównawczego, lecz **różne klasy** |

Nie usunięto ich automatycznie. Przeredagowano za to pary rzeczywiście bliskie dydaktycznie: `ADR-B-0034` i `ADR-B-0067` (identyfikacja dwóch członków załogi), `ADR-B-0036` i `ADR-B-0121` (treść szkolenia ochronnego vs reakcja na ślady naruszenia). Poprawiono też mało wiarygodne błędne odpowiedzi w 0034/0036.

**Ograniczenie:** skrypt nie rozpoznaje dobrze synonimów, parafraz ani tożsamych tez przedstawionych innym językiem. Konieczna jest niezależna ocena człowieka.

## Bramki przed publikacją

- [x] 20 nowych pytań ma A/B/C, klucz, wyjaśnienie i przepis do kontroli.
- [x] Wszystkie przypisane do odrębnych celów, 103/103 celów z co najmniej dwoma pytaniami.
- [x] Zidentyfikowano i opisano kandydatów podobieństwa oraz poprawiono cztery starsze pytania.
- [ ] Porównać każdą odpowiedź i dystraktor z **polskim tekstem ogłoszonym** (Dz.U. 2025 poz. 642) oraz sprostowaniem 1575.
- [ ] Niezależna recenzja specjalisty ADR dla wszystkich 216 pytań i 13 lekcji, z prawdziwą datą i tożsamością recenzenta.
- [ ] Ocena sytuacyjności, zagadnień błędnie uproszczonych, semantycznych powtórzeń i jakości ilustracji.
- [ ] Zatwierdzenie 3 scenariuszy praktycznych i ich rzeczywista realizacja przez uprawniony podmiot — niezależnie od quizu.
- [ ] Formalny Quality Gate **PASS** dla ostatniego commita PR.

## Źródła nadrzędne

- [ADR 2025 — Dz.U. 2025 poz. 642](https://dziennikustaw.gov.pl/DU/2025/642)
- [Sprostowanie ADR 2025 — Dz.U. 2025 poz. 1575](https://eli.gov.pl/eli/DU/2025/1575/ogl/pol/pdf)
- [Ministerstwo Infrastruktury: tomy pomocnicze PL](https://www.gov.pl/web/infrastruktura/towary-niebezpieczne)
- [UNECE: ADR 2025](https://unece.org/adr-2025-files)

**Status końcowy tego dokumentu:** przegląd autorski, nie podpisana opinia prawnomerytoryczna. `verified=0`.
