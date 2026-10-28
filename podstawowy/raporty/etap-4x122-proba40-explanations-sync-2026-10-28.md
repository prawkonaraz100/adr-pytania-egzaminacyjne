# Etap 4x122 — próbka 40 explanation, dystraktory i spójność

- Data: 2026-10-28.
- Świeży `main` na wejściu: `54bfc33446ad735be9ef86e721eac746c6c8da6d` (po scaleniu PR #582 i PASS CI).
- Bank: 609 pytań; blob na wejściu `f18b273e3451730a4efc28e10cd0ff16b03807f5`; blob po poprawkach `00d8dcc732fccefb5f5bbf021eec204533a75708`.
- Zakres: wyłącznie kurs podstawowy ADR.

## 1. Próbka

Próbkę wylosowano deterministycznie, seed `41222026`, z puli pozostałej po wyłączeniu ID jawnie zapisanych jako próby/zmiany etapów 4x114–4x121. Przeczytano wszystkie 40 pytań, odpowiedzi A/B/C, poprawną literę, explanation i podstawę ADR.

```
ADR-B-0026, ADR-B-0250, ADR-B-0087, ADR-B-0022, ADR-B-0296, ADR-B-0291, ADR-B-0126, ADR-B-0212, ADR-B-0236, ADR-B-0343, ADR-B-0010, ADR-B-0113, ADR-B-0100, ADR-B-0166, ADR-B-0045, ADR-B-0209, ADR-B-0146, ADR-B-0259, ADR-B-0038, ADR-B-0105, ADR-B-0049, ADR-B-0233, ADR-B-0109, ADR-B-0392, ADR-B-0012, ADR-B-0207, ADR-B-0327, ADR-B-0560, ADR-B-0362, ADR-B-0398, ADR-B-0144, ADR-B-0604, ADR-B-0066, ADR-B-0188, ADR-B-0542, ADR-B-0302, ADR-B-0115, ADR-B-0430, ADR-B-0249, ADR-B-0006
```

## 2. Potwierdzone poprawki

| ID | Problem | Poprawka | Podstawa wskazana w banku |
|---|---|---|---|
| ADR-B-0026 | Dystraktor o układaniu opakowań na boku nie był uniwersalnie błędny, a opcja „luźno na podłodze” była zbyt łatwa do odrzucenia. | Opcję C zmieniono na typową pomyłkę: mocowanie tylko przesyłek klasy 1. Explanation wyjaśnia, że trzeba zabezpieczyć cały ładunek, nie tylko jedną klasę. | ADR 7.5.7.1 |
| ADR-B-0250 | Pytanie było niemal równoważne ADR-B-0087. | Przeniesiono je na praktyczną sytuację kontroli: dokument ze zdjęciem pozostał w biurze. Opcje A/C i explanation teraz rozróżniają dokument okazany później lub listę załogi od dokumentu, który członek załogi ma przy sobie. Długości opcji zrównoważono (96/98/100 znaków). | ADR 1.10.1.4; 8.1.2.1 |
| ADR-B-0362 | Dwa dystraktory („prywatne wiadomości”, „paragon z parkingu”) były absurdalne i nie sprawdzały wiedzy o dostępie do dokumentów. | Zastąpiono je błędami związanymi z odkładaniem dokumentów do końca działań lub podaniem wyłącznie numeru UN ustnie. Explanation odnosi się teraz do obu realnych pomyłek. | ADR 5.4.3.4 (pozostaje do niezależnego potwierdzenia przez specjalistę) |
| ADR-B-0542 | Stem opisywał biały płomień na czerwonej nalepce klasy 3, co nie odpowiada standardowemu wzorowi ADR. | Poprawiono opis na czerwony romb z czarnym płomieniem i cyfrą 3; explanation przypomina, że klasę rozpoznaje się po całym wzorze, kolorze i numerze. | ADR 5.2.2.2.2; 2.2.3.1.1 |

Wszystkie poprawne litery pozostały bez zmian. Zmieniono cztery explanation, trzy zestawy dystraktorów i jeden opis pytania. Żadne pytanie nie otrzymało statusu `verified`.

## 3. Wynik oceny 40 wyjaśnień

- Przejrzano: **40/40**.
- Explanation przepisane: **4** — ADR-B-0026, 0250, 0362, 0542.
- Dystraktory poprawione: **3 pytania** — ADR-B-0026, 0250, 0362.
- Stem doprecyzowany: **1** — ADR-B-0542.
- Pozostałe 36 pytań pozostawiono bez zmian: wyjaśnienia są zrozumiałe, mają 3–5 zdań i odnoszą się do sensu poprawnej odpowiedzi oraz głównych błędów.
- W całej próbce explanation ma **301–430 znaków** i 3–5 zdań. Brak jednowyrazowych lub suchych cytatów przepisu w tej próbce.

## 4. Preflight Quality Gate

| Kontrola | Wynik |
|---|---:|
| Pytania | 609 |
| Unikalne ID / duplikaty | 609 / 0 |
| Statusy | 609 `needs_review`, 0 `verified` |
| Explanation poniżej 200 znaków | 0 |
| Najkrótsze / najdłuższe explanation | 300 / 498 znaków |
| Poprawna = jedyna najdłuższa | 72/609 = **11,82%** |
| Maksimum w dziale | B-07: 7/48 = **14,58%** |
| Próg | ≤18% — spełniony |

Wskaźnik per dział: B-01 6/45 (13,33%); B-02 8/56 (14,29%); B-03 5/49 (10,20%); B-04 6/46 (13,04%); B-05 5/43 (11,63%); B-06 6/45 (13,33%); B-07 7/48 (14,58%); B-08 3/42 (7,14%); B-09 5/46 (10,87%); B-10 4/55 (7,27%); B-11 6/43 (13,95%); B-12 5/44 (11,36%); B-13 6/47 (12,77%).

## 5. Synchronizacja i ograniczenia

- Odświeżono migawki `review/legal-clauses` i `review/sequential` dla ADR-B-0026, 0250, 0362 i 0542.
- W wariancie 004 zaktualizowano opcję C pytania ADR-B-0026; w kluczu 004 dopasowano explanation. Zaktualizowano `source_bank_head` we wszystkich wariantach i kluczach 001–005 do `00d8dcc732fccefb5f5bbf021eec204533a75708`.
- Raport i manifest próbki: [etap-4x122-proba40-explanations-sync-2026-10-28.md](etap-4x122-proba40-explanations-sync-2026-10-28.md), [manifest](etap-4x122-wykluczenia-proby.json).
- Lokalnego checkoutu repo nie udostępnia bieżące środowisko; nie deklaruję testów lokalnych. PR musi przejść pełny GitHub Actions Quality Gate. Podstawa ADR-B-0362 i pozostałe zmienione rekordy nadal wymagają niezależnej kontroli specjalisty.
