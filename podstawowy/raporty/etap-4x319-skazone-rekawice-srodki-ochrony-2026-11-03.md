# Etap 4x319 — skażone rękawice i środki ochrony

2026-11-03. Bazowy main `ced8074f5ce254b1e9c5631e31c0d54fea23725d`; gałąź `stage4x319-contaminated-clothing-protective-equipment`.

- Dodano ADR-B-0745 do `ADR-B-05-K08`: rozpoznanie skażonych rękawic użytych przy uszkodzonej przesyłce i bezpieczne postępowanie z nimi.
- Kompetencja wzrosła z 5 do 6 pytań; kompetencje teorii z mniej niż 6 pytaniami: **35** (3 praktyczne pominięte).
- Bank: **745** pytań (ADR-B-0001–0745), 745 `needs_review`, 0 `verified`; SHA `c53063274e59f9c2d45da3e0c5ef58ca2f1f496a`.
- Moduł ADR-B-05: **83** pytania.
- Rozkład kluczy A/B/C: 249/268/228.
- „Poprawna odpowiedź jest jedyną najdłuższą”: **81/745 = 10,87%**; maksimum działu **14,61%**. Długości wariantów ADR-B-0745: A=105, B=90, C=78; poprawna B jest najkrótsza.
- Explanation: 349 znaków, 4 zdania. Wyjaśnia, że rękawice po kontakcie z substancją trzeba traktować jako skażone nawet bez widocznej plamy; nie wolno ich ponownie zakładać ani przechowywać w kabinie. A myli brak widocznych śladów z brakiem skażenia, a C przenosi zagrożenie do kabiny.
- Podstawa: ADR 2025, 5.4.3.4 — zdjąć skażoną odzież i użyte skażone środki ochronne oraz zapewnić ich bezpieczne usunięcie. Status `needs_review`; pełne literalne porównanie i niezależna recenzja pozostają otwarte.
- Klucze i warianty egzaminów próbnych 001–005 zsynchronizowano z SHA banku; każdy ma 30 pozycji i aktualny `source_bank_head`.
- Dodano snapshoty sequential/legal dla ADR-B-0745; ledger i manifest pakietu zaktualizowane. Rejestr specjalisty: 745 unikalnych ID, bez duplikatów. Coverage i testy liczebności zaktualizowane.

## Pytanie ADR-B-0745

Po zakończeniu działań przy wycieku kierowca ma już czyste rękawice zapasowe. W kabinie leży para rękawic użytych przy uszkodzonej przesyłce. Które postępowanie jest właściwe przed powrotem do pojazdu?

A. Założyć użyte rękawice ponownie, jeśli wyglądają na suche; niewidoczne ślady nie muszą oznaczać skażenia.

B. Nie używać ich ponownie; odseparować skażone rękawice i zapewnić ich bezpieczne usunięcie.

C. Schować je do schowka kabiny, aby nie dotykały fotela ani dokumentów kierowcy.

Rękawice, które miały kontakt z uwolnioną substancją, traktuj jako skażone nawet wtedy, gdy nie widać na nich plamy. Nie zakładaj ich ponownie ani nie wkładaj do schowka; trzeba odseparować je i zapewnić bezpieczne usunięcie. Odpowiedź A myli brak widocznych śladów z brakiem zagrożenia, a C przenosi skażenie do kabiny. Podstawa: ADR 2025, 5.4.3.4.

## Audyt A/B/C i źródła

- A — błędna: brak widocznych śladów nie dowodzi, że użyte rękawice są czyste.
- B — poprawna: skażone środki ochronne należy zdjąć i bezpiecznie usunąć; nie używać ich ponownie.
- C — błędna: przechowywanie skażonych rękawic w kabinie może przenieść substancję na załogę i powierzchnie.
- Źródło: Dz.U. 2025 poz. 642, ADR 2025, 5.4.3.4 — https://eli.gov.pl/api/acts/DU/2025/642/text.pdf.
- Nie oznaczono żadnego pytania jako `verified`.
