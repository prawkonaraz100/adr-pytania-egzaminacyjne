# Etap 4x20 — audyt czytelności explanation ADR-B-0101–0150

- Punkt wyjścia: świeży `main` `3f1a33c6e417cb5a7e7e62273f38dc775b86e580`.
- Zakres: 50 pytań ADR-B-0101–0150.
- Metoda: skryptowa lista kandydatów (odwołania do punktów, akronimy, sygnały wyjaśniające) i ręczna lektura. Heurystyka nie była traktowana jako dowód błędu.

## Wynik

- Ręcznie przejrzano 50/50 explanation: ADR-B-0101–ADR-B-0150.
- Przepisano 8 explanation: ADR-B-0119, 0125, 0128, 0129, 0137, 0141, 0142 i 0145.
- Pozostałe 42 pozostawiono bez zmian; osiem trafień heurystycznych uznano za fałszywe alarmy:
  - **ADR-B-0106** — poprawnie wyjaśnia stronę nawietrzną i ryzyko wdychania oparów.
  - **ADR-B-0114** — samo wyjaśnienie już definiuje numer UN jako czterocyfrowy numer poprzedzony literami „UN”.
  - **ADR-B-0116** — prosty opis ryzyka wycieku i warunku wstrzymania przewozu.
  - **ADR-B-0120** — wyjaśnia, dlaczego weryfikacja tożsamości ogranicza ryzyko nieuprawnionego przejęcia.
  - **ADR-B-0130** — jasne polecenie unikania kontaktu z nieznaną cieczą i oparami.
  - **ADR-B-0136** — poprawnie wyjaśnia ograniczenie dotyczące pasażera spoza załogi.
  - **ADR-B-0147** — definiuje jednostkę transportową i wyjaśnia praktyczne znaczenie tej definicji.
  - **ADR-B-0150** — prostym językiem odróżnia wybuch masowy od ograniczonego zagrożenia podklasy 1.4.

## Przykłady przed/po

1. **ADR-B-0119 — IMDG**
   - Przed: „Ładunek przybyły statkiem może mieć oznakowanie IMDG...”
   - Po: dodano rozwinięcie IMDG jako międzynarodowego kodeksu przewozu towarów niebezpiecznych drogą morską i wyjaśniono, że uznanie oznakowania na drodze zależy od warunków ADR.
   - Podstawa: ADR 1.1.4.2.

2. **ADR-B-0128 — numer UN i klasa**
   - Przed: „W tabeli A odczytuje się ją z kolumny 3a; kolumna 1 służy do numeru UN...”
   - Po: wyjaśniono, że numer UN to czterocyfrowy identyfikator towaru, natomiast klasa opisuje rodzaj zagrożenia; wskazano też funkcję kolumn 1, 3a i 4.
   - Podstawa: ADR 3.2.1, tabela A.

3. **ADR-B-0137 — typy pojazdów**
   - Przed: „...EX/II, EX/III, FL, AT oraz MEMU...”
   - Po: wyjaśniono, że EX/II i EX/III są typami pojazdów do określonych materiałów wybuchowych, FL i AT odnoszą się do kategorii pojazdów cysternowych, a MEMU to mobilna jednostka do wytwarzania materiałów wybuchowych.
   - Podstawa: ADR 9.1.2.1 i 9.1.3.

## Wszystkie poprawione rekordy

- ADR-B-0119 — IMDG i oznakowanie w łańcuchu morsko-drogowym.
- ADR-B-0125 — numer UN i jego miejsce w tabeli A.
- ADR-B-0128 — numer UN, klasa zagrożenia i grupa pakowania.
- ADR-B-0129 — numer UN, grupa pakowania III i klasyfikacja odpadu.
- ADR-B-0137 — typy EX/II, EX/III, FL, AT oraz MEMU.
- ADR-B-0141 — różnica między ADR, RID i IMDG.
- ADR-B-0142 — warunkowe uznanie oznakowania IMDG na odcinku drogowym.
- ADR-B-0145 — kategoria pojazdu FL i świadectwo dopuszczenia.

## Integralność i metryki

- Bank: 609 rekordów, 609 unikalnych ID, 0 duplikatów.
- Explanation minimum: 300 znaków; 0 poniżej 300.
- Wszystkie pytania pozostają `needs_review`; `verified`: 0.
- Zmieniono tylko explanation, więc wskaźnik „poprawna = jedyna najdłuższa” pozostaje bez zmian:
  - B-01: 6/45 = 13,33%
  - B-02: 8/56 = 14,29%
  - B-03: 7/49 = 14,29%
  - B-04: 6/46 = 13,04%
  - B-05: 6/43 = 13,95%
  - B-06: 5/45 = 11,11%
  - B-07: 6/48 = 12,50%
  - B-08: 5/42 = 11,90%
  - B-09: 4/46 = 8,70%
  - B-10: 4/55 = 7,27%
  - B-11: 6/43 = 13,95%
  - B-12: 6/44 = 13,64%
  - B-13: 4/47 = 8,51%
- Zsynchronizowano arkusze i klucze egzaminów 001–005 oraz migawki audytów `review/sequential/` i `review/legal-clauses/` dla ośmiu zmienionych pytań.
- Nie zmieniono opcji, poprawnych liter ani statusów prawnych.

## Ograniczenia

To kontrola językowa, nie formalna recenzja prawna. Wymagany jest PASS Quality Gate CI; lokalny checkout nie był dostępny w tym środowisku.
