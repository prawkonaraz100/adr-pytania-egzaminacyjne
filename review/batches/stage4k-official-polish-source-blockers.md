# Etap 4k — rejestr dosłownej kontroli urzędowego ADR 2025

**Data:** 23.10.2026. Stan wejściowy `main`: 542 pytania, ADR-B-0001–0542, 542 `needs_review`, zero `verified`, brak otwartych PR.

## Wynik rzeczywistej próby odczytu źródła

Ustalono źródło prawa: [Dz.U. 2025 poz. 642](https://dziennikustaw.gov.pl/DU/2025/642) oraz [obwieszczenie o sprostowaniu, poz. 1575](https://dziennikustaw.gov.pl/DU/2025/1575). Urzędowa publikacja potwierdza istnienie ADR 2025 i sprostowania, ale **nie udało się programowo pobrać ani zanalizować stron oryginalnego polskiego PDF**.

Próby:
1. ELI plik segmentu 41 `https://eli.gov.pl/api/acts/DU/2025/642/text/O/D20250642-41.pdf` — blokada `DisabledError` narzędzia wyszukiwania;
2. ISAP `https://isap.sejm.gov.pl/isap.nsf/download.xsp/WDU20250000642/O/D20250642-02.pdf` — strona weryfikacji człowieka;
3. bezpośredni dostęp do ELI z izolowanego środowiska — błąd rozwiązywania domeny.

Dostępne były punktowe angielskie reprodukcje oraz [oficjalny ADR 2025 UNECE](https://unece.org/adr-2025-files), co pozwalało ustalić temat ustępów, **nie zweryfikować literalnie polskiego brzmienia**. Nie uznajemy tłumaczenia EN za dowód zgodności z polskim prawem.

## Kompletny wykaz kontroli

`review/legal-polish/stage4k-literal-verification-ledger-0001-0542.json` to rejestr wszystkich 542 ID z podstawą prawną, źródłami i statusem faktycznie wykonanej weryfikacji. Priorytet **P1** obejmuje 23 najnowsze pytania 0520–0542, każde osobno: podstawa, brak odczytu polskiego tekstu, brak potwierdzenia zastosowania sprostowania, obowiązek niezależnego przeglądu A/B/C. Pozostałe 519 mają P2 i odwołują się do wcześniejszych zapisów audytu.

### Lista P1 — szczególnie pilna kontrola

- **0520–0522:** szkolenia ADR 1.3.2.2 i 1.3.3; wymóg dokumentacji i granica zastosowania do pracownika;
- **0523–0525:** opis przewozowy 5.4.1.1.1 lit. c, d i k oraz ograniczenia tunelowe;
- **0526–0529:** ilości wyłączone EQ (3.5.4.3, 3.5.5, 3.5.6), szkolenie bezpieczeństwa 1.3.2.3;
- **0530–0533:** odpady 5.4.1.1.3, salvage packaging 5.4.1.1.5, nieoczyszczone środki 5.4.1.1.6.1, języki 5.4.1.4.1;
- **0534–0538:** LQ overpack 3.4.11, masa brutto 3.4.12, opis dokumentu 5.4.1.1.1 i 5.4.1.4.2;
- **0539–0540:** tunele 8.6.3.2, 8.6.4, 3.4.13/3.4.14;
- **0541–0542:** modele nalepek 2.2 i 3, grafiki według 5.2.2.2.2.

## Procedura zamknięcia P1 i P2 przez specjalistę

Dla każdego ID należy otworzyć konkretną **stronę urzędowego polskiego PDF**, zapisać numer pliku i strony, dosłowne brzmienie ustępu, wynik kontroli sprostowania, wskazać A/B/C i niezależnie opisać dlaczego każdy wariant jest zgodny lub niezgodny z zakresem, wyjątkami, jednostkami i rodzajem przewozu. Należy zanotować recenzenta, datę i aktualny hash treści zgodnie z `review/README.md`. Jeśli weryfikacja nie jest możliwa, pozycja pozostaje zablokowana do publikacji.

**Wynik etapu 4k tej partii jest częściowy:** wykonano inwentaryzację źródeł i próbę dostępu; **0/542 pełnych nowych porównań literalnych** w tym PR. Nie wolno przedstawiać tej partii jako zakończonej prawnie. Wszystkie pytania pozostają `needs_review`; egzamin próbny pozostaje nieaktywny. Nie rozpoczęto żadnych kursów specjalistycznych ani cystern.
