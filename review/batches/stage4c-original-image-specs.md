# Etap 4c — oryginalne specyfikacje grafik dla pytań rozpoznawczych

**Data:** 23.10.2026. Stan wejściowy: 506 pytań `needs_review`, 0 `verified`, brak otwartych PR. Etap nie zmienia żadnego pytania, odpowiedzi A/B/C, poprawnego klucza ani objaśnienia prawnego. Wprowadza jedynie siedem wartości niepustych w polu `image` i aktualizuje wynikające z tego migawki audytu.

## Materiały

| ID | Rodzaj | Oryginalna grafika | Podstawa do recenzji |
|---|---|---|---|
| ADR-B-0255 | tablica pomarańczowa 33/1203 | `assets/adr-original/adr-b-0255-orange-33-1203.svg` | ADR 5.3.2.2.2 |
| ADR-B-0256 | litera X na tablicy | `assets/adr-original/adr-b-0256-orange-x.svg` | ADR 5.3.2.3.1 |
| ADR-B-0260 | kod EQ E0 w kolumnie 7b | `assets/adr-original/adr-b-0260-eq-e0-table.svg` | ADR 3.5.1.2 |
| ADR-B-0262 | schemat tunelu E | `assets/adr-original/adr-b-0262-tunnel-e.svg` | ADR 1.9.5.3.6 i 8.6.4 |
| ADR-B-0268 | nalepka 4.1 | `assets/adr-original/adr-b-0268-label-4-1.svg` | ADR 5.2.2.2.2 |
| ADR-B-0270 | nalepka 5.1 | `assets/adr-original/adr-b-0270-label-5-1.svg` | ADR 5.2.2.2.2 |
| ADR-B-0273 | znak LQ | `assets/adr-original/adr-b-0273-lq-mark.svg` | ADR 3.4.7.1 |

Grafiki wykonano autorsko, bez pobierania cudzych plików. Są **szkicami edukacyjnymi**, nie dokumentacją produkcyjną znaków. SVG posiadają opisy dostępności i widok wektorowy. `assets/adr-original/specifications.json` zawiera identyfikatory, alt, podstawy prawne i status recenzji. Znak właściwy dla EQ 3.5.4.2 jest wyszczególniony jako przyszła specyfikacja bez mylącego przypisania do pytania 0260: **E0 nie stanowi pozwolenia na ilości wyłączone**.

Zaktualizowano dokładne migawki 7 rekordów w pięciu istniejących zakresach `review/sequential/` i `review/legal-clauses/`. `tests/test_original_image_assets.py` sprawdza istnienie plików, poprawność XML/SVG, brak zasobów zewnętrznych oraz zgodność rejestru specyfikacji z polem `image`.

**Brama publikacji:** wszystkie 506 pytań i ilustracje nadal oczekują na niezależną kontrolę polskiego ADR 2025 — Dz.U. poz. 642 oraz sprostowanie poz. 1575. Quality Gate potwierdza tylko integralność techniczną, nie uprawnienie do stosowania diagramów jako oficjalnych tablic lub znaków.
