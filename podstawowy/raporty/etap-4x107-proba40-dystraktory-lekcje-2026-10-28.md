# Etap 4x107 — próbka 40 explanation, dystraktory i regresja kursu

- Data: 2026-10-28.
- Punkt wejścia: świeży `main` `52ae58cf7343413ab3c453709a2cba3238dac2b4`.
- Zakres: wyłącznie kurs podstawowy ADR.
- Bank przed zmianami: 609 pytań, wszystkie `needs_review`, 0 `verified`.
- Lista próbki i wykluczeń: [JSON 4x107](etap-4x107-wykluczenia-proby.json), seed `41072026`.

## 1. Próbka 40 wyjaśnień

ID wybrano deterministycznie z puli po wykluczeniu wszystkich ID wymienionych w raportach 4x103–4x106 (183 unikalne ID, pula 426). Lista obejmuje 40 różnych pytań; żadne nie występuje w zestawie wykluczeń.

| Kontrola przed zmianą | Wynik |
|---|---:|
| Wyjaśnienia przeczytane w kontekście pytania, opcji A/B/C i podstawy ADR | 40/40 |
| Długość explanation | 302–427 znaków |
| Liczba zdań | 3–5 |
| Najdłuższe zdanie | 31 słów |
| Explanation poniżej 200 znaków | 0 |
| Wyjaśnienia wymagające redakcji struktury/niezrozumiałości przed zmianą opcji | 0 |
| Wyjaśnienia dopasowane po potwierdzonej korekcie dystraktorów | 4 |

Większość wyjaśnień już prostym językiem wyjaśniała poprawną odpowiedź, typowe pomyłki i podstawę ADR. Nie przepisywano dobrych wyjaśnień wyłącznie dla liczby zmian.

## 2. Potwierdzone poprawki dystraktorów i explanation

| ID | Problem | Poprawka | Podstawa |
|---|---|---|---|
| ADR-B-0009 | „brak silnego zapachu” i „przykryć kartonem” były zbyt łatwe do odrzucenia bez rozumienia ryzyka | Zastąpiono je realistycznymi błędami: uznaniem małej pozostałości za bezpieczną i odłożeniem oczyszczenia po odizolowaniu miejsca. Wyjaśnienie mówi, dlaczego oba działania nie zastępują oczyszczenia. | ADR 7.5.8.1 |
| ADR-B-0329 | Odpowiedzi „dopisać ODPAD” i „pojazd ma gaśnicę” były mało wiarygodne w pytaniu o niedopuszczony materiał | Zastąpiono je typowymi pomyłkami: wyborem numeru UN na podstawie przypuszczeń oraz uznaniem właściwego opakowania za zgodę na przewóz. Klucz B bez zmian. | ADR 2.1.3.5.5 |
| ADR-B-0401 | Dystraktor skupiający się na adresie biura i księgowości był odległy od rzeczywistej oceny ryzyka | Zastąpiono go częściowo prawdziwą, lecz niepełną oceną: uwzględnieniem postojów i przeładunków przy pominięciu ładunku pozostawionego w pojeździe. Klucz C bez zmian. | ADR 1.10.3.2.2(c) |
| ADR-B-0441 | Błędne odpowiedzi przypisywały zgłoszenie kierowcy lub odbiorcy, zamiast sprawdzać rozróżnienie ról państw | Dystraktory przeredagowano na pomyłkę państwa, na którego terytorium leży odcinek, oraz założenie, że zgłoszenie składa każde państwo uczestniczące. Explanation dopasowano do tych opcji. Klucz C bez zmian. | ADR 1.1.4.5.2 |

Zachowano wszystkie ID, poprawne litery i podstawy ADR. Nie wprowadzono nowych twierdzeń prawnych ani nie zmieniono statusu recenzji.

## 3. Spójność lekcji i scenariuszy

- Lekcje: **13/13** sprawdzone skryptowo pod kątem ID pytań. Wszystkie odwołania istnieją, należą do właściwego modułu, a każde pytanie banku jest wymienione w lekcji swojego działu.
- Scenariusze: **39/39**. Każdy ma co najmniej 3 kroki kierowcy, powiązane pytania, kryteria oceny, typowe błędy i podstawę ADR. Nie znaleziono nieistniejących ID ani pytań przypisanych do innego działu.
- Pokrycie programu: brak potwierdzonej luki w mapie 104 kompetencji teoretycznych, która uzasadniałaby dopisanie nowego pytania w tej partii. Nie dodawano pytań tylko dla zwiększenia liczby.

## 4. Egzaminy próbne i migawki audytu

Zaktualizowano `source_bank_head` wariantów i kluczy 001–005 do nowego blobu banku. Zmienione pytania nie występują w tych 150 pozycjach egzaminacyjnych, więc nie trzeba było przestawiać opcji w arkuszach; aktualizacja metadanych zapewnia zgodność z bieżącą migawką banku. Odświeżono snapshoty sekwencyjne i A/B/C dla ADR-B-0009, ADR-B-0329, ADR-B-0401 i ADR-B-0441.

## 5. Quality Gate — preflight

- Bank: 609 unikalnych ID, 609 `needs_review`, 0 `verified`.
- Explanation minimum: 300 znaków; poniżej 200: 0.
- Rozkład poprawnych liter: A=206, B=207, C=196.
- Poprawna odpowiedź jako jedyna najdłuższa: **72/609 = 11,82%**.
- Maksimum w dziale: **14,29%**; B-03 po korekcie: **6/49 = 12,24%**.
- Warianty 001–005: 30 pytań każdy, brak powtórzeń w wariancie, zgodność kluczy wymaga potwierdzenia przez CI.

## 6. Testy i ograniczenia

W tej sesji nie można było sklonować repozytorium do lokalnego środowiska z powodu niedostępności sieci dla lokalnego klienta. Wykonano preflight skryptowy na plikach pobranych z GitHub: metryki banku, długość explanation, referencje wszystkich lekcji i scenariuszy oraz metadane wariantów. PR pozostaje niescalony do czasu PASS pełnego Quality Gate w GitHub Actions. Wszystkie pytania pozostają `needs_review`; niezależna recenzja prawna nadal jest wymagana.

Nie rozpoczęto kursu cystern ani innego kursu.
