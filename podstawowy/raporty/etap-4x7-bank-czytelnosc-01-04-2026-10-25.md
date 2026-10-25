# Etap 4x7 — kontrola banku i czytelności, partia B-01–04

## Punkt wyjścia
- Świeży `main`: `6c90aac628c93be5e0241a8980d5a59c433d81de`.
- Bank: 609 pytań; zakres sprawdzenia: wszystkie rekordy z modułów ADR-B-01–04 (196 pytań). Weryfikacja obejmuje podobieństwo tekstu, zestawy odpowiedzi, długość i strukturę wyjaśnień oraz użycie skrótów.
- Nie zmieniono ID, przypisania modułów, poprawnych liter ani statusów weryfikacji.

## Powtórzenia
Automatyczny skan porównał pytania wewnątrz modułów, używając podobieństwa Jaccarda po normalizacji polskich znaków oraz porównania zestawów odpowiedzi:
- `ADR-B-0071` / `ADR-B-0072`: podobieństwo ok. 0,91, ale nie jest to duplikat potwierdzony. Oba pytania sprawdzają ten sam przepis o gaśnicach dla różnych DMC (3,5 t i 6 t); trzeba zastosować różne progi tabeli ADR. Para jest udokumentowana jako dopuszczony wyjątek w Quality Gate.
- `ADR-B-0169` / `ADR-B-0585`: podobieństwo ok. 0,64 i praktycznie identyczna sytuacja (gaśnica zasłonięta ładunkiem, brak szybkiego dostępu). To potwierdzony duplikat dydaktyczny, ale oba rekordy należą do modułu B-05. Zostawiono bez zmiany w tej partii, a poprawka jest przypisana do następnej partii B-05–08; para ma tymczasowy wpis w allowliście bramki, aby nie blokować istniejącego banku. Nowe podobne pary są blokowane.
- Brak potwierdzonych duplikatów w B-01–04.

## Czytelność explanation
- Dodano rozwinięcia skrótów w 19 wyjaśnieniach z B-01–04: `ADR-B-0046`, `ADR-B-0093`, `ADR-B-0149`, `ADR-B-0162`, `ADR-B-0179`, `ADR-B-0260`, `ADR-B-0261`, `ADR-B-0273`, `ADR-B-0294`, `ADR-B-0341`, `ADR-B-0343`, `ADR-B-0526`, `ADR-B-0527`, `ADR-B-0528`, `ADR-B-0534`, `ADR-B-0535`, `ADR-B-0572`, `ADR-B-0605`, `ADR-B-0609`.
- Rozwinięcia obejmują m.in. LQ (ilości ograniczone), EQ (ilości wyłączone), DMC (dopuszczalna masa całkowita) oraz numer UN jako identyfikator towaru niebezpiecznego.
- Nie wykryto explanation poniżej 200 znaków, jednozdaniowych, zaczynających się od samego numeru przepisu ani zdań dłuższych niż 35 słów w tej partii. Heurystyka słów kluczowych wskazuje kandydatów do dalszej redakcji, ale nie jest wystarczająca sama w sobie do uznania wyjaśnienia za błędne.
- Nie zmieniano odpowiedzi ani kluczy, ponieważ w tej partii nie wykryto potwierdzonego merytorycznego błędu.

## Słowniczek i ścieżka
- Dodano `podstawowy/SLOWNICZEK.md` z prostymi definicjami i odwołaniami do ADR.
- Dodano link do słowniczka w README i na końcu lekcji B-01–04. Kolejne partie dodadzą linki do pozostałych lekcji.

## Kontrole przed PR
- Pytania: 609; unikalne ID: 609; duplikaty ID: 0.
- Poprawna odpowiedź jest jedyną najdłuższą: 83/609 = 13.63% (limit 18%).
- Najkrótsze explanation: 300 znaków; poniżej 200: 0.
- Statusy: 609 `needs_review`, 0 `verified`.

## Ograniczenia
To jest redakcyjny i automatyczny przegląd, nie niezależna recenzja prawna. Pytania pozostają `needs_review`; niczego nie oznaczono jako `verified`.
