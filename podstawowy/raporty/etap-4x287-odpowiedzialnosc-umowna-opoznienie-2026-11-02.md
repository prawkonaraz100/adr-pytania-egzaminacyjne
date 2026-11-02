# Etap 4x287 — odpowiedzialność umowna przy opóźnieniu przewozu (ADR-B-0713)

Data: 02.11.2026  
Zakres: wyłącznie kurs ADR podstawowy dla kierowców  
Gałąź: stage4x287-contractual-liability-delay-closure  
Punkt wyjścia: main 718d4788bc8ee771c2ff8008eb5d45978cd14cef  
Nowy identyfikator: ADR-B-0713

## Luka i uzasadnienie
Kompetencja ADR-B-07-K07 („Podstawowe rozróżnienie odpowiedzialności cywilnej za szkodę i za niewykonanie zobowiązania”) miała 4 przypisane pytania — jeden z najniższych wyników w mapie kompetencji. Dotychczasowe pytania omawiały ogólne zasady winy i odpowiedzialności za działania kierowcy, ale brakowało scenariusza opóźnienia wskutek nagłego zamknięcia drogi oraz rozróżnienia między samym niewykonaniem terminu a odpowiedzialnością za jego przyczynę.

## Treść i audyt A/B/C
- Sytuacja: przewoźnik nie może dotrzymać terminu z powodu nagłego zamknięcia drogi po osunięciu ziemi; odbiorca żąda odszkodowania.
- Klucz: B — odpowiedzialność nie jest automatyczna; znaczenie ma, czy opóźnienie wynikało z okoliczności, za które przewoźnik odpowiada.
- A: błędnie zakłada automatyczną odpowiedzialność niezależnie od przyczyny.
- B: prawidłowo oddaje ogólną zasadę art. 471 KC, bez przesądzania wyniku konkretnego sporu.
- C: błędnie przenosi odpowiedzialność wyłącznie na kierowcę i pomija stronę umowy.
- Długości opcji A/B/C: 121/126/108 znaków; poprawna B jest najdłuższa.
- Explanation: 475 znaków, 4 zdania; najpierw praktyczny sens, następnie pułapki odpowiedzi, na końcu podstawa prawna.

## Podstawa prawna
- ADR 2025, 8.2.2.3.2(k): program kursu podstawowego obejmuje ogólne informacje o odpowiedzialności cywilnej.
- Kodeks cywilny, art. 471, tekst jednolity Dz.U. 2026 poz. 795: odpowiedzialność za szkodę wynikłą z niewykonania lub nienależytego wykonania zobowiązania, z zastrzeżeniem okoliczności, za które dłużnik nie odpowiada.
- Oficjalne źródła: https://eli.gov.pl/api/acts/DU/2025/642/text.pdf oraz https://api.sejm.gov.pl/eli/acts/DU/2026/795/text.pdf

## Status i ograniczenia
Pytanie pozostaje `needs_review`. Nie przeprowadzono pełnego literalnego porównania tekstu Dz.U. ani niezależnej recenzji specjalisty. Nic nie oznaczono jako `verified`. Scenariusz służy nauce ogólnej zasady i nie rozstrzyga, czy konkretne zamknięcie drogi zwalnia przewoźnika z odpowiedzialności.

## Synchronizacja i Quality Gate
Bank: 713 pytań po dodaniu ADR-B-0713; 713 `needs_review`, 0 `verified`.  
SHA banku: `f308b1555c50d3f657c2d753c81273bc56dda1de`.  
Po zmianie banku należy odświeżyć klucze i warianty egzaminu próbnego 001–005, snapshoty sequential/legal, rejestr źródeł, manifesty, indeks specjalisty, raporty, metryki oraz asercje liczby pytań. Wynik Quality Gate zostanie odnotowany dopiero po CI PR.
