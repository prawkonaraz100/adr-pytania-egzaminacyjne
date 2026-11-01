# Etap 4x260 — przenośna lampa dla każdego członka załogi

Data: 01.11.2026  
Zakres: wyłącznie kurs podstawowy ADR  
Baza: main `b06e708766ca5b2e15698cd10c1283edfffab7fb`  
Nowe ID: `ADR-B-0686`  
Kompetencja: `ADR-B-08-K05` — kamizelki i latarki dla członków załogi

## Wybór luki

ADR-B-08-K05 miała cztery pytania, ale wszystkie dotyczyły kamizelek ostrzegawczych. Nie było w niej pytania o drugi element wskazany w nazwie kompetencji — przenośną lampę. Uzupełniono lukę o wymaganą liczbę lamp: jedna dla każdego członka załogi. Odrębny warunek dotyczący powierzchni metalowej mogącej powodować iskrzenie wynika z ADR 8.3.4 i nie jest przedmiotem tego pytania (ten aspekt ma osobny rekord ADR-B-0663).

## Dodane pytanie

- `ADR-B-0686`: podczas kontroli w pojeździe są dwie osoby załogi, ale tylko jedna przenośna lampa.
- Klucz: **A** — przenośna lampa musi być dostępna dla każdego członka załogi; przy dwóch osobach potrzebne są dwie sztuki.
- Explanation: **361 znaków, 5 zdań**; tłumaczy praktyczny wymóg liczby lamp i wyjaśnia, dlaczego jedna wspólna lampa lub wyposażenie tylko kierowcy nie wystarczają.
- Długości odpowiedzi A/B/C: **109/123/92** znaków. Poprawna A nie jest ani najdłuższa, ani najkrótsza.
- Status: `needs_review`; nie zmieniono statusu żadnego pytania na `verified`.

## Podstawa prawna i ograniczenia

- **ADR 2025, 8.1.5.2** — przenośna lampa zgodna z 8.3.4 dla każdego członka załogi pojazdu.
- Źródło prawa: Dz.U. 2025 poz. 642: https://dziennikustaw.gov.pl/DU/2025/642
- Oficjalny tekst polski ADR tom II 2025, Ministerstwo Infrastruktury: https://www.gov.pl/attachment/b7292c03-ac9d-4f80-9a29-c22f53d847b8

Pytanie bada wyłącznie liczbę lamp z 8.1.5.2; nie powtarza pytania ADR-B-0663 o właściwości materiału lampy z 8.3.4. Pełne literalne porównanie z właściwym tekstem Dz.U. oraz niezależna recenzja specjalisty pozostają pending. Pytanie pozostaje `needs_review`.

## Synchronizacja #646

- Bank: **686** pytań ADR-B-0001–0686; wszystkie `needs_review`, 0 `verified`.
- Blob SHA `questions.jsonl`: `f44c2fdc0e99ccbb1311d61b7b4bc2dadf1a907d`.
- Rozkład prawidłowych opcji: **A=235 / B=234 / C=217**.
- „Poprawna = jedyna najdłuższa”: **72/686 = 10,50%**, poniżej limitu Quality Gate 18%.
- `ADR-B-08-K05` ma teraz 5 pytań; moduł ADR-B-08 ma 44 pytania.
- Zaktualizowano klucze i warianty egzaminów próbnych 001–005 do aktualnego SHA; odświeżono snapshoty `review/sequential/686-686.json` i `review/legal-clauses/686-686.json`; zaktualizowano ledger, manifesty, mapę kompetencji, lekcję i materiał instruktora.
- PR i CI: do potwierdzenia po otwarciu PR. Nie uruchomiono lokalnego Quality Gate.

## Pliki audytowe

- Rejestr: `review/specialist/REJESTR-0686-0686.md`
- Ledger: `review/legal-polish/stage4w4-literal-verification-ledger-0610-0678.json`
- Snapshot sekwencyjny: `review/sequential/686-686.json`
- Snapshot prawny: `review/legal-clauses/686-686.json`
