# Etap 4x117 — próbka 40 explanation, dystraktory, spójność kursu

- Data: 2026-10-28.
- Świeży `main` na wejściu: `cf78398aeca638cdd14f0d8e724cd8523f25af91` (PR #575 / etap 4x116).
- Zakres: wyłącznie kurs podstawowy ADR.
- Bank wejściowy: 609 pytań, wszystkie `needs_review`, 0 `verified`.
- Seed próby: `41172026`; pełna lista próby i wykluczeń: [manifest 4x117](etap-4x117-wykluczenia-proby.json).

## 1. Próbka 40 wyjaśnień

Próbę wylosowano deterministycznie spośród pytań, których explanation i dystraktory nie były zmieniane w etapach 4x103–4x116. Każde pytanie oceniono razem z treścią, odpowiedziami A/B/C, poprawną literą i podstawą ADR.

| Wynik | Liczba |
|---|---:|
| Wyjaśnienia przeczytane w kontekście pytania i odpowiedzi | 40 |
| Explanation przepisane dla początkującego | 3 |
| Pytania z potwierdzoną słabością dystraktora | 1 |
| Pytania pozostawione bez zmian | 37 |
| Explanation poniżej 200 znaków w próbie | 0 |
| Zmiany ID lub poprawnej litery | 0 |

**ID próbki (40):** ADR-B-0023, ADR-B-0050, ADR-B-0059, ADR-B-0076, ADR-B-0085, ADR-B-0098, ADR-B-0142, ADR-B-0148, ADR-B-0149, ADR-B-0151, ADR-B-0161, ADR-B-0165, ADR-B-0169, ADR-B-0176, ADR-B-0203, ADR-B-0214, ADR-B-0226, ADR-B-0248, ADR-B-0275, ADR-B-0278, ADR-B-0295, ADR-B-0310, ADR-B-0344, ADR-B-0357, ADR-B-0381, ADR-B-0386, ADR-B-0396, ADR-B-0415, ADR-B-0469, ADR-B-0486, ADR-B-0488, ADR-B-0502, ADR-B-0524, ADR-B-0535, ADR-B-0538, ADR-B-0565, ADR-B-0567, ADR-B-0576, ADR-B-0589, ADR-B-0599.

### Potwierdzone poprawki

| ID | Problem | Zmiana | Podstawa |
|---|---|---|---|
| ADR-B-0085 | Wyjaśnienie było zbyt zbite i powtarzało techniczne sformułowanie o wyłączeniu. | Przepisano je tak, by zaczynało się od praktycznej czynności: sprawdzenia, czy przewóz faktycznie spełnia warunki wyłączenia; zachowano zastrzeżenie dotyczące oznakowania LQ. | ADR 8.6.3.3 |
| ADR-B-0203 | Dystraktor C („ze względu na położenie portu w kraju”) był zbyt łatwy do odrzucenia; wyjaśnienie miało formalny zwrot o „warunkowym uznaniu”. | C zastąpiono wiarygodną pomyłką: założeniem, że dalszy odcinek morski sam uruchamia dodatkowy wpis. Explanation wyjaśnia, że trzeba spełnić warunki konkretnego przepisu. Klucz A bez zmian. | ADR 1.1.4.2.1 i 5.4.1.1.7 |
| ADR-B-0278 | Wyjaśnienie używało skrótu EDI i długiego zdania o papierowym certyfikacie. | Zachowano wymaganą wzmiankę po angielsku, ale rozdzielono ją od prostego objaśnienia EDI i IMDG; wyjaśniono, czemu faktura i usunięcie wzmianki nie wystarczają. | ADR 5.4.2 oraz IMDG 5.4.2.4 |

Przykłady przed/po:
1. **ADR-B-0085:** „jeśli przewóz korzysta z wyłączeń i nie zachodzi wyjątek” → „najpierw sprawdź, czy przewóz rzeczywiście spełnia warunki wyłączenia”.
2. **ADR-B-0203:** „położenie portu w kraju” → „przewóz ma być kontynuowany statkiem, nawet gdy warunek 1.1.4.2.1 nie jest spełniony”.
3. **ADR-B-0278:** „otrzymano przez EDI” → „EDI to elektroniczna wymiana danych”, po czym osobno opisano wymaganą wzmiankę i nazwisko.

Wszystkie trzy zmienione explanation mają 4–5 zdań i 340–488 znaków. Pozostałe 37 wyjaśnień uznano za wystarczająco zrozumiałe: podawały sens poprawnej odpowiedzi, wyjaśniały główne mylące warianty i kończyły się podstawą. Nie dopisywano zmian dla samej liczby edycji.

## 2. Notatki dla niezależnego specjalisty

- **ADR-B-0085:** zapis w istniejącej migawce prawnej nadal ma `official_polish_full_text_comparison: pending`. Nie zmieniano klucza ani zakresu prawnego pytania; przed oznaczeniem jako zweryfikowane specjalista powinien potwierdzić dokładne zastosowanie ADR 8.6.3.3 do opisanego wyłączenia i zastrzeżenia 3.4.13–3.4.14.
- **ADR-B-0567:** wyjaśnienie odwołuje się do art. 415 Kodeksu cywilnego, podczas gdy pole `sources` wskazuje ADR 8.2.2.3.2(k). Nie zmieniono treści bez recenzji prawnej; proszę specjalistę o sprawdzenie, czy metadane źródeł powinny jawnie obejmować Kodeks cywilny.

Te punkty są zgłoszeniami do recenzji, nie potwierdzonymi błędami klucza. Wszystkie pytania zachowują `needs_review`.

## 3. Spójność 13 lekcji, 39 scenariuszy i egzaminów

- **Lekcje B-01–B-13:** sprawdzono obecność sekcji podsumowania i listy powiązanych pytań. Łącznie odwołania obejmują 609 ID; brak nieistniejących ID i brak odwołań do pytania z innego działu.
- **Scenariusze praktyczne:** 39/39; wszystkie `question_ids` istnieją w banku i należą do działu scenariusza. Nie znaleziono brakujących kroków kierowcy.
- **Warianty egzaminu 001–005:** po 30 pytań, 30 unikalnych ID na arkusz, wszystkie pytania i zestawy odpowiedzi istnieją w banku; każdy wariant i każdy klucz wskazuje aktualny blob banku `b763f639efe11f972d4c3047dc8238334f9ff9f2`. Żadne z trzech pytań z poprawionym explanation nie występuje w arkuszach, więc nie było potrzeby zmiany ich treści ani kluczy odpowiedzi. Klucze zachowują mapowanie liter specyficzne dla wariantu.

## 4. Preflight Quality Gate

- Pytania: 609; unikalne ID: 609; duplikaty: 0.
- Statusy: 609 `needs_review`, 0 `verified`.
- Explanation minimum w banku: 300 znaków; poniżej 200: 0.
- Poprawna odpowiedź jest jedyną najdłuższą: **72/609 = 11,82%**.
- Najwyższy wynik działu: **14,29% (B-02)**; wszystkie działy są poniżej limitu 18%.

| Dział | Pytań | Poprawna = jedyna najdłuższa | Wskaźnik | Klucz A/B/C |
|---|---:|---:|---:|---:|
| B-01 | 45 | 6 | 13,33% | 17/17/11 |
| B-02 | 56 | 8 | 14,29% | 21/19/16 |
| B-03 | 49 | 5 | 10,20% | 16/21/12 |
| B-04 | 46 | 6 | 13,04% | 15/18/13 |
| B-05 | 43 | 5 | 11,63% | 18/14/11 |
| B-06 | 45 | 6 | 13,33% | 16/14/15 |
| B-07 | 48 | 6 | 12,50% | 18/18/12 |
| B-08 | 42 | 4 | 9,52% | 12/12/18 |
| B-09 | 46 | 5 | 10,87% | 13/15/18 |
| B-10 | 55 | 4 | 7,27% | 19/18/18 |
| B-11 | 43 | 6 | 13,95% | 12/13/18 |
| B-12 | 44 | 6 | 13,64% | 14/13/17 |
| B-13 | 47 | 5 | 10,64% | 15/15/17 |
| **Razem** | **609** | **72** | **11,82%** | **206/207/196** |

## 5. Testy

Próba klonowania repozytorium do lokalnego środowiska nie powiodła się, ponieważ środowisko nie mogło rozwiązać hosta `github.com`. Nie deklaruję uruchomienia pełnego zestawu testów lokalnie. Zamiast tego wykonano preflight na danych pobranych z GitHub: metryki banku, referencje lekcji/scenariuszy, identyfikatory i zestawy odpowiedzi wariantów oraz synchronizację `source_bank_head`. Pełny test jednostkowy i Quality Gate pozostają wymagane w GitHub Actions przed scaleniem.

Nie zmieniono ID, poprawnych liter, statusów weryfikacji ani podstaw prawnych pytań. Nie rozpoczęto kursu cystern ani innego kursu.
