# Etap 4x290 — zrozumienie instrukcji pisemnych przez całą załogę (ADR-B-0716)

Data: 02.11.2026  
Zakres: wyłącznie kurs podstawowy ADR  
Gałąź: stage4x290-written-instructions-understanding  
Punkt wyjścia: main 4e296a095f4c621cb7dc00a125668c5213bf8610  
Nowy identyfikator: ADR-B-0716

## Luka i uzasadnienie
Kompetencja ADR-B-05-K01 („Lokalizacja i znajomość instrukcji pisemnych”) miała 5 pytań. Dotychczasowe pozycje sprawdzały lokalizację instrukcji, zapoznanie się z nimi przed wyjazdem i wybór zrozumiałego języka. Brakowało jednak scenariusza, w którym kierowca potrafi przeczytać dokument, ale nie rozumie części poleceń, a przewoźnik błędnie uznaje samą obecność instrukcji w kabinie za wystarczającą.

## Treść i audyt A/B/C
- Sytuacja: przed wyjazdem kierowca nie rozumie części instrukcji pisemnych, a dyspozytor twierdzi, że dokument w kabinie wystarcza.
- Klucz: B — zgłosić problem przewoźnikowi i przed wyjazdem uzyskać instrukcje zrozumiałe dla każdego członka załogi.
- A: błędnie uznaje samą obecność dokumentu za wystarczającą i odkłada wyjaśnienie do awarii.
- C: błędnie traktuje ustne streszczenie jako zastępstwo pełnych instrukcji.
- Długości A/B/C: 105/104/102 znaków; klucz B nie jest najdłuższy.
- Explanation: 421 znaków, 4 zdania; wyjaśnia odpowiedzialność przewoźnika i obowiązek przygotowania przed podróżą.

## Podstawa prawna
- ADR 2025, 5.4.3.2 — przewoźnik przekazuje instrukcje w języku, który każdy członek załogi może przeczytać i zrozumieć, oraz zapewnia, że rozumie je i potrafi prawidłowo zastosować.
- ADR 2025, 5.4.3.3 — przed rozpoczęciem przewozu załoga zapoznaje się z przewożonymi towarami i sprawdza w instrukcjach działania na wypadek wypadku lub zagrożenia.
- Oficjalny tekst: https://eli.gov.pl/api/acts/DU/2025/642/text.pdf
- UNECE — wersje językowe ADR i instrukcje pisemne: https://unece.org/transport/road-transport/linguistic-versions-adr-instructions-writing

## Status i ograniczenia
Pytanie pozostaje `needs_review`. Podstawa została przypisana do konkretnych punktów ADR 2025, ale pełne literalne porównanie polskiego tekstu i niezależna recenzja specjalisty pozostają otwarte. Nic nie oznaczono jako `verified`.

## Metryki i synchronizacja
Bank: 716 pytań; wszystkie `needs_review`, 0 `verified`. SHA banku: `ca5eb4b1d8f82eed5081887537980076600b51f3`. Rozkład A/B/C: 239/257/220. Poprawna = jedyna najdłuższa: 76/716 = 10,61%; maksimum modułu: 13,95% (limit 18%). Klucze/warianty 001–005, snapshoty sequential/legal 716-716, ledger, manifest, indeks specjalisty i testy zostaną zsynchronizowane przed PR.
