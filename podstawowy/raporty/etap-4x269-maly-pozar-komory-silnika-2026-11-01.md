# Etap 4x269 — mały pożar komory silnika a pożar przedziału ładunkowego

Data: 01.11.2026  
Zakres: wyłącznie kurs podstawowy ADR  
Baza: main `db0da7918bfac87002bbf06075189d78b9530f5b`  
Gałąź: `stage4x269-small-fire-engine-compartment`  
Nowe ID: `ADR-B-0695`  
Kompetencja: `ADR-B-05-K05` — postępowanie przy pożarze pojazdu

## Wybór luki

Kompetencja miała cztery pytania (ADR-B-0107, 0166, 0222 i 0614). Wszystkie powtarzały zasadę, że członkowie załogi nie powinni gasić pożaru obejmującego przedział ładunkowy. Brakowało sytuacji sprawdzającej drugi, równie ważny element instrukcji pisemnych: przy małym lub początkowym pożarze opon, hamulców albo komory silnika można użyć gaśnicy, ale tylko jeśli jest to właściwe i bezpieczne.

## Dodane pytanie

- `ADR-B-0695`: mały, początkowy pożar w komorze silnika, bez objęcia przedziału ładunkowego.
- Klucz: **A** — użyć gaśnicy do małego pożaru, jeśli jest to właściwe i bezpieczne.
- Explanation: **398 znaków, 5 zdań**; najpierw praktyczny sens wyjątku, następnie pułapki w odpowiedziach i podstawa ADR.
- Długości A/B/C: **75/75/59** znaków; poprawna A nie jest jedyną najdłuższą.
- Audyt A/B/C: A — poprawna, bo odpowiada ograniczonemu zezwoleniu z instrukcji; B — błędna, bo bezpodstawnie rozszerza zakaz na wszystkie pożary pojazdu; C — błędna, bo pomija warunek właściwości i bezpieczeństwa.
- Status: `needs_review`; nic nie oznaczono jako `verified`.

## Podstawa prawna — źródło oficjalne sprawdzone

- **ADR 2025, 5.4.3.4**, model instrukcji pisemnych, tom II, s. 270 (PDF s. 281): jeżeli jest to właściwe i bezpieczne, użyć gaśnic do małego lub początkowego pożaru opon, hamulców lub przedziału silnika; członkowie załogi nie powinni gasić pożaru obejmującego przedział ładunkowy.
- Oficjalny polski tekst ADR 2025, Ministerstwo Infrastruktury: https://www.gov.pl/attachment/b7292c03-ac9d-4f80-9a29-c22f53d847b8
- Dz.U. 2025 poz. 642: https://dziennikustaw.gov.pl/DU/2025/642
- UNECE ADR 2025: https://unece.org/adr-2025-files

Właściwy fragment punktu został sprawdzony w oficjalnym polskim tekście ADR 2025. Pełne porównanie wszystkich elementów pytania z tekstem Dz.U. oraz niezależna recenzja specjalisty pozostają pending.

## Synchronizacja #646

- Bank po dodaniu: **695** pytań, ADR-B-0001–0695; SHA banku: `c9127a1fe91f03222089a434d5ec51f11f3b4e8a`.
- Kompetencja `ADR-B-05-K05` otrzymała piąte pytanie.
- Klucze i warianty egzaminów próbnych 001–005 wymagają odświeżenia do nowego SHA banku.
- Snapshoty: `review/sequential/695-695.json`, `review/legal-clauses/695-695.json`; ledger, indeks specjalisty i manifest pakietu dołączone.
- Rozkład prawidłowych odpowiedzi po dodaniu: A=237/B=240/C=218.
- Globalny wskaźnik „poprawna = jedyna najdłuższa”: **72/695 = 10,36%**.
- Quality Gate i pełne CI pozostają do potwierdzenia na PR. Lokalnego Quality Gate nie uruchamiano.

## Audyt A/B/C

| Opcja | Ocena | Uzasadnienie |
|---|---|---|
| A | Poprawna | ADR dopuszcza gaszenie małego lub początkowego pożaru komory silnika, jeśli jest to właściwe i bezpieczne. |
| B | Błędna | Instrukcje nie ustanawiają całkowitego zakazu użycia gaśnicy w każdym pożarze pojazdu. |
| C | Błędna | Nie wolno ignorować warunku bezpieczeństwa i rozpoczynać gaszenia bez oceny sytuacji. |

Raport nie stanowi niezależnej akceptacji prawnej ani zatwierdzenia pytania.
