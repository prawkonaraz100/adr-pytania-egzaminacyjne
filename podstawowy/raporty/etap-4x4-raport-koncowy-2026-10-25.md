# Raport końcowy ETAPU 4x4 — spójność banku i języka kursanta

- Data: 25.10.2026.
- Zakres: kurs podstawowy ADR, wszystkie 609 pytań w 13 działach.
- PR-y partii: B-01–04, B-05–08, B-09–12 oraz B-13; raporty szczegółowe są podlinkowane w `podstawowy/README.md`.

## Co objęto kontrolą

Dla każdej partii porównano treść pytań, odpowiedzi A/B/C, klucz i explanation z lekcją właściwego działu. Kontrola skupiała się na liczbach, progach, terminach, wymiarach/konfiguracjach oznakowania, nazwach dokumentów, skrótach, numerach punktów ADR i warunkach wyjątków. Uzupełnienia do lekcji opisano prostym językiem kursanta i powiązano z konkretnymi punktami ADR. Dystraktory sprawdzano pod kątem dwuznaczności, oczywistego absurdu i wskazówek wynikających z długości odpowiedzi.

## Poprawka końcowa PR #318

- CI wykryło niezsynchronizowany wariant próbny 003 i klucz: opcje `ADR-B-0039` w wariancie oraz explanation w kluczu nie odpowiadały bankowi. Zsynchronizowano je z rekordem źródłowym; poprawna odpowiedź nadal B.
- CI wykryło przekroczenie progu „poprawna odpowiedź jest najkrótsza” w B-13: 21/47. W pięciu pytaniach (`ADR-B-0037`, `0038`, `0087`, `0088`, `0145`) skrócono wiarygodne, ale błędne dystraktory, aby długość nie zdradzała klucza. Nie zmieniono kluczy ani sensu merytorycznego.
- Odświeżono odpowiednie snapshoty w `review/sequential` i `review/legal-clauses`, zachowując statusy audytu.
- Szczegóły i odnośniki do przebiegów CI: [PR #318](https://github.com/prawkonaraz100/adr-pytania-egzaminacyjne/pull/318).

## Wyniki po poprawkach

- Liczba pytań: 609; duplikaty ID: 0.
- Wskaźnik „poprawna = jedyna najdłuższa”: 83/609 = 13.63% (limit 18%).
- B-13: wskaźnik „poprawna = najkrótsza”: 16/47 = 34.04% (limit 38%).
- Explanation: 300–457 znaków; poniżej 200: 0.
- Status: 609 `needs_review`, 0 `verified`.
- Wariant próbny 003 ma 30 pytań, klucz odpowiedzi zachowuje spójność z bankiem, a jego publikacja nadal nie jest autoryzowana.

## Ograniczenia i dalsze wymagania

Kontrola spójności i języka nie zastępuje niezależnej weryfikacji prawnej przez specjalistę ADR. Nie stwierdza się pełnej zgodności z tekstem urzędowym, jeśli nie została oddzielnie potwierdzona. Żadne pytanie nie zostało oznaczone jako `verified`; nie zmieniano statusów recenzji. Zakres obejmuje wyłącznie kurs podstawowy — nie rozpoczęto kursu cystern ani innej specjalizacji.

Status CI należy uznać za PASS dopiero na podstawie zielonych obu wymaganych jobów dla końcowego commita PR #318.
