# Audyt sekwencyjny pytań ADR podstawowego — 001–216

**Data pierwszego przebiegu:** 23.10.2026  
**Stan:** przeczytano i oceniono redakcyjnie po kolei każde pytanie, każdą odpowiedź A/B/C, klucz, wyjaśnienie i wskazane odniesienie do ADR 2025. **To nie jest pełne porównanie 216 rekordów z urzędowym polskim tekstem przepisów i nie zastępuje niezależnej recenzji.**

## Wynik mierzalny

| Miernik | Wynik |
|---|---:|
| Rekordy banku objęte pierwszym czytaniem od `ADR-B-0001` do `ADR-B-0216` | **216/216** |
| Kolejne pakiety bez braków ID | **8/8** |
| Rekordy z dodatkowymi, konkretnymi uwagami do sprawdzenia | **34** |
| Odniesienia do wybranego punktu/tematu porównane również z innym źródłem | **25** |
| Wszystkie warianty porównane indywidualnie z pełnym urzędowym tekstem PL | **0/216** |
| Rekordy pozytywnie zatwierdzone przez specjalistę ADR | **0/216** |
| Obecny status pytań | **216 needs_review** |
| Eksport do produkcyjnego egzaminu | **BLOCKED** |

## Przebieg partii w kolejności numeracji

| Partia | Zakres | Liczba | Uwag do ręcznego rozstrzygnięcia | Dodatkowe kontrole źródeł |
|---|---|---:|---:|---:|
| [001-030.json](001-030.json) | ADR-B-0001–ADR-B-0030 | 30 | 2 | 3 |
| [031-060.json](031-060.json) | ADR-B-0031–ADR-B-0060 | 30 | 3 | 1 |
| [061-090.json](061-090.json) | ADR-B-0061–ADR-B-0090 | 30 | 11 | 8 |
| [091-120.json](091-120.json) | ADR-B-0091–ADR-B-0120 | 30 | 3 | 1 |
| [121-150.json](121-150.json) | ADR-B-0121–ADR-B-0150 | 30 | 5 | 2 |
| [151-180.json](151-180.json) | ADR-B-0151–ADR-B-0180 | 30 | 4 | 4 |
| [181-210.json](181-210.json) | ADR-B-0181–ADR-B-0210 | 30 | 5 | 5 |
| [211-216.json](211-216.json) | ADR-B-0211–ADR-B-0216 | 6 | 1 | 1 |

## Najważniejsze poprawki redakcyjne w tym przebiegu

- **`ADR-B-0048`** — poprawiono pytanie o zakaz otwierania sztuk przesyłek; wcześniejsze odpowiedzi „Tak” nie pasowały do pytania „Kiedy…?”.
- **`ADR-B-0099` i `ADR-B-0162`** — uzupełniono klasę 9 i nalepkę **9A** o baterie sodowo-jonowe objęte wymaganiem ADR 2025, w tym UN 3551 i UN 3552; nie tylko baterie litowe.
- **`ADR-B-0173`** — doprecyzowano, że oprócz kodów **BK/VC** w tabeli A dopuszczenie przewozu luzem może wynikać z wyraźnego odesłania do konkretnego ustępu zgodnie z 7.3.1.1.
- Przypomniano wcześniejszy błąd **`ADR-B-0073`**: pytanie nie może twierdzić, że gaśnica 6 kg jest niedopuszczalna przy wymaganym minimum 2 kg; obecne brzmienie pyta o wymagane minimum.

## Szczególnie wymagające uwagi recenzenta

| ID | Przyczyna priorytetu |
|---|---|
| ADR-B-0010 | Zakaz e-papierosów podczas manipulacji, sprawdzić 8.3.5 i 7.5.9. |
| ADR-B-0022 | Liczba gaśnic i minimalna pojemność łącznie przy DMC >7,5t. |
| ADR-B-0047 | Postępowanie z silnikiem i wyjątki napędu urządzeń. |
| ADR-B-0048 | Skorygowano pytanie i dwie odpowiedzi: wcześniejsza niezgodność gramatyczna pytania z odpowiedziami Tak/Nie. |
| ADR-B-0059 | Stosowanie wymogów piętrzenia przy opakowaniach i konstrukcji. |
| ADR-B-0061 | Wymagany dokładny zwrot polski dla przewozu 1.1.4.2.1 — wymaga oficjalnego brzmienia PL. |
| ADR-B-0064 | Wybór kodu tunelowego dla ładunku mieszanego z uwzględnieniem wyłączeń. |
| ADR-B-0071 | Liczba gaśnic i minimalna pojemność łącznie przy DMC 3,5t. |
| ADR-B-0072 | Liczba gaśnic i minimalna pojemność łącznie przy DMC 6t. |
| ADR-B-0073 | Wcześniej dopuszczało dwie odpowiedzi prawdziwe (2 i 6 kg). Po wcześniejszej korekcie zachowano pytanie o MINIMUM. |
| ADR-B-0078 | Stosowanie wymogów piętrzenia przy opakowaniach i konstrukcji. |
| ADR-B-0081 | 7.5.4 wymaga przypisania CV28, sprawdzić okoliczności i sposoby separacji 0,8 m. |
| ADR-B-0082 | Nie wszystkie sztuki 6.1 automatycznie wymagają oddzielenia od żywności: zależność od CV28. |
| ADR-B-0085 | Wyjątek 1.1.3 i oznakowanie LQ — wymagane warunki. |
| ADR-B-0086 | Wybór kodu tunelowego dla ładunku mieszanego z uwzględnieniem wyłączeń. |
| ADR-B-0089 | Wymagany dokładny zwrot polski dla przewozu 1.1.4.2.1. |
| ADR-B-0099 | Rozszerzono wyjaśnienie 9A o baterie sodowo-jonowe ADR 2025. |
| ADR-B-0113 | Część praktyczna pierwszej pomocy nie jest automatycznie zaliczana przez test. |
| ADR-B-0115 | Sprawdzić zakres obowiązku naklejania nalepek na opakowaniu i odpowiednie wyjątki. |
| ADR-B-0129 | Szczególna klasyfikacja odpadów i wyjątki 2.1.3.5.5. |
| ADR-B-0131 | 8.4 stosowany przez przepisy szczególne, kontrola ilości i S14–S24. |
| ADR-B-0139 | Pojęcie przewozu luzem obejmuje BK/VC i odesłania z kolumn (10)/(17). |
| ADR-B-0140 | 5.4.2 nie obejmuje każdego rodzaju kontenera / kontenera-cysterny. |
| ADR-B-0145 | M364: wyjątek dla naczepy, nie rozszerzać na pojazd silnikowy; sprawdzić sygnatariuszy. |
| ADR-B-0160 | Klasa 7: kurs specjalistyczny i wyjątki S12. |
| ADR-B-0162 | Baterie sodowo-jonowe UN 3551 i UN 3552 również mogą wymagać nalepki 9A; poprawiono zakres pytania. |
| ADR-B-0173 | Dopuszczenie przewozu luzem może wynikać z kodu BK/VC ALBO wyraźnego odesłania do przepisu. Wcześniejsze pytanie pomijało odesłania. |
| ADR-B-0176 | Wymagania oznakowania badań gaśnic, prawidłowy punkt. |
| ADR-B-0198 | M364: wyjątek dla naczepy, nie rozszerzać na pojazd silnikowy; sprawdzić sygnatariuszy. |
| ADR-B-0201 | Wyjątek czyszczenia luzem tego samego towaru nie może być przenoszony na 7.5.8.1. |
| ADR-B-0204 | Certyfikat pakowania: właściwy podmiot, warunki, łączenie dokumentów. |
| ADR-B-0207 | Kategoria tunelu E bardziej restrykcyjna niż B; kontrola stosowalności. |
| ADR-B-0209 | Ograniczenie tuneli dla LQ zależy od warunku oznakowania 3.4.13 i 3.4.14. |
| ADR-B-0215 | Sprawdzić przyjęty w polskim ADR zwrot dodatkowy i obowiązki 5.4.1. |

## Zakres faktycznej kontroli źródeł

Lista `supplementary_source_url` wskazuje źródło, w którym sprawdzono **konkretny wybrany temat lub przepis**, a nie prawne zatwierdzenie całej odpowiedzi. W pozostałych wpisach sprawdzono obecność podanej referencji i sens redakcyjny odpowiedzi, ale **nie wykonano porównania pełnej treści ustępu**.

Najważniejsze źródła dla obecnego etapu:

- [Oficjalne ogłoszenie ADR 2025 — Dz.U. poz. 642](https://dziennikustaw.gov.pl/DU/2025/642).
- [Sprostowanie — Dz.U. poz. 1575](https://eli.gov.pl/api/acts/DU/2025/1575/text.pdf), m.in. zmiana w 8.2.2.7.2.3 dotycząca liczby pytań.
- [UNECE — ADR 2025](https://unece.org/adr-2025-files).
- [Ministerstwo Infrastruktury — polskie tomy pomocnicze](https://www.gov.pl/web/infrastruktura/towary-niebezpieczne), z wyraźnym zastrzeżeniem, że źródłem prawa jest Dziennik Ustaw.
- [Regulator HSA — gaśnice ADR](https://www.hsa.ie/eng/your_industry/adr_-_carriage_of_dangerous_goods_by_road/information_guidance/faqs/adr_-_faqs/).
- [HSA — zmiany ADR 2025, nowe baterie sodowo-jonowe](https://www.hsa.ie/eng/your_industry/adr_-_carriage_of_dangerous_goods_by_road/news_updates/adr_2025_-_summary_of_main_changes/).
- [UNECE — umowy wielostronne](https://unece.org/transport/road-transport/adr-multilateral-agreements).

**Priorytet dalszej pracy:** szczegółowa weryfikacja prawa i wszystkich trzech wariantów najpierw dla pozycji wymienionych jako pilne, następnie dla wszystkich innych ID `0001…0216` z pełnym tekstem polskim, sprostowaniem i obowiązującymi odstępstwami. Każda zakończona kontrola prawna powinna otrzymać odrębny protokół z rzeczywistym źródłem i osobną recenzję fachowca.

## Mechanizmy spójności

`python scripts/check_sequential_audit.py` sprawdza wszystkie **216 kolejnych ID**, zestawia dokładny zapis tekstów A/B/C, klucza, wyjaśnienia i referencji z aktualnym JSONL oraz wykrywa nieaktualny przegląd po zmianie pytania. CI nie pozwala mylić tego pierwszego przebiegu z podpisaną akceptacją eksperta. `review/approvals.jsonl` pozostaje pusty.

**Nie zgłaszać: „zweryfikowano prawnie 216 pytań” — to byłoby niezgodne z faktycznie wykonanym zakresem.**
