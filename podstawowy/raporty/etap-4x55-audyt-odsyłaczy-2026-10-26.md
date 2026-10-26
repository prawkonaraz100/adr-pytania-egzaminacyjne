# Etap 4x55 — audyt odsyłaczy lekcji, materiałów instruktora i scenariuszy

- Data: 26.10.2026.
- Świeży `main` przed pracą: `39307c68c395daf40f5b11396e37be285d48aaeb` (po PR #504).
- Zakres: kurs podstawowy ADR.

## Wyniki audytu

| Zasób | Plików sprawdzonych | Brakujące ID | ID z innego działu | Brak linku do słowniczka | Brak odwołań do wszystkich 3 scenariuszy |
|---|---:|---:|---:|---:|---:|
| Lekcje | 13 | 0 | 0 | 0 | 0 |
| Materiały instruktora | 13 | 0 | 0 | 0 | 0 |
| Scenariusze JSON | 39 | 0 | 0 | n/d | n/d |

Wszystkie 13 lekcji miały odsyłacz do `SLOWNICZEK.md`, wszystkie 13 materiałów instruktora wskazywały trzy scenariusze właściwego działu i odwoływały się do istniejących pytań swojego modułu. Jedyną potwierdzoną niespójnością w materiałach instruktora był brak bezpośredniego linku do słowniczka.

## Zmiany

- Dodano link `../SLOWNICZEK.md` do wszystkich 13 materiałów instruktora, aby instruktor mógł szybko wyjaśnić kursantowi skróty i terminy fachowe.
- Rozszerzono `tests/test_learner_glossary.py` o testy blokujące:
  1. każdy materiał instruktora musi linkować do słowniczka i wskazywać wszystkie trzy istniejące scenariusze działu;
  2. wszystkie ID pytań występujące w lekcjach i materiałach instruktora muszą istnieć w banku i należeć do tego samego modułu;
  3. każde `question_id` w 39 scenariuszach musi istnieć w banku i należeć do modułu scenariusza.

Testy nie oceniają poprawności prawnej treści; sprawdzają tylko spójność odwołań i strukturę materiałów.

## Metryki banku

- Pytania: 609; duplikaty ID: 0.
- Statusy: 609 `needs_review`, 0 `verified`.
- Explanation poniżej 200 znaków: 0; minimum 300 znaków.
- „Poprawna = jedyna najdłuższa”: 72/609 = 11.82%; maksimum działu 14.29%.
- Nie zmieniono pytań, kluczy ani egzaminów; nie zmieniono żadnego statusu prawnego.

## Testy

Brak lokalnego checkoutu i niedostępny DNS dla `git clone` uniemożliwiają uczciwe zadeklarowanie testów lokalnych. Nowe testy i pełny Quality Gate muszą przejść w CI przed scaleniem.
