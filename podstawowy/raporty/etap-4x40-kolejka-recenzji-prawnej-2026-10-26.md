# Etap 4x40 — priorytetyzacja otwartej recenzji prawnej

- Data: 2026-10-26.
- Świeży `main` po PR #482: `efb084fcd64ffa1f6c3acb0d3797aa5a7bef1ebc`.
- Zakres: wyłącznie kurs podstawowy ADR; nie zmieniano banku pytań ani statusów.

## Dlaczego kolejny krok dotyczy dowodów prawnych

Etap 4x39 potwierdził spójność redakcyjną wybranej próbki. Następną istotną luką jest niezakończone, literalne porównanie z prawnie wiążącym polskim tekstem ADR 2025. Manifest nadal raportuje **376** nierozstrzygniętych porównań. Osobna lista specjalisty zawiera **121** ID bez zapisanego dosłownego fragmentu pomocniczego MI. To różne liczniki i nie wolno ich sumować ani traktować jako zamiennych.

Zasada zapisana w przekazaniu po 4x24 pozostaje w mocy: nie ponawiamy prób wydobywania cytatów z MI/PDF. Rozstrzygnięcie wymaga specjalisty i oficjalnego tekstu Dz.U. 2025 poz. 642 wraz ze sprostowaniem poz. 1575.

## Kolejka priorytetowa

Przygotowano 20 rekordów z listy 121 ID bez dosłownego fragmentu. Kolejność jest heurystyczna: premiuje liczby/progi, wyjątki, klasy o istotnych konsekwencjach bezpieczeństwa, dopuszczenie pojazdów, kody tunelowe oraz wymagane dokumenty.

| ID | Dział | Podstawa w banku | Powód priorytetu |
|---|---|---|---|
| ADR-B-0490 | ADR-B-11 | ADR 2025, 8.6.4, kod B1000C | próg liczbowy i kod tunelowy B1000C; materiał wybuchowy — wysoka waga bezpieczeństwa |
| ADR-B-0317 | ADR-B-02 | ADR 2025, 2.2.7.1.1 oraz 2.2.7.2.2.1–2.2.7.2.2.6 | kryteria klasy 7 i wartości progowe; klasyfikacja materiału promieniotwórczego |
| ADR-B-0497 | ADR-B-02 | ADR 2025, 2.2.1.1.5, podklasa 1.5 | podklasa materiałów wybuchowych; rozróżnienie małej wrażliwości i zagrożenia wybuchem masowym |
| ADR-B-0137 | ADR-B-08 | ADR 2025, 9.1.2.1; 9.1.3 | kategorie pojazdów i dopuszczenie; wymóg dokumentacyjny/certyfikacyjny |
| ADR-B-0162 | ADR-B-02 | ADR 2025, 5.2.2.2.2 (model nr 9A); 3.2 tabela A: UN 3551, UN 3552; 2.2.9.1.7.2 | baterie sodowo-jonowe UN 3551/3552; nalepka klasy 9A i powiązane wymagania |
| ADR-B-0402 | ADR-B-12 | ADR 2025, 1.10.3.2.2(d) | plan ochrony towarów dużego ryzyka; zakres działań ochronnych |
| ADR-B-0451 | ADR-B-10 | ADR 2025, 1.1.4.7.2(c) | termin badania okresowego butli DOT; warunki wyjątku eksportowego |
| ADR-B-0452 | ADR-B-10 | ADR 2025, 1.1.4.7.2(c) | termin badania butli DOT; zakres dopuszczonego przewozu do badania |
| ADR-B-0501 | ADR-B-02 | ADR 2025, 2.2.9.1.7.2(c) | baterie sodowo-jonowe UN 3551; warunki techniczne i zwarcie zewnętrzne |
| ADR-B-0510 | ADR-B-02 | ADR 2025, 2.2.43.1.1 | klasa 4.3 i reakcja z wodą; bezpieczne postępowanie przy uszkodzonym opakowaniu |
| ADR-B-0522 | ADR-B-01 | ADR 2025, 1.3.2.2 | szkolenie funkcjonalne w łańcuchu multimodalnym; zakres obowiązku szkoleniowego |
| ADR-B-0530 | ADR-B-13 | ADR 2025, 5.4.1.1.3 | opis odpadu w dokumencie przewozowym; wymagany zapis w ADR 5.4.1.1.3 |
| ADR-B-0534 | ADR-B-01 | ADR 2025, 3.4.11 | oznaczenie LQ opakowania zbiorczego; widoczność wymaganych oznaczeń |
| ADR-B-0537 | ADR-B-13 | ADR 2025, 5.4.1.1.1(f) | całkowita ilość dla różnych towarów UN; format danych ilościowych w dokumencie |
| ADR-B-0595 | ADR-B-01 | ADR 2025, 1.1.3.1(a) | wyłączenie dla osoby prywatnej; warunki łączne, nie sam prywatny cel |
| ADR-B-0599 | ADR-B-13 | ADR 2025, 5.4.1.1.1(e)–(f) | ilość towaru a liczba opakowań; wymagana zawartość dokumentu |
| ADR-B-0489 | ADR-B-11 | ADR 2025, 8.6.4, kod B/D | kod tunelowy B/D; różnica między kodem a kategorią tunelu |
| ADR-B-0508 | ADR-B-13 | ADR 2025, 5.4.1.1.1(a) | format numeru UN w dokumencie; wymagany prefiks UN |
| ADR-B-0536 | ADR-B-13 | ADR 2025, 5.4.1.1.1 | kolejność elementów opisu ADR; warunki prawidłowego wpisu |
| ADR-B-0591 | ADR-B-11 | ADR 2025, 8.6.3; 8.6.4 | ograniczenia tunelowe na trasie; decyzja przed wjazdem do tunelu |

Pełny rejestr strukturalny: `review/specialist/KOLEJKA-PRIORYTETOWA-4X40.json`.

## Jak specjalista ma rozstrzygać pozycję

1. Otworzyć dokładny punkt, tabelę, kolumnę i przypisy w ogłoszonym polskim tekście Dz.U. 2025 poz. 642 oraz sprawdzić sprostowanie poz. 1575.
2. Porównać niezależnie stem, odpowiedzi A/B/C, poprawną literę, explanation i podstawę prawną.
3. Zapisać dosłowny cytat i numer strony Dz.U. — nie przenosić paginacji kopii MI na Dziennik Ustaw.
4. Jeśli nie da się potwierdzić, pozostawić pozycję otwartą i opisać konkretną przyczynę; nie zgadywać i nie zmieniać klucza na podstawie pamięci.
5. Nie ustawiać `verified` bez autentycznej recenzji i zapisu dowodów.

## Kontrole niezmienione

- Bank: 609 pytań; 609 `needs_review`, 0 `verified`.
- Wskaźnik „poprawna = jedyna najdłuższa”: 72/609 = 11,82% globalnie; najwyższy dział 14,29%.
- Nie zmieniono treści pytań, odpowiedzi, explanation, wariantów egzaminów ani kluczy.
- To kolejka organizacyjna, nie wynik recenzji prawnej i nie redukuje liczby nierozstrzygniętych porównań.

## Ograniczenia

Testy lokalne nie zostały uruchomione: środowisko nie mogło rozwiązać `github.com` przy próbie klonowania. PR wymaga PASS pełnego Quality Gate CI. Wszystko pozostaje w kursie podstawowym; nie rozpoczęto cystern ani innego kursu.
