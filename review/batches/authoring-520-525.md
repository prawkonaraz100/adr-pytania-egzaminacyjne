# Etap 4h — pierwsza partia pogłębienia ADR-B-01 i ADR-B-13

**23.10.2026 | PR:** osobna partia 0520–0525 | **Status:** wersja redakcyjna, `needs_review`; nie gotowe do publikacji.

## Aktualny punkt startu
- Świeży `main`: ADR-B-0001–0519, **519 pytań**, 519 `needs_review`, 0 `verified`, bez otwartych PR.
- Dział 01: **26 pytań**; dział 13: **25 pytań**. Docelowo po tej partii odpowiednio **29 i 28**; cel 35–40 nie jest jeszcze osiągnięty.
- Nowe ID: **ADR-B-0520–0525**, kolejność rosnąca i unikatowa; trzy pytania dla działu 01 oraz trzy dla 13. Klucz: A=2, B=2, C=2.

## Zidentyfikowane, wcześniej słabiej sprawdzane tematy
| ID | Dział | Rzeczywista nowa sytuacja | ADR 2025 | Audyt A/B/C |
|---|---|---|---|---|
| 0520 | 01 | dostęp do zapisów szkolenia na żądanie właściwej władzy | 1.3.3 | 3 warianty, wyjaśnienia odrębne |
| 0521 | 01 | sprawdzenie wcześniejszego szkolenia przy nowym zatrudnieniu | 1.3.3 | 3 warianty |
| 0522 | 01 | szkolenie pracownika w łańcuchu multimodalnym | 1.3.2.2 | 3 warianty |
| 0523 | 13 | numer nalepki zagrożenia dodatkowego w dokumencie | 5.4.1.1.1(c) | 3 warianty |
| 0524 | 13 | wpis grupy pakowania w dokumencie | 5.4.1.1.1(d) | 3 warianty |
| 0525 | 13 | kod tunelowy w dokumencie przewozowym, gdy jest wymagany | 5.4.1.1.1(k) | 3 warianty |

## Źródła i granice legalnej kontroli

- Źródło prawa: [Dz.U. 2025 poz. 642](https://dziennikustaw.gov.pl/DU/2025/642); [sprostowanie Dz.U. 2025 poz. 1575](https://dziennikustaw.gov.pl/DU/2025/1575).
- Tekst ADR 2025 (wersja EN) [UNECE](https://unece.org/adr-2025-files), w tym rozdziały 1.3 i 5.4; dodatkowy punktowy crosscheck EN źródeł wtórnych. Dokumentacja w `review/legal-clauses/520-525.json` zawiera **18 indywidualnych uzasadnień** poprawności/fałszywości A/B/C.
- **Nie udało się dokończyć literalnego porównania całych odpowiednich polskich punktów z oryginalnymi skanami PDF z Dz.U.** Wykazano urzędową publikację i sprawdzono zakres ustępów z angielskim ADR 2025; to **nie jest pełne potwierdzenie urzędowego polskiego brzmienia**. Zgodność ze sprostowaniem w zakresie każdego pytania i ewentualne wyjątki pozostają **do niezależnego specjalisty**. Nie oznaczać rekordów `verified`.
- Warianty odpowiedzi mają przybliżoną długość i realistyczne alternatywne decyzje. Tekst poprawny prawnie pozostaje do weryfikacji przez eksperta.
- Mapa kompetencji zawiera odpowiednie wpisy; pytanie 0523 dotyczące zagrożeń dodatkowych rozszerza zakres roboczej kompetencji „Numer UN i nazwa” w dziale 13 i powinno zostać ocenione w kompleksowym przeglądzie sylabusa. Nie dodawano nowego celu programu.
- Nie rozpoczęto kursu cystern ani innych kursów.

## Warunek zamknięcia partii

Pełny `Quality Gate` w GitHub Actions ma uzyskać PASS we wszystkich obowiązkowych krokach (nie tylko schemat), następnie squash merge, świeży odczyt main i wpis do Issue #10. Sam PASS nie poświadcza zgodności z prawem.
