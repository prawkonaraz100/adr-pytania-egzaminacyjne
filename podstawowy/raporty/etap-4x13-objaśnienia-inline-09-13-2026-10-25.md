# Etap 4x13 — objaśnienia inline w lekcjach ADR-B-09–13

- Punkt wyjścia: świeży `main` po PR #349, commit `373d8b8fedc1329913b46533c7fb63be1be4eed0`.
- Zakres: B-09–B-13, domknięcie odsyłaczy pierwszego użycia w pozostałych lekcjach oraz blokujący test słowniczka.

## Zmiany w tej partii
- B-09: 6 odsyłaczy do haseł; wyjaśniono „przewóz luzem” prostym językiem i wskazano ADR 7.3.
- B-10: 4 odsyłacze; objaśniono transport kombinowany i uporządkowano różnicę ADR/RID/IMDG.
- B-11: 8 odsyłaczy; przy pierwszym użyciu objaśniono kod tunelowy D/E, instrukcje pisemne, LQ i tabelę A.
- B-12: 6 odsyłaczy; poprawiono zagnieżdżone nawiasy w objaśnieniu „security” i wyjaśniono plan ochrony oraz towary dużego ryzyka.
- B-13: 9 odsyłaczy; dodano wyjaśnienia dla numeru UN, dokumentu przewozowego, instrukcji pisemnych i dokumentów kierowcy/pojazdu.
- Naprawiono wadliwe odmiany „instrukcje pisemne” w B-03 i B-04 oraz domknięto brakujące kotwice pierwszego użycia w B-07/B-08/B-10.

## Przykłady przed → po
1. **B-09 — przewóz luzem**
   - Przed: „Przewóz luzem jest odrębnym sposobem przewozu i wymaga sprawdzenia, czy dany towar i pojazd są do tego dopuszczone.”
   - Po: „Przewóz luzem (przewóz bez osobnych sztuk przesyłek) wolno stosować tylko wtedy, gdy ADR dopuszcza go dla danego towaru i pojazdu. Przed załadunkiem sprawdź właściwy wpis i wymagania (ADR 7.3).”
2. **B-10 — transport kombinowany**
   - Przed: „Kontener może przebyć część trasy statkiem lub koleją, a następnie jechać drogą.”
   - Po: „W transporcie kombinowanym (jeden ładunek przewożony różnymi środkami transportu) kontener może część trasy pokonać statkiem lub koleją, a następnie ciężarówką.”
3. **B-11 — kategorie tuneli**
   - Przed: „Kategorie tuneli określają ograniczenia dla przewozu towarów niebezpiecznych. Kategorię wskazuje oznakowanie tunelu.”
   - Po: „Kategorie tuneli A–E wskazują, jakie przewozy mogą przez nie przejeżdżać. Kierowca porównuje kategorię z kodem tunelowym ładunku i nie wybiera tunelu objętego zakazem.”
4. **B-12 — ochrona przewozu**
   - Przed: „Ochrona przewozu (*security*) dotyczy zapobiegania kradzieży, sabotażowi i nieuprawnionemu dostępowi do towarów niebezpiecznych.”
   - Po: „Ochrona przewozu (security — zapobieganie kradzieży, sabotażowi i nieuprawnionemu dostępowi) ma ograniczać ryzyko przejęcia ładunku. To inne zadanie niż mocowanie, które zapobiega przesuwaniu się towaru podczas jazdy (ADR 1.10 i 7.5.7).”
5. **B-13 — dokument przewozowy**
   - Przed: „Sprawdź, czy dokument zawiera wymagane informacje dla konkretnego przewozu, m.in. oznaczenie UN przed numerem, właściwą nazwę przewozową, klasę i inne wymagane elementy opisu…”
   - Po: „Sprawdź, czy dokument zawiera wymagane dane dla konkretnego przewozu, w tym numer UN, właściwą nazwę przewozową, klasę i pozostałe wymagane informacje. Zestaw pól zależy od towaru, dlatego porównaj dokument z ADR 5.4.1.1.1 zamiast zakładać, że jedna lista pasuje do każdego ładunku.”

## Test CI
Zaktualizowano `tests/test_learner_glossary.py`: sprawdza obecność hasła i kotwicy w słowniczku, a dla każdego terminu z ustalonej listy — czy pierwsze wystąpienie w każdej lekcji ma link do kotwicy w tym samym akapicie lub elemencie listy. Test jest blokujący i uruchamia się przez `python -m unittest discover -s tests -v` w Quality Gate.

## Status banku
Bank i klucze egzaminów nie były zmieniane. Wszystkie 609 pytań pozostają `needs_review`; nie ustawiono `verified`. Minimalne explanation w banku: 300 znaków. Wskaźnik „poprawna = jedyna najdłuższa” pozostaje ≤16% w każdym dziale.
