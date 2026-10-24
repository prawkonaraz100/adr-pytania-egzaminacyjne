# Quality Gate — globalny próg długości odpowiedzi i wyjaśnienia ≥200 znaków

24.10.2026. Po osiągnięciu wskaźnika „poprawna odpowiedź jest najdłuższa” na poziomie 212/545 (38,9% z porównania długości odpowiedzi) sprawdzono dokładną metrykę CI: jednoznacznie najdłuższa poprawna odpowiedź to 191/545 (35,0%); 21 remisów nie jest liczonych jako „ściśle najdłuższa”.

Zmiany:
- Workflow CI uruchamia `answer_length_bias.py --threshold 0.40 --strict-global`; przekroczenie 40% globalnie blokuje CI. Wskaźniki per moduł nadal są raportowane ostrzegawczo, ponieważ celem tej zmiany jest próg globalny.
- `scripts/validate.py` wymaga teraz co najmniej 200 znaków w `explanation`.
- `schema/question.schema.json` deklaruje tę samą granicę `minLength: 200`.
- Dodano testy dla trybu `--strict-global` i odrzucania zbyt krótkiego wyjaśnienia; dostosowano testowy rekord do nowej granicy.
- Aktualny bank ma 545 pytań; najkrótsze wyjaśnienie ma 248 znaków, więc nie wymaga masowej redakcji w ramach tej zmiany.
- Nie zmieniono pytań, kluczy ani `verification_status`.

Wyłącznie kurs podstawowy ADR.
