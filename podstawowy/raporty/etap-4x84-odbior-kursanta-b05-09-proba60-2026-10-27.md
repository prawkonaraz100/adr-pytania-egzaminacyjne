# Etap 4x84 — odbiór kursanta B-05–B-09, próbka 60 explanation i dystraktory

- Data: 27.10.2026.
- Punkt wejściowy: świeży `main`, `8c212e3a573a016210ec3237e9d202efea5ebbb7`.
- Zakres: wyłącznie kurs podstawowy ADR.
- Bank po poprawce: 609 pytań, 609 unikalnych ID; wszystkie `needs_review`, 0 `verified`.

## 1. Odbiór lekcji B-05–B-09

| Lekcja | Pytań w module | ID w lekcji | Brakujące / obce ID | Scenariusze | Wynik |
|---|---:|---:|---:|---|---|
| B-05 | 43 | 43 | 0 / 0 | SC-ADR-B-05, SC-ADR-B-05-02, SC-ADR-B-05-03 | PASS struktury i referencji |
| B-06 | 45 | 45 | 0 / 0 | SC-ADR-B-06, SC-ADR-B-06-02, SC-ADR-B-06-03 | PASS struktury i referencji |
| B-07 | 48 | 48 | 0 / 0 | SC-ADR-B-07, SC-ADR-B-07-02, SC-ADR-B-07-03 | PASS struktury i referencji |
| B-08 | 42 | 42 | 0 / 0 | SC-ADR-B-08, SC-ADR-B-08-02, SC-ADR-B-08-03 | PASS struktury i referencji |
| B-09 | 46 | 46 | 0 / 0 | SC-ADR-B-09, SC-ADR-B-09-02, SC-ADR-B-09-03 | PASS struktury i referencji |

Każda lekcja zawiera wprowadzenie, cele nauki, rozdziały, typowe błędy, scenariusze, podsumowanie, pytania kontrolne, mapę pytań i podstawę prawną. Wszystkie pytania modułów są wymienione w odpowiedniej lekcji; brakujące ID: 0, obce działy: 0. Nie wykryto potwierdzonej sprzeczności wymagającej zmiany merytorycznej w tych pięciu lekcjach.

Sprawdzono 15 scenariuszy B-05–B-09. Każdy ma co najmniej trzy kroki, wniosek dla kursanta, powiązane ID pytań i podstawę ADR; brak brakujących ID i odwołań do innych działów. Scenariuszy nie zmieniano, ponieważ nie wykryto potwierdzonego błędu.

## 2. Losowa próbka 60 explanation

- Seed: `202610270084`; PRNG LCG (`state = 1664525 × state + 1013904223 mod 2^32`) i Fisher–Yates.
- Wynik redakcyjny: **60/60 bez potrzeby przepisywania**. Każde explanation ma 3–5 zdań i 300–422 znaki; brak krótkich wyjaśnień. W próbie nie znaleziono zdań dłuższych niż 35 słów.
- Próbka to kontrola redakcyjna, nie formalne zatwierdzenie prawne.

ID próbki:
1. `ADR-B-0011`
2. `ADR-B-0029`
3. `ADR-B-0032`
4. `ADR-B-0035`
5. `ADR-B-0047`
6. `ADR-B-0056`
7. `ADR-B-0057`
8. `ADR-B-0071`
9. `ADR-B-0081`
10. `ADR-B-0090`
11. `ADR-B-0116`
12. `ADR-B-0128`
13. `ADR-B-0130`
14. `ADR-B-0131`
15. `ADR-B-0135`
16. `ADR-B-0151`
17. `ADR-B-0154`
18. `ADR-B-0162`
19. `ADR-B-0171`
20. `ADR-B-0181`
21. `ADR-B-0189`
22. `ADR-B-0191`
23. `ADR-B-0196`
24. `ADR-B-0202`
25. `ADR-B-0225`
26. `ADR-B-0230`
27. `ADR-B-0231`
28. `ADR-B-0232`
29. `ADR-B-0260`
30. `ADR-B-0291`
31. `ADR-B-0298`
32. `ADR-B-0319`
33. `ADR-B-0336`
34. `ADR-B-0342`
35. `ADR-B-0373`
36. `ADR-B-0379`
37. `ADR-B-0399`
38. `ADR-B-0421`
39. `ADR-B-0422`
40. `ADR-B-0423`
41. `ADR-B-0436`
42. `ADR-B-0439`
43. `ADR-B-0486`
44. `ADR-B-0491`
45. `ADR-B-0494`
46. `ADR-B-0496`
47. `ADR-B-0498`
48. `ADR-B-0516`
49. `ADR-B-0527`
50. `ADR-B-0537`
51. `ADR-B-0541`
52. `ADR-B-0542`
53. `ADR-B-0543`
54. `ADR-B-0545`
55. `ADR-B-0560`
56. `ADR-B-0561`
57. `ADR-B-0573`
58. `ADR-B-0595`
59. `ADR-B-0606`
60. `ADR-B-0608`

## 3. Potwierdzona poprawka dystraktora

Zmieniono tylko błędny wariant B pytania **ADR-B-0116**. Poprzednia odpowiedź („zamknąć drzwi ładowni, aby osoby postronne nie zauważyły wycieku”) była zbyt jawnie absurdalna. Zastąpiono ją wariantem o zabezpieczeniu przesyłki pasem i kontynuowaniu jazdy po chwilowym ustaniu wycieku — nadal błędnym, ale bardziej wiarygodnym dydaktycznie.

Poprawiono również explanation, aby wyjaśniało, dlaczego krótka trasa, pas mocujący ani chwilowe ustanie wycieku nie usuwają niezgodności. Zachowano poprawną literę C, moduł B-07, źródła i status `needs_review`. Podstawa: ADR 2025, 1.4.2.2.1(c) oraz 1.4.2.2.3–1.4.2.2.4. Nie zmieniono twierdzenia prawnego.

- **Przed:** „Zamknąć drzwi ładowni i kontynuować jazdę, aby osoby postronne nie zauważyły wycieku”.
- **Po:** „Zabezpieczyć przesyłkę pasem i kontynuować jazdę, jeśli wyciek chwilowo ustanie”.

Migawka zmiany: [snapshot ADR-B-0116](../../review/batches/4x84-distractor-snapshot-ADR-B-0116.json).

## 4. Egzaminy próbne i metryki

Po zmianie banku odświeżono `source_bank_head` we wszystkich wariantach i kluczach 001–005. ADR-B-0116 nie występuje w tych arkuszach, więc nie zmieniano zestawów pytań ani kluczy odpowiedzi.

- Bank: 609 pytań, brak duplikatów ID.
- Explanation poniżej 200 znaków: 0; minimum w banku: 300 znaków.
- Poprawna odpowiedź jako jedyna najdłuższa: 73/609 = **11,99%**.
- Wszystkie działy poniżej 18%; maksimum: B-02 i B-03 po 14,29%.
- Statusy: 609 `needs_review`, 0 `verified`.

## 5. Testy i ograniczenia

Kontrolę skryptową danych wykonano na plikach pobranych z repozytorium. Nie ma dostępnego lokalnego checkoutu repozytorium przez użyte połączenie GitHub, więc nie deklaruję lokalnego uruchomienia pełnego zestawu testów. Wymagane testy automatyczne muszą zakończyć się PASS w GitHub Actions przed scaleniem.

Nie znaleziono potwierdzonej luki programu wymagającej nowego pytania. Nie zmieniano lekcji ani scenariuszy, ponieważ nie wykryto potwierdzonego błędu. Wszystkie pytania pozostają `needs_review`; nie rozpoczęto kursu cystern ani innego kursu.
