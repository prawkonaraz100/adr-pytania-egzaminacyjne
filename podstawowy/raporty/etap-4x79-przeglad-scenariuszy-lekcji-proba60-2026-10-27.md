# Etap 4x79 — przegląd scenariuszy B-06–13, lekcji B-01–04 i rotacyjnej próby explanation

- Punkt bazowy: `main` `11038337c0bd1dac95d5bd26545efd09d4692947` (27.10.2026).
- Zakres: wyłącznie kurs podstawowy ADR.
- Metoda: odczyt scenariuszy i lekcji z GitHub, kontrola skryptowa identyfikatorów, modułów, pól dydaktycznych i metryk banku; ręczny przegląd sytuacji, kroków i typowych błędów w scenariuszach B-06–13 oraz układu i języka lekcji B-01–04.

## 1. Quality Gate na wejściowym main

- Bank: 609 pytań, 609 unikalnych ID; wszystkie `needs_review`, 0 `verified`.
- Poprawna odpowiedź jest jedyną najdłuższą: 73/609 = 11.99%; limit 18%.
- Najkrótsze explanation: 300 znaków; poniżej 200 znaków: 0.
- Ostatni przebieg CI na wejściowym `main`: PASS [run #40461032801](https://github.com/prawkonaraz100/adr-pytania-egzaminacyjne/actions/runs/40461032801).

## 2. Scenariusze praktyczne B-06–13

Sprawdzono wszystkie 26 scenariuszy w tych działach (łącznie 39 w kursie). Wynik kontroli strukturalnej:
- każdy scenariusz ma opis sytuacji, co najmniej 3 kroki, pytanie dla kursanta, wniosek do zapamiętania, listę typowych błędów, podstawę ADR, kryteria oceny i powiązane pytania;
- wszystkie powiązane ID istnieją w banku i należą do modułu scenariusza;
- brak pustych list kroków, brakujących ID i odwołań do pytań z innego działu;
- scenariusze pokazują konkretną decyzję kierowcy, a błędy wyjaśniają, jakie ryzyko lub niezgodność powodują.

| Dział | Scenariusze | Wynik |
|---|---:|---|
| B-06 | 3 | Oznakowanie: nieczytelna nalepka, rozbieżność tablicy i dokumentu; kierowca wyjaśnia przed wyjazdem. |
| B-07 | 3 | Uszkodzone opakowanie, podział obowiązków, zrozumiałe i dostępne instrukcje pisemne. |
| B-08 | 3 | Gaśnice, mocowanie i dostępność sprzętu; wyposażenie osobiste każdego członka załogi. |
| B-09 | 3 | Pozostałości po ładunku, bezpieczne mocowanie, zabezpieczenie całego ładunku. |
| B-10 | 3 | Dokumentacja odcinka morskiego, warunki ADR dla drogi, zgodność certyfikatu pakowania. |
| B-11 | 3 | Ograniczenie tunelowe, różne kody w jednej jednostce, planowanie objazdu. |
| B-12 | 3 | Ochrona podczas postoju i weryfikacja uprawnienia do odbioru. |
| B-13 | 3 | Kompletność dokumentów i zrozumiałe instrukcje pisemne. |

Nie wykryto potwierdzonego błędu merytorycznego w tej partii wymagającego zmiany kroków lub podstaw ADR. Nie zmieniano tekstu tylko dla kosmetycznej różnicy ani nie dopisywano wymogów bez potwierdzenia prawnego. Szczegóły prawne nadal wymagają niezależnej recenzji specjalisty.

## 3. Lekcje B-01–04

| Lekcja | Liczba różnych ID w tekście | Brakujące ID | ID z innego modułu | Elementy dydaktyczne |
|---|---:|---:|---:|---|
| B-01 | 45 | 0 | 0 | podsumowanie, pytania kontrolne i scenariusz obecne |
| B-02 | 56 | 0 | 0 | podsumowanie, pytania kontrolne i scenariusz obecne |
| B-03 | 49 | 0 | 0 | podsumowanie, pytania kontrolne i scenariusz obecne |
| B-04 | 46 | 0 | 0 | podsumowanie, pytania kontrolne i scenariusz obecne |

Przegląd potwierdził, że lekcje mają praktyczny wstęp, sekcje tematyczne, podsumowanie i pytania kontrolne. W pierwszych użyciach najważniejszych pojęć występują proste objaśnienia lub odnośniki do słowniczka. Nie stwierdzono potwierdzonej sprzeczności lekcji z przypisanymi pytaniami, którą można bezpiecznie naprawić bez ponownego sprawdzenia urzędowego tekstu ADR. Nie zmieniono banku ani kluczy.

## 4. Rotacyjna próba 60 explanation — ograniczenie doboru

Nie wykonano nowej próby 60 i nie powtórzono wcześniejszych ID pod pozorem nowej próby. Raport 4x67 dokumentuje, że po zachowawczym wykluczeniu wszystkich ID pojawiających się w raportach 4x51–4x66 pozostało 59 rekordów; próbę 4x67 zbudowano z tych rekordów i dwóch kandydatów wspomnianych wyłącznie w karcie kontrolnej 4x66, a oceniono 60 ID. Z tego powodu nie ma już puli 60 niepowtarzanych rekordów według tej metody. Raporty 4x68–4x78 również zawierają kolejne przeglądy i próby.

Wynik: **0 nowych explanation przepisanych w tej partii**, ponieważ nie można uczciwie utworzyć nowej, 60-elementowej próby bez powtórzenia wcześniejszych pozycji. Nie należy deklarować próby jako świeżej, jeśli ID występowały w poprzednich próbach. Kolejna rotacja wymaga jawnej listy faktycznie próbkowanych ID, a nie wykluczania każdego przypadkowego wystąpienia w tekście raportu.

## 5. Luki programu i decyzja o banku

Mapa pokrycia programu wykazuje pytania dla wszystkich 104 z 104 kompetencji teoretycznych. W tej partii nie znaleziono konkretnej brakującej kompetencji potwierdzonej przepisem, więc nie dodano pytań od ADR-B-0610. Nie zmieniono przypisania pytań; warianty egzaminu 001–005 i klucze pozostają zsynchronizowane z niezmienionym bankiem.

## 6. Testy i ograniczenia

Nie ma lokalnego checkoutu repozytorium w tym środowisku, a wcześniejsze raporty odnotowują, że `git clone` nie działa z powodu braku DNS. Nie deklaruję uruchomienia lokalnych testów jednostkowych. Kontrola skryptowa danych pobranych z `main` dała wynik opisany powyżej; ostatecznym warunkiem przyjęcia raportu jest pełny PASS Quality Gate CI na PR.

Żadne pytanie nie zostało oznaczone jako `verified`. Kurs cystern i inne kursy pozostają poza zakresem.
