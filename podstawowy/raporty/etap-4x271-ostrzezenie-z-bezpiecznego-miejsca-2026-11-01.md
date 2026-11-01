# Etap 4x271 — ostrzeżenie osób postronnych bez wchodzenia w rozlew

Data: 01.11.2026  
Zakres: wyłącznie kurs podstawowy ADR  
Baza: main `7b6dd9356635e0202d414cb76334c12f2d9170e9`  
Gałąź: `stage4x271-safe-warning-from-distance`  
Nowe ID: `ADR-B-0697`  
Kompetencja: `ADR-B-05-K09` — ostrzeganie osób postronnych i trzymanie ich z dala od zagrożenia

## Wybór luki

Kompetencja miała cztery pytania (ADR-B-0111, 0186, 0224 i 0632), które powtarzały ogólny obowiązek ostrzegania osób postronnych i niedopuszczania ich do przesyłek. Brakowało sytuacji, w której kierowca widzi ludzi zbliżających się do uszkodzonego ładunku, ale bezpośrednia droga do nich prowadzi przez rozlew. Nowe pytanie sprawdza połączenie dwóch instrukcji: ostrzeżenia ludzi z bezpiecznego miejsca oraz zakazu dotykania rozlewu i przechodzenia przez niego.

## Dodane pytanie

- `ADR-B-0697`: dwie osoby idą w stronę uszkodzonej przesyłki, a droga podejścia kierowcy przecina rozlew.
- Klucz: **B** — ostrzec ludzi z bezpiecznego miejsca, aby odeszli od zagrożenia, i nie przechodzić przez rozlew.
- Explanation: **400 znaków, 4 zdania**; wyjaśnia praktyczną decyzję, ryzyko błędnych działań i podstawę ADR.
- Długości A/B/C: **108/95/73** znaków; poprawna B jest pośrodku — nie jest ani najdłuższa, ani najkrótsza.
- Audyt A/B/C: A — błędna, bo wymaga przejścia przez rozlew; B — poprawna, bo pozwala ostrzec ludzi bez wchodzenia w strefę zagrożenia; C — błędna, bo osoby postronne należy trzymać z dala od strefy zagrożenia nawet wtedy, gdy obiecują nie dotykać przesyłki.
- Status: `needs_review`; nic nie oznaczono jako `verified`.

## Podstawa prawna — źródło oficjalne sprawdzone

- **ADR 2025, 5.4.3.4**, model instrukcji pisemnych, tom II, s. 270 (PDF s. 281): ostrzec inne osoby i ruch drogowy o zagrożeniu oraz trzymać je z dala od strefy zagrożenia; nie dotykać rozlewów ani przez nie nie przechodzić. Czynności wykonuje się z uwzględnieniem warunku, że muszą być możliwe i bezpieczne.
- Oficjalny polski tekst ADR 2025, Ministerstwo Infrastruktury: https://www.gov.pl/attachment/b7292c03-ac9d-4f80-9a29-c22f53d847b8
- Dz.U. 2025 poz. 642: https://dziennikustaw.gov.pl/DU/2025/642
- UNECE ADR 2025: https://unece.org/adr-2025-files

Właściwe fragmenty punktu zostały sprawdzone bezpośrednio w oficjalnym polskim tekście ADR 2025. Pełne porównanie wszystkich elementów pytania z tekstem Dz.U. oraz niezależna recenzja specjalisty pozostają pending.

## Synchronizacja #646

- Bank po dodaniu: **697** pytań, ADR-B-0001–0697; SHA banku: `1821851aee9c83c4b4e3197aa3e59594b93bb513`.
- Kompetencja `ADR-B-05-K09` otrzymała piąte pytanie.
- Klucze i warianty egzaminów próbnych 001–005 wymagają odświeżenia do nowego SHA banku.
- Snapshoty: `review/sequential/697-697.json`, `review/legal-clauses/697-697.json`; ledger, indeks specjalisty i manifest pakietu dołączone.
- Rozkład prawidłowych odpowiedzi po dodaniu: A=237/B=241/C=219.
- Globalny wskaźnik „poprawna = jedyna najdłuższa”: **72/697 = 10,33%**; maksimum działu pozostaje 13,95%.
- Quality Gate i pełne CI pozostają do potwierdzenia na PR. Lokalnego Quality Gate nie uruchamiano.

## Audyt A/B/C

| Opcja | Ocena | Uzasadnienie |
|---|---|---|
| A | Błędna | Kierowca przechodzi przez rozlew, choć ADR zabrania przez niego przechodzić. |
| B | Poprawna | Ostrzega ludzi z bezpiecznego miejsca i nie wchodzi w rozlew. |
| C | Błędna | Nawet osoby, które nie dotykają opakowania, trzeba trzymać z dala od strefy zagrożenia. |

Raport nie stanowi niezależnej akceptacji prawnej ani zatwierdzenia pytania.
