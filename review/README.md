# Niezależny przegląd ADR — zatwierdzanie pojedynczych rekordów

> **Bieżący stan (etap 4x14):** 609 pytań w `podstawowy/questions.jsonl`; wszystkie `needs_review`, 0 `verified`, 0 formalnych zatwierdzeń. Aktualny indeks: `specialist/REJESTR-AKTUALNY-0001-0609.md`; manifest: `specialist/PAKIET-0609-MANIFEST.json`. W repo znajduje się 13 lekcji, 13 materiałów instruktora, 39 scenariuszy i 5 wariantów egzaminu próbnego z osobnymi kluczami. Poniższe analizy historyczne obejmują wskazane w nich zakresy i nie zastępują indywidualnej recenzji wszystkich 609 pytań.

**Stan początkowy: 0 zatwierdzonych pytań.** `approvals.jsonl` jest celowo pusty. W projekcie **nie wolno** samodzielnie wpisywać fikcyjnych recenzentów ani dat.

## Indywidualny przegląd wariantów A/B/C

Raporty [001–060](legal-clauses/RAPORT-001-060.md), [061–090](legal-clauses/RAPORT-061-090.md), [091–120](legal-clauses/RAPORT-091-120.md) i [121–216](legal-clauses/RAPORT-121-216.md), a także osiem plików `legal-clauses/*.json` zawierają 180 osobnych uzasadnień odpowiedzi A/B/C, podstawy i wyjątki. Są to analizy redakcyjne, nie podpisane opinie fachowca ani pełne porównanie tekstu ogłoszonego w języku polskim. Nie kopiować ocen do `approvals.jsonl`.

## Pełny wstępny przebieg redakcyjny 216 pytań

[Raport wszystkich pytań](sequential/RAPORT.md) i ośmiu plików `sequential/*.json` dokumentuje przejrzenie treści A/B/C, wyjaśnień i wskazanych referencji. **Zawiera stopień faktycznej kontroli źródeł i wskazuje, że wszystkie 216 wymagają pełnego porównania prawnego oraz eksperckiej recenzji**. Nie należy kopiować ich jako pozytywnych recenzji do `approvals.jsonl`.

## Pierwsza kontrola źródłowa (bez zatwierdzeń)

[Partia 001 — 30 pytań według ryzyka](batches/risk-001.md) / [JSON](batches/risk-001.json) zawiera wstępny audyt redakcyjno-źródłowy. Potwierdza wykryte wady i poprawki, **nie stanowi protokołu pozytywnej niezależnej recenzji**. Nie należy zamieniać wpisów `preliminary-consistent` ani `edited` na `verified` bez realnego przeglądu specjalisty.

## Co jest wymagane, aby pytanie trafiło do eksportu?

1. Rzeczywisty specjalista ADR sprawdza treść, **wszystkie trzy odpowiedzi**, wyjątki prawne i wyjaśnienie na podstawie urzędowego polskiego ADR (Dz.U. 2025 poz. 642 + sprostowanie 1575), uwzględniając mające zastosowanie umowy wielostronne.
2. Redaktor zapisuje rzeczywisty protokół do `review/reports/<identyfikator>.md`, co najmniej ID pytania, datę, recenzenta, zakres sprawdzonych punktów prawa, ocenę wariantów A/B/C, wyjątki, wynik i uzasadnienie.
3. Tylko po realnej pozytywnej recenzji rekord może otrzymać `verification_status: verified`, `checked_at` i `reviewer` zgodne z protokołem.
4. Do `approvals.jsonl` dopisuje się **jedną** zgodną linię JSON z kluczami:

```json
{"id":"ADR-B-0001","content_sha256":"<hash wyliczony z zatwierdzonego rekordu>","reviewer":"<rzeczywisty recenzent>","checked_at":"YYYY-MM-DD","evidence_path":"review/reports/ADR-B-0001.md"}
```

To **przykład schematu**, nie rzeczywista recenzja. Niczego takiego jeszcze nie dodano.

5. `python scripts/release_gate.py --report` pokazuje brakujące warunki bez generowania pliku.
6. `python scripts/release_gate.py --output dist/adr-podstawowy-verified.jsonl` eksportuje tylko pytania zatwierdzone i zgodne z ich udokumentowaną wersją, jeśli jest minimum 30 oraz reprezentowane są wszystkie 13 modułów.

**Nie tworzyć plików `review/reports/` automatycznie wyłącznie w celu przejścia testów.** Nie wprowadzać sztucznych akceptacji.

## Zabezpieczenia

- SHA-256 wiąże akceptację ze wszystkimi kluczowymi polami pytania: treścią, odpowiedziami, kluczem, wyjaśnieniem, źródłami, wersją prawa i ilustracją. Zmiana jednego z nich po zatwierdzeniu blokuje eksport.
- Nie wolno wyeksportować pytań `needs_review`, `draft` lub `blocked`, nawet jeśli miały stary wpis akceptacji.
- Uruchomienia testów syntetycznych używają **fikcyjnych danych tylko w katalogach tymczasowych**, nie zapisują testowych akceptacji w repo.
- Te kontrole **nie potwierdzają kwalifikacji osoby podpisującej, jej niezależności ani poprawności prawa**; recenzja jest czynnością człowieka. Administrator musi zweryfikować uprawnienia i tożsamość recenzenta oraz wiarygodność dokumentu.
- Domyślne repo zawiera 216 `needs_review` i 0 `verified`, więc bramka eksportu powinna zgłaszać `BLOCKED`.

## Ograniczenie

Plik już wcześniej wygenerowany i niezależnie przechowywany nie jest automatycznie wycofywany po aktualizacji pytań; publikujący musi przypinać wydanie do dokładnego commita oraz ponownie uruchamiać bramkę przed każdą publikacją. Nie publikować z katalogu `dist/` bez wersjonowania.
