# Etap 4x46 — przegląd 60 explanation, lekcji i synchronizacja pakietu

- Data: 26.10.2026; kurs podstawowy ADR.
- Sprawdzony świeży `main`: `c9113b1d9a85d2f1d919696ed6b87aab4532f334` (scalony PR #488, etap 4x45).
- Deterministyczna próbka: **seed 2026102646**, PRNG LCG `state = (1664525 * state + 1013904223) mod 2^32`, Fisher–Yates na ID banku w kolejności JSONL po usunięciu całej próbki 40 ID z 4x45.
- Oceniono wszystkie 60 explanation jako początkujący kursant, wraz z błędnymi odpowiedziami i wskazaniem punktu ADR. **8 przepisano**, 52 pozostawiono bez zmian. Nie zmieniano kluczy, dystraktorów, działów ani statusów prawnych.

## Lista 60 ID — próba w kolejności losowania

1. `ADR-B-0236` — bez zmiany
2. `ADR-B-0479` — bez zmiany
3. `ADR-B-0152` — bez zmiany
4. `ADR-B-0341` — przepisano
5. `ADR-B-0310` — bez zmiany
6. `ADR-B-0501` — bez zmiany
7. `ADR-B-0474` — bez zmiany
8. `ADR-B-0246` — bez zmiany
9. `ADR-B-0607` — bez zmiany
10. `ADR-B-0166` — bez zmiany
11. `ADR-B-0258` — bez zmiany
12. `ADR-B-0504` — przepisano
13. `ADR-B-0342` — bez zmiany
14. `ADR-B-0450` — przepisano
15. `ADR-B-0228` — bez zmiany
16. `ADR-B-0459` — bez zmiany
17. `ADR-B-0200` — przepisano
18. `ADR-B-0433` — bez zmiany
19. `ADR-B-0363` — przepisano
20. `ADR-B-0229` — bez zmiany
21. `ADR-B-0067` — bez zmiany
22. `ADR-B-0139` — przepisano
23. `ADR-B-0090` — bez zmiany
24. `ADR-B-0088` — bez zmiany
25. `ADR-B-0121` — bez zmiany
26. `ADR-B-0332` — bez zmiany
27. `ADR-B-0524` — bez zmiany
28. `ADR-B-0084` — bez zmiany
29. `ADR-B-0278` — bez zmiany
30. `ADR-B-0211` — bez zmiany
31. `ADR-B-0052` — bez zmiany
32. `ADR-B-0383` — bez zmiany
33. `ADR-B-0527` — bez zmiany
34. `ADR-B-0277` — bez zmiany
35. `ADR-B-0486` — bez zmiany
36. `ADR-B-0114` — bez zmiany
37. `ADR-B-0259` — bez zmiany
38. `ADR-B-0384` — przepisano
39. `ADR-B-0193` — bez zmiany
40. `ADR-B-0404` — bez zmiany
41. `ADR-B-0238` — bez zmiany
42. `ADR-B-0509` — bez zmiany
43. `ADR-B-0480` — bez zmiany
44. `ADR-B-0538` — bez zmiany
45. `ADR-B-0439` — bez zmiany
46. `ADR-B-0314` — bez zmiany
47. `ADR-B-0596` — bez zmiany
48. `ADR-B-0100` — bez zmiany
49. `ADR-B-0347` — bez zmiany
50. `ADR-B-0240` — bez zmiany
51. `ADR-B-0036` — bez zmiany
52. `ADR-B-0115` — bez zmiany
53. `ADR-B-0134` — bez zmiany
54. `ADR-B-0232` — bez zmiany
55. `ADR-B-0519` — bez zmiany
56. `ADR-B-0289` — bez zmiany
57. `ADR-B-0261` — bez zmiany
58. `ADR-B-0422` — przepisano
59. `ADR-B-0136` — bez zmiany
60. `ADR-B-0057` — bez zmiany

## Poprawki redakcyjne

| ID | Dlaczego zmieniono explanation | Zakres |
|---|---|---|
| ADR-B-0504 | Usunięto dwukrotne wyjaśnianie cyfry 5; osobno objaśniono zakaźność i ciśnienie gazu. | 4–5 zdań, 333 znaków; dotychczasowy klucz i podstawa ADR zachowane |
| ADR-B-0363 | Połączono powtórzone zdania o protokole i czasie postoju; wskazano konkretną czynność przewoźnika. | 4–5 zdań, 330 znaków; dotychczasowy klucz i podstawa ADR zachowane |
| ADR-B-0384 | Usunięto powtórzenie obowiązku tablic; objaśniono IMDG i błędne zastąpienie tablic etykietą spedytora. | 4–5 zdań, 363 znaków; dotychczasowy klucz i podstawa ADR zachowane |
| ADR-B-0422 | Usunięto dwukrotne powtarzanie, że wygląd obudowy nie zastępuje kontroli. | 4–5 zdań, 291 znaków; dotychczasowy klucz i podstawa ADR zachowane |
| ADR-B-0200 | Usunięto powtórzenie mocowania ciężkiej maszyny, doprecyzowano dlaczego ustawienie przy ścianie nie wystarczy. | 4–5 zdań, 350 znaków; dotychczasowy klucz i podstawa ADR zachowane |
| ADR-B-0450 | Objaśniono skrót DOT i rozróżniono oznaczenie ADR od znaku sprzedawcy oraz regulaminu promu. | 4–5 zdań, 374 znaków; dotychczasowy klucz i podstawa ADR zachowane |
| ADR-B-0139 | Wyjaśniono kody BK i VC zamiast pozostawiać je bez kontekstu. | 4–5 zdań, 379 znaków; dotychczasowy klucz i podstawa ADR zachowane |
| ADR-B-0341 | Uproszczono pojęcie numeru UN i wyjaśniono osobno, czemu kierowca ani magazynier nie mogą zgadywać. | 4–5 zdań, 379 znaków; dotychczasowy klucz i podstawa ADR zachowane |

Pozostałe 52 wyjaśnienia mają czytelny sens poprawnej odpowiedzi, omawiają błędne możliwości i podają odwołanie do ADR w stopniu wystarczającym do pozostawienia bez zmian redakcyjnych; to nie stanowi formalnego zatwierdzenia prawnego.

## 13 lekcji i scenariusze — kontrola strukturalna po etapach 4x42–4x45

Sprawdzono wszystkie pliki `podstawowy/lekcje/ADR-B-01.md` … `ADR-B-13.md` pod kątem obecności „Co musisz zapamiętać”, „Scenariusze praktyczne”, „Sprawdź się” oraz ID przypisanych do właściwego działu. **13/13** zachowuje wszystkie trzy sekcje, komplet powiązań do pytań swojego działu, bez ID nieistniejących lub z innego modułu. Zestaw `scenariusze-13-dzialow.json`: **39 scenariuszy**, brak odwołań do nieistniejących ID lub obcych działów. Nie wykryto potwierdzonego problemu powiązań wymagającego zmiany lekcji. Kontrola numerów i linków nie zastępuje pełnej prawnej weryfikacji treści scenariuszy.

**Nowe pytania:** nie dodano. W wykonanej próbce i kontroli powiązań nie wykryto potwierdzonej luki wymagającej nowego ID; nie jest to dowód wyczerpania programu ADR.

## Egzaminy i pakiet recenzenta

- Przeliczono pięć arkuszy i kluczy 001–005 według świeżego banku `questions.jsonl` (blob SHA `15fd07c36cd05fb59222fa6f15e4693d1d6a2664`).
- Poprawne litery i explanation w kluczach odpowiadają aktualnym pytaniom; brak nieznanych ID. Wszystkie warianty zachowują status treningowy `publication_authorized=false`.
- Zaktualizowano manifest, źródłowe SHA w obu kolejkach 4x40/4x44, bieżący rejestr i instrukcje przekazania. **376 nierozstrzygniętych porównań literalnych** pozostaje otwartych; nie traktowano kolejki jako potwierdzenia prawnego.

## Kontrole przed PR

- Bank: 609 unikatowych ID, **609 `needs_review`**, 0 `verified`.
- Explanation: minimum **300 znaków**; osiem nowych tekstów ma 300–406 znaków i 4–5 zdań.
- Wskaźnik „poprawna = jedyna najdłuższa”: **72/609 = 11,82%** globalnie, maksimum działu **14,29%**, limit 18%.
- Formalne porównanie z polskim tekstem ADR 2025 (Dz.U. 2025 poz. 642 i sprostowanie poz. 1575) pozostaje zadaniem niezależnego specjalisty.

## Dalsza luka jakości

W następnej partii warto zweryfikować pod kątem dydaktyki **powtarzające się schematy odpowiedzi w egzaminie** oraz krótkie automatyczne uzasadnienia w pozostałych 549 pytaniach spoza tej próby, bez ruszania niepotwierdzonych rozstrzygnięć prawnych.

## Naprawy po pierwszym przebiegu CI

Pierwsze uruchomienia Quality Gate wykryły: za krótkie explanation ADR-B-0422, pominięcie odwołania ADR 7.3.2 w ADR-B-0139, niezsynchronizowane `review/README.md` oraz zaburzenie rozkładu A/B/C po błędnym przywróceniu kolejności odpowiedzi z banku w wariantach treningowych. Przywrócono oryginalne permutacje pięciu wariantów i poprawne litery ich kluczy; zaktualizowano tylko treści explanation, migawkę banku i pozostałe wskazania. Nie zmieniono odpowiedzi źródłowych. Dodatkowo zaktualizowano dokładne snapshoty ośmiu zmienionych explanation w plikach `review/sequential/*.json` i `review/legal-clauses/*.json`, zachowując statusy `needs_review` i brak formalnych zatwierdzeń.
