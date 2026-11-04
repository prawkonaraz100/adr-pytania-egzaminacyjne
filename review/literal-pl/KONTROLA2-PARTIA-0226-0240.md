# Kontrola druga – partia ADR-B-0226–0240 (porównanie dosłowne z polskim tekstem ADR 2025)

Data: 2026-11-04, ok. 10:30 (czas polski, CET).
Przedmiot: PR #859 (scalony 10:08 CET, main **19e9d39**, CI Quality Gate zielone 10:08:56 CET). Raport ChatGPT `review/literal-pl/PARTIA-0226-0240.md/.json`, wynik ChatGPT 0 OK / 15 POPRAW / 0 BLOKUJ; ChatGPT **dostarczył 15 linii** `POPRAWKI-0226-0240.jsonl` + `tests/test_literal_proposals_0226_0240.py`. Bank bez zmian (blob f5a227e9…).
Źródło: Dz.U. 2025 poz. 642 (skany PDF), OCR tesseract `-l pol`; strony wg nagłówka „Dziennik Ustaw — NNNN —”. [obraz] = sprawdzone na obrazie strony PDF: `kontrola2/b16-p20-977-27.png` (tabela dodatkowych wskazówek, s. 977 – nalepka 6.1 „Użyć maski ucieczkowej.”); tabela s. 976 (2.3 – „Użyć maski ucieczkowej”) i tabela 8.1.4.1 (s. 1324) – obrazy z partii 15. Sprostowanie poz. 1575 nie dotyczy punktów tej partii.
Status: kontrola robocza. **Żadne pytanie nie jest oznaczone jako zweryfikowane**; wszystkie pozostają `needs_review`.

## Podsumowanie

- **Klucze wszystkich 15 pytań w banku są poprawne.** Żadna litera klucza się nie zmienia. Błędów klucza: 0.
- Werdykty (pytania w banku): **OK 0**, **POPRAW 15**, **BLOKUJ 0** – zgodnie z ChatGPT.
- **Duplikaty w banku – 14 z 15** (zgodnie z ChatGPT): 0226 = 0508/0577; 0227 = 0578; 0228 = 0590; 0229 = 0109/0185/0630/0362; 0230 = 0110/0167; 0232 = 0585; 0233 = 0579; 0234 = 0586/0088; 0235 = 0026/0703; 0236 = 0079/0518/0628; 0237 = 0059; 0238 = 0080; 0239 = 0138/0560; 0240 = **0677/0733** (luzem, inny towar → czyścić). **0231 nie jest duplikatem** (ChatGPT: 0112/0168/0693/0747 – to inne pytania), ale ma wady formy (A 89 zn., klucz z „tylko”).
- **Propozycje ChatGPT – 7 z 15 to znowu duplikaty** (ChatGPT ich nie wykrył): **0228** (pojazd zastępczy, dokument w starej kabinie) = **0780** (pojazd zastępczy, instrukcje w starej kabinie) i 0216 (8.1.2.1(a)); **0229** (podać znane dane, zaznaczyć nieznane) = **0165/0696**; **0230** (skażone rękawice) = **0745** (+0707); **0231** (światła awaryjne nie zastępują znaków) = **0747**; **0234** (brak 4. strony instrukcji) = 0039/0088/0586 (ta sama reguła „pełny czterostronicowy wzór”); **0239** (rozładunek, 7.5.1.3) = **0476** (7.5.1.3) i 0135; **0240** (przejazd do miejsca czyszczenia) = **0706**. Ponadto **0232** (gaśnica stała 8.1.4.3) – temat nowy, ale spoza kompetencji ADR-B-05-K12 (8.1.4.5; K12 spadłaby do 5 pytań).
- Propozycje przyjęte: bez zmian 0236, 0238 oraz 0233 (cała linia); z poprawką 0226 (B → nazwa handlowa, explanation z przykładem I.N.O.), 0227 (A bez „wszystkie”), 0235 (wiarygodne dystraktory), 0237 (A i C – długości/mylenie z piętrzeniem). **Nowe pytania z kontroli drugiej: 0228, 0229, 0230, 0232, 0234, 0239, 0240; 0231 – ten sam temat banku, nowa forma.** Wszystkie: ten sam ID, `module_id`, litera klucza i kompetencja w `kompetencje.json` (liczebność kompetencji bez zmian, wszystkie ≥6).
- **Cytaty ChatGPT istnieją dosłownie** (15/15); drobne: 0227 – cytat to UWAGA do (e), bez słowa „UWAGA:”; 0235 – zdanie przechodzi ze s. 1308 na 1309 (ChatGPT podał 1308–1309 – dobrze).
- **Strony – 15 z 15 dobrych:** 5.4.1.1.1(b) – **961**; 5.4.1.1.1(e) UWAGA – **962**; 8.1.2.1(a) – **1324**; 5.4.3.4 (powiadomić służby / zdjąć ubranie) – **975**; 8.1.5.2 – **1325**; 8.1.4.3 – **1325**; 5.4.1.1.1(g),(h) – **962**; 5.4.3.4 (czterostronicowy wzór) – **974**; 7.5.7.1 EN 12195-1 – **1308–1309**; 7.5.7.1 napinanie – **1308**; 7.5.7.3 – **1309**; 7.5.8.1 – **1309**; 7.5.1.3 – **1304**; 7.5.8.1 (środki ostrożności) – **1310**. Strony punktów dodanych w kontroli drugiej: 3.1.2.8.1, 3.1.2.8.1.1 – **305**; 1.1.3.6.2 – **26**; 5.4.1.1.1(f) – **962**; tabela wskazówek 6.1 – **977** [obraz], 2.3 – **976**; wykaz wyposażenia (4. strona wzoru) – **978**; 8.1.5.3 – **1325**; 8.1.4.4, 8.1.4.5 – **1325**; 7.5.1.2 – **1304**; 8.1.2.2(b) – **1324**; 7.5.8.2 – **1310**.
- Wskaźnik „poprawna = jedyna najdłuższa”: **70/780 = 8,97% → 69/780 = 8,85%** (ADR-B-13 5→4, tj. 9,26% → 7,41%; maks. działu 15,22% ADR-B-11 bez zmian). **Liczbę trzeba zmienić** w `docs/POKRYCIE-KURSU.md` (l. 11), `podstawowy/README.md` (l. 3) i `review/specialist/PAKIET-ZAMKNIECIE-0780.md` (l. 9).
- Wskaźnik „poprawna = jedyna najkrótsza” (limit 38%): globalnie 242 → 236; ADR-B-05 27,6% → 26,4%, ADR-B-09 33,9% → 29,0%, ADR-B-13 33,3% → 29,6% – zielone.
- Heurystyka explanation (check_mock_exam_variants.py, „brak prostego sygnału wyjaśniającego”): ostrzeżenia 104 → 102 (zniknęły 0232, 0236; nowe linie bez ostrzeżeń).
- Licznik: 528 → **513/780** po partii 16 – poprawny.
- Plik poprawek: `kontrola2/POPRAWKI-KONTROLA2-0226-0240.jsonl` – **15 pełnych linii**; kolejność pól, `module_id` i klucze bez zmian, `needs_review`, `checked_at/reviewer=null`. Generator: `kontrola2/build_p16.py` (te same kontrole co w p15: klucz nie jest jedyną najdłuższą/najkrótszą, opcje ≤80 zn., brak słów absolutnych i średników w opcjach, explanation 2–5 zdań, ≥300 zn., ≤35 słów w zdaniu, końcówka „Podstawa: ADR …”).
- Test na kopii repo (/tmp/b16 = main 19e9d39, bez commitów i pushu; `kontrola2/test_p16.sh` + `kontrola2/sync_p16_test.py`): `apply_poprawki.py` z `POPRAWKI-KONTROLA2-0226-0240.jsonl` → **Changed (15): ADR-B-0226 … ADR-B-0240**; nowy SHA blobu banku **98a390814b7f4a9f5bbdbf8b087b8a318d3635a4** (było f5a227e9cb534d76207435cd463dd9a49158cbb8). Synchronizacja: warianty/klucze egzaminów – 0237 (001), 0231 (002), 0234 (005); snapshoty `review/sequential/` i `review/legal-clauses/` 219-228, 229-234, 235-240 (15 ID; nowe przepisy, ocena A/B/C, notes ≥25 zn.); ledger `stage4w4-literal-verification-ledger-0001-0609.json` – 11 ID (0226, 0228, 0229, 0230, 0232, 0233, 0234, 0237, 0238, 0239, 0240); SHA w dokumentach jak w #858; wskaźnik 69/780. **Po synchronizacji wszystko zielone:** validate, coverage, check_mock_exam_variants, answer_leakage_metrics, answer_length_bias --threshold 0.16 --strict, check_explanation_quality --minimum 300, check_near_duplicates 0.60, check_cross_module_duplicates 0.80, similarity 0.45 (brak par z 0226–0240), check_explanation_heuristics, release_gate --report, check_sequential_audit, check_legal_clause_review, course_consistency; **unittest 157/157 OK** (w tym test_literal_proposals_0226_0240).
- Scenariusze: SC-ADR-B-05-02 i SC-ADR-B-06-02 poprawiono już w **#858** (9ce3d3c: „Wyciek przy rozładunku: kto wzywa służby”, „Specjalny kod zagrożenia 44”); #859 nie zmienia scenariuszy.

## Tabela werdyktów

| ID | Dział / kompetencja | Klucz | ChatGPT | Kontrola 2 | Punkt / s. Dz.U. | Uwagi |
|---|---|---|---|---|---|---|
| 0226 | 13 / K01 | A ✔ | POPRAW | POPRAW (linia CG z poprawką) | 5.4.1.1.1(b) / 961; 3.1.2.8.1(.1) / 305 | bank = 0508, 0577 |
| 0227 | 13 / K02 | C ✔ | POPRAW | POPRAW (linia CG, A bez „wszystkie”) | 5.4.1.1.1(e) UWAGA / 962 | bank = 0578 |
| 0228 | 13 / K07 | C ✔ | POPRAW | POPRAW (nowe pytanie) | 1.1.3.6.2 / 26; 8.1.2.1(a) / 1324 | bank = 0590; propozycja CG = 0780, 0216 |
| 0229 | 05 / K07 | A ✔ | POPRAW | POPRAW (nowe pytanie) | 5.4.3.4 / 975; 5.4.1.1.1(f) / 962 | bank = 0109, 0185, 0630, 0362; CG = 0165, 0696 |
| 0230 | 05 / K08 | B ✔ | POPRAW | POPRAW (nowe pytanie) | 5.4.3.4 / 975, 977 [obraz], 978; 8.1.5.3 / 1325 | bank = 0110, 0167; CG = 0745, 0707 |
| 0231 | 05 / K10 | C ✔ | POPRAW | POPRAW (ten sam temat, nowa forma) | 5.4.3.4 / 975; 8.1.5.2 / 1325 | nie duplikat; A 89 zn., „tylko” w kluczu; CG = 0747 |
| 0232 | 05 / K12 | A ✔ | POPRAW | POPRAW (nowe pytanie) | 8.1.4.5, 8.1.4.4 / 1325 | bank = 0585; CG (8.1.4.3) poza K12 |
| 0233 | 13 / K03 | B ✔ | POPRAW | POPRAW (linia CG bez zmian) | 5.4.1.1.1(g),(h) / 962 | bank = 0579 (opcje 90–103 zn.) |
| 0234 | 13 / K04 | C ✔ | POPRAW | POPRAW (nowe pytanie) | 5.4.3.4 / 974–978 | bank = 0586, 0088; CG = 0039/0088/0586 |
| 0235 | 09 / K02 | A ✔ | POPRAW | POPRAW (linia CG z poprawką) | 7.5.7.1 / 1308–1309 | bank = 0026, 0703 (C 98 zn., B 35 zn.) |
| 0236 | 09 / K06 | B ✔ | POPRAW | POPRAW (linia CG bez zmian) | 7.5.7.1 / 1308 | bank = 0079, 0518, 0628 |
| 0237 | 09 / K05 | C ✔ | POPRAW | POPRAW (linia CG z poprawką) | 7.5.7.3 / 1309 | bank = 0059 (B 91 zn., A nie odpowiada na „czy”) |
| 0238 | 09 / K07 | A ✔ | POPRAW | POPRAW (linia CG bez zmian) | 7.5.8.1 / 1309; 7.5.8.2 / 1310 | bank = 0080 (B 93 zn.) |
| 0239 | 09 / K08 | B ✔ | POPRAW | POPRAW (nowe pytanie) | 7.5.1.2 / 1304; 8.1.2.2(b) / 1324 | bank = 0138, 0560; CG = 0476, 0135 |
| 0240 | 09 / K07 | C ✔ | POPRAW | POPRAW (nowe pytanie) | 7.5.8.1 / 1309–1310 | bank = 0677, 0733; CG = 0706 |

---

## ADR-B-0226 – POPRAW (linia ChatGPT z poprawką)
- 5.4.1.1.1(b) (s. 961): „prawidłową nazwę przewozową, uzupełnioną, jeżeli jest to wymagane (patrz 3.1.2.8.1), nazwą techniczną podaną w nawiasach (patrz 3.1.2.8.1.1), ustaloną zgodnie z 3.1.2;” ✔. 3.1.2.8.1 (s. 305): nazwy ogólne i „I.N.O.” z przepisem szczególnym 274 lub 318 uzupełnia się nazwą techniczną w nawiasach, przykład „UN 1993 MATERIAŁ ZAPALNY CIEKŁY I.N.O. (ZAWIERA KSYLEN I BENZEN), 3, II”. 3.1.2.8.1.1: „Nie powinny być używane do tego celu nazwy handlowe.”
- Temat CG nowy w banku (brak pytań o nazwę techniczną). Poprawki: stem z konkretną pozycją I.N.O./PS 274; B → nazwa handlowa w nawiasie (wiarygodny błąd oparty na 3.1.2.8.1.1); explanation tłumaczy „I.N.O.” prostym językiem (bez kropek dzielących zdania). Sources „5.4.1.1.1(b); 3.1.2.8.1; 3.1.2.8.1.1”.

## ADR-B-0227 – POPRAW (linia ChatGPT, drobna poprawka)
- UWAGA do 5.4.1.1.1(e) (s. 962): „W przypadku opakowań kombinowanych nie wymaga się podawania liczby opakowań wewnętrznych zawartych w opakowaniu zewnętrznym, a także rodzaju opakowań wewnętrznych i ich pojemności.” ✔.
- Temat nowy (0261/0462 dotyczą LQ i środowiska). A „Wpisać wszystkie dwadzieścia cztery…” – słowo absolutne → „Wpisać dwadzieścia cztery butelki jako osobne sztuki przesyłek” (62).

## ADR-B-0228 – POPRAW (nowe pytanie)
- Propozycja CG (pojazd zastępczy, dokument został w starej kabinie) = **0780** (pojazd zastępczy, instrukcje w starej kabinie) i 0216 (8.1.2.1(a), wszystkie dokumenty w kabinie) – duplikat.
- Nowe: przewóz w limicie 1.1.3.6, kierowca zostawił dokument w biurze. 1.1.3.6.2 (s. 26) wyłącza m.in. rozdział 5.4.3 i część 8 „z wyjątkiem: 8.1.2.1 (a), 8.1.4.2 do 8.1.4.5, …”. C „Nie, dokument przewozowy musi być w kabinie także przy takim przewozie” (70); A „…w ogóle nie stosuje się przepisów części 8” (75); B „…zamiast dokumentu instrukcje pisemne” (61). Sources „1.1.3.6.2; 8.1.2.1(a)”. Kompetencja ADR-B-13-K07 (dokumenty w kabinie). Bank nie miał pytania o 8.1.2.1(a) przy 1.1.3.6.

## ADR-B-0229 – POPRAW (nowe pytanie)
- Cytat CG 5.4.3.4 (s. 975) „Powiadomić właściwe służby ratownicze, podając im możliwie wszystkie dostępne informacje…” ✔; propozycja = 0165 (jakie informacje podać służbom) i 0696 (podać znane dane, wskazać dokument) – duplikat; stem sztuczny („nie potrafi bezpiecznie odczytać danych drugiego”).
- Nowe: ratownik pyta o ilość litrów – A „W dokumencie przewozowym, w którym podano całkowitą ilość tego towaru” (69); B instrukcje pisemne (73); C nalepki (66). 5.4.1.1.1(f) (s. 962): „całkowitą ilość każdego z towarów niebezpiecznych mającego odrębny numer UN… (odpowiednio jako objętość, masę brutto lub masę netto)”; 5.4.3.4 – „Zapewnić przybyłym ratownikom łatwy dostęp do dokumentów przewozowych”. Sources „5.4.3.4; 5.4.1.1.1(f)”.

## ADR-B-0230 – POPRAW (nowe pytanie)
- Cytat CG 5.4.3.4 (s. 975) „Zdjąć zanieczyszczone ubranie i użyte zanieczyszczone wyposażenie ochronne oraz usunąć je w sposób bezpieczny.” ✔; propozycja (skażone rękawice) = **0745** (użyte skażone rękawice – nie używać, usunąć) i 0707 – duplikat.
- Nowe: opary z beczki z nalepką 6.1 – B „Użyć masek ucieczkowych i oddalić się od beczki na stronę nawietrzną” (68); A uszczelniać w masce (70); C maski dla ratowników (59). Tabela s. 977 [obraz]: 6.1 – „Użyć maski ucieczkowej.”; s. 976 – 2.3 to samo; s. 978 – maska ucieczkowa dla każdego członka załogi; 8.1.5.3 (s. 1325). Explanation kończy zdaniem o zdjęciu skażonego wyposażenia (kompetencja ADR-B-05-K08). Pokrewne 0171/0178 (wymóg maski, opary nieznanej substancji) – inny zakres.

## ADR-B-0231 – POPRAW (ten sam temat, nowa forma)
- Temat banku (ostrzeganie innych tylko bez narażenia się na opary) **nie jest duplikatem**; wady: A 89 zn., klucz C z „tylko”. Propozycja CG (światła awaryjne nie zastępują stojących znaków) = **0747** (dwa stojące znaki dla jednostki).
- Nowe opcje: C „Nie wchodzić w opary i ustawić znaki w miejscu, do którego dojdzie bezpiecznie” (78); A przejść przez opary na wstrzymanym oddechu (79); B nie ustawiać znaków (72). 5.4.3.4 (s. 975): „jeżeli jest to możliwe i bezpieczne”, „Założyć kamizelkę ostrzegawczą i odpowiednio umieścić stojące znaki ostrzegawcze”, „unikać wdychania oparów… poprzez pozostawanie po stronie nawietrznej”. Sources bez zmian „5.4.3.4; 8.1.5.2”. Pokrewne 0697 (ostrzec ludzi bez przechodzenia przez rozlew) – inna czynność.

## ADR-B-0232 – POPRAW (nowe pytanie)
- Cytat CG 8.1.4.3 (s. 1325) ✔, temat nowy, ale kompetencja ADR-B-05-K12 = 8.1.4.5 (mocowanie/dostępność); przeniesienie obniżyłoby K12 do 5 pytań. Temat 8.1.4.3 (gaśnica stała) zostaje jako luka do ewentualnego późniejszego wykorzystania.
- Nowe: 8.1.4.5 zd. 3 (s. 1325): „Podczas przewozu nie powinny być przekroczone terminy określone w 8.1.4.4.” – termin kontroli upływa w trakcie 3-dniowej trasy. A „Nie, bo termin kontroli gaśnicy nie może upłynąć w trakcie przewozu” (67); B „wystarczy ważny przy wyjeździe” (70); C „plomba nienaruszona” (65; plomba = brak użycia, 8.1.4.4). Sources „8.1.4.5; 8.1.4.4”. Pokrewne 0074/0422/0283 (termin już minął / brak oznaczenia) – nowe pytanie dotyczy terminu upływającego w czasie przewozu.

## ADR-B-0233 – POPRAW (linia ChatGPT bez zmian)
- 5.4.1.1.1(g),(h) (s. 962) – cytat ✔. Bank 0233 = 0579 (brak danych odbiorcy), opcje 90–103 zn. Propozycja (ta sama firma jako nadawca i odbiorca) – temat nowy. Przyjęta w całości.

## ADR-B-0234 – POPRAW (nowe pytanie)
- Cytat CG 5.4.3.4 (s. 974) „Forma i zawartość instrukcji pisemnych powinny odpowiadać czterostronicowemu wzorowi podanemu poniżej.” ✔; propozycja (brak 4. strony → potrzebne cztery strony) to piąte pytanie na tę samą regułę (0039, 0088, 0234, 0586).
- Nowe: gdzie we wzorze jest wykaz wyposażenia – C „Na ostatniej, czwartej stronie wzoru, w wykazie sprzętu ochrony załogi” (70); A pierwsza strona (72); B karta charakterystyki (68). Wzór s. 975 (czynności), 976–978 (wskazówki wg nalepek), 978 („Sprzęt ochrony ogólnej i indywidualnej…”). Sources „5.4.3.4”.

## ADR-B-0235 – POPRAW (linia ChatGPT z poprawką)
- 7.5.7.1 (s. 1308–1309): „Wymagania określone w tym przepisie uważa się za spełnione, jeżeli ładunek jest zabezpieczony zgodnie z EN 12195-1:2010.” ✔. Temat nowy (brak „12195” w banku).
- Dystraktory CG niewiarygodne („wyklucza tę normę”, „poniżej 3,5 tony”) → B „…wymaga jeszcze zatwierdzenia… przez właściwą władzę” (80), C „…osobnym pasem przypięto też najmniejsze kartony” (74; 7.5.7.1 dopuszcza przekładki/blokowanie); A (76). Stem jako sytuacja praktyczna.

## ADR-B-0236 – POPRAW (linia ChatGPT bez zmian)
- 7.5.7.1 (s. 1308) – zdanie o przekładkach/blokowaniu i o nadmiernym napinaniu ✔. Temat (wypełnienie luk przekładkami) nowy. Długości 61/49/42 – klucz nie jest skrajny.

## ADR-B-0237 – POPRAW (linia ChatGPT z poprawką)
- 7.5.7.3 (s. 1309): „Podczas załadunku i rozładunku sztuki przesyłek zawierające towary niebezpieczne powinny być chronione przed uszkodzeniem.” ✔ (+ UWAGA o przesuwaniu). Temat nowy; kompetencja K05 (piętrzenie) – sytuacja dotyczy piętrowanych opakowań.
- A „Przesunąć karton, bo dolny jest przeznaczony do piętrzenia” (58; mylenie 7.5.7.2 z 7.5.7.3), C „Zmienić sposób przeładunku tak, aby nie uszkodzić opakowań” (58; w wersji CG klucz byłby jedyną najkrótszą po zmianie A).

## ADR-B-0238 – POPRAW (linia ChatGPT bez zmian)
- 7.5.8.1 (s. 1309) ✔; 7.5.8.2 (s. 1310) – wyjątek „te same towary” tylko dla przewozu luzem. Uzupełnia 0201 (luzem, ten sam towar). Przyjęta.

## ADR-B-0239 – POPRAW (nowe pytanie)
- Cytat CG 7.5.1.3 (s. 1304) ✔; propozycja (rozładunek wstrzymać przy brakach) = **0476** (7.5.1.3, ADR-B-04) i 0135 – duplikat.
- Nowe: 7.5.1.2 (s. 1304) „załadunek nie powinien się odbyć, jeżeli: – sprawdzenie dokumentów; lub – oględziny pojazdu… wskazują, że załoga pojazdu… nie spełniają wymagań” – nieważne zaświadczenie ADR kierowcy przy rampie. B „Nie, bo sprawdzenie dokumentów wykazało, że kierowca nie spełnia wymagań” (72); A „sprawdza się pojazd, a nie dokumenty kierowcy” (71); C „przewoźnik pisemnie przejmie odpowiedzialność” (75). 8.1.2.2(b) (s. 1324) – zaświadczenie w kabinie. Sources „7.5.1.2; 8.1.2.2(b)”. Pokrewne 0607 (kierowca bez zaświadczenia – ADR-B-01) – inny uczestnik i inny przepis.

## ADR-B-0240 – POPRAW (nowe pytanie)
- Cytat CG 7.5.8.1 (s. 1310) „Środki ostrożności uważa się za odpowiednie…” ✔; propozycja (brak możliwości czyszczenia na miejscu → przejazd z zabezpieczeniem) = **0706** – duplikat (ChatGPT wskazał 0201/0677/0733, a pominął 0706). Bank 0240 (luzem, inny towar) = 0677, 0733.
- Nowe: czyszczenie możliwe u odbiorcy, kierowca chce jechać 150 km do bazy. C „Oczyścić pojazd u odbiorcy, bo przejazd jest dla sytuacji bez takiej możliwości” (79); A „wystarczy przed kolejnym załadunkiem” (79); B bez zabezpieczeń (67). 7.5.8.1 (s. 1309–1310): „niezwłocznie oczyścić…”, „Jeżeli czyszczenia nie można przeprowadzić w miejscu rozładunku, to… do najbliższego miejsca”. Sources „7.5.8.1”.

## Uwagi do raportu ChatGPT
- Liczby werdyktów 0/15/0 i licznik 513 – poprawne. Cytaty i strony 15/15 – dobrze.
- Postęp: są linie JSONL i test. Ale **7 z 15 propozycji to duplikaty** innych pytań banku (0780, 0165/0696, 0745, 0747, 0039/0586, 0476, 0706) – sprawdzać propozycję (nie tylko oryginał) w całym banku, także w innych działach (0476 jest w ADR-B-04, 0362 w ADR-B-04, 0677/0733 w ADR-B-03).
- Sprawdzać, którą kompetencję obsługuje ID, i nie wychodzić poza nią (0232: 8.1.4.3 zamiast 8.1.4.5).
- Dystraktory mają być wiarygodne (0235: „wyklucza normę”, „poniżej 3,5 t”), bez słów absolutnych (0227 „wszystkie”).
- Lekcje i scenariusze do sprawdzenia po wdrożeniu: `podstawowy/lekcje/ADR-B-05.md` (l. ok. 106, 146–149: 0229–0232), `ADR-B-09.md` (l. ok. 96, 117, 143–148: 0235–0240), `ADR-B-13.md` (l. ok. 131–135: 0226–0228, 0233, 0234); `podstawowy/praktyka/SCENARIUSZE.md` l. ok. 183 (ćwiczenie z 0235–0240: „źle zamocowane opakowania, zbyt mocno zaciśnięty pas, niedozwolone piętrzenie, pozostałości po wycieku” – 0239 dotyczy teraz kontroli dokumentów przed załadunkiem), l. 325 i SC-ADR-B-09-03 (0235 – teraz norma EN 12195-1, nadal pasuje), `scenariusze-13-dzialow.json` (0235).
