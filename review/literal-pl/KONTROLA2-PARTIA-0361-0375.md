# Kontrola druga — ADR-B-0361–0375

**Wynik: 0 OK / 15 POPRAW / 0 BLOKUJ.** Bank: 780 pytań. Blob SHA po wdrożeniu: `4e00ad8db1a63f644ab205910c434dae20669de8`.

## Zakres zmian

| ID | Kompetencja | Klucz | Rodzaj zmiany | Podstawa / strona Dz.U. |
|---|---|---:|---|---|
| 0361 | 04-K04 | A | Nowy temat: samozapalenie materiału po uwolnieniu, nalepka 4.2 | 5.4.3.4, instrukcje pisemne, s. 976 |
| 0362 | 04-K05 | B | Nowy temat: UWAGA 1 – stosowanie wszystkich wskazówek przy wielu zagrożeniach | 5.4.3.4, s. 975–977 |
| 0363 | 07-K02 | A | Nowy temat: dostępność EDP/EDT podczas przewozu co najmniej równoważna papierowej dokumentacji | 1.4.2.2.1(b), s. 56 |
| 0364 | 07-K02 | B | Przeredagowanie naruszenia wykrytego podczas przewozu; niezwłoczne przerwanie z zachowaniem bezpieczeństwa | 1.4.2.2.4, s. 56–57 |
| 0365 | 07-K01 | B | Przeredagowanie: zlecenie pakowania i załadunku nie zwalnia nadawcy | 1.4.2.1.2, s. 56 |
| 0366 | 07-K01 | A | Wyłącznie poprawione wyjaśnienie; stem i opcje bez zmian | 1.4.2.1.3, s. 56 |
| 0367 | 07-K05 | A | Przeredagowanie: pakujący sam oznakowuje sztuki przesyłek | 1.4.3.2(b), s. 57 |
| 0368 | 07-K05 | B | Nowy temat: definicja pakującego – kanistry jako opakowania | 1.2.1, s. 40, 43, 49 |
| 0369 | 07-K05 | A | Przeredagowanie: porównanie dokumentu przewozowego z oznakowaniem beczek i kontenera | 1.4.3.7.1(a), s. 58 |
| 0370 | 07-K05 | B | Nowy temat: definicja rozładowcy – wyjmowanie beczek z kontenera | 1.2.1, s. 45 |
| 0371 | 07-K05 | A | Nowy temat: obowiązki uczestników na tyle, na ile wiedzą lub powinni wiedzieć, niezależnie od umowy | 1.4.3, s. 57; 1.4.3.7.1, s. 58–59 |
| 0372 | 07-K05 | A | Przeredagowanie zgodnie z literą (f): kontener całkowicie rozładowany, oczyszczony i odkażony bez nalepek, znaków i tablic | 1.4.3.7.1(f), s. 59 |
| 0373 | 07-K03 | A | Nowy temat: załadowca wydaje wyłącznie towary dopuszczone do przewozu ADR | 1.4.3.1.1(a), 1.4.3.1.2, s. 57 |
| 0374 | 07-K02 | A | Przeredagowanie: przewoźnik sprawdza wymagane nalepki, znaki i tablice pojazdu | 1.4.2.2.1(f), 1.4.2.2.2–1.4.2.2.3, s. 56 |
| 0375 | 07-K02 | B | Przeredagowanie: przewoźnik może polegać na danych innych uczestników w zakresie 1.4.2.2.1(a), (b) | 1.4.2.2.2, s. 56 |

## Duplikaty i tematy zastępcze

Siedem duplikatów (0361, 0362, 0363, 0368, 0370, 0371, 0373) zastąpiono nowymi tematami w tych samych kompetencjach. Nie wykorzystano żadnej propozycji cysternowej – kurs cysternowy jest odłożony. Pozostałe osiem pytań przeredagowano w dotychczasowym podtemacie; dla 0366 zmieniono wyłącznie wyjaśnienie.

## Niezmienniki i synchronizacja

- Litery kluczy, `module_id`, kompetencje i liczebności kompetencji bez zmian.
- Wszystkie 15 rekordów ma status `needs_review`, `checked_at = null`, `reviewer = null`; 0 `verified`.
- Egzaminy próbne: wariant/klucz 001 – 0369; 002 – 0370 i 0373; 003 – 0371. Warianty 004/005 zachowują wykluczenia tych ID.
- Wskaźnik „poprawna = jedyna najdłuższa”: 35/780 (4,49%) → **34/780 (4,36%)**; maksimum działu pozostaje **7,87%**.
- Licznik pytań bez porównania po obu kontrolach partii 25: **405** (ADR-B-0376–0780).
- Bank SHA: `129d09039ee7fbee90198049cb3d733368070c77` → `4e00ad8db1a63f644ab205910c434dae20669de8`.

