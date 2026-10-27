# Etap 4x101 — zgodność mapy kompetencji i głębokości pokrycia

- Data: 2026-10-27.
- Punkt wejścia: świeży `main` po PR #558, commit `d56b39628484da5efbee626e88f419766f015a7b`.
- Zakres: spójność mapy kompetencji, programu kursu i raportu pokrycia; bez zmian w banku.

## Potwierdzona rozbieżność

`docs/PROGRAM-PODSTAWOWY.md` podawał 106 roboczych kompetencji, natomiast aktualna mapa `podstawowy/kompetencje.json` ma 107 pozycji. Poprawiono liczbę na 107. Nie jest to urzędowa liczba wymagań — pozostaje to autorski podział redakcyjny.

## Głębokość pokrycia

Sprawdzono bieżące 107 kompetencji:
- 104 teoretyczne i 3 praktyczne;
- wszystkie 104 cele teoretyczne mają co najmniej dwa pytania robocze;
- wszystkie 609 pytań jest przypisanych do co najmniej jednej kompetencji;
- brak nieistniejących ID i odwołań do pytań z innych modułów;
- wszystkie 609 pytań pozostają `needs_review`, 0 `verified`.

W `docs/POKRYCIE-KURSU.md` doprecyzowano, że 104/104 kompetencji teorii mają co najmniej dwa pytania robocze. Nie oznacza to, że kompetencje są zatwierdzone prawnie lub że dwa pytania wystarczają do pełnej nauki.

## Regresja

Dodano `tests/test_competency_depth_coverage.py`. Test sprawdza:
- zgodność liczby kompetencji w mapie i dokumencie programu;
- minimum dwa pytania dla każdego celu teoretycznego;
- istnienie i zgodność modułu każdego `question_id`;
- przypisanie wszystkich pytań do mapy;
- zgodność liczb kompetencji teoretycznych, praktycznych i pytań w tabeli `POKRYCIE-KURSU.md`.

## Bieżące metryki

- 609 pytań, 609 unikalnych ID, wszystkie `needs_review`.
- A=206, B=207, C=196.
- „Poprawna = jedyna najdłuższa”: 73/609 = 11,99%; maksimum działu 14,29%.
- Explanation minimum 300 znaków.
- 39 scenariuszy, 5 wariantów egzaminu i 5 kluczy.

Nie zmieniono pytań, poprawnych liter ani statusów prawnych. Kurs cysterny i inne specjalizacje nie były ruszane.
