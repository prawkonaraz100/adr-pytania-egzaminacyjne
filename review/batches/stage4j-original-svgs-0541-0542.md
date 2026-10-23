# Etap 4j — standard oryginalnych SVG i pierwsze dwa rozpoznawcze pytania

**Wejście:** świeży `main` 540 pytań / ostatni ADR-B-0540 / 8 istniejących niepustych pól `image`; 0 otwartych PR. Zakres: **tylko kurs podstawowy ADR**.

## Wynik pierwszej partii

- Utworzono własne schematy SVG bez zdjęć, skanów, zewnętrznych fontów i cudzych grafik: `assets/adr-original/adr-b-0541-label-2-2.svg` (zielony romb, butla, cyfra 2) i `assets/adr-original/adr-b-0542-label-3.svg` (czerwony romb, płomień, cyfra 3).
- Dodano dwa pytania rozpoznawcze: `ADR-B-0541` nalepka modelu 2.2, `ADR-B-0542` model 3. Każde ma `image` wskazujące naprawdę utworzony zasób i trzy warianty odpowiedzi. Sześć uzasadnień A/B/C w `review/legal-clauses/541-542.json`, migawki w `review/sequential/541-542.json`.
- Kompletny **katalog przyszłych prac** `review/batches/stage4j-visual-specifications.json`: 22 modele/odmiany nalepek (łącznie z 1.4/1.5/1.6, 2.1/2.2/2.3, 7A–7E, 9A) i 12 dodatkowych znaków/schematów (środowisko, temperatura, LQ/EQ, tablice, tunele B–E). Tylko dwa modele w tym katalogu zostały faktycznie narysowane w bieżącej partii. **Nie wpisano zaplanowanych plików do pola `image`.**

## Bezpieczeństwo, prawa i standard techniczny

- Schematy są samodzielnie napisanymi figurami SVG, bez kopiowania kompozycji cudzego pliku. Elementy wymagane normą ADR są z natury zestandaryzowane, dlatego samodzielny rysunek **wymaga wizualnego audytu specjalisty**, zanim zostanie pokazany kursantowi jako wiarygodny wzór.
- Wszystkie pliki mają opis dostępności `<title>`/`<desc>`, ostrzeżenie „schemat szkoleniowy — nie stosować jako nalepki przewozowej” i format 640×480.
- Żaden plik nie stanowi operacyjnego znaku do pojazdu, opakowania ani drogi. Przed publikacją zweryfikować kolory, symbole, geometrię, numerację i wyjątki z ADR 2025 5.2.2.2.2 i tekstu polskiego Dz.U. 2025 poz. 642 oraz sprostowania poz. 1575.
- Po scaleniu bank ma zawierać **542 pytania**, **10 pytań z `image`**, wszystkie `needs_review`, zero `verified`. Pełna realizacja wszystkich zaplanowanych ilustracji jest **otwartym kolejnym pakietem 4j**, a nie ukończonym etapem.

Nie rozpoczęto cystern ani innych kursów.