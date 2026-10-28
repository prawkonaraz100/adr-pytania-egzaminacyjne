# Etap 4x129 — praktyczne decyzje kierowcy w lekcjach B-07–B-09

- Punkt wyjścia: świeży `main` `0e7b7f7625c4d7ac32d0aed101c6b71ff5451358` (po PR #591 / etap 4x128).
- Zakres: wyłącznie kurs podstawowy ADR.
- Bank i klucze egzaminów nie były zmieniane.

## Zmiany w lekcjach

| Lekcja | Uzupełnienie | Decyzje kierowcy |
|---|---|---|
| B-07 — Obowiązki uczestników | Pęknięta sztuka na rampie; instrukcje w niezrozumiałym języku | Wstrzymanie przyjęcia, zgłoszenie niezgodności, ponowna kontrola; sprawdzenie dostępności i zrozumiałości instrukcji. |
| B-08 — Wyposażenie | Gaśnica niedostępna; jeden zestaw wyposażenia dla kilku osób | Sprawdzenie wymagań dla przewozu, stanu i dostępności sprzętu; uzupełnienie elementów osobistych przed wyjazdem. |
| B-09 — Załadunek i mocowanie | Pozostałości po poprzednim ładunku; pas odkształcający opakowanie | Wstrzymanie załadunku i zgłoszenie pozostałości; korekta mocowania bez uszkadzania opakowania oraz kontrola całego ładunku. |

Każdy nowy przypadek zawiera sekwencję kroków, typowy błąd kursanta z prostym wyjaśnieniem, punkt ADR do sprawdzenia i pytania do omówienia. Wpisy nie zastępują procedur pracodawcy, instrukcji pisemnych ani praktycznych zajęć z instruktorem.

## Spójność z mapą scenariuszy i bankiem

Istniejące trzy scenariusze działowe pozostają w `podstawowy/praktyka/scenariusze-13-dzialow.json`; nie tworzono duplikatów. Lekcje nadal odsyłają do mapy i zawierają odrębne ćwiczenia tekstowe. Kontrola referencji zaktualizowanych lekcji:
- B-07: 48 unikalnych referencji, brakujące ID: 0, ID z innego działu: 0, dodany przebieg krok po kroku: tak.
- B-08: 42 unikalnych referencji, brakujące ID: 0, ID z innego działu: 0, dodany przebieg krok po kroku: tak.
- B-09: 46 unikalnych referencji, brakujące ID: 0, ID z innego działu: 0, dodany przebieg krok po kroku: tak.

Nie dodano nowych pytań: ten przegląd nie potwierdził konkretnej luki programu, którą można bezpiecznie uzupełnić bez niezależnej kontroli źródeł prawnych.

## Preflight Quality Gate

- Pytania w banku: 609.
- Zduplikowane ID: 0.
- Explanation krótsze niż 200 znaków: 0; najkrótsze explanation: 300 znaków.
- Status `verified`: 0; statusy nie były zmieniane.
- Wskaźnik „poprawna = jedyna najdłuższa” według działu:
  - ADR-B-01: 6/45 = 13.33%; klucze A/B/C: 17/17/11.
  - ADR-B-02: 7/56 = 12.50%; klucze A/B/C: 21/19/16.
  - ADR-B-03: 4/49 = 8.16%; klucze A/B/C: 16/21/12.
  - ADR-B-04: 6/46 = 13.04%; klucze A/B/C: 15/18/13.
  - ADR-B-05: 5/43 = 11.63%; klucze A/B/C: 18/14/11.
  - ADR-B-06: 6/45 = 13.33%; klucze A/B/C: 16/14/15.
  - ADR-B-07: 6/48 = 12.50%; klucze A/B/C: 18/18/12.
  - ADR-B-08: 3/42 = 7.14%; klucze A/B/C: 12/12/18.
  - ADR-B-09: 5/46 = 10.87%; klucze A/B/C: 13/15/18.
  - ADR-B-10: 4/55 = 7.27%; klucze A/B/C: 19/18/18.
  - ADR-B-11: 6/43 = 13.95%; klucze A/B/C: 12/13/18.
  - ADR-B-12: 5/44 = 11.36%; klucze A/B/C: 14/13/17.
  - ADR-B-13: 6/47 = 12.77%; klucze A/B/C: 15/15/17.

Wyniki powyżej są kontrolą wstępną na danych pobranych z gałęzi. Testy lokalne nie były uruchamiane w tym środowisku; jako wymagany test wykonano repozytoryjny Quality Gate CI. Scalenie wymaga PASS repozytoryjnego Quality Gate CI na końcowym commicie PR.

## Podstawa prawna do niezależnej recenzji

- ADR 2025, Dz.U. 2025 poz. 642 ze sprostowaniem Dz.U. 2025 poz. 1575: 1.4.2–1.4.3, 5.4.3.1–5.4.3.3, 7.5.1, 7.5.7.1, 7.5.8.1, 8.1.4, 8.1.5.2 i 8.3.2.
- Nie zmieniono kluczy, treści odpowiedzi ani statusu weryfikacji prawnej.
