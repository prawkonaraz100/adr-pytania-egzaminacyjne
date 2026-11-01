# Etap 4x263 — oznakowanie opakowania zbiorczego i numer UN

Data: 01.11.2026  
Zakres: wyłącznie kurs podstawowy ADR  
Baza: main `f6bce8276cf56bc86c2bde9833cf27032fa15d71`  
Nowe ID: `ADR-B-0689`  
Kompetencja: `ADR-B-06-K01` — numer UN na sztuce przesyłki

## Wybór luki

Kompetencja miała cztery pytania o zapis numeru UN na sztuce przesyłki i rozpoznanie towaru na podstawie numeru UN. Nie obejmowała sytuacji, w której opakowanie zbiorcze całkowicie zasłania oznaczenia przesyłki. Nowe pytanie sprawdza obowiązek odtworzenia na zewnątrz numeru UN i pozostałych wymaganych oznaczeń, gdy nie są widoczne. Nie powiela pytań o opakowania w ilościach ograniczonych ani wyłączonych — te mają odrębne przepisy.

## Dodane pytanie

- `ADR-B-0689`: folia opakowania zbiorczego zasłania numer UN i nalepki zagrożeń jednej sztuki przesyłki ADR.
- Klucz: **B** — umieścić napis „OVERPACK” oraz odtworzyć na zewnątrz numer UN i inne wymagane oznaczenia i nalepki, których nie widać.
- Explanation: **431 znaków, 4 zdania**; wyjaśnia, dlaczego niewidoczne oznaczenia trzeba powtórzyć, oraz dlaczego sam napis lub dokument przewozowy nie wystarczają.
- Długości odpowiedzi A/B/C: **142/126/108** znaków. Poprawna B nie jest ani najdłuższa, ani najkrótsza.
- Status: `needs_review`; nie zmieniono statusu żadnego pytania na `verified`.

## Podstawa prawna

- **ADR 2025, 5.1.2.1(a)(i)** — jeżeli oznaczenia i nalepki reprezentujące wszystkie towary w opakowaniu zbiorczym nie są widoczne, opakowanie zbiorcze oznacza się napisem „OVERPACK” (wysokość liter co najmniej 12 mm).
- **ADR 2025, 5.1.2.1(a)(ii)** — na zewnątrz umieszcza się numer UN i inne wymagane oznaczenia oraz nalepki dla każdego rodzaju towaru znajdującego się w opakowaniu zbiorczym; każdy rodzaj znaku lub nalepki wystarczy umieścić raz.
- Dz.U. 2025 poz. 642: https://dziennikustaw.gov.pl/DU/2025/642
- Oficjalny tekst polski ADR tom II 2025, Ministerstwo Infrastruktury: https://www.gov.pl/attachment/b7292c03-ac9d-4f80-9a29-c22f53d847b8
- Tekst ADR 2025, tom II: https://www.mindop.sk/fileadmin/documents/doprava/nebezpecnetovary/cesta/ADR_2025_Vol._II._EN.pdf

Pytanie dotyczy standardowego opakowania zbiorczego, w którym wymagane oznaczenia nie są widoczne. Nie obejmuje szczególnych wyjątków dla ilości ograniczonych i wyłączonych ani odrębnych zasad dla materiałów promieniotwórczych. Pełne literalne porównanie z właściwym tekstem Dz.U. oraz niezależna recenzja specjalisty pozostają pending. Pytanie pozostaje `needs_review`.

## Synchronizacja #646

- Bank: **689** pytań ADR-B-0001–0689; wszystkie `needs_review`, 0 `verified`.
- Blob SHA `questions.jsonl`: `d607ae33a6268223f289fd94599f289c6115c9ce`.
- Rozkład prawidłowych opcji: **A=236 / B=236 / C=217**.
- „Poprawna = jedyna najdłuższa”: **72/689 = 10,45%**, poniżej limitu Quality Gate 18%; maksimum działu 13,95%.
- `ADR-B-06-K01` ma teraz 5 pytań; moduł ADR-B-06 ma 57 pytań.
- Zaktualizowano klucze i warianty egzaminów próbnych 001–005 do aktualnego SHA; dodano snapshoty `review/sequential/689-689.json` i `review/legal-clauses/689-689.json`; zaktualizowano ledger, manifesty, kolejki recenzenckie, mapę kompetencji, lekcję i materiał instruktora.
- PR i CI: do potwierdzenia po otwarciu PR. Nie uruchomiono lokalnego Quality Gate.

## Pliki audytowe

- Rejestr: `review/specialist/REJESTR-0689-0689.md`
- Ledger: `review/legal-polish/stage4w4-literal-verification-ledger-0610-0678.json`
- Snapshot sekwencyjny: `review/sequential/689-689.json`
- Snapshot prawny: `review/legal-clauses/689-689.json`
