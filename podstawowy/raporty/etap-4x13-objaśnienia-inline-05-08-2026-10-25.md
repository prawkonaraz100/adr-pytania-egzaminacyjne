# Etap 4x13 — objaśnienia inline w lekcjach ADR-B-05–08

- Punkt wyjścia: świeży `main` po PR #348, commit `79e54f79f3496924c9c3530d6f46a4165eec2aa7`.
- Zakres: B-05–B-08, słowniczek i język kursanta; bank pytań bez zmian.

## Zmiany i kontrole
- Objaśnienia dodane w pierwszym przebiegu redakcyjnym: B-05: 3; B-06: 4; B-07: 3; B-08: 5.
- Po kontroli pierwszego użycia dodano jeszcze 2 objaśnienia do wcześniejszych wystąpień (B-05 „instrukcje pisemne”, B-06 „numer rozpoznawczy zagrożenia”).
- Uproszczono 3 zdania/fragmenty wymogów: B-06 tablice pomarańczowe, B-07 podział obowiązków uczestników, B-08 dobór gaśnic. W B-05 przepisano wyjaśnienie dostępności instrukcji pisemnych.
- Naprawiono trzy niedokładne wstawienia wynikające z odmiany polskich wyrazów (B-05 „instrukcje pisemne”, B-06 „tablica pomarańczowa”) i poprawiono objaśnienie DMC w B-08.
- Dodano odsyłacze do kotwic słowniczka w akapicie pierwszego użycia.

## Przykłady przed → po
1. **B-06 — tablice pomarańczowe**
   - Przed: „Tablice pomarańczowe stosuje się w przypadkach określonych ADR.”
   - Po: „Tablice pomarańczowe są wymagane tylko w określonych rodzajach przewozu. Zanim uznasz, że tablica jest potrzebna lub zbędna, sprawdź wymagania dla danego towaru i konfiguracji pojazdu (ADR 5.3.2).”
2. **B-07 — obowiązki**
   - Przed: „ADR 1.4 przypisuje uczestnikom przewozu obowiązki zależne od roli.”
   - Po: „ADR rozdziela obowiązki według tego, co robi dana osoba lub firma. Nadawca, przewoźnik, załadowca i kierowca mają różne zadania, więc polecenie jednej osoby nie zwalnia pozostałych z ich obowiązków (ADR 1.4).”
3. **B-08 — gaśnice**
   - Przed: „Liczba i pojemność gaśnic zależą od wymagań ADR dla pojazdu, jego dopuszczalnej masy całkowitej (DMC) oraz warunków przewozu i ewentualnego zastosowania wyłączenia.”
   - Po: „To, ile gaśnic i jakiej pojemności trzeba mieć, zależy od pojazdu i rodzaju przewozu. Sprawdź dopuszczalną masę całkowitą (DMC — maksymalną masę pojazdu wraz z ładunkiem) oraz to, czy ma zastosowanie wyłączenie. Nie zakładaj, że jeden zestaw pasuje do każdej ciężarówki (ADR 8.1.4).”

## Walidacja odsyłaczy
- B-05: 4 linków do kotwic; nieistniejące kotwice: 0.
- B-06: 5 linków do kotwic; nieistniejące kotwice: 0.
- B-07: 3 linków do kotwic; nieistniejące kotwice: 0.
- B-08: 5 linków do kotwic; nieistniejące kotwice: 0.

## Bank i wskaźniki
- Bank: 609 pytań; bez zmian ID, odpowiedzi, explanation i statusów.
- „Poprawna = jedyna najdłuższa”:
  - ADR-B-05: 6/43 = 13.95% (cel ≤16%).
  - ADR-B-06: 5/45 = 11.11% (cel ≤16%).
  - ADR-B-07: 6/48 = 12.50% (cel ≤16%).
  - ADR-B-08: 6/42 = 14.29% (cel ≤16%).
- Explanation ≥200 znaków: bez zmian w tej partii.

## Testy
- Automatycznie sprawdzono, że każdy dodany link kotwicy w B-05–08 wskazuje istniejący identyfikator słowniczka.
- Blokujący test pierwszego wystąpienia w tym samym akapicie zostanie włączony w partii B-09–13 po przeredagowaniu wszystkich lekcji.
- Środowisko lokalne nie jest dostępne przez użyte połączenie; ostateczne testy wykona CI na PR. Żadne pytanie nie zostało oznaczone jako `verified`.
