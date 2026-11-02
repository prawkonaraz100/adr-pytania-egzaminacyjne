# Etap 4x298 — klasa 4.2: samonagrzewanie

Data: 2026-11-02. Bazowy main `dda654c9`, gałąź `stage4x298-class42-self-heating`.

- Dodano **ADR-B-0724** do **ADR-B-02-K05**: 5 → 6 pytań.
- **Kompetencje teorii <6 pytań: 56** (poprzednio 57; 3 praktyczne pominięte).
- Bank 724, wszystkie `needs_review`, 0 `verified`; blob SHA `ede1889d5ee07f9cb85a299a4ca095ebb897d034`.
- A/B/C: 242/259/223; poprawna jedyna najdłuższa: 78/724 = 10,77%, maksimum 13,95% (limit 18%).
- Klucz **A**, długości A/B/C 101/99/94; explanation 346 znaków.
- Podstawa prawna: ADR 2025, 2.2.42.1.1 i 2.2.42.1.3 (Dz.U. 2025 poz. 642); kontrola pełnego tekstu polskiego i niezależna recenzja specjalisty oczekują.
- Egzaminy próbne 001–005, audyty sequential/legal 724-724, manifesty, kolejki, rejestr i raport coverage synchronizowane.

## Pytanie

Podczas przygotowania przewozu materiału samonagrzewającego się klasy 4.2 ktoś twierdzi, że nie może się on zapalić bez płomienia ani iskry. Jak kierowca powinien ocenić to stwierdzenie?

A. Jest błędne: materiał może nagrzewać się w kontakcie z powietrzem i po pewnym czasie sam się zapalić.

B. Jest prawdziwe: materiał nagrzewa się jedynie wtedy, gdy z zewnątrz doprowadza się ogień lub iskrę.

C. Jest prawdziwe: samonagrzewanie oznacza wyłącznie wzrost temperatury bez możliwości zapalenia.

Materiał samonagrzewający się może w kontakcie z powietrzem powoli wytwarzać ciepło, nawet bez płomienia i iskry. Jeśli ciepło nie jest dostatecznie odprowadzane, po godzinach lub dniach może dojść do samozapłonu. Dlatego błędne są odpowiedzi wymagające zewnętrznego ognia albo wykluczające zapalenie. Podstawa: ADR 2025, 2.2.42.1.1 i 2.2.42.1.3.
