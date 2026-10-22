# ADR podstawowy — baza autorskich pytań

Stan na 22.10.2026: **146 rekordów** w pliku `questions.jsonl`, w tym partie 001 (39), 002 (31), 003 (20), 004 (32), 005 (24). Wszystkie **146 `needs_review` / 0 `verified`**. Nie publikować ich jako gotowych pytań bez niezależnej kontroli merytorycznej.

### Co już wykonano

- Przygotowano pytania z odpowiedziami A/B/C, objaśnieniami i punktem odniesienia ADR 2025.
- Wszystkie 13 modułów mają wstępne pokrycie (po 8–15 pytań). W matrycy 106 kompetencji 103/103 celów teorii mają co najmniej jeden szkic pytania; to nie oznacza eksperckiego zatwierdzenia ani wystarczającej liczby przykładów na cel.
- Ukończono redakcyjną kontrolę źródeł pierwszych 39 pytań i zapisano osobny audyt. To **nie** podpis specjalisty ADR.
- [Quality Gate na PR #5](https://github.com/prawkonaraz100/adr-pytania-egzaminacyjne/actions/runs/39832204845): PASS (składnia schematu, testy Python, struktura banku). Status checka dla najnowszego HEAD main wymaga osobnego potwierdzenia.

### Powiązane dokumenty

- [Program kursu](../docs/PROGRAM-PODSTAWOWY.md)
- [Kompetencje i cele](kompetencje.json)
- [Analiza luk i matryca pokrycia](../docs/POKRYCIE-KURSU.md)
- [Lekcje robocze](lekcje/) — 13 szkiców
- [Scenariusze praktyczne dla instruktora](praktyka/SCENARIUSZE.md)
- [Audyt partii 005](../docs/AUDYT-PARTIA-005.md)
- [Dokładna mapa zakresu ADR](../docs/MAPA-PUNKTOW-ADR-2025.md)
- [Audyt 39 + lista kontroli 31](../docs/AUDYT-MERYTORYCZNY-PARTIA-001.md)
- [Standard pytań](../docs/STANDARD-PYTAN.md)
- [Rejestr źródeł](../docs/ZRODLA.md)
- [Dziennik projektu](../docs/STATUS.md)

### Kontrola

```bash
python scripts/validate.py
python scripts/coverage.py
python -m unittest discover -s tests -v
```

Tryb egzaminu 30 pytań / 60 minut / próg 20 poprawnych jest celem produktu. Nie uruchamiać go produkcyjnie na niezatwierdzonych rekordach. To nieoficjalne materiały szkoleniowe, nie państwowy katalog pytań.
