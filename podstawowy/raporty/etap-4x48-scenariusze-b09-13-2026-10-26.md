# Etap 4x48 — scenariusze praktyczne B-09–13

- Data: 2026-10-26.
- Punkt bazowy: świeży `main` `420892b31cb73dfb4834ce9d71ced15d6ed178ec` (po PR #492).
- Zakres: wyłącznie kurs podstawowy ADR.

## Co sprawdzono i poprawiono

Przejrzano trzy scenariusze w każdym z działów B-09–13. Scenariusze już zawierały sytuację, kroki kierowcy, typowe błędy, kryteria oceny, podstawę ADR i krótkie podsumowanie. Potwierdzoną wadą były długie listy `question_ids`, w tym do 11 pytań w scenariuszu tunelowym i do 15 w scenariuszu dokumentacyjnym. Zawężono je do 1–3 pytań, które bezpośrednio sprawdzają decyzję opisaną w scenariuszu.

| Scenariusz | Pytania po zmianie | Główna kompetencja |
|---|---|---|
| SC-ADR-B-09 | ADR-B-0518, ADR-B-0554, ADR-B-0558 | kontrola przestrzeni, mocowanie i przewóz luzem |
| SC-ADR-B-10 | ADR-B-0396, ADR-B-0511 | warunki przewozu po odcinku morskim |
| SC-ADR-B-11 | ADR-B-0539, ADR-B-0592, ADR-B-0591 | kody tunelowe i zdarzenie w tunelu |
| SC-ADR-B-12 | ADR-B-0120, ADR-B-0304, ADR-B-0582 | plan ochrony, odbiorca i postój |
| SC-ADR-B-13 | ADR-B-0508, ADR-B-0589, ADR-B-0601 | dokument, instrukcje i odcinek morski |
| SC-ADR-B-09-02 | ADR-B-0554, ADR-B-0026, ADR-B-0518 | pozostałości przed załadunkiem |
| SC-ADR-B-09-03 | ADR-B-0026, ADR-B-0518, ADR-B-0558 | mocowanie i zabezpieczenie ładunku |
| SC-ADR-B-10-02 | ADR-B-0028, ADR-B-0030, ADR-B-0511 | sprawdzenie dokumentów na odcinek drogowy |
| SC-ADR-B-10-03 | ADR-B-0204, ADR-B-0030 | zgodność certyfikatu pakowania |
| SC-ADR-B-11-02 | ADR-B-0487, ADR-B-0591, ADR-B-0602 | zakaz tunelowy i wybór objazdu |
| SC-ADR-B-11-03 | ADR-B-0574, ADR-B-0539, ADR-B-0604 | połączenie kodów w jednym ładunku |
| SC-ADR-B-12-02 | ADR-B-0304, ADR-B-0582, ADR-B-0519 | zmiana miejsca postoju |
| SC-ADR-B-12-03 | ADR-B-0120, ADR-B-0304 | weryfikacja odbiorcy |
| SC-ADR-B-13-02 | ADR-B-0578, ADR-B-0579, ADR-B-0600 | brakujące dane dokumentu |
| SC-ADR-B-13-03 | ADR-B-0587, ADR-B-0589, ADR-B-0590 | zrozumiałe i dostępne instrukcje |

## Kontrola referencji

- Scenariusze zmienione: 15/15.
- Pytania na scenariusz: minimum 2, maksimum 3.
- Nieistniejące ID: 0.
- Pytania z niewłaściwego modułu: 0.
- Bank: 609 pytań; wszystkie `needs_review`, 0 `verified`.

## Ograniczenia

Nie zmieniono treści pytań, poprawnych liter, explanation ani statusów prawnych. Nie dopisywano nowych pytań, ponieważ w tym przeglądzie nie potwierdzono nowej luki programu wymagającej nowego rekordu. Lokalnych testów repozytorium nie da się uruchomić przez GitHub Contents API; wymagany jest pełny Quality Gate CI.
