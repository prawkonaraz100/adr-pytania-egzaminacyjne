# Etap 4x33 — poprawa dystraktorów dotyczących postoju i bezpieczeństwa, B-04

## Punkt wyjścia
- Świeży `main`: `1989b8950d1399ac92e60d295f1e7cd6b7de3cec`.
- Zakres: kurs podstawowy ADR, dział B-04.

## Potwierdzone przypadki
Przeredagowano 6 pytań bez zmiany ID, modułu ani poprawnej litery:
- **ADR-B-0310:** zamieniono „dowolne miejsce przy drodze” i „zawsze pobocze autostrady” na realistyczne, lecz błędne założenia o niezabezpieczonym parkingu i krótkim postoju.
- **ADR-B-0347:** zamiast „dowolnego parkingu” i polegania na telefonie do firmy, dystraktory sprawdzają pominięcie kolejności z ADR 8.4.1.
- **ADR-B-0348:** zastąpiono „dowolny chodnik” i pas awaryjny argumentami o oświetleniu parkingu i światłach awaryjnych.
- **ADR-B-0349:** zastąpiono „dowolny przystanek” i plac z dużym ruchem błędnym poleganiem na pozostaniu w kabinie lub braku autobusu w danej chwili.
- **ADR-B-0355:** zamiast stania pod pojazdem lub przy wylocie par, dystraktory sprawdzają wybór strony zawietrznej dla lepszego widoku i próbę rozpoznania substancji po zapachu.
- **ADR-B-0358:** zamiast argumentu „jest zimno” i ogólnego „zawsze włączony”, dystraktory mylą zasilanie kabiny oraz samą pracę pompy z warunkami wyjątku dla silnika.

Explanation wszystkich sześciu pytań przepisano prostym językiem (2–5 zdań, 300+ znaków), z uzasadnieniem poprawnej odpowiedzi, wyjaśnieniem błędnych opcji i podstawą ADR. Statusy pozostają `needs_review`.

## Metryki po zmianach
- Bank: 609 pytań; duplikaty ID: 0; explanation poniżej 200 znaków: 0.
- Globalnie „poprawna = jedyna najdłuższa”: 69/609 = 11.33%.
- B-04: 5/46 = 10.87%; minimum explanation 277 znaków.
- Klucz A/B/C w B-04: 15/18/13.
- Nie zmieniono poprawnych liter, numeracji ani statusów. Brak niezależnej aprobaty prawnej.

## Uwagi do dalszej kontroli
Po edycji trzeba zsynchronizować klucze egzaminów próbnych, manifest pakietu recenzyjnego oraz snapshoty audytów sekwencyjnych i klauzulowych dla zmienionych ID przed scaleniem.
