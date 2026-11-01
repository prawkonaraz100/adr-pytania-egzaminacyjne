# Etap 4x258 — wyjątek CV28 dla całkowicie przykrytych przesyłek

Data: 01.11.2026  
Zakres: wyłącznie kurs podstawowy ADR  
Baza: main `72c5f60ceb24b7f99fd048ccef08cc934a67ed47`  
Nowe ID: `ADR-B-0684`  
Kompetencja: `ADR-B-09-K03` — kontakt z żywnością i paszami

## Wybór luki

W mapie kompetencji ADR-B-09-K03 miała cztery pytania, podobnie jak 31 innych kompetencji w całej mapie. Wybrano ją jako jedną z najsłabiej reprezentowanych, ponieważ dotychczasowe pytania obejmowały CV28, warunki bliskości, metody oddzielenia i odstęp 0,8 m, ale nie sprawdzały osobno wyjątku dla przesyłek mających dodatkowe opakowanie lub całkowicie przykrytych. Temat nie był przedmiotem partii 4x227–4x257.

## Dodane pytanie

- `ADR-B-0684`: sytuacja załadunku przesyłek objętych CV28 blisko żywności, gdy każda przesyłka jest całkowicie przykryta.
- Klucz: **C** — ADR 7.5.4 przewiduje wyjątek od wskazanych sposobów oddzielenia, gdy przesyłki mają dodatkowe opakowanie lub są całkowicie przykryte.
- Explanation: **401 znaków, 4 zdania**; wyjaśnia praktyczny sens, wyjątek, błąd dystraktora A i nieprawidłowość polegania na adnotacji w dokumencie (B).
- Długości odpowiedzi A/B/C: **152/121/126** znaków. Poprawna C nie jest ani najdłuższa, ani najkrótsza.
- Status: `needs_review`; brak zmiany jakiegokolwiek statusu na `verified`.

## Podstawa prawna i ograniczenia

- **ADR 2025, 7.5.4** — środki ostrożności wobec żywności, artykułów spożywczych i karmy; wyjątek, gdy wskazane przesyłki mają dodatkowe opakowanie lub są całkowicie przykryte.
- Źródło prawa: Dz.U. 2025 poz. 642: https://dziennikustaw.gov.pl/DU/2025/642
- Tekst ADR 2025 na portalu gov.pl: https://www.gov.pl/attachment/b4638c72-30e3-4bff-afd1-1b9ba4100e70

Kwestia dotyczy wyjątku od sposobów oddzielenia, nie znosi pozostałych obowiązków ADR ani potrzeby sprawdzenia CV28 w kolumnie 18 tabeli A. Pełne literalne porównanie z właściwą stroną Dz.U. i niezależna recenzja specjalisty pozostają pending. Pytanie pozostaje `needs_review`.

## Synchronizacja #646

- Bank: **684** pytań ADR-B-0001–0684; wszystkie `needs_review`, 0 `verified`.
- Blob SHA `questions.jsonl`: `c8c1f0779bba936b20d6a8f2c9dc8be80aa6fe69`.
- Rozkład prawidłowych opcji: **A=234 / B=233 / C=217**.
- „Poprawna = jedyna najdłuższa”: **72/684 = 10,53%**, poniżej Quality Gate 18%.
- `ADR-B-09-K03` ma teraz 5 pytań.
- Zaktualizowano klucze źródłowe egzaminów próbnych 001–005 i warianty 001–005 do aktualnego SHA; dodano snapshoty `review/sequential/684-684.json` oraz `review/legal-clauses/684-684.json`; zaktualizowano mapę kompetencji, lekcję, materiał instruktora i manifest pakietu recenzyjnego.
- PR i CI: do potwierdzenia po otwarciu PR. Nie uruchomiono lokalnego Quality Gate.
