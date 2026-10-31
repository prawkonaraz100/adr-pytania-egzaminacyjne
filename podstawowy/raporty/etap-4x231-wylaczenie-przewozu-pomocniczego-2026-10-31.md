# Etap 4x231 — wyłączenie dla przewozu pomocniczego przedsiębiorstwa

Data: 31.10.2026. Zakres: wyłącznie kurs podstawowy ADR. Punkt wyjścia: świeży `main` `00f4f89960a7a636134b91ee393a1da7397bded3`, bank 655 pytań, blob SHA `ca07d9e94b63ba6b9f832838e645500bd2964939`.

## 1. Audyt luki

Kompetencja ADR-B-01-K04 „Wyłączenia ze względu na charakter przewozu” miała cztery pytania: ogólne zasady małej ilości, wyłączenie osoby prywatnej, warunek opakowania detalicznego i przewóz na własny użytek. Wszystkie dotyczyły przede wszystkim wyłączenia z ADR 1.1.3.1(a). Brakowało praktycznego sprawdzenia odrębnego wyłączenia dla przedsiębiorstw, gdy przewóz jest czynnością pomocniczą wobec ich zasadniczej działalności — ADR 1.1.3.1(c).

## 2. Nowe pytanie ADR-B-0656

Dodano ADR-B-0656 do ADR-B-01-K04. Scenariusz opisuje firmę serwisową przewożącą 300 l towaru do naprawy własnego urządzenia na budowie. W treści wyraźnie podano, że przewóz jest pomocniczy, nie służy zaopatrzeniu ani dystrybucji, ilość mieści się w 1.1.3.6, opakowanie zabezpiecza przed wyciekiem, a towar nie należy do klasy 7.

| Opcja | Długość | Ocena |
|---|---:|---|
| A | 141 | **Poprawna** — przewóz pomocniczy może korzystać z wyłączenia, jeżeli spełniono wszystkie warunki przepisu. |
| B | 153 | Błędna — myli wyłączenie dla osób prywatnych z wyłączeniem dla przedsiębiorstw. |
| C | 137 | Błędna — traktuje limit 450 l jako warunek wystarczający i pomija pozostałe ograniczenia. |

Poprawna odpowiedź A nie jest najdłuższa. Explanation ma 410 znaków i 4 zdania: wyjaśnia, kiedy przewóz przedsiębiorstwa jest pomocniczy, wymienia limit 450 l, warunki 1.1.3.6, zabezpieczenie opakowania i wyłączenie klasy 7, a także wykluczenie zaopatrzenia i dystrybucji. Status: `needs_review`.

## 3. Źródła i zakres prawny

- ADR 2025, 1.1.3.1(c): wyłączenie dla przewozu przedsiębiorstw pomocniczego wobec zasadniczej działalności, przykłady dostaw/zwrotów na budowy i czynności serwisowych, limit 450 l na opakowanie, warunki ilościowe 1.1.3.6, zabezpieczenie przed uwolnieniem, wyłączenie klasy 7 oraz brak zastosowania do zaopatrzenia i dystrybucji.
- ADR 2025, 1.1.3.6: maksymalne ilości dla właściwej kategorii transportowej.
- Ogłoszenie: Dz.U. 2025 poz. 642 — https://dziennikustaw.gov.pl/DU/2025/642
- Sprostowanie: Dz.U. 2025 poz. 1575 — https://eli.gov.pl/api/acts/DU/2025/1575/text.pdf. Zakres sprostowania obejmuje m.in. 1.8.5.3, 1.8.6.2.1, 2.2.9.3 i wskazane elementy 3.2.1; nie wskazuje 1.1.3.1(c).
- Oficjalna strona Ministerstwa Infrastruktury wskazuje polskie tomy ADR 2025 i wyjaśnia, że źródłem prawa jest tekst ogłoszony w Dzienniku Ustaw: https://www.gov.pl/web/infrastruktura/towary-niebezpieczne

W tym etapie sprawdzono zakres sprostowania i wskazane przepisy w źródłach. Pełne, literalne porównanie polskiego tekstu urzędowego z egzemplarzem PDF oraz niezależna recenzja specjalisty ADR pozostają otwarte; ledger dla 0656 nie jest zatwierdzeniem prawnym.

## 4. Materiały i synchronizacja

- Mapa: ADR-B-0656 przypisano do ADR-B-01-K04 (5 pytań w kompetencji).
- Lekcja i materiał instruktora ADR-B-01: dodano praktyczne omówienie i ćwiczenie rozpoznawania warunków wyłączenia.
- Bank: 656 rekordów ADR-B-0001–0656, ID ciągłe i unikalne; wszystkie `needs_review`, 0 `verified`.
- Blob SHA banku: `940d22f1a3965796d24029e621b05253ff98ece4`.
- Rozkład prawidłowych odpowiedzi: A=224, B=220, C=212.
- Wskaźnik „poprawna odpowiedź jest jedyną najdłuższą”: 72/656 = 10,98%; maksimum działu 13,95%.
- Warianty i klucze egzaminów próbnych 001–005 wskazują nowy blob SHA banku.
- Snapshoty dodano jako `review/sequential/656-656.json` i `review/legal-clauses/656-656.json`.
- Ledger rozszerzono do `review/legal-polish/stage4w4-literal-verification-ledger-0610-0656.json`; manifesty 0628/0638, kolejki recenzji i rejestr pozycji bez cytatu zaktualizowano do 656 rekordów.

## 5. Walidacja i ograniczenia wykonania

Ręcznie sprawdzono strukturę JSONL, ciągłość i unikalność ID, statusy, przypisanie kompetencji, rozkład odpowiedzi, długości A/B/C i explanation oraz synchronizację egzaminów, snapshotów i manifestów. Lokalny checkout i terminal repo nie były dostępne w tej sesji, więc lokalnego PASS nie deklaruję. Pełny Quality Gate CI na PR jest obowiązkową bramką przed scaleniem.

Nie zmieniono żadnego statusu prawnego; pytanie pozostaje `needs_review`. Zakres wyłącznie kurs podstawowy ADR, bez kursu cystern.
