# Kontrola potwierdzonych zbieżności — korekta bez usuwania historii (23.10.2026)

W raporcie `review/batches/semantic-001-502.md` rozpoznano trzy pary o zbliżonej treści merytorycznej. W nowej partii zachowano **wszystkie identyfikatory**, nie usuwano pytań ani dawnych wpisów historycznych; zmieniono tylko późniejszy rekord i jego bezpośrednio powiązane migawki w istniejących rejestrach. W repo pozostaje 506 pytań, wszystkie `needs_review`.

| Para | Przeredagowano | Uzasadnienie |
|---|---|---|
| 0009 / 0241 | 0241 | Zastąpiono powtórzony nakaz czyszczenia (0009) odrębnym warunkiem dokumentacyjnym dla przejazdu do miejsca czyszczenia. |
| 0204 / 0278 | 0278 | Zamiast powtórzenia pytania 0204 o osobę przekazującą certyfikat testuje odrębne wymaganie przy zmianie EDI na dokument papierowy. |
| 0025 / 0324 | 0324 | Zamiast ogólnego pytania o wybór tabeli (0025) sprawdza konkretną komórkę tabeli i znaczenie oznaczenia złożonego. |

## Kontrola źródeł i ograniczenia

- `0241`: ADR 2025 5.4.1.1.6.3(b) w związku z 7.5.8.1 — wpis dokumentowy dla pustego nieoczyszczonego kontenera kierowanego do najbliższego miejsca czyszczenia.
- `0278`: ADR 2025 5.4.2 z przywołaniem IMDG 5.4.2.4 — przy zmianie certyfikatu EDI na papier informacja o elektronicznym oryginale i identyfikacja podpisującego.
- `0324`: ADR 2025 tabela 7.5.2.1 — szczególny układ nalepek 5.2 + 1 oraz 5.2; zgodność z tabelą nie znosi innych obowiązków.
- Odczytano właściwe ustępy wersji ADR 2025 UNECE/EN i pomocniczą reprodukcję; źródłem prawa pozostaje Dz.U. 2025 poz. 642 wraz ze sprostowaniem poz. 1575. Pełne **polskie urzędowe** porównanie każdego wariantu i podpis eksperta **nie zostały wykonane**.
- Zaktualizowano oddzielnie trzy rekordy w `review/sequential/*.json` i `review/legal-clauses/*.json`; wszystkie `official_polish_full_text_comparison=pending`, `independent_specialist_approval=pending`, `final_verification_status=needs_review`.
- Nie zmieniono kluczy poza zachowaniem dotychczasowej litery A dla przeredagowanych pozycji.
