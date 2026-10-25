# Raport końcowy ETAPU 4x7 — powtórzenia i czytelność banku

**Data:** 25.10.2026  
**Zakres:** wyłącznie kurs podstawowy ADR; 609 pytań ADR-B-0001…ADR-B-0609.

## Wynik

- Przeskanowano wszystkie 609 pytań pod kątem podobieństwa stemów i identycznych zestawów odpowiedzi w obrębie modułu.
- **Potwierdzone duplikaty dydaktyczne poprawione: 1 para.** Zachowano oba ID; przeredagowano ADR-B-0585, aby sprawdzał mocowanie i ochronę gaśnicy przed uszkodzeniem, a ADR-B-0169 nadal sprawdza dostępność gaśnicy.
- **Wyjaśnienia poprawione: 59 rekordów** — 58 redakcyjnych doprecyzowań skrótów/terminów oraz 1 pełna zmiana explanation przy przeredagowaniu ADR-B-0585.
- Dodano `podstawowy/SLOWNICZEK.md`; README i wszystkie 13 lekcji linkują do słowniczka.
- Dodano blokującą bramkę `scripts/check_near_duplicates.py` oraz testy. Quality Gate wykrywa nowe pary w tym samym module o podobieństwie co najmniej 0,60 lub identycznych zestawach odpowiedzi. Dwie istniejące podobne pary mają jawne uzasadnienie w allowliście:
  - ADR-B-0071 / ADR-B-0072 — różne progi DMC i różne odpowiedzi wymagane przez tabelę ADR;
  - ADR-B-0330 / ADR-B-0337 — odrębne wyłączenia proceduralne dla klas 5.2 i 6.2.
- Wcześniejsza para ADR-B-0169 / ADR-B-0585 została usunięta z allowlisty po poprawce 0585. Nie znaleziono nowych nieudokumentowanych par.

## Partie i PR-y

| Partia | PR | Wynik |
|---|---|---|
| B-01–04 | [#327](https://github.com/prawkonaraz100/adr-pytania-egzaminacyjne/pull/327) | PASS i scalony |
| B-05–08 | [#328](https://github.com/prawkonaraz100/adr-pytania-egzaminacyjne/pull/328) | PASS i scalony |
| B-09–13 | [#329](https://github.com/prawkonaraz100/adr-pytania-egzaminacyjne/pull/329) | PASS i scalony |

Każda partia ma osobny raport szczegółowy w `podstawowy/raporty/`. Po zmianie explanation zsynchronizowano klucze egzaminów próbnych 001–005 i zaktualizowano `source_bank_head` wariantów. Nie zmieniły się ID, moduły ani poprawne litery, dlatego nie było potrzeby losowania nowych pytań do wariantów. Odświeżono snapshoty w `review/sequential/` i `review/legal-clauses/`; to aktualizacja integralności, nie nowa recenzja prawna.

## Końcowy Quality Gate

- Bank: **609 rekordów, 609 unikalnych ID, 0 duplikatów ID**.
- Status: **609 `needs_review`, 0 `verified`**.
- Poprawna odpowiedź jest jedyną najdłuższą w **82/609 = 13,46%**; próg CI wynosi 18%.
- Najkrótsze explanation: **300 znaków**; explanation poniżej 200 znaków: **0**.
- Warianty egzaminów próbnych: 001–005; klucze zsynchronizowane dla zmienionych wyjaśnień.
- Słowniczek jest podlinkowany z README i lekcji B-01–B-13.
- Kontrola podobieństwa jest częścią Quality Gate; CI PASS dla wszystkich trzech PR-ów.

## Ograniczenia i status prawny

Skan podobieństwa jest narzędziem przesiewowym, a nie dowodem błędu prawnego. Podobne pytania mogą sprawdzać różne progi, warunki lub wyjątki. Nie zmieniono odpowiedzi ani podstaw prawnych poza redakcją potwierdzonego duplikatu 0585. Nie dokonano niezależnej weryfikacji prawnej. Wszystkie pytania pozostają `needs_review`; niczego nie oznaczono jako `verified`. Kurs cystern ani inne specjalizacje nie były objęte pracami.
