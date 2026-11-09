# Kontrola druga — ADR-B-0376–0390

**Wynik: 0 OK / 15 POPRAW / 0 BLOKUJ.** Bank: 780 pytań. SHA blobu po wdrożeniu: `9475e2d4f7107dc676486710ce03d626dc7473d8`.

## Zakres wdrożenia

| ID | Kompetencja | Klucz | Zmiana | Podstawa |
|---|---|---:|---|---|
| 0376 | 07-K06 | A | Nowy temat: szkolenie kierowcy bez zaświadczenia ADR w limicie 1.1.3.6 | 8.2.3; 1.1.3.6.2 |
| 0377 | 07-K04 | B | Nowy temat: definicja odbiorcy przy wyznaczeniu osoby trzeciej | 1.2.1 |
| 0378 | 07-K03 | A | Nowy temat: załadowca uwzględnia towary już znajdujące się w pojeździe przy zakazach ładowania razem | 1.4.3.1.1(e); 1.4.3.1.2 |
| 0379 | 07-K02 | A | Przeredagowanie: kontrola przeciążenia pojazdu przez przewoźnika | 1.4.2.2.1(e); 1.4.2.2.2 |
| 0380 | 07-K01 | A | Przeredagowanie: nadawca może polegać na danych klasyfikacyjnych innych uczestników, bez przeniesienia odpowiedzialności | 1.4.2.1.2; 1.4.2.1.1(a) |
| 0381 | 10-K01 | A | Nowy temat: odstępstwo IMDG/ICAO wymaga zgodności z jednym z tych reżimów | 1.1.4.2.1; 5.4.1.1.7 |
| 0382 | 10-K01 | B | Przeredagowanie: zasady pakowania razem według IMDG/ICAO | 1.1.4.2.1(b); 5.4.1.1.7 |
| 0383 | 10-K01 | A | Nowy temat: definicja Instrukcji Technicznych ICAO | 1.2.1; 1.1.4.2.1(a) |
| 0384 | 10-K05 | B | Przeredagowanie: oznakowanie pojazdu tablicami pomarańczowymi według 5.3.2.1.1 | 1.1.4.2.1(c); 5.3.2.1.1 |
| 0385 | 10-K05 | A | Przeredagowanie: odstępstwo trwa do faktycznego oczyszczenia; nie wprowadzano nowego tematu cysternowego | 1.1.4.2.1(c) |
| 0386 | 10-K05 | B | Nowy temat: nieszczelna napełniona butla DOT nie może być nadana do przewozu | 1.1.4.7.2(c); 4.1.6.13(a) |
| 0387 | 10-K04 | A | Przeredagowanie: warunek tablic pomarańczowych dla pojazdu bez kontenera | 1.1.4.2.2; 5.3.2 |
| 0388 | 10-K03 | A | Nowy temat: czysty, suchy i przygotowany kontener w certyfikacie pakowania | 5.4.2, przypis 6 – IMDG 5.4.2.1.1 |
| 0389 | 10-K05 | B | Nowy temat: zakres odstępstwa 1.1.4.2.1 i wymagania ADR pozostające w mocy | 1.1.4.2.1 |
| 0390 | 10-K03 | A | Nowy temat: pionowe ustawienie bębnów w certyfikacie pakowania | 5.4.2, przypis 6 – IMDG 5.4.2.1.4 |

## Duplikaty i tematy zastępcze

Dziewięć duplikatów (0376, 0377, 0378, 0381, 0383, 0386, 0388, 0389, 0390) zastąpiono nowymi tematami w tych samych kompetencjach. W szczególności uwzględniono wcześniej przeoczone 0376 = 0472 i 0378 = 0482. Nowe tematy sprawdzono pod kątem ponownego dublowania banku. Nie dodano żadnych tematów cysternowych.

Sześć pozostałych rekordów (0379, 0380, 0382, 0384, 0385, 0387) przeredagowano w dotychczasowych podtematach. Klucze pozostają bez zmian. 0382 i 0384 miały wcześniej niesłusznie werdykt OK; teraz zostały poprawione.

## Niezmienniki i synchronizacja

- Wszystkie 15 rekordów zachowało `module_id`, literę klucza, przypisanie kompetencji oraz `image = null`.
- Statusy pozostają `needs_review`; `checked_at = null`, `reviewer = null`; 0 `verified`.
- Egzaminy próbne 002 (0387), 003 (0383) i 004 (0390) zsynchronizowane. Wariant 005 zachował `excluded_question_ids` bez zmian.
- Kolejka priorytetowa 4X44 dla 0379 i rejestry specjalisty zsynchronizowane.
- „Poprawna = jedyna najdłuższa”: **34/780 = 4,36%**, maksimum działu **7,87%** (bez zmian).
- „Poprawna = jedyna najkrótsza”: **205 → 197/780**; ADR-B-07: **31,5% → 24,1%**; ADR-B-10: **35,1% → 28,1%**; maksimum **35,4%** (ADR-B-12); każdy dział ≤ 38%.
- Licznik pytań bez porównania po obu kontrolach partii 26: **390** (ADR-B-0391–0780).
- Bank SHA: `4e00ad8db1a63f644ab205910c434dae20669de8` → `9475e2d4f7107dc676486710ce03d626dc7473d8`.

Pełny Quality Gate wymagany przed scaleniem.
