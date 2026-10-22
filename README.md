# ADR — pytania egzaminacyjne i szkoleniowe

Otwarty projekt autorskiej bazy pytań do nauki na **polski egzamin ADR dla kierowców**.

## Zakres

1. **ADR podstawowy (początkowy) — aktywny etap.**
2. **ADR specjalistyczny: cysterny — etap kolejny**, po zakończeniu i zatwierdzeniu podstawowego.
3. Inne specjalizacje poza bieżącym zakresem.

## Stan na 22.10.2026

- [x] Utworzono repozytorium i zapisano założenia.
- [x] Zidentyfikowano oficjalny program kursu: 13 tematów / 18 godzin lekcyjnych teorii plus ćwiczenia praktyczne.
- [x] Zidentyfikowano zasady państwowego egzaminu podstawowego: 30 pytań, 60 minut, próg 20 poprawnych odpowiedzi.
- [x] Wstępna mapa punktów ADR 2025 dla 13 tematów (do kontroli pełnego tekstu).
- [ ] Kompletny przegląd punktów ADR 2025 oraz aktów krajowych dla 13 tematów.
- [x] Pierwsza partia 39 pytań autorskich w statusie needs_review (3 na każdy z 13 działów).
- [ ] Autorska baza pytań po weryfikacji merytorycznej.
- [ ] Egzaminy próbne, ilustracje i pełny Quality Gate.
- [ ] Kurs specjalistyczny „cysterny”.

**Uwaga:** obecnie w banku jest 39 pytań w statusie needs_review i 0 pytań zatwierdzonych. Nie przedstawiamy pytań autorskich ani z komercyjnych testów jako oficjalnych pytań egzaminacyjnych. Publicznego kompletnego katalogu pytań państwowych nie potwierdzono.

## Jak pracujemy

- Opracowujemy własne pytania: dokładnie 3 odpowiedzi, jedna poprawna, prosty komentarz dla kierowcy.
- Każde pytanie wskazuje precyzyjne źródło: wydanie przepisów i konkretny punkt/artykuł.
- Wynik kontroli ma jednoznaczny status: draft, needs_review, verified albo blocked.
- W teście produkcyjnym używamy wyłącznie pytań verified i tylko z aktualną weryfikacją.
- Źródła zewnętrzne i testy szkoleniowe służą identyfikacji tematów i luk, nie do bezpośredniego kopiowania cudzych pytań, grafik ani objaśnień.
- Zmiany przepisów uruchamiają ponowną weryfikację powiązanych pytań.

## Dokumentacja

- [Plan i kryteria ukończenia](docs/PLAN.md)
- [Mapa punktów ADR 2025 do weryfikacji — 13 działów](docs/MAPA-PUNKTOW-ADR-2025.md)
- [Urzędowy program kursu](docs/PROGRAM-PODSTAWOWY.md)
- [Źródła prawne i zasady ich weryfikacji](docs/ZRODLA.md)
- [Standard pytań i publikacji](docs/STANDARD-PYTAN.md)
- [Stan prac i rejestr decyzji](docs/STATUS.md)

## Dane i narzędzia

- Dane: `podstawowy/questions.jsonl` (jeden obiekt JSON na linię).
- Schemat: `schema/question.schema.json`.
- Walidator: `python scripts/validate.py`.
- Testy walidatora: `python -m unittest discover -s tests -v`.
- Automatyczna kontrola w GitHub Actions: `.github/workflows/quality.yml`.

## Źródła podstawowe

- [Ministerstwo Infrastruktury — towary niebezpieczne i ADR 2025](https://www.gov.pl/web/infrastruktura/towary-niebezpieczne)
- [Rozporządzenie o prowadzeniu kursów, załącznik nr 1 (Dz.U. 2021 poz. 2150)](https://eli.gov.pl/api/acts/DU/2021/2150/text.pdf)
- [Rozporządzenie o egzaminach (Dz.U. 2024 poz. 964)](https://eli.gov.pl/api/acts/DU/2024/964/text.html)

**Charakter projektu:** nieoficjalna platforma edukacyjna, niezwiązana z komisją egzaminacyjną ani organem administracji.
