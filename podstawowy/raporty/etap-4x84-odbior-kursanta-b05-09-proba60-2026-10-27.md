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

## 2. Losowa próbka 60 explanation — rozdzielenie nowej puli i rotacji

- Seed losowania: `202610270084`; PRNG LCG (`state = 1664525 × state + 1013904223 mod 2^32`) i Fisher–Yates.
- **Ograniczenie pokrycia:** po odjęciu jawnych próbek 4x46, 4x48–4x50, próbek z rejestru 4x67 oraz ID z próbek 4x80–4x82 zostało tylko **26 ID, które dało się uznać za nowe z dostępnymi listami**. Nie przedstawiam ich jako 60 nowych.
- Aby nadal przejrzeć 60 explanation, sprawdzono wszystkie 26 nieobjętych wcześniej ID oraz 34 ID jako kontrolę rotacyjną. Te 34 powtórki są jawnie wydzielone poniżej; nie są liczone jako nowa próbka.
- Wynik: **59/60 bez zmiany**. ADR-B-0116 był jedyną pozycją, której explanation zmieniono równolegle z korektą dystraktora. W całej próbce explanation mają 3–5 zdań i co najmniej 300 znaków; dla 26 nowych ID zakres wynosi 301–408 znaków. Nie znaleziono zdania dłuższego niż 35 słów.
- Nie można uczciwie potwierdzić 60 zupełnie nowych ID, dopóki nie zostanie rozszerzony bank albo formalnie ustalony zakres wykluczeń dla wszystkich wcześniejszych próbek.

### 26 ID z puli niewystępującej w dostępnych wcześniejszych próbkach

1. `ADR-B-0010`
2. `ADR-B-0012`
3. `ADR-B-0032`
4. `ADR-B-0047`
5. `ADR-B-0054`
6. `ADR-B-0060`
7. `ADR-B-0131`
8. `ADR-B-0135`
9. `ADR-B-0162`
10. `ADR-B-0199`
11. `ADR-B-0230`
12. `ADR-B-0319`
13. `ADR-B-0379`
14. `ADR-B-0421`
15. `ADR-B-0497`
16. `ADR-B-0510`
17. `ADR-B-0514`
18. `ADR-B-0537`
19. `ADR-B-0541`
20. `ADR-B-0542`
21. `ADR-B-0543`
22. `ADR-B-0567`
23. `ADR-B-0573`
24. `ADR-B-0595`
25. `ADR-B-0606`
26. `ADR-B-0608`

### 34 ID w kontroli rotacyjnej (wcześniej próbkowane)

1. `ADR-B-0011`
2. `ADR-B-0029`
3. `ADR-B-0035`
4. `ADR-B-0056`
5. `ADR-B-0057`
6. `ADR-B-0071`
7. `ADR-B-0081`
8. `ADR-B-0090`
9. `ADR-B-0116`
10. `ADR-B-0128`
11. `ADR-B-0130`
12. `ADR-B-0151`
13. `ADR-B-0154`
14. `ADR-B-0171`
15. `ADR-B-0181`
16. `ADR-B-0189`
17. `ADR-B-0191`
18. `ADR-B-0196`
19. `ADR-B-0202`
20. `ADR-B-0225`
21. `ADR-B-0231`
22. `ADR-B-0232`
23. `ADR-B-0260`
24. `ADR-B-0291`
25. `ADR-B-0298`
26. `ADR-B-0336`
27. `ADR-B-0342`
28. `ADR-B-0373`
29. `ADR-B-0399`
30. `ADR-B-0422`
31. `ADR-B-0423`
32. `ADR-B-0436`
33. `ADR-B-0439`
34. `ADR-B-0486`

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
