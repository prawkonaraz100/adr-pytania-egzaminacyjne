# Etap 4x59 — próba 60 wyjaśnień, poprawa powtórzenia

- Data: 26.10.2026. Punkt wyjścia: świeży main `f81eb067d4a4a4a238ee04389d97c355a22ec6eb`, po PR #509.
- Tylko kurs podstawowy ADR. Seed: `2026102659`; LCG `(1664525 × stan + 1013904223) mod 2^32`, Fisher–Yates.
- Wykluczono wszystkie ID występujące w próbach 4x51, 4x52, 4x56, 4x57 i 4x58: 289 różnych ID. Pula: 320; wybrano 60 bez powtórzeń.
- Ocena: sens poprawnej odpowiedzi, argument przeciw błędnym wariantom, język początkującego i podstawa ADR. Ocena redakcyjna nie oznacza potwierdzenia poprawności prawnej.

## Lista 60 wyjaśnień

| ID | Ocena redakcyjna |
|---|---|
| ADR-B-0332 | Bez zmiany: wyjaśnienie ma więcej niż jedno zdanie, przekazuje sens i odnosi się do błędnych opcji oraz podstawy ADR |
| ADR-B-0275 | Bez zmiany: wyjaśnienie ma więcej niż jedno zdanie, przekazuje sens i odnosi się do błędnych opcji oraz podstawy ADR |
| ADR-B-0104 | Bez zmiany: wyjaśnienie ma więcej niż jedno zdanie, przekazuje sens i odnosi się do błędnych opcji oraz podstawy ADR |
| ADR-B-0129 | Bez zmiany: wyjaśnienie ma więcej niż jedno zdanie, przekazuje sens i odnosi się do błędnych opcji oraz podstawy ADR |
| ADR-B-0544 | Bez zmiany: wyjaśnienie ma więcej niż jedno zdanie, przekazuje sens i odnosi się do błędnych opcji oraz podstawy ADR |
| ADR-B-0425 | Bez zmiany: wyjaśnienie ma więcej niż jedno zdanie, przekazuje sens i odnosi się do błędnych opcji oraz podstawy ADR |
| ADR-B-0471 | Bez zmiany: wyjaśnienie ma więcej niż jedno zdanie, przekazuje sens i odnosi się do błędnych opcji oraz podstawy ADR |
| ADR-B-0067 | Bez zmiany: wyjaśnienie ma więcej niż jedno zdanie, przekazuje sens i odnosi się do błędnych opcji oraz podstawy ADR |
| ADR-B-0156 | Bez zmiany: wyjaśnienie ma więcej niż jedno zdanie, przekazuje sens i odnosi się do błędnych opcji oraz podstawy ADR |
| ADR-B-0546 | Bez zmiany: wyjaśnienie ma więcej niż jedno zdanie, przekazuje sens i odnosi się do błędnych opcji oraz podstawy ADR |
| ADR-B-0301 | Bez zmiany: wyjaśnienie ma więcej niż jedno zdanie, przekazuje sens i odnosi się do błędnych opcji oraz podstawy ADR |
| ADR-B-0002 | Bez zmiany: wyjaśnienie ma więcej niż jedno zdanie, przekazuje sens i odnosi się do błędnych opcji oraz podstawy ADR |
| ADR-B-0448 | Bez zmiany: wyjaśnienie ma więcej niż jedno zdanie, przekazuje sens i odnosi się do błędnych opcji oraz podstawy ADR |
| ADR-B-0249 | Bez zmiany: wyjaśnienie ma więcej niż jedno zdanie, przekazuje sens i odnosi się do błędnych opcji oraz podstawy ADR |
| ADR-B-0551 | Bez zmiany: wyjaśnienie ma więcej niż jedno zdanie, przekazuje sens i odnosi się do błędnych opcji oraz podstawy ADR |
| ADR-B-0532 | Bez zmiany: wyjaśnienie ma więcej niż jedno zdanie, przekazuje sens i odnosi się do błędnych opcji oraz podstawy ADR |
| ADR-B-0322 | Bez zmiany: wyjaśnienie ma więcej niż jedno zdanie, przekazuje sens i odnosi się do błędnych opcji oraz podstawy ADR |
| ADR-B-0274 | Bez zmiany: wyjaśnienie ma więcej niż jedno zdanie, przekazuje sens i odnosi się do błędnych opcji oraz podstawy ADR |
| ADR-B-0153 | Bez zmiany: wyjaśnienie ma więcej niż jedno zdanie, przekazuje sens i odnosi się do błędnych opcji oraz podstawy ADR |
| ADR-B-0445 | Bez zmiany: wyjaśnienie ma więcej niż jedno zdanie, przekazuje sens i odnosi się do błędnych opcji oraz podstawy ADR |
| ADR-B-0420 | Bez zmiany: wyjaśnienie ma więcej niż jedno zdanie, przekazuje sens i odnosi się do błędnych opcji oraz podstawy ADR |
| ADR-B-0376 | Bez zmiany: wyjaśnienie ma więcej niż jedno zdanie, przekazuje sens i odnosi się do błędnych opcji oraz podstawy ADR |
| ADR-B-0457 | Bez zmiany: wyjaśnienie ma więcej niż jedno zdanie, przekazuje sens i odnosi się do błędnych opcji oraz podstawy ADR |
| ADR-B-0461 | Bez zmiany: wyjaśnienie ma więcej niż jedno zdanie, przekazuje sens i odnosi się do błędnych opcji oraz podstawy ADR |
| ADR-B-0221 | Bez zmiany: wyjaśnienie ma więcej niż jedno zdanie, przekazuje sens i odnosi się do błędnych opcji oraz podstawy ADR |
| ADR-B-0438 | Bez zmiany: wyjaśnienie ma więcej niż jedno zdanie, przekazuje sens i odnosi się do błędnych opcji oraz podstawy ADR |
| ADR-B-0100 | Bez zmiany: wyjaśnienie ma więcej niż jedno zdanie, przekazuje sens i odnosi się do błędnych opcji oraz podstawy ADR |
| ADR-B-0305 | Bez zmiany: wyjaśnienie ma więcej niż jedno zdanie, przekazuje sens i odnosi się do błędnych opcji oraz podstawy ADR |
| ADR-B-0055 | Bez zmiany: wyjaśnienie ma więcej niż jedno zdanie, przekazuje sens i odnosi się do błędnych opcji oraz podstawy ADR |
| ADR-B-0106 | Bez zmiany: wyjaśnienie ma więcej niż jedno zdanie, przekazuje sens i odnosi się do błędnych opcji oraz podstawy ADR |
| ADR-B-0572 | Bez zmiany: wyjaśnienie ma więcej niż jedno zdanie, przekazuje sens i odnosi się do błędnych opcji oraz podstawy ADR |
| ADR-B-0393 | Bez zmiany: wyjaśnienie ma więcej niż jedno zdanie, przekazuje sens i odnosi się do błędnych opcji oraz podstawy ADR |
| ADR-B-0066 | Bez zmiany: wyjaśnienie ma więcej niż jedno zdanie, przekazuje sens i odnosi się do błędnych opcji oraz podstawy ADR |
| ADR-B-0137 | Bez zmiany: wyjaśnienie ma więcej niż jedno zdanie, przekazuje sens i odnosi się do błędnych opcji oraz podstawy ADR |
| ADR-B-0299 | Bez zmiany: wyjaśnienie ma więcej niż jedno zdanie, przekazuje sens i odnosi się do błędnych opcji oraz podstawy ADR |
| ADR-B-0004 | Bez zmiany: wyjaśnienie ma więcej niż jedno zdanie, przekazuje sens i odnosi się do błędnych opcji oraz podstawy ADR |
| ADR-B-0134 | Bez zmiany: wyjaśnienie ma więcej niż jedno zdanie, przekazuje sens i odnosi się do błędnych opcji oraz podstawy ADR |
| ADR-B-0252 | Bez zmiany: wyjaśnienie ma więcej niż jedno zdanie, przekazuje sens i odnosi się do błędnych opcji oraz podstawy ADR |
| ADR-B-0179 | Bez zmiany: wyjaśnienie ma więcej niż jedno zdanie, przekazuje sens i odnosi się do błędnych opcji oraz podstawy ADR |
| ADR-B-0576 | Bez zmiany: wyjaśnienie ma więcej niż jedno zdanie, przekazuje sens i odnosi się do błędnych opcji oraz podstawy ADR |
| ADR-B-0300 | Bez zmiany: wyjaśnienie ma więcej niż jedno zdanie, przekazuje sens i odnosi się do błędnych opcji oraz podstawy ADR |
| ADR-B-0072 | Bez zmiany: wyjaśnienie ma więcej niż jedno zdanie, przekazuje sens i odnosi się do błędnych opcji oraz podstawy ADR |
| ADR-B-0006 | Bez zmiany: wyjaśnienie ma więcej niż jedno zdanie, przekazuje sens i odnosi się do błędnych opcji oraz podstawy ADR |
| ADR-B-0200 | Bez zmiany: wyjaśnienie ma więcej niż jedno zdanie, przekazuje sens i odnosi się do błędnych opcji oraz podstawy ADR |
| ADR-B-0453 | Bez zmiany: wyjaśnienie ma więcej niż jedno zdanie, przekazuje sens i odnosi się do błędnych opcji oraz podstawy ADR |
| ADR-B-0186 | Bez zmiany: wyjaśnienie ma więcej niż jedno zdanie, przekazuje sens i odnosi się do błędnych opcji oraz podstawy ADR |
| ADR-B-0524 | Bez zmiany: wyjaśnienie ma więcej niż jedno zdanie, przekazuje sens i odnosi się do błędnych opcji oraz podstawy ADR |
| ADR-B-0251 | Bez zmiany: wyjaśnienie ma więcej niż jedno zdanie, przekazuje sens i odnosi się do błędnych opcji oraz podstawy ADR |
| ADR-B-0133 | Bez zmiany: wyjaśnienie ma więcej niż jedno zdanie, przekazuje sens i odnosi się do błędnych opcji oraz podstawy ADR |
| ADR-B-0289 | Bez zmiany: wyjaśnienie ma więcej niż jedno zdanie, przekazuje sens i odnosi się do błędnych opcji oraz podstawy ADR |
| ADR-B-0363 | Bez zmiany: wyjaśnienie ma więcej niż jedno zdanie, przekazuje sens i odnosi się do błędnych opcji oraz podstawy ADR |
| ADR-B-0177 | Bez zmiany: wyjaśnienie ma więcej niż jedno zdanie, przekazuje sens i odnosi się do błędnych opcji oraz podstawy ADR |
| ADR-B-0386 | Bez zmiany: wyjaśnienie ma więcej niż jedno zdanie, przekazuje sens i odnosi się do błędnych opcji oraz podstawy ADR |
| ADR-B-0520 | Bez zmiany: wyjaśnienie ma więcej niż jedno zdanie, przekazuje sens i odnosi się do błędnych opcji oraz podstawy ADR |
| ADR-B-0323 | Bez zmiany: wyjaśnienie ma więcej niż jedno zdanie, przekazuje sens i odnosi się do błędnych opcji oraz podstawy ADR |
| ADR-B-0306 | Bez zmiany: wyjaśnienie ma więcej niż jedno zdanie, przekazuje sens i odnosi się do błędnych opcji oraz podstawy ADR |
| ADR-B-0201 | Poprawiono: usunięto powtarzający się opis wyjątku od czyszczenia; 3 zdania plus podstawa ADR 7.5.8.2 |
| ADR-B-0110 | Bez zmiany: wyjaśnienie ma więcej niż jedno zdanie, przekazuje sens i odnosi się do błędnych opcji oraz podstawy ADR |
| ADR-B-0416 | Bez zmiany: wyjaśnienie ma więcej niż jedno zdanie, przekazuje sens i odnosi się do błędnych opcji oraz podstawy ADR |
| ADR-B-0440 | Bez zmiany: wyjaśnienie ma więcej niż jedno zdanie, przekazuje sens i odnosi się do błędnych opcji oraz podstawy ADR |

## Potwierdzona poprawka

- `ADR-B-0201`: dwukrotnie tłumaczono wyjątek przy ponownym załadunku dokładnie tego samego towaru przewożonego luzem. Pozostawiono jedno prostsze wyjaśnienie reguły oraz błędnego uogólnienia z odpowiedzi C, ze wskazaniem ADR 7.5.8.2. Nie zmieniono poprawnej litery, opcji, numeru ani źródła.
- Zsynchronizowano snapshoty w `review/sequential/181-210.json` i `review/legal-clauses/181-210.json` oraz źródłowy blob banku we wszystkich pięciu wariantach i kluczach egzaminu próbnego. Pytania nie ma w żadnym z pięciu kluczy.

## Quality Gate — stan po poprawce

- 609 pytań, brak duplikatów ID; 609 `needs_review`, 0 `verified`.
- „Poprawna = jedyna najdłuższa”: 72/609 = 11.82%, limit 18%.
- Minimum explanation: 300 znaków; poniżej 200: 0.
- Heurystycznie jednozdaniowych i rozpoczynających się cytatem przepisu w wybranej próbie: 0. Ręczny przegląd wykazał jedno powtarzalne wyjaśnienie do redakcji.

## Dalszy krok

Brak potwierdzonej nowej luki programu uzasadniającej tworzenie pytania 0610. Warto rozwijać testy przydatności scenariuszy na zajęciach i obserwować recenzję specjalisty. Wszystkie wskazania ADR pozostają `needs_review`; żadnego pytania nie oznaczono jako zweryfikowane.
