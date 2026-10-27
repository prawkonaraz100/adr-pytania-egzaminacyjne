# Etap 4x96 — próbka 60 explanation, naprawa synchronizacji i integracja

- Data: 2026-10-27.
- Gałąź robocza: `stage4x96-sample60-integration-20261027`.
- Punkt bazowy: świeży `main` `65b521853dc6fd4986ba3277742b17a87d7507fc`.
- Bank po trzech potwierdzonych korektach dystraktorów: 609 rekordów, blob `445c2d76652f2dccf5735f928083388484e147bc`.

## 1. Próbka 60 — metoda i wynik

Zastosowano seed `2026102796`, LCG i Fisher–Yates. Z puli wykluczono wszystkie 541 unikalnych ID występujące jawnie w treści raportów 4x84–4x95. Pozostało 68 pytań; wybrano 60. Pełna lista wykluczeń i ID próbki znajduje się w `etap-4x96-wykluczenia-prob.json`.

Wszystkie 60 pytań przejrzano wraz z treścią, opcjami A/B/C, poprawną literą, explanation i wskazaną podstawą. Explanation miały 302–438 znaków, 3–5 zdań, zawierały podstawę ADR i wyjaśniały sens odpowiedzi poprawnej oraz błędy istotnych dystraktorów. **Nie znaleziono potwierdzonego błędu wymagającego zmiany**: 0 explanation przepisanych i 0 zmian prawnych z samej próbki. Nie poprawiano treści na wyczucie.

### Lista 60 ID

1. `ADR-B-0006` — ADR-B-02
2. `ADR-B-0337` — ADR-B-03
3. `ADR-B-0339` — ADR-B-03
4. `ADR-B-0017` — ADR-B-06
5. `ADR-B-0588` — ADR-B-13
6. `ADR-B-0009` — ADR-B-03
7. `ADR-B-0014` — ADR-B-05
8. `ADR-B-0407` — ADR-B-12
9. `ADR-B-0172` — ADR-B-09
10. `ADR-B-0545` — ADR-B-06
11. `ADR-B-0129` — ADR-B-03
12. `ADR-B-0226` — ADR-B-13
13. `ADR-B-0114` — ADR-B-06
14. `ADR-B-0491` — ADR-B-09
15. `ADR-B-0374` — ADR-B-07
16. `ADR-B-0455` — ADR-B-12
17. `ADR-B-0170` — ADR-B-06
18. `ADR-B-0607` — ADR-B-01
19. `ADR-B-0228` — ADR-B-13
20. `ADR-B-0183` — ADR-B-05
21. `ADR-B-0139` — ADR-B-09
22. `ADR-B-0328` — ADR-B-03
23. `ADR-B-0107` — ADR-B-05
24. `ADR-B-0532` — ADR-B-13
25. `ADR-B-0479` — ADR-B-07
26. `ADR-B-0302` — ADR-B-02
27. `ADR-B-0246` — ADR-B-07
28. `ADR-B-0482` — ADR-B-07
29. `ADR-B-0300` — ADR-B-12
30. `ADR-B-0110` — ADR-B-05
31. `ADR-B-0040` — ADR-B-01
32. `ADR-B-0599` — ADR-B-13
33. `ADR-B-0115` — ADR-B-06
34. `ADR-B-0137` — ADR-B-08
35. `ADR-B-0404` — ADR-B-12
36. `ADR-B-0519` — ADR-B-12
37. `ADR-B-0560` — ADR-B-09
38. `ADR-B-0265` — ADR-B-02
39. `ADR-B-0219` — ADR-B-05
40. `ADR-B-0204` — ADR-B-10
41. `ADR-B-0111` — ADR-B-05
42. `ADR-B-0592` — ADR-B-11
43. `ADR-B-0506` — ADR-B-06
44. `ADR-B-0600` — ADR-B-13
45. `ADR-B-0310` — ADR-B-04
46. `ADR-B-0546` — ADR-B-06
47. `ADR-B-0134` — ADR-B-07
48. `ADR-B-0589` — ADR-B-13
49. `ADR-B-0051` — ADR-B-06
50. `ADR-B-0016` — ADR-B-06
51. `ADR-B-0274` — ADR-B-12
52. `ADR-B-0405` — ADR-B-12
53. `ADR-B-0192` — ADR-B-06
54. `ADR-B-0092` — ADR-B-01
55. `ADR-B-0524` — ADR-B-13
56. `ADR-B-0347` — ADR-B-04
57. `ADR-B-0515` — ADR-B-04
58. `ADR-B-0123` — ADR-B-01
59. `ADR-B-0476` — ADR-B-04
60. `ADR-B-0133` — ADR-B-06

### Ograniczenie audytowe

Raport 4x86 sam stwierdza, że nie publikuje pełnej listy swoich 60 ID. Dlatego można potwierdzić, że próbka 4x96 nie zawiera żadnego ID jawnie wymienionego w raportach 4x84–4x95, ale nie można udowodnić braku przecięcia z nieujawnioną częścią próby 4x86. To ograniczenie zostało zapisane w pliku danych, zamiast deklarować niepotwierdzoną pełną niezależność.

## 2. Naprawa czerwonego CI

CI dla wcześniejszego SHA gałęzi wykazało 4 błędy w `tests/test_review_packet_integrity.py`. Bank zmienił blob z `7a2f4615e652f69d4079bf622098c8dd586c1ae1` na `445c2d76652f2dccf5735f928083388484e147bc`, ale pakiet recenzyjny nadal wskazywał stary snapshot.

Zaktualizowano ten sam hash w:
- `review/specialist/PAKIET-0609-MANIFEST.json` — w tym `current_bank_blob_sha`, `stage4x31.source_bank_blob_sha` i odnośniki do kolejek;
- `review/specialist/INSTRUKCJA-RECENZJI.md`;
- `review/specialist/PRZEKAZANIE-ETAP4.md`;
- `review/specialist/REJESTR-AKTUALNY-0001-0609.md`;
- `review/README.md`;
- `review/specialist/KOLEJKA-PRIORYTETOWA-4X40.json` i `KOLEJKA-PRIORYTETOWA-4X44.json`.

Warianty 001–005 i klucze 001–005 wskazują już bieżący blob banku. Sprawdzono też 30 pytań na wariant, 30 unikalnych ID, zgodność kolejności ID wariantu z kluczem, istnienie wszystkich ID w banku, 13 działów oraz rozkład liter A/B/C po 10 na wariant. Zmienione pytania `ADR-B-0290`, `ADR-B-0304` i `ADR-B-0364` nie występują w wariantach 001–005, więc nie wymagały zmiany treści arkuszy ani kluczy; ich metadane źródła zostały zsynchronizowane.

## 3. Quality Gate — kontrola statyczna przed PR

- Bank: 609 pytań, 609 unikalnych ID, duplikaty ID: 0.
- Statusy: 609 `needs_review`, 0 `verified`.
- Explanation: minimum 300 znaków; poniżej 200: 0.
- „Poprawna = jedyna najdłuższa”: 73/609 = 11.99% (limit 18%).
- Maksymalny dział: 14.29% (limit 18%).
- Warianty: 5 × 30 pytań; każdy A/B/C = 10/10/10, maksymalna seria tej samej litery nie przekracza 3 (zapisany test w CI kontroluje to).
- Migawka banku w manifeście i obu kolejkach recenzyjnych: `445c2d76652f2dccf5735f928083388484e147bc`.

To są kontrole danych przed CI, nie zastępują uruchomienia testów repozytorium. Wszystkie pytania pozostają `needs_review`; żadna nie została oznaczona `verified`.

## 4. Zmiany w pytaniach i podstawy

Trzy zmienione rekordy banku w gałęzi 4x96, wykryte przez porównanie z wejściowym `main`:
- `ADR-B-0092` — urealniono dystraktor dotyczący szkolenia i bezpośredniego nadzoru nad pracownikiem; ADR 1.3.1.
- `ADR-B-0137` — zastąpiono absurdalne dystraktory wiarygodnymi pomyłkami o zakresie obowiązku posiadania świadectwa dopuszczenia pojazdu; ADR 9.1.2.1 i 9.1.3.
- `ADR-B-0360` — poprawiono dystraktor dotyczący zakazu palenia w trakcie załadunku i rozładunku; ADR 8.3.5.

Poprawna litera nie została zmieniona. Odświeżono migawki audytu sekwencyjnego oraz audytu A/B/C w `review/legal-clauses/` dla tych trzech ID; zaktualizowano także racjonalizacje błędnych opcji. Te korekty nie zostały uznane za formalną weryfikację prawną.

## 5. Następny sensowny krok

Po scaleniu przeprowadzić audyt regresji całego kursu: pełna zgodność 609 pytań z 13 lekcjami, 39 scenariuszami, pięcioma wariantami i pakietem recenzyjnym, bez zmiany statusów prawnych bez specjalisty.
