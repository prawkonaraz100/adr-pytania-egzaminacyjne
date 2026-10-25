# ETAP 4x9 — raport końcowy kontroli spójności i odporności na zmiany ADR

Data: 25.10.2026. Wykonano wyłącznie na kursie podstawowym ADR, przez GitHub i Quality Gate CI. Zakres bazowy: **609 pytań w 13 działach**, bez zmiany numeracji.

## Partie i rezultaty

| Zakres | PR | Rekordów | Zmiany |
|---|---|---:|---|
| B-01–04 | [#335](https://github.com/prawkonaraz100/adr-pytania-egzaminacyjne/pull/335) | 196 | Realistyczne dystraktory 0003, 0012, 0265; nowe explanation 0265; audyty i odpowiednie warianty zsynchronizowane |
| B-05–08 | [#336](https://github.com/prawkonaraz100/adr-pytania-egzaminacyjne/pull/336) | 178 | Uzupełniono brakujące w lekcjach wymiary tablic (B-06) oraz minimalne gaśnice według DMC (B-08), bank bez zmian |
| B-09–13 | [#337](https://github.com/prawkonaraz100/adr-pytania-egzaminacyjne/pull/337) | 235 | Poprawiono jedną błędną opcję 0086 (B-11); aktualizacja audytów i metryk |

**Wynik:** potwierdzonych sprzeczności prawnych wymagających zmiany poprawnej odpowiedzi: **0**; potwierdzone braki ilościowe w treści podręcznika: **2** (B-06, B-08), uzupełnione; poprawione dystraktory: **5 w 4 pytaniach**; poprawione explanation: **1**. Zmiany opcji dotyczyły typowych błędnych interpretacji, bez zmiany sensu ani poprawnej litery. Nie przeprowadzono niezależnej literalnej recenzji prawnej całych 609 rekordów; wynik 0 nie oznacza braku wszystkich rzeczywistych sprzeczności.

## Metryki po zmianach

| Dział | Pytania | Poprawna = jedyna najdłuższa | Wskaźnik | A/B/C |
|---|---:|---:|---:|---|
| ADR-B-01 | 45 | 7 | 15.56% | 17/17/11 |
| ADR-B-02 | 56 | 8 | 14.29% | 21/19/16 |
| ADR-B-03 | 49 | 7 | 14.29% | 16/21/12 |
| ADR-B-04 | 46 | 7 | 15.22% | 15/18/13 |
| ADR-B-05 | 43 | 6 | 13.95% | 18/14/11 |
| ADR-B-06 | 45 | 5 | 11.11% | 16/14/15 |
| ADR-B-07 | 48 | 6 | 12.50% | 18/18/12 |
| ADR-B-08 | 42 | 6 | 14.29% | 12/12/18 |
| ADR-B-09 | 46 | 4 | 8.70% | 13/15/18 |
| ADR-B-10 | 55 | 4 | 7.27% | 19/18/18 |
| ADR-B-11 | 43 | 6 | 13.95% | 11/13/19 |
| ADR-B-12 | 44 | 7 | 15.91% | 14/13/17 |
| ADR-B-13 | 47 | 4 | 8.51% | 15/15/17 |

Łącznie **77/609 = 12.64%** — poniżej progu 18%. Każdy dział jest **≤16%**. Minimalna długość explanation: 300 znaków, brak poniżej 200. Status: 609 `needs_review`, 0 `verified`.

## Wrażliwość na edycję ADR 2027

Powstały trzy rejestry, w sumie **258 flag (258 odrębnych ID)**:
- [B-01–04](etap-4x9-wrazliwosc-01-04.json) — 100 ID
- [B-05–08](etap-4x9-wrazliwosc-05-08.json) — 42 ID
- [B-09–13](etap-4x9-wrazliwosc-09-13.json) — 116 ID

Reguły wskazują ryzyka związane z liczbami, wymiarami, progami, kodami tunelowymi, klasami, wyposażeniem, dokumentami i rolami. Wiele flag jest szerokich — **nie oznaczają zmian w 2027**, a brak flagi nie daje gwarancji braku wpływu przyszłych przepisów. [Lista kontrolna specjalisty](../../review/specialist/ETAP-4X9-ADR-2027-LISTA-KONTROLNA.md) określa, co trzeba porównać w urzędowych tekstach wraz z A/B/C.

## Egzaminy próbne 001–005

Sprawdzono liczbę pytań (po 30), unikalność ID i zgodność poprawnych liter z bankiem. Rozkład A/B/C:
- 001: **16/5/9**, najdłuższa seria tej samej litery 4.
- 002: **10/11/9**, seria 4.
- 003: **8/14/8**, seria 3.
- 004: **9/10/11**, seria 3.
- 005: **10/10/10**, seria 4.

Wariant 001 jest nierównomierny. Zmiana samej kolejności pytań **nie zmienia częstości liter**; wymagałaby zmiany doboru pytań lub kolejności odpowiedzi w arkuszu wraz z kluczem, więc obecnego deterministycznego wariantu nie przestawiano bez osobnego sprawdzenia generatora i skutków dla testów. Klucze nie zmieniły poprawnych liter.

## Bramka i ograniczenia

Każda partia przeszła Quality Gate po naprawieniu błędów synchronizacji metryk w README / wyjaśnienia. Końcowe formalne zatwierdzenie wymaga literalnego porównania z polskim ADR 2025, sprostowaniem, a następnie przyszłą oficjalną edycją. **Nie zmieniono żadnego pytania na `verified` i nie rozpoczęto kursu cystern.**
