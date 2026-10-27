# Etap 4x98 — dopasowanie scenariuszy praktycznych do pytań

- Data: 2026-10-27.
- Punkt wejścia: świeży `main` `a826ea7b0f1cd53eeeeaa7ea884d3e829641a14d`.
- Zakres: scenariusze praktyczne B-02; bez zmian w banku pytań.

## Znalezione problemy i poprawki

### SC-ADR-B-02-02

**Problem:** sytuacja opisywała mokrą plamę i nieodczytaną nalepkę, ale połączone pytania obejmowały zarówno klasę 8, jak i klasę 4.3. Sam scenariusz nie wyjaśniał, że kursant ma porównać oba przykłady.

**Poprawka:** sytuacja wprost wskazuje dwie przesyłki — jedną z nalepką klasy 8, drugą mokrą i oznaczoną klasą 4.3. Kroki i kryteria wymagają rozróżnienia działania żrącego od zagrożenia wydzieleniem palnego gazu w kontakcie z wodą. Zachowano pytania `ADR-B-0005`, `ADR-B-0006` i `ADR-B-0510`.

**Podstawa:** ADR 2.2.8.1.1, 2.2.43.1.1, 5.2.2.2.2 i instrukcje pisemne 5.4.3.4.

### SC-ADR-B-02-03

**Problem:** tytuł obiecywał sprawdzenie grupy pakowania, ale trzy podłączone pytania dotyczyły klas 3, 8 i 4.3; żadne nie sprawdzało grupy pakowania. Opis sytuacji koncentrował się na rozbieżności dokument–nalepka, a nie na porównaniu klas.

**Poprawka:** scenariusz opisuje teraz trzy towary — benzynę, materiał żrący i materiał klasy 4.3 — i ćwiczy rozpoznanie klasy oraz podstawowego zagrożenia. Kroki nadal uczą porównywania nazwy, numeru UN, klasy i nalepek oraz wstrzymania przyjęcia przy rozbieżności. Zachowano pytania `ADR-B-0004`, `ADR-B-0005` i `ADR-B-0006`; usunięto nieuzasadnioną obietnicę ćwiczenia grup pakowania.

**Podstawa:** ADR 2.2.3.1.1, 2.2.8.1.1, 2.2.43.1.1, 3.2 tabela A i 5.2.2.2.2.

## Kontrola zakresu

Przejrzano mapę 39 scenariuszy i ich powiązane pytania. Dwa powyższe przypadki miały potwierdzoną rozbieżność między opisem sytuacji/tytułem a zakresem pytań; w pozostałych przypadkach sprawdzona zgodność ID, modułu i opisu nie wskazała równie jednoznacznego błędu wymagającego zmiany. Nie zmieniano banku, kluczy ani podstaw prawnych pytań.

Dodano test regresyjny `tests/test_stage4x98_scenario_alignment.py`, który blokuje powrót obu rozbieżności i sprawdza, że scenariusze B-02 wskazują istniejące pytania tego działu.

## Kontrole przed CI

- Bank: 609 unikalnych pytań, wszystkie `needs_review`, 0 `verified`.
- Scenariusze: 39, po 3 na dział; `question_ids` bez zmian, wszystkie pozostają w module B-02.
- „Poprawna = jedyna najdłuższa”: 73/609 = 11,99%; maksimum działu 14,29%.
- Explanation: minimum 300 znaków.
- Warianty i klucze egzaminu próbnego 001–005 bez zmian.

Zmiany są dydaktyczne i dotyczą dopasowania sytuacji do pytań; nie stanowią formalnej weryfikacji prawnej. Wszystkie pytania pozostają `needs_review`.
