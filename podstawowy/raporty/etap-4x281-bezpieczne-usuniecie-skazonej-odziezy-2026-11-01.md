# Etap 4x281 — bezpieczne usunięcie skażonej odzieży i użytych środków ochronnych

Data: 01.11.2026  
Zakres: wyłącznie kurs podstawowy ADR  
Baza: main `3fc998c5535291deb44572218245acea0728fb71`  
Gałąź: `stage4x281-cleaning-before-reuse-same-substance`  
Nowe ID: `ADR-B-0707`  
Kompetencja: `ADR-B-05-K08` — skażona odzież i środki ochrony

## Wybór luki

Kompetencja miała cztery pytania, które skupiały się na rozpoznaniu skażonej odzieży i jej zdjęciu. Brakowało pytania sprawdzającego drugi element instrukcji pisemnych: zapewnienie bezpiecznego usunięcia skażonej odzieży oraz użytych skażonych środków ochronnych. Nowe pytanie nie narzuca konkretnej metody ani miejsca utylizacji, których ADR w tym punkcie nie określa.

## Dodane pytanie

- `ADR-B-0707`: po bezpiecznym oddaleniu się od miejsca awarii kierowca zdjął skażoną odzież i użyte środki ochronne; musi zdecydować, co z nimi zrobić.
- Klucz: **B** — dopilnować ich bezpiecznego usunięcia bez narażania innych i rozprzestrzeniania skażenia.
- Explanation: **372 znaki**, 4 zdania; praktyczne uzasadnienie, pułapki odpowiedzi i krótka podstawa ADR.
- Długości A/B/C: **98/102/103** znaków; długości wyrównane, poprawna B nie jest najdłuższa.
- Audyt A/B/C: A — zwykły kosz nie zapewnia bezpiecznego usunięcia; B — realizuje wymóg bezpiecznego usunięcia; C — pozostawienie skażonych rzeczy przy drodze naraża osoby postronne i nie zapewnia bezpiecznego usunięcia.
- Status: `needs_review`; nic nie oznaczono jako `verified`.

## Podstawa prawna

- ADR 2025, 5.4.3.4 — wzór instrukcji pisemnych, działania w razie wypadku lub awarii: zdjąć skażoną odzież i użyte skażone środki ochronne oraz zapewnić ich bezpieczne usunięcie.
- Oficjalny portal Ministerstwa Infrastruktury — ADR 2025, tom I i II: https://www.gov.pl/web/infrastruktura/towary-niebezpieczne
- Dz.U. 2025 poz. 642: https://dziennikustaw.gov.pl/DU/2025/642
- UNECE ADR 2025: https://unece.org/adr-2025-files

Zakres normatywny punktu 5.4.3.4 został zidentyfikowany w modelu instrukcji pisemnych. Pełne literalne porównanie polskiego tekstu oraz niezależna recenzja specjalisty pozostają pending.

## Synchronizacja #646

- Bank: 707 pytań ADR-B-0001–0707; wszystkie `needs_review`, 0 `verified`.
- Blob SHA banku: `d2eaa0b3df4ee50661e30cf62554ae5ca62ea408`.
- Klucze i warianty egzaminów próbnych 001–005 wskazują ten SHA.
- Snapshoty sequential/legal 707-707, rejestr źródeł, manifesty, indeksy i metryki odświeżane w tej gałęzi.
- Rozkład prawidłowych opcji A/B/C: 238/250/219.
- „Poprawna = jedyna najdłuższa”: 75/707 = 10,61%; maksimum modułu: 13,95%.
