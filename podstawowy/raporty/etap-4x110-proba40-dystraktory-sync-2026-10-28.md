# Etap 4x110 — próbka 40, dystraktory i synchronizacja egzaminów

- Data: 2026-10-28.
- Punkt wejścia: świeży `main` `0380b90701759ad8434757450ee47d6d174e1185`; Quality Gate PASS, run [#40616357594](https://github.com/prawkonaraz100/adr-pytania-egzaminacyjne/actions/runs/40616357594).
- Zakres: wyłącznie kurs podstawowy ADR.
- Bank: 609 pytań, 609 unikalnych ID, wszystkie `needs_review`, 0 `verified`.
- Lista próbki i wykluczeń: [manifest 4x110](etap-4x110-wykluczenia-proby.json), seed `41102026`.

## 1. Próba 40 explanation

Próbka została wylosowana deterministycznie metodą LCG/Fisher–Yates z puli po konserwatywnym wykluczeniu wszystkich identyfikatorów ADR-B występujących w artefaktach raportowych etapów 4x103–4x109. Wykluczono 303 identyfikatorów; pula wynosiła 306; sprawdzono 40 unikalnych pytań.

- Długość explanation w próbie: 304–439 znaków.
- Liczba zdań: 3–5.
- Jednozdaniowe wyjaśnienia: 0; poniżej 200 znaków: 0.
- **Nie znaleziono w tej próbie explanation wymagających samodzielnej redakcji tylko ze względu na długość lub strukturę.** Wyjaśnienia już tłumaczyły sens poprawnej odpowiedzi, najważniejszą pomyłkę i podawały podstawę ADR. Trzy explanation dopasowano do zmienionych dystraktorów.

## 2. Potwierdzone poprawki dystraktorów

| ID | Potwierdzona słabość | Zmiana | Podstawa |
|---|---|---|---|
| ADR-B-0016 | „Na odwrocie tablicy” było mało wiarygodnym dystraktorem i nie sprawdzało typowej pomyłki w odczycie pól. | Zastąpiono je odpowiedzią o położeniu przy linii podziału; zachowano B jako poprawną. Explanation rozróżnia teraz górne pole zagrożenia i dolne pole numeru UN. | ADR 5.3.2.2.2 |
| ADR-B-0109 | „Wyrzucić dokumenty” było skrajnie absurdalne i zbyt łatwe do odrzucenia. | Zastąpiono je wiarygodnymi błędami: zasłanianiem dokumentów z obawy o informacje oraz przekazaniem tylko numeru UN ustnie. Poprawna odpowiedź i klucz bez zmian. | ADR 5.4.3.4 |
| ADR-B-0164 | Obie błędne odpowiedzi sprowadzały się do „bez płomienia = bezpiecznie”, a jedna nie uwzględniała częstego błędu z zasilaniem akumulatorowym. | Rozdzielono pomyłkę dotyczącą zasilania akumulatorowego i używania poza kabiną. C pozostaje poprawna. | ADR 5.4.3.4 |

Nie zmieniono ID, poprawnych liter ani podstaw prawnych pytań. Nie znaleziono potwierdzonej potrzeby zmiany klucza w banku.

## 3. Spójność egzaminów 001–005

- Zaktualizowano `source_bank_head` we wszystkich pięciu wariantach i kluczach do nowego blobu banku `c2bf003935faf9e51ae8b03759e456006049ef5b`.
- Zaktualizowano kopie odpowiedzi ADR-B-0164 w wariancie 001 i ADR-B-0109 w wariancie 004; poprawiono odpowiadające im explanation w kluczach.
- Kontrola wszystkich pięciu wariantów: po 30 pytań, 30 unikalnych ID, brak pytań spoza banku i brak różnic w zestawach odpowiedzi. Klucze zachowują poprawną literę dla tekstu poprawnej odpowiedzi.
- Kontrola A/B/C w kluczach każdego wariantu: 10/10/10.
- Wstępne porównanie surowych tekstów zgłosiło pozorną rozbieżność w ADR-B-0489. Po uwzględnieniu mapowania liter A/B/C w wariancie 001 potwierdzono, że explanation klucza było zgodne; zachowano prawidłowo zmapowany tekst i nie wprowadzono zmiany merytorycznej.

## 4. Quality Gate — metryki banku

- Poprawna odpowiedź jest jedyną najdłuższą: 72/609 = 11.82% (limit globalny 18%).
- Najkrótsze explanation: 300 znaków; poniżej 200: 0.
- Wszystkie pytania nadal mają status `needs_review`; nie oznaczono żadnego jako `verified`.

| Dział | Pytań | Poprawna = jedyna najdłuższa | Wskaźnik |
|---|---:|---:|---:|
| ADR-B-01 | 45 | 6 | 13.33% |
| ADR-B-02 | 56 | 8 | 14.29% |
| ADR-B-03 | 49 | 6 | 12.24% |
| ADR-B-04 | 46 | 5 | 10.87% |
| ADR-B-05 | 43 | 5 | 11.63% |
| ADR-B-06 | 45 | 6 | 13.33% |
| ADR-B-07 | 48 | 6 | 12.50% |
| ADR-B-08 | 42 | 5 | 11.90% |
| ADR-B-09 | 46 | 4 | 8.70% |
| ADR-B-10 | 55 | 4 | 7.27% |
| ADR-B-11 | 43 | 6 | 13.95% |
| ADR-B-12 | 44 | 6 | 13.64% |
| ADR-B-13 | 47 | 5 | 10.64% |

## 5. Scenariusze i lekcje

Scenariusze praktyczne pozostają 39; nie zmieniano ich treści ani przypisań. Przegląd 13 lekcji potwierdził obecność odwołań do pytań, a w tej partii nie znaleziono podstaw do poprawiania treści lekcji. Zmiany ograniczono do potwierdzonych słabości dystraktorów i kopii egzaminacyjnych.

## Ograniczenia

Próba była rozłączna z identyfikatorami jawnie wymienionymi w artefaktach etapów 4x103–4x109. Nie należy z tego wyciągać wniosku o rozłączności z wcześniejszymi etapami, których raporty nie zachowały kompletnych list. Przegląd dydaktyczny nie zastępuje niezależnej recenzji specjalisty ADR.
