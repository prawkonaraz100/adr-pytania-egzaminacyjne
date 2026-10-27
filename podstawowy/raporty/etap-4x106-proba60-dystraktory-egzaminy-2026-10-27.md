# Etap 4x106 — nowa próbka 60, dystraktor ADR-B-0211 i regresja kursu

- Data: 2026-10-27.
- Punkt wejścia: świeży `main` po PR #564, commit `89688b237bc8a7c9d06e2847bc05ae35e0071303`.
- Zakres: wyłącznie kurs podstawowy ADR.
- Metoda próbki: LCG/Fisher–Yates, seed `41062026); wyłączono 75 unikalnych ID z prób 4x103–4x105.

## 1. Próbka 60 explanation

ID sprawdzone:
```
ADR-B-0602, ADR-B-0304, ADR-B-0373, ADR-B-0383, ADR-B-0444, ADR-B-0081, ADR-B-0568, ADR-B-0609, ADR-B-0268, ADR-B-0450, ADR-B-0291, ADR-B-0366, ADR-B-0298, ADR-B-0048, ADR-B-0139, ADR-B-0227, ADR-B-0290, ADR-B-0520, ADR-B-0521, ADR-B-0178, ADR-B-0314, ADR-B-0380, ADR-B-0376, ADR-B-0183, ADR-B-0484, ADR-B-0372, ADR-B-0542, ADR-B-0381, ADR-B-0541, ADR-B-0461, ADR-B-0328, ADR-B-0353, ADR-B-0483, ADR-B-0434, ADR-B-0558, ADR-B-0305, ADR-B-0332, ADR-B-0234, ADR-B-0155, ADR-B-0432, ADR-B-0173, ADR-B-0204, ADR-B-0306, ADR-B-0031, ADR-B-0153, ADR-B-0163, ADR-B-0472, ADR-B-0569, ADR-B-0166, ADR-B-0393, ADR-B-0489, ADR-B-0514, ADR-B-0308, ADR-B-0391, ADR-B-0211, ADR-B-0262, ADR-B-0471, ADR-B-0116, ADR-B-0203, ADR-B-0074
```

- Przejrzano wszystkie 60 wyjaśnień w kontekście treści pytania, opcji A/B/C, poprawnej litery i podstawy ADR.
- Długość: **300–457 znaków**; liczba zdań: **3–5**; explanation poniżej 200 znaków: **0**.
- Nie znaleziono suchego cytatu przepisu ani wyjaśnienia, które wymagałoby przepisania ze względu na strukturę lub długość.
- Potwierdzony problem dydaktyczny znaleziono w dystraktorze ADR-B-0211: odpowiedź A była nadmiernie długa i niemal dosłownie wyliczała brak weryfikacji, przez co łatwo było ją odrzucić bez zrozumienia zasady.

## 2. Potwierdzona korekta ADR-B-0211

Pytanie dotyczy sprawdzenia tożsamości i upoważnienia przewoźnika przed wydaniem towaru. Zmieniono błędne opcje A i B, aby obie przedstawiały wiarygodne, ale niepełne sposoby weryfikacji. Poprawna litera C, treść pytania, explanation, podstawa ADR i status pozostały bez zmian.

- **Opcja A przed:** „Towar można wydać każdej osobie, która zna numer zamówienia i nazwę odbiorcy; nie trzeba sprawdzać, jakiego przewoźnika reprezentuje ani czy ma upoważnienie do odbioru”.
- **Opcja A po:** „Wydać po samym numerze zamówienia, bez sprawdzania upoważnienia do odbioru”.
- **Opcja B przed:** „Towar wolno wydać bez weryfikacji, jeśli kierowca nie żąda kopii dokumentów”.
- **Opcja B po:** „Wystarczy porównać nazwę przewoźnika na pojeździe z dokumentem; nie trzeba sprawdzać upoważnienia do odbioru”.
- **Dlaczego:** nowa opcja opisuje realistyczną pomyłkę — utożsamienie znajomości danych zamówienia z prawem do odbioru — bez nadmiernego naprowadzania długością. Aktualne explanation już wyjaśnia, dlaczego sam numer zamówienia lub nazwa odbiorcy nie potwierdzają upoważnienia.
- **Podstawa:** ADR 1.10.1.2.
- Migawka przed/po: [snapshot ADR-B-0211](../../review/batches/4x106-distractor-snapshot-ADR-B-0211.json).
- Odświeżono snapshot sekwencyjnego audytu `review/sequential/211-216.json`; rekord nadal oznaczony `needs_review` i niezatwierdzony przez specjalistę.

## 3. Scenariusze praktyczne

Skontrolowano wszystkie **39 scenariuszy** w `podstawowy/praktyka/scenariusze-13-dzialow.json`:
- każdy zawiera co najmniej 3 kroki działania kierowcy;
- każdy zawiera typowe błędy, podstawę ADR, kryteria oceny i wniosek dla kursanta;
- wszystkie `question_ids` istnieją i należą do modułu scenariusza;
- brak brakujących pól lub nieprawidłowych odwołań: **0**.

Nie zmieniano scenariuszy, ponieważ kontrola nie wykazała potwierdzonego błędu.

## 4. Egzaminy próbne i pakiet recenzyjny

Po zmianie banku zaktualizowano `source_bank_head` we wszystkich wariantach i kluczach 001–005. ADR-B-0211 nie występuje w żadnym z pięciu arkuszy, więc nie trzeba było zmieniać treści wariantów ani kluczy. Zaktualizowano również migawkę próbki 4x96, manifest pakietu recenzyjnego i bieżące indeksy specjalisty.

- Nowy blob `podstawowy/questions.jsonl`: `236819b5e6ea555285ad74d4a94ce6471bac2287`.
- 5 wariantów × 30 pytań; brak duplikatów w arkuszach i 150 unikalnych ID łącznie.
- Każdy wariant: 13 działów, A/B/C = 10/10/10, maksymalna seria tej samej litery = 3.
- Synchronizacja klucza po mapowaniu liter: bez rozbieżności.

## 5. Quality Gate — preflight danych

- Pytania: 609; unikalne ID: 609.
- Statusy: 609 `needs_review`, 0 `verified`.
- Minimum explanation: 300 znaków; poniżej 200: 0.
- „Poprawna = jedyna najdłuższa”: 73/609 = **11,99%** globalnie.
- Maksimum działowe: **14,29%** (B-02 i B-03); wszystkie działy poniżej 18%.
- Rozkład działów i poprawnych liter w banku nie uległ zmianie; zmieniono tylko długość błędnej opcji A w B-12.

## 6. Testy i ograniczenia

Nie uruchomiono testów lokalnych: dostępne połączenie umożliwia pracę z repozytorium przez GitHub, ale nie udostępnia lokalnego checkoutu. Pełny Quality Gate GitHub Actions na PR jest warunkiem scalenia. Kontrole skryptowe na pobranych plikach potwierdziły spójność metryk, scenariuszy, wariantów, kluczy i migawki audytu.

Nie dodano nowych pytań, ponieważ nie wykryto luki programu potwierdzonej w tej próbce. Nie zmieniono żadnej poprawnej litery i nie oznaczono pytania jako `verified`. Nie rozpoczęto kursu cystern ani innego kursu.
