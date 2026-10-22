# Audyt partii 007A — dodatkowe pytania sytuacyjne ADR-B-0177–0196

**Data:** 2026-10-22  
**Zakres:** 20 autorskich pytań (etap pogłębiania nauki kierowców).  
**Status:** kontrola redakcyjna z przypisanym źródłem; **brak końcowej recenzji eksperckiej, wszystkie `needs_review`**.

## Cel i metoda

Na początek etapu mieliśmy 40 ze 103 zagadnień teoretycznych z zaledwie jednym pytaniem. Nowa partia zwiększa liczbę różnych zadań dotyczących **20 z tych zagadnień**. Nie oceniamy tylko pamięci pojęć, ale decyzję kierowcy w konkretnej sytuacji. W banku jest po tej zmianie 196 pytań, a 20 celów teoretycznych nadal ma mniej niż dwa pytania.

Każda treść zawiera kontekst i dwie niepoprawne odpowiedzi. Podany `reference` identyfikuje fragment ADR wymagający końcowego porównania. Wykorzystano ADR 2025 (tomy i indeksowana treść) oraz aktualne źródła władz. **Nie oznacza to, że każdy zapis lub dystraktor został już zweryfikowany niezależnie z urzędowym tekstem polskim.**

## Mapa audytu pytań

| ID | Kompetencja | Wskazany ustęp ADR 2025 | Szczególna uwaga do recenzji | Status |
|---|---|---|---|---|
| ADR-B-0177 | ADR-B-03-K03 | ADR 2025, 7.5.8.1 | Przewóz do miejsca czyszczenia i zabezpieczenie wycieku; dokładne warunki | needs_review |
| ADR-B-0178 | ADR-B-03-K05 | ADR 2025, 5.4.3.4 | Czynności wyłącznie gdy właściwe i bezpieczne; nie przekraczać roli załogi | needs_review |
| ADR-B-0179 | ADR-B-03-K06 | ADR 2025, 5.4.1.1.1; 5.4.1.1.3.1 | Pełny punkt ADR, wyjątki i wiarygodność dystraktorów | needs_review |
| ADR-B-0180 | ADR-B-04-K05 | ADR 2025, 5.4.3.4 | Czynności wyłącznie gdy właściwe i bezpieczne; nie przekraczać roli załogi | needs_review |
| ADR-B-0181 | ADR-B-04-K06 | ADR 2025, 8.4.1 | Warunki zastosowania reżimu nadzoru i kolejność miejsc | needs_review |
| ADR-B-0182 | ADR-B-05-K02 | ADR 2025, 5.4.3.4 | Czynności wyłącznie gdy właściwe i bezpieczne; nie przekraczać roli załogi | needs_review |
| ADR-B-0183 | ADR-B-05-K04 | ADR 2025, 5.4.3.4 | Czynności wyłącznie gdy właściwe i bezpieczne; nie przekraczać roli załogi | needs_review |
| ADR-B-0184 | ADR-B-05-K06 | ADR 2025, 5.4.3.4 | Czynności wyłącznie gdy właściwe i bezpieczne; nie przekraczać roli załogi | needs_review |
| ADR-B-0185 | ADR-B-05-K07 | ADR 2025, 5.4.3.4 | Czynności wyłącznie gdy właściwe i bezpieczne; nie przekraczać roli załogi | needs_review |
| ADR-B-0186 | ADR-B-05-K09 | ADR 2025, 5.4.3.4 | Czynności wyłącznie gdy właściwe i bezpieczne; nie przekraczać roli załogi | needs_review |
| ADR-B-0187 | ADR-B-05-K11 | ADR 2025, 5.4.3.4; program szkolenia praktycznego | Czynności wyłącznie gdy właściwe i bezpieczne; nie przekraczać roli załogi | needs_review |
| ADR-B-0188 | ADR-B-06-K01 | ADR 2025, 5.2.1.1 | Warunkowe oznakowanie, tabela A i nalepki dodatkowe | needs_review |
| ADR-B-0189 | ADR-B-06-K02 | ADR 2025, 3.2 tabela A kol. (5); 5.2.2.1 | Warunkowe oznakowanie, tabela A i nalepki dodatkowe | needs_review |
| ADR-B-0190 | ADR-B-06-K03 | ADR 2025, 5.3.2.2.2 | Umiejscowienie, trwałość i wymiar oznakowania; wyjątki | needs_review |
| ADR-B-0191 | ADR-B-06-K05 | ADR 2025, 5.3.2.2.1 | Umiejscowienie, trwałość i wymiar oznakowania; wyjątki | needs_review |
| ADR-B-0192 | ADR-B-06-K06 | ADR 2025, 5.3.2.3.1 | Umiejscowienie, trwałość i wymiar oznakowania; wyjątki | needs_review |
| ADR-B-0193 | ADR-B-06-K07 | ADR 2025, 5.3.2.2.2 | Umiejscowienie, trwałość i wymiar oznakowania; wyjątki | needs_review |
| ADR-B-0194 | ADR-B-06-K08 | ADR 2025, 5.3.2.3.1 | Umiejscowienie, trwałość i wymiar oznakowania; wyjątki | needs_review |
| ADR-B-0195 | ADR-B-07-K04 | ADR 2025, 1.4.2.3.2 | Obowiązki odbiorcy, naruszenie dot. kontenera | needs_review |
| ADR-B-0196 | ADR-B-07-K06 | ADR 2025, 8.3.1 | Zakres zakazu osób niebędących załogą | needs_review |

## Zidentyfikowane pułapki i zastosowane poprawne rozróżnienia

- **7.5.8.1:** po wycieku z przewożonej sztuki przesyłki wymaga się oczyszczenia przed ponownym załadunkiem. Gdy nie można czyścić lokalnie, możliwy jest bezpieczny przewóz do najbliższego odpowiedniego miejsca, a nie dowolny kolejny załadunek. [Tekst ADR 2025](https://lerem.org/wp-content/uploads/2025/01/ADR2025_Vol2e.pdf).
- **1.4.2.3.2:** odbiorca po wykryciu naruszenia wymagań dotyczących kontenera ma doprowadzić do jego usunięcia przed oddaniem kontenera przewoźnikowi. [Tekst ADR 2025](https://www.mindop.sk/fileadmin/documents/doprava/nebezpecnetovary/cesta/ADR_2025_Vol._I._EN.pdf).
- **5.3.2.2:** na numerowanej tablicy górny numer dotyczy zagrożenia, dolny numer UN; w 5.3.2.2.1 przewidziano 300 × 120 mm jako minimum dla określonych przypadków braku miejsca. Jest to **wyjątek warunkowy**, nie dowolne skalowanie. [ADR 2025, tom II](https://www.euraca.eu/media/frmeo2lm/adr-2025-vol-ii.pdf).
- **5.4.3.4:** działania załogi muszą odpowiadać treści czterostronicowych instrukcji pisemnych oraz bezpieczeństwu ludzi. [UNECE: wzory instrukcji](https://unece.org/transport/road-transport/linguistic-versions-adr-instructions-writing).
- **8.4.1:** warunki postoju wynikają z zastosowania szczególnych wymagań, nie z samego faktu przewozu dowolnej ilości towaru niebezpiecznego.

## Bramka odbioru

- [x] 20 dodatkowych pytań ma trzy opcje A/B/C, wyjaśnienia i wskazane przepisy.
- [x] 20 dodatkowych pytań jest przypisanych do właściwej kompetencji.
- [ ] Recenzja fachowca w zakresie każdego poprawnego i obu błędnych wariantów oraz wszystkich warunków wyjątku.
- [ ] Porównanie pełnego polskiego brzmienia aktu **Dz.U. 2025 poz. 642** i sprostowania **poz. 1575**, odrębnie dla każdego pytania.
- [ ] Potwierdzenie PASS CI na ostatnim commicie PR i kontrolny odczyt po scaleniu.
- [ ] Zwiększenie liczby pytań w pozostałych 20 słabiej reprezentowanych celach.
- [ ] Audyt semantycznych podobieństw w całym banku 196 pytań.
- [ ] Niezależny podpis i rzeczywista data recenzenta przed nadaniem statusu `verified`.

## Podstawa prawna

- [Dz.U. 2025 poz. 642](https://dziennikustaw.gov.pl/DU/2025/642).
- [Sprostowanie Dz.U. 2025 poz. 1575](https://eli.gov.pl/api/acts/DU/2025/1575/text.pdf).
- [Ministerstwo Infrastruktury — ADR 2025 (pomocnicze tomy PL)](https://www.gov.pl/web/infrastruktura/towary-niebezpieczne).

**Kluczowe:** `needs_review` jest statusem roboczym. Quality Gate strukturalny nie sprawdza samodzielnie prawdziwości twierdzeń prawnych.
