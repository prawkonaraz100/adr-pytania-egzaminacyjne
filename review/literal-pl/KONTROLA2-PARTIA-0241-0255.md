# Kontrola druga – partia ADR-B-0241–0255 (porównanie dosłowne z polskim tekstem ADR 2025)

Data: 2026-11-04, ok. 11:15 (czas polski, CET).
Przedmiot: PR #861 (scalony 10:55 CET, main **0412d21**, CI zielone). Raport ChatGPT `review/literal-pl/PARTIA-0241-0255.md/.json`, wynik ChatGPT 0 OK / 15 POPRAW / 0 BLOKUJ; ChatGPT dostarczył 15 linii `POPRAWKI-0241-0255.jsonl` + `tests/test_literal_proposals_0241_0255.py`. Bank bez zmian (blob 98a39081…).
Źródło: Dz.U. 2025 poz. 642 (skany PDF), OCR tesseract `-l pol`; strony wg nagłówka „Dziennik Ustaw — NNNN —”. [obraz] = sprawdzone na obrazie strony PDF: `kontrola2/b17-p27-1325-25.png` (s. 1325 – 8.1.5.2, 8.1.5.3 i przypisy 2–4). Sprostowanie poz. 1575 nie dotyczy punktów tej partii.
Status: kontrola robocza. **Żadne pytanie nie jest oznaczone jako zweryfikowane**; wszystkie pozostają `needs_review`.

## Podsumowanie

- **Klucze wszystkich 15 pytań partii w banku są poprawne.** Żadna litera klucza się nie zmienia. Błędów klucza w partii: 0.
- **BŁĄD KLUCZA POZA PARTIĄ – ADR-B-0484** (ADR-B-08-K07): klucz C brzmi „Nie; ten zestaw dotyczy określonych materiałów w postaci stałej, a nie samej cieczy oznaczonej nalepką 8”, a przypis 4 do 8.1.5.3 (s. 1325 [obraz]) mówi: „Wymagane jest tylko w przypadku materiałów stałych **i materiałów ciekłych**, oznakowanych nalepkami ostrzegawczymi o numerach 3, 4.1, 4.3, 8 lub 9.” Pytanie przeczy też 0681 i 0734. Przygotowano linię zastępczą `kontrola2/POPRAWKI-KONTROLA2-0484-KLUCZ.jsonl` (litera C bez zmian, nowa treść C: „Tak, bo ten wymóg obejmuje materiały stałe i ciekłe oznaczone nalepką 8”; A/B – nowe dystraktory, explanation od nowa). 0484 nie występuje w egzaminach 001–005.
- Werdykty (pytania w banku): **OK 0**, **POPRAW 15**, **BLOKUJ 0** – zgodnie z ChatGPT. Licznik 513 → **498/780** – poprawny.
- **Duplikaty w banku – 14 z 15**: 0242 = 0100/0494 (i 0163); 0243 = 0011/0357 (i 0048/0678); 0244 = 0047/0359/0515; 0245 = 0020/0054/0517; 0246 = 0118; 0247 = 0028/0030; 0248 = 0063/0434/0575; 0249 = 0414 (numer zlecenia)/0120; 0250 = 0087/0175/0672; 0251 = 0023/0509; 0252 = 0075/0596; 0253 = 0076/0705/0597; 0254 = 0077/0171/0485; 0255 = 0016/0190. **0241 nie jest duplikatem** (jedyne pytanie o 5.4.1.1.6.3(b)), ale ma wady formy (A rzeczownikowa, B/C czasownikowe, C 88 zn.).
- **Propozycje ChatGPT – 9 z 15 to znowu duplikaty, a dwie dublują się wzajemnie:** **0242** (osłona kratki bez wchodzenia w wyciek) = **0163**; **0243** (zakres zakazu: kierowca i pomocnik) = **0048** (+0678/0737); **0244** (pompa + zgoda państwa → wolno) = **0358**; **0246** (podwykonawca odbiorcy) = **0477**; **0247** (1.1.4.2.1(c) tylko dla łańcucha morskiego) = **0206**; **0251** (przyczepa bez hamulca, 8.3.7) = **0352**; **0252** (jedno oświetlenie na dwie osoby) = **0686**; **0254** (łopata/osłona/pojemnik przy nalepce 8) = **0681**; **0249 i 0250** – obie propozycje to ta sama reguła (1.1.3.6.2 wyłącza dział 1.10 przy zwykłej klasie 3). ChatGPT sam wskazał ryzyko przy 0242, 0244, 0246, 0251, 0252, 0254 – słusznie; przeoczył 0243, 0247 i parę 0249/0250. **0248** (dolna część komórki) – bliskie 0208/0174, przerobione na rozróżnienie kategorii transportowej i kodu tunelowego.
- Propozycje przyjęte: **bez zmian 0245**; z poprawką **0241** (explanation – dopasowanie do aktualnych B/C), **0250** (A „każdego”, C niewiarygodna „wystarczy obecność drugiego członka załogi”, B była jedyną najkrótszą), **0253** (A „każde okulary” – słowo absolutne), **0255** (A „…jak przy odstępstwie” zdradzała błąd; nowe A/B/C o równej długości, stem odwołuje się do rysunku 33/1203, explanation wyjaśnia 65 mm/10 mm z 5.3.2.2.1). **Nowe pytania z kontroli drugiej: 0242, 0243, 0244, 0246, 0247, 0248, 0249, 0251, 0252, 0254.** Wszystkie: ten sam ID, `module_id`, litera klucza i kompetencja w `kompetencje.json` (liczebność kompetencji bez zmian – wszystkie ≥6; K03-03, K03-04, K04-02, K04-03, K07-03, K07-04, K08-04, K08-05, K08-06, K11-03, K12-04, K13-05 po 6, K08-07 8, K06-03 11, K10-01 11).
- **Cytaty ChatGPT istnieją dosłownie** (15/15) i pasują do punktów. Uwaga: 0249/0250 – cytat „działu 1.10, z wyjątkiem towarów dużego ryzyka” urwany przed „klasy 1 (zgodnie z 1.10.3.1) oraz z wyjątkiem materiałów klasy 7…” – nie urywać przed warunkiem.
- **Strony – 15 z 15 dobrych:** 5.4.1.1.6.3(b) – **965**; 8.1.5.3 (osłona) – **1325**; 8.3.3 – **1332**; 8.3.6 – **1332**; 1.4.3.1.1(b) – **57**; 1.4.2.3.3 – **57**; 1.1.4.2.1(c) – **29**; 8.6.3.1 – **1338**; 1.1.3.6.2 – **26** (×2); 8.3.7 – **1332**; 8.1.5.2 (oświetlenie, ochrona oczu) – **1325**; przypis do 8.1.5.3 – **1325**; 5.3.2.2.2 – **955**. Strony punktów dodanych w kontroli drugiej: 5.4.3.4 (środowisko wodne) – **975**; 1.4.2.3.1 – **57**; zdanie końcowe 1.1.4.2.1 („Powyższe odstępstwo nie ma zastosowania…”) – **30**; opis kolumny (15) w 3.2.1 – **311–312**; 1.10.1.2, 1.10.1.4, 1.10.3.1.1 – **110**; 8.1.5.1 – **1325**; 5.3.2.2.1 – **955**.
- Wskaźnik „poprawna = jedyna najdłuższa”: **69/780 = 8,85% → 66/780 = 8,46%** (ADR-B-08 6 → 4 [0253, 0484], ADR-B-10 4 → 3 [0247]; maks. działu 15,22% ADR-B-11 bez zmian). **Liczbę trzeba zmienić** w `docs/POKRYCIE-KURSU.md` (l. 11), `podstawowy/README.md` (l. 3) i `review/specialist/PAKIET-ZAMKNIECIE-0780.md` (l. 9).
- Wskaźnik „poprawna = jedyna najkrótsza” (limit 38%): globalnie 236 → 233 (0244, 0248, 0250 już nie); ADR-B-04 26,0% → 24,0%, ADR-B-11 28,3% → 26,1%, ADR-B-13 29,6% → 27,8% – zielone.
- Plik poprawek: `kontrola2/POPRAWKI-KONTROLA2-0241-0255.jsonl` – **15 pełnych linii** (+ `POPRAWKI-KONTROLA2-0484-KLUCZ.jsonl` – 1 linia); kolejność pól, `module_id`, `image` (0255 – rysunek zostaje) i litery kluczy bez zmian, `needs_review`, `checked_at/reviewer=null`. Generator: `kontrola2/build_p17.py` (kontrole: klucz nie jest jedyną najdłuższą/najkrótszą, opcje ≤80 zn., brak słów absolutnych i średników w opcjach, explanation 2–5 zdań, ≥300 zn., ≤35 słów w zdaniu, bez „np.”/„min.”/„kol.”, końcówka „Podstawa: ADR …”).
- Test na kopii repo (/tmp/b17 = main 0412d21, bez commitów i pushu; `kontrola2/test_p17.sh` + `kontrola2/sync_p17_test.py`): `apply_poprawki.py` z oboma plikami → **Changed (16): ADR-B-0241 … ADR-B-0255, ADR-B-0484**; nowy SHA blobu banku **944ba10bb1af4f1c20a291a3fa6a8304f1ba39b6** (było 98a390814b7f4a9f5bbdbf8b087b8a318d3635a4). Przed synchronizacją czerwone: 10 testów (test_course_consistency ×2, test_coverage_report_metrics, test_mock_exam_variants, test_review_packet_integrity ×4, test_stage4u_lesson_selfcheck, test_stage4x97_current_snapshot) oraz check_mock_exam_variants, check_sequential_audit, check_legal_clause_review, course_consistency. Synchronizacja: warianty/klucze egzaminów – 0251 (003), 0241 (004), 0254 (005); SHA we wszystkich wariantach i kluczach 001–005; snapshoty `review/sequential/` i `review/legal-clauses/` 241-246, 247-250, 251-254, 255-258 (15 ID) i 483-494 (0484) – nowe przepisy, ocena A/B/C, notes ≥25 zn.; ledger `stage4w4-literal-verification-ledger-0001-0609.json` – 8 ID (0242, 0245, 0248, 0249, 0250, 0251, 0254, 0255); SHA w dokumentach jak w #860; wskaźnik 66/780. **Po synchronizacji wszystko zielone:** validate, coverage, check_mock_exam_variants, answer_leakage_metrics, answer_length_bias --threshold 0.16 --strict, check_explanation_quality --minimum 300, check_near_duplicates 0.60, check_cross_module_duplicates 0.80, similarity 0.45 (brak par z 0241–0255/0484), check_explanation_heuristics, release_gate --report, check_sequential_audit, check_legal_clause_review, course_consistency; **unittest 159/159 OK** (w tym test_literal_proposals_0241_0255).

## Tabela werdyktów

| ID | Dział / kompetencja | Klucz | ChatGPT | Kontrola 2 | Punkt / s. Dz.U. | Uwagi |
|---|---|---|---|---|---|---|
| 0241 | 03 / K03 | A ✔ | POPRAW | POPRAW (linia CG, nowe explanation) | 5.4.1.1.6.3(b) / 965 | bank – temat unikalny, wady formy |
| 0242 | 03 / K04 | B ✔ | POPRAW | POPRAW (nowe pytanie) | 5.4.3.4 / 975; 8.1.5.3 / 1325 | bank = 0100, 0494; CG = 0163 |
| 0243 | 04 / K02 | C ✔ | POPRAW | POPRAW (nowe pytanie) | 8.3.3 / 1332 | bank = 0011, 0357; CG = 0048 |
| 0244 | 04 / K03 | A ✔ | POPRAW | POPRAW (nowe pytanie) | 8.3.6 / 1332 | bank = 0047, 0359, 0515; CG = 0358 |
| 0245 | 07 / K03 | B ✔ | POPRAW | POPRAW (linia CG bez zmian) | 1.4.3.1.1(b) / 57 | bank = 0020, 0054, 0517 |
| 0246 | 07 / K04 | C ✔ | POPRAW | POPRAW (nowe pytanie) | 1.4.2.3.1 / 57 | bank = 0118; CG = 0477 |
| 0247 | 10 / K01 | B ✔ | POPRAW | POPRAW (nowe pytanie) | 1.1.4.2.1 / 29–30 | bank = 0028, 0030 (B 90 zn.); CG = 0206 |
| 0248 | 11 / K03 | A ✔ | POPRAW | POPRAW (CG przerobiona) | 8.6.3.1 / 1338; 3.2.1 kol. (15) / 311–312 | bank = 0063, 0434, 0575; CG ≈ 0208, 0174 |
| 0249 | 12 / K04 | C ✔ | POPRAW | POPRAW (nowe pytanie) | 1.1.3.6.2 / 26; 1.10.1.2, 1.10.3.1.1 / 110 | bank = 0414, 0120; CG = ta sama reguła co CG 0250 |
| 0250 | 13 / K05 | B ✔ | POPRAW | POPRAW (linia CG z poprawką) | 1.1.3.6.2 / 26; 1.10.1.4 / 110 | bank = 0087, 0175, 0672 |
| 0251 | 08 / K04 | A ✔ | POPRAW | POPRAW (nowe pytanie) | 8.1.5.1, 8.1.5.2 / 1325 | bank = 0023, 0509; CG = 0352 |
| 0252 | 08 / K05 | B ✔ | POPRAW | POPRAW (nowe pytanie) | 8.1.5.2 / 1325 | bank = 0075, 0596; CG = 0686 |
| 0253 | 08 / K06 | C ✔ | POPRAW | POPRAW (linia CG, A bez „każde”) | 8.1.5.2 / 1325 | bank = 0076, 0705, 0597 |
| 0254 | 08 / K07 | A ✔ | POPRAW | POPRAW (nowe pytanie) | 8.1.5.1, 8.1.5.3 / 1325 | bank = 0077, 0171, 0485; CG = 0681 |
| 0255 | 06 / K03 | B ✔ | POPRAW | POPRAW (linia CG z poprawką) | 5.3.2.2.2, 5.3.2.2.1 / 955 | bank = 0016, 0190 |
| *0484* | *08 / K07* | *C ✘ treść* | – | *POPRAW – błąd klucza* | *8.1.5.3 przypis 4 / 1325 [obraz]* | *poza partią; przeczy 0681, 0734* |

---

## ADR-B-0241 – POPRAW (linia ChatGPT, nowe explanation)
- 5.4.1.1.6.3(b) (s. 965): „Jeżeli próżne nieoczyszczone pojazdy lub kontenery przewożone są zgodnie z przepisem 7.5.8.1 do najbliższego miejsca… powinien być zamieszczony dodatkowo następujący zapis: „PRZEWÓZ ZGODNY Z 7.5.8.1”.” ✔
- Linia CG: A z dosłownym zapisem (60), B „Zastąpić opis towaru słowami KONTENER BEZ ŁADUNKU” (51), C „Wskazać jedynie adres czyszczenia…” (68). Explanation CG mówiło o „wolnym od pozostałości” – nie odpowiadało B; nowe explanation omawia aktualne B i C.

## ADR-B-0242 – POPRAW (nowe pytanie)
- Propozycja CG (osłona kratki, dojść bez kontaktu) = **0163** („Osłonić kratkę, jeśli to właściwe i bezpieczne, bez wchodzenia w wyciek”). Bank = 0100/0494.
- Nowe: ciecz spływa do przydrożnego rowu z wodą, brak kratki. 5.4.3.4 (s. 975): „Jeżeli jest to właściwe i bezpieczne, zapobiec przedostaniu się uwolnionych materiałów do środowiska wodnego lub kanalizacji oraz zebrać uwolnione materiały, używając wyposażenia…”; „Nie wchodzić na uwolnione materiały, nie dotykać ich”. B „Ograniczyć spływ cieczy do rowu, jeżeli jest to właściwe i bezpieczne” (69); A „jedynie kanalizację” (77); C wejść do rowu (64). Bank nie miał pytania o środowisko wodne w instrukcjach (wszystkie K03-04 dotyczą kratki). Sources „5.4.3.4; 8.1.5.3”.

## ADR-B-0243 – POPRAW (nowe pytanie)
- Propozycja CG („zakaz dotyczy kierowcy i pomocnika, nie wszystkich magazynierów”) = **0048** (kogo obejmuje 8.3.3) i 0678/0737; dodatkowo mało przydatna dydaktycznie.
- Nowe: kierowca chce na postoju otworzyć karton i przełożyć puszki do lżejszego kartonu. 8.3.3 (s. 1332): „Zabrania się kierowcy i jego pomocnikowi otwierania sztuk przesyłek zawierających towary niebezpieczne.” C „Nie, bo kierowca nie może otwierać sztuk przesyłek z towarem ADR” (64); A puszki zamknięte (63); B zrobi to pomocnik (64).

## ADR-B-0244 – POPRAW (nowe pytanie)
- Propozycja CG (pompa niezbędna i przepisy państwa pozwalają → silnik może pracować) = **0358**.
- Nowe: pompa niezbędna, ale przepisy państwa NIE zezwalają – oba warunki 8.3.6 (s. 1332) są łączne („…niezbędne dla pracy pomp… oraz gdy zezwalają na to przepisy państwa”). A „Nie uruchamiać silnika, bo wyjątek wymaga też zgody przepisów tego państwa” (74); B (75); C „krócej niż piętnaście minut” (70).

## ADR-B-0245 – POPRAW (linia ChatGPT bez zmian)
- 1.4.3.1.1(b) (s. 57): „…obowiązek ten dotyczy również próżnych nieoczyszczonych opakowań” ✔. Temat nowy (brak pytań o próżne nieoczyszczone opakowania u załadowcy). Długości 41/60/69 – klucz w środku. Sources zawężone przez CG do „1.4.3.1.1(b)” – dobrze.

## ADR-B-0246 – POPRAW (nowe pytanie)
- Propozycja CG (odbiorca zleca rozładunek i czyszczenie podwykonawcy) = **0477** (zewnętrzna firma rozładunkowa, 1.4.2.3.3) – ta sama reguła. Bank = 0118 (zwłoka „bo tak wygodniej”).
- Nowe: odbiorca każe czekać, bo na rampie trwa usuwanie rozlewu – opóźnienie konieczne. 1.4.2.3.1 (s. 57): „Odbiorca zobowiązany jest nie opóźniać przyjęcia towarów, jeżeli takie opóźnienie nie jest konieczne…”. C „Nie, bo to opóźnienie jest konieczne ze względu na bezpieczeństwo” (65); A (70); B godzina ze zlecenia (62).

## ADR-B-0247 – POPRAW (nowe pytanie)
- Propozycja CG (kontener na lotnisko z nalepkami IMDG – (c) tylko łańcuch morski) = **0206** (ta sama reguła: odstępstwo (c) tylko z przewozem morskim); scenariusz mało realny.
- Nowe: zdanie końcowe 1.1.4.2.1 (s. 30): „Powyższe odstępstwo nie ma zastosowania do przewozu towarów sklasyfikowanych jako niebezpieczne w klasach 1 do 9 zgodnie z ADR, a nieuznanych za niebezpieczne według Kodeksu IMDG lub Instrukcji Technicznych ICAO.” – brak w banku. B „Nie, odstępstwo nie obejmuje towaru nieuznanego za niebezpieczny w IMDG” (71); A (71); C (63).

## ADR-B-0248 – POPRAW (propozycja ChatGPT przerobiona)
- 8.6.3.1 (s. 1338): „Kod ograniczeń przewozu przez tunele podany jest w nawiasie w dolnej części komórki.” ✔. Propozycja CG (w której części komórki) bliska 0208 (dolna część „(D/E)” – co oznacza) i 0174. K11-03 i ADR-B-11 mają nadmiar pytań o kolumnę 15 i „(-)” (0065, 0174, 0264, 0431, 0603).
- Nowe ujęcie: kierowca myli cyfrę kategorii transportowej „2” z kodem „(D/E)”. 3.2.1, opis kolumny (15) (s. 311–312): górna część – kategoria transportowa (1.1.3.6), dolna – kod w nawiasie. A „Nie, kodem jest „(D/E)”, a „2” to kategoria transportowa towaru” (63); B (62); C kolumna (7a) (67).

## ADR-B-0249 – POPRAW (nowe pytanie)
- Propozycja CG (klasa 3 w limicie 1.1.3.6 → 1.10.1.2 nie obowiązuje) to **ta sama reguła co propozycja CG 0250** (1.1.3.6.2 wyłącza dział 1.10). Bank 0249 = 0414 (zna numer zlecenia) / 0120.
- Nowe: wyjątek od tego wyłączenia – towar dużego ryzyka klasy 1 w limicie 1.1.3.6. 1.1.3.6.2 (s. 26): „działu 1.10, z wyjątkiem towarów dużego ryzyka klasy 1 (zgodnie z 1.10.3.1) oraz z wyjątkiem materiałów klasy 7…”; 1.10.1.2 (s. 110): „…wyłącznie przewoźnikowi odpowiednio zidentyfikowanemu”; 1.10.3.1.1 (s. 110) – definicja (zamachy terrorystyczne). C „Nie, bo dla towarów dużego ryzyka klasy 1 dział 1.10 nadal obowiązuje” (69); A „…dział 1.10 w ogóle nie obowiązuje” (76); B numer zlecenia (63). Pytanie uzupełnia 0211 (pełne ADR, klasa 3 → identyfikacja) i nowe 0250.

## ADR-B-0250 – POPRAW (linia ChatGPT z poprawką)
- 1.1.3.6.2 (s. 26) i 1.10.1.4 (s. 110) ✔. Temat nowy w K13-05 (dopełnienie 0175 „nie korzysta ze zwolnienia”). Poprawki: A „Tak, bo dokument ze zdjęciem obowiązuje przy klasie 3 w dowolnej ilości” (bez „każdego”), B (67; w CG była jedyną najkrótszą), C „…zwolnienie z 1.1.3.6 obejmuje jedynie przepisy części 8 ADR” (realne nieporozumienie zamiast „wystarczy obecność drugiego członka załogi”); explanation nazywa oba wyjątki (klasa 1 dużego ryzyka, klasa 7).

## ADR-B-0251 – POPRAW (nowe pytanie)
- Propozycja CG (odłączona przyczepa bez układu hamulcowego – klin, 8.3.7) = **0352** (8.3.7, ten sam przypadek).
- Nowe: przewóz wyłącznie z nalepką 9 – kierowca sądzi, że klin tylko przy towarach zapalnych. 8.1.5.1–8.1.5.2 (s. 1325): „Każda jednostka transportowa przewożąca towary niebezpieczne powinna posiadać…”; „klin pod koła, dla każdego pojazdu…”. A „Nie, klin pod koła jest wymagany przy towarach z dowolną nalepką” (64); B hamulec postojowy (67); C „wyposażenie dodatkowe dla klas 2 i 3” (56).

## ADR-B-0252 – POPRAW (nowe pytanie)
- Propozycja CG (jedno przenośne oświetlenie na dwie osoby) = **0686**. Bank = 0075/0596 (jedna kamizelka). Uwaga: polskie 8.3.4 (s. 1332) mówi tylko o powierzchniach metalowych mogących spowodować iskrę – temat lamp jest już w 0353, 0663, 0762.
- Nowe: norma podana jako przykład dla kamizelki – 8.1.5.2 (s. 1325): „kamizelka ostrzegawcza (np. określona w normie EN ISO 20471)”. B „Normę EN ISO 20471” (18); A „Normę EN 12195-1:2010” (21; mocowanie ładunku, 7.5.7.1); C „Normę EN 3-7:2004” (17; gaśnice, 8.1.4.3). Explanation mówi, że to przykład.

## ADR-B-0253 – POPRAW (linia ChatGPT, A bez „każde”)
- 8.1.5.2 (s. 1325): „ochrona oczu (np. okulary ochronne)” ✔. Temat nowy (okulary korekcyjne – brak w banku). A „Tak, bo zwykłe okulary też osłaniają oczy podczas przewozu towaru ADR” (69; w CG „każde okulary” i była jedyną najdłuższą).

## ADR-B-0254 – POPRAW (nowe pytanie)
- Propozycja CG (łopata, osłona, pojemnik przy cieczy z nalepką 8) = **0681** (to samo), a przy tym sprzeczna z 0484 (błąd klucza 0484 – patrz wyżej).
- Nowe: nalepka 6.1 jako dodatkowa przy nalepce 3 → maski ucieczkowe. 8.1.5.1 (s. 1325): „Elementy wyposażenia powinny być dobrane odpowiednio do numerów nalepek ostrzegawczych właściwych dla załadowanych towarów”; 8.1.5.3: „maska ucieczkowa… w przypadku numerów nalepek ostrzegawczych 2.3 lub 6.1”. A „Tak, bo maska jest wymagana przy nalepce 6.1, także jako dodatkowej” (67); B nalepka główna (60); C jedna maska dla kierowcy (69).

## ADR-B-0255 – POPRAW (linia ChatGPT z poprawką)
- 5.3.2.2.2 (s. 955): „…czarnymi cyframi o wysokości 100 mm i szerokości linii 15 mm” ✔; 5.3.2.2.1 (s. 955): 65 mm / 10 mm tylko dla zmniejszonych tablic przy opakowanym materiale promieniotwórczym (używanie wyłączne). Temat nowy (brak „100 mm” w banku); 0258 (partia 18) dotyczy wymiarów tablicy 40 × 30 cm – inny element.
- A CG „…jak przy odstępstwie” zdradzała błąd. Nowe A/B/C: 65/10, 100/15, 120/20 mm (48/49/49 zn.). Stem odwołuje się do rysunku `assets/adr-original/adr-b-0255-orange-33-1203.svg` (pole `image` zostaje).

## ADR-B-0484 (poza partią) – POPRAW, błąd treści klucza
- Bank: klucz C „Nie; ten zestaw dotyczy określonych materiałów w postaci stałej, a nie samej cieczy oznaczonej nalepką 8”. Przypis 4 do 8.1.5.3 (s. 1325 [obraz]) obejmuje **materiały stałe i ciekłe** z nalepkami 3, 4.1, 4.3, 8 lub 9 → odpowiedź merytorycznie błędna; sprzeczna z 0681 i 0734.
- Linia zastępcza (litera C bez zmian): C „Tak, bo ten wymóg obejmuje materiały stałe i ciekłe oznaczone nalepką 8” (71); A „Nie, bo zestaw jest wymagany przy materiałach stałych, a nie cieczach” (69); B „…przy nalepkach 2.3 i 6.1, a nie przy 8” (71). Explanation od nowa. Sources bez zmian „8.1.5.3, przypis 4”. Pytanie pozostaje bliskie 0681 (nalepka 8 → zestaw), ale akcentuje ciecz – do oceny w partii 33.

## Uwagi do raportu ChatGPT
- Liczby werdyktów 0/15/0 i licznik 498 – poprawne. Cytaty i strony 15/15 – dobrze.
- Postęp: ChatGPT sam zgłosił ryzyko duplikatów przy 6 propozycjach – ale zamiast je zostawić, trzeba było od razu zaproponować inny temat. Przeoczył 0243 (= 0048), 0247 (= 0206) i to, że 0249 i 0250 proponują tę samą regułę.
- „Podobne pytania” nie wychwyciło też sprzeczności 0484 ↔ 0681/0734 (pytania o ten sam wymóg z przeciwną odpowiedzią) – przy sprawdzaniu duplikatów porównywać też klucze.
- Lekcje: ADR-B-03.md l. 229 i 293 (oraz sources 0681, 0734) przypisują łopatę/osłonę/pojemnik do 8.1.5.2 – właściwy punkt to 8.1.5.3 (do poprawy przy partiach 46/49 lub przy okazji). Lekcje ADR-B-03/04/06/07/08/10/11/12/13 wymieniają zmienione ID tylko w listach – bez zmian treści; ADR-B-04.md l. 232 (0243 jako K02) – nadal prawda.
