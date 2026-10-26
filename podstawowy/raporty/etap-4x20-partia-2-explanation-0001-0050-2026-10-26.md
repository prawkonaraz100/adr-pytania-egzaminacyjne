# Etap 4x20 — audyt czytelności explanation ADR-B-0001–0050

- Punkt wyjścia: świeży `main` `41c7c46c7c13503f536346973a11dc38b2af95fc`.
- Zakres: pierwsze 50 pytań w banku kursu podstawowego.
- Metoda: skryptowa selekcja po długości zdań, początku od numeru przepisu, sygnałach przyczynowych i skrótach, a następnie ręczny odczyt treści jako początkujący kursant. Heurystyka była wyłącznie listą kandydatów; samo trafienie nie oznaczało błędu.

## Wynik

- Ręcznie przejrzano 50/50 explanation: ADR-B-0001–ADR-B-0050.
- Poprawiono 4 explanation: ADR-B-0025, ADR-B-0027, ADR-B-0028 i ADR-B-0029.
- Pozostałe 46 pozostawiono bez zmian: po odczycie zawierały zrozumiałe wyjaśnienie sensu, kontrast błędnych odpowiedzi i podstawę; część trafień heurystyki wynikała z samego cytowania „ADR” w podstawie prawnej, a nie z niewyjaśnionego żargonu.
- Nie zmieniano treści pytań, opcji, poprawnych liter ani statusów weryfikacji.

## Zmiany przed/po

1. **ADR-B-0025 — „sztuka przesyłki”**
   - Przed: „Dopuszczalność wspólnego załadunku wynika z zasad i tabeli zakazów ładowania razem w ADR 7.5.2.”
   - Po: dodano definicję wprost: „Sztuka przesyłki” to pojedyncze opakowanie albo zestaw opakowań przygotowany jako jedna przesyłka; objaśniono też, dlaczego kolor i wolne miejsce nie rozstrzygają o wspólnym załadunku.
   - Podstawa: ADR 7.5.2.

2. **ADR-B-0027 — kod CV28**
   - Przed: „...wskazane dla niej warunki... ADR 7.5.4 i CV28.”
   - Po: dodano wyjaśnienie, że CV28 to kod szczególnego warunku załadunku, a nie numer klasy ani ogólne zwolnienie.
   - Podstawa: ADR 7.5.4 i przepis szczególny CV28.

3. **ADR-B-0028 — IMDG**
   - Przed: „Dla drogi istotny jest ADR, a dla morza odpowiednie przepisy morskie.”
   - Po: wyjaśniono, że IMDG to międzynarodowy kodeks przewozu towarów niebezpiecznych drogą morską, i wskazano potrzebę sprawdzenia dokumentów oraz oznakowania dla każdego odcinka.
   - Podstawa: ADR 1.1.4.2.

4. **ADR-B-0029 — IMDG i odcinek drogowy**
   - Przed: ogólne określenie „kodeks morski IMDG”.
   - Po: podano prostą definicję skrótu i wyjaśniono, że uznanie wymagań dla odcinka drogowego jest warunkowe, a nie automatyczne.
   - Podstawa: ADR 1.1.4.2.1.

## Integralność i metryki

- Bank: 609 rekordów, 609 unikalnych ID, 0 duplikatów.
- Explanation minimum: 300 znaków; 0 poniżej 300.
- Wszystkie pytania pozostają `needs_review`; `verified`: 0.
- Wskaźnik „poprawna = jedyna najdłuższa” nie zmienił się, bo edytowano tylko explanation:
  - B-01: 6/45 = 13,33%
  - B-02: 8/56 = 14,29%
  - B-03: 7/49 = 14,29%
  - B-04: 6/46 = 13,04%
  - B-05: 6/43 = 13,95%
  - B-06: 5/45 = 11,11%
  - B-07: 6/48 = 12,50%
  - B-08: 5/42 = 11,90%
  - B-09: 4/46 = 8,70%
  - B-10: 4/55 = 7,27%
  - B-11: 6/43 = 13,95%
  - B-12: 6/44 = 13,64%
  - B-13: 4/47 = 8,51%
- Synchronizowano wszystkie 5 wariantów egzaminu i 5 kluczy z nowym blobem banku; klucz 002 otrzymał zaktualizowane explanation dla ADR-B-0028.
- Odświeżono migawki w `review/sequential/001-030.json` i `review/legal-clauses/001-030.json` dla czterech zmienionych rekordów. Status prawny i oceny A/B/C pozostają oczekujące na specjalistę.

## Ograniczenia

Zmiany językowe nie są potwierdzeniem prawnej poprawności treści. Testy zostaną potwierdzone przez Quality Gate CI w PR; lokalny checkout nie był dostępny w tym środowisku.
