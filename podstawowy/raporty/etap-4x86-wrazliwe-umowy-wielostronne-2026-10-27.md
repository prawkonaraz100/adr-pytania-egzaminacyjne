# Etap 4x86 — umowy wielostronne i terminy wrażliwe na zmianę

- Data: 27.10.2026.
- Punkt wejściowy: `main` `ca3cfb62f51c2f5f52160c83d5d060c38122fbd9`.
- Bank blob SHA: `7a02299fd6fc0cd944abd8b84840b535d371fad9`.
- Zakres: kurs podstawowy ADR; audyt odporności materiałów na wygaśnięcie czasowych umów wielostronnych.

## Wynik skanowania

Skan banku 609 pytań oraz 13 lekcji pod kątem oznaczeń umów wielostronnych i terminów kalendarzowych znalazł jedno konkretne ryzyko czasowe: **M364**, wspomniane w pytaniach ADR-B-0145 i ADR-B-0198 oraz w lekcjach B-08 i B-13.

Oficjalny wykaz UNECE podaje dla M364 termin ważności **31 grudnia 2026 r.**; polskie obwieszczenie w Dzienniku Urzędowym Ministra Infrastruktury 2025 poz. 37 podaje ten sam termin. Umowa dotyczy odstępstwa od ADR 8.1.2.2: świadectwo dopuszczenia dla **przyczepy** może być przechowywane w bezpiecznym, dostępnym miejscu na przyczepie, chronionym przed pogodą. Nie jest to ogólne zwolnienie dla samochodu silnikowego.

Źródła urzędowe:
- [Dziennik Urzędowy MI 2025 poz. 37 — M364](https://www.gov.pl/attachment/cea0faed-9de2-4c02-a423-0c7f19619a77)
- [UNECE — lista umów wielostronnych ADR](https://unece.org/transport/road-transport/adr-multilateral-agreements)

## Lista do ponownego sprawdzenia przez specjalistę

| ID | Dział | Powód | Wymagane działanie |
|---|---|---|---|
| ADR-B-0145 | B-13 | Explanation przywołuje M364 i termin 31.12.2026 w kontekście dokumentów pojazdu/naczepy. | Przed użyciem po terminie sprawdzić, czy M364 została przedłużona, zastąpiona lub wypowiedziana; ewentualną korektę wykonać dopiero po potwierdzeniu urzędowym. |
| ADR-B-0198 | B-08 | Wyjaśnienie rozróżnia ogólną zasadę dla pojazdu silnikowego i wyjątek dla naczepy. | Po terminie ponownie potwierdzić status M364 i utrzymać wyraźne rozróżnienie samochód silnikowy/naczepa. |

**Nie zmieniono żadnej odpowiedzi ani explanation** w ramach audytu czasowego: aktualny termin jeszcze nie upłynął w dniu kontroli, a brak potwierdzonej nowej umowy nie jest podstawą do zgadywania. Oba pytania pozostają `needs_review`.

## Zabezpieczenie CI

Dodano test blokujący `tests/test_time_sensitive_adr_reference_queue.py`. Test sprawdza, że każde pytanie i lekcja zawierające M364 jest ujęte w kolejce specjalisty, że kolejka podaje datę wygaśnięcia i źródła urzędowe oraz że nie sugeruje zatwierdzenia ani zmiany odpowiedzi. Jest blokujący, ponieważ pominięcie terminu umowy mogłoby pozostawić w materiale nieaktualny wyjątek.

## Kontrola banku i stan prawny

- Bank: 609 unikalnych pytań; 609 `needs_review`, 0 `verified`.
- Wskaźnik „poprawna = jedyna najdłuższa”: 73/609 = 11,99%; maksymalny dział 14,29%.
- Nie dodano pytań i nie zmieniono poprawnych liter.
- Nie zmieniono scenariuszy ani wariantów egzaminu, ponieważ bank i klucze nie zmieniły się.
- Pakiet recenzyjny zawiera osobną kolejkę M364 z wymaganym działaniem i źródłami.

## Ograniczenie

To kontrola odporności na wygaśnięcie umowy, nie formalna recenzja prawna banku. Po 31.12.2026 ponownie odczytać aktualny wykaz UNECE i urzędowe polskie ogłoszenia, a następnie zaktualizować materiał wyłącznie na podstawie potwierdzonego statusu.
