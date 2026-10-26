# Etap 4x32 — kontrola dystraktorów B-05–08

## Punkt wyjścia
- Świeży `main`: `a5a7cbbadd072ac275033b6f74dd6a87c1d55ffc`, po scaleniu PR #472.
- Bank: 609 pytań, statusy `needs_review`; 0 `verified`.
- Partia obejmuje tylko kurs podstawowy.

## Ręcznie potwierdzone problemy i poprawki
Przeredagowano 6 pytań bez zmiany ID, działu ani poprawnej litery:

| ID | Problem | Zmiana |
|---|---|---|
| ADR-B-0184 | „Zawsze gasić każdy pożar nawet niebezpiecznie” i otwieranie ładunku były zbyt skrajne. | Zastąpiono je błędami: rozpoczęcie gaszenia tylko dlatego, że jest gaśnica, oraz otwieranie przesyłki w celu sprawdzenia zawartości. Klucz B. |
| ADR-B-0223 | „Zawsze, nawet bez drogi ucieczki” oraz otwieranie wszystkich przesyłek były łatwe do odrzucenia. | Użyto bardziej realistycznych błędów dotyczących próby gaszenia bez bezpiecznej drogi odwrotu i sprawdzania przesyłki przez otwieranie. Klucz A. |
| ADR-B-0379 | Uznanie, że masa nie ma znaczenia przy zabezpieczonym ładunku, było zbyt uproszczone. | Zastąpiono je pominięciem masy całkowitej pojazdu oraz błędnym ograniczeniem kontroli do cystern. Klucz A. |
| ADR-B-0479 | „Nigdy nie można korzystać z danych innych uczestników” i pomijanie zakazów były zbyt absolutne. | Dystraktory sprawdzają teraz dwa realne nieporozumienia: konieczność powtarzania wszystkich badań oraz przekonanie, że komplet dokumentów uchyla zakaz wspólnego załadunku. Klucz C. |
| ADR-B-0552 | „Świadectwo nigdy nie jest wymagane” było zbyt łatwe do odrzucenia. | Zastąpiono je błędnym zawężeniem świadectwa wyłącznie do pojazdów dla materiałów wybuchowych klasy 1. Klucz B. |
| ADR-B-0565 | Natychmiastowe zdjęcie tablic i zamalowanie numeru były skrajne. | Zastąpiono je mylnym poleganiem na zamknięciu dokumentu oraz przekonaniem, że po opróżnieniu wystarczy usunąć numer UN. Klucz A. |

Explanation dla wszystkich sześciu pytań przepisano na 2–5 zdań: sens poprawnej odpowiedzi, dlaczego dystraktory są błędne i krótka podstawa ADR. Wszystkie mają co najmniej 300 znaków. Zmiany nie stanowią niezależnej recenzji prawnej.

## Kontrola lekcji B-05–08
Każda lekcja ma „Co musisz zapamiętać”, „Scenariusze praktyczne” oraz „Powiązane pytania w banku”. Nie wykryto brakującej z tych sekcji. W tej partii nie dopisywano nowej treści do lekcji, ponieważ problem dotyczył jakości odpowiedzi w banku, a nie braku podsumowania/scenariusza/odnośników.

## Metryki po zmianach
| Dział | Pytań | Poprawna = jedyna najdłuższa | Udział | Najkrótsze explanation | Klucz A/B/C |
|---|---:|---:|---:|---:|---|
| ADR-B-05 | 43 | 5 | 11.63% | 300 znaków | 18/14/11 |
| ADR-B-06 | 45 | 5 | 11.11% | 301 znaków | 16/14/15 |
| ADR-B-07 | 48 | 6 | 12.50% | 304 znaków | 18/18/12 |
| ADR-B-08 | 42 | 5 | 11.90% | 303 znaków | 12/12/18 |
- Globalnie po zmianach: 71/609 = 11.66% według ścisłego kryterium „poprawna = jedyna najdłuższa”.
- ID, dział, poprawna litera i statusy nie zostały zmienione.

## Następne kroki
Po edycji banku należy zsynchronizować manifest pakietu recenzyjnego, arkusze i klucze egzaminów próbnych oraz snapshoty audytów redakcyjnych/klauzulowych. Quality Gate CI ma potwierdzić spójność przed scaleniem.
