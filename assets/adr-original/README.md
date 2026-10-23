# Oryginalne schematy wizualne ADR (etap 4c)

Opracowane samodzielnie od podstaw jako **wektorowe materiały dydaktyczne SVG** dla kursu podstawowego; nie kopiowano grafik z komercyjnych podręczników, fotografii stockowych, znaków wydrukowanych przez osoby trzecie ani plików pobranych z sieci. Podstawę do niezależnej kontroli stanowią przepisy ADR 2025.

**Nie są to zatwierdzone oznakowania do stosowania na pojazdach i opakowaniach.** Odrębnej weryfikacji wymagają: wymiary, proporcje, piktogramy, kolory/kontrast, grubość linii, umieszczenie oznaczeń, interpretacja X, znak LQ i szczególne wymagania dla opakowań.

## Siedem przypisanych obrazów

- `adr-b-0255-orange-33-1203.svg`: 33 nad 1203, 5.3.2.2.2.
- `adr-b-0256-orange-x.svg`: litera X w numerze zagrożenia; kropki w miejscu UN świadomie oznaczają schemat, a nie prawdziwą tablicę przewozową.
- `adr-b-0260-eq-e0-table.svg`: **ilustracja kodu E0 w tabeli 3.2, kol. 7b**. Nie przedstawia dopuszczonego znaku EQ i nie sugeruje, że E0 pozwala na EQ.
- `adr-b-0262-tunnel-e.svg`: kategoria E w edukacyjnej ilustracji tunelu, **nie urzędowy znak drogowy**.
- `adr-b-0268-label-4-1.svg`: uproszczona nalepka 4.1.
- `adr-b-0270-label-5-1.svg`: uproszczona nalepka 5.1.
- `adr-b-0273-lq-mark.svg`: czarno-biały znak LQ w ujęciu schematycznym.

Kompletna specyfikacja przypisań, tekstów alternatywnych i zastrzeżeń: [specifications.json](specifications.json). Standardowa grafika **EQ dla ilości wyłączonych** z ADR 3.5.4.2 figuruje jako osobna specyfikacja *do opracowania po prawnej weryfikacji*; nie zastępowano nią ilustracji E0, ponieważ byłoby to merytorycznie mylące.

## Zasady publikacji i dostępności

Każdy SVG zachowuje własny `title`, `desc` i `viewBox`. Materiały mają być używane z indywidualnym tekstem alternatywnym; interfejs nie powinien wymagać rozpoznawania jedynie koloru. Stan ilustracji: **draft / specialist review pending**, bez zatwierdzenia. Nie wykorzystywać w produkcyjnym teście, dopóki samo pytanie i ilustracja nie zostaną podpisane przez specjalistę ADR.

Źródła normatywne do audytu: [Dz.U. 2025 poz. 642](https://dziennikustaw.gov.pl/DU/2025/642), [sprostowanie poz. 1575](https://dziennikustaw.gov.pl/DU/2025/1575). Program kursu początkowego podstawowego: Dz.U. 2021 poz. 2150.
