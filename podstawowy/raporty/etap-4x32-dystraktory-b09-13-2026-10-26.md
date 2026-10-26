# Etap 4x32 — kontrola dystraktorów B-09–13

## Punkt wyjścia
- Świeży `main`: `ba7d75199bbdb031ea87cf4f592b0a4d2dd5a28e`, po scaleniu PR #473.
- Bank: 609 pytań; statusy `needs_review`, 0 `verified`.
- Zakres wyłącznie kurs podstawowy.

## Ręcznie potwierdzone problemy i poprawki
Przeredagowano 6 pytań bez zmiany ID, działu ani poprawnej litery:

| ID | Problem | Zmiana |
|---|---|---|
| ADR-B-0079 | „Uszkodzenie opakowania nie ma znaczenia” było zbyt oczywistym dystraktorem. | Zmieniono na częstszy błąd: brak korekty mocowania, gdy nie widać pęknięcia mimo odkształcenia. Klucz C. |
| ADR-B-0213 | Rezygnacja z zabezpieczeń „zawsze” po poznaniu miejsca dostawy była łatwa do odrzucenia. | Zastąpiono ją błędnym ograniczeniem kontroli zabezpieczeń wyłącznie do postoju. Klucz B. |
| ADR-B-0228 | Zastąpienie instrukcji numerem telefonu było zbyt oczywiście błędne. | Zmieniono na przekonanie, że ustne omówienie pozwala trzymać instrukcje poza kabiną. Klucz C. |
| ADR-B-0248 | Nazwa nadawcy nie ma związku z kodem tunelowym. | Zastąpiono ją pomyleniem kolumny 1 i kolumny 7a z właściwą kolumną 15. Klucz A. |
| ADR-B-0398 | Kolor kontenera nie może zastąpić dokumentu; dystraktor był absurdalny. | Zmieniono na błędne poleganie na ustnym potwierdzeniu lub liście terminala zamiast wymaganym dokumencie. Klucz B. |
| ADR-B-0531 | Oświadczenie kierowcy o wytrzymałości i kolor opakowania nie odpowiadały wymogowi wpisu. | Zmieniono na mylenie odpowiedzialności za pakowanie oraz założenie, że oznakowanie opakowania zwalnia z wpisu w dokumencie. Klucz C. |

Wyjaśnienia sześciu pytań przepisano prostym językiem, na 2–5 zdań, z uzasadnieniem poprawnej odpowiedzi, błędów w dystraktorach i podstawą ADR. Wszystkie mają co najmniej 300 znaków. Nie oznaczono niczego jako `verified`.

## Kontrola lekcji B-09–13
Każda lekcja ma sekcję „Co musisz zapamiętać”, scenariusze praktyczne i odwołania do pytań. Nie wykryto braku strukturalnego wymagającego dopisania treści w tej partii. Przegląd dotyczy kompletności struktury oraz jakości dystraktorów, nie stanowi niezależnej oceny prawnej.

## Metryki po zmianach
| Dział | Pytań | Poprawna = jedyna najdłuższa | Udział | Najkrótsze explanation | Klucz A/B/C |
|---|---:|---:|---:|---:|---|
| ADR-B-09 | 46 | 3 | 6.52% | 301 znaków | 13/15/18 |
| ADR-B-10 | 55 | 4 | 7.27% | 308 znaków | 19/18/18 |
| ADR-B-11 | 43 | 6 | 13.95% | 300 znaków | 12/13/18 |
| ADR-B-12 | 44 | 6 | 13.64% | 303 znaków | 14/13/17 |
| ADR-B-13 | 47 | 4 | 8.51% | 308 znaków | 15/15/17 |
- Globalnie po zmianach: 70/609 = 11.49% według ścisłego kryterium.
- W tej partii nie zmieniono poprawnych liter ani statusów pytań.

## Kontrole integralności do odświeżenia przed scaleniem
Po zmianie banku należy zsynchronizować source_bank_head w wariantach i kluczach egzaminów próbnych 001–005, manifest i indeks pakietu recenzyjnego oraz snapshoty audytów sekwencyjnych i klauzulowych dla zmienionych ID. Końcowy merge dopiero po PASS Quality Gate CI.
