# ETAP 4x3 — raport końcowy zgodności banku z podręcznikiem

- Data: 25.10.2026.
- Zakres: kurs podstawowy ADR; 13 działów, 609 pytań.
- Wynik partii: PR #309 (B-01–04), #310 (B-05–08), #311 (B-09–12), #312 (B-13) — wszystkie scalone po PASS CI.

## Zestawienie audytu

| Działy | Liczba pytań | Raport szczegółowy |
|---|---:|---|
| ADR-B-01–04 | 196 | [Raport B-01–04](etap-4x3-pokrycie-banku-01-04-2026-10-25.md) |
| ADR-B-05–08 | 178 | [Raport B-05–08](etap-4x3-pokrycie-banku-05-08-2026-10-25.md) |
| ADR-B-09–12 | 188 | [Raport B-09–12](etap-4x3-pokrycie-banku-09-12-2026-10-25.md) |
| ADR-B-13 | 47 | [Raport B-13](etap-4x3-pokrycie-banku-13-2026-10-25.md) |
| **Razem** | **609** | Wszystkie rekordy objęte mapowaniem pytanie → fragment lekcji → źródło wskazane w rekordzie |

## Kontrola kompletności map pytań w lekcjach

Na aktualnym `main` porównano sekcję „Powiązane pytania w banku” każdej z 13 lekcji z rzeczywistym `module_id` w `podstawowy/questions.jsonl`.

- B-01: 45/45; B-02: 56/56; B-03: 49/49; B-04: 46/46.
- B-05: 43/43; B-06: 45/45; B-07: 48/48; B-08: 42/42.
- B-09: 46/46; B-10: 55/55; B-11: 43/43; B-12: 44/44; B-13: 47/47.
- Brakujące odwołania: 0. Nadmiarowe/obce odwołania: 0. ID nieistniejące: 0.

## Co uzupełniono

- B-01–04: szkolenie i ewidencja ADR 1.3, pola tabeli A, wyłączenia LQ/EQ/1.1.3.6, klasy i przypadki szczególne, znak środowiskowy i klasyfikacja odpadów, załoga i postój.
- B-05–08: instrukcje pisemne i reakcja na zdarzenie, tablice pomarańczowe i nalepki dużego formatu, obowiązki uczestników, gaśnice/wyposażenie i świadectwa pojazdów.
- B-09–12: wspólny załadunek i przewóz luzem, transport kombinowany, kody tunelowe i plan ochrony.
- B-13: kolejność pól dokumentu przewozowego, wpisy szczególne, dokumenty w kabinie oraz wzór, język i dostępność instrukcji pisemnych.

## Egzaminy próbne — kontrola po audycie

Nie zmieniono banku, ID pytań, kluczy ani przypisań `module_id`. Dlatego regeneracja wariantów nie była potrzebna. Zweryfikowano istniejące pliki wariantów 001–003 i kluczy:

- każdy wariant ma 30 pytań i 30 odpowiedzi w kluczu;
- brak duplikatów wewnątrz wariantu i brak powtórzeń między wariantami (łącznie 90 różnych ID);
- brak ID nieistniejących, niezgodności `module_id`, rozbieżności treści/opcji i rozbieżności klucza/wyjaśnienia względem bieżącego banku;
- każdy wariant obejmuje 13 działów;
- wszystkie warianty nadal mają `publication_authorized: false` i pozostają treningiem wewnętrznym. Brak regeneracji nie oznacza zatwierdzenia egzaminu.

## Quality Gate — bieżący bank

- Liczba rekordów: 609; unikalne ID: 609.
- Statusy: 609 `needs_review`, 0 `verified`.
- Poprawna odpowiedź jest jedyną najdłuższą: 86/609 = 14.12% (limit ≤18%).
- Najkrótsze explanation: 300; poniżej 200 znaków: 0; explanation poza zakresem 2–5 zdań: 0.

## Ograniczenia i dalsza kontrola

Audyt sprawdza pokrycie dydaktyczne i spójność referencji, ale nie stanowi niezależnej opinii prawnej. Wszystkie pytania nadal wymagają recenzji — nie zmieniono żadnego statusu na `verified`. Przed publicznym użyciem należy przeprowadzić niezależną recenzję ADR i formalny odbiór instruktorski.


## Korekta końcowej kontroli treści

W końcowym przeglądzie po audycie poprawiono opis tablicy pomarańczowej w B-06: dolne pole zawiera czterocyfrowy numer UN bez liter „UN”. Jednocześnie dopilnowano, by uzupełnienia dla B-06–B-08 obejmowały szczegółowy odczyt tablicy, obowiązki uczestników i wyposażenie zależne od DMC/zagrożeń. Nie zmieniono banku ani przypisań pytań.
