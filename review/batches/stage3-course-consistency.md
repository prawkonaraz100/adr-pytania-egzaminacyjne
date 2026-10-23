# Etap 3 — końcowy audyt spójności kursu podstawowego ADR

Data: 23.10.2026. Zakres: wersja `main` po PR #137 (pakiet recenzyjny) i #138 (zabezpieczony egzamin próbny). **To audyt integralności, nie podpis specjalisty ani prawne zatwierdzenie pytań.**

## Wynik przeglądu danych

| Weryfikacja | Wynik |
|---|---|
| Pytania w `podstawowy/questions.jsonl` | **506**, ID `ADR-B-0001..0506` |
| Brak powielonych ID | **TAK** |
| Statusy | **506 needs_review, 0 verified** |
| Materiały 13 lekcji | **13/13 obecne i rozwinięte** |
| Godziny teorii z tabeli programu | **18 godzin lekcyjnych (45 min)** |
| Cele w wewnętrznej matrycy | **106** (103 teoria + 3 praktyka) |
| Cele teorii bez przypisanego pytania | **0** |
| Minimalna liczba pytań na cel teoretyczny | **3** |
| Cele praktyczne | **3**, ćwiczenia P1/P2/P3 nie mogą być zaliczane quizem |
| Indeks recenzencki | **506/506** numerów ID i podstawy prawne |
| Wpisy w `review/approvals.jsonl` | **0** |
| Egzamin próbny z realnego banku | **BLOCKED** przez `release_gate` |
| Otwarte PR-y przed tą partią | **0** |

Źródła normatywne: zał. 1 rozporządzenia w Dz.U. 2021 poz. 2150; ADR 2025 ogłoszone w Dz.U. 2025 poz. 642 i sprostowanie poz. 1575. Powołanie aktu **nie jest jeszcze dowodem dosłownego porównania 506 rekordów**.

## Utworzony automatyczny audyt regresji

`scripts/course_consistency.py` sprawdza ciągłość i jednoznaczność ID, mapę 13 modułów i 106 kompetencji, obecność wszystkich 13 lekcji oraz scenariuszy P1/P2/P3, zgodność indeksu dla recenzenta z aktualną liczbą pytań i istnienie generatora egzaminu z bramką. Daje ostrzeżenie o niezakończonym eksperckim zatwierdzeniu, lecz nie udaje, że to błąd techniczny struktury. `tests/test_course_consistency.py` sprawdza poprawny projekt i odrzucenie pustego katalogu.

## Co nadal blokuje rzeczywistą publikację

1. Brak 506 rzeczywistych, niezależnych kontroli prawa polskiego, wyjątków i wszystkich opcji A/B/C.
2. Brak jakiejkolwiek zaakceptowanej merytorycznie pozycji `verified` z prawdziwym podpisem/raportem; wszelkie approvals pozostają puste.
3. Niezależne potwierdzenie zgodności materiałów lekcji z programem oraz rzeczywiste przeprowadzenie i odnotowanie ćwiczeń P1–P3.
4. Ponowne sprawdzenie podobieństw semantycznych, jakości grafik, wzorów dokumentów i kompletności zmian prawa.
5. Dopiero po spełnieniu warunków `review/README.md`: ponowny release gate, wersjonowanie konkretnego HEAD, oddzielny audyt bezpieczeństwa wdrożenia i klucza odpowiedzi.

**Wniosek:** struktura kursu jest kompletna redakcyjnie i nadaje się do przekazania specjaliście, ale kurs oraz egzamin próbny **nie są dopuszczone do publicznego użycia**. Nie rozpoczęto kursu cystern ani innych specjalizacji; nie zmieniono statusów pytań.
