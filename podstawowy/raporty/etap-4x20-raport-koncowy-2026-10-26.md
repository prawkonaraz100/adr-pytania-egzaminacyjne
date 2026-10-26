# Raport końcowy — etap 4x20

Data: 26.10.2026  
Repozytorium: `prawkonaraz100/adr-pytania-egzaminacyjne`  
Zakres: wyłącznie kurs podstawowy ADR.

## Wynik etapu

- Bank zawiera **609 pytań**: ADR-B-0001–ADR-B-0609.
- **609 `needs_review`, 0 `verified`, 0 formalnych zatwierdzeń.** Żadne pytanie nie zostało zatwierdzone automatycznie.
- W 14 partiach ręcznie przejrzano wyjaśnienia całego banku; **68 wyjaśnień przepisano lub doprecyzowano**. Zmiany obejmowały m.in. rozwinięcie skrótów UN, IMDG, ICAO/ICAO TI, EQ, LQ, DMC, FL, AT, EX/II i EX/III oraz prostsze objaśnienia wyłączenia 1.1.3.6, kodów tunelowych, dokumentów i obowiązków uczestników. Pozostałe wyjaśnienia zachowano po przeglądzie jako wystarczająco czytelne.
- Wyjaśnienia zachowują format dla kursanta: sens poprawnej odpowiedzi, powód, dla którego mylą się błędne warianty, i krótka podstawa ADR. Kontrola strukturalna wymaga minimum 200 znaków; w zakończonych partiach raportowano brak wyjaśnień krótszych od progu.
- Potwierdzone błędy prawne nie były korygowane na podstawie samej intuicji. W tej końcowej partii nie zmieniono treści pytań, opcji ani poprawnych liter; wyjaśnienia 0601, 0602, 0603, 0604, 0606 i 0608 uproszczono redakcyjnie.

## Egzaminy próbne 001–005

Po aktualizacji wyjaśnień ponownie wygenerowano wszystkie pięć wariantów i kluczy z aktualnego banku.

| Kontrola | Wynik |
|---|---|
| Liczba wariantów | 5 |
| Pytań na wariant | 30 |
| Łącznie unikalnych ID | 150, bez powtórzeń między wariantami |
| Pokrycie działów | Wszystkie 13 działów w każdym wariancie, po 2–3 pytania na dział |
| Poprawna odpowiedź jako jedyna najdłuższa | 0/30 (0%) w każdym wariancie |
| Rozkład poprawnych liter | A/B/C = 10/10/10 w każdym wariancie |
| Najdłuższa seria tej samej litery | Maksymalnie 3 |
| Synchronizacja | Arkusze i klucze wskazują aktualny blob banku; wyjaśnienia kluczy mapują się do kolejności opcji |
| Autoryzacja publikacji | Wyłączona; materiały treningowe, nie oficjalne egzaminy |

Dodano blokującą kontrolę progu 18% dla wskaźnika „poprawna = jedyna najdłuższa” w `scripts/check_mock_exam_variants.py` oraz test regresyjny w `tests/test_mock_exam_variants.py`.

## CI i raporty

- PR #393 — wyjaśnienia ADR-B-0601–0609 i synchronizacja snapshotów: PASS [Quality Gate](../actions/runs/40257321013), scalony.
- PR #394 — regeneracja egzaminów 001–005 i kontrola długości odpowiedzi: PASS [Quality Gate](../actions/runs/40258031058), scalony.
- Raport partii końcowej wyjaśnień: [etap 4x20, ADR-B-0601–0609](etap-4x20-partia-14-explanation-0601-0609-2026-10-26.md).
- Raport egzaminów: [regeneracja wariantów 001–005](etap-4x20-egzaminy-001-005-2026-10-26.md).

## Pakiet recenzyjny dla specjalisty

Pakiet ma stan na 26.10.2026 i zawiera:
- `podstawowy/questions.jsonl` — 609 pytań;
- 13 lekcji `podstawowy/lekcje/ADR-B-01.md`–`ADR-B-13.md`;
- 13 materiałów instruktora `podstawowy/instruktor/ADR-B-01.md`–`ADR-B-13.md`;
- `podstawowy/praktyka/scenariusze-13-dzialow.json` i `podstawowy/praktyka/SCENARIUSZE.md` — 39 scenariuszy, po 3 na dział;
- `podstawowy/SLOWNICZEK.md` — 90 haseł;
- `podstawowy/egzamin-probny/wariant-001.json`–`wariant-005.json` i odpowiadające pliki `klucz-001.json`–`klucz-005.json`;
- `review/specialist/REJESTR-AKTUALNY-0001-0609.md`, `review/specialist/PAKIET-0609-MANIFEST.json`, `review/specialist/INSTRUKCJA-RECENZJI.md`, `review/specialist/FORMULARZ-UWAG.md`;
- audyty `review/sequential/`, `review/legal-clauses/`, rejestr źródeł `review/legal-polish/stage4w4-literal-verification-ledger-0001-0609.json` oraz checklistę wrażliwości na ADR 2027 `review/specialist/ETAP-4X9-ADR-2027-LISTA-KONTROLNA.md`.

## Otwarte kwestie prawne — do rozstrzygnięcia przez specjalistę

- 376 rekordów nie ma jeszcze pobranego pełnego tekstu właściwego przepisu urzędowego w polskiej wersji do porównania literalnego.
- Dla 10 rekordów sprawdzono źródło docelowe, ale pełne porównanie przepisu pozostaje otwarte.
- 223 rekordy mają zapisany wynik porównania ukierunkowanego z tekstem polskim; nadal wymagają potwierdzenia względem prawnie wiążącego tekstu Dz.U. i niezależnej recenzji A/B/C.
- Wszystkie 609 pytań wymagają rzeczywistej recenzji specjalisty. Sprawdzenie automatyczne, redakcja językowa, raporty i PASS CI nie są zatwierdzeniem prawnym.
- Pytania wrażliwe na zmianę edycji ADR 2027 należy sprawdzać według checklisty 4x9. Nie zmieniać wartości, progów ani wyjątków bez opublikowanego i potwierdzonego tekstu.

## Status końcowy

Etap 4x20 redakcyjnie zakończony. Bank pozostaje materiałem roboczym do recenzji; nie rozpoczęto kursu cystern ani żadnego innego kursu.
