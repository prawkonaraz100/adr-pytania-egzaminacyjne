# Etap 4x47 — kontrola 13 sygnałów heurystyki wyjaśnień

- Data: 26.10.2026.
- Punkt wyjścia: świeży `main` `a08f1d3eec702bec169cfaa7d9e5ec2a4df71506` po 4x46.
- Zakres: wyłącznie ADR podstawowy, bez formalnej recenzji prawnej.
- Źródło kandydatów: uruchomiony w CI `scripts/check_explanation_heuristics.py` po 4x46 (13 sygnałów doradczych).

## Ręczny odbiór redakcyjny sygnałów

| ID | Wynik | Dlaczego |
|---|---|---|
| ADR-B-0067 | Bez zmiany | Objaśnia dokument ze zdjęciem oraz dlaczego cudzy dokument i list przewozowy nie wystarczą. |
| ADR-B-0086 | Bez zmiany | Wyjaśnia regułę najsurowszego kodu i rozdziela kolejność wpisu od masy towaru. |
| ADR-B-0120 | Bez zmiany | Łączy weryfikację tożsamości z ochroną ładunku i objaśnia mylące dane kontaktowe. |
| ADR-B-0136 | Bez zmiany | Zrozumiale objaśnia zakaz zabierania osoby spoza załogi oraz obie błędne przesłanki. |
| ADR-B-0147 | Bez zmiany | Wyjaśnia pojęcie jednostki transportowej złożonej z ciągnika i naczepy. |
| ADR-B-0186 | Bez zmiany | Łączy ostrzeżenie postronnych z zagrożeniem i wskazuje, dlaczego proszenie o przenoszenie ładunku jest złe. |
| ADR-B-0349 | Bez zmiany | Wyjaśnia sens odosobnionego postoju oraz dlaczego plac przy drodze i przystanek są niewłaściwe. |
| ADR-B-0357 | Bez zmiany | Prosto mówi o zakazie otwierania opakowania; obala rękawice i upływ czasu jako rzekome wyjątki. |
| ADR-B-0402 | Bez zmiany | Wskazuje cel planu ochrony i omawia, czemu model pojazdu lub stała pora posiłku nie zastąpią działań. |
| **ADR-B-0403** | **Przepisano** | Explanation mówiło o harmonogramie przerw, którego nie ma w A/B/C; obecnie odróżnia reklamację i odszkodowanie od zgłaszania naruszeń ochrony. |
| ADR-B-0529 | Bez zmiany | Pokazuje, czemu szkolenie zagrożeń nie jest szkoleniem z grafiku czy księgowości. |
| ADR-B-0534 | Bez zmiany | Rozwija LQ i opisuje wymagane oznakowanie zbiorcze zamiast samego listu przewozowego. |
| ADR-B-0573 | Bez zmiany | Wyjaśnia obowiązek wpisu i liczby sztuk przy EQ, odróżniając je od podpisu i małego opakowania. |

Sygnały przy 12 pozostawionych pytaniach uznano za **fałszywe alarmy heurystyki redakcyjnej**. Nie jest to akceptacja prawna pytań i nie rozstrzyga odstępstw w oficjalnym ADR.

## Zmiana i weryfikacja

- ADR-B-0403: explanation liczy 327 znaków, ma cztery zdania, odnosi się do poprawnej odpowiedzi C oraz obu błędnych odpowiedzi A i B.
- Zachowano ID, klucz C, tekst odpowiedzi, dział, podstawę ADR 1.10.3.2.2(e) i `needs_review`.
- Zsynchronizowano snapshot audytu sekwencyjnego i A/B/C w `399-416.json`, SHA pięciu wariantów i pięciu kluczy (bez zmiany ich permutacji), manifest, kolejki i bieżące instrukcje recenzenta.
- Bank nadal liczy 609 pytań: 609 `needs_review`, 0 `verified`, minimum explanation 300 znaków; „poprawna = jedyna najdłuższa” 72/609 = 11,82%, maksimum modułu 14,29%.
- Formalna publikacja i niezależna recenzja prawna pozostają zablokowane.

## Następna luka jakości

Warto kontynuować przegląd pozostałych wyjaśnień pod kątem zdań o nieistniejących dystraktorach, a nie polegać wyłącznie na słowach kluczowych heurystyki. Nie należy zgadywać poprawności prawnej bez urzędowego tekstu ADR i sprostowania.
