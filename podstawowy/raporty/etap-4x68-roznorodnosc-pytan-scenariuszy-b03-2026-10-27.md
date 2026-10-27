# Etap 4x68 — różnorodność pytań w scenariuszach B-03

Data: 27.10.2026. Świeży `main`: `e667e55a241427bdbc0da0537bb12a3bfc521646`. Kurs podstawowy ADR.

## Potwierdzony brak
Trzy różne scenariusze modułu B-03 (wyciek przy kanalizacji, nieznana ciecz na parkingu oraz pozostałości po rozładunku) wszystkie wskazywały dokładnie **ten sam zestaw dwóch pytań**: ADR-B-0009 oraz ADR-B-0514. Oba pytania dotyczyły przede wszystkim oczyszczania po wycieku, więc nie ćwiczyły wprost odrębnych decyzji opisanych w scenariuszach 1 i 2. To wada dydaktycznego mapowania, nie potwierdzony błąd przepisów.

## Zmiana mapowania

| Scenariusz | Poprzednio | Obecnie | Dlaczego |
|---|---|---|---|
| SC-ADR-B-03 — wyciek przy kratce | 0009, 0514 | **0100, 0163, 0009** | 0100 i 0163 sprawdzają bezpieczne ograniczenie odpływu, a 0009 przypomina o oczyszczeniu po wycieku |
| SC-ADR-B-03-02 — nieznany wyciek na parkingu | 0009, 0514 | **0101, 0178, 0295** | Te pytania uczą unikania kontaktu z nieznaną substancją i oparami |
| SC-ADR-B-03-03 — pozostałości przed kolejnym załadunkiem | 0009, 0514 | **0009, 0177, 0514** | Wszystkie trzy dotyczą oczyszczenia pojazdu/kontenera po wycieku, w tym przypadku braku miejsca do oczyszczania |

Nowe odwołania prowadzą wyłącznie do istniejących rekordów B-03. Żaden numer pytania, poprawna odpowiedź ani explanation nie zostały zmienione. Każdy scenariusz nadal ma 1–3 skupione na nim pytania.

## Regresja

Do `tests/test_stage4x59_scenario_questions.py` dodano blokującą kontrolę: w obrębie każdego z 13 działów nie mogą występować trzy scenariusze z identycznym zestawem pytań. Reguła pilnuje różnorodności powiązań, lecz nie udaje automatycznej oceny jakości merytorycznej.

## Podstawa i status

Wszystkie użyte odsyłacze zawierają podstawy ADR 2025: 5.4.3.4 dla bezpiecznej reakcji na wyciek i 7.5.8.1 dla oczyszczenia przestrzeni ładunkowej. Zmiana nie dodaje nowego twierdzenia prawnego; niezależna weryfikacja specjalisty pozostaje konieczna. Bank nadal ma **609 `needs_review`, 0 `verified`**, wskaźnik 72/609 = 11,82%, minimum explanation 300 znaków. Arkusze egzaminu próbnego i pakiet recenzyjny nie wymagają regeneracji, ponieważ pytania i przydziały działów są niezmienione. Scenariusze nadal są wyłącznie symulacjami.
