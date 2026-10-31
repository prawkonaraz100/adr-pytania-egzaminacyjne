# Etap 4x236 — materiały polimeryzujące klasy 4.1 i kontrola temperatury

Data: 31.10.2026. Zakres: wyłącznie kurs podstawowy ADR. Punkt wyjścia: świeży `main` `50bb3f83d7ad38008a4ee635006691a18cd2faef`, po scaleniu PR #704; bank 660 pytań, ostatnie ID ADR-B-0660.

## 1. Audyt luki

Kompetencja ADR-B-02-K04 „Klasa 4.1: materiały stałe zapalne” miała cztery pytania (ADR-B-0094, 0153, 0268 i 0611). Sprawdzały przede wszystkim rozpoznanie numeru klasy, odróżnienie 4.1 od 4.2/4.3 i odczyt nalepki. Brakowało praktycznego zastosowania odrębnych progów kontroli temperatury dla materiałów polimeryzujących przewożonych w DPPL i cysternach.

## 2. Nowe pytanie ADR-B-0661

Dodano ADR-B-0661 do ADR-B-02-K04. Scenariusz: materiał polimeryzujący klasy 4.1 przewożony w DPPL, TSP w tym DPPL wynosi 48°C. Pytanie sprawdza, czy kursant zastosuje próg 50°C dla DPPL, a nie próg 45°C dotyczący cystern ani próg 75°C używany w kryteriach klasyfikacji.

| Opcja | Długość | Ocena |
|---|---:|---|
| A | 76 | Błędna — myli próg 45°C dla cystern z wymaganiem dla DPPL. |
| B | 85 | **Poprawna** — dla DPPL kontrola temperatury jest wymagana przy TSP 50°C lub niższej. |
| C | 94 | Błędna — myli próg 75°C, używany w kryteriach klasyfikacji, z progiem obowiązku kontroli temperatury. |

Explanation ma 354 znaki i 4 zdania. Poprawna odpowiedź B nie jest ani najkrótsza, ani najdłuższa. Status: `needs_review`.

## 3. Podstawy prawne

- ADR 2025, 2.2.41.1.20 — kryteria klasyfikacji materiałów polimeryzujących do klasy 4.1; między innymi TSP 75°C lub mniej, ciepło reakcji ponad 300 J/g i brak spełnienia kryteriów innej klasy.
- ADR 2025, 2.2.41.1.21(a) — materiały polimeryzujące przewożone w sztuce przesyłki lub DPPL podlegają kontroli temperatury, jeżeli TSP w tej sztuce przesyłki lub DPPL wynosi 50°C lub mniej.
- ADR 2025, 2.2.41.1.21(b) — odrębny próg 45°C dotyczy przewozu w cysternie.
- ADR 2025, 7.1.7 — ogólne wymagania dotyczące przewozu w temperaturze kontrolowanej.
- Źródło wiążące: Umowa ADR ogłoszona w Dz.U. 2025 poz. 642: https://dziennikustaw.gov.pl/DU/2025/642
- Pomocniczy polski tekst ADR 2025 udostępniony przez Ministerstwo Infrastruktury (nie zastępuje źródła wiążącego): https://www.gov.pl/attachment/8856b22a-bfd8-4567-8386-b9709bba8da7
- Sprawdzono sprostowanie Dz.U. 2025 poz. 1575: https://eli.gov.pl/api/acts/DU/2025/1575/text.pdf. W wykazie sprostowanych przepisów nie wskazano 2.2.41.1.20, 2.2.41.1.21 ani 7.1.7.

**Granica pytania:** pytanie zakłada, że materiał został już prawidłowo zaklasyfikowany jako polimeryzujący i że TSP odnosi się do konkretnego DPPL, w którym ma być przewożony. Nie zastępuje sprawdzenia wpisu w tabeli A, przepisów szczególnych ani warunków 7.1.7 dla konkretnego towaru.

Pełne literalne porównanie polskiego tekstu wiążącego ADR ze sprostowaniem i niezależna recenzja specjalisty pozostają otwarte. Nie oznaczono pytania jako `verified`.

## 4. Materiały dydaktyczne i mapa

- Mapa kompetencji: ADR-B-02-K04 ma teraz 5 pytań: ADR-B-0094, 0153, 0268, 0611 i 0661.
- Lekcja ADR-B-02: dodano wyjaśnienie progów 50°C (sztuka przesyłki/DPPL), 45°C (cysterna) i 75°C (kryterium klasyfikacji).
- Materiał instruktora ADR-B-02: dodano fikcyjną kartę towaru i zadanie rozróżnienia progów; bez pracy na rzeczywistym materiale.
- Istniejące pytania i ich klucze nie zostały zmienione.

## 5. Synchronizacja po zmianie banku — pułapka #646

- Bank: 661 rekordów ADR-B-0001–0661, ID ciągłe i unikalne; wszystkie `needs_review`, 0 `verified`.
- Blob SHA `questions.jsonl`: `d7ad9711a2e5f5ced552ff6a4140455104536280`.
- Warianty i klucze egzaminów próbnych 001–005 wskazują aktualny blob SHA; nie zmieniono ich puli pytań ani kluczy odpowiedzi.
- Dodano snapshoty: `review/sequential/661-661.json` i `review/legal-clauses/661-661.json`.
- Ledger rozszerzono do `review/legal-polish/stage4w4-literal-verification-ledger-0610-0661.json`; dopisano ADR-B-0661 z literalnym porównaniem i recenzją specjalisty jako pending.
- Zaktualizowano oba manifesty specjalisty (0628/0638), rejestr, instrukcje recenzji, listę pozycji bez zapisanego cytatu i zagnieżdżone kolejki. Bieżące manifesty wskazują 661 pytań, 428 nierozstrzygniętych porównań z pełnym polskim tekstem urzędowym i 131 pozycji bez zapisanego dosłownego fragmentu MI.
- Rozkład prawidłowych odpowiedzi: A=228, B=221, C=212.
- Wskaźnik „poprawna odpowiedź jest jedyną najdłuższą”: 72/661 = 10,89%; maksimum działu 13,95%. Cel ≤18% spełniony.
- Wszystkie statusy pozostają `needs_review`; formalne zatwierdzenia i `verified`: 0.

## 6. Walidacja i ograniczenia wykonania

Zaktualizowano testy regresji utrzymujące licznik 661 rekordów, mapę pokrycia, wyjaśnienia i integralność pakietu recenzyjnego. Warianty egzaminów, snapshoty i manifesty mają wskazywać tę samą migawkę banku.

Lokalny checkout i terminal repo nie były dostępne w tej sesji, więc lokalnego PASS nie deklaruję. Pełny Quality Gate CI na PR pozostaje obowiązkową bramką przed scaleniem. Nie wolno scalać PR, dopóki wszystkie wymagane kontrole nie zakończą się PASS.

Zakres wyłącznie kurs podstawowy ADR; bez kursu cystern.
