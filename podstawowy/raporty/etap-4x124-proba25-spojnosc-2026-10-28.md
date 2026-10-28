# Etap 4x124 — pozostała pula, explanation i spójność egzaminów

- Data: 28.10.2026.
- Punkt wejścia: świeży `main` po PR #586, commit `4a2c9b343acffff5f6d7739155ad18795b37e811`.
- Zakres: kurs podstawowy ADR; bez cystern i innych kursów.
- Próbka: wszystkie **25 ID**, które pozostały po wykluczeniach i zapisanych próbkach 4x114–4x123. Pula nie pozwalała na nową próbkę 40 pytań bez powtarzania ID, dlatego nie zawyżono liczebności ani nie przedstawiono powtórzeń jako nowych.

## Lista sprawdzonych ID

- `ADR-B-0005`
- `ADR-B-0031`
- `ADR-B-0052`
- `ADR-B-0064`
- `ADR-B-0184`
- `ADR-B-0198`
- `ADR-B-0211`
- `ADR-B-0234`
- `ADR-B-0293`
- `ADR-B-0300`
- `ADR-B-0304`
- `ADR-B-0314`
- `ADR-B-0328`
- `ADR-B-0339`
- `ADR-B-0352`
- `ADR-B-0374`
- `ADR-B-0431`
- `ADR-B-0434`
- `ADR-B-0482`
- `ADR-B-0483`
- `ADR-B-0493`
- `ADR-B-0512`
- `ADR-B-0562`
- `ADR-B-0579`
- `ADR-B-0602`

## Wynik przeglądu

Przeczytano treść pytania, A/B/C, poprawną literę i explanation jak początkujący kursant. W 24 rekordach explanation były już zrozumiałe: 2–5 zdań, sens poprawnej odpowiedzi, omówienie kuszących błędnych opcji i wskazanie ADR. Nie znaleziono potwierdzonego powodu do zmiany tych pytań ani ich kluczy.

**Jedna potwierdzona korekta: ADR-B-0293 (ADR 8.3.1).**
- Przed: „Nie powinno się przewozić osób niebędących członkami załogi”.
- Po: „Nie wolno przewozić osób, które nie są członkami załogi”.
- Explanation przepisano na 3 zdania: zakaz i jego sens, wyjaśnienie dlaczego wolne miejsce/kamizelka nie znoszą wymogu, a na końcu podstawa ADR 8.3.1.
- Uzasadnienie: dotychczasowe „nie powinno się” brzmiało jak zalecenie, choć ADR 8.3.1 formułuje zakaz przewożenia osób spoza załogi w zakresie stosowania przepisu. Zmiana jest redakcyjnym doprecyzowaniem, nie zatwierdzeniem prawnym.
- Zaktualizowano migawki `review/legal-clauses/291-293.json` i `review/sequential/291-293.json`. ID 0293 nie występuje w wariantach egzaminu 001–005; odświeżono w nich jedynie metadane źródłowego SHA banku.
- W lekcji B-07 doprecyzowano opis zakazu i scenariusz pasażera spoza załogi, tak aby podręcznik nie osłabiał zakazu do samego zalecenia.

## Kontrola synchronizacji

- Bank: 609 unikalnych ID; wszystkie `needs_review`, 0 `verified`.
- Warianty i klucze 001–005 wskazują aktualny bank; każdy ma 30 unikalnych ID, A/B/C = 10/10/10, a tekst opcji oznaczonej w kluczu odpowiada poprawnej odpowiedzi z banku.
- Scenariusze i pozostałe pytania nie zmieniły się.
- „Poprawna = jedyna najdłuższa”: **69/609 = 11,33%**; maksimum działu **13,95%** (B-11).
- Explanation: minimum **300 znaków**, **0** poniżej 200.
- Status prawny wszystkich 609 pytań: `needs_review`; nie zmieniano statusów na `verified`.

## Quality Gate i ograniczenia

Manifest jawnie dokumentuje wyczerpanie dostępnej puli unikalnych ID po 4x114–4x123. Pełna rozłączność z 4x103–4x113 nie jest potwierdzona, ponieważ część starszych raportów nie zawiera kompletnych list wykluczeń. Testy lokalne nie są dostępne w tej sesji przez połączenie GitHub API; wymagany PASS CI przed scaleniem.

