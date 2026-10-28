# Etap 4x125 — próbka 40: wyjaśnienia, dystraktory i synchronizacja

- Data: 2026-10-28.
- Świeży punkt wejścia: `main` `1b9c1db026c1333bdefaeba25e40d6826b4fbe34`.
- Gałąź: `stage4x125-proba40-jakosc-dystraktorow`.
- Końcowy blob `questions.jsonl`: `36985d2be9667dad581f241d68f7df76ea47e0d5`.
- Zakres: wyłącznie kurs podstawowy ADR.
- Seed: `41252026`; deterministyczne tasowanie Fisher–Yates nad bankiem po wykluczeniu `sample_ids`, `edited_ids` i zapisanych follow-upów z etapów 4x122–4x124.

## Próbka

Sprawdzono 40 pytań: treść, wszystkie opcje A/B/C, poprawną literę, explanation i powiązanie z modułem. Próbka nie nakłada się na zapisane sample/follow-up IDs etapów 4x122–4x124.

- `ADR-B-0148` (ADR-B-01)
- `ADR-B-0272` (ADR-B-01)
- `ADR-B-0589` (ADR-B-13)
- `ADR-B-0400` (ADR-B-12)
- `ADR-B-0032` (ADR-B-11)
- `ADR-B-0436` (ADR-B-09)
- `ADR-B-0144` (ADR-B-12)
- `ADR-B-0285` (ADR-B-07)
- `ADR-B-0233` (ADR-B-13)
- `ADR-B-0253` (ADR-B-08)
- `ADR-B-0608` (ADR-B-01)
- `ADR-B-0489` (ADR-B-11)
- `ADR-B-0025` (ADR-B-09)
- `ADR-B-0584` (ADR-B-07)
- `ADR-B-0061` (ADR-B-10)
- `ADR-B-0264` (ADR-B-11)
- `ADR-B-0241` (ADR-B-03)
- `ADR-B-0173` (ADR-B-09)
- `ADR-B-0425` (ADR-B-09)
- `ADR-B-0604` (ADR-B-11)
- `ADR-B-0069` (ADR-B-13)
- `ADR-B-0488` (ADR-B-11)
- `ADR-B-0600` (ADR-B-13)
- `ADR-B-0185` (ADR-B-05)
- `ADR-B-0394` (ADR-B-10)
- `ADR-B-0504` (ADR-B-06)
- `ADR-B-0403` (ADR-B-12)
- `ADR-B-0316` (ADR-B-02)
- `ADR-B-0323` (ADR-B-01)
- `ADR-B-0081` (ADR-B-09)
- `ADR-B-0159` (ADR-B-02)
- `ADR-B-0174` (ADR-B-11)
- `ADR-B-0554` (ADR-B-09)
- `ADR-B-0523` (ADR-B-13)
- `ADR-B-0397` (ADR-B-10)
- `ADR-B-0048` (ADR-B-04)
- `ADR-B-0545` (ADR-B-06)
- `ADR-B-0222` (ADR-B-05)
- `ADR-B-0435` (ADR-B-11)
- `ADR-B-0071` (ADR-B-08)

Rozkład próbki według działu: ADR-B-01: 4; ADR-B-13: 5; ADR-B-12: 3; ADR-B-11: 7; ADR-B-09: 6; ADR-B-07: 2; ADR-B-08: 2; ADR-B-10: 3; ADR-B-03: 1; ADR-B-05: 2; ADR-B-06: 2; ADR-B-02: 2; ADR-B-04: 1.

## Potwierdzone poprawki

1. **ADR-B-0173 — treść pytania i explanation.** Wcześniej stem wskazywał równocześnie kolumny 10 i 17 jako miejsce kodów BK/VC. Doprecyzowano pytanie do kolumny 17 tabeli A, gdzie sprawdza się wskazanie dopuszczające przewóz luzem. Nie zmieniono poprawnej litery C ani ID. Podstawa: ADR 7.3.1.1 oraz 3.2, tabela A, kolumna 17.
2. **ADR-B-0425 — dystraktory A/B i explanation.** Zastąpiono dwa zbyt łatwe do odrzucenia warianty realistycznymi pomyłkami: potraktowaniem kodu 1.4S jako pełnego zwolnienia z kontroli oraz pominięciem warunków uwagi (a). Poprawna litera C bez zmian. Podstawa: ADR 7.5.2.1, uwaga (a).
3. **ADR-B-0488 — dystraktor B i explanation.** Zamiast ogólnego błędnego odwołania do tuneli A/B wprowadzono częstą pomyłkę: zastosowanie reguły cysternowej niezależnie od postaci przewozu. Poprawna litera A bez zmian. Podstawa: ADR 8.6.4, kod D/E.
4. **ADR-B-0608 — dystraktor C i explanation.** Zastąpiono łatwy do odrzucenia pomysł zmiany numeru UN sugestią, że przygotowanie dokumentów przez nadawcę wystarcza do rozpoczęcia przewozu. To wiarygodny błąd polegający na uznaniu dokumentacji za zgodę na przewóz. Poprawna litera A bez zmian. Podstawa: ADR 2.1 i 3.2, tabela A.

Pozostałe 36 pytań nie wymagało zmiany: explanation już podawały sens poprawnej odpowiedzi, odnosiły się do kuszących błędnych opcji i kończyły krótką podstawą ADR. Nie dopisywano zmian „na siłę”. Nie znaleziono luki programu, która uzasadniałaby nowe pytanie w tej partii.

## Synchronizacja

- Zaktualizowano migawki prawne i sekwencyjne dla zakresów 151–180, 417–436, 483–494 i 598–609, w których znajdują się zmienione ID.
- Zaktualizowano źródłowy hash banku i pozycje dotknięte zmianą w wariantach/kluczach 001–005. ADR-B-0425 występuje w wariancie 003; zaktualizowano jego opcje oraz wyjaśnienie w kluczu. Poprawnych liter nie zmieniono.
- Nie zmieniono liczby pytań, ID ani statusów prawnych.

## Preflight Quality Gate

- Bank: 609 pytań, 609 unikalnych ID; wszystkie `needs_review`, 0 `verified`.
- „Poprawna = jedyna najdłuższa”: 69/609 = 11.33%; maksymalny dział: 13.95%.
- Explanation minimum: 300 znaków; poniżej 200: 0.
- ID, poprawne litery i podstawy prawne zachowano poza redakcyjnym doprecyzowaniem referencji w ADR-B-0173.

## Testy i ograniczenia

Nie mogłem uruchomić lokalnego checkoutu/testów w tym połączeniu z GitHub; wykonano skryptowy preflight na pobranym banku, a obowiązkowym kryterium scalania pozostaje pełny Quality Gate GitHub Actions. Nie oznaczono pytań jako `verified`; wszystkie wymagają niezależnej recenzji prawnej.
