# Etap 4x50 — nowa próbka 60 explanation

- Data: 2026-10-26.
- Punkt wyjścia: świeży `main` po raporcie 4x49, commit `a9cd0ae0d45dd3d51e2a2fa70ea95dbd19a267bc`.
- Metoda do odtworzenia: wykluczono wszystkie ID wymienione w raportach 4x45, 4x46, 4x48 i 4x49, a następnie uszeregowano pozostałe pytania według deterministycznego wyniku `sin(numer_ID × 2026102650) × 10000`; wybrano pierwszych 60. To nowa próbka względem wcześniejszych list, ale nie zastępuje losowania z zatwierdzonym PRNG.
- Zakres: czytelność explanation dla początkującego; bez weryfikowania prawnego.

## Wynik

- Przeczytano 60 explanation razem z pytaniem, odpowiedziami A/B/C i podstawą ADR.
- **3 explanation przepisano** w celu usunięcia powtórzeń i niepasujących, niepomocnych uzasadnień.
- **57 pozostawiono bez zmian**: miały 3–5 zdań, 300+ znaków, podawały sens poprawnej odpowiedzi, wyjaśniały istotny błąd alternatywy i kończyły się podstawą ADR.
- Wszystkie pytania pozostają `needs_review`; żadne nie zostało oznaczone jako `verified`.

## Lista próbki

1. `ADR-B-0055` — bez zmiany; explanation zrozumiałe, 3–5 zdań, podstawa ADR i objaśnienie błędu
2. `ADR-B-0104` — bez zmiany; explanation zrozumiałe, 3–5 zdań, podstawa ADR i objaśnienie błędu
3. `ADR-B-0324` — bez zmiany; explanation zrozumiałe, 3–5 zdań, podstawa ADR i objaśnienie błędu
4. `ADR-B-0544` — bez zmiany; explanation zrozumiałe, 3–5 zdań, podstawa ADR i objaśnienie błędu
5. `ADR-B-0397` — bez zmiany; explanation zrozumiałe, 3–5 zdań, podstawa ADR i objaśnienie błędu
6. `ADR-B-0177` — bez zmiany; explanation zrozumiałe, 3–5 zdań, podstawa ADR i objaśnienie błędu
7. `ADR-B-0153` — bez zmiany; explanation zrozumiałe, 3–5 zdań, podstawa ADR i objaśnienie błędu
8. `ADR-B-0373` — **przepisano**
9. `ADR-B-0568` — bez zmiany; explanation zrozumiałe, 3–5 zdań, podstawa ADR i objaśnienie błędu
10. `ADR-B-0348` — bez zmiany; explanation zrozumiałe, 3–5 zdań, podstawa ADR i objaśnienie błędu
11. `ADR-B-0128` — bez zmiany; explanation zrozumiałe, 3–5 zdań, podstawa ADR i objaśnienie błędu
12. `ADR-B-0202` — **przepisano**
13. `ADR-B-0299` — **przepisano**
14. `ADR-B-0079` — bez zmiany; explanation zrozumiałe, 3–5 zdań, podstawa ADR i objaśnienie błędu
15. `ADR-B-0470` — bez zmiany; explanation zrozumiałe, 3–5 zdań, podstawa ADR i objaśnienie błędu
16. `ADR-B-0250` — bez zmiany; explanation zrozumiałe, 3–5 zdań, podstawa ADR i objaśnienie błędu
17. `ADR-B-0030` — bez zmiany; explanation zrozumiałe, 3–5 zdań, podstawa ADR i objaśnienie błędu
18. `ADR-B-0080` — bez zmiany; explanation zrozumiałe, 3–5 zdań, podstawa ADR i objaśnienie błędu
19. `ADR-B-0520` — bez zmiany; explanation zrozumiałe, 3–5 zdań, podstawa ADR i objaśnienie błędu
20. `ADR-B-0129` — bez zmiany; explanation zrozumiałe, 3–5 zdań, podstawa ADR i objaśnienie błędu
21. `ADR-B-0592` — bez zmiany; explanation zrozumiałe, 3–5 zdań, podstawa ADR i objaśnienie błędu
22. `ADR-B-0372` — bez zmiany; explanation zrozumiałe, 3–5 zdań, podstawa ADR i objaśnienie błędu
23. `ADR-B-0178` — bez zmiany; explanation zrozumiałe, 3–5 zdań, podstawa ADR i objaśnienie błędu
24. `ADR-B-0398` — bez zmiany; explanation zrozumiałe, 3–5 zdań, podstawa ADR i objaśnienie błędu
25. `ADR-B-0103` — bez zmiany; explanation zrozumiałe, 3–5 zdań, podstawa ADR i objaśnienie błędu
26. `ADR-B-0007` — bez zmiany; explanation zrozumiałe, 3–5 zdań, podstawa ADR i objaśnienie błędu
27. `ADR-B-0227` — bez zmiany; explanation zrozumiałe, 3–5 zdań, podstawa ADR i objaśnienie błędu
28. `ADR-B-0447` — bez zmiany; explanation zrozumiałe, 3–5 zdań, podstawa ADR i objaśnienie błędu
29. `ADR-B-0494` — bez zmiany; explanation zrozumiałe, 3–5 zdań, podstawa ADR i objaśnienie błędu
30. `ADR-B-0274` — bez zmiany; explanation zrozumiałe, 3–5 zdań, podstawa ADR i objaśnienie błędu
31. `ADR-B-0056` — bez zmiany; explanation zrozumiałe, 3–5 zdań, podstawa ADR i objaśnienie błędu
32. `ADR-B-0445` — bez zmiany; explanation zrozumiałe, 3–5 zdań, podstawa ADR i objaśnienie błędu
33. `ADR-B-0225` — bez zmiany; explanation zrozumiałe, 3–5 zdań, podstawa ADR i objaśnienie błędu
34. `ADR-B-0105` — bez zmiany; explanation zrozumiałe, 3–5 zdań, podstawa ADR i objaśnienie błędu
35. `ADR-B-0325` — bez zmiany; explanation zrozumiałe, 3–5 zdań, podstawa ADR i objaśnienie błędu
36. `ADR-B-0545` — bez zmiany; explanation zrozumiałe, 3–5 zdań, podstawa ADR i objaśnienie błędu
37. `ADR-B-0154` — bez zmiany; explanation zrozumiałe, 3–5 zdań, podstawa ADR i objaśnienie błędu
38. `ADR-B-0374` — bez zmiany; explanation zrozumiałe, 3–5 zdań, podstawa ADR i objaśnienie błędu
39. `ADR-B-0594` — bez zmiany; explanation zrozumiałe, 3–5 zdań, podstawa ADR i objaśnienie błędu
40. `ADR-B-0203` — bez zmiany; explanation zrozumiałe, 3–5 zdań, podstawa ADR i objaśnienie błędu
41. `ADR-B-0423` — bez zmiany; explanation zrozumiałe, 3–5 zdań, podstawa ADR i objaśnienie błędu
42. `ADR-B-0298` — bez zmiany; explanation zrozumiałe, 3–5 zdań, podstawa ADR i objaśnienie błędu
43. `ADR-B-0078` — bez zmiany; explanation zrozumiałe, 3–5 zdań, podstawa ADR i objaśnienie błędu
44. `ADR-B-0252` — bez zmiany; explanation zrozumiałe, 3–5 zdań, podstawa ADR i objaśnienie błędu
45. `ADR-B-0469` — bez zmiany; explanation zrozumiałe, 3–5 zdań, podstawa ADR i objaśnienie błędu
46. `ADR-B-0249` — bez zmiany; explanation zrozumiałe, 3–5 zdań, podstawa ADR i objaśnienie błędu
47. `ADR-B-0029` — bez zmiany; explanation zrozumiałe, 3–5 zdań, podstawa ADR i objaśnienie błędu
48. `ADR-B-0081` — bez zmiany; explanation zrozumiałe, 3–5 zdań, podstawa ADR i objaśnienie błędu
49. `ADR-B-0420` — bez zmiany; explanation zrozumiałe, 3–5 zdań, podstawa ADR i objaśnienie błędu
50. `ADR-B-0130` — bez zmiany; explanation zrozumiałe, 3–5 zdań, podstawa ADR i objaśnienie błędu
51. `ADR-B-0350` — bez zmiany; explanation zrozumiałe, 3–5 zdań, podstawa ADR i objaśnienie błędu
52. `ADR-B-0179` — bez zmiany; explanation zrozumiałe, 3–5 zdań, podstawa ADR i objaśnienie błędu
53. `ADR-B-0322` — bez zmiany; explanation zrozumiałe, 3–5 zdań, podstawa ADR i objaśnienie błędu
54. `ADR-B-0102` — bez zmiany; explanation zrozumiałe, 3–5 zdań, podstawa ADR i objaśnienie błędu
55. `ADR-B-0493` — bez zmiany; explanation zrozumiałe, 3–5 zdań, podstawa ADR i objaśnienie błędu
56. `ADR-B-0273` — bez zmiany; explanation zrozumiałe, 3–5 zdań, podstawa ADR i objaśnienie błędu
57. `ADR-B-0224` — bez zmiany; explanation zrozumiałe, 3–5 zdań, podstawa ADR i objaśnienie błędu
58. `ADR-B-0106` — bez zmiany; explanation zrozumiałe, 3–5 zdań, podstawa ADR i objaśnienie błędu
59. `ADR-B-0395` — bez zmiany; explanation zrozumiałe, 3–5 zdań, podstawa ADR i objaśnienie błędu
60. `ADR-B-0175` — bez zmiany; explanation zrozumiałe, 3–5 zdań, podstawa ADR i objaśnienie błędu

## Poprawki

| ID | Problem | Co zmieniono | Podstawa |
|---|---|---|---|
| ADR-B-0202 | Powtórzono, że faktura nie zastępuje dokumentu przewozowego; powtórzenie nie wnosiło nowej informacji. | Wyjaśniono różnicę między fakturą a dokumentem przewozowym oraz obowiązek kontroli przed załadunkiem. | ADR 7.5.1.2 |
| ADR-B-0299 | Dwa kolejne zdania powtarzały, że nalepki tylko na drzwiach nie wystarczają. | Wyjaśniono, które strony kontenera sprawdzić i że dokument nie zastępuje fizycznego oznakowania. | ADR 5.3.1.2 |
| ADR-B-0373 | Wyjaśnienie używało nieprzydatnych przykładów (wysokość pojazdu, daty faktur) zamiast wyjaśnić kryterium wspólnego przewozu. | Uporządkowano zasadę oddzielenia żywności/paszy od towarów niebezpiecznych i wskazano właściwy przepis. | ADR 1.4.3.1.1(e), 7.5.4 |

Nie zmieniono treści pytań, odpowiedzi, poprawnych liter ani numerów ID. Nie zmieniano statusów prawnych.

## Synchronizacja

Zaktualizowano snapshoty `review/sequential/` i `review/legal-clauses/` dla ID 0202, 0299 i 0373, klucz egzaminu 002, manifest pakietu specjalisty oraz indeks i README recenzji. Warianty 001–005 zawierają ID i kolejność pytań, a nie pełne explanation; kontrola synchronizacji nie wykazała potrzeby ich przestawiania. Nie zmieniono rozkładu poprawnych liter.

## Quality Gate — stan banku po zmianie

- 609 pytań; brak duplikatów ID.
- 609 `needs_review`, 0 `verified`.
- Explanation minimum 300 znaków; 0 poniżej 200.
- „Poprawna = jedyna najdłuższa”: 72/609 = 11,82% globalnie.

| Dział | Pytań | Jedyna najdłuższa | Wskaźnik |
|---|---:|---:|---:|
| B-01 | 45 | 6 | 13.33% |
| B-02 | 56 | 7 | 12.50% |
| B-03 | 49 | 7 | 14.29% |
| B-04 | 46 | 6 | 13.04% |
| B-05 | 43 | 5 | 11.63% |
| B-06 | 45 | 5 | 11.11% |
| B-07 | 48 | 6 | 12.50% |
| B-08 | 42 | 5 | 11.90% |
| B-09 | 46 | 4 | 8.70% |
| B-10 | 55 | 4 | 7.27% |
| B-11 | 43 | 6 | 13.95% |
| B-12 | 44 | 6 | 13.64% |
| B-13 | 47 | 5 | 10.64% |
| **Łącznie** | **609** | **72** | **11,82%** |

## Testy i ograniczenia

Lokalne testy nie są dostępne przez GitHub API; nie deklaruję ich wykonania. CI musi potwierdzić PASS dla pełnego zestawu testów. Korekty są redakcyjne i nie stanowią formalnej recenzji prawnej.


## CI: wykryte i naprawione rozbieżności migawki

Pierwsze przebiegi CI wykazały, że po zmianie explanation należało zaktualizować również `source_bank_head` w wariantach 001–005 i kluczach 001–005 oraz `current_bank_blob_sha`/`source_bank_blob_sha` w manifeście i obu kolejkach specjalisty. Wszystkie wskazane pola zsynchronizowano z blob SHA banku `626def46002cb4b065c402d0f30a9936ae30cf7d`. Końcowy wynik CI jest jeszcze wymagany przed scaleniem.

Dodatkowo CI wykrył dwa dokumenty instruktażowe specjalisty, które nie wskazywały nowego SHA: `review/specialist/INSTRUKCJA-RECENZJI.md` i `review/specialist/PRZEKAZANIE-ETAP4.md`. Dodano w nich krótką sekcję aktualnej migawki 4x50 i zachowano starsze aneksy jako historię. Po tej poprawce wymagany jest końcowy PASS CI.