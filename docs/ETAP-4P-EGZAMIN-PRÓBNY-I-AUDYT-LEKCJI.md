# Etap 4p — egzamin próbny i audyt jakości lekcji

Data: 24.10.2026. Punkt wyjścia `main`: `d8455fc96b6b3360ed0b66de01f61ee75eb89e82`. Zakres: ADR podstawowy; cysterny poza zakresem.

## Egzamin próbny

30 pytań, 60 minut, próg 20/30 (2/3). Dobór proporcjonalny do liczby pytań w 13 działach, minimum jedno pytanie na dział. Arkusz i klucz są osobnymi plikami. `scripts/draft_mock_exam.py` generuje kolejne warianty z banku; ten sam seed i bank dają powtarzalny zestaw. Wszystkie 566 rekordów są `needs_review`, 0 `verified`; to trening wewnętrzny, nie oficjalny arkusz. Bramka verified-only nie została osłabiona. Quality Gate sprawdza ID, unikalność i zgodność kolejności klucza.

## Wskaźnik długości odpowiedzi

Globalnie **90/566 = 15.90%** — próg 18% spełniony.

Powyżej 18% na poziomie działu:
- ADR-B-02: 12/56 (21.4%)
- ADR-B-03: 10/49 (20.4%)
- ADR-B-08: 8/40 (20.0%)
- ADR-B-09: 10/46 (21.7%)
- ADR-B-11: 9/35 (25.7%)
- ADR-B-13: 7/35 (20.0%)

Na poziomie 18% lub poniżej:
- ADR-B-01: 6/35 (17.1%)
- ADR-B-04: 5/44 (11.4%)
- ADR-B-05: 6/40 (15.0%)
- ADR-B-06: 4/45 (8.9%)
- ADR-B-07: 3/43 (7.0%)
- ADR-B-10: 4/55 (7.3%)
- ADR-B-12: 6/43 (14.0%)

Dalsze wyrównanie należy kierować najpierw do działów powyżej 18%, bez zmiany klucza ani sensu prawnego.

## Wstępny przegląd 13 lekcji

13/13 plików istnieje i zawiera kartę powtórkową po PR #257. Materiały mają cele, sekcje tematyczne, źródła i scenariusze, ale pozostają szkicami bez niezależnego odbioru. W sekcjach bazowych najmniej prostych przykładów kierowcy występuje w B-03, B-04, B-08, B-11 i B-12. Następna partia doda krótkie przykłady i jawne odsyłacze do pytań; nie będzie to zatwierdzenie prawne.

Pełne literalne porównanie z polskim tekstem ADR 2025 i sprostowaniem oraz niezależna recenzja A/B/C pozostają otwarte. Quiz nie zalicza praktyki P1–P3.

## Partia 2 — przegląd i dopracowanie 13 lekcji (24.10.2026)

- Wszystkie 13 lekcji otrzymało jawny wykaz ID pytań odpowiadających tematowi oraz prosty przykład z pracy kierowcy.
- Szczególnie doprecyzowano B-03 (rozlew i odpady), B-04 (zakaz palenia i postój z nadzorem), B-08 (liczba gaśnic vs. masa oraz świadectwo), B-11 (kod tunelowy i pożar) i B-12 (weryfikacja odbiorcy i tabela towarów dużego ryzyka), bo wcześniejsze sekcje bazowe miały niewiele praktycznych przykładów.
- Nie zmieniono banku pytań, kluczy ani statusów. Odsyłacze wskazują istniejące rekordy; wszystkie pozostają `needs_review`.
- To przegląd redakcyjny, nie prawny odbiór eksperta. Niezależny specjalista ADR musi jeszcze sprawdzić wyjątki, podstawy i wszystkie warianty A/B/C; instruktor powinien ocenić zrozumiałość w rzeczywistych zajęciach.
