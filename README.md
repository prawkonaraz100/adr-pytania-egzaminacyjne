# ADR — pytania egzaminacyjne i szkoleniowe

Otwarty projekt autorskiej bazy pytań do nauki na **polski egzamin ADR dla kierowców**.

## Zakres

1. **ADR podstawowy (początkowy) — aktywny etap.**
2. **ADR specjalistyczny: cysterny — etap kolejny**, po zakończeniu i zatwierdzeniu podstawowego.
3. Inne specjalizacje poza bieżącym zakresem.

## Stan na 22.10.2026

- [x] Utworzono repozytorium i zapisano założenia.
- [x] Zidentyfikowano oficjalny program kursu: 13 tematów / 18 godzin lekcyjnych teorii plus ćwiczenia praktyczne.
- [x] Zidentyfikowano zasady państwowego egzaminu podstawowego: 30 pytań, 60 minut, próg 20 poprawnych odpowiedzi.
- [x] Wstępna mapa punktów ADR 2025 dla 13 tematów (do kontroli pełnego tekstu).
- [ ] Kompletny przegląd punktów ADR 2025 oraz aktów krajowych dla 13 tematów.
- [x] Osiem partii autorskich pytań: 39 + 31 + 20 + 32 + 24 + 30 + 20 + 20 = 216 w statusie needs_review. Wszystkie 103 cele teorii mają co najmniej dwa szkice pytań; osobno 3 cele praktyczne.
- [ ] Autorska baza pytań po weryfikacji merytorycznej.
- [ ] Egzaminy próbne, ilustracje i pełny Quality Gate.
- [ ] Kurs specjalistyczny „cysterny”.

**Uwaga:** obecnie w banku jest **216 pytań w statusie needs_review i 0 zatwierdzonych**. 103/103 zagadnień teoretycznych ma co najmniej dwa szkice pytań; wszystkie 13 lekcji to szkice do recenzji. Wynik kontroli źródła przez autora nie zastępuje podpisu niezależnego recenzenta ADR. Nie przedstawiamy pytań autorskich ani z komercyjnych testów jako oficjalnych pytań egzaminacyjnych. Publicznego kompletnego katalogu pytań państwowych nie potwierdzono.

## Jak pracujemy

- Opracowujemy własne pytania: dokładnie 3 odpowiedzi, jedna poprawna, prosty komentarz dla kierowcy.
- Każde pytanie wskazuje precyzyjne źródło: wydanie przepisów i konkretny punkt/artykuł.
- Wynik kontroli ma jednoznaczny status: draft, needs_review, verified albo blocked.
- W teście produkcyjnym używamy wyłącznie pytań verified i tylko z aktualną weryfikacją.
- Źródła zewnętrzne i testy szkoleniowe służą identyfikacji tematów i luk, nie do bezpośredniego kopiowania cudzych pytań, grafik ani objaśnień.
- Zmiany przepisów uruchamiają ponowną weryfikację powiązanych pytań.

## Dokumentacja

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

## Szczegółowa kontrola odpowiedzi A/B/C — pytania 0001–0060

- [Raport dla 60 pytań](review/legal-clauses/RAPORT-001-060.md), z osobnymi uzasadnieniami **180 wariantów** odpowiedzi w plikach [001–030](review/legal-clauses/001-030.json) i [031–060](review/legal-clauses/031-060.json).
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
