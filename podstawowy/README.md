# ADR podstawowy — kurs i bank pytań

**Stan na 24.10.2026, main `1d2e5ae`: 566 pytań roboczych; 566 `needs_review`, 0 `verified`.** Materiał jest autorskim narzędziem szkoleniowym, nie oficjalnym katalogiem egzaminacyjnym. Nie publikować ani nie traktować pytań jako zatwierdzonych bez niezależnej kontroli specjalisty ADR.

## Jak korzystać z kursu

1. Zacznij od właściwej lekcji z tabeli poniżej. Czytaj część wprowadzającą, przykład z pracy kierowcy i pytania powtórkowe.
2. Rozwiąż pytania wskazane w lekcji, a następnie użyj pełnego banku `questions.jsonl` do dalszej nauki.
3. Przy każdym pytaniu przeczytaj wyjaśnienie i sprawdź wskazany punkt ADR. Jeśli widzisz sprzeczność, nie zgaduj — oznacz ją do przeglądu.
4. Scenariusze praktyczne P1–P3 są materiałem dla instruktora. Nie zastępują rzeczywistych zajęć ani oceny instruktora.

| Kolejność | Lekcja | Temat | Plik |
|---:|---|---|---|
| 1 | ADR-B-01 | Podstawy ADR i wyłączenia | [Otwórz lekcję](lekcje/ADR-B-01.md) |
| 2 | ADR-B-02 | Klasyfikacja i rodzaje zagrożeń | [Otwórz lekcję](lekcje/ADR-B-02.md) |
| 3 | ADR-B-03 | Środowisko i odpady | [Otwórz lekcję](lekcje/ADR-B-03.md) |
| 4 | ADR-B-04 | Zapobieganie zagrożeniom | [Otwórz lekcję](lekcje/ADR-B-04.md) |
| 5 | ADR-B-05 | Awaria i pierwsza pomoc | [Otwórz lekcję](lekcje/ADR-B-05.md) |
| 6 | ADR-B-06 | Oznakowanie i tablice | [Otwórz lekcję](lekcje/ADR-B-06.md) |
| 7 | ADR-B-07 | Obowiązki uczestników | [Otwórz lekcję](lekcje/ADR-B-07.md) |
| 8 | ADR-B-08 | Pojazdy i wyposażenie | [Otwórz lekcję](lekcje/ADR-B-08.md) |
| 9 | ADR-B-09 | Załadunek, pakowanie i mocowanie | [Otwórz lekcję](lekcje/ADR-B-09.md) |
| 10 | ADR-B-10 | Transport kombinowany | [Otwórz lekcję](lekcje/ADR-B-10.md) |
| 11 | ADR-B-11 | Tunele i ograniczenia trasy | [Otwórz lekcję](lekcje/ADR-B-11.md) |
| 12 | ADR-B-12 | Ochrona przewozu | [Otwórz lekcję](lekcje/ADR-B-12.md) |
| 13 | ADR-B-13 | Dokumentacja transportowa | [Otwórz lekcję](lekcje/ADR-B-13.md) |

## Egzamin próbny — tylko do treningu wewnętrznego

- [Wariant 001 — arkusz pytań](egzamin-probny/wariant-001.json)
- [Wariant 001 — klucz i wyjaśnienia](egzamin-probny/klucz-001.json)
- [Instrukcja generowania kolejnych wariantów](egzamin-probny/README.md)
- Format treningowy: 30 pytań, 60 minut, próg 20/30 (2/3). Generator dobiera pytania proporcjonalnie z 13 działów.
- **Zastrzeżenie:** wszystkie pytania pozostają `needs_review`, więc egzamin nie jest zatwierdzonym testem do formalnej oceny ani oficjalnym arkuszem.

## Raporty i materiały

- [Raport etapu 4q — przegląd oczami kursanta](raporty/etap-4q-przeglad-kursanta-2026-10-24.md)
- [Kompetencje i cele](kompetencje.json)
- [Analiza luk i matryca pokrycia](../docs/POKRYCIE-KURSU.md)
- [Program kursu podstawowego](../docs/PROGRAM-PODSTAWOWY.md)
- [Scenariusze praktyczne dla instruktora](praktyka/SCENARIUSZE.md)
- [Dokładna mapa punktów ADR 2025](../docs/MAPA-PUNKTOW-ADR-2025.md)
- [Standard redakcyjny pytań](../docs/STANDARD-PYTAN.md)
- [Rejestr źródeł](../docs/ZRODLA.md)
- [Dziennik projektu](../docs/STATUS.md) i [Issue #10](https://github.com/prawkonaraz100/adr-pytania-egzaminacyjne/issues/10)

## Aktualne kontrole jakości

```bash
python scripts/validate.py
python scripts/coverage.py
python scripts/answer_length_bias.py --threshold 0.18 --strict-global
python scripts/check_explanation_quality.py --minimum 300
python -m unittest discover -s tests -v
```

Globalny wskaźnik „poprawna odpowiedź jest jedyną najdłuższą”: **71/566 = 12,54%**, próg Quality Gate: 18%. Wewnętrzna mapa 103 kompetencji teoretycznych ma pytania robocze, ale to nie dowodzi poprawności prawnej ani wystarczającej głębokości nauczania.

## Status weryfikacji

- Bank: 566 `needs_review`, 0 `verified`.
- Lekcje: 13 szkiców z mapą pytań i przykładami; wymagają niezależnego odbioru dydaktycznego i prawnego.
- Praktyka: 3 scenariusze do przeprowadzenia i udokumentowania przez instruktora; repozytorium nie poświadcza, że ćwiczenia odbyły się.
- Prawo: pełne porównanie każdego punktu z polskim tekstem urzędowym i sprostowaniem oraz niezależna recenzja specjalisty pozostają otwarte.

**Nie przechodź do kursu cystern ani innych specjalizacji przed zamknięciem kursu podstawowego i niezależną weryfikacją.**
