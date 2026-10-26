# Etap 4x54 — synchronizacja starszego indeksu scenariuszy

- Data: 26.10.2026.
- Świeży `main` przed pracą: `b6f1ce90ba709930b137a823aea17534fdcab03d` (po PR #503).
- Zakres: wyłącznie kurs podstawowy ADR.

## Problem i poprawki

W `podstawowy/praktyka/SCENARIUSZE.md` znaleziono starsze podsumowania, które nie nadążyły za poprawkami question IDs z etapu 4x53. To mogło kierować instruktora do pytań niepasujących do sytuacji, mimo że kanoniczny JSON był już poprawiony.

- **B-06:** do zbiorczego indeksu dodano pytania o położenie numeru UN i znaczenie numeru rozpoznawczego zagrożenia (ADR-B-0016, ADR-B-0217), obok aktualnych pytań o rozbieżność tablicy i dokumentów oraz czytelność nalepek.
- **B-09:** z indeksu usunięto niepasujące pytanie o zamknięcia przewozu luzem (ADR-B-0558); wskazano pytania o zabezpieczenie sztuk, czyszczenie pozostałości i mocowanie ciężkiego elementu (ADR-B-0026, ADR-B-0080, ADR-B-0235, ADR-B-0518, ADR-B-0554).
- **B-12:** zbiorczy opis zmieniono z „weryfikacji uprawnienia do odbioru” na „weryfikację przewoźnika oraz postoju”, a listę uzupełniono o pytania dotyczące niezweryfikowanego przewoźnika i zabezpieczeń (ADR-B-0120, ADR-B-0211, ADR-B-0304–0305, ADR-B-0407, ADR-B-0414, ADR-B-0582).
- **B-09-03:** z krótkiego opisu usunięto nieaktualne wskazanie przewozu luzem; opis odpowiada teraz ćwiczeniu mocowania całego ładunku.
- **B-12-03:** skrót w indeksie potwierdza, że chodzi o tożsamość przewoźnika według ADR 1.10.1.2, a nie o ogólny wymóg weryfikacji odbiorcy.

## Walidacja

- Scenariusze w kanonicznym JSON: 39; 3 na każdy z 13 działów.
- question IDs nieistniejące lub przypisane do innego modułu: 0.
- Bank: 609 pytań; duplikaty ID: 0; statusy 609 `needs_review`, 0 `verified`.
- Nie zmieniono JSON scenariuszy, banku pytań, poprawnych odpowiedzi, explanation, egzaminów ani kluczy.
- Nie dodano nowych pytań, ponieważ nie stwierdzono potwierdzonej luki programu.

## Testy

Lokalny checkout nie jest dostępny, a `git clone` nie rozwiązuje DNS. PR musi przejść pełny Quality Gate CI przed scaleniem. Aktualizacja dotyczy wyłącznie dokumentacyjnego indeksu i nie zastępuje przeglądu instruktorskiego ani prawnego.
