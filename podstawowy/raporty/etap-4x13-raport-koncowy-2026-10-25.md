# Etap 4x13 — raport końcowy: objaśnienia przy pierwszym użyciu

Data: 25.10.2026. Zakres: wyłącznie kurs podstawowy.

## Wyniki dla wszystkich 13 lekcji

| Lekcja | Linki/objaśnienia inline do słowniczka | Zdania lub fragmenty przepisane na język kursanta |
|---|---:|---:|
| B-01 | 9 | 1 |
| B-02 | 9 | 1 |
| B-03 | 7 | 1 |
| B-04 | 4 | 1 |
| B-05 | 5 | 1 |
| B-06 | 6 | 1 |
| B-07 | 4 | 1 |
| B-08 | 6 | 1 |
| B-09 | 6 | 1 |
| B-10 | 4 | 1 |
| B-11 | 9 | 1 |
| B-12 | 6 | 1 |
| B-13 | 9 | 1 |
| **Razem** | **84** | **13** |

Liczba linków to stan końcowy kotwic inline w lekcjach; obejmuje też odsyłacze dodane przy pierwszym użyciu w listach i akapitach. W dodatkowej kontroli czytelności po partiach dodano 2 objaśnienia w B-03 i 1 w B-11; dlatego tabela i suma zostały zaktualizowane do 84. Nie są to zmiany w treści banku pytań.

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



## Kontrola naprawcza po odbiorze — 25.10.2026, wieczór

Po wcześniejszych partiach etapu 4x13 sprawdzono jeszcze raz rzeczywiste pliki na świeżym main. Ta kontrola wykazała kilka usterek w automatycznie wstawionych definicjach, których nie odzwierciedlała sama liczba odsyłaczy:

| Partia | Potwierdzone problemy | Naprawa | CI |
|---|---|---|---|
| B-01–04 | B-01: zagnieżdżony odsyłacz i powtarzające się objaśnienie ADR; B-02: uszkodzone słowo „kod klasyfikacyjny” i brak objaśnienia ADR przy pierwszym użyciu | Uproszczono wstęp B-01; poprawiono termin i pierwsze użycie ADR w B-02 | PASS — [PR #366](../pull/366), [run #40236972670](../actions/runs/40236972670) |
| B-05–08 | B-05: zagnieżdżone objaśnienie numeru UN; CI wskazało brak kotwicy ADR w B-05, tabeli A w B-06 i ADR w B-08 | Uproszczono pierwsze objaśnienia, dodano brakujące odsyłacze i definicję świadectwa dopuszczenia pojazdu | PASS — [PR #367](../pull/367), [run #40237227963](../actions/runs/40237227963) |
| B-09–13 | B-12: uszkodzony ciąg „))DR 1.10.3.1.2” | Naprawiono tekst i uproszczono wyjaśnienie sprawdzania progów dla towarów dużego ryzyka | PASS — [PR #368](../pull/368), [run #40237340053](../actions/runs/40237340053) |

### Dodatkowy wynik kontroli
- Potwierdzone uszkodzenia składni lub braków objaśnień: **6 problemów** (B-01, B-02, B-05, B-06, B-08, B-12), poprawione.
- Akapity/elementy listy uproszczone lub poprawione: 8; dodano bezpośrednią definicję świadectwa dopuszczenia pojazdu w B-08.
- Test tests/test_learner_glossary.py początkowo zablokował PR #366 i #367, ponieważ pierwsze użycia nie miały odsyłacza w tym samym akapicie. Po poprawkach wszystkie trzy PR-y naprawcze uzyskały PASS Quality Gate.
- Bank pytań, klucze egzaminów, poprawne litery i statusy weryfikacji nie zostały zmienione. Żadnego pytania nie oznaczono jako verified.
- Nie uruchomiono testów w osobnym lokalnym checkout; testy zostały wykonane przez CI GitHub. Nie deklarujemy lokalnego PASS.
- Nie dodano nowych twierdzeń prawnych ani nie zmieniano wartości progowych. Wszystkie pytania pozostają do niezależnej kontroli specjalisty ADR.
