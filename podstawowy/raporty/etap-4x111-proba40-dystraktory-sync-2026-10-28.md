# Etap 4x111 — próbka 40, jakość dystraktorów i synchronizacja audytu

- Data: 2026-10-28.
- Punkt wyjścia: świeży `main` po PR #569, commit `dadb15e223a7721e9a05163c55a5778f7be07c35`.
- Zakres: wyłącznie kurs podstawowy ADR.
- Bank przed partią: 609 pytań, wszystkie `needs_review`, 0 `verified`.
- Manifest próby: [etap 4x111 — seed i wykluczenia](etap-4x111-wykluczenia-proby.json), seed `41112026`.

## 1. Próba 40 explanation

Pula po konserwatywnym wykluczeniu identyfikatorów z artefaktów 4x103–4x109, próbki 4x110 i pytań zmienionych w 4x110: 266 pytań. Sprawdzono 40 unikalnych pytań, rozłącznych z zapisanym zbiorem wykluczeń.

- Explanation w próbie: 302–451 znaków.
- Liczba zdań: 4–5.
- Jednozdaniowe: 0; poniżej 200 znaków: 0.
- 35 explanation pozostało bez zmian, ponieważ już prostym językiem tłumaczyły poprawną odpowiedź, najważniejszą pomyłkę i podawały podstawę ADR.
- W pięciu pytaniach explanation dopasowano do przeredagowanych dystraktorów. Wszystkie pozostają w granicach 2–5 zdań i 200–500 znaków.

Lista próby: `ADR-B-0027`, `ADR-B-0061`, `ADR-B-0191`, `ADR-B-0029`, `ADR-B-0462`, `ADR-B-0090`, `ADR-B-0324`, `ADR-B-0296`, `ADR-B-0036`, `ADR-B-0228`, `ADR-B-0467`, `ADR-B-0179`, `ADR-B-0334`, `ADR-B-0142`, `ADR-B-0415`, `ADR-B-0494`, `ADR-B-0189`, `ADR-B-0151`, `ADR-B-0082`, `ADR-B-0511`, `ADR-B-0567`, `ADR-B-0271`, `ADR-B-0351`, `ADR-B-0093`, `ADR-B-0321`, `ADR-B-0123`, `ADR-B-0476`, `ADR-B-0584`, `ADR-B-0256`, `ADR-B-0457`, `ADR-B-0038`, `ADR-B-0146`, `ADR-B-0066`, `ADR-B-0037`, `ADR-B-0170`, `ADR-B-0454`, `ADR-B-0594`, `ADR-B-0382`, `ADR-B-0041`, `ADR-B-0423`.

## 2. Potwierdzone słabości dystraktorów i poprawki

| ID | Problem potwierdzony w przeglądzie | Poprawka | Podstawa |
|---|---|---|---|
| ADR-B-0082 | „Sprawdź prędkość dojazdu” nie sprawdzało rozumienia warunku CV28 i było łatwe do odrzucenia. | Zastąpiono je typowym błędem: uznaniem, że sama klasa 6.1 przesądza o oddzieleniu od żywności. Explanation wyjaśnia rolę numeru UN i tabeli A. | ADR 7.5.4; 7.5.11, CV28; tabela A, kol. 18 |
| ADR-B-0123 | „Towar cięższy od tony” nie było wiarygodnym kryterium definicji towaru niebezpiecznego. | Zastąpiono je błędem polegającym na utożsamieniu dużej ilości z niebezpiecznymi właściwościami. | Umowa ADR, art. 1(b) |
| ADR-B-0296 | „Otworzyć drzwi” i „włączyć urządzenia, by lepiej widzieć” zbyt słabo odzwierciedlały typowe racjonalizacje ryzyka. | Wprowadzono błędne, ale wiarygodne założenia: wyjście z kabiny usuwa ryzyko oraz brak widocznej iskry oznacza bezpieczeństwo. Explanation wskazuje, że oba założenia są błędne. | ADR 5.4.3.4, instrukcje pisemne |
| ADR-B-0351 | „Wyłączyć radio” było niezwiązane z wymaganiem hamulca postojowego. | Zastąpiono je błędem polegającym na uznaniu biegu i płaskiego terenu za zamiennik hamulca. | ADR 8.3.7 |
| ADR-B-0423 | „Wystarczy dostęp po rozładunku” było skrajnie oczywiste i nie badało rozumienia dostępności sprzętu. | Zastąpiono je błędem: gaśnica może być za ładunkiem, jeśli ma stabilny uchwyt. Explanation odróżnia stabilne mocowanie od szybkiej dostępności. | ADR 8.1.4.5 |

Nie zmieniono ID ani poprawnych liter. Zaktualizowano migawki `review/sequential/` oraz `review/legal-clauses/` dla zmienionych rekordów; wszystkie statusy recenzji prawnej pozostały `pending` / `needs_review`. Nie zmieniono żadnej podstawy prawnej i nie oznaczono pytań jako `verified`.

## 3. Spójność egzaminów i pakietu recenzyjnego

- Żadne z pięciu zmienionych pytań nie występuje w wariantach 001–005, więc ich treść i klucze nie wymagały merytorycznej regeneracji.
- Odświeżono `source_bank_head` w wariantach i kluczach 001–005 do `a0d901b67548cd9ae66eeb8fa09b7c8264640e3c`.
- Odświeżono źródłowe migawki pakietu recenzyjnego i kolejek priorytetowych do bieżącego blobu banku. Pytania w kolejce nadal wymagają niezależnego porównania z urzędowym tekstem.
- Scenariusze pozostały bez zmian; ich liczba wynosi 39. W tej partii nie wykryto potwierdzonej sprzeczności wymagającej zmiany scenariusza.

## 4. Quality Gate — metryki

- Bank: 609 unikalnych pytań.
- „Poprawna odpowiedź = jedyna najdłuższa”: 72/609 = 11.82% (limit globalny 18%).
- Najkrótsze explanation: 300 znaków; poniżej 200: 0.
- Statusy: 609 `needs_review`, 0 `verified`.

| Dział | Pytań | Poprawna = jedyna najdłuższa | Wskaźnik |
|---|---:|---:|---:|
| ADR-B-01 | 45 | 6 | 13.33% |
| ADR-B-02 | 56 | 8 | 14.29% |
| ADR-B-03 | 49 | 6 | 12.24% |
| ADR-B-04 | 46 | 5 | 10.87% |
| ADR-B-05 | 43 | 5 | 11.63% |
| ADR-B-06 | 45 | 6 | 13.33% |
| ADR-B-07 | 48 | 6 | 12.50% |
| ADR-B-08 | 42 | 5 | 11.90% |
| ADR-B-09 | 46 | 4 | 8.70% |
| ADR-B-10 | 55 | 4 | 7.27% |
| ADR-B-11 | 43 | 6 | 13.95% |
| ADR-B-12 | 44 | 6 | 13.64% |
| ADR-B-13 | 47 | 5 | 10.64% |

## Ograniczenia

Próba jest rozłączna z zapisanym zestawem wykluczeń. Nie dowodzi rozłączności z nieudokumentowanymi częściami próbek sprzed 4x103. Lokalny `git clone` nie powiódł się z powodu błędu DNS dla `github.com`; lokalnego PASS nie deklarowano. Ostateczny wynik zależy od GitHub Actions Quality Gate. Niezależna recenzja prawna nadal pozostaje otwarta.
