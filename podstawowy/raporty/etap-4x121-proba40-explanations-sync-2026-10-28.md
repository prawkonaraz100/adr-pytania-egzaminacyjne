# Etap 4x121 — próbka 40 explanation, wiarygodność dystraktorów i spójność

- Data: 2026-10-28.
- Punkt wejścia: świeży `main` po scaleniu PR #581, commit `bc20e8e97ceb29db96107580053b8d34f30c5f8a`.
- Gałąź: `stage4x121-proba40-explanations-sync`.
- Bank przed zmianami: 609 pytań; źródłowy blob `04ace7f478868d0901bbc45fb26af3d866e18538`.
- Zakres: wyłącznie kurs podstawowy ADR.

## 1. Próbka i wynik przeglądu

Próbka 40 pytań została wylosowana deterministycznie (seed `41212026`) z puli pozostałej po wyłączeniu ID z etapów 4x114–4x120. Przeczytano pytanie, wszystkie opcje A/B/C, klucz, explanation i podstawę prawną.

ID próbki:
```
ADR-B-0041, ADR-B-0426, ADR-B-0363, ADR-B-0080, ADR-B-0266, ADR-B-0348, ADR-B-0111, ADR-B-0258, ADR-B-0437, ADR-B-0019, ADR-B-0008, ADR-B-0070, ADR-B-0128, ADR-B-0447, ADR-B-0062, ADR-B-0379, ADR-B-0596, ADR-B-0057, ADR-B-0082, ADR-B-0423, ADR-B-0194, ADR-B-0521, ADR-B-0401, ADR-B-0265, ADR-B-0039, ADR-B-0029, ADR-B-0333, ADR-B-0549, ADR-B-0122, ADR-B-0055, ADR-B-0464, ADR-B-0403, ADR-B-0307, ADR-B-0606, ADR-B-0337, ADR-B-0130, ADR-B-0034, ADR-B-0173, ADR-B-0114, ADR-B-0140
```

- Przejrzano: **40/40**.
- Explanation przepisane: **1** — ADR-B-0041 (wyjaśnienie przyczyny okresowego uzupełniania szkolenia; wskazano osobno, dlaczego zmiana numeru UN i sama zmiana nazwy stanowiska nie są właściwym uzasadnieniem).
- Dystraktory zmienione: **1** — ADR-B-0041, opcja C. Wcześniejsze sformułowanie o zmianie stanowiska mogło sugerować realną potrzebę szkolenia przy zmianie obowiązków, a więc było niejednoznaczne. Zastąpiono je „Po każdej zmianie nazwy stanowiska, niezależnie od wykonywanych zadań”.
- Treść pytania doprecyzowana: **1** — ADR-B-0426. „Paleta” mogła oznaczać jednostkę zbiorczą, podczas gdy tabela 7.5.2.1 opisuje zestaw nalepek na sztuce przesyłki. Nowe brzmienie mówi wprost o jednej sztuce przesyłki z dwiema nalepkami.
- Pozostałe **38 pytań** pozostawiono bez zmian: explanation miały 2–5 zdań, mieściły się w progu długości i wyjaśniały sens odpowiedzi oraz główne pomyłki. Nie znaleziono potwierdzonego błędu wymagającego zmiany klucza lub podstawy prawnej.

## 2. Przykłady przed/po

### ADR-B-0041 — dystraktor C
- **Przed:** „Po zmianie stanowiska pracy, nawet gdy wcześniej zaktualizowano wymagania”.
- **Po:** „Po każdej zmianie nazwy stanowiska, niezależnie od wykonywanych zadań”.
- **Dlaczego:** obowiązki szkoleniowe zależą od rzeczywistych zadań i zmian wymagań, a nie od samej nazwy stanowiska.

### ADR-B-0041 — explanation
- **Przed:** nie wyjaśniało wprost, dlaczego opcja o zmianie stanowiska nie odpowiada na pytanie o okresowe uzupełnianie wiedzy.
- **Po:** „Szkolenie okresowo uzupełnia się, aby pracownik znał aktualne przepisy i umiał bezpiecznie wykonać swoje zadania. Sama zmiana numeru UN towaru nie wyznacza terminu takiej aktualizacji. Zmiana stanowiska może wymagać szkolenia, jeśli zmieniają się obowiązki, ale sama nazwa stanowiska nie oznacza automatycznie, że wiedzę trzeba odświeżyć. Chodzi o zmiany przepisów i wymagań pracy. Podstawa: ADR 1.3.2.4.”
- Długość: 404 znaki; 5 zdań; poprawna litera A i status `needs_review` bez zmian.

### ADR-B-0426 — treść pytania
- **Przed:** „Jedna paleta ma nalepkę 4.1 oraz dodatkową 1…”.
- **Po:** „Na jednej sztuce przesyłki znajdują się dwie nalepki: 4.1 oraz 1…”.
- **Dlaczego:** ujednolicono termin z tabelą ADR 7.5.2.1; klucz B, opcje i podstawa prawna bez zmian.

## 3. Kontrola banku i Quality Gate — preflight

| Kontrola | Wynik |
|---|---:|
| Liczba pytań | 609 |
| Zduplikowane ID | 0 |
| Statusy | 609 `needs_review`, 0 `verified` |
| Explanation poniżej 200 znaków | 0 |
| Najkrótsze / najdłuższe explanation | 300 / 498 znaków |
| Poprawna odpowiedź jako jedyna najdłuższa | 72/609 = **11,82%** |
| Maksimum w dziale | B-02: 8/56 = 14,29%; B-07: 7/48 = 14,58% |
| Limit wskaźnika | ≤18% — spełniony |

Wskaźnik per dział: B-01 6/45 (13,33%); B-02 8/56 (14,29%); B-03 5/49 (10,20%); B-04 6/46 (13,04%); B-05 5/43 (11,63%); B-06 6/45 (13,33%); B-07 7/48 (14,58%); B-08 3/42 (7,14%); B-09 5/46 (10,87%); B-10 4/55 (7,27%); B-11 6/43 (13,95%); B-12 5/44 (11,36%); B-13 6/47 (12,77%).

## 4. Synchronizacja

- Zmieniono bank w dwóch rekordach, bez zmiany ID, poprawnej litery ani podstawy ADR.
- Zaktualizowano migawki `review/legal-clauses/031-060.json`, `review/sequential/031-060.json`, `review/legal-clauses/417-436.json` i `review/sequential/417-436.json`.
- Zaktualizowano `source_bank_head` we wszystkich wariantach i kluczach egzaminu próbnego 001–005 do nowego bloba banku `f18b273e3451730a4efc28e10cd0ff16b03807f5`. Zestawy pytań nie zawierają zmienionych ID, więc nie zmieniano kluczy odpowiedzi ani składu arkuszy.
- Manifest próbki i wykluczeń: [etap-4x121-wykluczenia-proby.json](etap-4x121-wykluczenia-proby.json).

## 5. Testy i ograniczenia

Sprawdzono skryptowo pobrany JSONL: parsowanie wszystkich 609 rekordów, unikalność ID, długości explanation, poprawne litery A/B/C i wskaźnik długości odpowiedzi. W tym środowisku nie ma lokalnego checkoutu repozytorium, więc nie deklaruję uruchomienia pełnego zestawu testów lokalnych. PR wymaga PASS obu jobów Quality Gate CI przed scaleniem. Weryfikacja prawna i oznaczenie `verified` pozostają wyłącznie po stronie specjalisty.
