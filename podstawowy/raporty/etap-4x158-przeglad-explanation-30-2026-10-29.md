# Etap 4x158 — drugi przegląd explanation, partia 3 (29.10.2026)

## Zakres i metoda

Świeży main przed partią: `11745d8cf02404aa766654738a22c40d810b4a75`, bank 651 pytań (ADR-B-0001–0651). Wybrano 30 najkrótszych wyjaśnień spośród pominiętych w 4x156 i 4x157, omijając pytania stricte o kurs specjalistyczny cystern. Selekcja według długości, następnie ręczna redakcja ze znajomością treści pytania i A/B/C. Wszystkie nadal `needs_review`; redakcja nie oznacza weryfikacji prawnej specjalisty.

## Lista pytań, przed → po

| ID | Przed | Po — poprawa dydaktyczna |
|---|---|---|
| ADR-B-0023 | Klin: wyjaśnienie skrótowe | wyjaśniono dobór do masy i koła, odrzucono limit 7,5 t i dobór według klasy |
| ADR-B-0049 | Instrukcje: wyjaśnienie skrótowe | podkreślono przygotowanie przed trasą i błędność czytania po awarii |
| ADR-B-0050 | Język instrukcji: wyjaśnienie skrótowe | porównano zrozumiałość dla całej załogi z językiem nadawcy i kraju |
| ADR-B-0053 | Cyfra 8: wyjaśnienie skrótowe | wyjaśniono żrącość, niepromieniotwórczość i odczyt całego numeru |
| ADR-B-0056 | Klin: wyjaśnienie skrótowe | wyjaśniono funkcję klina i dlaczego znaki oraz pas nie blokują koła |
| ADR-B-0063 | Kod tunelowy: wyjaśnienie skrótowe | wyjaśniono kolumnę 15 i błędne kolumny 12/18 |
| ADR-B-0083 | Tunel E: wyjaśnienie skrótowe | odróżniono zakaz od godziny przejazdu i sposobu przewozu |
| ADR-B-0090 | Instrukcje w kabinie: wyjaśnienie skrótowe | wyjaśniono dostępność i zagrożenie pozostawienia ich w ładowni |
| ADR-B-0113 | Pomoc rannemu: wyjaśnienie skrótowe | wytłumaczono bezpieczeństwo ratownika i zagrożenie wtórne |
| ADR-B-0153 | Klasy 4.1 i 4.3: wyjaśnienie skrótowe | porównano mechanizmy zapłonu i reakcji z wodą |
| ADR-B-0222 | Pożar ładowni: wyjaśnienie skrótowe | wyjaśniono ryzyko gaszenia i otwierania opakowań |
| ADR-B-0234 | Cztery strony: wyjaśnienie skrótowe | odróżniono pełną instrukcję od firmowej notatki |
| ADR-B-0293 | Pasażer: wyjaśnienie skrótowe | wyjaśniono, czemu fotel i kamizelka nie dają prawa przewozu |
| ADR-B-0407 | Ochrona przed kradzieżą: wyjaśnienie skrótowe | wyjaśniono konieczność działania zabezpieczeń podczas przewozu |
| ADR-B-0414 | Tożsamość przewoźnika: wyjaśnienie skrótowe | odróżniono sprawdzenie przewoźnika od znajomości zlecenia |
| ADR-B-0416 | Dokument załogi: wyjaśnienie skrótowe | wyjaśniono indywidualny dokument ze zdjęciem |
| ADR-B-0438 | Prom: wyjaśnienie skrótowe | rozróżniono odcinek promowy od drogi przed i po nim |
| ADR-B-0443 | Sprzeczne konwencje: wyjaśnienie skrótowe | wyjaśniono zakres szczególnego pierwszeństwa zamiast dowolności |
| ADR-B-0461 | Znak środowiskowy: wyjaśnienie skrótowe | wyjaśniono warunek małego opakowania zamiast limitu 50 l |
| ADR-B-0474 | Kontrola przed załadunkiem: wyjaśnienie skrótowe | uzasadniono wstrzymanie załadunku i odrzucono argument pośpiechu |
| ADR-B-0477 | Odbiorca: wyjaśnienie skrótowe | wyjaśniono obowiązki odbiorcy mimo outsourcingu |
| ADR-B-0478 | Rozładowca: wyjaśnienie skrótowe | wyjaśniono, czemu odkażanie zewnętrzne nie usuwa obowiązków |
| ADR-B-0516 | Przygotowanie do jazdy: wyjaśnienie skrótowe | odrzucono krótką trasę i ustne streszczenie |
| ADR-B-0518 | Pasy: wyjaśnienie skrótowe | uzasadniono stabilność bez zgniatania opakowań |
| ADR-B-0562 | Nalepka dużego formatu: wyjaśnienie skrótowe | odrzucono dokument UN i dopisek nazwy jako zamienniki nalepki |
| ADR-B-0581 | Nadzór postoju: wyjaśnienie skrótowe | wyjaśniono, czemu polecenie dyspozytora nie znosi wymogu |
| ADR-B-0587 | Instrukcje przed jazdą: wyjaśnienie skrótowe | podkreślono samodzielne przygotowanie załogi |
| ADR-B-0592 | Zdarzenie w tunelu: wyjaśnienie skrótowe | wyjaśniono bezpieczne zatrzymanie i ryzyko otwierania ładowni |
| ADR-B-0597 | Ochrona dłoni i oczu: wyjaśnienie skrótowe | wyjaśniono różne funkcje wyposażenia |
| ADR-B-0602 | Tunel kategorii E: wyjaśnienie skrótowe | odrzucono argument krótszej drogi i poprawnych dokumentów |

## Zasady kontroli

Zmiany wyłącznie w polu `explanation` wybranych 30 rekordów; wszystkie pozostałe pola bez zmian, w tym klucz, A/B/C, sources i `verification_status`. Każde explanation: 2–5 zdań, 300–500 znaków (aktualny CI wymaga min. 300), najpierw praktyka, potem błędne odpowiedzi i na końcu ADR. Wskaźnik poprawnej najdłuższej odpowiedzi musi pozostać poniżej aktualnego progu CI 16% (surowszego niż cel 18%). Dokumenty pochodne (egzaminy, audyty, manifesty) należy zsynchronizować do nowego blobu banku; wymagany pełny PASS Quality Gate przed scaleniem. Nie przeprowadzono nowej literalnej recenzji ADR; podstawy prawne i status recenzji pozostają bez zmian.
