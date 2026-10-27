# Etap 4x75 — doprecyzowanie lekcji B-09 względem pytań ADR-B-0173 i ADR-B-0240

Data: 27.10.2026. Punkt wyjścia: świeży main `f15860a5bf2cfc54114b97fdf82aac7a8404c65c` po PASS PR #532. Zakres: tylko kurs podstawowy.

## Przegląd pytań i lekcji

| ID | Treść kluczowa | Wynik | Działanie |
|---|---|---|---|
| ADR-B-0173 | Brak w tabeli A dopuszczającego kodu/odesłania przewozu luzem; poprawna litera C mówi, że brak podstawy do tego sposobu przewozu | Wyjaśnienie jest zgodne z obecną decyzją w lekcji. Sam początek odpowiedzi „Nie” jest językowo niezgrabny względem pytania „Co wynika?” | Uzupełniono lekcję o prostą sekwencję sprawdzenia kodu BK/VC i decyzji przed załadunkiem. Rekordu banku nie zmieniano: wymaga równoległego audytu A/B/C, snapshotów i wariantów egzaminu. |
| ADR-B-0240 | Wyjątek dotyczący ponownego załadunku tego samego towaru po przewozie luzem; poprawna litera C | Odpowiedź zaczyna się od „Nie” na pytanie „Kiedy może odstąpić?”. To problem redakcyjny, nie dowód nieprawidłowego przepisu | Uzupełniono lekcję o warunki decyzji dotyczącej czyszczenia, z podstawą ADR 7.5.8.2. Zmiana rekordu odłożona do kompletnego audytu i synchronizacji. |

## Zakres poprawki

Zmieniono tylko `podstawowy/lekcje/ADR-B-09.md`. Dodano dwa krótkie, konkretne przykłady: sprawdzenie dopuszczenia przewozu luzem w tabeli A oraz decyzję o oczyszczeniu pojazdu przed kolejnym, innym ładunkiem. Nie usunięto wcześniejszych objaśnień, nie dodano nowych liczb ani wyjątków bez wskazania podstawy. Kierowca otrzymuje jasne działanie „sprawdź → nie zakładaj → wstrzymaj niezgodny przewóz”.

## Status metryk i granica prawna

Bank bez zmian: 609 rekordów, 609 `needs_review`, 0 `verified`; poprawna odpowiedź jedyną najdłuższą w 73/609 = 11,99%, minimum explanation 300 znaków. Nie ma podstaw do regeneracji wariantów 001–005 po zmianie wyłącznie lekcji. Pełne literalne porównanie źródła urzędowego ADR 2025, Dz.U. poz. 642 i sprostowania poz. 1575 oraz formalna recenzja specjalisty pozostają otwarte. Nie przechodzono do cystern ani innych kursów.
