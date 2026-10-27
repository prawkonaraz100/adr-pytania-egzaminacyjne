# Etap 4x93 — pełny indeks pytań wrażliwych na zmianę wartości ADR

- Data: 27.10.2026.
- Punkt wejścia: świeży `main`, `e0ef1ebe4ba3f246906293de06eebf6f17f788d9`.
- Bank blob: `4a1a5d7f1ca8a5124eb096cd228aa92952fac6da`.
- Zakres: wyłącznie kurs podstawowy ADR.

## 1. Cel i ograniczenia

To skryptowo wygenerowany **indeks wpływu zmian przepisów** dla specjalisty, nie stwierdzenie błędów. Regex wyszukuje wartości, jednostki, kody i punkty ADR w treści pytań, opcjach, explanation oraz podstawach. Kategorie nakładają się na siebie, a część wyników to zwykłe dystraktory lub ogólne odniesienia do przepisów. Samo wystąpienie liczby nie oznacza, że pytanie wymaga poprawki.

Nie zmieniano banku, poprawnych liter, lekcji, scenariuszy ani egzaminów. Nie ma potwierdzonego urzędowego tekstu ADR 2027, na podstawie którego można byłoby aktualizować wartości. Wszystkie rekordy pozostają `needs_review`.

## 2. Stan Quality Gate na wejściu

- Quality Gate `main`: PASS, [run #40544478785](https://github.com/prawkonaraz100/adr-pytania-egzaminacyjne/actions/runs/40544478785).
- Rekordy / unikalne ID: 609 / 609.
- Statusy: 609 `needs_review`, 0 `verified`.
- Minimum explanation: 300 znaków; poniżej 200: 0.
- Poprawna odpowiedź jako jedyna najdłuższa: 73/609 = 11.99%.

## 3. Wynik skanowania

| Kategoria wyszukiwania | Kandydaci | Priorytet recenzji | Uwaga |
|---|---:|---|---|
| Wyłączenia i limity ilościowe | 49 | Wysoki | Koniecznie odróżnić 1.1.3.6 od LQ i EQ; sprawdzić kategorię transportową, współczynniki, jednostki oraz warunki pakowania/dokumentacji. |
| Wymiary oznakowania | 5 | Wysoki | Sprawdzić standardowe wymiary, obrzeża i dokładne warunki dopuszczenia formatu zmniejszonego; błędne opcje nie są samodzielnie podstawą do zmiany. |
| Gaśnice i wyposażenie | 58 | Wysoki | Porównać DMC, granice przedziałów, liczbę gaśnic, łączną pojemność i odrębne minimum dla wyłączenia 1.1.3.6. |
| Kody tunelowe | 40 | Wysoki | Sprawdzić kolumnę 15 tabeli A, postać przewozu dla D/E, kombinowanie kodów oraz warunek B1000C przy dokładnie 1000 kg i po przekroczeniu progu. |
| Terminy i umowy | 9 | Krytyczny przed datą | Każdy termin sprawdzić w urzędowym źródle. M364: przed użyciem materiału po 31.12.2026 ponownie sprawdzić listę UNECE i polską publikację; nie zakładać przedłużenia. |
| Dokumenty, transport kombinowany i DOT | 160 | Średni/wysoki | To szeroki filtr przypisów i nazw gałęzi transportu, a nie lista 160 błędów. Specjalista powinien potwierdzić zakres wyjątku, wymagany zapis dokumentowy i warunki stosowania. |

Liczby są **niezależnymi zbiorami z nakładaniem się** — nie należy ich sumować jako liczby unikalnych pytań.

## 4. Pełne listy kandydatów

### 4.1 Wyłączenia i limity ilościowe — 49 ID

`ADR-B-0008`, `ADR-B-0046`, `ADR-B-0061`, `ADR-B-0073`, `ADR-B-0085`, `ADR-B-0089`, `ADR-B-0091`, `ADR-B-0093`, `ADR-B-0147`, `ADR-B-0149`, `ADR-B-0179`, `ADR-B-0197`, `ADR-B-0209`, `ADR-B-0248`, `ADR-B-0256`, `ADR-B-0259`, `ADR-B-0260`, `ADR-B-0261`, `ADR-B-0271`, `ADR-B-0272`, `ADR-B-0273`, `ADR-B-0282`, `ADR-B-0294`, `ADR-B-0313`, `ADR-B-0322`, `ADR-B-0323`, `ADR-B-0421`, `ADR-B-0456`, `ADR-B-0457`, `ADR-B-0461`, `ADR-B-0462`, `ADR-B-0463`, `ADR-B-0470`, `ADR-B-0490`, `ADR-B-0512`, `ADR-B-0526`, `ADR-B-0527`, `ADR-B-0528`, `ADR-B-0534`, `ADR-B-0535`, `ADR-B-0540`, `ADR-B-0570`, `ADR-B-0571`, `ADR-B-0572`, `ADR-B-0573`, `ADR-B-0595`, `ADR-B-0605`, `ADR-B-0606`, `ADR-B-0609`

Rozkład modułowy: ADR-B-01: 25; ADR-B-02: 0; ADR-B-03: 8; ADR-B-04: 0; ADR-B-05: 0; ADR-B-06: 1; ADR-B-07: 0; ADR-B-08: 4; ADR-B-09: 0; ADR-B-10: 1; ADR-B-11: 7; ADR-B-12: 2; ADR-B-13: 1.

### 4.2 Wymiary oznakowania — 5 ID

`ADR-B-0018`, `ADR-B-0191`, `ADR-B-0258`, `ADR-B-0469`, `ADR-B-0470`

Rozkład modułowy: ADR-B-01: 0; ADR-B-02: 0; ADR-B-03: 2; ADR-B-04: 0; ADR-B-05: 0; ADR-B-06: 3; ADR-B-07: 0; ADR-B-08: 0; ADR-B-09: 0; ADR-B-10: 0; ADR-B-11: 0; ADR-B-12: 0; ADR-B-13: 0.

### 4.3 Gaśnice i wyposażenie — 58 ID

`ADR-B-0015`, `ADR-B-0022`, `ADR-B-0023`, `ADR-B-0024`, `ADR-B-0056`, `ADR-B-0057`, `ADR-B-0071`, `ADR-B-0072`, `ADR-B-0073`, `ADR-B-0074`, `ADR-B-0075`, `ADR-B-0076`, `ADR-B-0077`, `ADR-B-0108`, `ADR-B-0112`, `ADR-B-0152`, `ADR-B-0166`, `ADR-B-0168`, `ADR-B-0169`, `ADR-B-0171`, `ADR-B-0176`, `ADR-B-0184`, `ADR-B-0197`, `ADR-B-0208`, `ADR-B-0222`, `ADR-B-0223`, `ADR-B-0231`, `ADR-B-0232`, `ADR-B-0251`, `ADR-B-0252`, `ADR-B-0253`, `ADR-B-0254`, `ADR-B-0282`, `ADR-B-0283`, `ADR-B-0329`, `ADR-B-0332`, `ADR-B-0352`, `ADR-B-0376`, `ADR-B-0417`, `ADR-B-0418`, `ADR-B-0419`, `ADR-B-0420`, `ADR-B-0421`, `ADR-B-0422`, `ADR-B-0423`, `ADR-B-0424`, `ADR-B-0472`, `ADR-B-0473`, `ADR-B-0483`, `ADR-B-0484`, `ADR-B-0485`, `ADR-B-0486`, `ADR-B-0493`, `ADR-B-0509`, `ADR-B-0585`, `ADR-B-0596`, `ADR-B-0597`, `ADR-B-0608`

Rozkład modułowy: ADR-B-01: 1; ADR-B-02: 1; ADR-B-03: 2; ADR-B-04: 3; ADR-B-05: 13; ADR-B-06: 0; ADR-B-07: 1; ADR-B-08: 35; ADR-B-09: 1; ADR-B-10: 0; ADR-B-11: 1; ADR-B-12: 0; ADR-B-13: 0.

### 4.4 Kody tunelowe — 40 ID

`ADR-B-0032`, `ADR-B-0033`, `ADR-B-0063`, `ADR-B-0064`, `ADR-B-0065`, `ADR-B-0083`, `ADR-B-0084`, `ADR-B-0085`, `ADR-B-0086`, `ADR-B-0174`, `ADR-B-0207`, `ADR-B-0208`, `ADR-B-0209`, `ADR-B-0248`, `ADR-B-0262`, `ADR-B-0263`, `ADR-B-0264`, `ADR-B-0322`, `ADR-B-0430`, `ADR-B-0431`, `ADR-B-0432`, `ADR-B-0434`, `ADR-B-0457`, `ADR-B-0487`, `ADR-B-0488`, `ADR-B-0489`, `ADR-B-0490`, `ADR-B-0508`, `ADR-B-0512`, `ADR-B-0525`, `ADR-B-0536`, `ADR-B-0539`, `ADR-B-0540`, `ADR-B-0574`, `ADR-B-0575`, `ADR-B-0576`, `ADR-B-0591`, `ADR-B-0602`, `ADR-B-0603`, `ADR-B-0604`

Rozkład modułowy: ADR-B-01: 0; ADR-B-02: 0; ADR-B-03: 0; ADR-B-04: 0; ADR-B-05: 0; ADR-B-06: 0; ADR-B-07: 0; ADR-B-08: 0; ADR-B-09: 0; ADR-B-10: 0; ADR-B-11: 36; ADR-B-12: 1; ADR-B-13: 3.

### 4.5 Terminy i umowy — 9 ID

`ADR-B-0145`, `ADR-B-0198`, `ADR-B-0211`, `ADR-B-0285`, `ADR-B-0413`, `ADR-B-0451`, `ADR-B-0452`, `ADR-B-0553`, `ADR-B-0566`

Rozkład modułowy: ADR-B-01: 0; ADR-B-02: 0; ADR-B-03: 0; ADR-B-04: 0; ADR-B-05: 0; ADR-B-06: 0; ADR-B-07: 1; ADR-B-08: 3; ADR-B-09: 0; ADR-B-10: 2; ADR-B-11: 0; ADR-B-12: 2; ADR-B-13: 1.

**Ważny punkt kontrolny — M364:** ADR-B-0145 i ADR-B-0198 odnoszą się do wyjątku dla świadectwa dopuszczenia przyczepy, a nie samochodu silnikowego. Według ostatniej kontroli urzędowej umowa jest wskazana jako ważna do 31.12.2026. Przed użyciem materiału po tej dacie sprawdzić ponownie listę [UNECE — ADR Multilateral Agreements](https://unece.org/transport/road-transport/adr-multilateral-agreements) i polską publikację. Nie aktualizować na podstawie domysłu.

### 4.6 Dokumenty, transport kombinowany i DOT — 160 ID

`ADR-B-0001`, `ADR-B-0004`, `ADR-B-0012`, `ADR-B-0027`, `ADR-B-0028`, `ADR-B-0029`, `ADR-B-0030`, `ADR-B-0033`, `ADR-B-0036`, `ADR-B-0041`, `ADR-B-0042`, `ADR-B-0043`, `ADR-B-0048`, `ADR-B-0049`, `ADR-B-0061`, `ADR-B-0062`, `ADR-B-0071`, `ADR-B-0078`, `ADR-B-0085`, `ADR-B-0089`, `ADR-B-0091`, `ADR-B-0094`, `ADR-B-0095`, `ADR-B-0096`, `ADR-B-0097`, `ADR-B-0101`, `ADR-B-0118`, `ADR-B-0119`, `ADR-B-0120`, `ADR-B-0131`, `ADR-B-0136`, `ADR-B-0140`, `ADR-B-0141`, `ADR-B-0142`, `ADR-B-0148`, `ADR-B-0150`, `ADR-B-0153`, `ADR-B-0156`, `ADR-B-0157`, `ADR-B-0159`, `ADR-B-0161`, `ADR-B-0162`, `ADR-B-0163`, `ADR-B-0178`, `ADR-B-0180`, `ADR-B-0187`, `ADR-B-0203`, `ADR-B-0205`, `ADR-B-0206`, `ADR-B-0207`, `ADR-B-0208`, `ADR-B-0209`, `ADR-B-0215`, `ADR-B-0229`, `ADR-B-0240`, `ADR-B-0247`, `ADR-B-0248`, `ADR-B-0250`, `ADR-B-0264`, `ADR-B-0266`, `ADR-B-0268`, `ADR-B-0269`, `ADR-B-0273`, `ADR-B-0275`, `ADR-B-0277`, `ADR-B-0278`, `ADR-B-0279`, `ADR-B-0280`, `ADR-B-0287`, `ADR-B-0290`, `ADR-B-0292`, `ADR-B-0295`, `ADR-B-0297`, `ADR-B-0306`, `ADR-B-0309`, `ADR-B-0311`, `ADR-B-0318`, `ADR-B-0320`, `ADR-B-0321`, `ADR-B-0322`, `ADR-B-0332`, `ADR-B-0346`, `ADR-B-0354`, `ADR-B-0358`, `ADR-B-0360`, `ADR-B-0368`, `ADR-B-0381`, `ADR-B-0382`, `ADR-B-0383`, `ADR-B-0384`, `ADR-B-0385`, `ADR-B-0386`, `ADR-B-0387`, `ADR-B-0388`, `ADR-B-0389`, `ADR-B-0393`, `ADR-B-0395`, `ADR-B-0396`, `ADR-B-0397`, `ADR-B-0398`, `ADR-B-0400`, `ADR-B-0410`, `ADR-B-0412`, `ADR-B-0417`, `ADR-B-0423`, `ADR-B-0427`, `ADR-B-0428`, `ADR-B-0433`, `ADR-B-0434`, `ADR-B-0438`, `ADR-B-0441`, `ADR-B-0442`, `ADR-B-0444`, `ADR-B-0445`, `ADR-B-0446`, `ADR-B-0447`, `ADR-B-0448`, `ADR-B-0449`, `ADR-B-0450`, `ADR-B-0451`, `ADR-B-0452`, `ADR-B-0453`, `ADR-B-0454`, `ADR-B-0461`, `ADR-B-0463`, `ADR-B-0464`, `ADR-B-0467`, `ADR-B-0483`, `ADR-B-0484`, `ADR-B-0486`, `ADR-B-0488`, `ADR-B-0492`, `ADR-B-0496`, `ADR-B-0498`, `ADR-B-0499`, `ADR-B-0500`, `ADR-B-0501`, `ADR-B-0503`, `ADR-B-0511`, `ADR-B-0516`, `ADR-B-0521`, `ADR-B-0522`, `ADR-B-0527`, `ADR-B-0529`, `ADR-B-0535`, `ADR-B-0549`, `ADR-B-0556`, `ADR-B-0563`, `ADR-B-0565`, `ADR-B-0568`, `ADR-B-0569`, `ADR-B-0572`, `ADR-B-0575`, `ADR-B-0576`, `ADR-B-0580`, `ADR-B-0581`, `ADR-B-0595`, `ADR-B-0596`, `ADR-B-0601`, `ADR-B-0604`

Rozkład modułowy: ADR-B-01: 12; ADR-B-02: 24; ADR-B-03: 10; ADR-B-04: 13; ADR-B-05: 4; ADR-B-06: 4; ADR-B-07: 6; ADR-B-08: 7; ADR-B-09: 8; ADR-B-10: 46; ADR-B-11: 14; ADR-B-12: 6; ADR-B-13: 6.

To szeroki filtr zawierający odniesienia do IMDG/RID/DOT i punktów dokumentowych. Nie oznacza, że każde pytanie z listy jest prawnie wrażliwe lub błędne. Przy recenzji sprawdzić, czy pytanie testuje konkretny warunek, a nie sugeruje automatycznego zwolnienia z ADR.

## 5. Kontrola zgodności z pozostałymi artefaktami

Na podstawie poprzednich kontroli 4x91 i 4x92:
- 13 lekcji obejmuje wszystkie 609 ID banku; w kontrolowanych partiach brakujących i obcych ID: 0.
- 39 scenariuszy, dokładnie 3 na dział; nieistniejące/obce `question_ids`: 0.
- Warianty egzaminów 001–005 i klucze wskazują blob banku `4a1a5d7f1ca8a5124eb096cd228aa92952fac6da`; każdy arkusz ma 30 unikalnych pytań, 13 działów, A/B/C 10/10/10 i maksymalną serię 3. Zgodność klucza z treścią poprawnej opcji: PASS.
- W 4x91–4x92 nie stwierdzono potwierdzonej sprzeczności wymagającej zmiany liczby, progu lub dokumentu w reprezentatywnych kontrolach. Pełny indeks pomaga specjaliście wybrać następne rekordy do porównania z urzędowym tekstem.

## 6. Lista kontrolna dla specjalisty

1. Dla każdego kandydata sprawdzić tekst ADR 2025 (Dz.U. 2025 poz. 642) i sprostowanie Dz.U. 2025 poz. 1575.
2. Zapisać dokładny punkt, warunki, wyjątki, jednostki i wynik porównania; nie poprawiać wartości wyłącznie dlatego, że pojawiła się w heurystyce.
3. Po opublikowaniu kolejnej edycji ADR porównać te same punkty w nowym tekście i zaznaczyć wyłącznie potwierdzone zmiany.
4. Dla każdego zmienionego pytania sprawdzić A/B/C, explanation, lekcję, scenariusze, warianty/klucze i snapshoty audytu.
5. Nie zmieniać `verification_status` z `needs_review` bez formalnej niezależnej recenzji.

## 7. Wynik etapu

- Potwierdzone sprzeczności prawne w tym skanowaniu: **0**.
- Pytania zmienione: **0**.
- Warianty i klucze zregenerowane: **nie — bank nie został zmieniony**.
- Status: indeks gotowy do wykorzystania przez specjalistę; nie jest zatwierdzeniem prawnym.
- Zakres: wyłącznie kurs podstawowy ADR.
