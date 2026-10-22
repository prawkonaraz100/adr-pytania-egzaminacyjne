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

## 2026-10-22 — kontrola techniczna partii 001 (PR #3)

- Raport QA: `docs/QA-PARTIA-001.md`, PR #3 **merged** jako `125133b21437c1dd913232b7bd6149cabe974772`.
- GitHub Actions: [Quality Gate run #14](https://github.com/prawkonaraz100/adr-pytania-egzaminacyjne/actions/runs/39828372547), wynik **success** dla commita PR `e90bab7b4b79f549f509231a4b373055cd509628`.
- Kroki tego uruchomienia: wczytanie repo, konfiguracja Python, składnia JSON schema, testy jednostkowe, walidacja bazy — **success** według danych zadania `structure-and-tests`.
- Bramka techniczna potwierdza tylko strukturę, a nie poprawność przepisów.
- Końcowy HEAD po aktualizacji tego pliku może mieć osobny przebieg CI; nie przenosić automatycznie statusu PASS na nowszy commit.
- Nadal: **39 needs_review, 0 verified** — prawny audyt merytoryczny otwarty w #2.

## 2026-10-22 — przegląd treści partii 001 (PR oczekuje na CI)

- Wpisy poddane analizie: **39/39**, wyniki per ID w `docs/AUDYT-MERYTORYCZNY-PARTIA-001.md`.
- Bezpośrednio skonfrontowano 24 tezy z tekstem ADR 2025 i źródłami aktualnymi; 15 nadal wymaga pełnego sprawdzenia i wyjątków.
- Poprawiono pytania 0007, 0008, 0009, 0018, 0022, 0029, 0030, 0033, 0035; w #0009 także odpowiedź B.
- Ujęto sprostowanie ADR 2025: **Dz.U. 2025 poz. 1575**, w tym uwagę o pkt 8.2.2.7.2.3. Nie jest to podstawa do niezweryfikowanego dopisywania odpowiedzi.
- Linki prawne do 39 pytań kierują teraz do stabilnej strony oficjalnego ogłoszenia (Dz.U. 2025 poz. 642), a wskazanie punktu pozostaje w `reference`.
- Statusy pozostają: **39 needs_review / 0 verified**; brak niezależnego eksperta ADR i pełnego audytu każdego pkt PL.
- Bramka merytoryczna nadal **OPEN**; techniczną sprawdzić na PR i HEAD po scaleniu.
