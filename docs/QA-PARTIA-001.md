# Audyt kontrolny partii 001 — 39 pytań (ADR podstawowy)

## Stan i zakres

Data zapisu: 22 października 2026.

- Bank: `podstawowy/questions.jsonl`
- Liczba rekordów: **39**
- Pokrycie: **13 z 13** tematów urzędowego programu (po 3 przykłady na temat).
- Statusy: **39 needs_review / 0 verified / 0 blocked**.
- Duplikaty identyfikatorów i dosłownych pytań: brak w pierwszym kontrolnym odczycie.
- Każdy rekord ma trzy odpowiedzi i jedno pole correct_option.
- Każdy rekord wskazuje ADR 2025 oraz punkt do recenzji.
- Rekordy nie mogą być używane w egzaminach produkcyjnych przed zatwierdzeniem.

## Kategorie ryzyka do audytu

| Pytania | Priorytet | Co sprawdzić |
|---|---|---|
| ADR-B-0001 do 0003 | wysoki | Wyłączenia szkoleniowe i zakres kierowców objętych zaświadczeniem |
| ADR-B-0004 do 0006 | średni | Numery klas i dokładne brzmienie punktu 2.2.43 |
| ADR-B-0007 do 0009 | wysoki | Kiedy stosuje się znak środowiskowy i zapis ODPAD; stan pojazdu po wycieku |
| ADR-B-0010 do 0012 | średni | Zakaz palenia/e-papierosów i wyjątek od wyłączania silnika |
| ADR-B-0013 do 0015 | średni | Instrukcje pisemne oraz wyposażenie awaryjne |
| ADR-B-0016 do 0018 | średni | Wymiary tablic, litera X, warunki zmniejszenia tablic |
| ADR-B-0019 do 0021 | średni | Odpowiedzialność nadawcy, przewoźnika i załadowcy |
| ADR-B-0022 do 0024 | wysoki | Masa pojazdu, rodzaje gaśnic, zwolnienia, PPE |
| ADR-B-0025 do 0027 | wysoki | Ładunki mieszane, żywność, zasady zabezpieczenia |
| ADR-B-0028 do 0030 | wysoki | Stosowanie IMDG i obowiązki na odcinku drogowym |
| ADR-B-0031 do 0033 | wysoki | Tunele A–E, kod D/E, ilości i przypadki wyjątku |
| ADR-B-0034 do 0036 | średni | Ochrona osób i towarów, wymagany identyfikator ze zdjęciem |
| ADR-B-0037 do 0039 | średni | Zawartość dokumentu, czterostronicowy wzór instrukcji |

## Bramka jakości

- [x] Zapis w repozytorium 39 rekordów ze spójną strukturą.
- [x] Wstępna kontrola składni JSONL i formatu pól w niezależnym odczycie z GitHub: brak uwag.
- [ ] **Formalny** walidator Python uruchomiony na HEAD.
- [ ] Testy Python na HEAD: wszystkie PASS.
- [ ] GitHub Actions na HEAD: status success.
- [ ] Pełna kontrola aktów prawnych i sprostowań.
- [ ] Recenzja eksperta ADR.
- [ ] Wszystkie pytania gotowe do publikacji.

## Krytyczne ograniczenie

**Kontrola schematu nie sprawdza prawdziwości prawa.** `verified` może zostać nadany dopiero po sprawdzeniu źródła, wyjątku, poprawnej odpowiedzi i wyjaśnienia, z zapisem daty oraz recenzenta.
