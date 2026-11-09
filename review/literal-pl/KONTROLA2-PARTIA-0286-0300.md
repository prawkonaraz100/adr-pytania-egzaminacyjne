# Kontrola druga — ADR-B-0286–0300

**Wynik: 0 OK / 15 POPRAW / 0 BLOKUJ.** Wszystkie 15 rekordów zastąpiono nowymi tematami z tych samych kompetencji. Zachowano literę klucza, `module_id`, liczbę pytań w kompetencjach oraz `image: null`. Żaden rekord nie został oznaczony jako `verified`.

## Rozstrzygnięcia

- **0286 (09-K04, C):** zakaz nanoszenia innych oznaczeń ze strzałkami na opakowanie oznaczone strzałkami kierunkowymi (ADR 5.2.1.10.1 i 5.2.1.10.3, s. 938–939).
- **0287 (13-K06, A):** wpis „PRZEWÓZ ZGODNY Z 1.1.4.2.1” jest wymagany także przy korzystaniu z odstępstwa dla pakowania razem według IMDG (1.1.4.2.1 (b), s. 29–30; 5.4.1.1.7, s. 965).
- **0288 (02-K03, A):** ciecz o temperaturze zapłonu powyżej 60 °C przewożona w temperaturze równej lub wyższej od temperatury zapłonu należy do klasy 3, UN 3256 (2.2.3.1.1, s. 165; 2.2.9.3 M9, s. 293).
- **0289 (02-K09, B):** grupa pakowania III w klasie 6.1 oznacza materiał słabo trujący, ale nadal należący do klasy 6.1 (2.2.61.1.1, s. 214; 2.2.61.1.4, s. 215).
- **0290 (07-K05, C):** napełniający kontener do przewozu luzem zapewnia wymagane nalepki, znaki i tablice (1.2.1, s. 40; 1.4.3.3 (h), s. 58).
- **0291 (09-K01, B):** zakaz wspólnego załadunku LQ z materiałami wybuchowymi poza wskazanymi wyjątkami (7.5.2.4, s. 1307; 3.4.1 (g), s. 686).
- **0292 (09-K09, A):** zakaz przewozu luzem materiałów, które mogą przejść w stan ciekły (7.3.1.2, s. 1291).
- **0293 (07-K06, C):** jednostka transportowa przewożąca towary niebezpieczne może mieć najwyżej jedną przyczepę lub naczepę (8.1.1, s. 1324).
- **0294 (03-K02, A):** wyrazu „ODPAD” nie dodaje się ponownie, gdy już występuje w prawidłowej nazwie przewozowej, np. UN 3291 (5.4.1.1.3.1, s. 962–963; 2.2.62.1.11.2, uwaga 1, s. 232).
- **0295 (03-K05, B):** przy nalepce 7 instrukcje pisemne nakazują ograniczyć czas narażenia (5.4.3.4, s. 975 i 977).
- **0296 (04-K04, C):** flara z płomieniem jest źródłem zapłonu; do ostrzegania służą stojące znaki ostrzegawcze (5.4.3.4, s. 975; 8.1.5.2, s. 1325).
- **0297 (04-K05, A):** nalepka 6.2 oznacza zagrożenie zakażeniem; nie wolno dotykać uwolnionego materiału (5.4.3.4, s. 975 i 977).
- **0298 (06-K08, A):** numer 85 oznacza materiał żrący lub słabo żrący o działaniu utleniającym (5.3.2.3.1, s. 956; 5.3.2.3.2, s. 959).
- **0299 (06-K09, B):** duże nalepki na elastycznym kontenerze do przewozu luzem umieszcza się na dwóch przeciwległych bokach (5.3.1.2, s. 951).
- **0300 (12-K01, C):** praktykant jadący w celu szkolenia jest członkiem załogi i musi posiadać dokument z fotografią (1.2.1, s. 33; 1.10.1.4, s. 110).

## Korekty pierwszej kontroli i wady poprzednich wersji

Blokady **BLOKUJ** dla 0288 i 0289 uchylono: strona 946 była błędna. Wzór nalepki 3 znajduje się na stronie 945, a wzór nalepki 6.1 na stronie 947. Nowe rekordy nie pytają o wygląd tych nalepek.

Skorygowano numery stron: 1.4.3.2 – s. 57; 5.3.1.2 – s. 951; kod 80 z 5.3.2.3.2 – s. 959 (5.3.2.3.1 – s. 956); 5.4.1.1.3.1 – s. 962–963. W poprzednich wersjach klucz był jedyną najdłuższą odpowiedzią w 0287, 0292, 0293, 0295, 0296, 0297, 0298 i 0300; opcje przekraczały 80 znaków w 0290, 0292, 0295, 0296 i 0297.

## Stan po wdrożeniu

- Bank: 780 pytań; wszystkie `needs_review`, 0 `verified`.
- Kompetencje, moduły i klucze literowe: bez zmian.
- SHA blobu `podstawowy/questions.jsonl`: `1a173de4bd198c3e9c890e9813740e0ad1210dde`.
- Poprawna odpowiedź jako jedyna najdłuższa: **47/780 = 6,03%**; maksimum działu 11,24%.
- Licznik pytań bez porównania literalnego: **453**.
