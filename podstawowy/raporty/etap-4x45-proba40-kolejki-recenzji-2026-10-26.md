# Etap 4x45 — próbka 40 explanation i przegląd dwóch kolejek recenzji

- Data: 26.10.2026.
- Punkt bazowy świeżego `main`: `72b9da2e18887258c7b426e382311ad2920d10d1`.
- Gałąź robocza: `stage4x45-przeglad-kolejek-proba40`.
- Zakres: tylko kurs podstawowy ADR.

## 1. Wynik próby 40 explanation

Próbka została wylosowana deterministycznie metodą PRNG z ziarnem `4292026`. Każde z 40 wybranych pytań przeczytano pod kątem zrozumiałości dla początkującego, dopasowania wyjaśnienia do odpowiedzi A/B/C, zbędnych powtórzeń oraz podania podstawy ADR.

**Wynik:** 4 explanation przepisano; 36 pozostawiono bez zmian, bo przekazywały sens prostym językiem i omawiały błędne odpowiedzi bez potwierdzonego problemu.

| ID | Zmiana | Powód |
|---|---|---|
| ADR-B-0379 | Przepisano explanation (351 znaków) | Usunięto wzmiankę o pasach mocujących, której nie było w żadnej błędnej opcji; wyjaśnienie odnosi się teraz do masy samego ładunku i ograniczenia do cystern. |
| ADR-B-0543 | Przepisano explanation (321 znaków) | Usunięto powtórzenie znaczenia cyfry 2; zachowano rozróżnienie emisji gazu, działania utleniającego i palności. |
| ADR-B-0371 | Przepisano explanation (339 znaków) | Usunięto powtórzenie obowiązku rozładowcy; pozostawiono jasne wyjaśnienie, dlaczego obowiązku nie przejmuje kolejny kierowca ani księgowość. |
| ADR-B-0421 | Przepisano explanation (344 znaki) | Usunięto powtórzenie, że wyłączenie nie znosi wymogu gaśnicy, i wyraźniej rozdzielono wymaganie minimum od zestawu dla innej konfiguracji. |

Pozostałe 36 ID z próbki: ADR-B-0120, ADR-B-0321, ADR-B-0532, ADR-B-0063, ADR-B-0300, ADR-B-0593, ADR-B-0053, ADR-B-0006, ADR-B-0047, ADR-B-0230, ADR-B-0272, ADR-B-0528, ADR-B-0032, ADR-B-0206, ADR-B-0349, ADR-B-0271, ADR-B-0361, ADR-B-0359, ADR-B-0506, ADR-B-0333, ADR-B-0330, ADR-B-0567, ADR-B-0054, ADR-B-0572, ADR-B-0019, ADR-B-0135, ADR-B-0440, ADR-B-0089, ADR-B-0595, ADR-B-0008, ADR-B-0199, ADR-B-0337, ADR-B-0268, ADR-B-0319, ADR-B-0275, ADR-B-0589. Nie znaleziono w nich potwierdzonego jednozdaniowego, niezrozumiałego lub „przepisowego” explanation wymagającego zmiany w tej próbce.

## 2. Kolejka 4x40 i kolejka 4x44

Ręcznie sprawdzono sformułowania wszystkich 40 pozycji w obu kolejkach. Kolejki są rankingiem do pracy specjalisty, a nie wykazem potwierdzonych błędów. Zmiany wykonano wyłącznie tam, gdzie sformułowanie samo w sobie mogło być niejasne, bez zmiany podstawy prawnej ani poprawnej litery.

| ID | Rozstrzygnięcie redakcyjne |
|---|---|
| ADR-B-0060 | Treść sprawdzona pod kątem jednoznaczności. Nie znaleziono potwierdzonego błędu wyłącznie redakcyjnego; porównanie prawne nadal pending. |
| ADR-B-0131 | Treść sprawdzona pod kątem jednoznaczności. Nie znaleziono potwierdzonego błędu wyłącznie redakcyjnego; porównanie prawne nadal pending. |
| ADR-B-0137 | Pytanie doprecyzowano: „szczególne dopuszczenie” zastąpiono konkretnym określeniem „świadectwo dopuszczenia”; odpowiedź i podstawa ADR bez zmian. |
| ADR-B-0162 | Treść sprawdzona pod kątem jednoznaczności. Nie znaleziono potwierdzonego błędu wyłącznie redakcyjnego; porównanie prawne nadal pending. |
| ADR-B-0317 | Pytanie doprecyzowano, wskazując wprost porównanie danych z progami ADR; poprawna litera i zakres klasyfikacji bez zmian. |
| ADR-B-0319 | Treść sprawdzona pod kątem jednoznaczności. Nie znaleziono potwierdzonego błędu wyłącznie redakcyjnego; porównanie prawne nadal pending. |
| ADR-B-0379 | Treść sprawdzona pod kątem jednoznaczności. Nie znaleziono potwierdzonego błędu wyłącznie redakcyjnego; porównanie prawne nadal pending. |
| ADR-B-0402 | Pytanie doprecyzowano, nazywając cel planu ochrony: ograniczenie kradzieży i nieuprawnionego dostępu; odpowiedź bez zmian. |
| ADR-B-0427 | Treść sprawdzona pod kątem jednoznaczności. Nie znaleziono potwierdzonego błędu wyłącznie redakcyjnego; porównanie prawne nadal pending. |
| ADR-B-0428 | Treść sprawdzona pod kątem jednoznaczności. Nie znaleziono potwierdzonego błędu wyłącznie redakcyjnego; porównanie prawne nadal pending. |
| ADR-B-0448 | Treść sprawdzona pod kątem jednoznaczności. Nie znaleziono potwierdzonego błędu wyłącznie redakcyjnego; porównanie prawne nadal pending. |
| ADR-B-0451 | Treść sprawdzona pod kątem jednoznaczności. Nie znaleziono potwierdzonego błędu wyłącznie redakcyjnego; porównanie prawne nadal pending. |
| ADR-B-0452 | Treść sprawdzona pod kątem jednoznaczności. Nie znaleziono potwierdzonego błędu wyłącznie redakcyjnego; porównanie prawne nadal pending. |
| ADR-B-0453 | Treść sprawdzona pod kątem jednoznaczności. Nie znaleziono potwierdzonego błędu wyłącznie redakcyjnego; porównanie prawne nadal pending. |
| ADR-B-0473 | Doprecyzowano, że chodzi o dopuszczalną maksymalną masę przyczepy; warunek i poprawna odpowiedź bez zmian. |
| ADR-B-0474 | Treść sprawdzona pod kątem jednoznaczności. Nie znaleziono potwierdzonego błędu wyłącznie redakcyjnego; porównanie prawne nadal pending. |
| ADR-B-0482 | Treść sprawdzona pod kątem jednoznaczności. Nie znaleziono potwierdzonego błędu wyłącznie redakcyjnego; porównanie prawne nadal pending. |
| ADR-B-0489 | Treść sprawdzona pod kątem jednoznaczności. Nie znaleziono potwierdzonego błędu wyłącznie redakcyjnego; porównanie prawne nadal pending. |
| ADR-B-0490 | Treść sprawdzona pod kątem jednoznaczności. Nie znaleziono potwierdzonego błędu wyłącznie redakcyjnego; porównanie prawne nadal pending. |
| ADR-B-0495 | Treść sprawdzona pod kątem jednoznaczności. Nie znaleziono potwierdzonego błędu wyłącznie redakcyjnego; porównanie prawne nadal pending. |
| ADR-B-0496 | Treść sprawdzona pod kątem jednoznaczności. Nie znaleziono potwierdzonego błędu wyłącznie redakcyjnego; porównanie prawne nadal pending. |
| ADR-B-0497 | Zastąpiono niejednoznaczne „brak wrażliwości” sformułowaniem „bardzo mała wrażliwość”; nie zmieniono sensu klasyfikacji ani odpowiedzi. |
| ADR-B-0498 | Treść sprawdzona pod kątem jednoznaczności. Nie znaleziono potwierdzonego błędu wyłącznie redakcyjnego; porównanie prawne nadal pending. |
| ADR-B-0501 | Treść sprawdzona pod kątem jednoznaczności. Nie znaleziono potwierdzonego błędu wyłącznie redakcyjnego; porównanie prawne nadal pending. |
| ADR-B-0508 | Treść sprawdzona pod kątem jednoznaczności. Nie znaleziono potwierdzonego błędu wyłącznie redakcyjnego; porównanie prawne nadal pending. |
| ADR-B-0510 | Treść sprawdzona pod kątem jednoznaczności. Nie znaleziono potwierdzonego błędu wyłącznie redakcyjnego; porównanie prawne nadal pending. |
| ADR-B-0522 | Usunięto żargon „szkolenie funkcjonalne” na rzecz „szkolenie dostosowane do jego zadań”; odpowiedź i podstawa bez zmian. |
| ADR-B-0525 | Treść sprawdzona pod kątem jednoznaczności. Nie znaleziono potwierdzonego błędu wyłącznie redakcyjnego; porównanie prawne nadal pending. |
| ADR-B-0528 | Treść sprawdzona pod kątem jednoznaczności. Nie znaleziono potwierdzonego błędu wyłącznie redakcyjnego; porównanie prawne nadal pending. |
| ADR-B-0530 | Treść sprawdzona pod kątem jednoznaczności. Nie znaleziono potwierdzonego błędu wyłącznie redakcyjnego; porównanie prawne nadal pending. |
| ADR-B-0534 | Treść sprawdzona pod kątem jednoznaczności. Nie znaleziono potwierdzonego błędu wyłącznie redakcyjnego; porównanie prawne nadal pending. |
| ADR-B-0536 | Treść sprawdzona pod kątem jednoznaczności. Nie znaleziono potwierdzonego błędu wyłącznie redakcyjnego; porównanie prawne nadal pending. |
| ADR-B-0537 | Treść sprawdzona pod kątem jednoznaczności. Nie znaleziono potwierdzonego błędu wyłącznie redakcyjnego; porównanie prawne nadal pending. |
| ADR-B-0541 | Treść sprawdzona pod kątem jednoznaczności. Nie znaleziono potwierdzonego błędu wyłącznie redakcyjnego; porównanie prawne nadal pending. |
| ADR-B-0542 | Treść sprawdzona pod kątem jednoznaczności. Nie znaleziono potwierdzonego błędu wyłącznie redakcyjnego; porównanie prawne nadal pending. |
| ADR-B-0579 | Treść sprawdzona pod kątem jednoznaczności. Nie znaleziono potwierdzonego błędu wyłącznie redakcyjnego; porównanie prawne nadal pending. |
| ADR-B-0591 | Treść sprawdzona pod kątem jednoznaczności. Nie znaleziono potwierdzonego błędu wyłącznie redakcyjnego; porównanie prawne nadal pending. |
| ADR-B-0595 | Treść sprawdzona pod kątem jednoznaczności. Nie znaleziono potwierdzonego błędu wyłącznie redakcyjnego; porównanie prawne nadal pending. |
| ADR-B-0599 | Treść sprawdzona pod kątem jednoznaczności. Nie znaleziono potwierdzonego błędu wyłącznie redakcyjnego; porównanie prawne nadal pending. |
| ADR-B-0600 | Treść sprawdzona pod kątem jednoznaczności. Nie znaleziono potwierdzonego błędu wyłącznie redakcyjnego; porównanie prawne nadal pending. |

Wszystkie pozostałe pozycje bez wpisu w kolumnie zmian pozostają do literalnego porównania z urzędowym polskim tekstem ADR 2025 i sprostowaniem. Nie poprawiano odpowiedzi ani podstaw prawnych na podstawie samego rankingu. Nie zmieniono statusów prawnych.

### Uwaga dla specjalisty

- **ADR-B-0567** z próbki 40 ma podstawę cywilnoprawną (art. 415 Kodeksu cywilnego) oraz dodatkowe odwołanie do ADR 8.2.2.3.2(k). Nie zmieniono tego odwołania: specjalista powinien ustalić, czy odwołanie ADR jest uzasadnione zakresem materiału szkoleniowego, czy należy je oddzielić od podstawy odpowiedzialności cywilnej.
- Próg, kody, wyjątki i wymagania techniczne w kolejkach 4x40/4x44 nadal wymagają potwierdzenia w urzędowym tekście; ta praca nie stanowi recenzji prawnej.

## 3. Jakość banku po zmianach

- Pytań: 609; duplikaty ID: 0.
- Statusy: 609 `needs_review`, 0 `verified`.
- Explanation: minimum 300 znaków, 0 poniżej 200.
- „Poprawna = jedyna najdłuższa”: 72/609 = **11,82%**.
- Wszystkie działy mieszczą się poniżej 16%:

| Dział | Pytania | Poprawna jedyną najdłuższą | Wskaźnik |
|---|---:|---:|---:|
| B-01 | 45 | 6 | 13,33% |
| B-02 | 56 | 7 | 12,50% |
| B-03 | 49 | 7 | 14,29% |
| B-04 | 46 | 6 | 13,04% |
| B-05 | 43 | 5 | 11,63% |
| B-06 | 45 | 5 | 11,11% |
| B-07 | 48 | 6 | 12,50% |
| B-08 | 42 | 5 | 11,90% |
| B-09 | 46 | 4 | 8,70% |
| B-10 | 55 | 4 | 7,27% |
| B-11 | 43 | 6 | 13,95% |
| B-12 | 44 | 6 | 13,64% |
| B-13 | 47 | 5 | 10,64% |

## 4. Synchronizacja pakietu i egzaminów

- Doprecyzowano 6 pytań: ADR-B-0137, 0317, 0402, 0473, 0497 i 0522. Nie zmieniono ID, poprawnych liter ani podstaw ADR.
- Zaktualizowano obie kolejki, manifest pakietu, bieżący indeks specjalisty, instrukcję recenzji i przekazanie.
- Zsynchronizowano pola migawki w wariantach egzaminu próbnego 001–005 i odpowiadających im kluczach. Treść pytań w wariantach nie wymagała zmian, ponieważ zmienione ID nie występują w tych pięciu zestawach.
- Nowy bank blob SHA: `31fa3773a0b1e96e3ef892c22897cd7bf8661a8b`.

## 5. Testy i ograniczenia

Próba lokalnego `git clone` nie powiodła się z powodu niedostępnego DNS (`Could not resolve host: github.com`). Nie deklaruję lokalnego PASS. Wymagany pełny Quality Gate musi przejść w CI dla PR przed scaleniem.

Nie dodano nowych pytań: w zakresie tej próbki i dwóch kolejek nie potwierdzono konkretnej luki programu, która uzasadniałaby nowy rekord z potwierdzoną podstawą prawną. Wszystkie pytania pozostają `needs_review`; żadne nie zostało oznaczone jako `verified`.
