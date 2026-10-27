# Etap 4x102 — audyt różnorodności pytań kompetencji i synchronizacja migawki

- Data: 2026-10-27.
- Punkt wejścia: świeży `main` `b986648c4aedf3a8751a27569249fc8e0b0e2968`, po PASS Quality Gate PR #559.
- Zakres: sprawdzenie par pytań przypisanych do tej samej kompetencji, które heurystyka podobieństwa uznała za kandydatów do ręcznego przeglądu, oraz synchronizacja nagłówka raportu pokrycia.

## Wynik kontroli podobieństwa

Przesiano pary pytań przypisane do tej samej kompetencji, porównując tokeny w treści pytania. To heurystyka redakcyjna, nie dowód duplikatu ani weryfikacja prawna. Przy progu Jaccarda 0,55 znaleziono dwie pary; obie przejrzano ręcznie.

| Pytania | Kompetencja | Ocena | Uzasadnienie |
|---|---|---|---|
| ADR-B-0071 / ADR-B-0072 | ADR-B-08-K01 | Fałszywy alarm — zachować | Pytania porównują dwa różne progi DMC: 3,5 t i 6 t. Oczekiwane wartości gaśnic są różne (4 kg i 8 kg), więc druga sytuacja sprawdza zastosowanie tabeli ADR 8.1.4.1 w innym przedziale, a nie powtarza tę samą odpowiedź. |
| ADR-B-0330 / ADR-B-0337 | ADR-B-03-K06 | Fałszywy alarm — zachować | Pytania sprawdzają odrębne wyłączenia uproszczonej procedury klasyfikacji odpadów o nieznanym składzie: klasa 5.2 oraz klasa 6.2. To podobny schemat dydaktyczny, ale inne fakty do rozpoznania. Podstawa wskazana w rekordach: ADR 2.1.3.5.3 i 2.1.3.5.5. |

Nie znaleziono na tej próbie potwierdzonego duplikatu, który uzasadniałby zmianę pytania. Bank, poprawne litery, explanation i ID nie zostały zmienione.

## Potwierdzona rozbieżność dokumentacyjna

`docs/POKRYCIE-KURSU.md` nadal wskazywał etap 4x100, mimo że README kursanta, indeks recenzyjny i raport 4x101 opisywały nowszy stan. Nagłówek zmieniono na etap 4x102, a `tests/test_coverage_report_metrics.py` aktualizuje asercję, żeby przyszła zmiana migawki wymagała świadomej aktualizacji testu.

## Stan banku

- 609 pytań, wszystkie `needs_review`, 0 `verified`.
- Rozkład poprawnych liter: A=206, B=207, C=196.
- „Poprawna = jedyna najdłuższa”: 73/609 = 11,99%; maksimum działu 14,29%.
- Explanation minimum 300 znaków.
- Nie zmieniono żadnego klucza egzaminu ani treści pytania.

## Testy i ograniczenia

Testy zostaną potwierdzone przez GitHub Actions na końcowym SHA PR. Nie ma lokalnego checkoutu repo w tej sesji. Heurystyka tokenowa nie wykrywa wszystkich parafraz i nie zastępuje ręcznego przeglądu ani niezależnej kontroli ADR. Wszystkie pytania pozostają `needs_review`.
