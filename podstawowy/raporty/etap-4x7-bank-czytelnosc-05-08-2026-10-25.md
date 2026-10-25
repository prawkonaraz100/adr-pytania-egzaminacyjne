# Etap 4x7 — kontrola banku i czytelności, partia B-05–08

## Punkt wyjścia
- Świeży `main`: `f4b0d4f140a6a07cbe1e507e640f81bf098f6301`.
- Sprawdzono 178 pytań przypisanych do modułów ADR-B-05–08 w całym banku 609 rekordów. ID pozostają bez zmian, żaden status nie został podniesiony do `verified`.

## Potwierdzony duplikat i poprawka
- `ADR-B-0169` i `ADR-B-0585` sprawdzały praktycznie tę samą sytuację: gaśnica zasłonięta ładunkiem i brak szybkiego dostępu.
- Zachowano oba ID. Przeredagowano `ADR-B-0585`, by sprawdzało inny aspekt tej samej podstawy: luźne mocowanie gaśnicy i ochronę przed uszkodzeniem podczas jazdy. Zmieniono sytuację, dystraktory i explanation; poprawna odpowiedź nadal ma klucz B, ale nie jest jedyną najdłuższą.
- Podstawa wskazana w rekordzie: ADR 8.1.4.5. Zmiana jest redakcyjna; nie stanowi potwierdzenia prawnej poprawności przez specjalistę.
- Para została usunięta z allowlisty bramki podobieństwa. Po zmianie skan nie wykrywa już tej pary jako niemal identycznej.

## Czytelność explanation
- Rozwinięto skróty w 17 istniejących wyjaśnieniach przypisanych do B-05–08; wraz z przebudowanym explanation pytania `ADR-B-0585` dotknięto 18 rekordów:
  `ADR-B-0016`, `ADR-B-0071`, `ADR-B-0115`, `ADR-B-0188`, `ADR-B-0190`, `ADR-B-0255`, `ADR-B-0256`, `ADR-B-0257`, `ADR-B-0298`, `ADR-B-0417`, `ADR-B-0418`, `ADR-B-0419`, `ADR-B-0420`, `ADR-B-0507`, `ADR-B-0547`, `ADR-B-0562`, `ADR-B-0583`, `ADR-B-0585`.
- Zmiany dodają proste objaśnienia terminów (m.in. numer UN, DMC, LQ/EQ), zachowując sens odpowiedzi i krótką podstawę ADR.
- Synchronizowano wyjaśnienia, klucze i źródła w wariantach/kluczach egzaminów 001–005 tam, gdzie dotyczyły zmienionych pytań. Odświeżono snapshoty w obu rejestrach audytowych, bez zmiany ich statusów lub deklaracji o recenzji prawnej.

## Kontrola podobieństw
- `ADR-B-0071` / `ADR-B-0072` pozostają udokumentowaną parą podobnych pytań: dotyczą różnych progów DMC (3,5 t i 6 t), więc sprawdzają odrębne wartości tabeli ADR.
- `ADR-B-0330` / `ADR-B-0337` są opisane jako podobne pytania o odrębne wyłączenia proceduralne (klasy 5.2 i 6.2).
- Nie znaleziono nowej nieudokumentowanej pary o podobieństwie co najmniej 0,60 ani identycznych zestawach odpowiedzi w jednym module.

## Kontrole przed PR
- Bank: 609 pytań, 609 unikalnych ID, 0 duplikatów ID.
- Poprawna odpowiedź jest jedyną najdłuższą: 82/609 = 13,46% (limit 18%).
- Najkrótsze explanation: 300 znaków; poniżej 200: 0.
- Statusy: 609 `needs_review`, 0 `verified`.
- Warianty 001–005: pola pytań i klucze synchronizowane z aktualnym bankiem; Quality Gate CI sprawdza spójność.

## Ograniczenia
To przegląd redakcyjny i automatyczna kontrola podobieństwa, nie recenzja prawna. Pytania pozostają `needs_review`; wymagają niezależnej oceny specjalisty ADR.
