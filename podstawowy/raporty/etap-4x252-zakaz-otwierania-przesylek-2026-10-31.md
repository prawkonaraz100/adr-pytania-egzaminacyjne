# Etap 4x252 — zakaz otwierania sztuk przesyłek ADR

Data: 31.10.2026  
Zakres: wyłącznie kurs podstawowy ADR  
Baza: świeży `main` przed pracą, bank 677 pytań; commit main po PR #721: `36d0bb3dc7495b8d8563d280ad78dd03f71422b4`  
Nowe pytanie: `ADR-B-0678`; poprawione pytania: `ADR-B-0011`, `ADR-B-0048`, `ADR-B-0243`.

## Najważniejsze ustalenie audytu prawnego

Dotychczasowe materiały zbyt szeroko parafrazowały ADR 8.3.3 jako zakaz obejmujący „wszystkich członków załogi”. Przepis 8.3.3 wskazuje kierowcę i pomocnika kierowcy (w oficjalnym tekście angielskim: „A driver or a driver's assistant may not open a package containing dangerous goods”). Nie należy bez podstawy rozszerzać konkretnego przepisu na każdą osobę znajdującą się w pojeździe. Podstawą polską jest Umowa ADR 2025 ogłoszona w Dz.U. 2025 poz. 642; oficjalny polski tom II ADR 2025 udostępnia Ministerstwo Infrastruktury. Dokładne brzmienie polskiego ADR 2025, 8.3.3, zostało sprawdzone w oficjalnym materiale Ministerstwa Infrastruktury: „Zabrania się kierowcy i jego pomocnikowi otwierania sztuk przesyłek zawierających towary niebezpieczne.” Potwierdza to zakres ograniczony do kierowcy i pomocnika kierowcy. Niezależna recenzja specjalisty oraz pełne porównanie wszystkich elementów pytań nadal pozostają do wykonania. Po sprawdzeniu dokładnego ustępu 8.3.3 dla czterech pytań (0011, 0048, 0243, 0678) liczba rekordów bez pobranego dokładnego ustępu wynosi 439; 17 ma kontrolę celowaną, ale pełne porównanie wszystkich elementów pytań i niezależna recenzja pozostają otwarte.

## Zmiany banku

- **ADR-B-0678** — nowa sytuacja: kierowca chce sprawdzić paczkę i prosi pomocnika kierowcy, by otworzył ją za niego. Klucz C: ani kierowca, ani pomocnik nie mogą otwierać sztuk przesyłek z towarami niebezpiecznymi.
- Explanation: 337 znaków, 4 zdania; A/B/C 78/88/76 znaków. Poprawna odpowiedź nie jest najdłuższa.
- **ADR-B-0011** — doprecyzowano odpowiedź i explanation, aby nie rozszerzać zakresu przepisu poza kierowcę.
- **ADR-B-0048** — poprawiono błędne twierdzenie, że zakaz obejmuje każdego członka załogi; prawidłowy zakres to kierowca i pomocnik kierowcy.
- **ADR-B-0243** — doprecyzowano podmiot zakazu i kontrolę oznakowania bez otwierania paczki.
- **ADR-B-0357** bez zmian; pozostaje poprawnym pytaniem o zakaz otwierania przez kierowcę w celu sprawdzenia wycieku.
- Wszystkie rekordy zachowują status `needs_review`; nic nie oznaczono jako `verified`.

## Zmiany materiałów i kontroli

- Kompetencja ADR-B-04-K02 obejmuje teraz pięć pytań: 0011, 0048, 0243, 0357 i 0678.
- Scenariusz `SC-ADR-B-04-04` skorygowano: prośba odbiorcy dotyczy pomocnika kierowcy, a kryterium oceny odnosi się do kierowcy i pomocnika kierowcy. Powiązane pytania scenariusza: ADR-B-0048, ADR-B-0357 i ADR-B-0678; ADR-B-0011 i ADR-B-0243 pozostają dodatkowymi pytaniami K02.
- Uzupełniono lekcję i materiał instruktora, usuwając nieprecyzyjne sformułowanie „wszyscy członkowie załogi”.
- Dodano snapshoty `review/sequential/4x252-0011-0678.json` i `review/legal-clauses/4x252-0011-0678.json`; suplement rejestru literalnej weryfikacji rozszerzono do ADR-B-0678.
- Warianty i klucze egzaminów próbnych 001–005 wskazują SHA banku `7c21fccb7d7e17e71fd98be534133582b54d52af`.

## Podstawa prawna i źródła

- ADR 2025, 8.3.3 — zakaz otwierania sztuk przesyłek przez kierowcę lub pomocnika kierowcy.
- Dz.U. 2025 poz. 642: https://dziennikustaw.gov.pl/DU/2025/642
- Oficjalny polski tom II ADR 2025, Ministerstwo Infrastruktury: https://www.gov.pl/attachment/b7292c03-ac9d-4f80-9a29-c22f53d847b8
- Oficjalny tekst ADR 2025 UNECE, tom II: https://unece.org/adr-2025-files

## Naprawa CI — PR #722

Pierwszy Quality Gate zakończył się błędem w `test_current_repository_structure`: skrypt zlicza osobne, niearchiwalne rejestry `review/specialist/REJESTR-*.md` i wykrył 677 wpisów przy 678 rekordach banku. Brakował osobny plik `REJESTR-0678-0678.md`; dodano go na tej samej gałęzi. Pełny bieżący rejestr `REJESTR-AKTUALNY-0001-0628.md` nie zastępuje rejestru przyrostowego używanego przez tę kontrolę. Pierwsza poprawka ujawniła w kolejnym uruchomieniu rozbieżność licznika dowodów: po przeniesieniu czterech wpisów z „nie pobrano tekstu” do „kontrola celowana — pełne porównanie oczekuje” manifest nadal zawierał 442 zamiast 439 i nie odzwierciedlał dokładnie podziału 17/222/292. Zaktualizowano oba manifesty, obie kolejki i asercję testu do bieżących liczników. Końcowy PASS zostanie odnotowany po zakończeniu najnowszego CI.

## Stan dowodów prawnych po porównaniu 8.3.3

- 4 rekordy (ADR-B-0011, 0048, 0243, 0678) mają zapisane ukierunkowane porównanie dokładnego polskiego brzmienia 8.3.3 z materiałem Ministerstwa Infrastruktury.
- Liczniki pakietu: 439 bez pobranego dokładnego ustępu; 17 kontroli celowanych z pełnym porównaniem nadal pending; 292 rekordy z zapisanym wynikiem kontroli celowanej; 222 w kategorii porównania z kopią ministerialną, z potwierdzeniem specjalisty i Dz.U. nadal pending.
- To nie jest pełna akceptacja pytań: wszystkie 678 pozostają `needs_review`, niezależna recenzja ADR nadal pending.

## Stan po partii

- Bank: **678** pytań, ID ADR-B-0001–0678; wszystkie `needs_review`, zero `verified`.
- SHA banku: `7c21fccb7d7e17e71fd98be534133582b54d52af`.
- Rozkład kluczy: A=232, B=230, C=216; „poprawna = jedyna najdłuższa”: 72/678 = 10,62% (próg ≤18%).
- Scenariusze: 42; B-03, B-04 i B-05 mają po 4, pozostałe działy co najmniej 3.
- Pełny Quality Gate, w tym egzaminy 001–005, snapshoty, mapa kompetencji i raporty, musi zakończyć się PASS przed scaleniem.
