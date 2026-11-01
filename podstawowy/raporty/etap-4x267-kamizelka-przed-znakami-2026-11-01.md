# Etap 4x267 — kamizelka przed ustawieniem znaków ostrzegawczych

Data: 01.11.2026  
Zakres: wyłącznie kurs podstawowy ADR  
Baza: main `57787a4cccaf2f48a25f89a2d6a5bbe1b6887399`  
Gałąź: `stage4x267-warning-vest-before-signs`  
Nowe ID: `ADR-B-0693`  
Kompetencja: `ADR-B-05-K10` — kamizelka i znaki ostrzegawcze

## Wybór luki

Kompetencja miała cztery pytania. Istniejące pozycje sprawdzały głównie obowiązek użycia kamizelki i znaków albo warunek bezpieczeństwa, ale nie sprawdzały praktycznego przygotowania kierowcy przed podejściem do miejsca, w którym ustawi znaki. Nowe pytanie koncentruje się na założeniu kamizelki przed opuszczeniem bezpiecznej strefy kabiny i podejściem do jezdni.

## Dodane pytanie

- `ADR-B-0693`: kierowca po bezpiecznym zatrzymaniu może wyjść z kabiny i ustawić stojące znaki ostrzegawcze.
- Klucz: **B** — założyć kamizelkę ostrzegawczą, a potem odpowiednio ustawić stojące znaki, jeśli jest to bezpieczne.
- Explanation: **344 znaki, 4 zdania**; wyjaśnia praktyczny sens kamizelki, warunek bezpieczeństwa i mylące odpowiedzi.
- Długości A/B/C: **103/100/63** znaki; poprawna B nie jest ani najdłuższa, ani najkrótsza.
- Audyt A/B/C: A — błędna, bo kierowca wychodzi bez kamizelki; B — poprawna, bo odtwarza czynności z instrukcji pisemnych przy zachowaniu warunku bezpieczeństwa; C — błędna, bo światła awaryjne nie zastępują stojących znaków, gdy można je bezpiecznie ustawić.
- Status: `needs_review`; nic nie oznaczono jako `verified`.

## Podstawa prawna — źródło oficjalne sprawdzone

- **ADR 2025, 5.4.3.4**, model instrukcji pisemnych, tom II, s. 270 (PDF s. 281): załoga ma założyć kamizelkę ostrzegawczą i odpowiednio umieścić stojące znaki ostrzegawcze, jeżeli jest to możliwe i bezpieczne.
- Oficjalny polski tekst ADR 2025, Ministerstwo Infrastruktury: https://www.gov.pl/attachment/b7292c03-ac9d-4f80-9a29-c22f53d847b8
- Dz.U. 2025 poz. 642: https://dziennikustaw.gov.pl/DU/2025/642
- UNECE ADR 2025: https://unece.org/adr-2025-files

Właściwy fragment punktu został sprawdzony bezpośrednio w oficjalnym polskim PDF. Pełne porównanie wszystkich elementów pytania z tekstem Dz.U. oraz niezależna recenzja specjalisty pozostają pending.

## Synchronizacja #646

- Bank po dodaniu: **693** pytań, ADR-B-0001–0693; SHA banku zostanie wpisany po zatwierdzeniu commitu.
- Kompetencja `ADR-B-05-K10` otrzymała piąte pytanie.
- Klucze i warianty egzaminów próbnych 001–005 wymagają odświeżenia do nowego SHA banku.
- Snapshoty: `review/sequential/693-693.json`, `review/legal-clauses/693-693.json`; ledger, indeks specjalisty i manifest pakietu dołączone.
- Rozkład prawidłowych odpowiedzi po dodaniu: A=236/B=239/C=218.
- Globalny wskaźnik „poprawna = jedyna najdłuższa”: **72/693 = 10,39%**; maksimum działu pozostaje 13,95%.
- Quality Gate i pełne CI pozostają do potwierdzenia na PR. Lokalnego Quality Gate nie uruchamiano.

## Audyt A/B/C

| Opcja | Ocena | Uzasadnienie |
|---|---|---|
| A | Błędna | Kierowca podchodzi do miejsca ustawienia znaków bez kamizelki ostrzegawczej. |
| B | Poprawna | Najpierw zwiększa własną widoczność, a następnie ustawia znaki, jeśli jest to bezpieczne. |
| C | Błędna | Same światła awaryjne nie zastępują stojących znaków ostrzegawczych. |

Raport nie stanowi niezależnej akceptacji prawnej ani zatwierdzenia pytania.
