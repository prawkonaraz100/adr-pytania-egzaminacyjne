# Etap 4x122 — próbka 40, czytelność explanation i jakość dystraktorów

- Data: 2026-10-28.
- Punkt wejścia: świeży `main`, commit `54bfc33446ad735be9ef86e721eac746c6c8da6d` (PR #582, etap 4x121, już scalony).
- Zakres: wyłącznie kurs podstawowy ADR.
- Bank przed zmianami: 609 pytań, blob `f18b273e3451730a4efc28e10cd0ff16b03807f5`.
- Bank po zmianach: 609 pytań, blob `6612e0241dc9e9b3a01f6b456f58d141dc53ada9`.
- Wszystkie pytania pozostają `needs_review`; żadne nie zostało oznaczone jako `verified`.

## Porządek PR i dziennik
PR #579 jest już zamknięty bez scalania jako duplikat/konflikt po PR #578. Issue #10 zawiera wpis podsumowujący 4x117/4x118, w tym decyzję o zamknięciu #579. Wpisów 4x119 (#580), 4x120 (#581) i 4x121 (#582) również już dokonano; ten raport kontynuuje od następnego niewykonanego etapu — 4x122.

## Próbka
- Seed: `41222026`.
- Przejrzano 40/40 pytań: treść, opcje A/B/C, poprawną literę, explanation i wskazaną podstawę.
- Próbka jest rozłączna z zapisanymi ID z dostępnych manifestów 4x107–4x121. Pula po wykluczeniach: 106 pytań.
- ID próbki:
```
ADR-B-0432, ADR-B-0096, ADR-B-0155, ADR-B-0204, ADR-B-0332,
ADR-B-0067, ADR-B-0306, ADR-B-0112, ADR-B-0133, ADR-B-0384,
ADR-B-0471, ADR-B-0270, ADR-B-0002, ADR-B-0284, ADR-B-0015,
ADR-B-0369, ADR-B-0139, ADR-B-0175, ADR-B-0178, ADR-B-0188,
ADR-B-0309, ADR-B-0605, ADR-B-0011, ADR-B-0236, ADR-B-0302,
ADR-B-0247, ADR-B-0210, ADR-B-0246, ADR-B-0495, ADR-B-0353,
ADR-B-0376, ADR-B-0392, ADR-B-0298, ADR-B-0365, ADR-B-0325,
ADR-B-0335, ADR-B-0156, ADR-B-0291, ADR-B-0444, ADR-B-0461
```

## Potwierdzone poprawki

| ID | Zmiana | Powód dydaktyczny |
|---|---|---|
| ADR-B-0015 | Dystraktor C zmieniony na „W miejscu dostępnym dopiero po przełożeniu części ładunku”; explanation dopasowane. | Poprzednia opcja „w magazynie przewoźnika” była zbyt oczywista. Nowa bada pomyłkę między obecnością sprzętu a szybkim dostępem. |
| ADR-B-0306 | Opcje A/B opisują teraz niepełne, lecz wiarygodne zestawy dokumentów; explanation wyjaśnia oba braki. | Poprzednie opcje o samej fakturze lub rozpisce godzin były łatwe do odrzucenia bez rozumienia ADR. |
| ADR-B-0376 | Dystraktor C zmieniony na „Wystarczy przeczytać etykietę gaśnicy dopiero podczas pożaru”; explanation dopasowane. | Sprawdza pomyłkę między doraźnym czytaniem etykiety a wcześniejszą znajomością obsługi. |
| ADR-B-0432 | Dystraktory odnoszą się teraz do wyboru najkrótszej trasy i masy największego towaru; explanation dopasowane. | Poprzedni dystraktor oparty na cenie ładunku był nienaturalny. Nowe opcje sprawdzają wiarygodne, lecz błędne uproszczenia przy różnych kodach tunelowych. |
| ADR-B-0471 | Dystraktor B zmieniony na zgodę kierowcy i pasażera oraz deklarowaną znajomość zagrożeń; explanation dopasowane. | Sprawdza błędne przekonanie, że zgoda i świadomość ryzyka mogą zastąpić wymaganie ADR. |

W żadnym z pięciu pytań próbki nie zmieniono ID, poprawnej litery ani podstawy prawnej. Dwa dodatkowe follow-upy poza próbką (ADR-B-0288 i ADR-B-0290) wykorzystano do poprawy czytelności wzoru nalepki i wiarygodności pomyłki dotyczącej obowiązków pakującego. Nie wykryto potwierdzonej sprzeczności prawnej wymagającej zmiany klucza. Pozostałe 35 pytań próbki pozostawiono bez zmian.

## Przykłady przed/po

1. **ADR-B-0432, opcja B** — przed: „Zakres ograniczeń ustala się wyłącznie według tańszego z przewożonych towarów”. Po: „Stosuje kod tunelowy towaru, którego masa w ładunku jest największa”. Nowa opcja nadal jest błędna, ale sprawdza typową pomyłkę: wybór jednego towaru według udziału masy zamiast zastosowania reguły ADR dla całego ładunku.
2. **ADR-B-0306, opcja B** — przed: „Wyłącznie rozpiska godzin pracy”. Po: „Dokumenty przewozowe i dokument kierowcy, bez instrukcji pisemnych, jeśli kierowca zna procedury”. Teraz trzeba rozumieć, że znajomość procedury nie zastępuje wymaganego dokumentu.
3. **ADR-B-0376, opcja C** — przed: „Gaśnicy wolno używać wyłącznie po dostawie towaru”. Po: „Wystarczy przeczytać etykietę gaśnicy dopiero podczas pożaru”. Nowa opcja jest bardziej wiarygodną pomyłką początkującego, a explanation wyjaśnia potrzebę wcześniejszej znajomości sprzętu.

## Quality Gate — preflight

- Rekordy: 609; unikalne ID: 609; duplikaty ID: 0.
- Statusy: 609 `needs_review`, 0 `verified`.
- Explanation poniżej 200 znaków: 0; minimum w banku: 300 znaków.
- „Poprawna = jedyna najdłuższa”: 70/609 = 11,49%, limit ≤18%.
- Maksimum działu: B-11 — 6/43 = 13,95%, poniżej ostrzejszego progu działowego 14%.

| Dział | Pytań | Poprawna jedyną najdłuższą | Odsetek |
|---|---:|---:|---:|
| B-01 | 45 | 6 | 13,33% |
| B-02 | 56 | 7 | 12,50% |
| B-03 | 49 | 5 | 10,20% |
| B-04 | 46 | 6 | 13,04% |
| B-05 | 43 | 5 | 11,63% |
| B-06 | 45 | 6 | 13,33% |
| B-07 | 48 | 6 | 12,50% |
| B-08 | 42 | 3 | 7,14% |
| B-09 | 46 | 5 | 10,87% |
| B-10 | 55 | 4 | 7,27% |
| B-11 | 43 | 6 | 13,95% |
| B-12 | 44 | 5 | 11,36% |
| B-13 | 47 | 6 | 12,77% |

## Synchronizacja
- Zaktualizowano migawki `review/legal-clauses` i `review/sequential` dla siedmiu zmienionych ID: pięciu z próbki oraz follow-upów ADR-B-0288 i ADR-B-0290.
- Zaktualizowano `source_bank_head` w wariantach i kluczach egzaminu próbnego 001–005. Nie zmieniono składu wariantów ani kluczy odpowiedzi. Żadne z siedmiu zmienionych ID nie występuje w wariantach 001–005.
- Manifest próby i wykluczeń: [etap 4x122 — manifest](etap-4x122-wykluczenia-proby.json).
- Pakiet recenzyjny i indeksy zaktualizowano do nowego blob SHA; statusy i zastrzeżenie o niezależnej recenzji pozostają bez zmian.

## Testy i ograniczenia
Próba skryptowa potwierdziła parsowanie JSONL, 609 unikalnych ID, poprawne litery A/B/C, minimum explanation 300 znaków i wskaźnik długości odpowiedzi. Próba lokalnego klonowania repo nie powiodła się, ponieważ środowisko nie rozwiązuje `github.com` (DNS). Dlatego nie deklaruję lokalnego uruchomienia pełnego zestawu testów; przed scaleniem wymagany jest PASS obu jobów Quality Gate CI.

Dla etapów 4x103–4x106 nie znaleziono kompletnych, oddzielnych manifestów ID w repo. Nie deklaruję zatem pełnej rozłączności z ewentualnymi nieujętymi pytaniami z tych etapów; ograniczenie jest zapisane w manifeście. Recenzja prawna specjalisty pozostaje wymagana.
