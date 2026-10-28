## Najnowsza synchronizacja — etap 4x122 (28.10.2026)

- Aktualny blob banku: `00d8dcc732fccefb5f5bbf021eec204533a75708`.
- Bank: 609 pytań; wszystkie `needs_review`, 0 `verified`; minimum explanation 300 znaków.
- W próbce 40 dopracowano ADR-B-0026, ADR-B-0250, ADR-B-0362 i ADR-B-0542. Zaktualizowano migawki audytu; w wariancie 004 zmieniono opcję ADR-B-0026, a klucz zachowuje tę samą poprawną literę.
- Wszystkie warianty i klucze 001–005 wskazują nowy blob banku. Raport: [Etap 4x122](../raporty/etap-4x122-proba40-explanations-sync-2026-10-28.md); manifest: [próba i wykluczenia](../raporty/etap-4x122-wykluczenia-proby.json).

## Najnowsza synchronizacja — etap 4x121 (28.10.2026)

- Aktualny blob banku: `f18b273e3451730a4efc28e10cd0ff16b03807f5`.
- Bank: 609 pytań; wszystkie `needs_review`, 0 `verified`; minimum explanation 300 znaków.
- W próbce 40 poprawiono dystraktor i explanation ADR-B-0041 oraz doprecyzowano treść ADR-B-0426. Żaden z tych ID nie występuje w wariantach 001–005, więc nie zmieniono ich składu ani kluczy; zaktualizowano wyłącznie `source_bank_head` w pięciu wariantach i kluczach.
- Raport: [Etap 4x121](../raporty/etap-4x121-proba40-explanations-sync-2026-10-28.md); manifest: [próba i wykluczenia](../raporty/etap-4x121-wykluczenia-proby.json).

## Najnowsza synchronizacja — etap 4x120 (28.10.2026)

- Aktualny blob banku: `04ace7f478868d0901bbc45fb26af3d866e18538`.
- Bank: 609 pytań; wszystkie `needs_review`, 0 `verified`; minimum explanation 300 znaków.
- Próbka 4x120: 40 ID, seed `411202026`; 4 pytania w próbie otrzymały poprawione dystraktory i dopasowane explanation, bez zmiany ID, poprawnych liter i podstaw prawnych; 5 dodatkowych celowanych follow-upów opisano osobno.
- Warianty i klucze 001–005 zachowują zestawy pytań i są zsynchronizowane z aktualnym blobem banku; żaden klucz nie wymagał remapowania.
- Raport: [Etap 4x120](../raporty/etap-4x120-proba40-dystraktory-sync-2026-10-28.md); manifest: [próba i wykluczenia](../raporty/etap-4x120-wykluczenia-proby.json).

## Najnowsza synchronizacja — etap 4x119 (28.10.2026)

- Aktualny blob banku: `35549752d913c85daf1fc3c9492d9c04fce777a1`.
- Bank: 609 pytań; wszystkie `needs_review`, 0 `verified`; minimum explanation 300 znaków.
- Siedem unikalnych zmian z zamkniętego PR #579 przeniesiono na nową gałąź, bez zmiany poprawnych liter; zaktualizowano migawki audytu.
- Warianty i klucze 001–005 zachowują ID i poprawne litery; odświeżono ich `source_bank_head`.
- Raport próby 40: [etap 4x119](../raporty/etap-4x119-proba40-spojnosc-2026-10-28.md).

## Najnowsza synchronizacja — etap 4x118 (28.10.2026)

- Aktualny blob banku: `28d809ccbf973fc8101f456eb9ab0144165110f1`.
- Bank: 609 pytań; wszystkie `needs_review`, 0 `verified`; minimum explanation 300 znaków.
- Etap 4x118: poprawiono dystraktory i explanation w ADR-B-0028, 0054, 0354, 0492 i 0535; poprawne litery i podstawy ADR bez zmian.
- Zmienione ID nie występują w wariantach 001–005. Zsynchronizowano `source_bank_head` wszystkich wariantów i kluczy.
- To wewnętrzne materiały treningowe, nie oficjalny egzamin ani zatwierdzony pakiet.

## Najnowsza synchronizacja — etap 4x113 (28.10.2026)

- Aktualny blob banku: `2675c0636a421bf3b4347ad0117087d6ec633321`.
- Bank: 609 pytań; wszystkie `needs_review`, 0 `verified`; minimum explanation 300 znaków.
- Etap 4x113: próbka 40, seed `41132026`; poprawiono dystraktory i explanation w ADR-B-0035, ADR-B-0143, ADR-B-0516, ADR-B-0292, ADR-B-0199 i ADR-B-0345. Zachowano ID, poprawne litery i podstawy ADR.
- ADR-B-0035 występuje w wariancie 005; jego opcje zostały przestawione zgodnie z mapowaniem wariantu, a explanation klucza 005 zsynchronizowano z bankiem.
- Wszystkie warianty i klucze 001–005 wskazują aktualny blob banku; każdy wariant ma 30 unikalnych pytań. Raport: [Etap 4x113](../raporty/etap-4x113-proba40-dystraktory-sync-2026-10-28.md); manifest: [seed, próbka i wykluczenia](../raporty/etap-4x113-wykluczenia-proby.json).
- Etap 4x112: przejrzano próbkę 40 (seed `41122026`); poprawiono wiarygodność dystraktorów i explanation dla ADR-B-0498, ADR-B-0525, ADR-B-0224, ADR-B-0110, ADR-B-0174 i ADR-B-0207. Zachowano ID, poprawne litery i podstawy prawne.
- Dla ADR-B-0489 sprawdzono mapowanie litery w explanation klucza 001 (bankowa A → wariantowa C); wszystkie klucze 001–005 zgadzają się z tekstem poprawnej opcji i explanation banku po mapowaniu.
- Warianty i klucze 001–005 wskazują bieżący blob banku; każdy wariant ma 30 unikalnych pytań.
- Raport 4x112: [próbka 40 i synchronizacja](../raporty/etap-4x112-proba40-dystraktory-sync-2026-10-28.md); manifest: [seed, lista próby i wykluczenia](../raporty/etap-4x112-wykluczenia-proby.json).


- Bank: 609 pytań, wszystkie `needs_review`, 0 `verified`.
- Próbka 40: urealniono dystraktory ADR-B-0233, ADR-B-0280, ADR-B-0323, ADR-B-0342, ADR-B-0389 i ADR-B-0437; uproszczono explanation ADR-B-0319. Żadna poprawna litera ani podstawa ADR nie uległa zmianie.
- Warianty i klucze 001–005 wskazują bieżący blob banku. Każdy arkusz ma 30 pytań, 13 działów, brak duplikatów, A/B/C 10/10/10 i maksymalną serię 3.
- Etap 4x110: urealniono dystraktory i dopasowano explanation dla ADR-B-0016, ADR-B-0109 i ADR-B-0164. Zsynchronizowano kopie w wariantach 001 i 004 oraz klucz ADR-B-0489 w wariancie 001.
- Raport 4x110: [próbka 40, dystraktory i synchronizacja egzaminów](../raporty/etap-4x110-proba40-dystraktory-sync-2026-10-28.md); manifest: [lista próbki i wykluczeń](../raporty/etap-4x110-wykluczenia-proby.json).
- Etap 4x111: urealniono dystraktory ADR-B-0082, ADR-B-0123, ADR-B-0296, ADR-B-0351 i ADR-B-0423, bez zmiany poprawnych liter; źródłowy blob banku: `a0d901b67548cd9ae66eeb8fa09b7c8264640e3c`. Raport: [Etap 4x111 — próbka 40 i poprawki dystraktorów](../raporty/etap-4x111-proba40-dystraktory-sync-2026-10-28.md); manifest: [lista próbki i wykluczeń](../raporty/etap-4x111-wykluczenia-proby.json).
- Zmienione pytania nie występują w wariantach, dlatego nie trzeba było zmieniać treści arkuszy; CI nadal sprawdza ich zgodność z bankiem.
- Raport: [Etap 4x108 — próbka 40 i regresja kursu](../raporty/etap-4x108-proba40-dystraktory-regresja-2026-10-28.md).

## Jak interpretować wynik

- **20–30 poprawnych odpowiedzi:** osiągasz próg treningowy tego arkusza, ale nie jest to oficjalne potwierdzenie kwalifikacji ani dowód, że wszystkie zagadnienia opanowano.
- **0–19 poprawnych odpowiedzi:** wróć do nauki przed kolejną próbą. Zapisz ID pytań, na które odpowiedziałeś błędnie, i sprawdź ich `module_id` w banku.
- **Po każdym błędzie:** przeczytaj explanation do końca: najpierw sens poprawnej odpowiedzi, potem przyczynę błędu pozostałych opcji, a na końcu wskazany punkt ADR. Nie ucz się samej litery, bo warianty mogą mieć inne kolejności A/B/C.
- **Powtórka:** otwórz lekcję właściwego działu, przećwicz trzy scenariusze tego działu i dopiero wtedy rozwiąż inny wariant.
- **Status materiału:** wszystkie pytania pozostają `needs_review`; wynik jest wyłącznie informacją do samodzielnej nauki.

**Karta powtórki:** [wypełnij kartę analizy wyniku](KARTA-ANALIZY-WYNIKU.md) — zapisz ID błędnych pytań, wyjaśnij mylące warianty i wróć do scenariuszy właściwego działu. To pomoc do samodzielnej nauki, nie zapis oficjalnego wyniku.

## Arkusze — rozwiąż przed otwarciem klucza

- [Wariant 001 — arkusz pytań](wariant-001.json)
- [Wariant 002 — arkusz pytań](wariant-002.json)
- [Wariant 003 — arkusz pytań](wariant-003.json)
- [Wariant 004 — arkusz pytań](wariant-004.json)
- [Wariant 005 — arkusz pytań](wariant-005.json)

## Klucze i wyjaśnienia — dopiero po rozwiązaniu

- [Wariant 001 — klucz i wyjaśnienia](klucz-001.json)
- [Wariant 002 — klucz i wyjaśnienia](klucz-002.json)
- [Wariant 003 — klucz i wyjaśnienia](klucz-003.json)
- [Wariant 004 — klucz i wyjaśnienia](klucz-004.json)
- [Wariant 005 — klucz i wyjaśnienia](klucz-005.json)

**Uwaga o dostępie:** klucze są rozdzielone od arkuszy w nawigacji, ale repozytorium jest publiczne, więc nie ma technicznego ograniczenia dostępu. Przed zakończeniem próby nie otwieraj plików kluczy.

## Po błędzie — wróć do właściwej lekcji

Każdy wpis w plikach `klucz-001.json`–`klucz-005.json` zawiera `lesson_path`, wskazujący lekcję odpowiadającą działowi pytania. Po przeczytaniu explanation otwórz tę lekcję, przejrzyj jej scenariusze w `../praktyka/scenariusze-13-dzialow.json`, a następnie powtórz pytania działu. Quality Gate sprawdza, czy każdy odnośnik prowadzi do istniejącej lekcji właściwego modułu.

## Status prawny

Bank zawiera 609 pytań `needs_review` i 0 `verified`. Arkusze mają `publication_authorized: false` i nie są oficjalnymi arkuszami ani materiałem do formalnej oceny. Klucze i explanation są synchronizowane z bankiem przez Quality Gate.

## Etap 4x20 — regeneracja wariantów 001–005 (2026-10-26)

- Migawka banku: `46e7d1a0c28d21dce01b054be8513ef7db1f6210` (609 pytań; ADR-B-0001–ADR-B-0609).
- Warianty 001–005 i odpowiadające im klucze zostały wygenerowane ponownie z aktualnego banku. Każdy wariant ma 30 pytań, obejmuje wszystkie 13 działów (po 2–3 pytania na dział), a ID nie powtarzają się ani w wariancie, ani między wariantami.
- Wskaźnik „poprawna odpowiedź jest jedyną najdłuższą”: 001=0/30 (0%), 002=0/30 (0%), 003=0/30 (0%), 004=0/30 (0%), 005=0/30 (0%); próg kontrolny wynosi 18%.
- Rozkład poprawnych liter A/B/C: każdy wariant 10/10/10. Najdłuższa seria tej samej litery: każdy wariant ≤3.
- Warianty i klucze wskazują ten sam blob banku. Wyjaśnienia w kluczach są mapowane do kolejności odpowiedzi na arkuszu.
- Quality Gate: `scripts/check_mock_exam_variants.py` blokuje również przekroczenie 18% w dowolnym wariancie; test regresyjny w `tests/test_mock_exam_variants.py`.
- Raport: [Etap 4x20 — regeneracja egzaminów 001–005](../raporty/etap-4x20-egzaminy-001-005-2026-10-26.md).

**Status prawny:** 609 pytań `needs_review`, 0 `verified`; arkusze są wyłącznie materiałem treningowym, `publication_authorized: false`.


## Etap 4x25 — końcowa kontrola synchronizacji (2026-10-26)

- Bank: 609 pytań, wszystkie `needs_review`, 0 `verified`.
- Warianty 001–005: każdy ma 30 pytań i 30 odpowiedzi w kluczu; brak duplikatów w arkuszach i między wariantami.
- Każdy arkusz i klucz wskazuje aktualny blob `questions.jsonl`; treść, moduł, zestaw odpowiedzi, poprawna litera i explanation zostały porównane z bankiem z uwzględnieniem przestawiania liter A/B/C.
- Rozkład poprawnych odpowiedzi dla każdego wariantu: A/B/C = 10/10/10; najdłuższa seria tej samej litery = 3; 13 działów reprezentowanych w każdym arkuszu.
- Korekta explanation ADR-B-0197 nie wymagała zmiany pytań w arkuszach, ponieważ ten ID nie występuje w wariantach 001–005. Zaktualizowano wyłącznie metadane źródła w arkuszach i kluczach.
- Raport pełny: [Etap 4x25 — raport końcowy](../raporty/etap-4x25-raport-koncowy-2026-10-26.md).


## Etap 4x26 — ponowna synchronizacja po redakcji podręcznika (2026-10-26)

- Lekcje i materiały instruktora zostały zredagowane; bank nie zmienił się od wygenerowania wariantów.
- Warianty 001–005 i klucze ponownie zsynchronizowano z aktualnym `questions.jsonl`, zachowując wybór ID i proporcje działów oraz odświeżając kolejność błędnych odpowiedzi. `source_bank_head` pozostaje blob SHA banku: `ed0dee6e93f21cbb758c3d088a4d02e0aaed9fc4`.
- Każdy wariant ma 30 pytań, 13 działów, brak powtórzeń w arkuszu i między wariantami, rozkład A/B/C 10/10/10 oraz najdłuższą serię tej samej poprawnej litery nie większą niż 3.
- Klucze są zsynchronizowane z poprawnymi opcjami i explanation banku; explanation mają co najmniej 200 znaków.
- Pełny raport: [Etap 4x26 — raport końcowy](../raporty/etap-4x26-raport-koncowy-2026-10-26.md).


## Aktualizacja synchronizacji — etap 4x31

- Migawka banku i kluczy: `99c06e736c0e5812e97d4ff02567dbf741629434`.
- Po redakcji wyjaśnienia ADR-B-0540 zsynchronizowano `source_bank_head` we wszystkich wariantach i kluczach 001–005.
- Wszystkie warianty pozostają materiałami treningowymi; pytania nadal mają status `needs_review`.


## Etap 4x34 — kontrola powtórzeń i podpowiedzi (2026-10-26)

- Migawka aktualnego banku: `7c7573215da82caeabe9543eb47dfc9703ecf622`.
- Zmieniono pytania ADR-B-0048, ADR-B-0078, ADR-B-0127 i ADR-B-0238; warianty i klucze 001–005 wskazują aktualny blob banku.
- Wariant 002 i jego klucz zaktualizowano dla ADR-B-0078; pozostałe warianty zachowały zestaw pytań.
- Status prawny pozostaje bez zmian: 609 pytań `needs_review`, 0 `verified`, brak formalnej zgody na publikację.

## Kontrola po etapie 4x46 (26.10.2026)

- Pięć wariantów 001–005 oraz pięć kluczy zsynchronizowano z bankiem o blob SHA `7d69e28fb83341ff225d402da30ef38bac7dd047`.
- Zgodność zestawów pytań, poprawnych liter i wyjaśnień z bankiem: 5/5, brak rozbieżności; wszystkie arkusze nadal są treningowe i niezatwierdzone.
- Zmodyfikowano wyłącznie osiem wyjaśnień w banku (bez zmiany poprawnych liter, opcji A/B/C lub przypisań działów).
- Szczegóły: [raport 4x46](../raporty/etap-4x46-proba60-i-synchronizacja-2026-10-26.md).

## Synchronizacja po 4x47

- Aktualny bank blob SHA: `6de0159ce4d80799104a01170c42e363623045eb`. Wszystkie warianty 001–005 i ich klucze zachowują te same pytania i poprawne litery; zaktualizowano migawkę banku. ADR-B-0403 nie należy do pięciu obecnych wariantów.
