# ADR 2025 — mapa przepisów i zagadnień do podstawowego

**Stan:** 2026-10-22. Pierwsza mapa robocza, wymagająca kontroli zgodności numerów punktów i wyjątków w pełnym polskim tekście ogłoszonym w Dz.U. z 2025 r. poz. 642 (łącznie ze sprostowaniami). **Mapa jest punktem startowym, nie zakończoną recenzją każdego przepisu.**

## Zasada czytania tabeli

„Punkt ADR” określa **adres do audytu i źródło zagadnienia**, nie oznacza, że każda możliwa odpowiedź została już sprawdzona w całym dokumencie. Wersja zatwierdzona dla produkcji wymaga dokładnej kontroli brzmienia konkretnego ustępu. Polską podstawę ustawową i wymogi kursu weryfikować równolegle.

| Moduł | Przykładowe podtematy | Mapa punktów do kontroli w ADR 2025 | Ryzyko |
|---|---|---|---|
| ADR-B-01 | Ogólne wymogi i wyłączenia; szkolenie; definicje; progi 1.1.3.6 | 1.1.3; 1.1.3.6; 1.2.1; 1.3; 8.2.1 | Wysokie: wyjątki, warunki i progi ilościowe |
| ADR-B-02 | Klasy, zagrożenia, numery UN, grupy pakowania | 2.1; 2.2.1–2.2.9; 3.2 tabela A | Średnie: wyjątki zależne od konkretnego towaru |
| ADR-B-03 | Materiały zagrażające środowisku; odpady; wycieki | 2.2.9.1.10; 5.2.1.8; 5.4.1.1.3; 7.5.8 | Wysokie: warunki oznakowania i klasyfikacja odpadów |
| ADR-B-04 | Palenie, urządzenia iskrowe, silnik przy przeładunku | 7.5.9; 8.3.3–8.3.6 | Niskie/średnie: wyjątek dotyczący silnika |
| ADR-B-05 | Instrukcje pisemne; wypadek; środki ochronne; gaśnice | 5.4.3; 8.1.4; 8.1.5; 8.2.2.3 | Wysokie: zachowania zależą od rodzaju zagrożenia |
| ADR-B-06 | Nalepki, znaki, pomarańczowe tablice i cyfry | 5.2.1–5.2.2; 5.3.1–5.3.2 | Średnie: rodzaj pojazdu, opakowanie, wyłączenia |
| ADR-B-07 | Nadawca, przewoźnik, odbiorca, załadowca, kierowca | 1.4.1; 1.4.2.1–1.4.2.3; 1.4.3.1 | Średnie: odpowiedzialność podzielona |
| ADR-B-08 | Minimalne gaśnice, kliny, lampy, kamizelki, rękawice | 8.1.4; 8.1.5.1–8.1.5.3; 8.3.4 | Wysokie: masa pojazdu i zwolnienia |
| ADR-B-09 | Wspólny załadunek, żywność, mocowanie i rozładunek | 7.5.1; 7.5.2; 7.5.4; 7.5.7; 7.5.8 | Wysokie: warunki wyłączeń |
| ADR-B-10 | Przewóz łączący transport drogowy z morskim/kolejowym | 1.1.4.2; 1.1.4.3; 5.4.1.1.7 | Wysokie: uznawanie oznakowania i dokumentów |
| ADR-B-11 | Kategorie tuneli, znak drogowy, kody tunelowe | 1.9.5.3; 3.2 tabela A kol. 15; 5.4.1.1.1 (k); 8.6.3–8.6.4 | Wysokie: różne przypadki przy cysternach i sztukach przesyłek |
| ADR-B-12 | Kradzież, identyfikacja załogi, bezpieczne przechowywanie | 1.10.1; 1.10.2; 1.10.3 | Średnie: towary wysokiego ryzyka |
| ADR-B-13 | Dokument przewozowy, instrukcje i świadectwa | 5.4.1; 5.4.3; 8.1.2; 8.2.1.8 | Wysokie: informacje warunkowe |

## Protokół kontroli mapy

Dla każdej pozycji w tabeli należy:
1. Otworzyć i porównać tekst ogłoszony w Dz.U. z 2025 r. poz. 642 z pomocniczym polskim tłumaczeniem MI, uwzględnić sprostowania.
2. Dla twierdzenia wykorzystywanego w pytaniu zanotować **dokładny podpunkt** (np. 8.1.4.1 lub 5.4.3.2) oraz wyjątki.
3. Upewnić się, że pytanie nadaje się do kursu **podstawowego**, a nie wyłącznie do cystern.
4. Zapisać datę sprawdzenia, osobę recenzującą oraz wynik; dopiero wówczas zmienić needs_review na verified.
5. Jeżeli źródła się różnią, przejść na blocked i wyjaśnić rozbieżność w dokumencie lub issue.

## Potwierdzone dokumenty główne

- **Dz.U. 2025 poz. 642** — rządowe ogłoszenie tekstu ADR 2025: https://eli.gov.pl/api/acts/DU/2025/642/text.pdf
- **Ministerstwo Infrastruktury** — pomocnicze PDF po polsku, ADR 2025 i sprostowanie: https://www.gov.pl/web/infrastruktura/towary-niebezpieczne
- **UNECE** — wydanie referencyjne ADR 2025, t. 1 i 2: https://unece.org/adr-2025-files
- **Dz.U. 2021 poz. 2150** — polski program kursu (załącznik nr 1, s. 6): https://eli.gov.pl/api/acts/DU/2021/2150/text.pdf
- **Dz.U. 2024 poz. 964** — polskie zasady egzaminu (§ 9–11): https://eli.gov.pl/api/acts/DU/2024/964/text.html

## Weryfikacja źródeł w tej iteracji

Przejrzano zakres kursu w oficjalnym załączniku i podstawę egzaminu; wyszukano potwierdzenia 1.4.2.2.6, 5.4.1.1.1, 5.4.3, 5.3.2, 8.1.4, 8.1.5, 8.3 oraz zakresów innych bloków w ADR 2025. **Nie przeprowadzono jeszcze pełnej recenzji eksperckiej wszystkich 13 bloków.** 
