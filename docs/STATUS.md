# Status i dziennik decyzji

## 2026-10-22 — start projektu

- Repozytorium: prawkonaraz100/adr-pytania-egzaminacyjne (publiczne, decyzja właściciela).
- Zakres aktywny: polski kurs ADR **początkowy podstawowy**, pytania autorskie i objaśnienia.
- Kolejny zakres: ADR **specjalistyczny — cysterny**; nie zaczynamy, zanim podstawa nie przejdzie przeglądu jakości.
- Oficjalny program: 13 pozycji a–m, 18 godzin lekcyjnych teorii, oddzielne ćwiczenia praktyczne.
- Egzamin państwowy: pisemny, 30 pytań / 3 odpowiedzi / 60 minut / próg 20 poprawnych.
- Stan banku pytań po inicjalizacji: **0 zweryfikowanych**, 0 gotowych do publikacji.
- Kwota 400 pytań: **robocza propozycja planistyczna**, nie obowiązek prawny.
- Pełna urzędowa baza pytań: **brak potwierdzenia publicznego udostępnienia**.
- Polityka treści: osobno wymagana walidacja strukturalna, prawna i redakcyjna.
- Przepisy główne: ADR 2025 + prawo polskie. Dla szczegółowych pytań stosować konkretne źródła i datę sprawdzenia.

## Jak aktualizować ten plik

Każdy ukończony etap wpisywać z datą, identyfikatorem commita, dokładnymi wynikami walidacji i CI. Nie oznaczać prac jako DONE bez potwierdzonego wyniku. Zapis zmian decyzji zachowywać, nie nadpisywać historii.

## 2026-10-22 — etap 1 / partia 001

- **Zapisano mapę przepisów** 13 tematów w `docs/MAPA-PUNKTOW-ADR-2025.md` (commit `7e0249849de848125128284328f35f61e4a4f9b8`).
- **Zapisano 39 autorskich pytań**, po 3 na każdy temat, w `podstawowy/questions.jsonl` (commit `96e7c9b98e9a5a141d207a4891031b6929b6e2ec`).
- Wszystkie 39 rekordów: `needs_review`. W szczególności **0 verified**, 0 zwolnionych do publikacji.
- Przeprowadzono kontrolę spójności JSONL przez odczyt pliku z GitHub i walidację struktury w kodzie pomocniczym: 39 rekordów, 13 modułów, po 3 pytania, unikalne identyfikatory, 3 odpowiedzi, poprawny klucz, metadane źródeł: 0 usterek w tym przeglądzie.
- **Niepotwierdzony CI PASS** i brak eksperckiej recenzji prawnomerytorycznej. GitHub Actions ma konfigurację, ale wynik jej uruchomienia nie został w tym kroku odczytany.
- Pytania uwzględniają punkty referencyjne ADR 2025; każdy podpunkt i wyjątek wymagają końcowej lektury pełnego tekstu Dz.U. 2025 poz. 642, a także sprawdzenia sprostowań.
- Podstawa prawna ADR 2025 ogłoszona w **Dz.U. 2025 poz. 642** została dodana do mapy — to ważniejsze źródło niż pomocnicze pliki na stronie MI.
- Bieżące zadania: #1 dokończenie mapy i weryfikacja pełnych ustępów, #2 audyt partii 001.
- Kurs cysterny: nadal **NIE ROZPOCZĘTO**.

**Następny wymagany krok:** pełna kontrola 39 pytań z dokładnym brzmieniem ADR 2025, rozstrzygnięcie wyjątków i niezależna recenzja fachowa; następnie walidator Python i potwierdzony wynik CI.
