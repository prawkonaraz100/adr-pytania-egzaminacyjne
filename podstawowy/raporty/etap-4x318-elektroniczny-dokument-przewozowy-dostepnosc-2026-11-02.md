# Etap 4x318 — elektroniczny dokument przewozowy i dostępność

2026-11-02. Gałąź `stage4x318-electronic-transport-doc-availability`; bank bazowy main: 743 pytania.

- ADR-B-0744 przypisano do `ADR-B-05-K07`: przekazanie dokumentów ratownikom. Kompetencja wzrosła z 5 do 6 pytań.
- Kompetencje teorii z mniej niż 6 pytaniami: **36** (3 praktyczne pominięte).
- Bank: **744** pytania (ADR-B-0001–0744), 744 `needs_review`, 0 `verified`; SHA `2c20fa651689bb224e88f2d52775207ad6d864eb`.
- Moduł ADR-B-05: **82** pytania.
- Rozkład prawidłowych opcji: A=249, B=267, C=228.
- „Poprawna odpowiedź jest jedyną najdłuższą”: **81/744 = 10,89%**; maksimum działu **14,61%**. Długości wariantów ADR-B-0744: A=112, B=112, C=119; poprawna A nie jest najdłuższa.
- Explanation: 393 znaki, 4 zdania. A opisuje wymaganą niezawodność i dostępność elektronicznych danych co najmniej równoważną papierowi; B błędnie zakłada, że sam numer UN zastępuje pełny dokument; C błędnie każe czekać na sieć, zamiast zapewnić dostęp podczas przewozu i służbom.
- Podstawa: ADR 2025, 5.4.0.2 oraz 5.4.3.4. Status `needs_review`; pełne literalne porównanie i niezależna recenzja specjalisty pozostają otwarte.
- Zweryfikowano synchronizację kluczy i wariantów egzaminów próbnych 001–005 z SHA banku; każdy ma 30 pozycji i `source_bank_head` równy SHA powyżej.
- Snapshot sequential i legal-review dla ADR-B-0744 odpowiadają dokładnie aktualnemu rekordowi banku. Rejestr specjalisty ma 744 unikalne wiersze, bez duplikatów. Manifest pakietu, kolejki prawne i coverage wskazują bank 744.

## Pytanie ADR-B-0744

Dokument przewozowy jest przechowywany wyłącznie w aplikacji, która pobiera go z internetu. Po wypadku w miejscu bez zasięgu ratownicy nie mogą go otworzyć. Jakie wymaganie ADR dotyczące takiego rozwiązania nie zostało spełnione?

A. Dostęp do wymaganych danych podczas przewozu musi być co najmniej tak niezawodny jak przy dokumencie papierowym.

B. Wystarczy podać ratownikom tylko numer UN z pamięci, a pełny dokument udostępnić dopiero po zakończeniu działań.

C. Pozostawić dokument wyłącznie w chmurze i poprosić ratowników, by poczekali na zasięg albo skontaktowali się z nadawcą.

Elektroniczny dokument jest dopuszczalny, ale wymagane dane muszą być dostępne podczas przewozu i równie wiarygodnie jak przy papierze. Jeśli brak zasięgu uniemożliwia otwarcie pliku, ratownicy nie otrzymają informacji potrzebnych do rozpoznania ładunku. Sam numer UN podany z pamięci nie zastępuje całego dokumentu, a oczekiwanie na sieć opóźnia dostęp. Podstawa: ADR 2025, 5.4.0.2 i 5.4.3.4.

## Audyt A/B/C i źródła

- A — poprawna: ADR dopuszcza EDP/EDI, gdy zachowana jest co najmniej równoważna dostępność i wartość dowodowa danych względem papieru.
- B — błędna: sam numer UN nie zastępuje kompletu danych dokumentu przewozowego.
- C — błędna: oczekiwanie na zasięg nie zapewnia dostępności danych podczas przewozu ani szybkiego dostępu służbom ratowniczym.
- Źródło: Dz.U. 2025 poz. 642, ADR 2025, 5.4.0.2 i 5.4.3.4 — https://eli.gov.pl/api/acts/DU/2025/642/text.pdf.
- Żadnego pytania nie oznaczono jako `verified`.
