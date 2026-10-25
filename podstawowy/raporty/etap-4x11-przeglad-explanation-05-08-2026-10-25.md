# Etap 4x11 — ręczny przegląd ostrzeżeń explanation, partia B-05–08

- Data: 25.10.2026.
- Świeży punkt startowy: `main` `0d2718bab4a318d9a7b8ab12b90951a4ad5a1aeb`.
- Zakres: 25 ostrzeżeń z listy 4x10 przypisanych do działów B-05–B-08.
- Bank: 609 pytań; żaden status weryfikacji nie został podniesiony do `verified`.

## Wynik ręcznego przeglądu

| Dział | Przejrzane | Przepisane | Fałszywe alarmy |
|---|---:|---:|---:|
| B-05 | 1 | 0 | 1 |
| B-06 | 6 | 2 | 4 |
| B-07 | 6 | 0 | 6 |
| B-08 | 12 | 3 | 9 |
| **Razem** | **25** | **5** | **20** |

## Lista sprawdzonych ID

- **B-05 (1):** ADR-B-0186.
- **B-06 (6):** ADR-B-0132, ADR-B-0255, ADR-B-0257, ADR-B-0281, ADR-B-0561, ADR-B-0563.
- **B-07 (6):** ADR-B-0136, ADR-B-0285, ADR-B-0365, ADR-B-0368, ADR-B-0374, ADR-B-0378.
- **B-08 (12):** ADR-B-0022, ADR-B-0023, ADR-B-0024, ADR-B-0057, ADR-B-0075, ADR-B-0137, ADR-B-0176, ADR-B-0198, ADR-B-0254, ADR-B-0319, ADR-B-0417, ADR-B-0486.

## Potwierdzone poprawki

- **ADR-B-0281:** usunięto powtórzone zdanie o nazwie handlowej i numerze rejestracyjnym. Wyjaśnienie nadal wskazuje, że standardowe oznakowanie sztuki przesyłki wymaga prefiksu „UN”, a inne dane go nie zastępują. Podstawa: ADR 5.2.1.1.
- **ADR-B-0563:** usunięto powtórzenie dotyczące podpisu odbioru i oceny kierowcy. Zachowano zasadę, że samo rozładowanie nie oznacza automatycznej możliwości usunięcia nalepek, jeśli nie spełniono warunków ADR. Podstawa: ADR 5.3.1.1.5.
- **ADR-B-0198:** połączono powtarzające się zdanie o przechowywaniu świadectwa u odbiorcy lub w archiwum. Wyjaśnienie rozróżnia świadectwo dopuszczenia pojazdu od zaświadczenia kierowcy. Podstawa: ADR 8.1.2.2(a).
- **ADR-B-0319:** usunięto powtórzenie, które dwukrotnie mówiło, że typy FL i AT nie zastępują EX/II lub EX/III. Podstawa: ADR 9.1.1.2.
- **ADR-B-0417:** usunięto powtórzenie porównania jednej gaśnicy 6 kg i zestawu 12 kg. Pozostawiono jasne wyjaśnienie, że w opisanym przedziale DMC wymagane są co najmniej dwie gaśnice i łączna pojemność minimum 4 kg. Podstawa: ADR 8.1.4.1.

Dla wszystkich pięciu rekordów zachowano ID, treść pytania, opcje, poprawną literę, źródła i status `needs_review`. Zaktualizowano odpowiednie snapshoty w `review/sequential/`, aby audyt odzwierciedlał aktualny bank.

## Fałszywe alarmy

Pozostałe 20 wyjaśnień uznano za dydaktycznie wystarczające: podają sens poprawnej odpowiedzi, konkretnie wskazują błąd kuszących dystraktorów i kończą się podstawą ADR. Nie przepisano ich tylko po to, by dopasować je do słów-sygnałów. W szczególności objaśnienia numeru UN, rozdziału tablicy pomarańczowej, wyposażenia, odpowiedzialności nadawcy/pakującego/przewoźnika i typów pojazdów były konkretne i zrozumiałe.

## Heurystyka i Quality Gate

Rozszerzony walidator `scripts/check_explanation_heuristics.py` nadal sprawdza wszystkie 86 kandydatów z raportu 4x10:
- przed rozszerzeniem: **86** ostrzeżeń;
- po rozszerzeniu słownictwa: **12** pozycji bez żadnego z sygnałów;
- brak sygnału pozostaje wskazówką do ręcznego przeglądu, a nie automatycznym błędem.

## Wskaźniki banku

- Wskaźnik „poprawna = jedyna najdłuższa”: **77/609 = 12,64%** globalnie; według raportu 4x10 każdy dział ≤16%. Zmiany dotyczyły tylko explanation, więc długości odpowiedzi A/B/C się nie zmieniły.
- Minimum explanation: **300 znaków** po poprawkach; wszystkie spełniają próg Quality Gate 300 znaków (a więc także wymagane minimum 200).
- Statusy: **609 `needs_review`, 0 `verified`**.
- Klucze egzaminów próbnych 001–005 nie wymagają zmian: nie zmieniono pytań, opcji ani poprawnych liter.

## Ograniczenia

To redakcja dydaktyczna i kontrola spójności audytu, a nie formalna akceptacja prawna. Nie potwierdzano zmian w ADR 2027 i nie rozpoczęto pracy nad cysternami ani innym kursem.
