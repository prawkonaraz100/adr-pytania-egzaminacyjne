# Audyt luk pokrycia kursu ADR podstawowego — 24.10.2026

## Zakres i metoda

Sprawdzono świeży `main` `3d9286d2ae1e384ffc6e36cfc12f32af6605f113`, bank pytań, wewnętrzną mapę 106 kompetencji, program kursu, dokument pokrycia, skrypt walidujący i scenariusze praktyczne. Urzędowy program obejmuje 13 tematów a–m, 18 godzin lekcyjnych teorii i ćwiczenia praktyczne (Dz.U. 2021 poz. 2150, zał. 1). Wewnętrzne cele liczebności pytań są planem redakcyjnym, nie wymogiem prawa.

## Wynik bazowy przed uzupełnieniem

- Bank: 545 unikalnych pytań, wszystkie `needs_review`; brak `verified`.
- Mapa: 106 kompetencji (103 teoretyczne i 3 praktyczne); wszystkie cele teorii mają pytania przypisane, a każde pytanie jest przypisane do kompetencji. Nie stwierdzono luk binarnych „kompetencja bez żadnego pytania”.
- To nie dowodzi jednak pełnej głębokości programu, poprawności prawnej ani wystarczającej różnorodności sytuacji. Wewnętrzna matryca pozostaje `draft_coverage_map_not_approved`.
- Różnice względem wewnętrznych kwot planistycznych: B-06 oznakowanie 35/45 (−10), B-08 wyposażenie 36/40 (−4), B-09 załadunek i mocowanie 39/45 (−6). Są to cele projektu, nie oficjalne minima. Pozostałe działy mają liczby równe lub wyższe od swoich roboczych kwot; dalsza produkcja powinna priorytetowo uzupełniać głębokość i różnorodność, nie zwiększać bez celu całej bazy.
- Luka jakościowa krytyczna: brak niezależnej recenzji eksperta ADR; walidacja strukturalna nie jest zatwierdzeniem prawnym.
- Luka dydaktyczna: potrzebne są więcej sytuacyjnych decyzji przed załadunkiem, odczyt oznakowania dużego formatu, rozróżnienie dopuszczenia towaru i zgodności pojazdu oraz warunków przewozu luzem.
- Praktyka: trzy scenariusze są materiałem dla instruktora, nie dowodem odbycia ćwiczeń; wymagają rzeczywistego odbioru i ewidencji.
- Materiały wizualne: bank nie zastępuje kompletnego, legalnego zestawu ilustracji nalepek/tablic ani przykładowych dokumentów przewozowych.

## Priorytety i działanie

| Priorytet | Dział | Luka głębokości | Działanie |
|---|---|---|---|
| P1 | ADR-B-06 | Nalepki dużego formatu: widoczność, kompletność, czytelność i pozostałości po rozładunku | Dodano 0546–0550; ADR 5.3.1 |
| P1 | ADR-B-08 | Świadectwo dopuszczenia: wymaganie zależne od typu pojazdu, ważność i dokumenty | Dodano 0551–0553; ADR 9.1.3.1 i 8.1.2.2 |
| P1 | ADR-B-09 | Kontrola przed załadunkiem oraz dopuszczalność i warunki przewozu luzem | Dodano 0554–0560; ADR 7.5.1.2, 7.3 i tabela A |
| P2 | Wszystkie 13 działów | Pokrycie robocze istnieje, ale nie jest niezależnym potwierdzeniem poprawności i wyczerpania wyjątków | Audyt kompetencja po kompetencji przez eksperta; bez automatycznej zmiany statusów |
| P2 | 13 lekcji | Szkice istnieją, ale nie są niezależnie zatwierdzone | Przegląd treści, wyjątków, przykładów i grafik |
| P2 | Praktyka P1–P3 | Materiał nie potwierdza przeprowadzenia zajęć | Odbiór instruktora i protokół rzeczywistych ćwiczeń |

## Dodane pytania 0546–0560

- B-06-K09: 0546–0550.
- B-08-K08: 0551–0553.
- B-09-K08: 0554, 0555, 0560.
- B-09-K09: 0556–0559.

Każdy rekord zawiera trzy opcje, jeden klucz, wyjaśnienie 300–500 znaków, podstawę ADR 2025 i status `needs_review`. Dodatkowo zbalansowano długości wariantów A/B/C w nowej partii: żaden z 15 kluczy nie jest jedyną ściśle najdłuższą opcją; klucze nie zostały zmienione. Mapa została zaktualizowana wyłącznie przez dopisanie identyfikatorów do odpowiednich kompetencji. `checked_at` i `reviewer` pozostają puste; nie nadano `verified`.

## Następne kroki

1. Uruchomić pełny CI i poprawić wszystkie błędy, nie osłabiając bramek.
2. Dokończyć kolejne partie zgodnie z raportem i sprawdzić liczbę pytań w 13 działach.
3. Przeprowadzić niezależną kontrolę polskiego tekstu ADR 2025 (Dz.U. poz. 642 wraz ze sprostowaniem poz. 1575) oraz każdego wariantu A/B/C.
4. Zatwierdzić lekcje i ćwiczenia przez uprawnionego instruktora; quiz nie zalicza praktyki.
5. Nie rozpoczynać kursu cysterny — zakres pozostaje wyłącznie podstawowy.

Źródła: [program kursu (Dz.U. 2021 poz. 2150)](https://eli.gov.pl/api/acts/DU/2021/2150/text.pdf), [ADR 2025 (Dz.U. 2025 poz. 642)](https://dziennikustaw.gov.pl/DU/2025/642), [sprostowanie (Dz.U. 2025 poz. 1575)](https://eli.gov.pl/eli/DU/2025/1575/ogl/pol/pdf).
