# Etap 4x259 — trwałość i mocowanie tablic pomarańczowych

Data: 01.11.2026  
Zakres: wyłącznie kurs podstawowy ADR  
Baza: main `559d0dbdbcaaafbdf7f538ea31c34c5124657f97`  
Nowe ID: `ADR-B-0685`  
Kompetencja: `ADR-B-06-K07` — kolor i budowa tablicy

## Wybór luki

ADR-B-06-K07 miała cztery pytania, czyli minimalny poziom pokrycia w mapie. Dotychczasowe pytania sprawdzały kolor, czytelność, układ pól i widoczność oznakowania. Nie sprawdzały odrębnie trwałości materiału oraz utrzymania tablicy na mocowaniu podczas 15 minut objęcia ogniem. Kompetencja nie była tematem partii 4x227–4x258.

## Dodane pytanie

- `ADR-B-0685`: sytuacja kontroli pojazdu, którego tablica pomarańczowa jest czytelna, lecz jej mocowanie może puścić podczas pożaru.
- Klucz: **B** — materiał ma być odporny na warunki pogodowe, zapewniać trwałe oznaczenie, a tablica nie może odpaść od mocowania podczas 15 minut działania ognia.
- Explanation: **340 znaków, 4 zdania**; prostym językiem tłumaczy praktyczny wymóg, odrzuca błędne uproszczenia i podaje podstawę.
- Długości odpowiedzi A/B/C: **159/147/117** znaków. Poprawna B nie jest ani najdłuższa, ani najkrótsza.
- Status: `needs_review`; nie zmieniono statusu żadnego pytania na `verified`.

## Podstawa prawna i ograniczenia

- **ADR 2025, 5.3.2.2.1** — tablice pomarańczowe mają być odblaskowe, wykonane z materiału odpornego na warunki pogodowe i zapewniającego trwałe oznaczenie; nie mogą odpaść od mocowania podczas 15 minut objęcia ogniem.
- Źródło prawa: Dz.U. 2025 poz. 642: https://dziennikustaw.gov.pl/DU/2025/642
- Oficjalny tekst polski ADR tom II 2025, Ministerstwo Infrastruktury: https://www.gov.pl/attachment/b7292c03-ac9d-4f80-9a29-c22f53d847b8

Pytanie dotyczy tablicy na pojeździe. Nie obejmuje alternatywnego oznakowania dopuszczonego dla niektórych kontenerów, zbiorników i MEGC. Pełne literalne porównanie z właściwym tekstem Dz.U. oraz niezależna recenzja specjalisty pozostają pending. Pytanie pozostaje `needs_review`.

## Synchronizacja #646

- Bank: **685** pytań ADR-B-0001–0685; wszystkie `needs_review`, 0 `verified`.
- Blob SHA `questions.jsonl`: `a456d5fdab0c686b1c657be3f213ac873c491ae4`.
- Rozkład prawidłowych opcji: **A=234 / B=234 / C=217**.
- „Poprawna = jedyna najdłuższa”: **72/685 = 10,51%**, poniżej limitu Quality Gate 18%.
- `ADR-B-06-K07` ma teraz 5 pytań; moduł ADR-B-06 ma 55 pytań.
- Zaktualizowano klucze i warianty egzaminów próbnych 001–005 do aktualnego SHA; dodano snapshoty `review/sequential/685-685.json` i `review/legal-clauses/685-685.json`; zaktualizowano ledger, manifesty, mapę kompetencji, lekcję i materiał instruktora.
- PR i CI: do potwierdzenia po otwarciu PR. Nie uruchomiono lokalnego Quality Gate.

## Pliki audytowe

- Rejestr: `review/specialist/REJESTR-0685-0685.md`
- Ledger: `review/legal-polish/stage4w4-literal-verification-ledger-0610-0678.json`
- Snapshot sekwencyjny: `review/sequential/685-685.json`
- Snapshot prawny: `review/legal-clauses/685-685.json`
