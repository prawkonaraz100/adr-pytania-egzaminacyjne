# Etap 4x291 — ochrona gaśnicy przed pogodą (ADR-B-0717)

Data: 02.11.2026  
Zakres: wyłącznie kurs podstawowy ADR  
Gałąź: `stage4x291-extinguisher-weather-protection`  
Punkt wyjścia: main `b972e66ad19b6fc197feb18aff952d6f670c193b`  
Nowy identyfikator: `ADR-B-0717`

## Luka w pokryciu
Kompetencja ADR-B-05-K13 (praktyczne używanie gaśnicy) miała 4 przypisane pytania. Dodano ćwiczenie kontroli osłony gaśnicy zamocowanej na zewnątrz pojazdu. Wcześniejsze pytania weryfikowały rodzaj pożaru, dostępność oraz konieczność ćwiczeń, ale nie stawiały jednocześnie wymagań dotyczących pogody i szybkiego dostępu.

## Audyt A/B/C
- Klucz C: zapewnić ochronę przed wpływem pogody i nie utrudniać dostępu załogi.
- A: nieprawidłowo pomija wymóg ochrony przed pogodą.
- B: błędnie przedkłada zamknięcie gaśnicy w schowku na klucz nad łatwy dostęp.
- Długości A/B/C: 108/106/103 znaków — poprawna C **nie jest najdłuższa**.
- Explanation: 408 znaków, 4 zdania, dla początkującego kursanta.
- Rozkład odpowiedzi po dodaniu: A 239, B 257, C 221. Wskaźnik najdłuższej poprawnej: 76/717 = **10,60%** (limit 18%, CI egzekwuje 16%); maksimum działu 13,95%.

## Podstawa prawna
- ADR 2025, 8.1.4.5: gaśnice łatwo dostępne dla załogi i chronione przed skutkami pogody, aby nie pogorszyć ich bezpieczeństwa działania.
- ADR 2025, 8.2.2.3.8: indywidualne ćwiczenia praktyczne obejmują gaszenie pożaru.
- Oficjalny tekst polski: https://eli.gov.pl/api/acts/DU/2025/642/text.pdf
- UNECE: https://unece.org/info/Transport/pub/395786

## Status i synchronizacja
Pytanie pozostaje `needs_review`; niezależna recenzja specjalisty i pełne literalne porównanie polskiego tekstu ADR są nadal otwarte. Nic nie oznaczono jako `verified`.

- Bank po zmianie: 717 pytań; wszystkie `needs_review`, 0 `verified`.
- Git blob SHA `questions.jsonl`: `f171a97a6d4a62812ba8ae399ec9d063902a1ee9`.
- Klucze i warianty egzaminów 001–005, snapshoty sequential/legal, ledger źródeł, rejestr, manifesty oraz metryki muszą odpowiadać temu blobowi.
- Wynik Quality Gate zostanie wpisany do Issue #10 po PASS CI.
