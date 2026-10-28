# Etap 4x131 — spójność banku, lekcji, scenariuszy i egzaminu próbnego

- Punkt wyjścia: świeży `main` `f116d88aed6b1487a1f20f7dc8a204ee75d59d5f` (po PR #593 / etap 4x130).
- Zakres: wyłącznie kurs podstawowy ADR; bez zmiany statusów recenzji.
- Bank: 609 rekordów, 609 unikalnych ID; wszystkie `needs_review`, zero `verified`.

## 1. Spójność lekcji i banku

Skryptowo sprawdzono wszystkie 13 plików lekcji pod kątem odwołań do ID pytań:
- 13/13 lekcji istnieje.
- Wszystkie znalezione ID istnieją w banku.
- Nie wykryto odwołań do pytania przypisanego do innego działu.
- Nie stwierdzono podstaw do zmiany klucza ani treści odpowiedzi na podstawie samego audytu odwołań.

Kontrola referencji nie jest równoznaczna z literalną weryfikacją każdego twierdzenia prawnego. Wartości liczbowe i wyjątki ADR, które zależą od konkretnego wpisu towaru lub konfiguracji przewozu, pozostają do potwierdzenia w polskim tekście urzędowym przez specjalistę.

## 2. Przegląd pytań ADR-B-0586–0609

Przeczytano stem, wszystkie odpowiedzi A/B/C, klucz, explanation i wskazaną podstawę dla każdego z 24 pytań:

| ID | Dział | Wynik przeglądu |
|---|---|---|
| ADR-B-0586 | B-13 | Poprawiono potwierdzoną niespójność explanation: usunięto wzmiankę o telefonie dyspozytora, której nie odpowiadała żadna opcja; wyjaśnienie wskazuje teraz wprost, dlaczego mylą B i C. |
| ADR-B-0587 | B-13 | Wyjaśnienie odpowiada rozróżnieniu „instrukcje dostępne” vs. „załoga zna ich treść”; bez zmiany. |
| ADR-B-0588 | B-13 | Wyjaśnienie odróżnia dokumenty dostępne w pojeździe od dokumentów w archiwum/odbiorcy; bez zmiany. |
| ADR-B-0589 | B-13 | Wyjaśnia, dlaczego język instrukcji musi być zrozumiały; bez zmiany. |
| ADR-B-0590 | B-13 | Wyjaśnia dostępność instrukcji w kabinie; bez zmiany. |
| ADR-B-0591 | B-11 | Wyjaśnia kod tunelowy i ograniczenia trasy; bez zmiany. |
| ADR-B-0592 | B-11 | Wyjaśnia bezpieczną reakcję na zdarzenie w tunelu; bez zmiany. |
| ADR-B-0593 | B-05 | Wyjaśnia wyłączenie silnika w ramach instrukcji awaryjnych i wyjątku; bez zmiany. |
| ADR-B-0594 | B-05 | Wyjaśnia przekazywanie faktów zamiast przypuszczeń; bez zmiany. |
| ADR-B-0595 | B-01 | Wyjaśnia, że prywatny cel nie wystarcza bez spełnienia warunków wyłączenia; bez zmiany. |
| ADR-B-0596 | B-08 | Wyjaśnia indywidualne wyposażenie członków załogi i odmienną funkcję trójkąta; bez zmiany. |
| ADR-B-0597 | B-08 | Wyjaśnia, dlaczego latarka nie zastępuje ochrony dłoni i oczu; bez zmiany. |
| ADR-B-0598 | B-13 | Wyjaśnia różnicę między numerem UN, nazwą handlową i wymaganą nazwą przewozową; bez zmiany. |
| ADR-B-0599 | B-13 | Rozróżnia liczbę opakowań od ilości towaru; bez zmiany. |
| ADR-B-0600 | B-13 | Wyjaśnia rolę danych nadawcy i odbiorcy; bez zmiany. |
| ADR-B-0601 | B-13 | Wyjaśnia, dlaczego dokument morski nie zastępuje automatycznie wymagań drogowych; bez zmiany. |
| ADR-B-0602 | B-11 | Wyjaśnia, że krótsza trasa nie uchyla ograniczenia tunelowego; bez zmiany. |
| ADR-B-0603 | B-11 | Wyjaśnia znaczenie kodu „(-)” i zachowanie innych ograniczeń drogowych; bez zmiany. |
| ADR-B-0604 | B-11 | Wyjaśnia zastosowanie D/E dla przewozu w cysternie; bez zmiany. |
| ADR-B-0605 | B-01 | Wyjaśnia LQ, limit opakowania zewnętrznego i potrzebę sprawdzenia rodzaju opakowania; bez zmiany. |
| ADR-B-0606 | B-01 | Wyjaśnia kategorię transportową i obliczanie ilości dla 1.1.3.6; bez zmiany. |
| ADR-B-0607 | B-01 | Rozróżnia prawo jazdy od zaświadczenia ADR kierowcy; bez zmiany. |
| ADR-B-0608 | B-01 | Wyjaśnia, że dokument nie legalizuje zakazanego przewozu; bez zmiany. |
| ADR-B-0609 | B-01 | Wyjaśnia funkcję oznakowania LQ i dlaczego nie zastępuje go wpis na liście dostawy; bez zmiany. |

Zmiana wyłącznie redakcyjna: zachowano ID, poprawną literę, opcje i podstawę prawną ADR-B-0586. Explanation ma 333 znaki, 4 zdania i omawia oba błędne warianty. Odświeżono jego migawki w `review/sequential/586-597.json` oraz `review/legal-clauses/586-597.json`.

## 3. Scenariusze praktyczne

Sprawdzono strukturę i referencje wszystkich 39 scenariuszy w `podstawowy/praktyka/scenariusze-13-dzialow.json`:
- 3 scenariusze dla każdego z 13 działów;
- każdy scenariusz ma 4 kroki, pole typowych błędów, podstawy ADR, kryteria oceny i listę `question_ids`;
- 0 brakujących ID pytań;
- 0 ID przypisanych do niewłaściwego działu.

W tym etapie nie zmieniano scenariuszy, ponieważ kontrola strukturalna i powiązań nie wykazała potwierdzonego błędu wymagającego zmiany treści. Nie oznacza to niezależnego zatwierdzenia wszystkich podstaw prawnych.

## 4. Egzaminy próbne i klucze

Pytanie ADR-B-0586 występuje w wariancie 001 i kluczu 001. Zaktualizowano explanation w kluczu 001 oraz pole `source_bank_head` we wszystkich wariantach 001–005 i kluczach 001–005 do nowego bloba banku `30de3cb6e3990155bc5fd81437b404554fd95d9f`. Nie zmieniano zestawów pytań, kolejności opcji ani kluczy odpowiedzi.

## 5. Metryki i kontrola jakości

| Kontrola | Wynik |
|---|---:|
| Pytania w banku | 609 |
| Duplikaty ID | 0 |
| `needs_review` / `verified` | 609 / 0 |
| „Poprawna = jedyna najdłuższa” globalnie | 69/609 = 11,33% |
| Najwyższy wynik działu | B-11: 6/43 = 13,95% |
| Najkrótsze explanation w banku | 300 znaków |
| Explanation poniżej 200 znaków | 0 |
| Explanation przejrzane w tej partii | 24 |
| Explanation poprawione | 1 |
| Potwierdzone sprzeczności merytoryczne poprawione | 0 |
| Potwierdzone rozbieżności redakcyjne poprawione | 1 |
| Scenariusze sprawdzone | 39 |
| Brakujące / błędnie przypisane ID scenariuszy | 0 / 0 |

## Ograniczenia i dalsza recenzja

Kontrola spójności, czytelności i powiązań nie stanowi zatwierdzenia prawnego. Źródłem odniesienia pozostaje ADR 2025 (Dz.U. 2025 poz. 642) wraz ze sprostowaniem Dz.U. 2025 poz. 1575. Nie oznaczono żadnego pytania jako `verified`; niezależna recenzja specjalisty nadal jest wymagana.
