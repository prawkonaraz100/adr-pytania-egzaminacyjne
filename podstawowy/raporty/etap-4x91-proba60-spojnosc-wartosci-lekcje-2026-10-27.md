# Etap 4x91 — próbka 60, spójność wartości ADR i odbiór lekcji B-01–B-05

- Data: 27.10.2026.
- Punkt wejścia: świeży `main`, `683cb2bea24214ac7ec5bbe7a1769784353d518d`.
- Zakres: wyłącznie kurs podstawowy ADR.
- Bank: blob `4a1a5d7f1ca8a5124eb096cd228aa92952fac6da`, 609 pytań ADR-B-0001–ADR-B-0609.

## 1. Stan Quality Gate i metryki

Ostatni workflow na wejściowym `main` zakończył się PASS: [Quality Gate run #40535870762](https://github.com/prawkonaraz100/adr-pytania-egzaminacyjne/actions/runs/40535870762).

| Kontrola | Wynik |
|---|---:|
| Rekordy / unikalne ID | 609 / 609 |
| Duplikaty ID | 0 |
| `needs_review` / `verified` | 609 / 0 |
| Najkrótsze explanation | 300 znaków |
| Explanation poniżej 200 znaków | 0 |
| Poprawna odpowiedź jako jedyna najdłuższa | 73/609 = 11,99% |
| Maksimum w pojedynczym dziale | 14,29% (B-02 i B-03) |

| Dział | Pytań | Poprawna jedyna najdłuższa | Wskaźnik |
|---|---:|---:|---:|
| B-01 | 45 | 6 | 13,33% |
| B-02 | 56 | 8 | 14,29% |
| B-03 | 49 | 7 | 14,29% |
| B-04 | 46 | 6 | 13,04% |
| B-05 | 43 | 5 | 11,63% |
| B-06 | 45 | 5 | 11,11% |
| B-07 | 48 | 6 | 12,50% |
| B-08 | 42 | 5 | 11,90% |
| B-09 | 46 | 4 | 8,70% |
| B-10 | 55 | 4 | 7,27% |
| B-11 | 43 | 6 | 13,95% |
| B-12 | 44 | 6 | 13,64% |
| B-13 | 47 | 5 | 10,64% |
| **Razem** | **609** | **73** | **11,99%** |

## 2. Próbka 60 explanation

- Seed: `2026102791`; PRNG LCG oraz Fisher–Yates.
- Pula po odjęciu ID występujących w dostępnych raportach 4x84, 4x85, 4x86, 4x87, 4x89 i 4x90: 297 rekordów; wylosowano 60.
- Ważne ograniczenie: raport 4x86 nie publikuje kompletnej listy wszystkich 60 ID z tamtej próbki. Dlatego nie można dowieść braku przecięcia z jego nieujawnioną częścią. Z puli usunięto wszystkie ID widoczne w dostępnych raportach, a ograniczenie pozostaje jawnie zapisane.
- Ręcznie sprawdzono pytanie, wszystkie trzy opcje, poprawną literę, explanation i wskazaną podstawę. Nie stwierdzono jednozdaniowych wyjaśnień, rozpoczęcia od samego numeru przepisu ani zdań dłuższych niż 35 słów. Explanation miały 301–431 znaków i 4–5 zdań według kontroli interpunkcji uwzględniającej kropki w numerach ADR.
- Potwierdzone poprawki: **0**. Nie zmieniono treści banku ani poprawnych liter.

### Lista sprawdzonych ID

```
ADR-B-0159, ADR-B-0036, ADR-B-0253, ADR-B-0264, ADR-B-0216,
ADR-B-0252, ADR-B-0296, ADR-B-0237, ADR-B-0223, ADR-B-0552,
ADR-B-0544, ADR-B-0055, ADR-B-0363, ADR-B-0095, ADR-B-0209,
ADR-B-0464, ADR-B-0441, ADR-B-0576, ADR-B-0559, ADR-B-0539,
ADR-B-0176, ADR-B-0229, ADR-B-0193, ADR-B-0561, ADR-B-0338,
ADR-B-0533, ADR-B-0248, ADR-B-0308, ADR-B-0203, ADR-B-0173,
ADR-B-0104, ADR-B-0377, ADR-B-0562, ADR-B-0429, ADR-B-0281,
ADR-B-0402, ADR-B-0325, ADR-B-0603, ADR-B-0370, ADR-B-0316,
ADR-B-0362, ADR-B-0490, ADR-B-0080, ADR-B-0058, ADR-B-0026,
ADR-B-0451, ADR-B-0314, ADR-B-0575, ADR-B-0152, ADR-B-0059,
ADR-B-0066, ADR-B-0471, ADR-B-0509, ADR-B-0004, ADR-B-0469,
ADR-B-0327, ADR-B-0517, ADR-B-0385, ADR-B-0155, ADR-B-0148
```

### Kandydaci heurystyki i fałszywe alarmy

Kontrola automatyczna zwróciła terminy, które mogą wyglądać na skróty niewyjaśnione. Ręczny przegląd nie potwierdził potrzeby zmiany:
- **ADR-B-0248** — wyjaśnienie rozróżnia kolumny 1, 7a i 15 tabeli A oraz rozwija LQ jako ilości ograniczone; numer UN jest opisany jako sposób znalezienia właściwego wpisu. W kontekście tego pytania nie zmienia to odpowiedzi ani nie powoduje niezrozumienia właściwej reguły.
- **ADR-B-0209** — LQ jest rozwinięte jako *limited quantities — ilości ograniczone*.
- **ADR-B-0281, ADR-B-0314 i ADR-B-0327** — numer UN jest objaśniony jako czterocyfrowy identyfikator towaru niebezpiecznego.
- **ADR-B-0036** — termin *security* jest wyjaśniony przez przeciwstawienie ochrony przewozu zwykłemu mocowaniu ładunku.

Wynik: 5 grup potencjalnych alarmów sprawdzonych ręcznie; 0 potwierdzonych problemów wymagających korekty. Nie zmieniono explanation wyłącznie po to, by dopasować je do heurystyki.

## 3. Kontrola wartości wrażliwych na zmianę ADR

Wykonano skryptowy spis wartości liczbowych i odwołań do przepisów z pytań każdego modułu oraz porównano je z odpowiednią lekcją. Dla scenariuszy sprawdzono powiązane `question_ids`, podstawy i pola strukturalne. Ręczny przegląd objął szczególnie wartości z rejestru 4x90 oraz ich reprezentatywne pytania i lekcje.

| Wartość / reguła | Miejsce porównania | Wynik |
|---|---|---|
| ADR 1.1.3.6 — próg 1000 i mnożnik kategorii 2 = 3, kategorii 3 = 1 | B-01, ADR-B-0570/0571, rejestr 4x90 | Zgodne: 100×3+600=900; 250×3+300=1050 |
| LQ — limit opakowania zewnętrznego 30 kg brutto, gdy ma zastosowanie | B-01, ADR-B-0605, scenariusz B-01 | Zgodne: przykład 32 kg przekracza limit; oznaczenie LQ samo nie zwalnia z warunków pakowania |
| EQ — limit liczby sztuk i wymagane warunki pakowania/oznakowania/dokumentacji | B-01, ADR-B-0572/0573 | Zgodne w kontrolowanym zakresie: 990 nie przekracza 1000, ale sama liczba nie potwierdza spełnienia wszystkich warunków |
| Znak środowiskowy na sztuce przesyłki — warunkowe 5 l / 5 kg | B-03 i pytania o 5 l, 6 l i 5 kg | Zgodne: limit nie zastępuje pozostałych warunków przepisu |
| Znak środowiskowy na jednostce transportowej — standard 250×250 mm; warunkowe zmniejszenie 100×100 mm dla określonej cysterny do 3000 l | B-03, ADR-B-0469 i pytania z działu B-03 | Zgodne w sprawdzonych rekordach; rozmiar zmniejszony jest wyjątkiem warunkowym, nie dowolnym wyborem |
| Tablica pomarańczowa — standard 400×300 mm, obrzeże 15 mm; w szczególnych warunkach 300×120 mm, obrzeże 10 mm | B-06, ADR-B-0018/0191/0258 | Zgodne między lekcją a bankiem |
| Gaśnice — 4 kg / 8 kg / 12 kg w zależności od DMC; odrębne minimum przy zastosowaniu 1.1.3.6 | B-08, ADR-B-0022/0071/0072/0073 | Zgodne między tabelą lekcji i sprawdzonymi pytaniami |
| Kody tunelowe D/E, zapis `(-)`, kod B1000C i granica 1000 kg netto | B-11, ADR-B-0033/0264/0490/0576/0603/0604 | Zgodne w sprawdzonych pytaniach i objaśnieniach |
| Świadectwo przyczepy — M364 | B-08/B-13, ADR-B-0145 i rejestr 4x88–4x90 | Bez zmiany. Według ostatniego odnotowanego źródła M364 jest ważna do 31.12.2026; przed użyciem materiału po tej dacie trzeba ponownie sprawdzić oficjalny wpis UNECE i polską publikację |

Nie stwierdzono potwierdzonej sprzeczności prawnej w powyższych porównaniach. To ukierunkowana kontrola wartości wrażliwych, nie niezależna opinia prawna o każdym rekordzie. Wartości niewystępujące w lekcji mogą być wyłącznie błędnymi opcjami lub przykładowymi danymi; nie uznano ich automatycznie za sprzeczność.

## 4. Odbiór lekcji B-01–B-05

| Lekcja | Pytań w module | ID w lekcji | Brakujące ID | Cel, przykłady, podsumowanie i odsyłacze |
|---|---:|---:|---:|---|
| B-01 | 45 | 45 | 0 | Obecne |
| B-02 | 56 | 56 | 0 | Obecne |
| B-03 | 49 | 49 | 0 | Obecne |
| B-04 | 46 | 46 | 0 | Obecne |
| B-05 | 43 | 43 | 0 | Obecne |
| **Razem** | **239** | **239** | **0** | **Referencje PASS** |

Przegląd potwierdził, że każda z tych lekcji ma jasne „Po co to jest?”, cele, przykłady z pracy kierowcy, scenariusze, sekcję „Co musisz zapamiętać”, pytania kontrolne i podstawę prawną. Wszystkie ID banku z modułów B-01–B-05 występują w odpowiedniej lekcji. Nie znaleziono konkretnego potwierdzonego błędu, który uzasadniałby zmianę treści w tej partii.

## 5. Scenariusze praktyczne

Skrypt sprawdził 39/39 scenariuszy:
- dokładnie 3 scenariusze na każdy z 13 modułów;
- po 4 kroki postępowania w każdym scenariuszu;
- brak nieistniejących lub obcych modułowo `question_ids`;
- każdy scenariusz ma podstawę prawną, typowe błędy i kryteria oceny.

Nie wykryto potwierdzonej rozbieżności w referencjach. Przegląd wartości liczbowych scenariuszy nie wykazał nowego konfliktu z odpowiednimi wpisami banku w kontrolowanych przypadkach.

## 6. Egzaminy próbne 001–005

Wszystkie arkusze i klucze zostały porównane z aktualnym bankiem. Nie zmieniono banku, więc nie było potrzeby regeneracji wariantów.

| Wariant | Pytania | Unikalne ID | Działy | A/B/C | Maks. seria | Zgodność klucza z treścią poprawnej opcji |
|---|---:|---:|---:|---|---:|---|
| 001 | 30 | 30 | 13 | 10/10/10 | 3 | PASS |
| 002 | 30 | 30 | 13 | 10/10/10 | 3 | PASS |
| 003 | 30 | 30 | 13 | 10/10/10 | 3 | PASS |
| 004 | 30 | 30 | 13 | 10/10/10 | 3 | PASS |
| 005 | 30 | 30 | 13 | 10/10/10 | 3 | PASS |

- Warianty i klucze wskazują aktualny blob banku `4a1a5d7f1ca8a5124eb096cd228aa92952fac6da`.
- Każdy wariant ma 30 unikalnych pytań, obejmuje 13 działów i nie ma powtórzeń ID w obrębie arkusza.
- W kluczach nie wykryto różnicy między wskazaną poprawną literą a treścią poprawnej odpowiedzi w arkuszu.
- Nie było zmian pytań ani explanation, więc nie trzeba było odświeżać snapshotów audytu ani pakietu recenzyjnego.

## 7. Testy i ograniczenia

Skryptowy preflight wykonano na plikach pobranych z GitHub: metryki banku, ID lekcji, referencje scenariuszy, synchronizacja wariantów i kluczy oraz kontrola wartości wskazanych w rejestrze 4x90. Nie deklaruję uruchomienia lokalnego zestawu testów Pythona, ponieważ dostępne połączenie nie udostępnia lokalnego checkoutu repozytorium. Warunkiem scalenia pozostaje PASS GitHub Actions Quality Gate dla tego PR.

Nie oznaczono żadnego pytania jako `verified`. Nie rozpoczęto kursu cystern ani innego kursu.
