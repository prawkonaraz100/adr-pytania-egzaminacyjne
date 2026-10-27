# Etap 4x97 — regresja bieżącej migawki i indeksów kursu

- Data: 2026-10-27.
- Punkt wejścia: `main` po scaleniu PR #554, commit `1fcd549636b49cb91ec337c1648524752f336ff4`.
- Zakres: wyłącznie kurs podstawowy ADR; bez zmian merytorycznych w banku.

## 1. Znalezisko i poprawka

Po scaleniu 4x96 README kursanta i dwa indeksy pakietu recenzyjnego nadal nazywały etap 4x95 bieżącym. To był potwierdzony błąd dokumentacji: aktualny raport i wynik integracji 4x96 już istniały, ale nie były wskazane jako najnowsza migawka. Zaktualizowano:
- `podstawowy/README.md` — status 4x97 po scaleniu 4x96 i linki do raportu oraz listy próbki;
- `review/specialist/PRZEKAZANIE-ETAP4.md` — bieżąca migawka 4x96, stan banku i jawne ograniczenie próbki;
- `review/README.md` — bieżący stan i odsyłacze do raportu próbki.

## 2. Kontrole integracyjne

Punkt wyjścia z `main`:
- 609 pytań i 609 unikalnych ID; wszystkie `needs_review`, 0 `verified`;
- blob banku: `445c2d76652f2dccf5735f928083388484e147bc`;
- 39 scenariuszy praktycznych, trzy na każdy z 13 działów;
- pięć wariantów egzaminu i pięć kluczy, po 30 pytań;
- „poprawna = jedyna najdłuższa”: 73/609 = 11,99%; maksymalnie 14,29% w dziale;
- explanation minimum 300 znaków.

Dodano blokujący test `tests/test_stage4x97_current_snapshot.py`. Sprawdza, czy README kursanta i indeksy recenzyjne wskazują najnowszy raport, czy raport i JSON próbki istnieją, czy lista próbki zawiera 60 unikalnych ID z banku, czy nie przecina się z zapisanym zbiorem jawnych wykluczeń, czy manifest pakietu wskazuje aktualny blob i czy żadne pytanie nie zostało oznaczone jako `verified`.

## 3. Ograniczenie audytowe zachowane

Raport 4x86 nie publikuje kompletnej listy ID swojej próbki. Raport 4x96 wyklucza wszystkie ID jawnie wymienione w raportach 4x84–4x95, ale nie deklaruje udowodnionego braku przecięcia z nieujawnioną częścią 4x86. Test utrwala ten jawny status ograniczenia, nie tworzy pozornej gwarancji.

## 4. Status

Ta partia nie zmienia banku, poprawnych liter, explanation ani statusów prawnych. Po CI wymagany jest PASS dla nowego testu i całego Quality Gate. Wszystkie pytania nadal wymagają niezależnej kontroli specjalisty ADR.
