# Etap 4x159 — drugi przegląd explanation (partia 4)

Data: 29.10.2026. Świeży main: `fad2789e422352cfcdca391da728c215b585b6a8`. Zakres: wyłącznie kurs podstawowy ADR, bank 651 pytań do ADR-B-0651.

## Wynik

Wybrano kolejnych 30 najkrótszych wyjaśnień, niewystępujących w partiach 4x156–4x158, z pominięciem tematów wyłącznie kursu cystern. Poprawiono tylko pole `explanation`. Każde wyjaśnienie ma 2–5 zdań, co najmniej 300 i nie więcej niż 500 znaków, prosty sens praktyczny, odniesienie do mylących odpowiedzi i zwięzłą podstawę ADR. Nie zmieniono kluczy, A/B/C, źródeł ani `verification_status`.

## Wykaz poprawionych pytań — przed / po

| ID | Przed | Po — zmiana dla kursanta |
|---|---|---|
| ADR-B-0004 | Krótka definicja benzyny | Porównano klasę 3 z 8 i 6.2 oraz znaczenie zapalnych par |
| ADR-B-0005 | Definicja klasy 8 | Wyjaśniono żrącość i pomyłkę z promieniowaniem i zakażeniem |
| ADR-B-0045 | Znak środowiskowy | Rozdzielono znak opakowania od dokumentu i nalepki klasy 9 |
| ADR-B-0068 | Dane odbiorcy | Wyjaśniono, czemu kod pocztowy i spedytor nie zastępują adresu odbiorcy |
| ADR-B-0106 | Nawietrzność | Wyjaśniono praktyczne unikanie chmury i ryzyko strony zawietrznej |
| ADR-B-0128 | Kolumny tabeli A | Rozdzielono klasę w 3a, numer UN w 1 i grupę w 4 |
| ADR-B-0138 | Kontrola przed załadunkiem | Uzasadniono usunięcie niezgodności mimo krótkiej trasy |
| ADR-B-0143 | Pożar w tunelu | Wytłumaczono priorytet ewakuacji zamiast gaszenia ładowni |
| ADR-B-0156 | Utleniacze 5.1 | Wyjaśniono nasilanie pożaru i odróżnienie od klasy 7 |
| ADR-B-0175 | Dokumenty załogi | Wytłumaczono wymóg zdjęcia dla każdej osoby |
| ADR-B-0176 | Gaśnica | Rozdzielono plombę, badanie i datę przeglądu |
| ADR-B-0194 | Numer 88 | Wyjaśniono nasilenie działania żrącego i odrzucono pozostałe warianty |
| ADR-B-0211 | Podwykonawca | Wyjaśniono prawdziwą identyfikację przewoźnika przed wydaniem ładunku |
| ADR-B-0218 | Dwie nalepki | Rozdzielono zagrożenie główne/dodatkowe od dwóch towarów |
| ADR-B-0246 | Obowiązek odbiorcy | Wyjaśniono nieuzasadnioną zwłokę i problemy bezpieczeństwa |
| ADR-B-0263 | Kilka kodów tunelowych | Wyjaśniono najostrzejszy kod bez sugerowania się masą |
| ADR-B-0269 | Nalepka 4.3 | Wyjaśniono reakcję z wodą i różnicę względem 3 oraz 4.2 |
| ADR-B-0276 | Ryba i drzewo | Odróżniono znak środowiskowy od klasy 8 i tuneli |
| ADR-B-0285 | Informacje od nadawcy | Wyjaśniono, czemu dane firmy i pojazdu nie zastępują informacji o towarze |
| ADR-B-0288 | Nalepka klasy 3 | Porównano symbole 3, 2.3 i 5.1 |
| ADR-B-0312 | Definicja przewozu | Włączono postoje i pobyt towaru w pojeździe |
| ADR-B-0359 | Pracujący silnik | Wyjaśniono wyjątek przeładunkowy i błędność klimatyzacji |
| ADR-B-0411 | Szkolenie ochronne | Wyjaśniono potrzebę szkolenia przed obowiązkami i odświeżania |
| ADR-B-0459 | Próg zero | Wyjaśniono dodatnią ilość i zakres tabeli ochronnej |
| ADR-B-0476 | Kontrola rozładunku | Wyjaśniono wstrzymanie przy niezgodności i wyjątki |
| ADR-B-0485 | Maski ucieczkowe | Wyjaśniono maskę dla każdej osoby i brak wyjątku dla butli |
| ADR-B-0519 | Identyfikacja załogi | Wyjaśniono brak zastępowalności dowodu przez paszport kierowcy |
| ADR-B-0524 | Grupa pakowania | Rozdzielono opis dokumentu od numeru auta i instrukcji |
| ADR-B-0549 | Nalepka kontenera | Wyjaśniono standard ADR zamiast firmowej grafiki |
| ADR-B-0555 | Uszkodzone opakowanie | Wyjaśniono, czemu folia i pozycja załadunku nie naprawiają wycieku |

## Ograniczenia i kontrola

Niezależna recenzja prawna i porównanie z pełnym tekstem ADR 2025 pozostają do wykonania przez specjalistę. Każdy rekord pozostaje `needs_review`. Walidacja: integralność JSONL, zachowanie A/B/C, min. 300 znaków, 2–5 zdań, najdłuższa poprawna poniżej surowszego progu 16%, snapshoty audytu sekwencyjnego i klauzul, egzaminów 001–005 oraz pełny Quality Gate CI przed scaleniem. Nowych pytań nie dodawano, ponieważ praca dotyczyła istniejących explanation.
