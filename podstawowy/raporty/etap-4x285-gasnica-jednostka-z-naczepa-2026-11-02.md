# Etap 4x285 — gaśnica dla jednostki transportowej z naczepą

Data: 02.11.2026  
Zakres: wyłącznie kurs podstawowy ADR  
Baza: main po PR #755, commit `718548eccb525f2acff935fd9c84bdaa910772d0`  
Gałąź: `stage4x285-fire-extinguisher-per-transport-unit`  
Nowe ID: `ADR-B-0711`  
Kompetencja: `ADR-B-08-K02` — gaśnica przy 1.1.3.6

## Wybór luki

W kompetencji były cztery pytania o minimalną gaśnicę przy wyłączeniu 1.1.3.6, ale nie sprawdzały rozróżnienia między całą jednostką transportową a jej elementami. Nowe pytanie używa sytuacji ciągnika z naczepą i sprawdza, czy kursant potrafi zastosować minimum z 8.1.4.2 do zestawu jako jednej jednostki, zamiast automatycznie wymagać osobnej gaśnicy w każdym elemencie albo błędnie uznać, że wyłączenie zwalnia z gaśnicy.

## Podstawa prawna

ADR 1.2.1 definiuje jednostkę transportową jako pojazd silnikowy bez przyczepy albo połączenie pojazdu silnikowego z jedną lub większą liczbą przyczep. ADR 8.1.4.2 wymaga dla jednostki transportowej przewożącej towary zgodnie z 1.1.3.6 co najmniej jednej przenośnej gaśnicy o minimalnej pojemności 2 kg proszku lub równoważnej pojemności innego odpowiedniego środka. Źródło: Dz.U. 2025 poz. 642. Literalne porównanie i niezależna recenzja specjalisty pozostają wymagane.

## Dodane pytanie

- `ADR-B-0711`: ciągnik z dołączoną naczepą, przewóz na warunkach 1.1.3.6, jedna sprawna i dostępna gaśnica 2 kg w ciągniku.
- Kompetencja: `ADR-B-08-K02`.
- Klucz: **B** — ciągnik z naczepą stanowi jedną jednostkę transportową, dla której minimum wynosi jedną gaśnicę.
- Explanation: **382 znaki**, 4 zdania; praktyczne znaczenie, pułapki w błędnych odpowiedziach, podstawa ADR na końcu.
- Długości A/B/C: **157/119/103**; poprawna B nie jest najdłuższa.
- Audyt A/B/C: A błędnie traktuje ciągnik i naczepę jako dwie jednostki; B stosuje definicję 1.2.1 i minimum 8.1.4.2; C błędnie twierdzi, że 1.1.3.6 znosi obowiązek gaśnicy.
- Status: `needs_review`; nic nie oznaczono jako `verified`.

## Migawka banku i synchronizacja #646

- Blob SHA `podstawowy/questions.jsonl`: `daa0a72906bb1ca4b6ea0724c4c8078126d3ce04`.
- Bank: 711 pytań; wszystkie `needs_review`, 0 `verified`.
- Rozkład prawidłowych odpowiedzi: A=238, B=253, C=220.
- „Poprawna = jedyna najdłuższa”: 75/711 = **10,55%** (poniżej limitu 18%).
- ADR-B-08-K02 ma 5 pytań; moduł ADR-B-08 ma 48 pytań.
- Klucze i warianty egzaminów 001–005 należy zsynchronizować z nowym SHA.
- Snapshoty audytu sekwencyjnego i przeglądu klauzul: `review/sequential/711-711.json`, `review/legal-clauses/711-711.json`.
- Pełne porównanie literalne i niezależna recenzja ADR pozostają otwarte.

## Kontrole przed PR

CI musi potwierdzić ciągłość i unikalność ID 0001–0711; mapę kompetencji i liczniki; explanation minimum 300 znaków; rozkład A/B/C i limit długości poprawnej odpowiedzi; brak duplikatów; klucze 001–005; snapshoty 711-711; ledger, manifesty i SHA.
