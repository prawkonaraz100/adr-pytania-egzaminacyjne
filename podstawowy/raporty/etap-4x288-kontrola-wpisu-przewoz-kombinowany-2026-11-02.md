# Etap 4x288 — kontrola wpisu w dokumencie przewozowym (ADR-B-0714)

Data: 02.11.2026  
Zakres: wyłącznie kurs podstawowy ADR  
Gałąź: stage4x288-multimodal-transport-document-check  
Punkt wyjścia: main 67b57e8e3354ecdd4fefd4c22d6714b2d8e74742  
Nowy identyfikator: ADR-B-0714

## Luka i uzasadnienie
Kompetencja ADR-B-13-K06 („Dodatkowy wpis w transporcie kombinowanym”) miała 4 przypisane pytania, co było jednym z najniższych wyników w mapie. Dotychczasowe pytania sprawdzały głównie znajomość wymaganej formuły i ogólne warunki łańcucha morskiego lub lotniczego. Brakowało sytuacji, w której kierowca wykrywa brak wpisu przed rozpoczęciem odcinka drogowego i musi zareagować na prośbę nadawcy, by samodzielnie go dopisał.

## Treść i audyt A/B/C
- Sytuacja: brak adnotacji wymaganej przez 5.4.1.1.7; nadawca telefonicznie poleca kierowcy samodzielne dopisanie formuły.
- Klucz: A — wstrzymać rozpoczęcie przewozu, poprosić nadawcę o uzupełnienie dokumentu i ponownie sprawdzić go przed odjazdem.
- B: błędnie zakłada, że dokument IMDG automatycznie zastępuje wymagany wpis ADR.
- C: błędnie uznaje samo dopisanie formuły za potwierdzenie spełnienia warunków 1.1.4.2.1.
- Długości A/B/C: 119/110/119 znaków; odpowiedzi wyrównane, poprawna A nie jest jedyną najdłuższą.
- Explanation: 493 znaki, 5 zdań, język kursanta; rozróżnia kontrolę dokumentu od warunków zastosowania szczególnych zasad.

## Podstawa prawna
- ADR 2025, 1.1.4.2.1 — warunki przewozu w łańcuchu zawierającym przewóz morski lub lotniczy.
- ADR 2025, 1.4.2.2.1(b) i 1.4.2.2.3 — kontrola informacji w dokumencie przez przewoźnika oraz zakaz rozpoczęcia przewozu do czasu usunięcia stwierdzonych naruszeń.
- ADR 2025, 5.4.1.1.7 — dodatkowy wpis w dokumencie dla przewozu na warunkach 1.1.4.2.1.
- Oficjalny tekst: https://eli.gov.pl/api/acts/DU/2025/642/text.pdf

## Metryki banku po dodaniu pytania

- Bank: 714 pytań; wszystkie `needs_review`, 0 `verified`.
- SHA banku: `22c93b8abec0abd002fff821a873bde1776d0f56`.
- Rozkład odpowiedzi A/B/C: 239/255/220.
- Poprawna odpowiedź będąca jedyną najdłuższą: 76/714 = 10,64%; maksimum modułu: 13,95% (limit 18%).

## Status i ograniczenia
Pytanie pozostaje `needs_review`. Nie przeprowadzono pełnego literalnego porównania ani niezależnej recenzji specjalisty. Nic nie oznaczono jako `verified`.

## Synchronizacja i Quality Gate
Po zmianie banku odświeżone zostaną klucze i warianty egzaminu próbnego 001–005, snapshoty sequential/legal, ledger źródeł, manifesty, indeks specjalisty, metryki i asercje. Wynik Quality Gate zostanie odnotowany po CI PR.
