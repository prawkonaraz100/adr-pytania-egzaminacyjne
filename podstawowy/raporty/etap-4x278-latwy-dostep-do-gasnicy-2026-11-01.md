# Etap 4x278 — łatwy dostęp do gaśnicy ADR

Data: 01.11.2026  
Zakres: wyłącznie kurs podstawowy ADR  
Baza: main `f1dfc58ceb94e9ba9f88da38d703640987a98824`  
Gałąź: `stage4x278-fire-extinguisher-accessibility-release`  
Nowe ID: `ADR-B-0704`  
Kompetencja: `ADR-B-05-K12` — mocowanie i dostępność gaśnic

## Wybór luki

Kompetencja miała cztery pytania o mocowanie gaśnicy, jej zasłonięcie ładunkiem i ryzyko poluzowania. Brakowało sytuacji, w której gaśnica jest stabilnie zamocowana, ale jej wyjęcie wymaga dodatkowej czynności i szukania klucza — co utrudnia szybki dostęp załogi.

## Dodane pytanie

- `ADR-B-0704`: gaśnica jest zamocowana, lecz uchwyt otwiera się kluczem przechowywanym w zamkniętej skrzynce.
- Klucz: **B** — przenieść ją do uchwytu zapewniającego szybki dostęp załogi.
- Explanation: **367 znaków**, 5 zdań.
- Długości A/B/C: **97/96/100** znaków; odpowiedzi są wyrównane.
- Audyt A/B/C: A — myli stabilne mocowanie z łatwym dostępem; B — usuwa przeszkodę i zapewnia szybkie wyjęcie; C — etykieta nie usuwa konieczności szukania klucza.
- Status: `needs_review`; nic nie oznaczono jako `verified`.

## Podstawa prawna

- ADR 2025, 8.1.4.5: gaśnice powinny być zamontowane tak, aby załoga miała do nich łatwy dostęp; powinny być również chronione przed wpływem warunków atmosferycznych.
- Oficjalny polski tekst ADR 2025, tom II: https://www.gov.pl/attachment/b4638c72-30e3-4bff-afd1-1b9ba4100e70
- Dz.U. 2025 poz. 642: https://dziennikustaw.gov.pl/DU/2025/642
- UNECE ADR 2025: https://unece.org/adr-2025-files

Właściwy punkt 8.1.4.5 sprawdzono w oficjalnym polskim tekście ADR 2025. Pełne literalne porównanie całego pytania i niezależna recenzja specjalisty pozostają pending.

## Synchronizacja #646

- Bank: 704 pytania ADR-B-0001–0704; wszystkie `needs_review`, 0 `verified`.
- Blob SHA banku: `681b94b07ae6673fa120326cb2eba6423eb22957`.
- Warianty i klucze egzaminów próbnych 001–005 wskazują aktualny SHA.
- Snapshoty sequential/legal 704-704; rejestr źródeł, manifesty, indeksy, metryki i materiały kursu aktualizowane.
- Rozkład odpowiedzi A/B/C: 238/247/219.
- Wskaźnik „poprawna = jedyna najdłuższa”: 75/704 = 10,65%; maksimum modułu 13,95%.
