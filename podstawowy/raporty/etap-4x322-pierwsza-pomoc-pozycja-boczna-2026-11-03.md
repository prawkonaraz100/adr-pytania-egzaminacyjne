# Etap 4x322 — pierwsza pomoc: pozycja boczna i kontrola oddechu

2026-11-03. Bazowy main `8643fc2e5db4ebf978f0618fd23aea83a1525a63`; gałąź `stage4x322-first-aid-scene-safety`.

- Dodano ADR-B-0748 do `ADR-B-05-K11`: ocena bezpieczeństwa udzielania pierwszej pomocy.
- Kompetencja wzrosła z 5 do 6 pytań; kompetencje teorii z mniej niż 6 pytaniami: **32** (3 praktyczne pominięte).
- Bank: 748 pytań (ADR-B-0001–0748), 748 `needs_review`, 0 `verified`; SHA `29d91dfb906ddb9c1cc075ab0803b0e2311f8fd5`.
- Moduł ADR-B-05: 86 pytań.
- Rozkład kluczy A/B/C: 252/268/228.
- „Poprawna odpowiedź jest jedyną najdłuższą”: **81/748 = 10,83%**; maksimum działu **14,61%**. Długości opcji ADR-B-0748: A=95, B=87, C=99; poprawna A nie jest najdłuższa.
- Explanation: 447 znaków, 4 zdania. Zakłada bezpieczne miejsce, prawidłowy oddech i brak podejrzenia urazu; zaleca pozycję boczną i monitorowanie. Nie utożsamia braku reakcji z zatrzymaniem krążenia.
- Podstawa programowa ADR: 8.2.2.3.2(e) — kurs podstawowy obejmuje pierwszą pomoc po wypadku. Szczegółowa procedura: ERC Guidelines 2025, First Aid (pozycja boczna u osoby nieprzytomnej, oddychającej prawidłowo, bez wskazań do CPR; monitorowanie oddechu). Status `needs_review`; pełne literalne porównanie i niezależna recenzja pozostają otwarte.
- Odświeżono klucze i warianty 001–005, snapshoty sequential/legal 748, ledger, manifesty, kolejki, rejestr specjalisty (748 unikalnych ID), coverage, lekcję B-05, README i testy regresji.

## Pytanie ADR-B-0748

Po wypadku ADR miejsce zdarzenia jest już bezpieczne. Poszkodowany nie reaguje, ale oddycha prawidłowo i nie ma oznak urazu. Co powinien zrobić kierowca, udzielając pierwszej pomocy?

A. Ułożyć go na boku, utrzymać drożność dróg oddechowych i kontrolować oddech do przyjazdu pomocy.

B. Rozpocząć uciskanie klatki piersiowej od razu, mimo że poszkodowany oddycha prawidłowo.

C. Pozostawić go na plecach bez nadzoru, bo prawidłowy oddech oznacza, że nie wymaga dalszej kontroli.

Jeśli poszkodowany nie reaguje, ale oddycha prawidłowo i nie ma podejrzenia urazu, ułóż go w pozycji bezpiecznej na boku. Dzięki temu łatwiej utrzymać drożność dróg oddechowych; do przyjazdu pomocy regularnie sprawdzaj oddech i reaguj, gdy się pogorszy. Uciskanie klatki piersiowej rozpoczyna się przy braku prawidłowego oddechu, a nie przy samym braku reakcji. Podstawa kursu: ADR 2025, 8.2.2.3.2(e); postępowanie: ERC Guidelines 2025, First Aid.

## Audyt A/B/C i źródła

- A — poprawna: przy obniżonej świadomości, prawidłowym oddechu i braku podejrzenia urazu zalecana jest pozycja boczna oraz dalsza kontrola oddechu.
- B — błędna: uciskanie klatki piersiowej nie jest wskazane, gdy poszkodowany oddycha prawidłowo.
- C — błędna: nieprzytomnej osoby nie należy pozostawiać bez nadzoru; trzeba monitorować drożność dróg oddechowych i oddech.
- ADR: Dz.U. 2025 poz. 642, 8.2.2.3.2(e) — https://eli.gov.pl/api/acts/DU/2025/642/text.pdf.
- Procedura: European Resuscitation Council Guidelines 2025, First Aid — https://www.erc.edu/media/i2vllpae/gl2025-12-faid-e.pdf.
- Nie oznaczono żadnego pytania jako `verified`.
