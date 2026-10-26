## Bieżąca migawka — etap 4x46 (26.10.2026)

- Bank blob SHA: `6de0159ce4d80799104a01170c42e363623045eb`.
- Bank: 609 `needs_review`, 0 `verified`, brak formalnych zatwierdzeń.
- Próba 60 nowych pytań względem 4x45: 8 redakcyjnych korekt explanation; pełne porównanie z urzędowym polskim ADR i niezależna recenzja pozostają otwarte.
- [Raport 4x46](../podstawowy/raporty/etap-4x46-proba60-i-synchronizacja-2026-10-26.md).

## Bieżąca migawka — etap 4x45 (26.10.2026)

- Bank blob SHA: `31fa3773a0b1e96e3ef892c22897cd7bf8661a8b`.
- 609 pytań, wszystkie `needs_review`, zero `verified`; nie ma formalnych zatwierdzeń.
- Redakcyjne korekty próby 40 i sformułowań z kolejek nie stanowią recenzji prawnej. 376 porównań literalnych pozostaje nierozstrzygniętych; 40 wpisów kolejek 4x40/4x44 nadal wymaga sprawdzenia przez specjalistę.

# Niezależny przegląd ADR — zatwierdzanie pojedynczych rekordów

- [Etap 4x44 — druga kolejka priorytetowa recenzji prawnej](../podstawowy/raporty/etap-4x44-druga-kolejka-recenzji-2026-10-26.md)

- [Etap 4x43 — aktualność pakietu recenzyjnego](../podstawowy/raporty/etap-4x43-aktualnosc-pakietu-recenzyjnego-2026-10-26.md)

## Etap 4x25 — czytelność explanation i zgodność egzaminów

- [Raport końcowy 4x25](../podstawowy/raporty/etap-4x25-raport-koncowy-2026-10-26.md): 609 pytań sprawdzonych w partiach; jedna korekta końcowa ADR-B-0197; 0 potwierdzonych duplikatów.
- [Rejestr zbiorczy 4x24 bez cytatu MI](specialist/ETAP-4X24-POZYCJE-BEZ-CYTATU-MI.md): 121 ID według świeżego indeksu; bez dalszego wydobywania cytatów.


## Etap 4x25 — audyt czytelności explanation

- [Raport partii ADR-B-0001–0050](../podstawowy/raporty/etap-4x25-explanation-0001-0050-2026-10-26.md): przeczytano 50 pytań, 0 zmian, 0 potwierdzonych duplikatów, 4 przeczenia sprawdzone.
- [Zbiorczy rejestr 4x24 — rekordy bez dosłownego fragmentu MI](specialist/ETAP-4X24-POZYCJE-BEZ-CYTATU-MI.md): 121 ID według świeżego indeksu; dalsze poszukiwania cytatów zakończone.


> **Bieżący stan (etap 4x42, 26.10.2026):** bank blob SHA `8a16afb47c5d5a9e460092b7e474b4a3e8a5a8d9`; 609 pytań w `podstawowy/questions.jsonl`; wszystkie `needs_review`, 0 `verified`, 0 formalnych zatwierdzeń. Aktualny indeks: `specialist/REJESTR-AKTUALNY-0001-0609.md`; manifest: `specialist/PAKIET-0609-MANIFEST.json`. W repo znajduje się 13 lekcji, 13 materiałów instruktora, 39 scenariuszy, słowniczek 90 haseł i 5 wariantów egzaminu z kluczami. Kolejka 4x40 ma 20 priorytetów; kolejka uzupełniająca 4x44 ma następne 20 unikalnych ID z listy 121 rekordów bez cytatu MI. Każda odpowiedź w kluczach zawiera `lesson_path` do właściwej lekcji; blokujący test sprawdza wszystkie 150 odnośników. W każdym wariancie wskaźnik „poprawna = jedyna najdłuższa” wynosi 0/30; rozkład A/B/C to 10/10/10. [Raport końcowy 4x20](../podstawowy/raporty/etap-4x20-raport-koncowy-2026-10-26.md); [raport 4x42](../podstawowy/raporty/etap-4x42-scenariusze-egzaminy-2026-10-26.md). Analizy historyczne nie zastępują niezależnej recenzji wszystkich pytań.

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


## Aktualizacja etapu 4x18 — egzamin próbny i priorytety recenzji

Stan migawki banku po wyrównaniu dystraktorów: 609 pytań, wszystkie `needs_review`, 0 `verified`, 0 formalnych akceptacji. Arkusze 001–005 i ich klucze są przypięte do bieżącego Git blob SHA banku; test blokujący sprawdza aktualność migawki, kompletność 30 pytań, wszystkie 13 działów, zgodność poprawnej litery i explanation z bankiem oraz brak duplikatów.

**Priorytet do niezależnej kontroli prawnej:** pytania zależne od wartości liczbowych, wyposażenia, terminów kontroli, postojów i ochrony przewozu, w szczególności ADR-B-0073, ADR-B-0074, ADR-B-0253, ADR-B-0283, ADR-B-0420, ADR-B-0422, ADR-B-0484, ADR-B-0144, ADR-B-0249, ADR-B-0274, ADR-B-0275, ADR-B-0300, ADR-B-0304 i ADR-B-0305. To lista priorytetowa, nie wyczerpująca: wszystkie 609 pytań nadal wymagają indywidualnej recenzji. Dla pytań wrażliwych na aktualizację ADR należy też wykorzystać rejestry `podstawowy/raporty/etap-4x9-wrazliwosc-01-04.json`, `...-05-08.json` i `...-09-13.json`.

Nie zmieniaj `verification_status` na `verified` automatycznie. Zmiana tego statusu wymaga rzeczywistej recenzji specjalisty, potwierdzenia polskiego tekstu urzędowego ADR i sprostowania, oceny każdej odpowiedzi A/B/C oraz wpisu z prawdziwą tożsamością recenzenta w procesie zatwierdzania. Wskaźniki jakości, testy i automatyczne porównania nie stanowią opinii prawnej.


## Etap 4x19 — uzgodnienie licznika dowodów

Rejestr 609 rekordów rozbija stan na 376 wpisów, gdzie dokładny tekst urzędowy nie został pobrany, 10 porównań ukierunkowanych oczekujących na pełne porównanie i 223 wpisy z zapisanym wynikiem porównania ukierunkowanego. **To nie oznacza 223 pytań zatwierdzonych prawnie:** wszystkie 609 pozostają `needs_review`, a recenzja A/B/C przez specjalistę jest pending. Szczegóły: [raport etapu 4x19](batches/etap-4x19-uzgodnienie-pakietu-2026-10-25.md).
