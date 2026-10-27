# Etap 4x69 — kontrola scenariuszy i lekcji B-09–13

- Punkt bazowy: świeży `main` `de4c2a640ae791bb1bbb2367588e44df60b7563e` (po PR #525).
- Zakres: wyłącznie kurs podstawowy ADR.
- Sprawdzono 235 pytań B-09–13 oraz 15 scenariuszy tych działów.

## Mapa scenariusz → pytania

| Scenariusz | Pytania | Wynik |
|---|---|---|
| `SC-ADR-B-09` — Kontrola przed załadunkiem i mocowania | `ADR-B-0518`, `ADR-B-0554`, `ADR-B-0558` | PASS — istnieją i są z właściwego działu |
| `SC-ADR-B-10` — Kontener po rejsie morskim — dalszy odcinek drogowy | `ADR-B-0396`, `ADR-B-0511` | PASS — istnieją i są z właściwego działu |
| `SC-ADR-B-11` — Planowanie trasy i ograniczenia tunelowe | `ADR-B-0539`, `ADR-B-0592`, `ADR-B-0591` | PASS — istnieją i są z właściwego działu |
| `SC-ADR-B-12` — Ochrona przewozu i weryfikacja uprawnienia do odbioru | `ADR-B-0120`, `ADR-B-0304`, `ADR-B-0582` | PASS — istnieją i są z właściwego działu |
| `SC-ADR-B-13` — Kontrola dokumentów i instrukcji przed wyjazdem | `ADR-B-0508`, `ADR-B-0589`, `ADR-B-0601` | PASS — istnieją i są z właściwego działu |
| `SC-ADR-B-09-02` — Oględziny przed załadunkiem | `ADR-B-0554`, `ADR-B-0080` | PASS — istnieją i są z właściwego działu |
| `SC-ADR-B-09-03` — Mocowanie przed dłuższą trasą | `ADR-B-0026`, `ADR-B-0518`, `ADR-B-0235` | PASS — istnieją i są z właściwego działu |
| `SC-ADR-B-10-02` — Dokumenty po rejsie morskim | `ADR-B-0028`, `ADR-B-0030`, `ADR-B-0511` | PASS — istnieją i są z właściwego działu |
| `SC-ADR-B-10-03` — Niezgodność certyfikatu pakowania | `ADR-B-0204`, `ADR-B-0030` | PASS — istnieją i są z właściwego działu |
| `SC-ADR-B-11-02` — Objazd tunelu z ograniczeniem | `ADR-B-0487`, `ADR-B-0591`, `ADR-B-0602` | PASS — istnieją i są z właściwego działu |
| `SC-ADR-B-11-03` — Różne kody tunelowe w jednym ładunku | `ADR-B-0574`, `ADR-B-0539`, `ADR-B-0604` | PASS — istnieją i są z właściwego działu |
| `SC-ADR-B-12-02` — Zmiana planowanego postoju | `ADR-B-0304`, `ADR-B-0582`, `ADR-B-0407` | PASS — istnieją i są z właściwego działu |
| `SC-ADR-B-12-03` — Niezweryfikowany przewoźnik przy odbiorze ładunku | `ADR-B-0120`, `ADR-B-0211`, `ADR-B-0414` | PASS — istnieją i są z właściwego działu |
| `SC-ADR-B-13-02` — Brak danych w dokumencie przewozowym | `ADR-B-0578`, `ADR-B-0579`, `ADR-B-0600` | PASS — istnieją i są z właściwego działu |
| `SC-ADR-B-13-03` — Instrukcje pisemne w nieznanym języku | `ADR-B-0587`, `ADR-B-0589`, `ADR-B-0590` | PASS — istnieją i są z właściwego działu |

Każda z lekcji B-09–13 zawiera odwołania do wszystkich trzech scenariuszy swojego działu i ma listę pytań z banku. W 5 sprawdzonych lekcjach nie znaleziono brakujących ID ani odwołań do innych modułów. Scenariusze mają opis sytuacji, kroki, podstawę ADR, pytania, typowe błędy, kryteria oceny i granice bezpieczeństwa.

## Przegląd lekcji B-09–13

- **B-09:** kontrola przed załadunkiem, zgodność wspólnego załadunku, mocowanie, pozostałości i przewóz luzem. Nie znaleziono potwierdzonej sprzeczności z bankiem.
- **B-10:** rozróżnienie ADR/RID/IMDG, dokumentacja przewozu kombinowanego i warunki wyjątku. Nie znaleziono potwierdzonej sprzeczności wymagającej zmiany klucza.
- **B-11:** kody tunelowe i planowanie trasy. Przepisano explanation `ADR-B-0031`, ponieważ dwa zdania powtarzały tę samą myśl. Nowa wersja wyjaśnia, co oznacza kategoria A, czemu opcje o zakazie dla wszystkich pojazdów i o klasie 3 są błędne oraz że pozostałe znaki nadal obowiązują. Poprawna litera B i podstawa ADR bez zmian.
- **B-12:** ochrona przewozu, weryfikacja uprawnień i poufność danych. Nie znaleziono potwierdzonej sprzeczności w przeglądzie redakcyjnym.
- **B-13:** dokument przewozowy, dokumenty załogi i instrukcje pisemne. Nie znaleziono potwierdzonej sprzeczności w przeglądzie redakcyjnym.

## Metryki banku

- 609 pytań, 609 `needs_review`, 0 `verified`.
- Wskaźnik „poprawna = jedyna najdłuższa”: 72/609 = 11,82% globalnie.
- B-09: 4/46 = 8,70%; B-10: 4/55 = 7,27%; B-11: 6/43 = 13,95%; B-12: 6/44 = 13,64%; B-13: 5/47 = 10,64%.
- Explanation minimum 300 znaków; 0 poniżej 200.
- Nie zmieniano ID, poprawnej litery, `module_id` ani statusów prawnych.

## Ograniczenia

Kontrola dydaktyczna i spójności nie stanowi niezależnego zatwierdzenia prawnego tekstu ADR. Wszystkie pytania pozostają `needs_review`.
