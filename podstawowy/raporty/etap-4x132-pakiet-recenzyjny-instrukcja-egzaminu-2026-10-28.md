# Etap 4x132 — aktualizacja pakietu recenzyjnego i instrukcji egzaminu próbnego

- Punkt wyjścia: świeży `main` po scaleniu PR #594, commit `e32fccb78cb928c6d44b6e4fcbdcd4a0d541470e`.
- Zakres: wyłącznie kurs podstawowy ADR.
- Bieżący bank: 609 pytań `ADR-B-0001–ADR-B-0609`; wszystkie `needs_review`, 0 `verified`, 0 formalnych zatwierdzeń.
- Bieżący blob banku: `595d47e4f7a15cc93a5c42cd8285d153529f906c`.

## 1. Aktualny pakiet dla specjalisty

Zaktualizowano bieżącą migawkę i opis zakresu w manifeście `review/specialist/PAKIET-0609-MANIFEST.json`, indeksach recenzji i przekazaniu. Pakiet opisuje aktualny stan:
- 609 pytań w 13 działach; 609 `needs_review`, 0 `verified`;
- 13 lekcji i 13 materiałów instruktorskich;
- 39 scenariuszy praktycznych, po 3 na dział;
- 5 wariantów egzaminu próbnego i 5 kluczy;
- 90 haseł w słowniczku;
- 10 grafik ADR wymienionych w manifeście do porównania ze wzorem źródłowym;
- raport 4x131 i nowa instrukcja egzaminu próbnego.

Pakiet nie jest akceptacją prawną. Wszystkie pytania nadal wymagają niezależnej recenzji. Rejestr dowodów wskazuje:
- 376 pytań, dla których pełny tekst właściwego polskiego przepisu nie został pobrany i porównany dosłownie;
- 10 pytań, dla których źródło sprawdzono, ale pełne porównanie literalne nadal oczekuje;
- 223 pytania porównane z kopią polskiego tekstu opublikowaną przez Ministerstwo, ale mapowanie do właściwego fragmentu Dziennika Ustaw i niezależna recenzja specjalisty nadal oczekują;
- 291 wpisów z wynikiem kontroli celowanej — to nie jest 291 zatwierdzeń.

### Lista kontrolna specjalisty

1. Dla każdego z 609 pytań sprawdzić treść pytania, wszystkie odpowiedzi A/B/C, klucz, explanation oraz wskazany punkt w polskim tekście ADR 2025, Dz.U. 2025 poz. 642, wraz ze sprostowaniem Dz.U. 2025 poz. 1575.
2. Zapisać dokładny plik/stronę i fragment źródła, rozstrzygnąć niejednoznaczności oraz uzasadnić każdą zmianę klucza.
3. Sprawdzić 13 lekcji i 13 materiałów instruktorskich w powiązaniu z 39 scenariuszami i ID pytań; szczególną uwagę zwrócić na liczby, progi, wyjątki i wymagania zależne od konkretnego wpisu w tabeli A.
4. Sprawdzić 5 wariantów i 5 kluczy względem aktualnego banku, w tym treść opcji po ewentualnym przestawieniu liter, wyjaśnienia, podstawy ADR i ścieżki lekcji.
5. Porównać 10 grafik wskazanych w manifeście z odpowiednimi wzorami ADR i potwierdzić, że żadna ilustracja nie sugeruje błędnego oznakowania.
6. Przejrzeć rejestr zmian potencjalnie wrażliwych na kolejną edycję ADR 2027: progi i limity ilościowe, kody tunelowe, wymiary/układ oznakowania, wyposażenie, terminy badań/ważności i wyjątki. Nie aktualizować wartości wyłącznie na podstawie projektu lub przypuszczenia; wymagać formalnego tekstu i wskazania daty wejścia w życie.
7. Dopiero po wykonaniu recenzji zapisać rzeczywistego recenzenta, datę, dowody i hash; nie nadawać `verified` bez formalnego protokołu.

## 2. Instrukcja dla kursanta do egzaminu próbnego

Dodano `podstawowy/egzamin-probny/INSTRUKCJA-KURSANTA.md` i podlinkowano ją w README egzaminów.

Potwierdzone parametry egzaminu podstawowego:
- 30 pytań jednokrotnego wyboru, po trzy możliwe odpowiedzi — rozporządzenie Ministra Infrastruktury z 26 czerwca 2024 r., Dz.U. 2024 poz. 964, § 9 ust. 1 i 3 pkt 1;
- 60 minut — § 10 pkt 1;
- co najmniej 2/3 poprawnych odpowiedzi — § 11, czyli 20 z 30.

Źródło urzędowe: [ELI — Dz.U. 2024 poz. 964, akt o statusie „obowiązujący”](https://eli.gov.pl/eli/DU/2024/964/ogl).

Instrukcja rozróżnia oficjalne parametry od statusu naszego narzędzia: warianty 001–005 pozostają wewnętrznymi arkuszami treningowymi, a nie oficjalnym katalogiem egzaminacyjnym. Wynik 20/30 jest progiem porównawczym do samodzielnej nauki i nie stanowi formalnego zdania egzaminu ani przyznania uprawnień.

Instrukcja opisuje również liczenie wyniku, sposób korzystania z explanation, powrót do właściwej lekcji i słowniczka oraz ćwiczenie powiązanego scenariusza.

## 3. Stan po etapach 4x131–4x132

| Kontrola | Wynik |
|---|---:|
| Pytania | 609 |
| `needs_review` / `verified` | 609 / 0 |
| „Poprawna = jedyna najdłuższa” | 69/609 = 11,33% |
| Maksimum działu | 13,95% |
| Minimum explanation | 300 znaków |
| Lekcje | 13 |
| Materiały instruktora | 13 |
| Scenariusze | 39 |
| Warianty / klucze | 5 / 5 |
| Słowniczek | 90 haseł |
| Formalne zatwierdzenia prawne | 0 |

## 4. Granice i niepewności

- Redakcyjna poprawka ADR-B-0586 w etapie 4x131 nie zmieniła klucza, opcji ani podstawy prawnej.
- Nie znaleziono potwierdzonej sprzeczności prawnej wymagającej zmiany odpowiedzi w zakresie przeprowadzonej kontroli; nie oznacza to, że pełna kontrola wszystkich punktów ADR została zakończona.
- Przyszłe wymagania ADR 2027 są oznaczone jako obszar do ponownej weryfikacji, a nie jako obowiązujące zmiany.
- Wszystkie pytania pozostają `needs_review`; warianty mają `publication_authorized: false`.
