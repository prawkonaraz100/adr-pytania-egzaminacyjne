# Egzamin próbny ADR podstawowego — tryb wewnętrzny, bez publikacji

**Stan 23.10.2026 (po 4m):** 545 pytań `needs_review`, **0 zatwierdzonych**. System świadomie **odmawia wygenerowania prawdziwego arkusza z banku**. Nie ma publicznego testu, nie utworzono żadnego pliku z niezatwierdzonymi pytaniami do dystrybucji.

## Tryb roboczy

Po rzeczywistej niezależnej recenzji, utworzeniu właściwych dowodów i przejściu istniejącej `scripts/release_gate.py` można wygenerować **wewnętrzny** zestaw 30 pytań. Mechanizm `scripts/mock_exam.py` korzysta wyłącznie z `eligible()` tej samej bramki, wymaga co najmniej 30 zatwierdzonych rekordów oraz co najmniej jednej pozycji z każdego z 13 działów. Losuje 30 **unikalnych** rekordów przy podanym ziarnie. Zawiera domyślną, **projektową** konfigurację 60 minut i 20 poprawnych odpowiedzi jako próg; nie oznacza to potwierdzenia aktualnych urzędowych zasad egzaminu.

## Obsługa

```bash
python scripts/mock_exam.py --report
# Obecnie: BLOCKED: brak zatwierdzonych pytań
python scripts/mock_exam.py --seed 2025 --output local-private/adr-basic-mock.json
# Obecnie: kod wyjścia 1, brak pliku
```

Plik jest wyłącznie **wewnętrzny**. Zawiera pytania i klucz odpowiedzi w polu `answer_key_internal_only`; nie udostępniać publicznie ani nie umieszczać we frontendzie. Przed wdrożeniem produkcyjnym potrzebne odrębne bezpieczne przechowywanie klucza, identyfikacja wersji i formalna zgoda wydawnicza. Nie przechowywać wygenerowanych arkuszy w repo.

## Testy bezpieczeństwa

`tests/test_mock_exam.py` tworzy dane **syntetyczne wyłącznie w katalogach tymczasowych** i sprawdza:
- odmowę generowania arkusza z `needs_review`, nawet gdy istnieje 39 rekordów;
- brak tworzenia jakiegokolwiek pliku wyjściowego przy blokadzie;
- powtarzalny dobór i reprezentację 13 działów;
- utworzenie wewnętrznego arkusza tylko po przejściu tej samej kontroli dowodów co `release_gate.py`.

Wszystkie rekordy banku pozostają `needs_review`. Żaden test syntetyczny nie stanowi rzeczywistej akceptacji specjalisty ADR.


## Aktualizacja etapu 4l — ADR-B-0520–0542 i grafiki SVG

Bieżący bank zawiera **542 pytania**, wszystkie `needs_review`. Mimo dodania autorskich rysunków SVG generator **nie produkuje** egzaminu z niezatwierdzonych treści. Wewnętrzny egzamin może zawierać opcjonalną ścieżkę `image` dopiero po przejściu istniejącej `release_gate.eligible()` i potwierdzeniu istnienia pliku SVG w `assets/`. Jeśli wybrany zatwierdzony rekord ma nieistniejący lub niebezpieczny plik, generowanie kończy się bez zapisu. Wynik wewnętrzny zawiera `source_bank_sha256`, pozwalający zidentyfikować bajtową wersję źródłowego banku, a nie zatwierdzenie prawne. Klucz `answer_key_internal_only` nie nadaje się do umieszczania w ogólnodostępnym frontendzie.

Specjalista korzysta z `review/specialist/REJESTR-AKTUALNY-0001-0542.md` i rejestru otwartych porównań `review/legal-polish/stage4k-literal-verification-ledger-0001-0542.json`. Próby w `tests/test_mock_exam.py` są wyłącznie syntetyczne i nie podnoszą statusu żadnego rzeczywistego pytania. Ustawienia czasu i progu egzaminu są konfiguracyjnym szkicem, nie poświadczeniem obowiązujących urzędowych zasad.


## Aneks 4m — aktualna blokada i źródła recenzji

Aktualny bank to **545 pytań**, 545 `needs_review`, **0 verified**. Aktualny indeks: `review/specialist/REJESTR-AKTUALNY-0001-0545.md`, manifest `review/specialist/PAKIET-0545-MANIFEST.json`, otwarty rejestr kontroli PL `review/legal-polish/stage4m-literal-verification-ledger-0001-0545.json`. Wcześniejsze odnośniki do 542 rekordów pozostają historycznym opisem etapu 4l.

Brak poświadczonych wyników recenzji oznacza, że `scripts/mock_exam.py` nadal **odmawia generowania realnego arkusza**. Wskaźnik nadmiernej długości poprawnej odpowiedzi 365/545 (67,0%) jest nadal powyżej planowanego 40%; wyniku ostrzegawczego z CI nie utożsamiać z zatwierdzeniem jakości.


## Aneks 4m — wynik partii ADR-B-06

Po redakcji pięciu wariantów w module ADR-B-06, lokalny próg długości odpowiedzi jest spełniony (**14/35 = 40,0%**); aktualny wskaźnik globalny to **365/545 = 67,0%**. Nadal brak 545 autoryzacji prawnych, wszystkie pytania `needs_review`. Publiczny egzamin jest zablokowany. Szczegóły: `review/batches/stage4m-length-bias-batch4-b06.md`.
