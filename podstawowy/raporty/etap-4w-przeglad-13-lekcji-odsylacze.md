# Etap 4w — kontrola jakości 13 lekcji i odnośników

Stan porównania: `main` 1051df7c0dfa2c7e3756f3f19f12ba1299690050, 569 pytań, 13 lekcji. Kontrola techniczna objęła końcową sekcję `Sprawdź się` wszystkich 13 lekcji i przyporządkowanie ich pełnych ID do modułów w `questions.jsonl`.

| Lekcja | Pełne ID w końcowym samosprawdzaniu | Nieistniejące ID | ID z obcego działu | Fragment praktyczny | Wynik |
|---|---:|---:|---:|---|---|
| ADR-B-01 | 8 | 0 | 0 | Tak | Zgodny technicznie |
| ADR-B-02 | 8 | 0 | 0 | Tak | Zgodny technicznie |
| ADR-B-03 | 8 | 0 | 0 | Tak | Zgodny technicznie |
| ADR-B-04 | 8 | 0 | 0 | Tak | Zgodny technicznie |
| ADR-B-05 | 8 | 0 | 0 | Tak | Zgodny technicznie |
| ADR-B-06 | 8 | 0 | 0 | Tak | Zgodny technicznie |
| ADR-B-07 | 8 | 0 | 0 | Tak | Zgodny technicznie |
| ADR-B-08 | 8 | 0 | 0 | Tak | Zgodny technicznie |
| ADR-B-09 | 8 | 0 | 0 | Tak | Zgodny technicznie |
| ADR-B-10 | 8 | 0 | 0 | Tak | Zgodny technicznie |
| ADR-B-11 | 8 | 0 | 0 | Tak | Zgodny technicznie |
| ADR-B-12 | 8 | 0 | 0 | Tak | Zgodny technicznie |
| ADR-B-13 | 8 | 0 | 0 | Tak | Zgodny technicznie |

## Potwierdzona usterka dydaktyczna

W `podstawowy/lekcje/ADR-B-09.md` karta powtórkowa kierowała kursanta do całego zakresu **ADR-B-0546–0560**, lecz 0546–0550 dotyczą oznakowania (B-06), a 0551–0553 wyposażenia (B-08). **Skorygowano główne skierowanie do ADR-B-0554–0560**, zachowując zrozumiałe wskazanie, gdzie znaleźć pozostałe pytania. Nie zmieniano kluczy ani wymagań prawnych.

## Granice oceny

- Potwierdzono obecność 13 lekcji i przykładu/scenariusza w każdej, oraz istnienie i przyporządkowanie końcowych 8 odsyłaczy z każdej lekcji. To 104 odwołania, nie niezależny audyt poprawności wszystkich ich odpowiedzi.
- Nie potwierdzono luki polegającej na braku kompetencji teoretycznej w programie: aktualna mapa zawiera 104 cele teoretyczne z pytaniami i 3 cele praktyczne z programem ćwiczeń.
- Wciąż otwarte: recenzja pedagogiczna całości akapitów i niezależne potwierdzenie podstaw prawnych przez specjalistę. Żadne pytanie nie otrzymało `verified`.
- Nie regenerowano egzaminu próbnego: nie zmieniono banku ani ID.
