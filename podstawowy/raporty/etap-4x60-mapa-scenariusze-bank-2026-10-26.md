# Etap 4x60 — mapa powiązań scenariusze ↔ bank pytań

- Data: 26.10.2026. Świeży `main`: `8c3fef5ad3cf856b32b7b35c345aeb98c79b37ea`.
- Zakres: wyłącznie podstawowy kurs ADR, bez zmian prawa i kluczy.
- Po zakończeniu 4x59 w każdym z 39 scenariuszy jest sytuacja, pytanie kursanta, kroki, błędy i uzasadnienie.

## Wynik audytu pokrycia sytuacyjnego

Liczba pytań występujących w przynajmniej jednym polu `question_ids` scenariuszy wynosi **75/609** (12.3%). **534** pytań nie ma bezpośredniego przypisania do scenariusza. To **nie znaczy**, że nie zostały omówione w podręczniku albo że bank jest niekompletny — scenariusze obejmują reprezentatywne sytuacje, a nie każdy wariant pytania. Dodawanie losowych odsyłaczy tylko po to, by podnieść procent byłoby błędem dydaktycznym.

| Dział | Bank | ID w scenariuszach | Bez powiązania | Pięć ID do oceny merytorycznej |
|---|---:|---:|---:|---|
| ADR-B-01 | 45 | 7 | 38 | ADR-B-0001, ADR-B-0003, ADR-B-0040, ADR-B-0041, ADR-B-0091 |
| ADR-B-02 | 56 | 4 | 52 | ADR-B-0042, ADR-B-0043, ADR-B-0044, ADR-B-0094, ADR-B-0095 |
| ADR-B-03 | 49 | 2 | 47 | ADR-B-0007, ADR-B-0008, ADR-B-0045, ADR-B-0046, ADR-B-0100 |
| ADR-B-04 | 46 | 5 | 41 | ADR-B-0011, ADR-B-0047, ADR-B-0048, ADR-B-0102, ADR-B-0103 |
| ADR-B-05 | 43 | 8 | 35 | ADR-B-0013, ADR-B-0014, ADR-B-0015, ADR-B-0049, ADR-B-0050 |
| ADR-B-06 | 45 | 7 | 38 | ADR-B-0017, ADR-B-0018, ADR-B-0051, ADR-B-0052, ADR-B-0053 |
| ADR-B-07 | 48 | 4 | 44 | ADR-B-0021, ADR-B-0054, ADR-B-0055, ADR-B-0116, ADR-B-0117 |
| ADR-B-08 | 42 | 6 | 36 | ADR-B-0022, ADR-B-0023, ADR-B-0024, ADR-B-0056, ADR-B-0057 |
| ADR-B-09 | 46 | 6 | 40 | ADR-B-0025, ADR-B-0027, ADR-B-0058, ADR-B-0059, ADR-B-0060 |
| ADR-B-10 | 55 | 5 | 50 | ADR-B-0029, ADR-B-0061, ADR-B-0062, ADR-B-0119, ADR-B-0140 |
| ADR-B-11 | 43 | 7 | 36 | ADR-B-0031, ADR-B-0032, ADR-B-0033, ADR-B-0063, ADR-B-0064 |
| ADR-B-12 | 44 | 6 | 38 | ADR-B-0034, ADR-B-0035, ADR-B-0036, ADR-B-0066, ADR-B-0067 |
| ADR-B-13 | 47 | 8 | 39 | ADR-B-0037, ADR-B-0038, ADR-B-0039, ADR-B-0068, ADR-B-0069 |

## Kontrole

- 39 scenariuszy, dokładnie trzy na dział.
- Brakujące lub międzydziałowe `question_ids`: 0.
- Każdy scenariusz ma `learner_question`, co najmniej cztery kroki, typowe błędy, podstawę ADR i krótkie uzasadnienie.
- Bank: 609 pytań, 609 `needs_review`, 0 `verified`, wyjaśnienia nie krótsze niż 300 znaków, globalny wskaźnik „poprawna = jedyna najdłuższa” 72/609 = 11,82%.

## Następny krok jakości

Dla każdego z 13 działów instruktor lub recenzent powinien sprawdzić kilka pytań dotąd niepowiązanych z żadnym scenariuszem i ustalić, czy dotyczą praktycznej czynności kierowcy. **Tylko po potwierdzeniu** dopasować je do istniejącego scenariusza lub opisać potrzebę czwartego ćwiczenia. Nie tworzyć powiązań na podstawie samego podobieństwa słów i nie uznawać braku powiązania za błąd prawny.

Ta mapa stanowi plan kolejnej kontroli, a nie formalną zgodę na użycie szkoleniowe.
