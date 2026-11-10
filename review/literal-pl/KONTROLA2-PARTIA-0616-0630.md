# Kontrola druga — partia ADR-B-0616–0630

Data: 2026-11-10. Bank przed wdrożeniem: 780 pytań, blob `7c6b46d4134301f616cfc39d2b3e33e4318da428`.
Wynik kontroli drugiej: **0 OK / 15 POPRAW / 0 BLOKUJ**. Licznik pytań bez obu kontroli: **165 → 150**. Wszystkie 15 rekordów zastąpiono nowymi elementami tej samej kompetencji; moduły, kompetencje i litery kluczy pozostają bez zmian. Wszystkie statusy pozostają `needs_review`; nie nadano `verified`.

| ID | Werdykt II | Nowy element / podstawa |
|---|---|---|
| 0616 | POPRAW | Trwały i czytelny numer UN; ADR 5.2.1.1–5.2.1.2, s. 935 |
| 0617 | POPRAW | Wyjątek dla hermetycznych opakowań wewnętrznych do 500 ml; 5.2.1.10.2(f), s. 939 |
| 0618 | POPRAW | Znak DPPL „nie piętrzyć”; 6.5.2.2.2, s. 1109; 7.5.7.2, s. 1309 |
| 0619 | POPRAW | Ważność zaświadczenia po egzaminie poza okresem 12 miesięcy; 8.2.2.8.2(b), s. 1330 |
| 0620 | POPRAW | Instrukcje pisemne nie są zastępowane kartami charakterystyki; 5.4.3.1–5.4.3.4, s. 974–975; 8.1.2.1(b), s. 1324 |
| 0621 | POPRAW | Rozpoznanie nalepki 4.2; 5.2.2.2.2, s. 946 (obraz); 2.2.42.1.1, s. 182 |
| 0622 | POPRAW | Nadtlenek organiczny i ryzyko uszkodzenia rogówki; 2.2.52.1.4, s. 196 |
| 0623 | POPRAW | Toksyczność przez przenikanie przez skórę; 2.2.61.1.1, s. 214; 5.4.3.4, s. 975 |
| 0624 | POPRAW | Nalepka 7C, kategoria III-ŻÓŁTA; 5.2.2.2.2, s. 948 (obraz) |
| 0625 | POPRAW | UN 2794: klasa 8, kod C11; tabela A, s. 517 (obraz); 2.2.8.1.1 i 2.2.8.1.4.1, s. 264 |
| 0626 | POPRAW | Przytomną osobę w oparach zawołać na stronę nawietrzną; 5.4.3.4, s. 975 |
| 0627 | POPRAW | Nalepki 3 i 6.1 na tej samej stronie, blisko siebie; 5.2.2.1.6(a),(c), s. 939–940 |
| 0628 | POPRAW | Mocowanie kontenera do pojazdu; 7.5.7.4, s. 1309; 7.5.7.1, s. 1308 |
| 0629 | POPRAW | Zapis „PRZEWÓZ ZGODNIE Z 4.1.1.5.3”; 5.4.1.1.3.3, s. 963; 4.1.1.5.3, s. 712 |
| 0630 | POPRAW | Odczyt zagrożenia dodatkowego z dokumentu przewozowego; 5.4.1.1.1(c), s. 961; wzór 5.4.3.4, s. 975 |

## Korekta ustaleń kontroli pierwszej

Wszystkie pięć pierwotnych werdyktów OK (0616, 0618, 0619, 0626, 0628) zmieniono na POPRAW. Wykryto także przeoczone duplikaty/zbliżenia: 0617 = 0058/0172/0286/0682; 0621 ≈ 0665/0724; 0623 ≈ 0158; 0624 = 0729; 0625 ≈ 0161; 0630 ≈ 0109. Pozostałe duplikaty i uzasadnienia szczegółowe opisano w materiale kontroli drugiej dostarczonym dla tej partii.

## Kontrola podobieństw i metryki

Po zastosowaniu 15 nowych rekordów: `similarity.py` — 7 par ≥0,45 i 154 pary ≥0,25 w całym banku; 0 par z udziałem tej partii przy obu progach. Wskaźnik „poprawna odpowiedź jedyną najdłuższą”: 23/780 = 2,95%, maksimum działu 5,66%. „Poprawna odpowiedź jedyną najkrótszą”: 104/780; maksimum działu 24,1%.

Wdrożenie ma zachować dokładnie 780 rekordów, te same ID i kolejność, klucze, moduły i kompetencje. Bez zmian w `kompetencje.json`; bez oznaczania `verified`. Plik źródłowy banku ma blob SHA-1 `8596a7a61cdc27c4f558af7197cdca9072090c4e`.
