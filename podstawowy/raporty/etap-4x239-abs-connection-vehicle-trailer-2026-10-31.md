# Etap 4x239 — połączenia ABS ciągnika i przyczepy

Data: 31.10.2026. Zakres: wyłącznie kurs podstawowy ADR.

## 1. Luka w pokryciu

W ADR-B-07-K06 były pytania o odpowiedzialność załogi, urządzenia oświetleniowe i inne obowiązki, ale brakowało praktycznego sprawdzenia ciągłości połączeń ABS w zestawie pojazdów z przyczepą o maksymalnej masie powyżej 3,5 t. Dodano pytanie sytuacyjne ADR-B-0664.

## 2. Pytanie ADR-B-0664

Pytanie opisuje kierowcę, który podczas postoju zauważa rozłączone połączenie ABS między pojazdem samochodowym i przyczepą. Poprawna odpowiedź B wskazuje, że wymagane połączenie trzeba przywrócić przed dalszą jazdą.

| Opcja | Długość | Ocena |
|---|---:|---|
| A | 148 | Błędna — sprawność hamulców zasadniczych nie znosi wymogu z ADR 8.3.8. |
| B | 128 | **Poprawna** — połączenia wskazane w 9.2.2.6 mają łączyć pojazd ciągnący i przyczepę przez cały przewóz. |
| C | 115 | Błędna — nie można odłożyć przywrócenia połączenia do końca przewozu. |

Explanation: 373 znaki, 4 zdania; najpierw praktyczny sens poprawnej odpowiedzi, następnie wyjaśnienie mylących wariantów i podstawa ADR. Poprawna B nie jest najdłuższą odpowiedzią. Status pozostaje `needs_review`.

## 3. Podstawa i ograniczenia recenzji

- ADR 2025, 8.3.8 — dla jednostki transportowej wyposażonej w ABS, złożonej z pojazdu samochodowego i przyczepy o maksymalnej masie powyżej 3,5 t, połączenia wskazane w 9.2.2.6 mają łączyć pojazd ciągnący i przyczepę przez cały czas przewozu.
- ADR 2025, 9.2.2.6 — wskazane połączenia elektryczne układu ABS.
- Dz.U. 2025 poz. 642: https://dziennikustaw.gov.pl/DU/2025/642
- Ministerstwo Infrastruktury udostępnia polskie tomy ADR 2025: https://www.gov.pl/web/infrastruktura/towary-niebezpieczne
- Niezależny tekst ADR 2025 UNECE potwierdza treść 8.3.8: https://unece.org/adr-2025-files
- Sprostowanie Dz.U. 2025 poz. 1575: https://eli.gov.pl/api/acts/DU/2025/1575/text.pdf. Wskazane punkty nie są wymienione w zakresie sprostowania.

To jest przegląd redakcyjny i ukierunkowane porównanie źródeł, a nie formalne zatwierdzenie prawne. Pełne literalne porównanie tekstu wiążącego Dz.U. oraz niezależna recenzja specjalisty ADR pozostają otwarte. Nie oznaczono pytania jako `verified`.

## 4. Synchronizacja artefaktów

- Bank: 664 rekordy ADR-B-0001–0664; ID ciągłe i unikalne; wszystkie `needs_review`, 0 `verified`.
- Blob SHA banku: `a81581438b449107fb42dcb10450acc5a69278e4`.
- Warianty i klucze egzaminów próbnych 001–005 wskazują powyższy blob SHA.
- Snapshot sequential: `review/sequential/664-664.json`.
- Snapshot legal-review: `review/legal-clauses/664-664.json`.
- Ledger prawny rozszerzony do ADR-B-0664.
- Manifest 0638, obie kolejki zagnieżdżone, README, mapa pokrycia i rejestr specjalisty zsynchronizowane.
- Lekcja i materiał instruktora ADR-B-07 zawierają objaśnienie i ćwiczenie dotyczące ABS.
- Rozkład odpowiedzi A/B/C: 228/223/213.
- Wskaźnik „poprawna odpowiedź jest jedyną najdłuższą”: 72/664 = 10,84%; maksimum działu: 13,95% (limit 18%).

## 5. Walidacja

Sprawdzono ręcznie ciągłość i unikalność ID, statusy, wyjaśnienie, długości A/B/C, rozkład kluczy, metrykę długości odpowiedzi oraz SHA egzaminów. Lokalnego checkoutu i terminala repozytorium nie udostępniono w tej sesji, dlatego nie deklaruję lokalnego PASS testów. Pełny Quality Gate CI na PR jest obowiązkową bramką przed scaleniem.
