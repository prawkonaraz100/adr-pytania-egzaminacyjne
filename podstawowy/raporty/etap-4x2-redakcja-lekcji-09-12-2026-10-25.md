# Etap 4x2 — redakcja podręcznikowa lekcji ADR-B-09–12

- Data: 25.10.2026.
- Punkt wyjścia: `main` po PR #306, commit `119e27c8aff8cc67d8e27a1849b059a1335378d7`.
- Zakres: wyłącznie kurs podstawowy ADR.

## Co zredagowano

- **B-09 — Załadunek, mocowanie i przewóz luzem:** połączono kontrolę przed załadunkiem, wspólny załadunek, ochronę żywności, mocowanie bez uszkadzania opakowań, pozostałości po rozładunku i dopuszczalność przewozu luzem.
- **B-10 — Transport kombinowany:** uporządkowano różnice ADR/RID/IMDG, dokumenty po odcinku morskim, warunki ADR 1.1.4.2, dodatkowe wpisy i certyfikat pakowania kontenera/pojazdu.
- **B-11 — Tunele:** zebrano kategorie A–E, kolumnę 15 tabeli A, regułę kodu D/E, łączenie kodów w jednej jednostce, wybór trasy i reakcję na zdarzenie w tunelu.
- **B-12 — Ochrona przewozu:** rozdzielono security od mocowania, zebrano plan ochrony, kontrolę uprawnienia odbiorcy, poufność informacji i postój.

Z tekstu kursanta usunięto nagłówki etapowe, daty, etykiety szkicu i powtarzające się instrukcje redakcyjne. Przykłady z kart kursanta i map pytań połączono z odpowiednimi rozdziałami i scenariuszami.

## Materiały instruktorskie

Plany zajęć, zadania instruktorskie i kryteria obserwacji przeniesiono do:
- `podstawowy/instruktor/ADR-B-09.md`
- `podstawowy/instruktor/ADR-B-10.md`
- `podstawowy/instruktor/ADR-B-11.md`
- `podstawowy/instruktor/ADR-B-12.md`

Nie dodano fikcyjnych dat, ocen ani podpisów.

## Zachowanie treści i odwołań

Zachowano przykłady dotyczące pozostałości po ładunku, zbyt mocno zaciągniętego pasa, mocowania ciężkiej maszyny, certyfikatu pakowania, odcinka drogowego po morskim, kodu tunelowego D/E, zdarzenia w tunelu, ochrony postoju i weryfikacji odbiorcy. Nie zmieniano banku ani kluczy.

W starym B-09 pojawiały się odwołania ADR-B-0546 i ADR-B-0551 z innych działów. Nowa lekcja odwołuje się wyłącznie do pytań modułu B-09; nie usuwano pytań z banku.

## Preflight Quality Gate

- Bank: 609 pytań; duplikaty ID: 0.
- Poprawna odpowiedź jest jedyną najdłuższą: 86/609 = 14.12% (limit 18%).
- Najkrótsze explanation: 300 znaków; poniżej 200 znaków: 0.
- Status: 609 `needs_review`, 0 `verified`.
- Referencje:
  - B-09: 46 unikalnych ID; brakujące 0; inne działy 0.
  - B-10: 55 unikalnych ID; brakujące 0; inne działy 0.
  - B-11: 43 unikalnych ID; brakujące 0; inne działy 0.
  - B-12: 44 unikalnych ID; brakujące 0; inne działy 0.

## Ograniczenia

Redakcja nie stanowi niezależnej recenzji polskiego tekstu ADR. Wszystkie pytania zachowują `needs_review`; nie stwierdzono potwierdzonego błędu wymagającego zmiany klucza. Nie rozpoczęto kursu cystern ani innej specjalizacji.
