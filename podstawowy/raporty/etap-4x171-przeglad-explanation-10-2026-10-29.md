# Etap 4x171 — drugi przegląd explanation, partia 12

Data: 2026-10-29

## Zakres
Na świeżym `main` (commit `05edc1ecb67c91563219edaaf9be2eaeeb57e805`) poprawiono wyjaśnienia dla 10 pytań: ADR-B-0030, ADR-B-0031, ADR-B-0034, ADR-B-0035, ADR-B-0036, ADR-B-0037, ADR-B-0038, ADR-B-0039, ADR-B-0040 i ADR-B-0041. Zakres nie pokrywa się z listami ID wymienionymi w wpisach etapów 4x156–4x170 w Issue #10.

## Zasady redakcji
Wyjaśnienia mają 350–396 znaków i prowadzą od praktycznego sensu poprawnej odpowiedzi, przez wyjaśnienie mylących wariantów, do krótkiej podstawy ADR. Uproszczono sformułowania, objaśniono skróty lub terminy i dodano wskazówki do zastosowania przed wyjazdem albo w pracy z dokumentacją.

## Zakres zmian i kontrole
- Zmieniono wyłącznie pole `explanation` w `podstawowy/questions.jsonl`.
- Nie zmieniano treści pytań, opcji A/B/C, kluczy, źródeł ani podstaw prawnych.
- Status wszystkich rekordów pozostaje `needs_review`; nic nie oznaczono jako `verified`.
- Liczba pytań pozostaje 651 (ADR-B-0001–0651).
- Nie wykonano jeszcze lokalnego uruchomienia Quality Gate: zmiany zapisano przez GitHub API, a walidacja CI musi potwierdzić zgodność banku i snapshotów. Etap nie może być uznany za zakończony przed zielonym CI i scaleniem PR.

## ID i długości
| ID | Znaki w explanation |
|---|---:|
| ADR-B-0030 | 373 |
| ADR-B-0031 | 396 |
| ADR-B-0034 | 358 |
| ADR-B-0035 | 386 |
| ADR-B-0036 | 367 |
| ADR-B-0037 | 350 |
| ADR-B-0038 | 385 |
| ADR-B-0039 | 358 |
| ADR-B-0040 | 353 |
| ADR-B-0041 | 366 |

## Ograniczenia
To redakcja dydaktyczna, nie niezależna recenzja prawna. Wszystkie pytania pozostają do sprawdzenia przez specjalistę ADR. Wyłącznie kurs podstawowy; kurs cysterny pozostaje poza zakresem.
