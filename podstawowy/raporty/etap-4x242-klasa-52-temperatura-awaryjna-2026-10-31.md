# Etap 4x242 — klasa 5.2: temperatura awaryjna nadtlenków organicznych

Data: 31.10.2026. Zakres: wyłącznie kurs podstawowy ADR. Punkt wyjścia: świeży `main` `d12c654c4e26a5e91ef57b193d68ad88e4329149`, 666 pytań, ostatnie ID ADR-B-0666.

## 1. Luka pokrycia

Kompetencja ADR-B-02-K08 „Klasa 5.2: nadtlenki organiczne” miała cztery pytania: rozpoznanie klasy, odróżnienie od 5.1, ogólne ryzyko rozkładu pod wpływem ciepła i rozpoznanie klasy na oznaczeniu. Brakowało sytuacyjnego pytania o różnicę między temperaturą kontrolowaną i awaryjną oraz reakcję kierowcy po osiągnięciu progu awaryjnego. Dodano scenariusz praktyczny ADR-B-0667.

## 2. Nowe pytanie ADR-B-0667

Podczas przewozu nadtlenku organicznego klasy 5.2 czujnik wskazuje osiągnięcie temperatury awaryjnej podanej w dokumentacji. Prawidłowe działanie: niezwłocznie uruchomić przewidziane procedury awaryjne.

| Opcja | Długość | Ocena |
|---|---:|---|
| A | 147 | **Poprawna** — temperatura awaryjna oznacza próg uruchomienia procedur. |
| B | 133 | Błędna — myli próg awaryjny z temperaturą kontrolowaną i każe zwlekać z reakcją. |
| C | 172 | Błędna — traktuje próg jako zalecenie i proponuje improwizowane chłodzenie zamiast procedury. |

Poprawna A nie jest najdłuższa. Explanation ma 400 znaków i 4 zdania; najpierw wyjaśnia działanie kierowcy, potem odróżnia temperaturę kontrolowaną od awaryjnej i objaśnia, dlaczego pozostałe odpowiedzi są błędne. Status `needs_review`.

## 3. Podstawa i źródła

- ADR 2025, 7.1.7.3.4 — temperatura kontrolowana to maksymalna temperatura, przy której substancja może być bezpiecznie przewożona; temperatura awaryjna to próg, przy którym należy wdrożyć procedury awaryjne.
- ADR 2025, 7.1.7.4.1 — po osiągnięciu temperatury awaryjnej należy rozpocząć procedury awaryjne; przepis wymienia też m.in. kontrolę stanu jednostki przed załadunkiem, regularne monitorowanie temperatury i przygotowanie na utratę kontroli.
- ADR 2025, 2.2.52.1.15–1.16 — które nadtlenki organiczne podlegają kontroli temperatury oraz odwołanie do warunków temperatur kontrolowanej i awaryjnej.
- Dz.U. 2025 poz. 642 (ADR 2025): https://dziennikustaw.gov.pl/DU/2025/642
- Polska strona objaśniająca CIOP, „Umowa międzynarodowa ADR”, opis 2.2.52.1.15–18 i znaczenia TSR oraz temperatur: https://www.ciop.pl/CIOPPortalWAR/appmanager/ciop/pl?_nfpb=true&_pageLabel=P48600114441551177218047&html_klucz=300010071&html_tresc_id=300010085&html_tresc_root_id=300010071
- Tekst ADR 2025, wydanie UNECE: https://unece.org/adr-2025-files

Uwaga recenzencka: polskie materiały CIOP są źródłem objaśniającym, nie zastępują wiążącego tekstu ogłoszonego w Dz.U. Literalne porównanie polskiego tekstu Dz.U. z dokładną stroną/cytatem i niezależna recenzja specjalisty ADR pozostają otwarte. Nie jest to zatwierdzenie prawne.

## 4. Synchronizacja i kontrola

- Bank: 667 pytań ADR-B-0001–0667, ID ciągłe i unikalne; wszystkie `needs_review`, 0 `verified`.
- Blob SHA banku: `4d3a2dd4c7c43ee9fc00d829981cac50098fc462`.
- Mapa: ADR-B-0667 przypisano do ADR-B-02-K08 (5 pytań w kompetencji); lekcja B-02 i materiał instruktora B-02 uzupełnione o temperaturę awaryjną.
- Warianty i klucze egzaminów próbnych 001–005 wskazują nowy blob SHA.
- Snapshoty: `review/sequential/667-667.json` i `review/legal-clauses/667-667.json`.
- Ledger: `review/legal-polish/stage4w4-literal-verification-ledger-0610-0667.json`; manifesty i obie kolejki priorytetowe zaktualizowane, w tym zagnieżdżone pola aktualnego SHA.
- Rozkład prawidłowych odpowiedzi A/B/C: 230/224/213.
- „Poprawna odpowiedź jest jedyną najdłuższą”: 72/667 = 10,79%; maksimum działu 13,95% — poniżej limitu 18%.

Ręcznie sprawdzono strukturę i ciągłość banku, statusy, przypisanie kompetencji, długości odpowiedzi i explanation, rozkład kluczy oraz SHA i snapshoty. Lokalny checkout repo nie był dostępny, więc nie deklaruję lokalnego uruchomienia Quality Gate. Pełny PASS CI na PR pozostaje obowiązkową bramką przed scaleniem.
