# Etap 4x6 — spójność materiałów instruktora B-01–B-04

Punkt wyjścia: świeży `main` `651d317ab45f302deb3edfb56cf868bd04586543`. Zakres: kurs podstawowy ADR.

## Zmiany

Uzupełniono materiały instruktora B-01–B-04 o prowadzenie wszystkich trzech scenariuszy z `podstawowy/praktyka/scenariusze-13-dzialow.json`, obserwowalne kryteria, typowe błędy z prostym wyjaśnieniem, granice bezpieczeństwa, powiązane ID pytań oraz pytania kontrolne na koniec zajęć.

| Dział | Scenariusze | Kompetencje z mapy | Pytania kontrolne | Kontrola ID |
|---|---|---|---|---|
| ADR-B-01 | SC-ADR-B-01, SC-ADR-B-01-02, SC-ADR-B-01-03 | ADR-B-01-K01, ADR-B-01-K02, ADR-B-01-K03, ADR-B-01-K04, ADR-B-01-K05, ADR-B-01-K06, ADR-B-01-K07 | ADR-B-0002, ADR-B-0259, ADR-B-0526, ADR-B-0570, ADR-B-0571, ADR-B-0572, ADR-B-0573, ADR-B-0595 | PASS — istnieją i należą do działu |
| ADR-B-02 | SC-ADR-B-02, SC-ADR-B-02-02, SC-ADR-B-02-03 | ADR-B-02-K01, ADR-B-02-K02, ADR-B-02-K03, ADR-B-02-K04, ADR-B-02-K05, ADR-B-02-K06, ADR-B-02-K07, ADR-B-02-K08, ADR-B-02-K09, ADR-B-02-K10, ADR-B-02-K11, ADR-B-02-K12, ADR-B-02-K13, ADR-B-02-K14 | ADR-B-0006, ADR-B-0510, ADR-B-0004, ADR-B-0005 | PASS — istnieją i należą do działu |
| ADR-B-03 | SC-ADR-B-03, SC-ADR-B-03-02, SC-ADR-B-03-03 | ADR-B-03-K01, ADR-B-03-K02, ADR-B-03-K03, ADR-B-03-K04, ADR-B-03-K05, ADR-B-03-K06 | ADR-B-0009, ADR-B-0514, ADR-B-0007, ADR-B-0008 | PASS — istnieją i należą do działu |
| ADR-B-04 | SC-ADR-B-04, SC-ADR-B-04-02, SC-ADR-B-04-03 | ADR-B-04-K01, ADR-B-04-K02, ADR-B-04-K03, ADR-B-04-K04, ADR-B-04-K05, ADR-B-04-K06 | ADR-B-0010, ADR-B-0012, ADR-B-0580, ADR-B-0581, ADR-B-0310, ADR-B-0347, ADR-B-0011 | PASS — istnieją i należą do działu |

## Typowe błędy i trudność pytań

Każdy scenariusz otrzymał wskazówki, czego instruktor ma słuchać i jak prostymi słowami wyjaśnić typowy błąd. Repo nie zawiera statystyk odpowiedzi kursantów; dlatego pytania wskazano jako kandydatów do dodatkowego omówienia na podstawie powiązania ze scenariuszami, nie jako empiryczny ranking trudności.

## Kontrola zgodności

- Liczba pytań w banku: 609; statusy: 609 `needs_review`, 0 `verified`.
- ID scenariuszy są pobrane z bieżącego pliku JSON; żadne ID pytań nie zostało zmienione.
- Podstawy i ID kompetencji zestawiono z `podstawowy/kompetencje.json` i odsyłaczami do lekcji. Nie poprawiano merytorycznych odniesień bez potwierdzonej rozbieżności w urzędowym tekście ADR.
- Testy lokalne nie zostały uruchomione w lokalnym checkoutie; zmiany należy weryfikować przez pełny CI Quality Gate przed scaleniem.
- Materiał nadal wymaga niezależnej recenzji prawnej i instruktorskiej.
