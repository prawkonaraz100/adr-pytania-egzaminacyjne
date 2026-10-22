# Audyt wydawniczy ADR — październik 2026

**Data: 23.10.2026. Status: audyt procesu i wybranych zapisów, NIE niezależne zatwierdzenie prawne 216 pytań.**

## Punkt wyjścia

- 216 rekordów `ADR-B-0001…0216`; **216 needs_review / 0 verified**.
- 103/103 celów teorii ma co najmniej dwa autorskie szkice, 3 cele praktyczne wymagają zajęć stacjonarnych.
- 13/13 lekcji w formie redakcyjnej, bez podpisanej niezależnej recenzji.
- Sama walidacja struktury, równowaga klucza i powiązanie z matrycą **nie mogą** uzasadniać wydania.

## Działania wykonane w tej partii

### 1. Zabezpieczenie eksportu

Dodano `scripts/release_gate.py` i **pusty** rejestr `review/approvals.jsonl`; proces opisany w `review/README.md`.

Eksporter wymaga: właściwego `verified`, recenzenta i daty zgodnych z wpisem, dokładnego SHA-256 zatwierdzonej treści (w tym A/B/C, klucza, wyjaśnienia i źródeł), istniejącego protokołu `review/reports/…md`, co najmniej 30 pytań oraz reprezentacji 13 modułów. Zapis jest atomowy i nie następuje przed przejściem wszystkich kontroli.

Przy obecnych danych powinien zwracać `BLOCKED` i nie tworzyć zbioru produkcyjnego. Parametr `--report` pokazuje wynik nie blokując CI, bez eksportu. Testy syntetyczne nie są recenzją rzeczywistych pytań.

**Ograniczenie:** automatyczne sprawdzenie pliku i skrótu nie może udowodnić kwalifikacji, rzeczywistej tożsamości lub niezależności recenzenta. Odbiór fachowy musi być rzeczywisty, a nie odtworzony w programie.

### 2. Kontrola prawna 2026 / odstępstwa

Zweryfikowano istnienie i zakres wybranych umów wielostronnych podpisanych przez Polskę. Szczegóły, daty graniczne i źródła: [ODSTEPSTWA-ADR-2026.md](ODSTEPSTWA-ADR-2026.md).

**M364**: w określonych przewozach między jej sygnatariuszami świadectwo dopuszczenia **naczepy** może być przechowywane poza kabiną, w odpowiednim miejscu na naczepie. Skorygowano `ADR-B-0145` i `ADR-B-0198`: mają teraz jednoznacznie dotyczyć **samochodu ciężarowego FL, nie naczepy**. Ich poprawne litery pozostają B, status pozostaje `needs_review`.

**M369 / M370**: dokumentacja wskazuje na obowiązujące czasowo wyjątki (odpowiednio określone paliwa UN 1202 oraz posiłki MRE z określonymi podgrzewaczami UN 2813). Nie są to wyłączenia dla wszystkich paliw lub wszystkich urządzeń; nie wprowadzono nowych pytań bez kompleksowej kontroli szczegółowych warunków.

### 3. Błędne odpowiedzi

Poprawiono wyłącznie błędne warianty w:

| ID | Były problem | Poprawa |
|---|---|---|
| `ADR-B-0001` | Kurs tachografu jako „alternatywa” szkolenia ADR pracownika | Realistyczne pomieszanie BHP i szkoleń 1.3 vs 8.2 |
| `ADR-B-0112` | Lampka tachografu jako sposób oznaczenia miejsca wypadku | Różnica między gaśnicą, światłami a kamizelką i znakami |
| `ADR-B-0122` | Pieczątka i tablica rejestracyjna zamiast planu ochrony | Rozróżnienie planu ochrony, procedury przeciwpożarowej i mocowania |
| `ADR-B-0140` | Wydruk tachografu zamiast certyfikatu pakowania | Różnica między dokumentem przewozowym, dopuszczeniem a certyfikatem |
| `ADR-B-0168` | Tablica rejestracyjna i telefon jako jedyne zabezpieczenie | Zależność między ostrzeganiem a użyciem wyposażenia załogi |

Nie zmieniano kluczy prawidłowych odpowiedzi. **Wszystkie warianty, również poprawione, wciąż wymagają niezależnej kontroli zgodności z ADR**.

## Uruchomione/oczekujące bramki

- [x] Przed zmianą [Quality Gate #149](https://github.com/prawkonaraz100/adr-pytania-egzaminacyjne/actions/runs/39859118111) — PASS 5 kontroli na poprzednim PR, ale **nie jest dowodem PASS nowej gałęzi**.
- [x] Opracowano testy odrzucania zmienionej odpowiedzi, zmienionego wyjaśnienia, brakującego protokołu, braku podpisu i zbyt małego lub nierównomiernego zbioru.
- [x] Dodano raport bramki wydawniczej do GitHub Actions.
- [ ] PASS kompletu testów bieżącej gałęzi/PR, sprawdzony na końcowym commicie.
- [ ] Zatwierdzenie 216 pytań przez rzeczywistego specjalistę ADR z aktualnym prawem i odstępstwami.
- [ ] Zatwierdzenie 13 lekcji, dobór/licencje ilustracji, przykładowe dokumenty.
- [ ] Zatwierdzenie 3 scenariuszy praktycznych i wykonanie zajęć przez uprawniony ośrodek.
- [ ] Produkcyjny generator 30 pytań / 60 minut z odpowiednim losowaniem wyłącznie na dopuszczonym zbiorze.

## Kryterium następnego etapu

Nie dodawać teraz kolejnych dziesiątek szkiców tylko dla liczby. Najpierw przeprowadzić partiami **faktyczną recenzję** 216 rekordów na podstawie polskiego ogłoszenia, sprostowania i stosownych umów wielostronnych, zaczynając od najbardziej ryzykownych wyjątków, uprawnień i bezpieczeństwa.

**Zasada:** „gotowy schemat + automatyczny PASS” nie oznacza „poprawna odpowiedź ADR”.
