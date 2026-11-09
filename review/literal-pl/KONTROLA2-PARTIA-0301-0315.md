# Kontrola druga — ADR-B-0301–0315

**Wynik: 0 OK / 15 POPRAW / 0 BLOKUJ.** Kontrola druga potwierdziła wszystkie 15 uwag. Dwanaście duplikatów lub agregatów (ADR-B-0301–0310, 0313 i 0315) zastąpiono nowymi tematami w tych samych kompetencjach. Pytania ADR-B-0311, ADR-B-0312 i ADR-B-0314 przeredagowano w obrębie zachowanych podtematów. Litery kluczy, identyfikatory modułów i przypisania kompetencji pozostały bez zmian; wszystkie rekordy pozostają `needs_review`, bez ustawiania `verified`.

## Korekty podstaw prawnych i stron Dz.U.

- ADR 1.1.3.1 (a)(i): **s. 23**, nie s. 24.
- ADR 2.2.9.1.7.2: **s. 275**, nie s. 274.
- ADR 5.2.2.1.1: **s. 939**, nie s. 940; punkt 5.2.2.1.6(a) przechodzi na s. 940.

## Nowe zagadnienia w rekordach zastępujących

| ID | Nowy temat | Podstawa ADR |
|---|---|---|
| 0301 | Ważność nowego zaświadczenia po kursie doskonalącym w ostatnich 12 miesiącach | 8.2.2.8.2(a)–(b) |
| 0302 | Kod klasyfikacyjny SW dla klasy 4.2 | 2.2.42.1.2 |
| 0303 | Nalepki na DPPL o pojemności ponad 450 l | 5.2.2.1.7 |
| 0304 | Definicja towarów niebezpiecznych dużego ryzyka | 1.10.3.1.1–1.10.3.2.1 |
| 0305 | Zabezpieczenie odłączonej naczepy z ładunkiem | 1.10.3.3; Umowa ADR art. 1(a) |
| 0306 | Kopia świadectwa dopuszczenia dla UN 0190 w kabinie | 5.4.1.2.1(c); 8.1.2.2(c) |
| 0307 | Czynniki inicjujące rozkład nadtlenków organicznych | 2.2.52.1.4 |
| 0308 | Oddalenie się od pożaru w tunelu po stronie nawietrznej | 5.4.3.4; 8.2.2.3.2(n) |
| 0309 | Toksyny bez czynników zakaźnych – klasa 6.1 | 2.2.62.1.1, UWAGA 2 |
| 0310 | Spełnienie nadzoru nad pojazdem na zwykłym parkingu | 8.4.1 |
| 0311 | Rozróżnienie UN 2814 i UN 2900 dla kategorii A | 2.2.62.1.2; 2.2.62.1.4.1(a) |
| 0312 | Postój w korku jako część przewozu | 1.2.1 |
| 0313 | Limity 60 l na naczynie i 240 l na jednostkę | 1.1.3.1(a)(i), (c) |
| 0314 | Nazwa i opis materiału w kolumnie (2) tabeli A | 3.2.1 |
| 0315 | PCB i możliwość tworzenia dioksyn w pożarze | 2.2.9.1.5 |

## Metryki i stan banku

- „Poprawna = jedyna najdłuższa”: **47/780 = 6,03% → 39/780 = 5,00%**.
- Maksimum działu: **11,24% → 7,87%**.
- Poprawna = jedyna najkrótsza: w każdym dziale maksymalnie 38%.
- Licznik pytań bez porównania literalnego po partii 21: **438**.
- Oczekiwany i potwierdzony blob banku po wdrożeniu: `b8055016086e53a9da3349ab1c58a096a83210f9`.

Nie zmieniono liter kluczy, `module_id`, przypisań w `kompetencje.json` ani statusów w kierunku zatwierdzenia eksperckiego.