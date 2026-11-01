# Etap 4x261 — skażona odzież i środki ochronne po awarii

Data: 01.11.2026  
Zakres: wyłącznie kurs podstawowy ADR  
Baza: main `cd29ba93bf95ef43b5c1001057c4ae715c788ee4`  
Nowe ID: `ADR-B-0687`  
Kompetencja: `ADR-B-03-K05` — unikanie skażenia przy rozlewie

## Wybór luki

Kompetencja miała cztery pytania, wszystkie dotyczące niezbliżania się do nieznanego rozlewu, unikania oparów i bezpiecznego wezwania pomocy. Nie obejmowała dalszego kroku z instrukcji pisemnych: postępowania ze skażoną odzieżą i użytymi skażonymi środkami ochronnymi po bezpiecznym oddaleniu się od miejsca awarii. Nowe pytanie uzupełnia ten etap i nie powiela pytań o sam rozlew.

## Dodane pytanie

- `ADR-B-0687`: po bezpiecznym oddaleniu się od rozlewu kierowca zauważa, że odzież i użyte rękawice ochronne są skażone.
- Klucz: **A** — zdjąć skażoną odzież i użyte skażone środki ochronne oraz bezpiecznie je usunąć; nie zabierać ich do kabiny.
- Explanation: **410 znaków, 4 zdania**; najpierw wyjaśnia ryzyko przeniesienia substancji, następnie wskazuje prawidłowe działanie, odrzuca mylące dystraktory i podaje podstawę.
- Długości odpowiedzi A/B/C: **110/109/114** znaków. Poprawna A nie jest ani najdłuższa, ani najkrótsza.
- Status: `needs_review`; nie zmieniono statusu żadnego pytania na `verified`.

## Podstawa prawna

- **ADR 2025, 5.4.3.4** — czterostronicowy model instrukcji pisemnych. W części „Działania w razie wypadku lub awarii” model nakazuje zdjąć skażoną odzież i użyte skażone środki ochronne oraz bezpiecznie je usunąć.
- Dz.U. 2025 poz. 642: https://dziennikustaw.gov.pl/DU/2025/642
- Oficjalny tekst polski ADR tom II 2025, Ministerstwo Infrastruktury: https://www.gov.pl/attachment/b7292c03-ac9d-4f80-9a29-c22f53d847b8
- UNECE — polskie i inne językowe wersje instrukcji pisemnych ADR: https://unece.org/transport/road-transport/linguistic-versions-adr-instructions-writing

Pytanie nie dopowiada kodu odpadu, firmy odbierającej ani szczegółowej technologii unieszkodliwiania — ADR w tym punkcie wymaga bezpiecznego usunięcia skażonych rzeczy. Pełne literalne porównanie z właściwym tekstem Dz.U. oraz niezależna recenzja specjalisty pozostają pending. Pytanie pozostaje `needs_review`.

## Synchronizacja #646

- Bank: **687** pytań ADR-B-0001–0687; wszystkie `needs_review`, 0 `verified`.
- Blob SHA `questions.jsonl`: `ba18db9994feecf876b449a203dcc1590e16523f`.
- Rozkład prawidłowych opcji: **A=236 / B=234 / C=217**.
- „Poprawna = jedyna najdłuższa”: **72/687 = 10,48%**, poniżej limitu Quality Gate 18%; maksimum działu 13,95%.
- `ADR-B-03-K05` ma teraz 5 pytań; moduł ADR-B-03 ma 56 pytań.
- Zaktualizowano klucze i warianty egzaminów próbnych 001–005 do aktualnego SHA; dodano snapshoty `review/sequential/687-687.json` i `review/legal-clauses/687-687.json`; zaktualizowano ledger, manifesty, kolejki recenzenckie, mapę kompetencji, lekcję i materiał instruktora.
- PR i CI: do potwierdzenia po otwarciu PR. Nie uruchomiono lokalnego Quality Gate.

## Pliki audytowe

- Rejestr: `review/specialist/REJESTR-0687-0687.md`
- Ledger: `review/legal-polish/stage4w4-literal-verification-ledger-0610-0678.json`
- Snapshot sekwencyjny: `review/sequential/687-687.json`
- Snapshot prawny: `review/legal-clauses/687-687.json`
