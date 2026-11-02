# Etap 4x284 — dobór wyposażenia według numerów nalepek zagrożenia

Data: 02.11.2026  
Zakres: wyłącznie kurs podstawowy ADR  
Baza: main `b3c9069ace8715584519a709df42d9239d2413dd`  
Gałąź: `stage4x284-equipment-check-before-transport`  
Nowe ID: `ADR-B-0710`  
Kompetencja: `ADR-B-08-K07` — wyposażenie dobierane z uwzględnieniem nalepek zagrożenia

## Wybór luki

W module wyposażenia pojazdu brakowało sytuacyjnego sprawdzenia samej metody doboru wyposażenia. Dotychczasowe pytania skupiały się na konkretnych elementach, np. masce ucieczkowej lub łopacie. Nowe pytanie sprawdza, czy kierowca potrafi odczytać numery nalepek zagrożenia z dokumentu przewozowego i na tej podstawie dobrać wymagane wyposażenie ogólne i ochronne, zamiast zakładać jeden stały zestaw dla każdego przewozu.

## Podstawa prawna

ADR 2025, 8.1.5.1 stanowi, że wyposażenie ogólne i ochronne dobiera się odpowiednio do numerów nalepek zagrożenia towarów przewożonych; numery nalepek można ustalić na podstawie dokumentu przewozowego. Wykaz wyposażenia znajduje się w 8.1.5.2. Źródło aktu: Dz.U. 2025 poz. 642. Pomocniczy oficjalny tekst ADR 2025 publikuje Ministerstwo Infrastruktury. Pełne literalne porównanie z tekstem urzędowym i niezależna recenzja specjalisty pozostają wymagane.

## Dodane pytanie

- `ADR-B-0710`: przed wyjazdem kierowca ustala wymagany zestaw wyposażenia na podstawie numerów nalepek w dokumencie przewozowym.
- Kompetencja: `ADR-B-08-K07`.
- Klucz: **C** — odczytać numery nalepek i dobrać wyposażenie według wykazu ADR.
- Explanation: **373 znaki**, 4 zdania; najpierw praktyczny sens, potem wyjaśnienie mylących odpowiedzi, na końcu podstawa ADR.
- Długości A/B/C: **121/132/117** znaków; poprawna odpowiedź nie jest najdłuższa.
- Audyt A/B/C: A — pomija numery nalepek i sprowadza dobór do nazwy/klasy głównej; B — błędnie zakłada jeden stały zestaw; C — odpowiada metodzie z ADR 8.1.5.1 i wykazowi 8.1.5.2.
- Status: `needs_review`; nic nie oznaczono jako `verified`.

## Migawka banku i synchronizacja #646

- Blob SHA `podstawowy/questions.jsonl`: `40abca10d9e69a22bdc13523124ca00c43fb5236`.
- Bank: 710 rekordów; wszystkie `needs_review`, 0 `verified`.
- Rozkład prawidłowych odpowiedzi po dodaniu C: A=238, B=252, C=220.
- „Poprawna = jedyna najdłuższa”: 75/710 = **10,56%** (poniżej limitu 18%).
- Klucze i warianty egzaminów próbnych 001–005 zsynchronizowano z SHA banku.
- Snapshoty audytu sekwencyjnego i przeglądu klauzul: `review/sequential/710-710.json`, `review/legal-clauses/710-710.json`.
- Statusy pozostają robocze; niezależna recenzja ADR nadal wymagana.

## Kontrole przed PR

Sprawdzić w CI: unikalność i ciągłość ID 0001–0710; zgodność mapy kompetencji i liczników; explanation co najmniej 200 znaków; rozkład A/B/C i wskaźnik „poprawna = najdłuższa” nie większy niż 18%; aktualność kluczy 001–005, snapshotów i SHA pakietów recenzyjnych.

