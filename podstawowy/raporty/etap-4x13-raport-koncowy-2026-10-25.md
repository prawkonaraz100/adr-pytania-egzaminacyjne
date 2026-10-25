# Etap 4x13 — raport końcowy: objaśnienia przy pierwszym użyciu

Data: 25.10.2026. Zakres: wyłącznie kurs podstawowy.

## Wyniki dla wszystkich 13 lekcji

| Lekcja | Linki/objaśnienia inline do słowniczka | Zdania lub fragmenty przepisane na język kursanta |
|---|---:|---:|
| B-01 | 9 | 1 |
| B-02 | 9 | 1 |
| B-03 | 5 | 1 |
| B-04 | 4 | 1 |
| B-05 | 5 | 1 |
| B-06 | 6 | 1 |
| B-07 | 4 | 1 |
| B-08 | 6 | 1 |
| B-09 | 6 | 1 |
| B-10 | 4 | 1 |
| B-11 | 8 | 1 |
| B-12 | 6 | 1 |
| B-13 | 9 | 1 |
| **Razem** | **81** | **13** |

Liczba linków to stan końcowy kotwic inline w lekcjach; obejmuje też odsyłacze dodane przy pierwszym użyciu w listach i akapitach. Nie są to zmiany w treści banku pytań.

## Co zrobiono
- Dodano objaśnienia przy pierwszym użyciu skrótów i terminów fachowych, m.in. numeru UN, LQ/EQ, ADR 1.1.3.6, DMC, RID/IMDG, kodu tunelowego D/E, instrukcji pisemnych, grupy pakowania, numeru rozpoznawczego zagrożenia, tablicy pomarańczowej, świadectwa dopuszczenia pojazdu, zaświadczenia kierowcy ADR, OVERPACK, kategorii transportowej, planu ochrony, towarów dużego ryzyka, kodu klasyfikacyjnego, zagrożenia dodatkowego i tabeli A.
- Dodano/ujednolicono kotwice w `podstawowy/SLOWNICZEK.md`.
- Uproszczono po jednym zdaniu lub fragmencie w każdej lekcji, wyjaśniając sens wymogu i praktyczne działanie kierowcy.
- Naprawiono wadliwe odmiany wyrazów powstałe przy wcześniejszych wstawieniach i sprawdzono, że nie pozostały ciągi typu `pisemn (... )e` lub `pomarańczow (... )ej`.
- Dodano blokujący test `tests/test_learner_glossary.py` sprawdzający pierwsze użycie w tym samym akapicie/list item.

## Testy i stan banku
- Test słowniczka: uruchamiany w Quality Gate przez `python -m unittest discover -s tests -v`; wynik końcowy potwierdzi CI dla PR tej partii.
- Bank: 609 pytań, bez zmian ID, poprawnych liter, explanation i statusów.
- Wszystkie pytania pozostają `needs_review`; 0 oznaczono jako `verified`.
- Explanation: minimum 300 znaków, 0 poniżej 200.
- „Poprawna = jedyna najdłuższa” per dział:
  - B-01: 15,56%; B-02: 14,29%; B-03: 14,29%; B-04: 15,22%.
  - B-05: 13,95%; B-06: 11,11%; B-07: 12,50%; B-08: 14,29%.
  - B-09: 8,70%; B-10: 7,27%; B-11: 13,95%; B-12: 15,91%; B-13: 8,51%.
- Wszystkie działy pozostają w limicie ≤16%.

## Ograniczenia
Nie zmieniano merytorycznych odpowiedzi ani podstaw prawnych w banku. Redakcja językowa nie jest niezależną weryfikacją prawną; materiały i pytania pozostają do odbioru specjalisty.


## Dodatkowa kontrola czytelności — dwie lekcje

Po scaleniu partii wykonano osobny przegląd dwóch lekcji wybranych do kontroli języka: B-03 i B-11. Była to próba jakościowa, nie dowód pełnego audytu wszystkich 13 lekcji.

| Lekcja | Przed | Po | Zmiana |
|---|---|---|---|
| B-03 | „MARINE POLLUTANT” występowało bez polskiego objaśnienia, a relację z „ENVIRONMENTALLY HAZARDOUS” opisano abstrakcyjnie. | Dodano krótkie polskie znaczenia obu określeń i prostą instrukcję, by sprawdzić warunki ADR 5.4.1.1.18, zamiast traktować je jako automatyczne zamienniki. | 2 określenia objaśnione w kontekście; bez zmiany reguły prawnej. |
| B-11 | „Jednostka” w zdaniu o wielu kodach tunelowych mogła być odczytana jako dowolny przedmiot lub kontener. | Przy pierwszym użyciu dodano prostą definicję jednostki transportowej i link do kotwicy słowniczka. | 1 objaśnienie inline. |

### Przykłady przed → po
1. **B-03 — wpis w dokumencie:** „wpis „MARINE POLLUTANT” może mieć znaczenie w warunkach określonych przepisem” → „„MARINE POLLUTANT” („zanieczyszczający środowisko morskie”) […] sprawdź warunki ADR 5.4.1.1.18”.
2. **B-11 — różne kody:** „Jeśli jednostka przewozi towary z różnymi kodami tunelowymi” → „Jeśli jednostka transportowa (pojazd silnikowy z przyczepą lub naczepą, gdy tworzą zestaw; [słowniczek](../SLOWNICZEK.md#jednostka-transportowa)) […]”.
3. **Ograniczenie przeglądu:** w tej próbie nie wykryto podstawy do zmiany numerów przepisów ani wymagań liczbowych. Nie oznacza to niezależnej weryfikacji prawnej całego podręcznika.

