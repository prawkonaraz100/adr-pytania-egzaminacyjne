# Etap 4x235 — odpowiedzialność cywilna przewoźnika w praktyce

Data: 31.10.2026. Zakres: wyłącznie kurs podstawowy ADR. Punkt wyjścia: świeży `main` `45a675cffdcc5bbb2ca198e957632e5c0d167003`, po scaleniu PR #703; bank 659 pytań, ostatnie ID ADR-B-0659.

## 1. Audyt luki

Kompetencja ADR-B-07-K07 „Podstawowe rozróżnienie odpowiedzialności cywilnej za szkodę i za niewykonanie zobowiązania” miała trzy pytania (ADR-B-0567–0569). Dotychczas sprawdzały ogólne przesłanki odpowiedzialności za szkodę, odpowiedzialność kontraktową i brak automatyzmu w przypisaniu odpowiedzialności. Brakowało czwartego pytania, które łączy te zasady z typową sytuacją z przewozu: przewoźnik zawarł umowę, a nieprawidłowe wykonanie czynności powierzono kierowcy.

Temat jest częścią programu szkolenia podstawowego: ADR 8.2.2.3.2(k) wymaga ogólnych informacji dotyczących odpowiedzialności cywilnej. Nie oznacza to, że ADR samodzielnie określa całość zasad odpowiedzialności cywilnej; w pytaniu zastosowano odpowiednie przepisy Kodeksu cywilnego.

## 2. Nowe pytanie ADR-B-0660

Dodano ADR-B-0660 do ADR-B-07-K07. Scenariusz dotyczy krajowej umowy przewozu, w której kierowca nie zabezpieczył ładunku, a kontrahent dochodzi odszkodowania od przewoźnika.

| Opcja | Długość | Ocena |
|---|---:|---|
| A | 121 | **Poprawna** — przewoźnik może odpowiadać wobec kontrahenta za nienależyte wykonanie umowy i działanie osoby, którą posłużył się przy wykonaniu zobowiązania. |
| B | 127 | Błędna — błędnie przenosi całą odpowiedzialność wyłącznie na kierowcę, pomijając odpowiedzialność dłużnika za osoby pomocnicze. |
| C | 127 | Błędna — błędnie uzależnia odpowiedzialność przewoźnika od osobistego prowadzenia pojazdu i zabezpieczania ładunku. |

Explanation ma 469 znaków i 4 zdania. Najpierw wyjaśnia, dlaczego przewoźnik może odpowiadać wobec kontrahenta, następnie wskazuje, dlaczego mylące są warianty przerzucające odpowiedzialność wyłącznie na kierowcę lub wyłączające przewoźnika, a na końcu zastrzega konieczność zbadania okoliczności i przepisów szczególnych. Poprawna odpowiedź A nie jest najdłuższa. Status: `needs_review`.

## 3. Podstawy prawne i granice pytania

- ADR 2025, 8.2.2.3.2(k) — w programie podstawowego szkolenia wymieniono ogólne informacje dotyczące odpowiedzialności cywilnej.
- Kodeks cywilny, tekst jednolity Dz.U. 2026 poz. 795, art. 471 — ogólna odpowiedzialność dłużnika za szkodę wynikłą z niewykonania lub nienależytego wykonania zobowiązania, z ustawowym zastrzeżeniem okoliczności, za które dłużnik nie odpowiada.
- Kodeks cywilny, art. 474 — dłużnik odpowiada jak za własne działanie lub zaniechanie za działania i zaniechania osób, z których pomocą wykonuje zobowiązanie, oraz osób, którym jego wykonanie powierza.
- Kodeks cywilny, art. 415 — ogólna zasada odpowiedzialności za szkodę wyrządzoną z własnej winy; pomaga odróżnić odpowiedzialność za czyn niedozwolony od odpowiedzialności kontraktowej.
- ADR 2025 ogłoszony w Dz.U. 2025 poz. 642: https://dziennikustaw.gov.pl/DU/2025/642
- Oficjalny tekst jednolity Kodeksu cywilnego, Dz.U. 2026 poz. 795: https://eli.gov.pl/eli/DU/2026/795/ogl

**Granica pytania:** to informacja ogólna do programu szkolenia, nie porada prawna i nie rozstrzygnięcie konkretnego roszczenia. W indywidualnym sporze trzeba ustalić stronę umowy, rodzaj szkody, związek przyczynowy, okoliczności odpowiedzialności i zastosowanie przepisów szczególnych. W zależności od przewozu mogą mieć zastosowanie także przepisy szczególne lub konwencje.

Pełne literalne porównanie wskazanego polskiego tekstu ADR 2025 ze sprostowaniem oraz niezależna recenzja specjalisty ADR pozostają otwarte. Nie oznaczono pytania jako `verified`.

## 4. Materiały dydaktyczne i mapa

- Mapa kompetencji: ADR-B-07-K07 ma teraz 4 pytania: ADR-B-0567–0569 i ADR-B-0660.
- Lekcja ADR-B-07: dodano proste omówienie odpowiedzialności przewoźnika za wykonanie umowy i przykład krajowego zlecenia.
- Materiał instruktora ADR-B-07: dodano symulację na fikcyjnym zleceniu i pytanie kontrolne o odpowiedzialność za działania kierowcy.
- Nie zmieniano istniejących pytań ani kluczy 0567–0569.

## 5. Synchronizacja po zmianie banku — pułapka #646

- Bank: 660 rekordów ADR-B-0001–0660, ID ciągłe i unikalne; wszystkie `needs_review`, 0 `verified`.
- Blob SHA `questions.jsonl`: `d900e67721ee4b9ef962a0a7479ecdcd2c6f01ec`.
- Warianty i klucze egzaminów próbnych 001–005 wskazują aktualny blob SHA; nie zmieniono ich puli pytań ani kluczy odpowiedzi.
- Dodano snapshoty: `review/sequential/660-660.json` i `review/legal-clauses/660-660.json`.
- Ledger rozszerzono do `review/legal-polish/stage4w4-literal-verification-ledger-0610-0660.json`; dopisano ADR-B-0660 ze statusem porównania literalnego i recenzji specjalisty jako pending.
- Zaktualizowano oba manifesty specjalisty (0628/0638), rejestr, instrukcje recenzji, listę pozycji bez zapisanego cytatu i zagnieżdżone kolejki. Bieżące manifesty wskazują bank 660 rekordów, 427 nierozstrzygniętych porównań z pełnym polskim tekstem urzędowym oraz 130 pozycji bez zapisanego dosłownego fragmentu MI.
- Rozkład prawidłowych odpowiedzi: A=228, B=220, C=212.
- Wskaźnik „poprawna odpowiedź jest jedyną najdłuższą”: 72/660 = 10,91%; maksimum działu 13,95%. Cel ≤18% spełniony.
- Wszystkie statusy pozostają `needs_review`; formalne zatwierdzenia i `verified`: 0.

## 6. Walidacja i ograniczenia wykonania

Zaktualizowano testy regresji utrzymujące licznik 660 rekordów, mapę pokrycia, wyjaśnienia i integralność pakietu recenzyjnego. Warianty egzaminów, snapshoty i manifesty mają wskazywać tę samą migawkę banku.

Lokalny checkout i terminal repo nie były dostępne w tej sesji, więc lokalnego PASS nie deklaruję. Pełny Quality Gate CI na PR pozostaje obowiązkową bramką przed scaleniem. Nie wolno scalać PR, dopóki wszystkie wymagane kontrole nie zakończą się PASS.

Zakres wyłącznie kurs podstawowy ADR; bez kursu cystern.
