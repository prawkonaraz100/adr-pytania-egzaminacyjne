# Kontrola druga — partia ADR-B-0316–0330

**Źródło:** ADR 2025, Dz.U. 2025 poz. 642 (polski tekst urzędowy); sprostowanie Dz.U. 2025 poz. 1575 nie zmienia punktów tej partii. Data kontroli: 9.11.2026.

**Wynik kontroli drugiej:** **1 OK (0319), 14 POPRAW, 0 BLOKUJ.** Żadnego rekordu nie oznaczono jako `verified`.

## Werdykty i zakres zmian

| ID | Werdykt | Podstawa / strona Dz.U. | Ustalenie kontroli drugiej |
|---|---|---|---|
| 0316 | POPRAW | 2.2.1.1.4; 2.2.1.1.6; 3.2.1 kol. (3b), s. 129–130, 308 | Stary temat podklasy 1.1 dublował 0126. Zastąpiono pytaniem o literę grupy zgodności w kodzie klasyfikacyjnym klasy 1. |
| 0317 | POPRAW | 2.2.7.1.1, s. 234 | Doprecyzowano warunek klasy 7: jednocześnie stężenie promieniotwórcze i aktywność całkowita przesyłki muszą przekraczać odpowiednie progi. |
| 0318 | POPRAW | 5.4.1.1.3.2, s. 963 | Stary temat wiedzy nadawcy dublował 0335/0336. Zastąpiono go zasadami szacowania ilości odpadów i wymaganym wpisem w dokumencie. |
| 0319 | OK | 9.1.1.2, s. 1342 | Definicje pojazdów EX/II i EX/III; klucz A pozostaje prawidłowy. Bez zmian. |
| 0320 | POPRAW | 1.2.3 (ADN), 1.2.1 (IMDG), s. 52, 36 | Stary temat dublował pytania o IMDG. Zastąpiono go rozróżnieniem przepisów dla żeglugi śródlądowej (ADN). |
| 0321 | POPRAW | 1.1.4.7.1; 1.1.4.2, s. 31, 29 | Stary temat dodatkowych informacji przy dokumencie IMDG dublował 0388/0398. Zastąpiono go warunkiem łańcucha transportowego dla butli DOT. |
| 0322 | POPRAW | 1.1.3.3(a); 8.6.3.3, s. 25, 1338 | Stary temat dublował 0512/0540. Zastąpiono go wyłączeniem paliwa w zbiornikach pojazdu przy ustalaniu kodu tunelowego. |
| 0323 | POPRAW | 1.1.3.6.2; tabela 1.1.3.6.3, s. 26–27 | Stary temat dublował 0606 oraz 0272/0570/0571. Zastąpiono go niestosowaniem działu 5.3 w przewozie objętym limitem 1.1.3.6. |
| 0324 | POPRAW | 7.5.2.1, s. 1305 | Obraz tabeli potwierdza klucz A dla „5.2 + 1” i „5.2”. Usunięto wady formy odpowiedzi; nie zmieniono klucza. |
| 0325 | POPRAW | 2.1.3.9, s. 123 | Stary temat dublował 0129. Zastąpiono go odpadami objętymi Konwencją Bazylejską i pozycjami UN 3077/3082. |
| 0326 | POPRAW | 2.1.3.5.5, s. 123 | Przeredagowano odpowiedzi; wyłączenie metody uproszczonej dla klasy 4.3. |
| 0327 | POPRAW | 2.1.3.5.5, s. 123 | Przeredagowano odpowiedzi; odpad mający wyłącznie właściwości zagrażające środowisku. |
| 0328 | POPRAW | 2.1.3.5.5, s. 123 | Przeredagowano odpowiedzi; domyślna II grupa pakowania po wykazaniu, że nie zachodzą kryteria I grupy. |
| 0329 | POPRAW | 2.1.3.5.5, s. 123 | Przeredagowano odpowiedzi; wyłączenie odpadów zawierających materiały niedopuszczone do przewozu według 2.2.x.2. |
| 0330 | POPRAW | 2.1.3.5.3(g); 2.1.3.5.5, s. 122–123 | Przeredagowano odpowiedzi; wyłączenie odpadów zawierających nadtlenki organiczne klasy 5.2 z listy 2.1.3.5.3. |

## Najważniejsze rozstrzygnięcia

- **Duplikaty:** 0316, 0318, 0320, 0321, 0322, 0323 i 0325 zastąpiono nowymi tematami w tej samej kompetencji. W kontroli całego banku uwzględniono m.in. 0388/0398, 0606, 0129 oraz 0335/0336.
- **Forma:** 0317 i 0326–0330 zachowały podtemat, ale otrzymały przeredagowane treści. 0324 rozstrzygnięto z obrazu tabeli 7.5.2.1 na s. 1305; wcześniejsze BLOKUJ było nieuzasadnione.
- **Strona:** punkt 1.1.3.6.4 znajduje się na s. 28, nie s. 27.
- **Dalsze podobieństwa do sprawdzenia w kolejnych partiach:** 0337–0339 dublują stary temat 0330 i siebie nawzajem; 0335/0336 i 0334/0344 również są podobnymi parami; 0341/0343 są bliskie 0129.

## Wdrożenie

- Zapisano 14 pełnych rekordów korekt w `review/literal-pl/POPRAWKI-KONTROLA2-0316-0330.jsonl`.
- Zastosowano je do banku bez zmiany kluczy, `module_id`, `needs_review`, `checked_at=null`, `reviewer=null` i `image=null`.
- ADR-B-0319 pozostaje bez zmian.
- Oczekiwany i potwierdzony Git blob SHA banku: `57ec8c29983bc8e3ccd48354f9f5f16c93b51c9f`.
- Warianty i klucze egzaminów próbnych 001–005 wskazują ten SHA; ID 0316–0330 nie występują w tych wariantach.
- Wskaźnik „poprawna = jedyna najdłuższa”: **36/780 = 4,62%**; maksimum działu **7,87%**.
- Wszystkie 780 rekordów pozostają `needs_review`; 0 `verified`; brak formalnych zatwierdzeń.

**Licznik kontroli dosłownej:** przed partią 22 pozostawało 465 pytań; po porównaniu 15 pytań pozostaje **450 (ADR-B-0331–0780)**. Wartości 438/423 z wcześniejszego raportu były błędne.
