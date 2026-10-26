# Etap 4x49 — raport zbiorczy przeglądu lekcji i próbki explanation

- Data: 2026-10-26.
- Punkt wyjścia: main po PR #495, `1248360df8dc6fc3b4f8325026d264b83714af51`.
- Ostatni commit tego etapu przed raportem: `b38155c369002192b320547eed71d98c2ad9f4fd`.
- Zakres: kurs podstawowy ADR; nie rozpoczęto kursu cystern ani innej specjalizacji.

## Stan banku i Quality Gate

| Kontrola | Wynik |
|---|---|
| Pytania | 609 |
| Duplikaty ID | 0 |
| Statusy | 609 `needs_review`, 0 `verified` |
| Poprawna odpowiedź jest jedyną najdłuższą | 72/609 = 11,82% |
| Najwyższy wskaźnik działu | 14,29% (B-03) |
| Najkrótsze explanation | 300 znaków |
| Explanation poniżej 200 znaków | 0 |
| Scenariusze | 39, po 3 na dział |
| Warianty egzaminu / klucze | 5 wariantów i 5 kluczy; nie zmieniono ich w tym etapie |

Stan początkowy potwierdzony przez PR #495: [Quality Gate PASS](https://github.com/prawkonaraz100/adr-pytania-egzaminacyjne/actions/runs/40353693368).

## Przegląd 13 lekcji

| Lekcje | Wynik kontroli | Potwierdzone poprawki |
|---|---|---|
| B-01–B-04 | Każda ma wprowadzenie „Po co to jest?”, podsumowanie, pytania kontrolne; wszystkie referencje do banku istnieją i są w module | 0 |
| B-05–B-08 | Każda ma wprowadzenie, podsumowanie, pytania kontrolne; terminy i odwołania sprawdzone, brak brakujących/międzydziałowych ID | 0 |
| B-09–B-13 | Struktura i ID sprawdzone; brak brakujących/międzydziałowych referencji | 2 poprawki językowe |

### Szczegóły poprawek

1. **B-10:** tautologiczne objaśnienie RID zastąpiono prostym opisem, że są to przepisy dla przewozu kolejowego. Zakres prawny bez zmian.
2. **B-12:** usunięto powtórzenie wyjaśnienia różnicy między ochroną przewozu a mocowaniem. Pozostawiono jedno zdanie kontrastujące cel obu działań (ADR 1.10 i 7.5.7).
3. CI początkowo wykrył brak linku do hasła „ADR” przy pierwszym użyciu w B-12. Dodano odsyłacz do kotwicy słowniczka na tej samej gałęzi; końcowy CI przeszedł.

### Liczba powiązań sprawdzonych w lekcjach

| Dział | Unikalne ID znalezione w pliku | Brakujące ID | ID z innego działu |
|---|---:|---:|---:|
| B-01 | 45 | 0 | 0 |
| B-02 | 56 | 0 | 0 |
| B-03 | 49 | 0 | 0 |
| B-04 | 46 | 0 | 0 |
| B-05 | 43 | 0 | 0 |
| B-06 | 45 | 0 | 0 |
| B-07 | 48 | 0 | 0 |
| B-08 | 42 | 0 | 0 |
| B-09 | 46 | 0 | 0 |
| B-10 | 55 | 0 | 0 |
| B-11 | 43 | 0 | 0 |
| B-12 | 44 | 0 | 0 |
| B-13 | 47 | 0 | 0 |

Liczby oznaczają unikalne identyfikatory znalezione w tekście lekcji, nie liczbę pytań w samym dziale. Przegląd struktury i referencji nie zastępuje formalnej recenzji prawnej.

## Próbka 60 explanation

- Seed: `2026102649`.
- Wybrano 60 ID spoza identyfikatorów wymienionych w raportach 4x45, 4x46 i 4x48.
- Wynik: 60 przeczytanych; 0 wymagało przepisania.
- Każde miało 3–5 zdań, 300+ znaków, wyjaśniało sens odpowiedzi i kluczowy błąd alternatyw oraz wskazywało podstawę ADR.
- Lista ID i szczegóły: `podstawowy/raporty/etap-4x49-przeglad-b01-04-proba60-2026-10-26.md`.
- Nie zmieniano banku, poprawnych liter, statusów ani kluczy egzaminów.

## Raporty cząstkowe

- `podstawowy/raporty/etap-4x49-przeglad-b01-04-proba60-2026-10-26.md`
- `podstawowy/raporty/etap-4x49-przeglad-b05-08-2026-10-26.md`
- `podstawowy/raporty/etap-4x49-przeglad-b09-13-2026-10-26.md`

## Status testów

- PR #496: Quality Gate PASS — [run #40361232536](https://github.com/prawkonaraz100/adr-pytania-egzaminacyjne/actions/runs/40361232536).
- PR #497: Quality Gate PASS — [run #40361570617](https://github.com/prawkonaraz100/adr-pytania-egzaminacyjne/actions/runs/40361570617).
- PR #498: końcowy Quality Gate PASS — [run #40361932596](https://github.com/prawkonaraz100/adr-pytania-egzaminacyjne/actions/runs/40361932596) i [run #40361923927](https://github.com/prawkonaraz100/adr-pytania-egzaminacyjne/actions/runs/40361923927).
- Lokalne testy nie były dostępne przez użyte połączenie GitHub API; nie deklarowano ich wykonania. CI uruchomiło pełny zestaw testów.

## Zastrzeżenia

Nie oznaczono żadnego pytania jako `verified`. Wnioski o czytelności są redakcyjne; kwestie niepewne prawnie pozostają dla specjalisty. Nie zmieniano wartości ani odpowiedzi bez potwierdzonego błędu i podstawy urzędowej.
