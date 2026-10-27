# Etap 4x100 — naprawa nieaktualnych metryk pokrycia

- Data: 2026-10-27.
- Punkt wejścia: świeży `main` `9c0cbcfa35cf4964c78aeb4838d9602369653c95`.
- Zakres: synchronizacja dokumentacji pokrycia z bankiem; bez zmian w pytaniach i kluczach.

## Potwierdzone rozbieżności

W `docs/POKRYCIE-KURSU.md` bieżąca sekcja zawierała metryki z wcześniejszej migawki:
- wskaźnik „poprawna = jedyna najdłuższa”: zapisano 86/609 = 14,12%, podczas gdy aktualne ścisłe kryterium liczy 73/609 = 11,99%;
- rozkład liter poprawnych odpowiedzi: zapisano A=205, B=207, C=197; bank daje A=206, B=207, C=196;
- liczby pytań w matrycy były zaniżone w ośmiu działach.

## Poprawione liczby

| Dział | Stara liczba w matrycy | Aktualna liczba w banku |
|---|---:|---:|
| ADR-B-01 | 35 | 45 |
| ADR-B-04 | 44 | 46 |
| ADR-B-05 | 40 | 43 |
| ADR-B-07 | 46 | 48 |
| ADR-B-08 | 40 | 42 |
| ADR-B-11 | 35 | 43 |
| ADR-B-12 | 43 | 44 |
| ADR-B-13 | 35 | 47 |

Pozostałe działy już miały prawidłowe liczby. Suma matrycy to teraz 609.

## Metryki z banku

- Pytania: 609, wszystkie ID unikalne; 609 `needs_review`, 0 `verified`.
- Poprawna litera: A=206, B=207, C=196.
- Poprawna odpowiedź jest **jedyną najdłuższą** w 73/609 = 11,99%; maksymalnie 14,29% w pojedynczym dziale.
- Explanation: minimum 300 znaków.
- 107 kompetencji na mapie (104 teoretyczne i 3 praktyczne); wszystkie pytania są przypisane do istniejących kompetencji, bez odwołań między działami.
- 39 scenariuszy, po 3 na dział; 5 wariantów i 5 kluczy egzaminu.

## Regresja

Dodano `tests/test_coverage_report_metrics.py`. Test oblicza metryki bezpośrednio z `questions.jsonl` i blokuje niezgodność rozkładu A/B/C, wskaźnika długości odpowiedzi, liczby pytań w tabeli dla każdego działu i statusów weryfikacji.

Dokumentacja została skorygowana na podstawie obliczeń z bieżącego banku. Nie zmieniono treści pytań ani nie oznaczono żadnego pytania jako `verified`.
