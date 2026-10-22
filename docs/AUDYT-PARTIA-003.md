# Audyt roboczy partii 003 — ADR-B-0071–0090

**Data:** 2026-10-22  
**Charakter:** własny materiał treningowy do kursu podstawowego kierowców, NIE urzędowa baza pytań.  
**Status:** 20 nowych pytań `needs_review`; bank łącznie **90**, `verified = 0`.

## Dlaczego ta partia jest inna?

W poprzednich 70 pytaniach istniały błędne odpowiedzi niezwiązane z ADR (np. karta stacji paliw czy lakier pojazdu). To zaniża trudność egzaminu. Zastąpiono **22 zestawy dystraktorów** bardziej zbliżonymi do rzeczywistych pomyłek. Na dalszym etapie należy podobnie przejrzeć resztę bazy. **Poprawienie dystraktora nie jest potwierdzeniem prawidłowości prawnej pytania.**

Pierwotny rozkład liter w bazie 90 pytań: **A=57, B=24, C=9**. Rozkład po przestawieniu wariantów przy zachowaniu poprawnych *tekstów* i kluczy: **A=30, B=30, C=30**. Zmiana pozycji prawidłowej odpowiedzi w 27 pytaniach nie zmieniła treści pytania ani znaczenia odpowiedzi. Dodano test automatyczny odrzucający koncentrację >55% poprawnych odpowiedzi na jednej literze, gdy bank ma co najmniej 30 pytań.

## Pytania sytuacyjne i źródła

| ID | Punkt ADR 2025 | Co ćwiczymy | Uwagi do niezależnej recenzji |
|---|---|---|---|
| ADR-B-0071 | 8.1.4.1 | Gaśnice: DMC 3,5 t → 4 kg łącznie | Odróżniać łączną pojemność od minimalnej pojemności pojedynczej |
| ADR-B-0072 | 8.1.4.1 | Gaśnice: DMC 6 t → 8 kg | Sprawdzić rozkład 2+6 kg i minimum dwóch gaśnic |
| ADR-B-0073 | 8.1.4.2 | Zwolnienie 1.1.3.6 → minimum jedna gaśnica 2 kg | Nie stosować automatycznie do wszystkich innych zwolnień |
| ADR-B-0074 | 8.1.4.4–5 | Termin ważności przeglądu gaśnicy | Sprawdzić wymogi oznaczeń wg krajowych zasad |
| ADR-B-0075 | 8.1.5.2 | Kamizelki dla każdego członka załogi | Uwzględnić stosowalność 8.1.5.1 |
| ADR-B-0076 | 8.1.5.2 | Ochrona oczu | Nie mylić ze zwykłymi okularami |
| ADR-B-0077 | 8.1.5.3 | Maska ucieczkowa: 2.3 lub 6.1 | Nie mylić z aparatem oddechowym dla ratownika |
| ADR-B-0078 | 7.5.7.2 | Piętrzenie opakowań | Konstrukcja opakowania, nie nalepka, rozstrzyga |
| ADR-B-0079 | 7.5.7.1 | Nadmierne naprężenie pasów | Ograniczenie uszkadzania opakowań |
| ADR-B-0080 | 7.5.8.1 | Wycieki po rozładunku | Czyszczenie przed kolejnym załadunkiem |
| ADR-B-0081 | 7.5.4 (c) | Separacja od żywności 0,8 m | To jedna z opcji separacji, nie jedyna |
| ADR-B-0082 | 7.5.4 | Towary oznaczone 6.1 i żywność | Warunki oddzielenia oraz zakres nalepki |
| ADR-B-0083 | 8.6.4 | Kod E w tunelu E | Upewnić się, że ograniczenie dotyczy przewozu |
| ADR-B-0084 | 8.6.4 | D/E w sztukach przesyłek w tunelu D | Rozróżnić sztuki przesyłek od cystern/luzem |
| ADR-B-0085 | 8.6.3.3 | Wyłączenia 1.1.3 w ograniczeniach tunelowych | **Poprawiono z uwzględnieniem wyjątku 3.4.13 i 3.4.14** |
| ADR-B-0086 | 8.6.3.2 | Najbardziej restrykcyjny kod kilku towarów | Doprecyzować warunki przejazdu |
| ADR-B-0087 | 8.1.2.1 (d) | Dokument ID ze zdjęciem | Nie zawsze wystarczy identyfikator firmowy |
| ADR-B-0088 | 5.4.3.4 | Pisemne instrukcje według wzoru | Notatka kierowcy nie jest substytutem |
| ADR-B-0089 | 5.4.1.1.7 | Wpis przy 1.1.4.2.1 | Zweryfikowano literalne polskie brzmienie |
| ADR-B-0090 | 8.1.2.3 | Dostępność instrukcji w kabinie | Zgodność z 5.4.3 |

## Podstawy w materiałach i numery stron

- [Polski tom II ADR 2025, MI](https://www.gov.pl/attachment/b7292c03-ac9d-4f80-9a29-c22f53d847b8): s. 260 (wpis multimodalny, 5.4.1.1.7); s. 602 (7.5.4); s. 604 (7.5.7, 7.5.8); s. 619–620 (8.1.2, 8.1.4, 8.1.5); s. 633–634 (8.6.3–8.6.4).
- [Źródło prawa: Dz.U. 2025 poz. 642](https://dziennikustaw.gov.pl/DU/2025/642), wraz ze [sprostowaniem poz. 1575](https://eli.gov.pl/eli/DU/2025/1575/ogl/pol/pdf).
- PDF z MI jest **pomocniczy**, natomiast źródłem prawa w Polsce jest tekst ogłoszony w Dzienniku Ustaw.

## Pozostające bramki

- [x] Opracowano 20 pytań praktycznych i zidentyfikowano punkty prawne.
- [x] Zmieniono 22 zestawy niewiarygodnych odpowiedzi i wyrównano klucze.
- [x] Odrębna kontrola JSON: 90 pytań, 13 działów, unikalne ID, rozkład A/B/C 30/30/30.
- [ ] Udokumentowana niezależna recenzja prawna 90 pytań, weryfikacja zgodności z tekstem ogłoszonym i poprawności dystraktorów.
- [ ] Potwierdzony test Python na commicie PR.
- [ ] Potwierdzony PASS GitHub Actions na commicie PR, a osobno na końcowym HEAD main.
- [ ] Dopiero potem nadanie `verified` i publikacja szkoleniowa.

**Wniosek:** techniczne przejście walidatora nie dowodzi merytorycznej prawidłowości 90 odpowiedzi. 
