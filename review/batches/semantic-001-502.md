# Audyt podobieństwa całego banku ADR-B-0001–0502

23.10.2026; 502 rekordy porównane parami w ramach działów (około 125 tys. możliwych par, sprawdzane pary w obrębie danego działu). Metoda: tokeny znormalizowane do ASCII, pominięcie wybranych słów funkcyjnych, podobieństwo Jaccarda zbioru tokenów, próg 0,40. **To tylko screening leksykalny; parafrazy semantyczne o innym słownictwie mogą zostać przeoczone.** 15 par z wynikiem ≥ 0,40; 2 z wynikiem ≥0,60. Nie wolno automatycznie usuwać lub przenumerowywać pytań z powodu wyniku.

| Para ID | Wynik | Ocena redakcyjna |
|---|---:|---|
| ADR-B-0071 / ADR-B-0072 | 0.909 | niepotwierdzone — odrębne limity, klasy lub szczegółowe warunki; pozostawić do ręcznej oceny |
| ADR-B-0330 / ADR-B-0337 | 0.636 | niepotwierdzone — odrębne limity, klasy lub szczegółowe warunki; pozostawić do ręcznej oceny |
| ADR-B-0017 / ADR-B-0052 | 0.500 | niepotwierdzone — odrębne limity, klasy lub szczegółowe warunki; pozostawić do ręcznej oceny |
| ADR-B-0022 / ADR-B-0419 | 0.500 | niepotwierdzone — odrębne limity, klasy lub szczegółowe warunki; pozostawić do ręcznej oceny |
| ADR-B-0042 / ADR-B-0096 | 0.500 | niepotwierdzone — odrębne limity, klasy lub szczegółowe warunki; pozostawić do ręcznej oceny |
| ADR-B-0153 / ADR-B-0159 | 0.500 | niepotwierdzone — odrębne limity, klasy lub szczegółowe warunki; pozostawić do ręcznej oceny |
| ADR-B-0223 / ADR-B-0493 | 0.500 | niepotwierdzone — odrębne limity, klasy lub szczegółowe warunki; pozostawić do ręcznej oceny |
| ADR-B-0304 / ADR-B-0400 | 0.462 | niepotwierdzone — odrębne limity, klasy lub szczegółowe warunki; pozostawić do ręcznej oceny |
| ADR-B-0017 / ADR-B-0051 | 0.444 | niepotwierdzone — odrębne limity, klasy lub szczegółowe warunki; pozostawić do ręcznej oceny |
| ADR-B-0031 / ADR-B-0262 | 0.444 | niepotwierdzone — odrębne limity, klasy lub szczegółowe warunki; pozostawić do ręcznej oceny |
| ADR-B-0326 / ADR-B-0338 | 0.438 | niepotwierdzone — odrębne limity, klasy lub szczegółowe warunki; pozostawić do ręcznej oceny |
| ADR-B-0043 / ADR-B-0095 | 0.429 | niepotwierdzone — odrębne limity, klasy lub szczegółowe warunki; pozostawić do ręcznej oceny |
| ADR-B-0204 / ADR-B-0278 | 0.429 | potwierdzone powtórzenie tej samej kompetencji / rekomendacja przeprojektowania |
| ADR-B-0005 / ADR-B-0097 | 0.400 | niepotwierdzone — odrębne limity, klasy lub szczegółowe warunki; pozostawić do ręcznej oceny |
| ADR-B-0308 / ADR-B-0435 | 0.400 | niepotwierdzone — odrębne limity, klasy lub szczegółowe warunki; pozostawić do ręcznej oceny |

## Potwierdzone zbieżności treści wymagające różnicowania

- **ADR-B-0204 / ADR-B-0278:** pytanie pierwsze: „Kontener z towarami niebezpiecznymi jedzie drogą, a następnie ma być załadowany na statek. Kto, zgodnie z ADR 5.4.2, dostarcza przewoźnikowi morskiemu certyfikat pakowania kontenera?”; drugie: „Kontener z zapakowanymi towarami niebezpiecznymi ma zostać załadowany na statek po odcinku drogowym. Kto zgodnie z ADR 5.4.2 odpowiada za przekazanie przewoźnikowi morskiemu świadectwa pakowania kontenera?”. Wspólny rezultat prawny: ADR 2025, 5.4.2 / ADR 2025, 5.4.2. Zachować ID i historię audytów; przygotować odrębny przypadek graniczny dla drugiego wpisu zamiast zmieniać klucz bez źródłowego potwierdzenia.
- **ADR-B-0009 / ADR-B-0241:** pytanie pierwsze: „Podczas rozładunku sztuk przesyłek ADR stwierdzono, że zawartość jednego opakowania wyciekła i zabrudziła pojazd. Co należy zrobić przed ponownym załadunkiem?”; drugie: „Po rozładunku ADR na podłodze pojazdu zauważono wyciek z przesyłki. Co należy zrobić przed ponownym załadunkiem?”. Wspólny rezultat prawny: ADR 2025, 7.5.8.1 / ADR 2025, 7.5.8.1. Zachować ID i historię audytów; przygotować odrębny przypadek graniczny dla drugiego wpisu zamiast zmieniać klucz bez źródłowego potwierdzenia.
- **ADR-B-0025 / ADR-B-0324:** pytanie pierwsze: „Na jakiej podstawie należy ustalić, czy sztuki przesyłek z różnymi nalepkami ostrzegawczymi ADR wolno załadować do jednego pojazdu?”; drugie: „Przed wspólnym załadunkiem do jednego pojazdu sztuk przesyłek z różnymi nalepkami ostrzegawczymi, co należy sprawdzić zgodnie z ADR 7.5.2.1?”. Wspólny rezultat prawny: ADR 2025, 7.5.2 / ADR 2025, 7.5.2.1 (tabela i uwagi). Zachować ID i historię audytów; przygotować odrębny przypadek graniczny dla drugiego wpisu zamiast zmieniać klucz bez źródłowego potwierdzenia.

## Pary podobne tylko językowo

- 0071/0072: różne granice DMC, **obie potrzebne**.
- 0330/0337: różne wyłączenia klas odpadów, **obie potrzebne**.
- 0223/0493: opona vs hamulec, podobna decyzja, ale różne zdarzenia.
- Pozostałe pary należy porównać dodatkowo metodą parafraz i ręcznie na poziomie wszystkich A/B/C; podobieństwo słów nie potwierdza powielenia odpowiedzi.

## Granice audytu

To pełny screening pytań całego banku, **nie zweryfikowane semantyczne embeddings 502 rekordów**. Brak indywidualnego niezależnego stwierdzenia poprawności prawnej i pełnego porównania z polskim tekstem urzędowym. Zmiany w treści powtórzeń wolno przeprowadzać wyłącznie z równoczesnym odświeżeniem `review/sequential` i `review/legal-clauses`, aby nie tworzyć nieaktualnych snapshotów.
