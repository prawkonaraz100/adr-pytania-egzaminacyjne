# Kontrola uzupełniająca — integralność słowniczka kursanta

- Data: 2026-10-26.
- Punkt wyjścia: świeży `main` po PR #467, commit `699b08f7a5bb3685c839e00e360cf9efbab75cda`.
- Zakres: słowniczek kursanta i testy CI; wyłącznie kurs podstawowy.

## Znaleziony problem

Audyt kotwic wykazał 90 wierszy haseł, ale tylko 89 unikalnych identyfikatorów kotwic. Hasło „Jednostka transportowa” występowało dwa razy z identyczną kotwicą `jednostka-transportowa`. Powodowało to niejednoznaczne miejsce docelowe dla linków z lekcji.

## Poprawki

1. Scalono obie definicje „Jednostka transportowa” w jedną prostą definicję, zachowując znaczenie: pojazd silnikowy z połączoną przyczepą lub naczepą, oraz wyjaśnienie, dlaczego pojęcie ma znaczenie przy ilościach i wyposażeniu. Pozostawiono podstawę ADR 1.2.1.
2. Aby zachować kompletność słowniczka, dodano brakujące hasło „Nadawca” z prostym opisem roli i podstawą ADR 1.2.1 oraz 1.4.2.1.
3. Dodano blokujący test, który odrzuca powtarzające się identyfikatory kotwic i identyczne nagłówki haseł.
4. Dodano „Nadawca” do listy pojęć sprawdzanych przez test słowniczka.

## Wynik po zmianach

- Hasła: 90 wierszy, 90 unikalnych kotwic.
- Powtarzające się kotwice: 0.
- Powtarzające się identyczne nagłówki: 0.
- Pytania banku, klucze egzaminów i statusy weryfikacji: bez zmian.
- Wszystkie pytania pozostają `needs_review`; nie nadano `verified`.

## Kontrola

Testy uruchamia CI w PR. Nie zmieniano żadnej podstawy prawnej ani odpowiedzi egzaminacyjnej; poprawka dotyczyła wyłącznie nawigacji i definicji słowniczkowej.
