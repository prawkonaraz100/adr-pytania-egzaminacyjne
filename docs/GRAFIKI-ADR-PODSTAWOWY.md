# Etap 4c — autorskie grafiki ADR podstawowego

**Cel:** obrazy poglądowe służą rozpoznawaniu znaków, nie rzeczywistemu oznakowaniu pojazdów ani opakowań. Dokument do recenzji specjalisty ADR. Podstawa: ADR 2025 w Dz.U. 2025 poz. 642 i sprostowanie poz. 1575.

## Standard projektowy

Grafiki wykonujemy samodzielnie jako SVG (widok 640×480), bez zewnętrznych fontów, logotypów, fotografii, skanów lub kopiowania cudzych rysunków. Każdy plik musi mieć dostępne `<title>` i `<desc>`, właściwy kontrast oraz komunikat „schemat edukacyjny — nie do stosowania na pojeździe”. Sprawdzamy kształty i barwy według ADR 2025 przed uznaniem ilustracji za wystarczająco dokładną.

Różnice obowiązkowe w rysunkach: **nalepka ostrzegawcza** nie jest tym samym co znak LQ lub EQ; kod E0 w tabeli A nie jest wzorem znaku EQ; górny numer zagrożenia na tablicy pomarańczowej jest różny od dolnego numeru UN; kategoria tunelu i kod ograniczenia tunelowego są odrębnymi informacjami. Nie umieszczamy w grafice odpowiedzi, jeśli miałoby to wypaczać test.

Ścieżkę w polu `image` wpisujemy **dopiero gdy wskazany plik naprawdę istnieje w repo**; zmiana pola oznacza aktualizację obu historycznych migawek audytu, kontrolę praw i pełny CI. Pytania i ilustracje pozostają `needs_review`.

## Istniejące pliki w polu `image`

| Pytanie | Obraz | Kontrola |
|---|---|---|
| ADR-B-0255 | `assets/adr-original/adr-b-0255-orange-33-1203.svg` | oryginalny schemat, do recenzji ADR |
| ADR-B-0256 | `assets/adr-original/adr-b-0256-orange-x.svg` | oryginalny schemat, do recenzji ADR |
| ADR-B-0260 | `assets/adr-original/adr-b-0260-eq-e0-table.svg` | oryginalny schemat, do recenzji ADR |
| ADR-B-0262 | `assets/adr-original/adr-b-0262-tunnel-e.svg` | oryginalny schemat, do recenzji ADR |
| ADR-B-0268 | `assets/adr-original/adr-b-0268-label-4-1.svg` | oryginalny schemat, do recenzji ADR |
| ADR-B-0270 | `assets/adr-original/adr-b-0270-label-5-1.svg` | oryginalny schemat, do recenzji ADR |
| ADR-B-0273 | `assets/adr-original/adr-b-0273-lq-mark.svg` | oryginalny schemat, do recenzji ADR |
| ADR-B-0504 | `assets/adr-original/adr-b-0504-hin-leading-5.svg` | oryginalny schemat, do recenzji ADR |

## Kolejka nowych grafik — bez przypisywania fikcyjnych ścieżek

| Pytanie | Typ | Specyfikacja | Planowana ścieżka |
|---|---|---|---|
| ADR-B-0016 | orange_plate | dwa pola; dolny numer UN | `assets/adr-original/adr-b-0016-visual.svg` |
| ADR-B-0017 | orange_plate | znak X przed górnym numerem | `assets/adr-original/adr-b-0017-visual.svg` |
| ADR-B-0018 | orange_plate | standardowe wymiary tablicy | `assets/adr-original/adr-b-0018-visual.svg` |
| ADR-B-0192 | orange_plate | podwojona cyfra 3 | `assets/adr-original/adr-b-0192-visual.svg` |
| ADR-B-0194 | orange_plate | cyfra 8 w numerze zagrożenia | `assets/adr-original/adr-b-0194-visual.svg` |
| ADR-B-0289 | hazard_label | nalepka 6.1 czaszka i piszczele | `assets/adr-original/adr-b-0289-visual.svg` |
| ADR-B-0161 | hazard_label | nalepka klasy 8 | `assets/adr-original/adr-b-0161-visual.svg` |
| ADR-B-0151 | hazard_label | nalepka 2.3 | `assets/adr-original/adr-b-0151-visual.svg` |
| ADR-B-0162 | hazard_label | wzór 9A | `assets/adr-original/adr-b-0162-visual.svg` |
| ADR-B-0266 | hazard_label | nalepka 5.1 | `assets/adr-original/adr-b-0266-visual.svg` |
| ADR-B-0149 | LQ | znak LQ oraz osobno limit z kolumny 7a | `assets/adr-original/adr-b-0149-visual.svg` |
| ADR-B-0033 | tunnel | kod D/E i tunel kategorii E | `assets/adr-original/adr-b-0033-visual.svg` |
| ADR-B-0322 | tunnel_LQ | oznaczenie LQ i tunel E | `assets/adr-original/adr-b-0322-visual.svg` |
| ADR-B-0433 | tunnel | znak tunelu E | `assets/adr-original/adr-b-0433-visual.svg` |
| ADR-B-0505 | orange_plate | cyfra 9; bez wymyślonego numeru UN | `assets/adr-original/adr-b-0505-visual.svg` |
| ADR-B-0045 | environmental_mark | oznaczenie materiału zagrażającego środowisku | `assets/adr-original/adr-b-0045-visual.svg` |

## Karta odbioru przed użyciem

1. Zidentyfikuj dokładny przepis 3.4/3.5/5.2/5.3/8.6, klasę i wyjątki.
2. Potwierdź autorstwo SVG bez cudzych zasobów.
3. Sprawdź kształty, proporcje, kolory, numery, znaki oraz tekst alternatywny na podstawie urzędowego polskiego ADR 2025.
4. Potwierdź, że ilustracja nie jest używana jako rzeczywiste oznakowanie ani jako zamiennik tablicy ADR.
5. Zapisz wynik recenzji grafiki oddzielnie od recenzji merytorycznej pytania.

**Zrealizowane w tej partii:** autorski schemat `assets/adr-original/adr-b-0504-hin-leading-5.svg` został dodany i wpisany do pola `image` ADR-B-0504. Pokazuje początek numeru zagrożenia „50”; dolny numer UN jest celowo zakryty. Zaktualizowano dokładne migawki audytu. Pozostałe propozycje są specyfikacjami, nie gotowymi obrazami.
