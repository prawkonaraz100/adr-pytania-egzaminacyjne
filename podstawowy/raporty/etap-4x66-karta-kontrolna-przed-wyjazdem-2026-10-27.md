# Etap 4x66 — przygotowanie kierowcy do wyjazdu, ścieżka międzydziałowa

Data: 27.10.2026. Świeży main: `414ea1ac1aed5b18408849f353512e04ba0a7214` (po PR #518). Zakres: **wyłącznie kurs podstawowy ADR**.

## Potrzeba dydaktyczna

Lekcje B-01, B-06, B-08 i B-13 opisują poprawne zasady osobno. Jednak początkujący kierowca może mieć trudność z połączeniem ich w **jedną kolejność decyzji przed wyjazdem**. Jest to luka w nawigacji dydaktycznej między działami, a nie potwierdzony brak konkretnego pytania prawnego.

## Zmiana

Dodano [KARTA-KONTROLI-PRZED-WYJAZDEM.md](../praktyka/KARTA-KONTROLI-PRZED-WYJAZDEM.md): pięć kroków — ustalenie towaru i wyłączenia (B-01), oznakowanie (B-06), wyposażenie (B-08), dokumenty/instrukcje (B-13), a na końcu decyzja o zgłoszeniu niezgodności przed wyjazdem. Każdy krok opisuje *co robi kierowca* i *dlaczego*, z podstawą ADR do sprawdzenia, linkiem do lekcji i do trzech przykładowych pytań. Karta zawiera cztery typowe błędy, odnośniki do scenariuszy i zastrzeżenie statusu.

Dodano linki do karty w `podstawowy/README.md` i `podstawowy/praktyka/SCENARIUSZE.md`, aby kursant trafiał do ćwiczenia ze ścieżki kursu.

## Identyfikatory i zgodność

| Dział | Istniejące question_ids użyte w karcie | Odpowiednie lekcje |
|---|---|---|
| B-01 | ADR-B-0605, ADR-B-0606, ADR-B-0607 | `ADR-B-01.md` |
| B-06 | ADR-B-0258, ADR-B-0504, ADR-B-0506 | `ADR-B-06.md` |
| B-08 | ADR-B-0596, ADR-B-0597 | `ADR-B-08.md` |
| B-13 | ADR-B-0598, ADR-B-0600, ADR-B-0586, ADR-B-0579 | `ADR-B-13.md` |

Wszystkie 12 ID sprawdzono na świeżym banku: istnieją i należą do podanych działów. Wykorzystane `SC-ADR-B-01`, `SC-ADR-B-06`, `SC-ADR-B-08`, `SC-ADR-B-13` oraz ich warianty `-02`, `-03` istnieją w mapie 39 scenariuszy.

## Granice zmian

Nie zmieniano `questions.jsonl`, kluczy ani arkuszy egzaminu próbnego. Bank pozostaje 609 `needs_review`, 0 `verified`, wskaźnik „poprawna = jedyna najdłuższa” 72/609 = **11,82%**, a explanation ma minimum 300 znaków. Karta nie potwierdza prawnej poprawności przewozu ani wykonania zajęć praktycznych. Punkty ADR podane do niezależnego sprawdzenia: 1.1.3.6, 3.2, 3.4, 5.2, 5.3, 5.4.1, 5.4.3, 8.1.4, 8.1.5 i 8.2; tekst urzędowy ADR 2025 Dz.U. poz. 642 wraz ze sprostowaniem poz. 1575.

## Quality Gate

Wynik testów CI z PR jest bramką do scalenia. Pozytywny wynik dokumentuje zgodność strukturalną repozytorium, **nie** zastępuje recenzji specjalisty ADR.
