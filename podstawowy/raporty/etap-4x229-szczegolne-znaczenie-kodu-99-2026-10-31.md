# Etap 4x229 — szczególne znaczenie numeru zagrożenia 99

Data: 31.10.2026. Zakres: wyłącznie kurs podstawowy ADR. Punkt wyjścia: main po 4x228 `41bbe9823313da4162dd334d1b980c57d32d0d72`, bank 653 pytań.

## 1. Luka semantyczna

W kompetencji ADR-B-06-K06 były pytania o ogólną regułę powtarzania cyfry (zwykle oznacza nasilenie zagrożenia) oraz przykłady 33 i 88. Nie było pytania o wyjątek z listy kombinacji o szczególnym znaczeniu w ADR 5.3.2.3.1–5.3.2.3.2.

Kod 99 jest takim wyjątkiem. ADR 2025, 5.3.2.3.2, określa go jako różne towary niebezpieczne przewożone w stanie podgrzanym. Nie należy interpretować go wyłącznie przez ogólną regułę podwojenia cyfry 9. To odrębna wiedza, przydatna przy odczytywaniu numeru na tablicy pomarańczowej.

## 2. Nowe pytanie ADR-B-0654

Dodano `ADR-B-0654` do kompetencji `ADR-B-06-K06`. Nazwę kompetencji rozszerzono na „Powtórzone cyfry i szczególne kombinacje numerów zagrożenia”.

**Pytanie:** W górnym polu numerowanej tablicy ADR widnieje kod 99. Co oznacza on w szczególności?

| Opcja | Długość | Ocena |
|---|---:|---|
| A | 58 | **Poprawna** — różne towary niebezpieczne przewożone w stanie podgrzanym. |
| B | 59 | Błędna — znaczenie silnie żrącego i toksycznego ma kod 886. |
| C | 78 | Błędna — kod 99 ma szczególne znaczenie, a nie tylko ogólne znaczenie podwojonej cyfry 9. |

Poprawna odpowiedź A nie jest najdłuższa. Explanation ma 352 znaki i 4 zdania: najpierw znaczenie poprawnej odpowiedzi, następnie wyjaśnienie, dlaczego ogólna reguła powtórzenia cyfry nie wystarcza, potem odróżnienie błędnych interpretacji i krótka podstawa ADR. Status: `needs_review`.

## 3. Aktualizacja lekcji i instruktora

Lekcja ADR-B-06 otrzymała objaśnienie szczególnego znaczenia kodu 99 i odsyłacz do ADR-B-0654. Materiał instruktora rozszerzono o wyjątki od ogólnej reguły powtórzenia cyfry. Nie zastępuje to ćwiczenia z odczytywania całego numeru na makiecie tablicy.

## 4. Synchronizacja

- Bank: 654 pytania, wszystkie `needs_review`, 0 `verified`.
- ADR-B-06: 54 pytania; kompetencja K06: 5 pytań.
- Warianty i klucze egzaminów próbnych 001–005: `source_bank_head` aktualizowany do nowego blob SHA banku.
- Snapshoty sequential/legal: zakres 629–654. Rejestr polskiego tekstu: zakres 0610–0654; dla 0654 pełne porównanie polskiego tekstu urzędowego i niezależna recenzja A/B/C pozostają otwarte.
- Manifesty pakietu: 654 rekordy, 654 `needs_review`, 0 `verified`, aktualny SHA banku.
- Wskaźnik „poprawna odpowiedź jest jedyną najdłuższą”: 72/654 = 11,01%; nowa poprawna odpowiedź nie jest najdłuższa.

## 5. Źródła

- ADR 2025, 5.3.2.3.1–5.3.2.3.2 — zasada powtórzenia cyfry i lista kombinacji o szczególnym znaczeniu, w tym kod 99: https://dziennikustaw.gov.pl/DU/2025/642
- Oficjalne wydanie ADR 2025, UNECE: https://unece.org/adr-2025-files

Odczyt w tym etapie jest wstępnym sprawdzeniem redakcyjnym. Pełne porównanie polskiego tekstu urzędowego ze sprostowaniem i niezależna recenzja specjalisty pozostają otwarte. Wszystkie statusy pozostają `needs_review`.
