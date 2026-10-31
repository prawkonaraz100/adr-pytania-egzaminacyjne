# Etap 4x257 — zgodność konstrukcji opakowań przy piętrzeniu

Data: 01.11.2026  
Zakres: wyłącznie kurs podstawowy ADR  
Baza: main po PR #726, bank 682 pytań; nowy ID: ADR-B-0683  
Kompetencja: ADR-B-09-K05 — piętrzenie opakowań

## Dlaczego wybrano tę lukę

Kompetencja miała cztery pytania, które skupiały się na zakazie piętrzenia opakowań nieprzeznaczonych do tego celu oraz na uszkodzeniu lub uginaniu się dolnego opakowania. Brakowało osobnego sprawdzenia zgodności różnych konstrukcji opakowań, które są przeznaczone do piętrzenia, i roli elementów nośnych.

## Dodane pytanie

- **ADR-B-0683** — dwa różne typy opakowań są przeznaczone do piętrzenia; kursant ocenia zgodność ich wspólnego piętrzenia i wskazuje, kiedy zastosować elementy nośne.
- Klucz: **B** — należy uwzględnić zgodność różnych konstrukcji; gdy to potrzebne, elementy nośne mają chronić dolne opakowanie przed uszkodzeniem przez górne.
- Explanation: **394 znaki, 4 zdania**; wyjaśnia właściwą ocenę zgodności, warunek zastosowania elementów nośnych i błędy obu dystraktorów.
- Długości A/B/C: **176/174/162** znaków. Poprawna odpowiedź B nie jest ani najdłuższa, ani najkrótsza.
- Status: `needs_review`; niczego nie oznaczono jako `verified`.

## Podstawa prawna

- ADR 2025, **7.5.7.2** — opakowań nie piętrzy się, jeżeli nie są do tego przeznaczone; przy wspólnym piętrzeniu różnych konstrukcji trzeba uwzględnić ich wzajemną zgodność; w razie potrzeby stosuje się elementy nośne chroniące opakowanie poniżej.
- Źródło prawa: Umowa ADR 2025 ogłoszona w Dz.U. 2025 poz. 642: https://dziennikustaw.gov.pl/DU/2025/642 .
- Oficjalny tekst ADR 2025 UNECE: https://unece.org/adr-2025-files .

Dokładne literalne porównanie polskiego brzmienia 7.5.7.2 w pliku Dz.U. i niezależna recenzja specjalisty pozostają pending. Pytanie pozostaje `needs_review`.

## Synchronizacja #646 — stan po dodaniu pytania

- Bank: **683** pytań ADR-B-0001–0683; wszystkie `needs_review`, 0 `verified`.
- Blob SHA: `03382720e316001da10ddb968fb6c1956107bcef`.
- Rozkład prawidłowych opcji: A=234, B=233, C=216.
- „Poprawna = jedyna najdłuższa”: **72/683 = 10,54%**, poniżej Quality Gate 18%.
- B-09: 52 pytania; poprawna odpowiedź najkrótsza w 18/52 = 34,62%, poniżej 38%.
- Zaktualizowano mapę, lekcję i materiał instruktora B-09, snapshoty sequential/legal, ledger i rejestr recenzji. Synchronizacja egzaminów 001–005, kolejek i manifestów pakietu jest wykonywana w kolejnych commitach.
