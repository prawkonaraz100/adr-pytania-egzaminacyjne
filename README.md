# ADR — pytania egzaminacyjne i szkoleniowe

Otwarty projekt autorskiej bazy pytań do nauki na **polski egzamin ADR dla kierowców**.

## Zakres

1. **ADR podstawowy (początkowy) — aktywny etap.**
2. **ADR specjalistyczny: cysterny — etap kolejny**, po zakończeniu i zatwierdzeniu podstawowego.
3. Inne specjalizacje poza bieżącym zakresem.

## Stan na 25.10.2026 — po etapie 4t

- [x] Bank ADR podstawowy: **579 pytań**; **579 `needs_review` / 0 `verified`**.
- [x] 104/104 wewnętrznych celów teorii ma pytania robocze; 3/3 cele praktyczne mają scenariusze, ale wykonanie wymaga rzeczywistych zajęć i potwierdzenia instruktora.
- [x] 13/13 lekcji ma mapę ID pytań i przykłady praktyczne; Quality Gate sprawdza, że wskazane ID istnieją w banku.
- [x] Dodano egzamin próbny 30-pytaniowy (60 min, próg treningowy 20/30), osobny klucz i generator wariantów proporcjonalnych do 13 działów.
- [x] Quality Gate sprawdza unikalne ID egzaminu, zgodność klucza i powtarzalność wariantu 001.
- [x] Wskaźnik „poprawna odpowiedź jest jedyną najdłuższą” wynosi **80/579 = 13,82%**; każdy z 13 działów jest poniżej 18%.
- [ ] Pełne porównanie polskiego tekstu ADR 2025 i sprostowania oraz niezależna recenzja wszystkich odpowiedzi A/B/C.
- [ ] Odbiór merytoryczny lekcji przez instruktora i rzeczywiste wykonanie ćwiczeń praktycznych.

**Ważne:** egzamin próbny i bank pytań są materiałami autorskimi do treningu wewnętrznego, nie oficjalnymi pytaniami państwowymi. Żaden rekord nie ma statusu `verified`; bramka wydania nadal dopuszcza wyłącznie rekordy z udokumentowaną akceptacją. Kurs cystern pozostaje poza bieżącym zakresem.

## Jak pracujemy

- Opracowujemy własne pytania: dokładnie 3 odpowiedzi, jedna poprawna, prosty komentarz dla kierowcy.
- Każde pytanie wskazuje precyzyjne źródło: wydanie przepisów i konkretny punkt/artykuł.
- Wynik kontroli ma jednoznaczny status: draft, needs_review, verified albo blocked.
- W teście produkcyjnym używamy wyłącznie pytań verified i tylko z aktualną weryfikacją.
- Źródła zewnętrzne i testy szkoleniowe służą identyfikacji tematów i luk, nie do bezpośredniego kopiowania cudzych pytań, grafik ani objaśnień.
- Zmiany przepisów uruchamiają ponowną weryfikację powiązanych pytań.

## Dokumentacja

- [Egzamin próbny ADR podstawowy — wariant 001, klucz i generator](podstawowy/egzamin-probny/README.md)
- [Raport etapu 4p — egzamin, jakość lekcji i wskaźnik długości odpowiedzi](docs/ETAP-4P-EGZAMIN-PRÓBNY-I-AUDYT-LEKCJI.md)

- [Plan i kryteria ukończenia](docs/PLAN.md)
- [Mapa punktów ADR 2025 do weryfikacji — 13 działów](docs/MAPA-PUNKTOW-ADR-2025.md)
- [Urzędowy program kursu](docs/PROGRAM-PODSTAWOWY.md)
- [Źródła prawne i zasady ich weryfikacji](docs/ZRODLA.md)
- [Standard pytań i publikacji](docs/STANDARD-PYTAN.md)
- [Stan prac i rejestr decyzji](docs/STATUS.md)
- [Audyt 39 pytań i uzupełnienie 15 wcześniejszych pozycji](docs/AUDYT-MERYTORYCZNY-PARTIA-001.md)
- [Audyt partii 003: 20 pytań sytuacyjnych i kontrola odpowiedzi](docs/AUDYT-PARTIA-003.md)
- [Pokrycie 106 kompetencji, luki i materiały praktyczne](docs/POKRYCIE-KURSU.md)
- [Audyt partii 005: 24 pytania zamykające luki tematyczne](docs/AUDYT-PARTIA-005.md)
- [Audyt partii 006: 30 pytań sytuacyjnych pogłębiających 30 celów](docs/AUDYT-PARTIA-006.md)
- [Audyt partii 007A: 20 pytań sytuacyjnych](docs/AUDYT-PARTIA-007A.md)
- [Audyt partii 007B: 20 pytań, analiza podobieństw i warunki prawne](docs/AUDYT-PARTIA-007B.md)
- [Scenariusze ćwiczeń praktycznych](podstawowy/praktyka/SCENARIUSZE.md)
- [Matryca kompetencji JSON](podstawowy/kompetencje.json)

## Szczegółowa analiza redakcyjna A/B/C — cała baza 0001–0216

- Raporty: [001–060](review/legal-clauses/RAPORT-001-060.md), [061–090](review/legal-clauses/RAPORT-061-090.md), [091–120](review/legal-clauses/RAPORT-091-120.md), [121–216](review/legal-clauses/RAPORT-121-216.md). **216 pytań / 648 indywidualnych uzasadnień A/B/C** w ośmiu plikach JSON.
- `python scripts/check_legal_clause_review.py` wymaga kompletności analizy całych 216 pytań, ale **nie poświadcza poprawności prawa, dokładnego polskiego tekstu ani kwalifikacji specjalisty**. 0 pytań ekspercko zatwierdzonych.
- Poprawiono pytania `0009`, `0019`, `0027`, `0031`, `0033`, `0043`.
- `python scripts/check_legal_clause_review.py` wykrywa brak oceny wariantu lub nieaktualny zapis po edycji pytania.
- To porównanie redakcyjno-źródłowe, **nie dosłowny odbiór pełnego tekstu polskiego i nie zatwierdzenie eksperta**. Nadal 216 `needs_review` / 0 `verified`.

## Pełny pierwszy przebieg redakcyjny pytań 001–216 (23.10.2026)

- [Raport 216 pytań w kolejności ID](review/sequential/RAPORT.md) i **8 rejestrów** w `review/sequential/`; każda pozycja ma kopię A/B/C, klucza, wyjaśnienia, referencji oraz stopnia faktycznej kontroli źródeł.
- Wszystkie 216 wpisów przeczytano i przeanalizowano redakcyjnie; 34 wymagają dodatkowej uwagi, w 25 odnotowano porównanie konkretnego tematu/punktu z dodatkowym źródłem. **To NIE jest 216 zakończonych indywidualnych przeglądów prawa.**
- W tej partii poprawiono `0048`, `0099`, `0162`, `0173` (gramatyka, baterie sodowo-jonowe 9A, wyjątki 7.3.1.1).
- `python scripts/check_sequential_audit.py` — pełne, aktualne pokrycie redakcyjne; kolejna edycja pytania wymaga aktualizacji jego śladu w audycie.
- **216 `needs_review`, 0 `verified`**; eksport prawidłowo pozostaje `BLOCKED` do czasu rzeczywistego odbioru przez specjalistę ADR.

## Audyt merytoryczny — pierwsza partia 30 pytań (23.10.2026)

- [Raport redakcyjny 30 pytań wybranych wg ryzyka](review/batches/risk-001.md) oraz [rejestr maszynowy](review/batches/risk-001.json).
- Sprawdzono treść wszystkich trzech wariantów i wskazane przepisy w ograniczonym zakresie; **8 pytań poprawiono**, 3 skierowano do szczególnej kontroli, 19 nie wykazało sprzeczności w przeglądzie wstępnym.
- Wykryto **istotne pytanie z dwoma możliwymi poprawnymi odpowiedziami** (ADR-B-0073: gaśnica 2 kg / 6 kg) i usunięto niejednoznaczność. Dodano testy regresyjne.
- **Nie ma podpisanej recenzji specjalisty ADR**: wszystkie 216 rekordów pozostają `needs_review`; `review/approvals.jsonl` jest pusty, eksport `BLOCKED`. Wynik wstępny nie jest prawnym zatwierdzeniem.

## Kontrola wydania (nowa bramka)

- [Rejestr aktualnych odstępstw ADR 2026](docs/ODSTEPSTWA-ADR-2026.md) — w tym M364 dotycząca świadectw naczep, M369 i M370.
- [Audyt wydawniczy i zmiany siedmiu pytań](docs/AUDYT-WYDAWNICZY-2026.md).
- [Zasady rzeczywistej recenzji i zatwierdzeń](review/README.md); plik `review/approvals.jsonl` jest **pusty** — 0 podpisanych zatwierdzeń.
- `python scripts/release_gate.py --report` — informuje, że eksport jest obecnie **BLOCKED**; test techniczny nie oznacza odbioru prawnego.
- Eksport `--output dist/adr-podstawowy-verified.jsonl` dopuszcza tylko rekordy `verified` zgodne z udokumentowaną akceptacją i dokładnym skrótem treści. Wymaga minimum 30 pytań z wszystkich 13 działów. Obecnie niczego nie wygeneruje.

## Dane i narzędzia

- Dane: `podstawowy/questions.jsonl` (jeden obiekt JSON na linię).
- Schemat: `schema/question.schema.json`.
- Walidator: `python scripts/validate.py`.
- Testy walidatora: `python -m unittest discover -s tests -v`.
- Automatyczna kontrola w GitHub Actions: `.github/workflows/quality.yml`.
- Mapa pokrycia: `python scripts/coverage.py` (brak pytania ≠ niepoprawny rekord, ale stanowi lukę programu).
- Lekcje w `podstawowy/lekcje/`: 13 szkiców (01–13), bez odbioru merytorycznego.

## Źródła podstawowe

- [Ministerstwo Infrastruktury — towary niebezpieczne i ADR 2025](https://www.gov.pl/web/infrastruktura/towary-niebezpieczne)
- [Rozporządzenie o prowadzeniu kursów, załącznik nr 1 (Dz.U. 2021 poz. 2150)](https://eli.gov.pl/api/acts/DU/2021/2150/text.pdf)
- [Rozporządzenie o egzaminach (Dz.U. 2024 poz. 964)](https://eli.gov.pl/api/acts/DU/2024/964/text.html)

**Charakter projektu:** nieoficjalna platforma edukacyjna, niezwiązana z komisją egzaminacyjną ani organem administracji.


## Aktualizacja etapu 4t — 25.10.2026

- Audyt porównał 13 tematów polskiego programu z ADR 2025 8.2.2.3.2(a)–(n). Zidentyfikowano brak wyodrębnionego celu odpowiedzialności cywilnej i dodano ADR-B-07-K07 oraz pytania 0567–0569.
- Szczegóły: [raport pokrycia](podstawowy/raporty/etap-4t-pokrycie-programu-2026-10-25.md).
- Bank: 569 `needs_review`, 0 `verified`. Dalsze kroki wymagają PASS Quality Gate i niezależnej recenzji prawnej.
