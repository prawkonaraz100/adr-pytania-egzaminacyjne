# Etap 4x20 — audyt czytelności explanation ADR-B-0201–0250

- Punkt wyjścia: świeży main `b17010ad25783017ad675064dbdda5190373cc5d`.
- Zakres: 50 pytań ADR-B-0201–0250.
- Metoda: automatyczne wskazanie kandydatów i ręczna lektura pod kątem żargonu, początkującego kursanta i sensu błędnych opcji.

## Wynik

- Ręcznie przejrzano 50/50 explanation: ADR-B-0201–ADR-B-0250.
- Przepisano 4 explanation: ADR-B-0205, 0206, 0215 i 0220.
- Pozostałe 46 pozostawiono bez zmian. Siedem trafień heurystycznych uznano za fałszywe alarmy:
  - **ADR-B-0208** — kod D/E jest opisany jako kod ograniczeń tunelowych, a wyjaśnienie wskazuje sposób jego zastosowania.
  - **ADR-B-0211** — wyjaśnia, dlaczego sama nazwa odbiorcy i numer zamówienia nie potwierdzają upoważnienia.
  - **ADR-B-0228** — jasno wskazuje potrzebę łatwego dostępu do instrukcji i dlaczego telefon nie jest ich zamiennikiem.
  - **ADR-B-0240** — wyraźnie wyjaśnia zasadę czyszczenia i ograniczony wyjątek dla tego samego towaru.
  - **ADR-B-0242** — wyjaśnia, że ochronę odpływu wolno próbować tylko, jeśli jest odpowiednia i bezpieczna.
  - **ADR-B-0248** — numer UN jest objaśniony w nawiasie jako identyfikator towaru niebezpiecznego.
  - **ADR-B-0250** — trafienie wynikało z dopasowania fragmentu numeru przepisu 8.1.2.1, a nie z niewyjaśnionego terminu.

## Przykłady przed/po

1. **ADR-B-0205 — RID**
   - Przed: „Kolejowy odcinek transportu towarów niebezpiecznych podlega zasadom RID, a drogowy zasadom ADR...”
   - Po: dodano proste rozwinięcie RID jako przepisów dla kolejowego przewozu towarów niebezpiecznych i wyjaśniono, dlaczego zmiana środka transportu nie przenosi automatycznie przepisów z jednego odcinka na drugi.
   - Podstawa: ADR 1.1.4.2–1.1.4.3.

2. **ADR-B-0206 — IMDG**
   - Przed: „ADR może uznać wybrane wymagania morskiego IMDG...”
   - Po: objaśniono IMDG jako międzynarodowy kodeks przewozu towarów niebezpiecznych drogą morską i wskazano, że uznanie wymagań na drodze zależy od szczególnych warunków.
   - Podstawa: ADR 1.1.4.2.1.

3. **ADR-B-0220 — numer UN**
   - Przed: „...sam numer UN identyfikuje towar, lecz nie wyjaśnia, czy doszło do wycieku...”
   - Po: dopowiedziano, że numer UN to czterocyfrowy identyfikator towaru niebezpiecznego, i rozdzielono informację o towarze od opisu samego zdarzenia.
   - Podstawa: ADR 5.4.3.4.

## Wszystkie poprawione rekordy
- ADR-B-0205 — RID i ADR w transporcie łączonym.
- ADR-B-0206 — IMDG i warunki uznania wymagań morskich na drodze.
- ADR-B-0215 — adnotacja dla przewozu łączonego, numer UN i nazwa przewozowa.
- ADR-B-0220 — numer UN a opis zdarzenia przekazywany służbom.

## Integralność i metryki
- Bank: 609 rekordów, 609 unikalnych ID, 0 duplikatów.
- Explanation minimum: 300 znaków; 0 poniżej 300.
- Wszystkie pytania nadal `needs_review`; `verified`: 0.
- Wskaźniki „poprawna = jedyna najdłuższa” bez zmian:
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
- Zsynchronizowano arkusze i klucze 001–005 oraz snapshoty audytów sekwencyjnego i klauzulowego dla czterech zmienionych rekordów.
- Nie zmieniono opcji, poprawnych liter ani statusów prawnych.

## Ograniczenia
Kontrola językowa nie zastępuje recenzji prawnej. Wymagany jest PASS Quality Gate CI; lokalny checkout nie był dostępny w tym środowisku.
