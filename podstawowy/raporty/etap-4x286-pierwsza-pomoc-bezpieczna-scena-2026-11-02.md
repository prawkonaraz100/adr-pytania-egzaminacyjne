# Etap 4x286 — pierwsza pomoc po zabezpieczeniu miejsca zdarzenia

Data: 02.11.2026  
Zakres: wyłącznie kurs podstawowy ADR  
Baza: main po PR #756, commit `1815a446f563ea777e5f5cc2e5c0bef8ff6f47e1`  
Gałąź: `stage4x286-first-aid-safe-scene-assessment`  
Nowe ID: `ADR-B-0712`  
Kompetencja: `ADR-B-05-K11` — ocena bezpieczeństwa udzielania pierwszej pomocy

## Wybór luki

Mapa kompetencji wskazuje, że ADR-B-05-K11 ma 4 pytania — najmniej spośród kompetencji teoretycznych. Dotychczasowe pytania skupiają się przede wszystkim na tym, by nie wchodzić do skażonej strefy. Brakowało sytuacji, w której miejsce jest już zabezpieczone i kursant powinien rozpoznać, że może przejść do podstawowej pomocy. Nowe pytanie uzupełnia ten drugi etap, nie powtarzając jedynie zakazu wchodzenia w wyciek.

## Podstawa prawna i granice twierdzenia

ADR 2025, 8.2.2.3.2(e), wymienia w programie kursu podstawowego postępowanie po wypadku, w tym pierwszą pomoc. Ten punkt potwierdza, że pierwsza pomoc jest obowiązkowym tematem szkolenia kierowcy. Nie jest natomiast szczegółowym protokołem leczenia krwawiącej rany; czynności opatrzenia i ucisku przedstawiono jako podstawową treść dydaktyczną po potwierdzeniu bezpieczeństwa miejsca, a nie jako dosłowny nakaz techniczny ADR.

Źródło aktu: Dz.U. 2025 poz. 642. Oficjalne materiały polskie publikuje Ministerstwo Infrastruktury. Pełne literalne porównanie z tekstem aktu i niezależna recenzja specjalisty pozostają wymagane.

## Dodane pytanie

- `ADR-B-0712`: po kolizji miejsce jest zabezpieczone, nie ma wycieku ani oparów, a przytomny kolega ma krwawiącą ranę przedramienia.
- Kompetencja: `ADR-B-05-K11`.
- Klucz: **B** — rękawiczki, jałowy opatrunek i ucisk; przy silnym lub nieustającym krwawieniu wezwanie 112.
- Explanation: **439 znaków**, 4 zdania; praktyczne uzasadnienie, wyjaśnienie pułapek w dystraktorach i podstawa ADR na końcu.
- Długości A/B/C: **108/98/96**; poprawna B nie jest najdłuższa.
- Audyt A/B/C: A błędnie proponuje bezpośredni kontakt z krwią; B stosuje podstawowe czynności po potwierdzeniu bezpieczeństwa; C opóźnia pomoc i proponuje nieprzydatne podawanie jedzenia i napoju.
- Status: `needs_review`; nic nie oznaczono jako `verified`.

## Migawka banku i synchronizacja #646

- Blob SHA `podstawowy/questions.jsonl`: `634d7c00f27f7213b70c6aeab716230d0eaa24dc`.
- Bank: 712 pytań; wszystkie `needs_review`, 0 `verified`.
- Rozkład prawidłowych odpowiedzi: A=238, B=254, C=220.
- „Poprawna = jedyna najdłuższa”: 75/712 = **10,53%** (poniżej limitu 18%).
- Moduł ADR-B-05: 72 pytania; ADR-B-05-K11: 5 pytań.
- Klucze i warianty egzaminów 001–005 zsynchronizowano z nowym SHA.
- Snapshoty audytu sekwencyjnego i przeglądu klauzul: `review/sequential/712-712.json`, `review/legal-clauses/712-712.json`.
- Ledger, manifesty i indeks recenzji zaktualizowane; formalne zatwierdzenia: 0.

## Kontrole przed PR

CI musi potwierdzić ciągłość i unikalność ID 0001–0712; mapę kompetencji i liczniki; explanation minimum 300 znaków; rozkład A/B/C i limit długości poprawnej odpowiedzi; brak duplikatów; klucze 001–005; snapshoty 712-712; ledger, manifesty i SHA.
