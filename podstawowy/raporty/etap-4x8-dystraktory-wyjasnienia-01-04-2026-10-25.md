# Etap 4x8 — jakość dystraktorów i wyjaśnień, B-01–04

## Zakres i metoda
- Punkt wyjścia: `main` `4645de1fb054522b6d8b0a8f30ce8bf81799f760`.
- Sprawdzono wszystkie pytania przypisane do działów B-01–B-04 w `podstawowy/questions.jsonl`: 196 pytań, identyfikatory od ADR-B-0001 do ADR-B-0608 z zachowaniem przypisania modułowego (lista ID odpowiada filtrowaniu `module_id` B-01–B-04 w banku).
- Skryptowa kontrola wyjaśnień: długość, liczba zdań, początek od cytowania przepisu, niewyjaśnione skróty oraz sygnały słabych dystraktorów. Kandydaci z samym skrótem nie byli automatycznie uznawani za błąd: termin „numer UN” i skróty ADR są częścią tematu, a część wyjaśnień już rozwija je w treści.
- Ręczny przegląd kandydata na oczywiście absurdalny dystraktor wykrył ADR-B-0350 („kolor kabiny”), który nie sprawdzał kompetencji kursanta w sposób realistyczny.

## Potwierdzona poprawka
- **ADR-B-0350** — zachowano ID i poprawną literę A. Zastąpiono „kolor kabiny” wiarygodnym błędem: sprawdzeniem wyłącznie kategorii transportowej bez przepisu S. Drugi dystraktor doprecyzowano jako mylne założenie o jednym progu dla wszystkich towarów klasy 3. Explanation wyjaśnia teraz, dlaczego oba podejścia są błędne. Podstawa: ADR 8.4.1 i tabela A, kolumna (19).
- Klucze egzaminów próbnych 001–005 nie wymagały aktualizacji: nie zmieniono poprawnej litery ani ID.

## Sekcja w lekcjach
Dodano „Najczęstsze błędy kursantów” do B-01–B-04, z odwołaniami do właściwych pytań/kompetencji, przepisów oraz słowniczka:
- B-01: automatyczne zwolnienie małej ilości, pomylenie uprawnień, szkolenie do zadań, dokumenty a zakaz przewozu.
- B-02: mylenie klas, klasy a numeru UN, niepełne oznakowanie i klasyfikacja na podstawie nazwy handlowej.
- B-03: „ODPAD” a dane dokumentu, nieuzasadniona grupa III, ilość a zwolnienie, reakcja na rozlew.
- B-04: e-papierosy, samowolne otwieranie przesyłek, silnik podczas załadunku, sprawdzanie nadzoru.

## Lista pytań objętych przeglądem
Wszystkie ID z modułów B-01, B-02, B-03 i B-04 w pliku `podstawowy/questions.jsonl` (moduły: ADR-B-01–ADR-B-04). Skrypt oznaczył 17 pozycji do dodatkowej oceny heurystycznej; CI ujawniło, że poprzednie brzmienie dystraktora w ADR-B-0350 zwiększyło wskaźnik dla B-04 do 9/46 (19,57%). Wydłużono realistyczny dystraktor B tak, aby nie tworzyć wskazówki długości poprawnej odpowiedzi; po korekcie moduł B-04 wrócił do progu. Po ręcznym sprawdzeniu nie potraktowano samej obecności skrótu jako błędu, bo wyjaśnienia te rozwijają go w treści albo używają terminu poprawnie. Nie znaleziono potwierdzonej sprzeczności prawnej wymagającej zmiany klucza w tej partii. Nie zmieniono poprawnej litery.

## Preflight Quality Gate
- Bank: 609 pytań; duplikaty ID: 0.
- „Poprawna odpowiedź jest jedyną najdłuższą”: 82/609 = 13.46% (limit 18%).
- Najkrótsze explanation: 300 znaków; poniżej 200 znaków: 0.
- Statusy: 609 `needs_review`, 0 `verified`.
- Nie oznaczono żadnego pytania jako `verified`.

## Zakres recenzji prawnej
Nie zmieniano interpretacji ADR na podstawie domysłu. Zmieniono tylko brzmienie dwóch błędnych odpowiedzi i explanation w ADR-B-0350; podstawę prawną wskazano bez zmiany klucza. Pozostałe kandydaty heurystyczne pozostawiono bez zmian, gdy nie wykazano jednoznacznej wady dydaktycznej lub prawnej.