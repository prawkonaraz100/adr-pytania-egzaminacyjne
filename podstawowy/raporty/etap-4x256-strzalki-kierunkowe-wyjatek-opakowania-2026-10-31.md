# Etap 4x256 — strzałki kierunkowe: wyjątek dla małych opakowań wewnętrznych

Data: 31.10.2026  
Zakres: wyłącznie kurs podstawowy ADR  
Baza: main po PR #725, bank 681 pytań; nowy ID: ADR-B-0682  
Kompetencja: ADR-B-09-K04 — strzałki kierunkowe

## Dlaczego wybrano tę lukę

Kompetencja miała cztery pytania, z których dotychczasowe sprawdzały głównie ustawienie opakowania i miejsce umieszczenia strzałek. Brakowało sprawdzenia, czy kursant rozpoznaje wyjątek z ADR 5.2.1.10.2(b), a nie zakłada automatycznie, że strzałki są wymagane dla każdego opakowania z cieczą.

## Dodane pytanie

- **ADR-B-0682** — opakowanie zewnętrzne zawiera opakowania wewnętrzne po 100 ml, a materiał chłonny może wchłonąć całą ciecz; kursant rozpoznaje wyjątek od obowiązku strzałek.
- Klucz: **B** — wyjątek działa, jeśli każde opakowanie wewnętrzne ma najwyżej 120 ml i materiał chłonny wystarcza do wchłonięcia całej cieczy.
- Explanation: **417 znaków, 4 zdania**; wyjaśnia oba łączne warunki wyjątku, wskazuje, co dzieje się po niespełnieniu warunków, i podaje podstawę ADR.
- Długości A/B/C: **142/136/107** znaków. Poprawna odpowiedź B nie jest ani najdłuższa, ani najkrótsza.
- Status: needs_review; niczego nie oznaczono jako verified.

## Podstawa i ograniczenia

- ADR 2025, **5.2.1.10.1** — wymaganie strzałek dla określonych opakowań, w tym opakowań kombinowanych z opakowaniami wewnętrznymi zawierającymi ciecze; strzałki umieszcza się na dwóch przeciwległych pionowych bokach.
- ADR 2025, **5.2.1.10.2(b)** — wyjątek dla opakowania zewnętrznego, gdy każde opakowanie wewnętrzne zawiera nie więcej niż 120 ml, a materiał chłonny wystarcza do wchłonięcia całej cieczy.
- Źródło prawa: ADR 2025 ogłoszony w Dz.U. 2025 poz. 642: https://dziennikustaw.gov.pl/DU/2025/642 .
- Porównanie treści ADR 2025: oficjalny tekst UNECE, ECE/TRANS/351: https://digitallibrary.un.org/record/4092124/files/E_ECE_TRANS_351-EN.pdf .

Dokładny polski tekst ustępu w Dz.U. nie został pobrany i porównany literalnie; pełne porównanie pytania A/B/C oraz niezależna recenzja specjalisty pozostają otwarte. Nie oznaczono pytania jako verified.

## Synchronizacja #646 — stan po dodaniu pytania

- Bank: **682** pytań ADR-B-0001–0682; wszystkie needs_review, 0 verified.
- Blob SHA: do uzupełnienia po zapisaniu banku.
- Rozkład A/B/C: **234/232/216**; „poprawna = jedyna najdłuższa”: **72/682 = 10,56%**, poniżej Quality Gate 18%.
- Zaktualizowano mapę kompetencji, lekcję i materiał instruktora B-09, snapshoty sequential/legal oraz ledger źródeł. Synchronizacja egzaminów 001–005 i pakietu recenzyjnego następuje w kolejnych commitach.
