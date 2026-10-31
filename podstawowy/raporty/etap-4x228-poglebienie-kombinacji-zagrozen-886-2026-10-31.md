# Etap 4x228 — pogłębienie kompetencji ADR-B-06-K08: kombinacja 886

Data: 31.10.2026. Zakres: wyłącznie kurs podstawowy ADR. Punkt wyjścia: main po scaleniu 4x227 `64c30b805c0e56ae37c50cd90359f3d7d8045665`, bank 652 pytań.

## 1. Wynik audytu semantycznego

W 4x227 zidentyfikowano, że kompetencja ADR-B-06-K08 (znaczenie cyfry 8) obejmowała cztery pytania o ogólne znaczenie cyfry 8 i przykłady 80/88. Pytania ADR-B-0298 i ADR-B-0637 w praktyce powtarzały odczyt kodu 80. Nie było pytania uczącego rozpoznawania kombinacji 3-cyfrowej, w której numer identyfikuje więcej niż jedną właściwość zagrożenia.

ADR 2025, 5.3.2.3.2, podaje kod 886 jako „highly corrosive substance, toxic” (substancja silnie żrąca i toksyczna). To odrębne zastosowanie niż samo odczytanie cyfry 8 lub numeru 80/88. W ten sposób kompetencja zyskuje pytanie o odczytanie całego kodu i rozdzielenie jego elementów.

## 2. Nowe pytanie ADR-B-0653

Dodano `ADR-B-0653` do kompetencji `ADR-B-06-K08`.

**Pytanie:** Na górnym polu pomarańczowej tablicy ADR widnieje numer 886. Jakie zagrożenia wskazuje ten numer?

| Opcja | Długość | Ocena |
|---|---:|---|
| A | 54 | **Poprawna** — substancja jest silnie żrąca i toksyczna. |
| B | 71 | Błędna — cyfra 6 oznacza toksyczność, nie palność; 886 nie opisuje utleniania. |
| C | 74 | Błędna — cyfra 6 nie jest kodem kategorii tunelu. |

Poprawna odpowiedź A nie jest najdłuższa. Explanation ma 333 znaki i 5 zdań: najpierw sens poprawnej odpowiedzi, potem wyjaśnienie błędnych interpretacji, na końcu podstawa ADR. Źródło: ADR 2025, 5.3.2.3.2, Dz.U. 2025 poz. 642. Status: `needs_review`; nie nadano `verified`.

## 3. Aktualizacja lekcji i materiału instruktora

Lekcja ADR-B-06 otrzymała krótkie objaśnienie przykładu 886 i odsyłacz do ADR-B-0653. Materiał instruktora rozszerzono o kombinację zagrożeń 886 w kompetencji K08. To materiał roboczy; nie zastępuje ćwiczenia na makiecie tablicy ani niezależnego odbioru instruktora.

## 4. Synchronizacja

- Bank: 653 pytania, wszystkie `needs_review`, 0 `verified`.
- ADR-B-06: 53 pytania; ADR-B-06-K08: 5 pytań.
- Warianty i klucze egzaminów próbnych 001–005: `source_bank_head` aktualizowany do nowego blob SHA banku.
- Snapshoty sekwencyjnego audytu i przeglądu prawnego: zakres ostatniej partii rozszerzony z 629–652 do 629–653.
- Rejestr kontroli polskiego tekstu: ADR-B-0653 dodany jako nieporównany dosłownie; niezależna recenzja A/B/C pozostaje pending.
- Manifesty pakietu recenzyjnego: 653 rekordy, 653 `needs_review`, 0 `verified`, bieżący blob SHA banku.
- Wskaźnik „poprawna odpowiedź jest jedyną najdłuższą”: 72/653 = 11,03%; nowa poprawna odpowiedź nie jest najdłuższa.

## 5. Źródła

- ADR 2025, 5.3.2.3.2 — tabela znaczeń numerów rozpoznawczych zagrożenia, w tym 886: https://dziennikustaw.gov.pl/DU/2025/642
- Oficjalne wydanie ADR 2025, UNECE: https://unece.org/adr-2025-files

Odczyt w tym etapie jest wstępnym sprawdzeniem redakcyjnym. Pełne porównanie polskiego tekstu urzędowego ze sprostowaniem i niezależna recenzja specjalisty pozostają otwarte. Wszystkie statusy pozostają `needs_review`.
